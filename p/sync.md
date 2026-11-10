# Sync.com

> sync.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sync/ | JSON https://fshy.ajam.dev/api/v1/entity/sync.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sync.com

- `storage/sync-com` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.sync.com/free-cloud-storage/
- free tier: 5 GB free, permanent; referral top-ups. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 5 GB storage; pull-count 3 share links; 5 devices; 30-day version history and deleted-file recovery on free. | days: 30 | source: [1] | note: not stated
- egress: Free within plan; sharing limited to 3 password-protected links and 3 team folders on free. | metered: no
- identity: email
- interface: s3, webdav, rclone
- limits note: 5 GB storage; pull-count 3 share links; 5 devices; 30-day version history and deleted-file recovery on free.
- interface detail: web + desktop clients; no S3/WebDAV on free
- tooling: official desktop/mobile clients only; no rclone backend
- composes with: 5 GB x unlimited accounts with referral bonuses. The classic multiplier, but there is no programmatic path, so each 5 GB account costs a human signup.
- reliability: E2E-encrypted, so no server-side processing; free tier is stable but tiny and sharing is deliberately constrained.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free, permanent; referral top-ups.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '5 GB free cloud storage space', 'Sync up to 5 of your own devices', 'Create up to 3 password protected links and 3 team shared folders', 'up to 30 days' version history
- sources:
  - [1] https://www.sync.com/free-cloud-storage/
