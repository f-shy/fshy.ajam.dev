"""raw_issues.py: the issues titled "[raw] ..." that ask the research repository for work, from the data.

Two kinds of check write them:

  gaps        "[raw] <topic>": the records of the topic that research added or checked again with no row of the change
              ledger (publog.py). A later publish that gives each one a ledger row closes it.
  coverage    "[raw] <topic>: <check>", from the store and rules/coverage.json:
                stale records    a share of the hosted records of the topic is past its stale date
                few records      the topic has fewer hosted records than the minimum
                unknown values   the hosted records of the topic have many values that research did not establish
                no <kind>        a kind of resource that the catalogue does not cover, in the topic that would hold it

Each issue has the label raw and a first line <!-- fshy:raw-... -->. The research repository reads these issues and
makes each one its own work. This script is the only writer of them, and it changes only an issue with that first
line. The workflow raw-issues runs it after each push to main and once a day, so an issue never says more or less
than the data:

  a check that holds, with no open issue      it opens an issue, or reopens the closed one
  a check that holds, with an open issue      it writes the body again when the text changed
  an open issue whose check no longer holds   it closes the issue with a comment
  more than one open issue of one title       it closes all but the oldest

  python publish/raw_issues.py --dry-run           print what it would do, and each body
  python publish/raw_issues.py --sync              do it: needs gh, and GH_TOKEN with issues: write
  python publish/raw_issues.py --body TITLE        print the body of one issue

The coverage checks read the store that python publish/build.py --check writes (--db gives another one)
and the date of today in UTC (--today). Each title and body passes the commit-msg hook and the leak rules before it
is sent; a refused text stops the run.

Standard library only.
"""

import argparse
import datetime
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile

import publog

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ORIGIN = os.environ.get("FSHY_ORIGIN", "https://fshy.ajam.dev").rstrip("/")
LABEL = "raw"
OURS = "<!-- fshy:raw-"  # the first line of every issue that this script writes
LIST_MAX = 400  # the records that one body lists; the rest are a count and the command that lists them
RULES = os.path.join(HERE, "rules", "coverage.json")
TOPICS = [t["id"] for t in json.load(open(os.path.join(HERE, "rules", "topics.json"), encoding="utf-8"))["topics"]]


def title(topic, check=None):
    return "[%s] %s%s" % (LABEL, topic, (": " + check) if check else "")


def link(rid):
    return "[`%s`](%s/r/%s)" % (rid, ORIGIN, rid)


def listing(lines, total, where):
    more = ("\n\nThis list shows %d of %d records. %s lists all of them." % (LIST_MAX, total, where)) if total > LIST_MAX else ""
    return "<details><summary>%d records</summary>\n\n%s%s\n\n</details>" % (total, "\n".join(lines[:LIST_MAX]), more)


FOOT = "The check writes this text again after each publish and once a day, so an edit by hand does not stay.\n"


# ------------------------------------------------------------------ gaps
def gap_body(topic, gs):
    """The issue text of the gaps of one topic (publog.gaps)."""
    by = {}
    for g in gs:
        k = (g["when"][:10], g["source"][:7])
        by.setdefault(k, {"added": 0, "rechecked": 0})[g["kind"]] += 1
    rows = "\n".join("| %s | %s | %d | %d |" % (d, s, n["added"], n["rechecked"]) for (d, s), n in sorted(by.items(), reverse=True))
    word = {"added": "added", "rechecked": "re-checked"}
    lines = ["- %s %s, publish %s" % (link(g["rid"]), word[g["kind"]], g["when"][:10]) for g in gs]
    return (
        "<!-- fshy:raw-gaps topic=%s -->\n"
        "Research changed %d record%s of the topic `%s`, but the change ledger has no row for the change. The Changes "
        "page and the feed show only the changes that the ledger records, so these changes are not visible there.\n\n"
        "To close this issue, write the ledger rows of these changes in the research repository, then publish. The check "
        "reads the data after each push to main and once a day. It closes this issue when each record below has a "
        "ledger row, or is removed.\n\n"
        "| publish | source commit | added | re-checked |\n| --- | --- | --- | --- |\n%s\n\n%s\n\n%s"
    ) % (topic, len(gs), "" if len(gs) == 1 else "s", topic, rows, listing(lines, len(gs), "`python publish/publog.py --gaps`"), FOOT)


def gap_issues(gaps):
    return {title(t): gap_body(t, gs) for t, gs in gaps.items()}


