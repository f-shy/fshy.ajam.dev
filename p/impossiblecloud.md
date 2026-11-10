# Impossible Cloud

> impossiblecloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/impossiblecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/impossiblecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Impossible Cloud

- `storage/impossible-cloud` | trial-only | evidence reported | binding retention-clamped | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.impossiblecloud.com/pricing
- free tier: No free tier. '5 TB Cloud Storage Free for 30 Days' trial, then '€7.99 per TB/month' pay-as-you-go. Reserved capacity starts at 25 TB and is partners-only. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: No free tier. '5 TB Cloud Storage Free for 30 Days' trial, then '€7.99 per TB/month' pay-as-you-go. | days: 30 | source: [1] | note: not stated
- egress: 'Free egress and API calls'. 0 € egress, 0 € API fees, on paid plans. | metered: no
- identity: card
- interface: s3-compatible
- limits:
  - retention-clamped (binding): retention: 30 days [1]
- limits note: per-object-cap: 'No minimum file size or storage duration fees' (notably better than Storj). retention: 30 days (trial). Binding constraint: 30-day clock, then €7.99/TB.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: s3
- tooling: S3-compatible; positioned as drop-in S3 replacement.
- composes with: Trial-only x unlimited accounts = 5 TB re-uploaded monthly. Not storage.
- reliability: EU-only data residency and a sales-gated reserved plan; the self-serve product is pure pay-as-you-go.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier — '5 TB Cloud Storage Free for 30 Days' trial, then '€7.99 per TB/month' pay-as-you-go. Reserved capacity starts at 25 TB and is partners-only.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Pay-as-you-go €7.99 Per TB/month', 'Free egress and API calls'
  - [1] 2026-10-21: 'Start Free Trial — 5 TB Cloud Storage Free for 30 Days ... Zero egress fees'
- sources:
  - [1] https://www.impossiblecloud.com/free-trial
  - [2] https://www.impossiblecloud.com/pricing
