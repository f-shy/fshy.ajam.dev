# data.gov.ie

> data.gov.ie | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-ie/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-ie.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.ie (Ireland)

- `storage/data-gov-ie` | fails-identity | evidence reported | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.ie/
- free tier: 22,883 datasets, 172 organisations. No published per-user quota. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: public. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: write-gated: /user/register returns 403 'Error 403 - data.gov.ie'. Read is fully open, write is closed to the public entirely. Publishing is via the Public Bodies / Open Data Unit process.
- interface detail: CKAN 2.x action API (200 OK, package_search and organization_list both answer).
- tooling: curl.
- composes with: n/a.
- reliability: read path very healthy (largest of the CKANs probed besides Queensland); write path hard-closed at the WAF.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 22,883 datasets, 172 organisations. No published per-user quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: HTTP 200, count 22883
  - [3] 2026-10-21: live, 172 organisations enumerated
  - [4] 2026-10-21: HTTP 403, 'Error 403 - data.gov.ie'
- sources:
  - [1] https://data.gov.ie/
  - [2] https://data.gov.ie/api/3/action/package_search?rows=0
  - [3] https://data.gov.ie/api/3/action/organization_list
  - [4] https://data.gov.ie/user/register
