# Baponi

> baponi.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/baponi/ | JSON https://fshy.ajam.dev/api/v1/entity/baponi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Baponi

- `compute/baponi` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:05.598Z (live) | stale on 2026-12-05
- url https://baponi.ai/pricing/
- free tier: Free forever, no card: 1,000 credits a month, 5 concurrent runs and 10,000 credits included at signup | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or overage price is stated on https://baponi.ai/pricing/ or in the API docs; the default network policy is blocked, and an unrestricted sandbox has its outbound bytes metered internally for billing | metered: yes | source: [1]
- identity: email | detail: 'No credit card required' and 'Free forever' on the pricing page, read 2026-10-22; the page states no other gate
- interface: rest
- limits:
  - request-rate (binding): 1,000 credits a month on Free; 5 concurrent runs [1]
- interface detail: REST API, an MCP server and a Python SDK (pip install baponi); no CLI or SSH interface is documented
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states a free-forever tier that needs no card, which also settles identity_cost as email
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; the binding limit is 5 concurrent runs
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · Everything you need to ship AI agents to production. No credit card required. Free forever. · 1,000 credits / month · 5 concurrent runs · 10,000 credits included · $1.00 per 1K additional credits', quoted
  - [2] 2026-11-03: unrestricted sandboxes have outbound bytes metered for billing; no allowance or price is published | capture: sha256:04f92017035404c7c4965ab2591ff6f51b2913058eecbe06146e5c9fc19405b6 | quote: | `unrestricted` | Full internet access. Outbound bytes are metered internally for billing. |
  - [3] 2026-11-03: a REST API exists | capture: sha256:ab6e512bedcb0a8f274739ec90573405b4d313e36941e34b1cd89940670214bc | quote: The API is a standard REST interface. Any HTTP client works:
- sources:
  - [1] https://baponi.ai/pricing/
  - [2] https://baponi.ai/docs/api/execute.md
  - [3] https://baponi.ai/docs/api/overview.md
