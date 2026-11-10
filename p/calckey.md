# calckey.world

> calckey.world | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/calckey/ | JSON https://fshy.ajam.dev/api/v1/entity/calckey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## calckey.world — Sharkey, 10 GB per user

- `storage/calckey-world-sharkey-10-gb-per-user` | fails-quota | evidence reported | binding per-object-cap | category fediverse-sharkey
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://calckey.world
- free tier: 10240 MB = 10 GiB per user; maxFileSize 250 MiB. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free CDN. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 250 MiB [1]
- limits note: per-object-cap 250 MiB; per-user 10 GiB.
- interface detail: rest
- tooling: Misskey-compatible API.
- composes with: Open registration, ~1030 users. 10 GiB x N.
- reliability: Generic-purpose host that has been continuously migrated Firefish->Sharkey; stable enough, single operator.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10240 MB = 10 GiB per user; maxFileSize 250 MiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=10240, maxFileSize=262144000, disableRegistration=false
  - [2] 2026-10-21: probe: GET -> 200, software sharkey 2025.4.7, openRegistrations=true
- sources:
  - [1] https://calckey.world/api/meta
  - [2] https://calckey.world/nodeinfo/2.0
