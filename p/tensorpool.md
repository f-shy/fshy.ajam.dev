# TensorPool

> tensorpool.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensorpool/ | JSON https://fshy.ajam.dev/api/v1/entity/tensorpool.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TensorPool

- `compute/tensorpool` | paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:36.649Z (live) | stale on 2026-12-04
- url https://tensorpool.dev
- free tier: no price is published: the home page sells on-demand multi-node GPU clusters (its example command creates an 8xB200 cluster) and lists no card at all and no hourly rate, tier, billing granularity or minimum | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no free tier or trial is published; SSH access is offered to an account that has bought capacity [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes the product and SSH access; it publishes no plan or price, so the record's paid-only verdict rests on an absence and is recorded as such
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states no session cap
  - free_tier_kind: none
  - reclassified_from: dead
  - net.in: yes
  - net.ports: SSH
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Training with no orchestration burden. Manage experiments with a familiar push/pull paradigm that eliminates idle GPU time. Normal SSH access also offered.' quoted; the page publishes no free tier
  - [1] 2026-11-03: the home page sells on-demand multi-node clusters and prints no hourly price for any card | capture: sha256:f50e7cc856af748ad01ae1ee9b1e20aa0c87f0f55d13417e56d7180254a3ec80 | quote: Multi-node GPU clusters on demand. Always 3.2Tbs Infiniband.
  - [1] 2026-11-03: the capacity is on-demand multi-node clusters, scheduled onto clusters operated with compute partners | capture: sha256:f50e7cc856af748ad01ae1ee9b1e20aa0c87f0f55d13417e56d7180254a3ec80 | quote: TensorPool provides on-demand multi-node clusters.
- sources:
  - [1] https://tensorpool.dev
