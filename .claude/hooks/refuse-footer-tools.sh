#!/bin/sh
# PreToolUse hook. The GitHub MCP tools that this hook matches add a credit line to the text that they send.
# Rule 2 of AGENTS.md refuses that line, CI fails on it, and GitHub keeps it in the edit history even after an
# edit. So the call must not reach GitHub. Exit code 2 stops the call and gives this text to the agent.
cat >/dev/null
cat >&2 <<'MSG'
Refused: this GitHub tool adds a credit line to the text that it sends. Rule 2 of AGENTS.md refuses it, and
GitHub keeps it in the edit history. Do not send public text through it.
- To open a pull request: push the branch, then give the operator this link to open it:
  https://github.com/f-shy/fshy.ajam.dev/compare/main...BRANCH
- To change the title or the body of an open pull request: mcp__github__update_pull_request adds no line.
- To read the result of CI: python scripts/ci.py pr NUMBER
MSG
exit 2
