# data.gov.ie

> data.gov.ie | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-ie/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-ie.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.ie (Ireland)

- `storage/data-gov-ie` | fails-identity | evidence reported | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:30.233Z (live) | stale on 2026-12-04
- url https://data.gov.ie/
- free tier: 23,002 datasets, 172 organisations. No published per-user quota. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
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
- notes: 22,883 datasets, 172 organisations. No published per-user quota.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 22,883 datasets, 172 organisations. No published per-user quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: HTTP 200, count 22883
  - [3] 2026-10-21: live, 172 organisations enumerated
  - [4] 2026-10-21: HTTP 403, 'Error 403 - data.gov.ie'
  - [2] 2026-11-19: the CKAN API reports 23,002 datasets today | capture: sha256:a934e3d63b7aa6095cf7eda4503b642e3684a6e9fa92b9dc62eb85b1f2a48e01 | quote: "count": 23002
  - [3] 2026-11-19: the organization list endpoint answers successfully and enumerates the organisations | capture: sha256:3540a1cbbd2e946778fcf0f67ee9831dd7e258b53091c491cae25e6c6b1c764b | quote: "success": true, "result": ["3d", "adaptcentre", "an-coimisun-pleanala"
  - [4] 2026-11-19: the registration page states users are not authorised to register, so public write stays closed | capture: sha256:8f346e9dbcb1de33044e232e310f1127c4c97955a7be128bbb2bc6bf2eea0800 | quote: Unauthorised to register as a user.
- sources:
  - [1] https://data.gov.ie/
  - [2] https://data.gov.ie/api/3/action/package_search?rows=0
  - [3] https://data.gov.ie/api/3/action/organization_list
  - [4] https://data.gov.ie/user/register
