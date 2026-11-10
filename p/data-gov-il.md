# data.gov.il

> data.gov.il | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-il/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-il.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.il (Israel, CKAN)

- `storage/data-gov-il` | fails-identity | evidence reported | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.il/
- free tier: 1,203 datasets, 61 organisations. Files self-hosted (/dataset/.../download/datafile.csv). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: public. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: write-gated: /user/register returns CloudFront 'Request blocked' 403; organization_create POST falls through to the Hebrew HTML app shell rather than a JSON API, i.e. no exposed write endpoint.
- interface detail: CKAN 2.x action API (200 OK).
- tooling: curl.
- composes with: n/a.
- reliability: government-mandated publication by ministries; no individual channel.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1,203 datasets, 61 organisations. Files self-hosted (/dataset/.../download/datafile.csv).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 200, count 1203
  - [3] 2026-10-21: 61 organisations
  - [4] 2026-10-21: 403 'The request could not be satisfied / Request blocked'
- sources:
  - [1] https://data.gov.il/
  - [2] https://data.gov.il/api/3/action/package_search?rows=0
  - [3] https://data.gov.il/api/3/action/organization_list
  - [4] https://data.gov.il/user/register
