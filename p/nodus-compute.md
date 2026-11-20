# Nodus Compute

> nodus-compute.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodus-compute/ | JSON https://fshy.ajam.dev/api/v1/entity/nodus-compute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nodus Compute

- `compute/nodus-compute` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:29.691Z (live) | stale on 2026-11-22
- url https://www.nodus-compute.ai/pricing/
- free tier: no free tier: six CPU and memory sizes from $0.0075 to $0.1054, each with an included disk, and a GPU table the page loads on demand | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.0075 for 1 vCPU and 1 GiB up to $0.1054 for 4 vCPU and 16 GiB [1]
  - per-object-cap: included disk ranges from 25 GB at the smallest size to 160 GB at 4 vCPU and 8 GiB [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the six CPU shapes with supply-side rates and included disk. There is no free tier, so the record's USD 30 credit is not established and the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 25
  - shape.note: the smallest of six CPU/RAM sizes; the GPU table is loaded by script and was not read
  - session_cap.restart_required: no
  - session_cap.note: supply-side pricing; the page states no clock
  - free_tier_kind: none
  - ps.gib: 25
  - ps.price: included disk per size
  - ps.durability: included disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| 1 vCPU | 1 GiB | 25 GB | $0.0075 |' through '| 4 vCPU | 16 GiB | 64 GiB | $0.1054 |' with the note 'These six CPU/RAM sizes have nominal Modal equivalents', quoted
- sources:
  - [1] https://www.nodus-compute.ai/pricing/
