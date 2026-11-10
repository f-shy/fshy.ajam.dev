# Datum Storage

> datum.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datum/ | JSON https://fshy.ajam.dev/api/v1/entity/datum.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Datum Storage

- `storage/datum-storage` | trial-only | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://storage.datum.org
- free tier: 1 TB free from signup ('Get 1TB Free Cloud Storage From Datum'), S3-compatible endpoint | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published on the getstarted page; sold as 'decentralized cloud storage' with S3 API compatibility (unverified per-GB) | metered: no
- identity: any-phone
- interface: s3-compatible
- limits note: 1 TB/account; requires the Datum ID mobile app on iOS/Android as the identity provider. There is no web-only path.
- interface detail: s3
- tooling: S3 API only ('designed to be compatible with the Amazon S3 API format'); tested clients Arq Backup, Duplicati/Duplicity/Duplicacy untested
- composes with: 1 TB x N identities, but each identity needs a phone-verified Datum ID, so identity cost is the multiplier
- reliability: app-gated identity makes account automation awkward; the product markets itself as early-stage ('not all [S3 clients] have been tested')
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB free from signup ('Get 1TB Free Cloud Storage From Datum'), S3-compatible endpoint
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Datum Storage accounts are attached to a Datum Identity... creating a Datum Identity will require verification of your email address and phone number'; 'designed to be compatible with the Amazon S3 API format'
  - [1] 2026-10-21: 'Datum ID on the App Store / Google Play' (no web signup path)
- sources:
  - [1] https://storage.datum.org/getstarted
