# circle

> circle.so | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/circle/ | JSON https://fshy.ajam.dev/api/v1/entity/circle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## circle

- `storage/circle` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:07.130Z (live) | stale on 2026-12-04
- url https://help.circle.so/p/administration/site-management/community-storage
- free tier: None reachable: Paid-only. Storage is 200 GB (Professional) / 500 GB (Business) / 1 TB (Scale, Plus), starting at $89/mo after a 14-day trial, and overage is auto-billed at $10/month per 50 GB block. The o. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Paid-only — storage is 200 GB (Professional) / 500 GB (Business) / 1 TB (Scale, Plus), starting at $89/mo after a 14-day trial, and overage is auto-billed at $10/month per 50 GB block. The…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Paid-only — storage is 200 GB (Professional) / 500 GB (Business) / 1 TB (Scale, Plus), starting at $89/mo after a 14-day trial, and overage is auto-billed at $10/month per 50 GB block. The…
  - [2] 2026-10-21: cited as the basis of the rejection: Paid-only — storage is 200 GB (Professional) / 500 GB (Business) / 1 TB (Scale, Plus), starting at $89/mo after a 14-day trial, and overage is auto-billed at $10/month per 50 GB block. The o
  - [1] 2026-11-19: storage tiers 200 GB/500 GB/1 TB/1 TB are unchanged, matching the recorded paid-only figures | capture: sha256:4ce7492068b192f790ae359188420e7422b4a1edef5aa2953f42d3b412dddc75 | quote: - Professional: 200 GB - Business: 500 GB - Scale: 1TB - Plus: 1TB
  - [2] 2026-11-19: plans are paid with a 14-day trial and no card required to start, matching the recorded paid-only rejection | capture: sha256:52443f882762d974ba5e4721e1dcc60aeafc71b3304ada1c5f8092e2ffaf26a4 | quote: Start your free 14-day trial today. No credit card required.
- sources:
  - [1] https://help.circle.so/p/administration/site-management/community-storage
  - [2] https://circle.so/pricing
