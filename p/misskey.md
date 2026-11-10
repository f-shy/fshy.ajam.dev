# misskey.io registration

> misskey.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.io registration (as opposed to its capacity)

- `storage/misskey-io-registration` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://misskey.io/api/meta
- free tier: None reachable: Its numbers are good (10 GiB, 500 MiB objects) but signup is closed indefinitely. The operator states it cannot add server capacity because their cloud provider was breached. Capacity witho. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: Its numbers are good (10 GiB, 500 MiB objects) but signup is closed indefinitely — the operator states it cannot add server capacity because their cloud provider was breached. Capacity…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Its numbers are good (10 GiB, 500 MiB objects) but signup is closed indefinitely — the operator states it cannot add server capacity because their cloud provider was breached. Capacity…
- sources:
  - [1] https://misskey.io/api/meta

## misskey.io — 10 GiB drive, 500 MiB per object

- `storage/misskey-io-10-gib-drive-500-mib-per-object` | fails-quota | evidence reported | binding per-object-cap | category fediverse-misskey
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://misskey.io
- free tier: 10240 MB = 10 GiB per user; maxFileSize 524288000 bytes = 500 MiB per object. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MiB per object | bytes: 524288000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, served from misskey.io's own CDN (Cloudflare + object storage). No egress charge. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 500 MiB per object [1]
- limits note: per-object-cap 500 MiB; per-user 10 GiB; request-rate is the real constraint here (huge shared IP pool, aggressive per-IP limits).
- interface detail: rest
- tooling: Misskey API / MiAuth.
- composes with: The largest Misskey instance in existence (~600k users) so the best-tested API, BUT registration is CLOSED: the /api/meta description states in Japanese that new signups are suspended because the cloud provider for their servers suffered unauthorised access and they cannot add capacity. Only useful with existing accounts or an invite if the operator reopens.
- reliability: Registration closed as of this probe; operator explicitly cannot expand capacity. The 500 MiB per-object number is still the useful data point: it proves the family's per-object ceiling.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10240 MB = 10 GiB per user; maxFileSize 524288000 bytes = 500 MiB per object.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=10240, maxFileSize=524288000, disableRegistration=true
  - withheld 2026-10-21: probe: description field (ja) — '現在、利用しているクラウド事業者への不正アクセスによりサーバーの増設が出来ないため新規登録を停止しています'
- sources:
  - [1] https://misskey.io/api/meta
