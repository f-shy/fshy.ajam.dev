# Archal

> archal.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archal/ | JSON https://fshy.ajam.dev/api/v1/entity/archal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Archal

- `compute/archal` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:05.598Z (live) | stale on 2026-12-05
- url https://www.archal.ai/
- free tier: $20 in free usage, no card: $5 at signup and $15 when the first sandbox is ready | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: neither https://www.archal.ai/ nor https://docs.archal.ai/ states an egress allowance or an overage price; usage is metered per ready environment | metered: no | source: [1]
- identity: email | detail: 'No card required' for the $20 in free usage, quoted from argalabs.com read 2026-10-22
- interface: rest, cli
- limits:
  - request-rate (binding): $20 of credit: $5 at signup and $15 when the first sandbox is ready [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST endpoints per environment, the archal CLI (npm), a TypeScript client and MCP; no SSH interface is documented
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the product page was read on 2026-10-22 and states the split credit and the no-card condition. The record's USD 20 figure was right; the split and the trigger were missing
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a sandbox resets to its baseline between runs; the page states no clock
  - free_tier_kind: one-time-credit
  - ps.price: not stated on this page
  - ps.durability: state persists across tool calls then resets to baseline
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: the sandbox's baseline
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Get $20 in free usage. No card required. $5 arrives upon sign up and the remaining $15 when your first sandbox is ready.' and 'Changes persist across tool calls, then reset to the same baseline', quoted
  - [2] 2026-11-03: usage is metered per ready environment; no egress or data-transfer meter is stated | capture: sha256:74ca300baa9c5c4c968e2f18781e03aae9354abf0f0158da542947353b6e6117 | quote: usage metering per ready environment
  - [2] 2026-11-03: the sandbox is reached by CLI, TypeScript client, MCP or REST | capture: sha256:74ca300baa9c5c4c968e2f18781e03aae9354abf0f0158da542947353b6e6117 | quote: Use the CLI, TypeScript client, MCP, or raw REST without a coding agent.
- sources:
  - [1] https://www.archal.ai/
  - [2] https://docs.archal.ai/
