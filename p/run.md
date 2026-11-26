# Run Cloud

> run.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/run/ | JSON https://fshy.ajam.dev/api/v1/entity/run.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Run Cloud

- `compute/run-cloud` | dead | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.run.cloud/sandboxes/index.md
- free tier: no longer available to new organizations; existing sandbox workloads continue during the deprecation window | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: Listed with a USD 0.00 promotional credit; ongoing compute requires paid plans.
- per-object cap: not applicable
- retention: a sandbox can be snapshotted and restored; the deprecation window is the retention limit | days: 0
- egress: not published on the page read | metered: no | source: [1]
- identity: card | detail: no new organization can obtain it, so the identity cost is moot
- interface: rest, cli
- limits:
  - per-object-cap: maximum 32 vCPUs and 112 GiB RAM per sandbox; default 0.125 vCPU and 128 MiB [1]
  - retention-clamped (binding): the capability is being retired and is closed to new organizations [1]
- limits note: paused and stopped sandboxes continue to reserve capacity until permanently destroyed
- binding note: the capability is being retired and is closed to new organizations, so the withdrawal is the constraint
- interface detail: Firecracker microVM with an API and a CLI
- tooling: runcloud CLI and API; snapshot and restore
- composes with: none: a new organization cannot create one
- reliability: no reliability event recorded
- notes: RunCloud promotional free credits previously advertised have been discontinued; the platform offers paid server management tiers.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - billing_model: allocated
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: moot: withdrawn
  - keep_rate.basis: not established
  - keep_rate.source: https://docs.run.cloud/sandboxes/index.md
  - persistent_storage.durability: snapshot
  - persistent_storage.survives_stop: yes
  - persistent_storage.max_retention: the deprecation window
  - free_tier_kind: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: the price of a product nobody can buy is not zero, it is unreachable
- evidence:
  - [1] 2026-10-22: 'Linux microVM sandboxes are deprecated. This capability is being retired and is no longer available to new organizations.'
  - [1] 2026-10-22: maximum 32 vCPUs and 112 GiB RAM; default reservation 0.125 vCPU and 128 MiB
- sources:
  - [1] https://docs.run.cloud/sandboxes/index.md
