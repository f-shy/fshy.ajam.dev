"""publog.py: the publish log of data/, read from the git history of this repository.

A publish is a commit that changes data/meta.json. Only publish/export.py writes data/, so each such commit is one
export. For each publish, the log gives:

  added      the records that the publish added
  removed    the records that the publish removed
  rechecked  the records that research checked again: a new verified_at, or a changed evidence list
  amended    the other changed records that got a ledger row: research changed a value with no new check
  ledger     the records that got a new or changed row of the change ledger (data/tables/ledger.jsonl)

A change of the text alone (a new render, a prose pass) is not a re-check, so it is in no list.

A gap is a record that research added or re-checked with no ledger row in the same publish. The change pages and the
feed show only what the ledger records, so a gap is a change that the public cannot see. A later publish that gives
the record a ledger row, or removes the record, closes its gap. publish/raw_issues.py keeps one issue open for each
topic with gaps.

  python publish/publog.py                 the publishes, newest first, as JSON
  python publish/publog.py --gaps          the open gaps, by topic, as JSON

The log is empty when the data is not data/ of a git checkout. It starts at the first publish whose parent commit has
data/meta.json, so the first export, which added every record, is not in it, and a shallow clone gives a short log.
When the data/ of the working tree differs from HEAD, that export is the first entry, with no commit.

Standard library only.
"""

import argparse
import collections
import datetime
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
META = "data/meta.json"
RECORDS = "data/records/"
LEDGER = "data/tables/ledger.jsonl"
ZERO = "0" * 40
RECHECK = ("verified_at", "evidence")  # a change of one of these keys is a re-check by research


class GitError(Exception):
    pass


def git(repo, *args, data=None):
    try:
        r = subprocess.run(["git", "-C", repo] + list(args), input=data, capture_output=True, timeout=300)
    except (OSError, subprocess.SubprocessError) as e:
        raise GitError(str(e))
    if r.returncode:
        raise GitError("git %s: %s" % (" ".join(args[:2]), r.stderr.decode("utf-8", "replace").strip()[:200]))
    return r.stdout


def has(repo, rev, path):
    try:
        git(repo, "cat-file", "-e", "%s:%s" % (rev, path))
        return True
    except GitError:
        return False


def blobs(repo, shas):
    """{sha: bytes} of the blobs, read by one git cat-file --batch."""
    shas = sorted(set(shas))
    if not shas:
        return {}
    out = git(repo, "cat-file", "--batch", data=("\n".join(shas) + "\n").encode())
    got, i = {}, 0
    for sha in shas:
        j = out.index(b"\n", i)
        head = out[i:j].split()
        if len(head) < 3 or head[1] == b"missing":
            raise GitError("blob %s is missing" % sha)
        n = int(head[2])
        got[sha] = out[j + 1:j + 1 + n]
        i = j + 1 + n + 1
    return got


def rid_of(path):
    return path[len(RECORDS):-len(".json")]


def entry(repo, old, new, when):
    """One publish: the change of data/ from the commit old to the commit new, or to the working tree when new is None."""
    span = [old] if new is None else [old, new]
    raw = git(repo, "diff", "--raw", "--no-renames", "--no-abbrev", "-z", *span, "--", RECORDS).split(b"\0")
    added, removed, changed = set(), set(), []
    i = 0
    while i + 1 < len(raw):
        head, path = raw[i].decode(), raw[i + 1].decode()
        i += 2
        if not path.endswith(".json"):
            continue
        _, _, a, b, status = head.split()
        if status == "A":
            added.add(rid_of(path))
        elif status == "D":
            removed.add(rid_of(path))
        else:
            changed.append((path, a, b))
    if new is None:  # a new record file of the working tree is untracked, so git diff does not list it
        for p in git(repo, "ls-files", "-z", "--others", "--exclude-standard", "--", RECORDS).split(b"\0"):
            if p.endswith(b".json"):
                added.add(rid_of(p.decode()))
    got = blobs(repo, [a for _, a, _ in changed] + [b for _, _, b in changed if b != ZERO])
    rechecked = set()
    for path, a, b in changed:
        before = json.loads(got[a])
        if b == ZERO:
            with open(os.path.join(repo, path), encoding="utf-8") as f:
                after = json.load(f)
        else:
            after = json.loads(got[b])
        if any(before.get(k) != after.get(k) for k in RECHECK):
            rechecked.add(rid_of(path))
    ledger = set()
    for line in git(repo, "diff", "-U0", "--no-color", *span, "--", LEDGER).decode("utf-8").splitlines():
        if line.startswith("+{"):
            ledger.add(json.loads(line[1:])["rid"])
    if new is None:
        with open(os.path.join(repo, META), encoding="utf-8") as f:
            meta = json.load(f)
    else:
        meta = json.loads(git(repo, "show", "%s:%s" % (new, META)))
    amended = {rid_of(p) for p, _, _ in changed} & ledger - rechecked
    return {"commit": new or "", "when": when or "%sT00:00:00Z" % meta.get("as_of", ""), "as_of": meta.get("as_of") or "",
            "source": meta.get("source_commit") or "", "added": sorted(added), "removed": sorted(removed),
            "rechecked": sorted(rechecked - added), "amended": sorted(amended - added), "ledger": sorted(ledger)}


def entries(repo=ROOT, data=None, limit=None):
    """The publishes, newest first; at most limit of them. [] when data is not data/ of a git checkout."""
    data = data or os.path.join(repo, "data")
    if os.path.realpath(data) != os.path.realpath(os.path.join(repo, "data")):
        return []
    try:
        if git(repo, "rev-parse", "--is-inside-work-tree").strip() != b"true" or not has(repo, "HEAD", META):
            return []
        out = []
        if git(repo, "status", "--porcelain", "--", "data").strip():
            out.append(entry(repo, "HEAD", None, None))
        log = git(repo, "log", "--format=%H %ct", "--", META).decode().split("\n")
        for line in log:
            if not line.strip() or (limit and len(out) >= limit):
                continue
            sha, ts = line.split()
            # in UTC: the time zone of a commit names the place of its author
            when = datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            if not has(repo, sha + "^", META):
                break
            out.append(entry(repo, sha + "^", sha, when))
        return out[:limit] if limit else out
    except GitError as e:
        print("publog: %s; the change pages get no publish log" % e, file=sys.stderr)
        return []


def gaps(log):
    """{topic: [{rid, kind, when, source}]}: the records that research added or re-checked with no ledger row, and
    that no later publish gave a ledger row or removed. log is newest first, as entries() gives it."""
    open_ = {}
    for p in reversed(log):
        for rid in set(p["ledger"]) | set(p["removed"]):
            open_.pop(rid, None)
        led = set(p["ledger"])
        for kind in ("added", "rechecked"):
            for rid in p[kind]:
                if rid not in led:
                    open_[rid] = {"rid": rid, "kind": kind, "when": p["when"], "source": p["source"]}
    by = collections.defaultdict(list)
    for rid in sorted(open_):
        by[rid.split("/", 1)[0]].append(open_[rid])
    return dict(sorted(by.items()))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--gaps", action="store_true", help="print the open gaps by topic")
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args(argv)
    log = entries(ROOT, limit=None if a.gaps else a.limit)
    print(json.dumps(gaps(log) if a.gaps else log, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
