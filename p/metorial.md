# Metorial

> metorial.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/metorial/ | JSON https://fshy.ajam.dev/api/v1/entity/metorial.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Metorial

- `compute/metorial` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:32.968Z (live) | stale on 2026-12-05
- url https://metorial.com
- free tier: a free Dev plan, a fixed-price Scale plan and custom Enterprise pricing | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://metorial.com/pricing lists tool-call, team-member and integration limits and no data-transfer term or price | metered: no | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - write-gated (binding): the Dev plan's limits and the Scale plan's price are on a separate pricing page this record does not cite [1]
- interface detail: the Metorial API with keys issued in the dashboard, and the metorial and metorial-admin CLIs (npm @metorial/cli)
- tooling: the @metorial/cli npm package and the API
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the three-plan ladder with a free Dev plan. The page does not publish the Dev plan's limits, so no number is given
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the product connects MCP servers; there is no machine and no session clock
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'There is a free Dev plan, a fixed-price Scale plan, and custom Enterprise pricing.' and 'Get started for free', quoted
  - [2] 2026-11-03: the free plan is limited by tool calls, members and integrations, with no egress term | capture: sha256:b644d36852d2c630ba71c5df44d59f0255d4a13e01cad07b765ac5b7acbaecc6 | quote: Metorial Dev is free, at $0/month: 500K tool calls per month, unlimited auth connections, up to 2 team members, and up to 10 provider integrations.
  - [2] 2026-11-03: an API is included on every plan, Dev included | capture: sha256:b644d36852d2c630ba71c5df44d59f0255d4a13e01cad07b765ac5b7acbaecc6 | quote: Developer API access | Access to the Metorial API. | Yes | Yes | Yes |
  - [3] 2026-11-03: two CLIs exist | capture: sha256:d4b0f54c713cac1f189d96ce68a62890767caf403c583d1eadbb166d25c6f1dc | quote: Metorial ships two CLIs:
- sources:
  - [1] https://metorial.com
  - [2] https://metorial.com/pricing
  - [3] https://metorial.com/cli.md
