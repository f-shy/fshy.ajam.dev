# data.gov.sg

> data.gov.sg | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-sg/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-sg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.sg (singapore)

- `storage/data-gov-sg` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.sg/api/3/action/package_search?rows=0
- free tier: None reachable: No longer a CKAN instance. It is a Next.js app and /api/3/action/* returns 404; there is no public register page either. Publication is by Singapore government agencies via the SingStat/Gov. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: No longer a CKAN instance — it is a Next.js app and /api/3/action/* returns 404; there is no public register page either. Publication is by Singapore government agencies via the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No longer a CKAN instance — it is a Next.js app and /api/3/action/* returns 404; there is no public register page either. Publication is by Singapore government agencies via the…
  - [2] 2026-10-21: cited as the basis of the rejection: No longer a CKAN instance — it is a Next.js app and /api/3/action/* returns 404; there is no public register page either. Publication is by Singapore government agencies via the SingStat/Gov
- sources:
  - [1] https://data.gov.sg/api/3/action/package_search?rows=0
  - [2] https://data.gov.sg/user/register
