# uploadthing

> uploadthing.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadthing/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadthing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uploadthing

- `storage/uploadthing` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.963Z (live) | stale on 2026-11-19
- url https://uploadthing.com/pricing
- free tier: none reachable: Free '2GB App' with storage shared between all apps; next tier is 100GB App at $10/month | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Bandwidth is not charged on usage-based pricing; billing is by storage used | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: read 2026-11-03: https://uploadthing.com/pricing (free App storage shared between all apps) and https://docs.uploadthing.com/blog/usage-based (no bandwidth charge, billing by storage used); the 100GB App price at $10/month carries the 2026-10-21 evidence rows only.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free '2GB App' shared across all apps, no egress allowance beyond that; next tier is 100 GB for $10/mo
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free '2GB App' shared across all apps, no egress allowance beyond that; next tier is 100 GB for $10/mo
  - [2] 2026-11-03: bandwidth is not charged; billing is by storage used | capture: sha256:2c6881c187f97296bd363503385c48f0fa0154baf1a7eeac0c404fbc27c8b0a5 | quote: we don't charge for things like seats, requests, or bandwidth. You just pay for the storage used.
  - [1] 2026-11-03: the free 2GB App shares its storage between all apps | capture: sha256:ffa86816e95dfc1d0d243f5f6a3627d3f1d89a352322594911e946cc967fc848 | quote: - * Storage shared between all apps
  - [1] 2026-11-04: the free 2GB App shares its storage between all apps | capture: sha256:ffa86816e95dfc1d0d243f5f6a3627d3f1d89a352322594911e946cc967fc848 | quote: - * Storage shared between all apps
- sources:
  - [1] https://uploadthing.com/pricing
  - [2] https://docs.uploadthing.com/blog/usage-based
