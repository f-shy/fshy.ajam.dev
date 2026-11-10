# Trainy

> trainy.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trainy/ | JSON https://fshy.ajam.dev/api/v1/entity/trainy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trainy

- `compute/trainy` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-10-30T00:03:24.252Z (live) | stale on 2026-11-30
- url https://trainy.ai/
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price: the product is orchestration tooling over GPUs rented elsewhere [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only rather than dead: the product is sold and reachable. Self-hosted: the user deploys Konduktor on its own cluster in any cloud or on bare metal, and Trainy helps pick a cloud provider rather than being one.
- evidence note: the site was read on 2026-10-22 and sells cluster orchestration over existing or rented GPUs, with no plan or price. That confirms paid-only
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a job is rescheduled onto healthy hardware; the page states no clock
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Run your GPUs like a frontier lab' with 'From local to 64 H100s in under an hour' and 'Konduktor detects bad GPUs and nodes, cordons them, and reschedules your job onto healthy hardware', quoted; no plan and no price
  - [1] 2026-10-29: Trainy's Konduktor is deployed on a user's cluster in a cloud or on bare metal; Trainy is not a cloud provider | capture: sha256:bcc6e9d764dbf5d25615f466c293b873ce6a5fb39cb9909232b1cd89338552f1 | quote: Deploy Konduktor on any cloud or on bare metal.
- sources:
  - [1] https://trainy.ai/
