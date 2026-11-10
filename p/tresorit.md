# Tresorit Basic

> tresorit.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tresorit/ | JSON https://fshy.ajam.dev/api/v1/entity/tresorit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tresorit

- `storage/tresorit` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:53.247Z (inherited) | stale on 2026-11-14
- url https://tresorit.com/pricing/personal
- free tier: Tresorit Basic: 3 GB of encrypted storage, free with no expiring trial and no credit card; uploads up to 500 MB per file, sync across 2 devices and up to 10 encrypted links per month. | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: https://tresorit.com/pricing/personal lists paid plans only: Personal Lite 50 GB, Personal Essential 1 TB and Personal Pro 4 TB, each with a 14-day trial for which payment information is required.
- per-object cap: not recorded | source: [2] | note: not applicable
- retention: not recorded | source: [2]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Personal Lite plan provides 50 GB storage with a 2 GB maximum file size and 2 GB link sharing allowance. Business plans start at significantly higher monthly rates.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: Bus
  - [1] 2026-10-30: Tresorit Basic gives 3 GB of encrypted storage, 500 MB per file, 2 devices | capture: sha256:6b798f0d76b53412ac91773c5c861e602e7f3fe3b0c169f851e25bb91cf78fef | quote: It gives you the essentials: 3 GB of encrypted storage, uploads up to 500 MB per file, and syncing across 2 devices.
  - [1] 2026-10-30: Tresorit Basic is free with no expiry and no credit card | capture: sha256:6b798f0d76b53412ac91773c5c861e602e7f3fe3b0c169f851e25bb91cf78fef | quote: Yes. Tresorit Basic is completely free to use – no trials that expire, no hidden fees, and no credit card needed.
  - [2] 2026-10-30: the personal plans' 14-day trial requires payment information | capture: sha256:37ab970ac779073e56aca25e87520fa6a614b001359a040d5ff3ae58df84dea3 | quote: For security reasons, payment information is required even during the trial phase.
- sources:
  - [1] https://tresorit.com/pricing/basic
  - [2] https://tresorit.com/pricing/personal

## Tresorit Basic

- `storage/tresorit-basic` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://tresorit.com/pricing/basic
- free tier: 3 GB free, permanent (not a trial), zero-knowledge encrypted. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB per file | bytes: 500000000 | source: [1] | note: not stated
- retention: 3 GB free, permanent (not a trial), zero-knowledge encrypted | source: [1] | note: not stated
- egress: Free within plan; 10 encrypted links per month on the free tier. | metered: no
- identity: institution
- interface: s3, webdav, rclone
- limits:
  - per-object-cap (binding): 500 MB per file [1]
- limits note: per-object-cap 500 MB per file; 3 GB total; pull-count 10 encrypted links/month; 2 devices; zero-knowledge means no server-side API for bulk movement.
- interface detail: web + desktop; no S3/WebDAV
- tooling: official clients, Gmail/Outlook plugins; no rclone backend
- composes with: 3 GB x unlimited accounts, but 500 MB per-file cap and 2 devices make bulk ingest painful; the encryption is client-side, so a custom client would have to reimplement Tresorit's crypto. Not viable.
- reliability: Data is E2E encrypted with keys Tresorit does not hold. Losing credentials loses data; free tier has no recovery path beyond the local copy.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 3 GB free, permanent (not a trial), zero-knowledge encrypted.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'you get 3 GB of private, encrypted storage', 'uploads up to 500 MB per file, and syncing across 2 devices', 'You can create up to 10 encrypted links per month', 'completely free to use – no trials that expire'
- sources:
  - [1] https://tresorit.com/pricing/basic
