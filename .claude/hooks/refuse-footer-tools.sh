#!/bin/sh
# PreToolUse hook. The GitHub MCP tools that this hook matches add a credit line to the text that they send.
# Rule 2 of AGENTS.md refuses that line, CI fails on it, and GitHub keeps it in the edit history even after an
# edit. So the call must not reach GitHub. Exit code 2 stops the call and gives this text to the agent.
cat >/dev/null
cat >&2 <<'MSG'
Refused: this GitHub tool adds a credit line to the text that it sends. Rule 2 of AGENTS.md refuses it, and
GitHub keeps it in the edit history. Do not send public text through it.
- To open a pull request: push the branch. The workflow open-pr opens the pull request from the
  commits and re-runs its held pull_request run of build. Read the result with: python scripts/ci.py pr NUMBER
- To change the title or the body of an open pull request: mcp__github__update_pull_request adds no line.
- To read the result of CI: python scripts/ci.py pr NUMBER
MSG
exit 2
