# Sandbox as a Service

> sandbox-as-a-service.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandbox-as-a-service/ | JSON https://fshy.ajam.dev/api/v1/entity/sandbox-as-a-service.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sandbox as a Service

- `compute/sandbox-as-a-service` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:21:03.221Z (live) | stale on 2026-12-25
- url https://sandbox-as-a-service.com/pricing
- free tier: $5 of signup credit, which the page estimates at about 56 hours of a small sandbox; small is 2 vCPU, 4 GB and 40 GB at $0.09 an hour | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: A sandbox is destroyed when its timeout expires, extensions included; nothing inside survives. Prepaid credit does not expire. | source: [1]
- egress: The pricing page lists hourly sandbox prices only; no egress price or transfer allowance is published. | metered: no | source: [1]
- identity: email | detail: Sign in with Google, create an API key, and spend the free credit; adding a payment method is needed only when the credit runs out.
- interface: rest
- limits:
  - request-rate (binding): $0.09 an hour for small, $0.28 for medium and $0.55 for large [1]
  - request-rate (binding): Per account, provisioning plus running. Going over 20 returns 429 until one is destroyed; more can be arranged on request. [1]
  - retention-clamped: A sandbox is destroyed when its 1440-minute lifetime expires, extensions included. [1]
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
  - [1] 2026-11-24: the 1440-minute lifetime destroys the sandbox | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: A sandbox is destroyed when its timeout expires, extensions included. Sandboxes are disposable by design; nothing inside survives.
  - [1] 2026-11-24: Google sign-in and API key; a card is needed only after the credit runs out | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: Sign in with Google, create an API key, and spend the free credit. Adding a payment method is only necessary when you run out.
  - [1] 2026-11-24: billing per second of sandbox runtime with no minimum or rounding | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: Prepaid credit, charged for exactly as long as a sandbox runs — no minimum, no rounding up, and provisioning time is not billed.
  - [1] 2026-11-24: the 20-concurrency cap returns 429 | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: Per account, provisioning plus running. Going over returns `429` until one is destroyed.
  - [1] 2026-11-24: the USD 5 signup credit and no-card signup | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: New accounts receive $5 of runtime credit — about 56 hours on the small size. No credit card is required to sign up, and we never charge a card automatically.
  - [1] 2026-11-24: the small, medium and large size table with hourly prices | capture: sha256:b0ed2b9c866e43b89c33a3e98ae708615f368d83735f072e47055c01b0fc2a4e | quote: The E2B column is their published $0.000014/vCPU/second and $0.0000045/GiB/second applied to the same vCPU and memory, read from e2b.dev/pricing on 20 September 2026.
- sources:
  - [1] https://sandbox-as-a-service.com/pricing
  - [2] https://sandbox-as-a-service.com/
