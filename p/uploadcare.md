# Uploadcare

> uploadcare.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadcare/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadcare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uploadcare

- `storage/uploadcare-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uploadcare.com/pricing
- disagrees on identity_kind: `storage/uploadcare` says institution, `storage/uploadcare-2` says email
- free tier: none reachable: Free plan provides 10 GB storage, 25 GB traffic, 5,000 operations per month, and a 1 GB maximum file size. Operations are consumed per upload and transformation. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free plan is 10 GB storage / 25 GB traffic / 5,000 operations per month, 1 GB max file, and operations are consumed…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is 10 GB storage / 25 GB traffic / 5,000 operations per month, 1 GB max file, and operations are consumed per
- sources:
  - [1] https://uploadcare.com/pricing

## Uploadcare (free plan)

- `storage/uploadcare` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uploadcare.com
- disagrees on identity_kind: `storage/uploadcare` says institution, `storage/uploadcare-2` says email
- free tier: 1 GB storage, 1,000 operations/month, 5 GB/month traffic. Their pricing page lists operations and file-size caps rather than a storage number; 1 GB is the documented free storage allowance. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: max file size on free (1 GB | bytes: 1000000000 | source: [1] | note: not stated
- retention: CRITICAL: 'Unless the file is stored, it will be deleted after 24 hours'. API uploads are transient until explicitly stored, which costs operations. | days: 1 | source: [1] | note: not stated
- egress: 5 GB/month traffic on free, then metered. Fails free-egress. | metered: yes | free allowance: 5 GB per month
- identity: institution
- interface: s3-compatible, rest
- limits:
  - retention-clamped: deleted after 24 hours [1]
  - per-object-cap (binding): max file size on free (1 GB [1]
- limits note: 500 MB max file size on free (1 GB Pro, 10 GB Business, 5 TB Enterprise). CRITICAL: 'Unless the file is stored, it will be deleted after 24 hours'. API uploads are transient until explicitly stored, which costs operations.
- interface detail: rest
- tooling: Strong: Upload API (signed uploads), REST API, webhooks, uploading widget, File Uploader element, S3-compatible storage connect on higher tiers.
- composes with: Unlimited free projects x 1 GB. Trivially repeatable but each is tiny.
- reliability: 24-hour auto-deletion of unstored files is a data-loss trap for bulk workloads; storing each file consumes operations from a 1,000/mo pool.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB storage, 1,000 operations/month, 5 GB/month traffic. Their pricing page lists operations and file-size caps rather than a storage number; 1 GB is the documented free storage allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: '1,000 operations per month', '500 MB max file size'
  - [2] 2026-10-21: 'Unless the file is stored, it will be deleted after 24 hours'
  - [3] 2026-10-21: 'Free plan includes 1 GB storage' (third-party restatement)
- sources:
  - [1] https://uploadcare.com/pricing/
  - [2] https://uploadcare.com/docs/uploads/storage.md
  - [3] https://docs.aeroftp.app/providers/uploadcare.html