# ------------------------------------------------------------------ coverage
def coverage_issues(db, today, rules):
    """{title: body} of the coverage checks that hold on the store db at the date today (YYYY-MM-DD)."""
    out = {}
    q = db.execute
    for t in TOPICS:
        hosted = q("SELECT count(*) FROM record WHERE topic=? AND self_hosted=0", (t,)).fetchone()[0]
        if not hosted:
            out[title(t, "no records")] = (
                "<!-- fshy:raw-coverage topic=%s check=no-records -->\n"
                "The topic `%s` is in the topic list of the site, but it has no hosted record. Research it, or remove the "
                "topic from the list.\n\nThe check closes this issue when the topic has a hosted record.\n\n%s") % (t, t, FOOT)
            continue
        stale = q("SELECT rid, stale_on FROM record WHERE topic=? AND self_hosted=0 AND stale_on < ? ORDER BY stale_on, rid",
                  (t, today)).fetchall()
        if len(stale) >= rules["stale_share"] * hosted:
            lines = ["- %s stale since %s" % (link(r), s) for r, s in stale]
            out[title(t, "stale records")] = (
                "<!-- fshy:raw-coverage topic=%s check=stale-records -->\n"
                "%d of the %d hosted records of the topic `%s` (%d%%) are past their stale date on %s. A record past "
                "its stale date has a check that is older than its own budget, so its values can be wrong now.\n\n"
                "To close this issue, check these records again in the research repository, then publish. The check "
                "closes this issue when fewer than %d%% of the hosted records of the topic are past their stale date. "
                "The oldest come first.\n\n%s\n\n%s") % (
                t, len(stale), hosted, t, round(100 * len(stale) / hosted), today, round(100 * rules["stale_share"]),
                listing(lines, len(stale), "%s/api/v1/worklist/stale" % ORIGIN), FOOT)
        if hosted < rules["min_hosted"]:
            usable = q("SELECT count(*) FROM record WHERE topic=? AND self_hosted=0 AND grp='usable'", (t,)).fetchone()[0]
            cats = q("SELECT category, count(*) FROM record WHERE topic=? AND self_hosted=0 GROUP BY 1 ORDER BY 2 DESC, 1",
                     (t,)).fetchall()
            out[title(t, "few records")] = (
                "<!-- fshy:raw-coverage topic=%s check=few-records -->\n"
                "The topic `%s` has %d hosted records, and %d of them are usable. The minimum for a topic is %d hosted "
                "records, so the topic probably leaves out offers of its kind.\n\n"
                "To close this issue, find and research more providers of this topic in the research repository, then "
                "publish. The check closes this issue when the topic has %d hosted records.\n\n"
                "| category | records |\n| --- | --- |\n%s\n\n%s") % (
                t, t, hosted, usable, rules["min_hosted"], rules["min_hosted"],
                "\n".join("| %s | %d |" % ((c or "not stated").replace("|", "/"), n) for c, n in cats), FOOT)
        cls = rules["gap_classes"]
        marks = ",".join("?" * len(cls))
        n_gap = q("SELECT count(*) FROM unknown u JOIN record r ON r.rid=u.rid WHERE r.topic=? AND r.self_hosted=0 AND u.class IN (%s)"
                  % marks, (t, *cls)).fetchone()[0]
        if n_gap >= rules["gap_mean"] * hosted:
            by_cls = q("SELECT u.class, count(*) FROM unknown u JOIN record r ON r.rid=u.rid WHERE r.topic=? AND r.self_hosted=0 "
                       "AND u.class IN (%s) GROUP BY 1 ORDER BY 2 DESC, 1" % marks, (t, *cls)).fetchall()
            by_path = q("SELECT u.path, count(*) FROM unknown u JOIN record r ON r.rid=u.rid WHERE r.topic=? AND r.self_hosted=0 "
                        "AND u.class IN (%s) GROUP BY 1 ORDER BY 2 DESC, 1 LIMIT 15" % marks, (t, *cls)).fetchall()
            out[title(t, "unknown values")] = (
                "<!-- fshy:raw-coverage topic=%s check=unknown-values -->\n"
                "The %d hosted records of the topic `%s` have %d values that research did not establish: %.1f for each "
                "record. The maximum mean is %.1f, so many records of this topic cannot answer a filter or a comparison.\n\n"
                "To close this issue, establish these values from first-party sources in the research repository, then "
                "publish. The check closes this issue when the mean is below %.1f.\n\n"
                "| class | values |\n| --- | --- |\n%s\n\n"
                "| field | values |\n| --- | --- |\n%s\n\n%s") % (
                t, hosted, t, n_gap, n_gap / hosted, rules["gap_mean"], rules["gap_mean"],
                "\n".join("| %s | %d |" % (c, n) for c, n in by_cls),
                "\n".join("| `%s` | %d |" % (p, n) for p, n in by_path), FOOT)
    rows = q("SELECT rid, category FROM record WHERE self_hosted=0").fetchall()
    for k in rules["kinds"]:
        rx = re.compile(k["category"], re.I)
        have = sorted(r for r, c in rows if c and rx.search(c))
        if len(have) < k["min"]:
            out[title(k["topic"], "no " + k["kind"])] = (
                "<!-- fshy:raw-coverage topic=%s check=kind kind=%s -->\n"
                "The catalogue has %d hosted record%s of the kind %s%s. Providers of this kind have free or cheap "
                "tiers, for example %s, so the catalogue leaves out a whole kind of offer.\n\n"
                "To close this issue, research the providers of this kind in the research repository, in the topic `%s` "
                "or in a topic that suits them better, then publish. The check closes this issue when %d hosted records "
                "have a category of this kind.\n\n%s") % (
                k["topic"], anchorless(k["kind"]), len(have), "" if len(have) == 1 else "s", k["kind"],
                (": " + ", ".join(link(r) for r in have)) if have else "", k["examples"], k["topic"], k["min"], FOOT)
    return out


