# Xata

> xata.io | Databases and KV, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xata/ | JSON https://fshy.ajam.dev/api/v1/entity/xata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xata (Databases and KV)

- `databases-kv/xata` | trial-only | evidence documented | binding retention-clamped | category managed Postgres with branching
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://xata.io/pricing
- price USD 0.28/GB-month storage, micro compute USD 9/month equivalent | parsed USD 280/TB-mo
- free tier: no free tier; Xata Cloud starts with a 14-day free trial, then pay as you go | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: the open-source core is free to self-host and is a different product from Xata Cloud
- per-object cap: not applicable: the trial bills by branch-hour and GB-month rather than capping an object
- retention: the trial ends after 14 days; a credit card is required after it to keep the database | days: 14 | source: [1]
- egress: not published on the pricing page; recorded as a gap | metered: no | source: [1]
- identity: card | detail: email for the trial; a credit card after it to stay on pay as you go
- interface: rest, cli
- limits:
  - retention-clamped (binding): 14-day trial; the always-free 15 GB tier is retired [1]
- interface detail: Postgres wire protocol plus an HTTP data API and a CLI
- tooling: psql and any Postgres client; the xata CLI
- composes with: no path: a 14-day trial cannot anchor a workload that has to outlive a fortnight
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: Any corpus that still lists Xata's 15 GB always-free tier is describing a plan that no longer exists.
- evidence note: the pricing page states the 14-day trial in its own FAQ answer; the 15 GB free tier that aggregators still print is not on the page.
- evidence:
  - [1] 2026-10-22: 'Open source is free forever. Xata Cloud starts with a 14-day free trial. Add a credit card after the trial to keep using Xata on Pay As You Go'; micro instance USD 0.012/hr, storage USD 0.28/GB-month
- sources:
  - [1] https://xata.io/pricing

## xata (Storage)

- `storage/xata` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://xata.io/pricing.md
- free tier: none reachable: Explicitly no free tier. Xata Cloud is a 14-day trial then $0.012/hr compute + $0.28/GB/mo storage. The open-source engine is Apache 2.0 (self-host only, no hosted storage). | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: Explicitly no free tier. Xata Cloud is a 14-day trial then $0.012/hr compute + $0.28/GB/mo storage. The open-source engine is Apache 2.0 (self-host only, no hosted storage).
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly no free tier. Xata Cloud is a 14-day trial then $0.012/hr compute + $0.28/GB/mo storage. The open-source engine is Apache 2.0 (self-host only, no hosted storage).
- sources:
  - [1] https://xata.io/pricing.md
