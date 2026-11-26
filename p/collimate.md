# Collimate

> collimate.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/collimate/ | JSON https://fshy.ajam.dev/api/v1/entity/collimate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Collimate

- `compute/collimate` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T11:38:12.285Z (live) | stale on 2026-12-25
- url https://collimate.ai/pricing
- free tier: a free demo key with no card: 2 concurrent sandboxes at 1 hour each, and a suspend call that stops the meter | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the price list on https://collimate.ai/ and https://collimate.ai/pricing has vCPU, RAM and suspended-storage meters and states no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: 'Sign up with an email and the gateway mints a key scoped to your tenant', quoted from collimate.ai/pricing read 2026-10-22
- interface: rest
- limits:
  - request-rate (binding): 2 concurrent sandboxes on the free demo key, 100 on the paid tier [1]
  - retention-clamped: a free sandbox session is capped at 1 hour; a paid session runs to 24 hours [1]
- interface detail: REST API, a Python SDK and a hosted MCP server; no CLI or SSH interface is documented
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the demo key's concurrency, the 1-hour session and the suspend verb. The free tier is a capped demo, so the record names the caps
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: 1 hour per session on the free key, 24 hours paid; an explicit suspend stops the meter before the cap
  - free_tier_kind: trial
  - burst_x: 1.0
  - ps.price: not stated on this page
  - ps.durability: forks preserve live process memory across clones
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free with a demo key, no card' and '2 concurrent sandboxes, 1 hour each' and 'Sign up with an email and the gateway mints a key scoped to your tenant - rate-limited and capped per key' and 'suspend # stops the meter', quoted
  - [2] 2026-11-03: the price list has vCPU, RAM and suspended storage meters and no egress meter | capture: sha256:c704be3c5d15941b50ce7ba4870e8d7e0ae379658dde92fbacd1c88214e984b1 | quote: vCPU $0.040 / hr · RAM $0.012 / GB-hr · suspended storage $0.10 / GB-mo · spawning and forking free.
  - [2] 2026-11-03: access is by REST, the Python SDK or hosted MCP | capture: sha256:c704be3c5d15941b50ce7ba4870e8d7e0ae379658dde92fbacd1c88214e984b1 | quote: Give an agent a real shell and Python per task, over REST, the Python SDK, or hosted MCP.
  - [1] 2026-11-24: a free demo key is available without a card | capture: sha256:73e4d01f28e85cb02e6f112a644dc2de0c4396cce23ad10f6e245a7d31b04169 | quote: Start free with a demo key, no card.
  - [1] 2026-11-24: the demo key allows 2 concurrent sandboxes of 1 hour each | capture: sha256:73e4d01f28e85cb02e6f112a644dc2de0c4396cce23ad10f6e245a7d31b04169 | quote: * 2 concurrent sandboxes, 1 hour each
  - [1] 2026-11-24: sign-up takes an email address and mints a tenant key | capture: sha256:73e4d01f28e85cb02e6f112a644dc2de0c4396cce23ad10f6e245a7d31b04169 | quote: Sign up with an email and the gateway mints a key scoped to your tenant
  - [2] 2026-11-24: access is through REST, a Python SDK and hosted MCP | capture: sha256:c704be3c5d15941b50ce7ba4870e8d7e0ae379658dde92fbacd1c88214e984b1 | quote: Give an agent a real shell and Python per task, over REST, the Python SDK, or hosted MCP.
  - [1] 2026-11-24: the published meters are CPU, memory and suspended storage, with no egress charge listed | capture: sha256:73e4d01f28e85cb02e6f112a644dc2de0c4396cce23ad10f6e245a7d31b04169 | quote: Pro is billed per second on the CPU and memory a sandbox holds while it is live, plus snapshot storage while it is suspended.
  - [1] 2026-11-24: an explicit suspend call stops the meter | capture: sha256:73e4d01f28e85cb02e6f112a644dc2de0c4396cce23ad10f6e245a7d31b04169 | quote: suspend # stops the meter
- sources:
  - [1] https://collimate.ai/pricing
  - [2] https://collimate.ai/
