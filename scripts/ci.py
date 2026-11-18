#!/usr/bin/env python3
"""Read the state of the GitHub Actions runs of this repository, with no token and no gh.

The reads go to the GitHub REST API through forge.web.pkgforge.dev (its guide is
https://forge.web.pkgforge.dev/llms.txt). Use this tool, not a notification or an MCP
event alone, to know how a run, a job or a deploy ended.

    python scripts/ci.py runs   [--sha SHA | --branch BRANCH] [--workflow FILE] [--event EVENT]
    python scripts/ci.py run    RUN_ID
    python scripts/ci.py pr     NUMBER
    python scripts/ci.py wait   RUN_ID | --sha SHA [--workflow FILE] [--event EVENT] [--timeout S]

Exit codes: 0 every run read is completed with success (or skipped), 1 a run failed or
was cancelled, 2 usage or a request that the service refused, 3 a run is not completed
(for wait: the timeout passed).

Standard library only, Python 3.9 or later.
"""

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

FORGE = "https://forge.web.pkgforge.dev/github"
REPO = "f-shy/fshy.ajam.dev"
# forge stores an Actions answer for 60 s, so a poll faster than this reads the same answer
POLL_S = 60
GOOD = {"success", "skipped", "neutral"}


class Refused(Exception):
    pass


def get(path, query=None, tries=6):
    """GET one GitHub REST path through forge. Returns (body, cache) on a 200."""
    url = f"{FORGE}/{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    delay = 5
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"accept": "application/vnd.github+json",
                                                   "user-agent": "fshy-ci-status"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r), r.headers.get("x-web-cache", "")
        except urllib.error.HTTPError as e:
            reason = ""
            try:
                reason = json.load(e).get("reason", "")
            except Exception:
                pass
            retry_after = e.headers.get("retry-after")
            # the retry rules of forge's pipeline contract
            if e.code == 429 or (e.code == 503 and reason == "disabled"):
                wait = int(retry_after) if retry_after and retry_after.isdigit() else 60
            elif e.code in (500, 502, 504) or (e.code == 503 and reason in ("deadline", "budget")):
                wait = delay
                delay = min(delay * 2, 120)
            else:
                raise Refused(f"{e.code} {reason or e.reason}: {url}")
            print(f"# {e.code} {reason}: retry in {wait} s", file=sys.stderr)
            time.sleep(wait)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"# {e}: retry in {delay} s", file=sys.stderr)
            time.sleep(delay)
            delay = min(delay * 2, 120)
    raise Refused(f"no answer after {tries} tries: {url}")


def fresh(path, query=None):
    """A read that is not a stale stored answer, when forge can give one."""
    body, cache = get(path, query)
    if cache == "stale":
        # forge reads the path again after a stale answer, so a second read is fresh
        time.sleep(5)
        body, cache = get(path, query)
    return body


def list_runs(repo, sha=None, branch=None, workflow=None, event=None):
    q = {"per_page": 20}
    if sha:
        q["head_sha"] = sha
    if branch:
        q["branch"] = branch
    if event:
        q["event"] = event
    base = f"repos/{repo}/actions/workflows/{workflow}/runs" if workflow else f"repos/{repo}/actions/runs"
    return fresh(base, q).get("workflow_runs", [])


def jobs(repo, run_id):
    return fresh(f"repos/{repo}/actions/runs/{run_id}/jobs", {"per_page": 50}).get("jobs", [])


def show(repo, run, with_jobs=True):
    print(f"run {run['id']} {run['name']} event={run['event']} sha={run['head_sha'][:12]} "
          f"branch={run['head_branch']} attempt={run.get('run_attempt', 1)} "
          f"status={run['status']} conclusion={run.get('conclusion') or '-'}")
    print(f"  {run['html_url']}")
    if with_jobs:
        for j in jobs(repo, run["id"]):
            print(f"  job {j['name']}: status={j['status']} conclusion={j.get('conclusion') or '-'}")
            for s in j.get("steps") or []:
                if s.get("conclusion") not in (None, "success", "skipped"):
                    print(f"    step {s['number']} {s['name']}: {s['conclusion']}")


def verdict(runs):
    if not runs:
        return 3
    if any(r["status"] != "completed" for r in runs):
        return 3
    return 0 if all(r.get("conclusion") in GOOD for r in runs) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=REPO)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("runs", help="the runs of a commit or a branch, with their jobs")
    p.add_argument("--sha")
    p.add_argument("--branch")
    p.add_argument("--workflow", help="a workflow file name, for example build.yml")
    p.add_argument("--event", help="push, pull_request, workflow_dispatch, schedule")
    p = sub.add_parser("run", help="one run, with its jobs")
    p.add_argument("run_id", type=int)
    p = sub.add_parser("pr", help="the runs of the head commit of a pull request")
    p.add_argument("number", type=int)
    p = sub.add_parser("wait", help="poll until each run is completed")
    p.add_argument("run_id", type=int, nargs="?")
    p.add_argument("--sha")
    p.add_argument("--workflow")
    p.add_argument("--event")
    p.add_argument("--timeout", type=int, default=3600, help="seconds, default 3600")
    a = ap.parse_args()

    try:
        if a.cmd == "runs":
            if not (a.sha or a.branch):
                ap.error("runs needs --sha or --branch")
            runs = list_runs(a.repo, a.sha, a.branch, a.workflow, a.event)
        elif a.cmd == "run":
            runs = [fresh(f"repos/{a.repo}/actions/runs/{a.run_id}")]
        elif a.cmd == "pr":
            pr = fresh(f"repos/{a.repo}/pulls/{a.number}")
            sha = pr["head"]["sha"]
            print(f"pr {a.number} state={pr['state']} merged={pr.get('merged')} head={sha[:12]}")
            runs = list_runs(a.repo, sha=sha)
            # each workflow and event keeps only its newest attempt
            newest = {}
            for r in runs:
                newest.setdefault((r["workflow_id"], r["event"]), r)
            runs = list(newest.values())
        else:
            if not (a.run_id or a.sha):
                ap.error("wait needs RUN_ID or --sha")
            end = time.time() + a.timeout
            while True:
                if a.run_id:
                    runs = [fresh(f"repos/{a.repo}/actions/runs/{a.run_id}")]
                else:
                    runs = list_runs(a.repo, sha=a.sha, workflow=a.workflow, event=a.event)
                code = verdict(runs)
                if code != 3 or time.time() >= end:
                    break
                states = ", ".join(f"{r['id']}={r['status']}" for r in runs) or "no run yet"
                print(f"# {time.strftime('%H:%M:%S')} {states}", file=sys.stderr, flush=True)
                time.sleep(POLL_S)
    except Refused as e:
        print(f"refused: {e}", file=sys.stderr)
        return 2

    for r in runs:
        show(a.repo, r)
    if not runs:
        print("no run")
    return verdict(runs)


if __name__ == "__main__":
    sys.exit(main())
