# Impossible Cloud

> impossiblecloud.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/impossiblecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/impossiblecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Impossible Cloud

- `storage/impossible-cloud` | trial-only | evidence reported | binding retention-clamped | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:01.149Z (live) | stale on 2026-12-04
- url https://www.impossiblecloud.com/pricing
- free tier: No free tier. '5 TB Cloud Storage Free for 30 Days' trial, then '€7.99 per TB/month' pay-as-you-go. Reserved capacity starts at 25 TB and is partners-only. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: No free tier. '5 TB Cloud Storage Free for 30 Days' trial, then '€7.99 per TB/month' pay-as-you-go. | days: 30 | source: [1] | note: not stated
- egress: 'Free egress and API calls'. 0 € egress, 0 € API fees, on paid plans. | metered: no
- identity: anonymous | detail: the free-trial page states 'No credit card or commitment required', so the trial is available without a card
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
  - [1] 2026-11-19: the free-trial page states 5 TB free for 30 days | capture: sha256:5841246693dbfd745a0ce96f4578ebc2b6f411629747b9da084a4e751a875808 | quote: Instant access to 5TB free for 30 days
  - [2] 2026-11-19: the pricing page states EUR 7.99 per TB per month | capture: sha256:eab3d66ac4e3f0381e1a5865a2f9a29e33d77d14700df4331090dfa4aad11a97 | quote: €7.99 per TB/month
  - [2] 2026-11-19: egress and API calls are free | capture: sha256:eab3d66ac4e3f0381e1a5865a2f9a29e33d77d14700df4331090dfa4aad11a97 | quote: Free egress and API calls
  - [3] 2026-11-19: the product is an S3-compatible storage API | capture: sha256:c4513a9f8d2cf344c7d39a0cd94a36ad1ee9d8c005ab192daf1826d380e3489f | quote: S3-compatible storage API
  - [1] 2026-11-19: the trial requires no credit card | capture: sha256:5841246693dbfd745a0ce96f4578ebc2b6f411629747b9da084a4e751a875808 | quote: No credit card or commitment required
- sources:
  - [1] https://www.impossiblecloud.com/free-trial
  - [2] https://www.impossiblecloud.com/pricing
  - [3] https://www.impossiblecloud.com/start-building
