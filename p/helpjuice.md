# helpjuice

> helpjuice.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/helpjuice/ | JSON https://fshy.ajam.dev/api/v1/entity/helpjuice.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## helpjuice

- `storage/helpjuice` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.helpjuice.com/billing-subscription/is-there-are-a-storage-limit
- free tier: None reachable: 12 GB / 24 GB / 38 GB by plan is the whole storage story and there is no free plan. 'Free 14 Day Trial' only. Small and paywalled. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: read-gated
  - dead_end.why: 12 GB / 24 GB / 38 GB by plan is the whole storage story and there is no free plan — 'Free 14 Day Trial' only. Small and paywalled.
  - dead_end.retry_when: if the read path opens anonymously
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 12 GB / 24 GB / 38 GB by plan is the whole storage story and there is no free plan — 'Free 14 Day Trial' only. Small and paywalled.
  - [2] 2026-10-21: cited as the basis of the rejection: 12 GB / 24 GB / 38 GB by plan is the whole storage story and there is no free plan — 'Free 14 Day Trial' only. Small and paywalled.
- sources:
  - [1] https://help.helpjuice.com/billing-subscription/is-there-are-a-storage-limit
  - [2] https://helpjuice.com/pricing
