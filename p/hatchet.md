# Hatchet

> hatchet.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hatchet/ | JSON https://fshy.ajam.dev/api/v1/entity/hatchet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hatchet

- `compute/hatchet-run` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:47:00.633Z (live) | stale on 2026-11-22
- url https://hatchet.run
- free tier: no credit card, and the first 100,000 runs are free; the orchestration runs on the user's own workers, so the free unit is runs against a control plane. | unit: objects | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: 'No credit card required', quoted from hatchet.run read 2026-10-22
- interface: unknown
- limits:
  - request-rate (binding): the first 100,000 runs are free [1]
  - write-gated: workers run on the user's own platform, so the control plane is free but the compute is not. [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The free unit is runs against Hatchet's control plane; the user deploys the workers, and the vendor names hosted container platforms (Railway, Render, ECS) for them.
- evidence note: the site was read on 2026-10-22 and states the free allowance and that workers run on the user's own infrastructure. The unit is a run count against a queue, not machine time.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a run is a task in a DAG; there is no machine and no session clock
  - free_tier_kind: one-time-credit
  - ps.price: the persistence layer holds run state; a user's workers do the work
  - ps.durability: run state in the queue
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the platform's retention policy
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Get started for free today. No credit card required and your first 100,000 runs are on us.' with 'Deploy workers on Kubernetes, Porter, Railway, Render, ECS, or any container platform. They automatically connect to Hatchet', quoted
- sources:
  - [1] https://hatchet.run
