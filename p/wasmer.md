# Wasmer

> wasmer.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wasmer/ | JSON https://fshy.ajam.dev/api/v1/entity/wasmer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wasmer

- `compute/wasmer` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T10:36:19.923Z (live) | stale on 2026-12-05
- url https://wasmer.io/pricing
- free tier: Free forever: 150 GB of bandwidth, a global edge CDN and 6 compute hours on a single seat | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Pricing table, Bandwidth row: Hobby (free) 150 GB; Pro 150 GB, then $0.10 per GB; Enterprise Custom. No overage price is stated for the Hobby column. | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): 6 compute hours on Free [1]
  - per-ip-shaping: 150 GB of bandwidth on Free [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free tier is a permanent one rather than a trial, and the two numbers that decide it are 6 compute hours and 150 GB of bandwidth
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - network_out.allow_outbound: yes
  - network_out.per_session_bytes: 150 GB on Free
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free forever · 150 GB bandwidth · Global Edge network CDN · 6 Compute Hours' on a single-member seat, quoted
  - [1] 2026-11-04: the Bandwidth row lists 150 GB (Hobby), 150 GB then $0.10 per GB (Pro) and Custom (Enterprise) | capture: sha256:c772992da7fd3be44adc13c546c89b39e4aac74f0179414be95851678648e21d | quote: Bandwidth 150 GB 150 GB (then $0.10 per GB) Custom
- sources:
  - [1] https://wasmer.io/pricing
