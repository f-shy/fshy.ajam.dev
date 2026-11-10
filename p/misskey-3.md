# misskey.flowers

> misskey.flowers | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey-3/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.flowers — Misskey (hanami fork), 12 GB per user

- `storage/misskey-flowers-misskey-12-gb-per-user` | fails-quota | evidence reported | binding per-object-cap | category fediverse-misskey
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://misskey.flowers
- free tier: 12288 MB = 12 GiB per user; maxFileSize 250 MiB. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, plain CDN path. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 250 MiB [1]
- limits note: per-object-cap 250 MiB; per-user 12 GiB.
- interface detail: rest
- tooling: Misskey API / MiAuth as above.
- composes with: Open registration. 12 GiB x N.
- reliability: Small themed instance; nothing special but live and open.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 12288 MB = 12 GiB per user; maxFileSize 250 MiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=12288, maxFileSize=262144000, disableRegistration=false, version 2026.9.2-hanami
- sources:
  - [1] https://misskey.flowers/api/meta
