# Sandbox as a Service

> sandbox-as-a-service.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandbox-as-a-service/ | JSON https://fshy.ajam.dev/api/v1/entity/sandbox-as-a-service.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandbox as a Service

- `compute/sandbox-as-a-service` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:16.353Z (live) | stale on 2026-12-05
- url https://sandbox-as-a-service.com/pricing
- free tier: $5 of signup credit, which the page estimates at about 56 hours of a small sandbox; small is 2 vCPU, 4 GB and 40 GB at $0.09 an hour | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: No card is required to sign up; the quickstart signs in with Google and creates an API key. The kind email is inferred from the Google sign-in.
- interface: rest
- limits:
  - request-rate (binding): $0.09 an hour for small, $0.28 for medium and $0.55 for large [1]
  - request-rate (binding): 20 concurrent sandboxes per account; going over returns 429 until one is destroyed [1]
  - retention-clamped: a sandbox has a 1,440-minute maximum lifetime [1]
- interface detail: REST API at sandbox-as-a-service.com/v1 with bearer API keys, plus an MCP server; no SDK, CLI or SSH documented
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the credit, the ladder, the concurrency cap and the 1,440-minute lifetime. That lifetime is the wall-clock axis, stated by the vendor in the units it is enforced in
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 4
  - shape.disk: 40
  - shape.note: small; medium is 4 vCPU, 8 GB and 80 GB, large is 8 vCPU, 16 GB and 160 GB
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: 1,440 minutes maximum lifetime per sandbox, and an account with no running sandboxes costs nothing
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 40
  - ps.price: included in the sandbox size
  - ps.durability: sandbox disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the 1,440-minute lifetime
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Prepaid credit, charged for exactly as long as a sandbox runs - no minimum, no rounding up, and provisioning time is not billed. No subscription, no seats, no minimum spend. An account with no running sandboxes costs nothing.' with the ladder 'small 2 vCPU 4 GB 40 GB $0.09/hour', 'A 10-minute small sandbox: about $0.015. The $5 of credit you get on signup covers roughly 56 hours', '20 concurrent sandboxes' and '1440 minutes maximum lifetime', quoted
  - [2] 2026-11-03: the service is reached by REST and an MCP server | capture: sha256:b036caf42e41feaad8f8f2d12dc96c0a34c6e910278feacd8b7ce9ebd5950011 | quote: Dedicated VMs for AI agents · REST + MCP
  - [1] 2026-11-03: signup needs no card | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: No credit card is required to sign up, and we never charge a card automatically.
  - [1] 2026-11-03: the pricing page lists hourly sandbox prices only; no egress allowance or egress price | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: Prepaid credit, charged for exactly as long as a sandbox runs
- sources:
  - [1] https://sandbox-as-a-service.com/pricing
  - [2] https://sandbox-as-a-service.com/
