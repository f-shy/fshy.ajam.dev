"""raw_issues.py: one issue for each topic whose records research changed with no row of the change ledger.

The issue is titled "[raw] <topic>" and has the label raw. The research repository reads these issues and makes each
one its own work: it writes the missing ledger rows, and a later publish closes the gaps (publog.py). This script is
the only writer of these issues. The workflow raw-issues runs it after each push to main and once a day, so an issue
never says more or less than the data:

  a topic with gaps and no open issue      it opens an issue, or reopens the closed one
  a topic with gaps and an open issue      it writes the body again when the list changed
  an open issue of a topic with no gap     it closes the issue with a comment
  more than one open issue of a topic      it closes all but the oldest

  python publish/raw_issues.py --dry-run       print what it would do, and each body
  python publish/raw_issues.py --sync          do it: needs gh, and GH_TOKEN with issues: write
  python publish/raw_issues.py --body TOPIC    print the body of one topic

Each title and body passes the commit-msg hook and the leak rules before it is sent; a refused text stops the run.

Standard library only.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile

import publog

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ORIGIN = os.environ.get("FSHY_ORIGIN", "https://fshy.ajam.dev").rstrip("/")
LABEL = "raw"
MARK = "<!-- fshy:raw-gaps topic=%s -->"
LIST_MAX = 400  # the records that one body lists; the rest are a count and the command that lists them


def title(topic):
    return "[%s] %s" % (LABEL, topic)


def body(topic, gs):
    """The issue text of one topic, from its gaps (publog.gaps)."""
    by = {}
    for g in gs:
        k = (g["when"][:10], g["source"][:7])
        by.setdefault(k, {"added": 0, "rechecked": 0})[g["kind"]] += 1
    rows = "\n".join("| %s | %s | %d | %d |" % (d, s, n["added"], n["rechecked"]) for (d, s), n in sorted(by.items(), reverse=True))
    word = {"added": "added", "rechecked": "re-checked"}
    items = "\n".join("- [`%s`](%s/r/%s) %s, publish %s" % (g["rid"], ORIGIN, g["rid"], word[g["kind"]], g["when"][:10])
                      for g in gs[:LIST_MAX])
    more = ("\n\nThis list shows %d of %d records. `python publish/publog.py --gaps` lists all of them."
            % (LIST_MAX, len(gs))) if len(gs) > LIST_MAX else ""
    return (
        MARK % topic + "\n"
        "Research changed %d record%s of the topic `%s`, but the change ledger has no row for the change. The Changes "
        "page and the feed show only the changes that the ledger records, so these changes are not visible there.\n\n"
        "To close this issue, write the ledger rows of these changes in the research repository, then publish. The check "
        "reads the data after each push to main and once a day. It closes this issue when each record below has a "
        "ledger row, or is removed.\n\n"
        "| publish | source commit | added | re-checked |\n| --- | --- | --- | --- |\n%s\n\n"
        "<details><summary>%d records</summary>\n\n%s%s\n\n</details>\n\n"
        "The check writes this text again after each publish, so an edit by hand does not stay.\n"
    ) % (len(gs), "" if len(gs) == 1 else "s", topic, rows, len(gs), items, more)


def refused(text):
    """The reason when the commit-msg hook or the leak rules refuse the text, else None."""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(text)
        path = f.name
    try:
        for cmd in (["sh", os.path.join(ROOT, ".githooks", "commit-msg"), path],
                    [sys.executable, os.path.join(HERE, "build.py"), "--scan", path]):
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode:
                return (r.stderr or r.stdout).strip()[:400]
        return None
    finally:
        os.unlink(path)


def gh(*args, data=None):
    r = subprocess.run(["gh"] + list(args), input=data, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("raw_issues: gh %s: %s" % (" ".join(args[:2]), r.stderr.strip()[:300]))
    return r.stdout


def plan(gaps, issues):
    """[(action, topic, number, body)] that make the issues match the gaps. issues: [{number, title, state, body}]."""
    by = {}
    for i in sorted(issues, key=lambda i: i["number"]):
        if i["title"].startswith("[%s] " % LABEL):
            by.setdefault(i["title"][len(LABEL) + 3:], []).append(i)
    acts = []
    for topic in sorted(set(gaps) | set(by)):
        have = by.get(topic, [])
        live = [i for i in have if i["state"].lower() == "open"]
        if topic in gaps:
            text = body(topic, gaps[topic])
            if live:
                keep = live[0]
                if keep["body"].strip() != text.strip():
                    acts.append(("edit", topic, keep["number"], text))
                acts += [("close-duplicate", topic, i["number"], None) for i in live[1:]]
            elif have:
                acts.append(("reopen", topic, have[-1]["number"], text))
            else:
                acts.append(("create", topic, None, text))
        else:
            acts += [("close", topic, i["number"], None) for i in live]
    return acts


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--sync", action="store_true")
    g.add_argument("--body", metavar="TOPIC")
    a = ap.parse_args(argv)
    log = publog.entries(ROOT)
    if not log:
        print("raw_issues: no publish log (no git history of data/); nothing to do", file=sys.stderr)
        return 2
    gaps = publog.gaps(log)
    if a.body:
        print(body(a.body, gaps.get(a.body, [])))
        return 0
    for topic in gaps:
        why = refused(title(topic) + "\n\n" + body(topic, gaps[topic]))
        if why:
            print("raw_issues: the text of %s is refused: %s" % (title(topic), why), file=sys.stderr)
            return 1
    repo = os.environ.get("GITHUB_REPOSITORY", "f-shy/fshy.ajam.dev")
    issues = []
    if a.sync or os.environ.get("GH_TOKEN"):
        issues = json.loads(gh("issue", "list", "--repo", repo, "--label", LABEL, "--state", "all", "--limit", "500",
                               "--json", "number,title,state,body"))
    acts = plan(gaps, issues)
    source = log[0]["source"][:7]
    print("raw_issues: %d topic(s) with gaps: %s" % (len(gaps), ", ".join("%s %d" % (t, len(v)) for t, v in gaps.items()) or "none"))
    for act, topic, number, text in acts:
        print("%s %s%s" % (act, title(topic), (" #%d" % number) if number else ""))
        if a.dry_run:
            if text:
                print(text)
            continue
        if act in ("create", "reopen", "edit"):
            with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
                f.write(text)
            try:
                if act == "create":
                    gh("label", "create", LABEL, "--repo", repo, "--force", "--color", "5319e7",
                       "--description", "research changes with no ledger row, for the research repository")
                    gh("issue", "create", "--repo", repo, "--title", title(topic), "--label", LABEL, "--body-file", f.name)
                else:
                    if act == "reopen":
                        gh("issue", "reopen", str(number), "--repo", repo)
                    gh("issue", "edit", str(number), "--repo", repo, "--body-file", f.name)
            finally:
                os.unlink(f.name)
        elif act == "close":
            gh("issue", "close", str(number), "--repo", repo, "--reason", "completed", "--comment",
               "Closed by the check: each record of this list has a ledger row now, or is removed (publish at source commit %s)."
               % source)
        elif act == "close-duplicate":
            gh("issue", "close", str(number), "--repo", repo, "--reason", "not planned", "--comment",
               "Closed by the check: an older open issue holds the list of this topic.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
