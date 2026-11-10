# misskey.gg

> misskey.gg | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey-4/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.gg — Misskey 2026.10, 1 TB drive per user

- `storage/misskey-gg-misskey-2026-10-1-tb-drive-per-user` | qualifies-with-caveat | evidence documented | binding per-object-cap | category fediverse-misskey
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://misskey.gg
- free tier: 1024000 MB = 1 TiB drive capacity PER USER. The per-object cap is 250 MiB: maxFileSizeMb reads 1024 (1 GiB) but the top-level maxFileSize of 262,144,000 bytes is the enforced field. This is the single largest per-user quota located on a live, registration-open fediverse instance. | unit: TiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 250 MiB per object, enforced by the top-level maxFileSize of 262,144,000 bytes | bytes: 262144000 | source: [1] | note: policies.maxFileSizeMb states 1024 (1 GiB) and the top-level maxFileSize states 262,144,000 bytes (250 MiB). The evidence entry notes that the top-level field is the cap actually enforced, so the record carries 250 MiB and the 1 GiB figure lives here as the field that lies.
- retention: source: [1] | note: not stated
- egress: Free. Media is served from a plain path on the instance domain (observed scheme: https://sss.<instance>/sss/<shard>/<uuid>) with `Cache-Control: max-age=31536000, immutable`. No egress meter, no bandwidth charge, no signed URL. | metered: no | source: [2]
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 250 MiB per object (top-level maxFileSize 262,144,000 bytes); policies.maxFileSizeMb claims 1 GiB and is not enforced [1]
  - write-gated: inviteLimit: 1` per 1440 min does NOT gate open signup [1]
- limits note: per-object-cap 1 GiB (maxFileSizeMb=1024, verified 262144000 bytes = 250 MiB on most other instances, 524288000 = 500 MiB on misskey.io). Drive quota 1 TiB/user. Usage-anomaly controls: `inviteLimit: 1` per 1440 min does NOT gate open signup. Request-rate: Misskey applies a per-IP rate limiter on /api/drive/files/create (4096 req/hr default per IP, plus per-account limits, 250 MB/hr-ish effective on small instances).
- interface detail: rest
- tooling: Misskey HTTP API is a clean JSON REST surface: POST /api/drive/files/create (multipart, `file` field) with an `i` (token) in the body; POST /api/drive/files/upload-from-url; POST /api/drive/files/delete; POST /api/drive/files (list). Token minted via MiAuth (GET https://<host>/miauth/<uuid>?name=...&permission=write:drive,read:drive) or POST /api/signin with username+password -> returns `i`, which is then just a query param. No library needed: it is a 20-line requests wrapper. rclone has no Misskey backend; write a thin one.
- composes with: DriveCapacityMb is a per-user soft counter enforced by the instance, not a hard technical wall. Media attached to notes can still be served after the drive is full. Because each account is an independent counter and registration is open (API reports `disableRegistration: false`, `emailRequiredForSignup: true`), each account holds 1 TiB. Ten accounts hold 10 TiB. The provider accepts a single POST per account, so a client with mail control can register many.
- reliability: Instance is a single volunteer-run host with ~small user count; a 1 TB drive is a published number, not a promise, and one operator decision or a disk-full incident takes everything offline at once. No SLA, no backup guarantee. Treat as 'high capacity, zero durability'.
- notes: 1024000 MB = 1 TiB drive capacity PER USER, with a 250 MiB per-object cap: maxFileSizeMb reads 1024 (1 GiB) and the top-level maxFileSize of 262,144,000 bytes is enforced, so a 1 TiB drive at 250 MiB per object needs 4,096 uploads. This is the single largest per-user quota located on a live, registration-open fediverse instance.
- evidence note: The quota is a live API field read on 2026-10-21, not a page claim. The record stays documented because the identity field is inferred from prose, not read from the API. Was documented, now documented.
- extras:
  - verified[0].url: https://misskey.gg/api/meta
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 3228
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change to the numbers; the field's location is confirmed (maxFileSize is top-level, not under policies)
- evidence:
  - [1] 2026-10-22: driveCapacityMb = 1024000 (1,024,000 MB = 1 TiB per user); policies.maxFileSizeMb = 1024 while the top-level maxFileSize = 262,144,000 B = 250.0 MiB is the cap actually enforced; emailRequiredForSignup = true, disableRegistration = false. The per-object cap and the field's own location disagree, which is the trap.
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=1024000, policies.maxFileSizeMb=1024, maxFileSize=262144000, disableRegistration=false, emailRequiredForSignup=true, version=2026.10.0
  - [3] 2026-10-21: probe: GET -> 200, software.name=misskey, openRegistrations=true
  - [4] 2026-10-21: probe: HEAD -> 200, Content-Type: application/octet-stream, Cache-Control: max-age=31536000, immutable
  - probe:https://misskey.gg/api/meta 2026-10-22: POST /api/meta {detail:true} 2026-10-22: 200, 3,228 B; policies.driveCapacityMb 1,024,000, policies.maxFileSizeMb 1024, top-level maxFileSize 262,144,000, emailRequiredForSignup true
- sources:
  - [1] https://misskey.gg/api/meta
  - [2] https://sss.<instance>/sss/<shard>/<uuid>
  - [3] https://misskey.gg/nodeinfo/2.1
  - [4] https://sss.misskey.gg/sss/gg/ed101a7b-8b8c-4d91-b67d-cb381562323d
