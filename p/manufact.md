# Manufact

> manufact.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/manufact/ | JSON https://fshy.ajam.dev/api/v1/entity/manufact.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Manufact

- `compute/manufact` | qualifies-with-caveat | evidence reported | binding volume-quota | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-18T04:58:06.793Z (live) | stale on 2026-12-03
- url https://manufact.com
- free tier: Free, $0 a month with no card: $5 of included credits per month and 1 project. Tool calls, builds, evals, publishing checks, bandwidth and managed-chat output draw from that pool; when it runs out, metered activity pauses until the monthly reset and Free incurs no overage | unit: credits | metered on: wall-clock | read on: 2026-10-29 | source: [1] | note: read from the vendor pricing page; allowances reset on the monthly cycle of the organisation and do not roll over
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: "Bandwidth (egress)" row in the first-party compare-plans table, priced per GB on every metered tier | metered: yes | price per TB: $0.15 / GB on Free, Pay as you go and Pro; Custom on Enterprise | source: [2]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): the Free plan includes $5 of credits a month and 1 project; when the credits run out, metered activity pauses until the monthly reset [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-29: a hosted Free plan ($5 of credits a month, 1 project, no card) above Pay as you go, Pro and Enterprise; self-hosting is included only on Enterprise. The site read on 2026-10-22 published no plan
- self hosted: no
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an MCP server is deployed as a service; the page states no clock
  - free_tier_kind: none
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: the site was read on 2026-10-22 and presents an MCP server framework with a cloud to deploy them, built on mcp-use; it publishes no plan and no price
  - [1] 2026-10-29: the hosted Free plan is $0 a month with $5 of included credits per month and 1 project, no card required; self-hosting is not included on Free | capture: sha256:7de0438d49db41655672d6b312cb3dee42296aa089e5f66405ce61474cf52926 | quote: $5 included credits per month
  - [1] 2026-11-18: not stated | capture: sha256:902c091a96f1066d818092276bd343ed7bca3c93e65088ca9f9bc321d7850fec | quote: ## Free Explore MCP. Ship your first server.
- sources:
  - [1] https://manufact.com/pricing
  - [2] https://manufact.com
