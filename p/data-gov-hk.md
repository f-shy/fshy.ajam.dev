# data.gov.hk

> data.gov.hk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-hk/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-hk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.hk (hong kong) and data.gov.tw (taiwan)

- `storage/data-gov-hk-and-data-gov-tw` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:43.469Z (inherited) | stale on 2026-12-04
- url https://data.gov.hk/api/3/action/package_search?rows=0
- free tier: none reachable: Neither exposes the CKAN action API (404 on package_search) and both have no /user/register route. Data.Gov.HK is a DATA.GOV.HK publishing platform for bureaux and departments; data.gov.tw… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Neither exposes the CKAN action API (404 on package_search) and both have no /user/register route. Data.Gov.HK is a DATA.GOV.HK publishing platform for bureaux and departments; data.gov.tw…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Neither exposes the CKAN action API (404 on package_search) and both have no /user/register route. Data.Gov.HK is a DATA.GOV.HK publishing platform for bureaux and departments; data.gov.tw…
  - [2] 2026-10-21: cited as the basis of the rejection: Neither exposes the CKAN action API (404 on package_search) and both have no /user/register route. Data.Gov.HK is a DATA.GOV.HK publishing platform for bureaux and departments; data.gov.tw i
  - probe:https://data.gov.hk/api/3/action/package_search?rows=0 2026-11-19: the CKAN action API endpoint is not exposed on data.gov.hk today | capture: sha256:39e54bcbf3db773f2bdb5e64ad23ee9183db3bc350cc6e53ed8fa235114ad6e3 | quote: "status": 404
  - probe:https://data.gov.tw/api/3/action/package_search?rows=0 2026-11-19: the CKAN action API endpoint is not exposed on data.gov.tw today | capture: sha256:aee279fb1b25ea747c3c01a5ac888b8dbff9a62a4672f5aca8478db1a1b2bf15 | quote: "status": 404
  - probe:https://data.gov.hk/api/3/action/package_search?rows=0 2026-11-19: the CKAN action API endpoint on data.gov.hk is gone today | capture: sha256:39e54bcbf3db773f2bdb5e64ad23ee9183db3bc350cc6e53ed8fa235114ad6e3 | quote: "status": 404
- sources:
  - [1] https://data.gov.hk/api/3/action/package_search?rows=0
  - [2] https://data.gov.tw/api/3/action/package_search?rows=0
