# misskey.art

> misskey.art | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey-2/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.art — 5 GiB per user, 250 MiB per object

- `storage/misskey-art-5-gib-per-user-250-mib-per-object` | fails-quota | evidence reported | binding per-object-cap | category fediverse-misskey
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:11.822Z (live) | stale on 2026-12-04
- url https://misskey.art
- free tier: 5120 MB = 5 GiB per user; maxFileSize 250 MiB. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free CDN. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 250 MiB [1]
- limits note: per-object-cap 250 MiB; per-user 5 GiB.
- interface detail: rest
- tooling: Misskey API / MiAuth.
- composes with: Open registration (email required). Art-focused instance so large uploads are normal traffic, less likely to trigger usage-anomaly detection.
- reliability: Live, open, art community.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5120 MB = 5 GiB per user; maxFileSize 250 MiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: POST -> 200, policies.driveCapacityMb=5120, maxFileSize=262144000, disableRegistration=false, version 2026.10.0-art+4.0
  - [2] 2026-11-19: Misskey.art publishes 5120 MB drive capacity and a 262144000-byte file cap, with registration open and email required | capture: sha256:1fe4f9a0b7f20495f824ccc004ecba649f790854886475f7a142d45fae7c524b | quote: "driveCapacityMb":5120 ... "maxFileSize":262144000 ... "disableRegistration":false ... "emailRequiredForSignup":true
- sources:
  - [1] https://misskey.art/api/meta
  - [2] https://misskey.art/api-v1/meta