def anchorless(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ------------------------------------------------------------------ the issues
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


def gh(*args):
    r = subprocess.run(["gh"] + list(args), capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("raw_issues: gh %s: %s" % (" ".join(args[:2]), r.stderr.strip()[:300]))
    return r.stdout


def plan(wanted, issues):
    """[(action, title, number, body)] that make the issues match wanted ({title: body}). issues: [{number, title, state,
    body}]; only an issue whose body opens with OURS is ours to change."""
    by = {}
    for i in sorted(issues, key=lambda i: i["number"]):
        if (i.get("body") or "").startswith(OURS):
            by.setdefault(i["title"], []).append(i)
    acts = []
    for t in sorted(set(wanted) | set(by)):
        have = by.get(t, [])
        live = [i for i in have if i["state"].lower() == "open"]
        if t in wanted:
            if live:
                if live[0]["body"].strip() != wanted[t].strip():
                    acts.append(("edit", t, live[0]["number"], wanted[t]))
                acts += [("close-duplicate", t, i["number"], None) for i in live[1:]]
            elif have:
                acts.append(("reopen", t, have[-1]["number"], wanted[t]))
            else:
                acts.append(("create", t, None, wanted[t]))
        else:
            acts += [("close", t, i["number"], None) for i in live]
    return acts


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--sync", action="store_true")
    g.add_argument("--body", metavar="TITLE")
    ap.add_argument("--db", default=os.path.join(ROOT, ".tmp", "fshy", "public.db"))
    ap.add_argument("--today", default=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"))
    a = ap.parse_args(argv)
    log = publog.entries(ROOT)
    if not log:
        print("raw_issues: no publish log (no git history of data/); nothing to do", file=sys.stderr)
        return 2
    if not os.path.exists(a.db):
        print("raw_issues: no store at %s; run python publish/build.py --check first" % a.db, file=sys.stderr)
        return 2
    db = sqlite3.connect(a.db)
    with open(RULES, encoding="utf-8") as f:
        rules = json.load(f)
    wanted = gap_issues(publog.gaps(log))
    wanted.update(coverage_issues(db, a.today, rules))
    if a.body:
        print(wanted.get(a.body, "no issue is titled %s today" % a.body))
        return 0
    for t, text in wanted.items():
        why = refused(t + "\n\n" + text)
        if why:
            print("raw_issues: the text of %s is refused: %s" % (t, why), file=sys.stderr)
            return 1
    repo = os.environ.get("GITHUB_REPOSITORY", "f-shy/fshy.ajam.dev")
    issues = []
    if a.sync or os.environ.get("GH_TOKEN"):
        issues = json.loads(gh("issue", "list", "--repo", repo, "--label", LABEL, "--state", "all", "--limit", "500",
                               "--json", "number,title,state,body"))
    acts = plan(wanted, issues)
    source = log[0]["source"][:7]
    print("raw_issues: %d issue(s) wanted: %s" % (len(wanted), "; ".join(sorted(wanted)) or "none"))
    for act, t, number, text in acts:
        print("%s %s%s" % (act, t, (" #%d" % number) if number else ""))
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
                       "--description", "work that the data asks of the research repository")
                    gh("issue", "create", "--repo", repo, "--title", t, "--label", LABEL, "--body-file", f.name)
                else:
                    if act == "reopen":
                        gh("issue", "reopen", str(number), "--repo", repo)
                    gh("issue", "edit", str(number), "--repo", repo, "--body-file", f.name)
            finally:
                os.unlink(f.name)
        elif act == "close":
            gh("issue", "close", str(number), "--repo", repo, "--reason", "completed", "--comment",
               "Closed by the check: the condition of this issue no longer holds (publish at source commit %s, %s)."
               % (source, a.today))
        elif act == "close-duplicate":
            gh("issue", "close", str(number), "--repo", repo, "--reason", "not planned", "--comment",
               "Closed by the check: an older open issue has this title.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
