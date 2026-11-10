# mk.absturztau.be

> absturztau.be | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/absturztau/ | JSON https://fshy.ajam.dev/api/v1/entity/absturztau.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mk.absturztau.be — Sharkey, 50 GB drive per user

- `storage/mk-absturztau-be-sharkey-50-gb-drive-per-user` | fails-quota | evidence reported | binding per-object-cap | category fediverse-sharkey
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mk.absturztau.be
- free tier: 50000 MB = 50 GB per user drive; maxFileSize 262144000 bytes (250 MiB) per object. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, CDN-served, no meter. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 250 MiB [1]
- limits note: per-object-cap 250 MiB; per-user 50 GB; request-rate: Sharkey enforces per-IP 429 on drive writes.
- interface detail: rest
- tooling: Sharkey/IceShark is Misskey-API-compatible: same POST /api/drive/files/create, same MiAuth. A single client works across Misskey, Sharkey, Firefish and Iceshrimp.NET.
- composes with: Open registration (`openRegistrations: true`, 916 users). 50 GB x N accounts. Best tier-2 host of the family: bigger than most, still sane per-file.
- reliability: 916-user German hobby instance, 1.7 M local posts — active and healthy, but single-operator. Sharkey 2025.5.2-dev, self-described non-stable branch.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 50000 MB = 50 GB per user drive; maxFileSize 262144000 bytes (250 MiB) per object.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=50000, maxFileSize=262144000, disableRegistration=false
  - [2] 2026-10-21: probe: GET -> 200, software sharkey 2025.5.2-dev+g8e80ed6771, openRegistrations=true, users.total=916, localPosts=1708820
- sources:
  - [1] https://mk.absturztau.be/api/meta
  - [2] https://mk.absturztau.be/nodeinfo/2.1
