# misskey.social

> misskey.social | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/misskey-6/ | JSON https://fshy.ajam.dev/api/v1/entity/misskey-6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## misskey.social — 50 mb drive

- `storage/misskey-social-50-mb-drive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:11.823Z (live) | stale on 2026-12-04
- url https://misskey.social/api/meta
- free tier: none reachable: Instance configuration publishes driveCapacityMb of 50 and maxFileSize of 16 MB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Live and open, but driveCapacityMb=50 and maxFileSize=16 MB. Listed to show the family's low end and that 'Misskey' does not imply 'gigabytes'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Live and open, but driveCapacityMb=50 and maxFileSize=16 MB. Listed to show the family's low end and that 'Misskey' does not imply 'gigabytes'.
  - [2] 2026-11-19: misskey.social publishes 50 MB drive capacity and a 16000000-byte file cap, with registration open and email required | capture: sha256:48a742bbcc01195ab4f289f3f5ad54a929a1cb5d92a5786b84eeeb6ddcf6d06e | quote: "driveCapacityMb":50 ... "maxFileSize":16000000 ... "disableRegistration":false ... "emailRequiredForSignup":true
- sources:
  - [1] https://misskey.social/api/meta
  - [2] https://misskey.social/api-v1/meta
