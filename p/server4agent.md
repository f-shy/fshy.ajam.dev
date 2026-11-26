# Server4Agent

> server4agent.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/server4agent/ | JSON https://fshy.ajam.dev/api/v1/entity/server4agent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Server4Agent

- `compute/server4agent` | trial-only | evidence documented | binding request-rate | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.387Z (live) | stale on 2026-12-05
- url https://www.server4agent.com/pricing
- free tier: $2 of trial credits with 5 GB of storage; usage is metered in dollar credits and the account-wide budget cap is the hard ceiling | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Free plan: 10 GB egress a month, overage n/a. Paid plans: Starter 100 GB then $0.12 / GB, Pro 250 GB then $0.10 / GB, Business 1 TB then $0.08 / GB, Enterprise custom and negotiated | metered: yes | free allowance: 10 GB a month on the Free plan | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - request-rate (binding): $2 of trial credits; paid tiers grant $10, $40 and $150 a month [1]
  - retention-clamped: the $2 is a trial balance; the account-wide budget cap is a hard ceiling on spend [1]
  - per-object-cap: 5 GB of storage on the free tier, 20 GB and 100 GB on the paid ones [1]
- interface detail: REST API at https://api.server4agent.com with an OpenAPI spec, a CLI (@server4agent/cli), typed JavaScript/TypeScript, Python and Go SDK clients, an MCP server (https://mcp.server4agent.com), webhooks and a browser dashboard
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and labels the $2 grant as trial credits, which the record's USD 2 figure matches. The hard budget cap is the mechanism that stops a runaway
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: metered as dollar credits against a hard budget cap; the page states no session clock
  - free_tier_kind: trial
  - ps.gib: 5
  - ps.price: 20 GB and 100 GB on the paid tiers
  - ps.durability: storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the account exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Pick a plan for the projects, credits, and support you need. Usage is metered as dollar credits, and the account-wide budget cap is the hard ceiling.' with 'Free: $2 (trial) credits, 5 GB storage, community support' and paid tiers at $10, $40 and $150 of credits, quoted
  - [1] 2026-11-03: egress overage is $0.12, $0.10 and $0.08 per GB on Starter, Pro and Business; n/a on Free | capture: sha256:0936bc45550081e4b82a34d31ad5b09c520213165e98d491b8c0ab2cffd79e01 | quote: | Egress overage | n/a | $0.12 / GB | $0.10 / GB | $0.08 / GB | Negotiated |
  - [1] 2026-11-03: Free allows 10 GB egress a month; Starter 100 GB, Pro 250 GB, Business 1 TB | capture: sha256:0936bc45550081e4b82a34d31ad5b09c520213165e98d491b8c0ab2cffd79e01 | quote: | Egress / mo | 10 GB | 100 GB | 250 GB | 1 TB | Custom |
  - [2] 2026-11-03: a REST API exists with the same primitives as the MCP tools | capture: sha256:625378466d3389cfe5b52531052616e16cf900596e3acb85aa000d9b3fdc3203 | quote: Everything the MCP tools do is available over HTTP, authenticated by API key.
  - [3] 2026-11-03: a command-line client exists (@server4agent/cli) | capture: sha256:a1ec95f77d47ff493f587d94da06d4e0e94b8039c06b5ab4e1a88cf17352f449 | quote: npx @server4agent/cli login # approve in the browser
  - [4] 2026-11-03: SDKs exist | capture: sha256:1eddb569c01efebdc7417f0ab8b889613e0ca804747549dc0ee99960cb39f911 | quote: Typed JavaScript/TypeScript, Python, and Go clients for the code around your agent.
- sources:
  - [1] https://www.server4agent.com/pricing
  - [2] https://www.server4agent.com/docs/api
  - [3] https://www.server4agent.com/docs/sdks
  - [4] https://www.server4agent.com/docs
