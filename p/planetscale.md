# PlanetScale

> planetscale.com | Databases and KV, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/planetscale/ | JSON https://fshy.ajam.dev/api/v1/entity/planetscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PlanetScale (Databases and KV)

- `databases-kv/planetscale` | dead | evidence documented | binding write-gated | category managed MySQL
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://support.planetscale.com/hc/en-us/articles/32303734121239
- free tier: none. No free plan; every database must be on a paid plan from creation | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: there is no free tier to cap
- retention: not applicable; a paid database accrues charges from creation until it is deleted | source: [1]
- egress: network transfer is billed separately from the SKU rate | metered: yes | source: [2]
- identity: card | detail: a payment method, because the cheapest database is billable at creation
- interface: rest, cli
- limits:
  - write-gated (binding): every database is paid from creation; no free tier exists [1]
- interface detail: the MySQL wire protocol; a platform API and the pscale CLI
- tooling: any MySQL client, the pscale CLI
- composes with: no path on a zero budget; cheapest published SKU is PS-10 arm64 at USD 30 a month
- reliability: the Hobby plan was deprecated in March 2024 and remaining databases were slept; a 24-hour wake was offered to dump data
- notes: Every 'PlanetScale free tier' listicle is describing a plan that closed in March 2024.
- evidence note: PlanetScale's own support answer and its plans doc were read.
- evidence:
  - [1] 2026-10-22: 'Not at this time.' The free Hobby plan was deprecated in March 2024; all databases must be placed on a paid Scaler Pro plan when created
  - [3] 2026-10-22: 'PlanetScale does not offer a free plan, previously known as the Developer or Hobby plan'
  - [2] 2026-10-22: cheapest published SKU PS-10 arm64 1/8 vCPU 1 GiB at USD 30 a month, x86-64 at USD 39
- sources:
  - [1] https://support.planetscale.com/hc/en-us/articles/32303734121239
  - [2] https://www.planetscale.com/pricing
  - [3] https://planetscale.com/docs/planetscale-plans

## planetscale (Storage)

- `storage/planetscale` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://planetscale.com/docs/plans/hobby-plan-deprecation-faq
- free tier: none reachable: Free tier is GONE, confirmed on their own docs: 'PlanetScale does not offer a free plan, previously known as the "Developer" or "Hobby" plan.' Cheapest entry is a $5/month single-node… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Free tier is GONE, confirmed on their own docs: 'PlanetScale does not offer a free plan, previously known as the "Developer" or "Hobby" plan.' Cheapest entry is a $5/month single-node…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free tier is GONE, confirmed on their own docs: 'PlanetScale does not offer a free plan, previously known as the "Developer" or "Hobby" plan.' Cheapest entry is a $5/month single-node…
  - [2] 2026-10-21: cited as the basis of the rejection: Free tier is GONE, confirmed on their own docs: 'PlanetScale does not offer a free plan, previously known as the "Developer" or "Hobby" plan.' Cheapest entry is a $5/month single-node Postgr
- sources:
  - [1] https://planetscale.com/docs/plans/hobby-plan-deprecation-faq
  - [2] https://planetscale.com/pricing
