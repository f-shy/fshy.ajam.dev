# data.qld.gov.au

> data.qld.gov.au | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-qld-gov-au/ | JSON https://fshy.ajam.dev/api/v1/entity/data-qld-gov-au.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.qld.gov.au (Queensland Open Data Portal)

- `storage/data-qld-gov-au` | fails-identity | evidence reported | binding none | category municipal-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.data.qld.gov.au/
- free tier: 188,887 datasets. No published per-user or per-file quota. Resources split between portal-hosted /download/ paths and agency app endpoints (apps.des.qld.gov.au). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered public GET. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated: invite restriction, and the page title is 'Register - Open Data Portal | Queensland Go [1]
- limits note: The most open registration form found in the whole survey. /user/register accepts only Username, Displayed name, Email, Password, with no domain or invite restriction, and the page title is 'Register - Open Data Portal | Queensland Government'. But a self-registered account still lands with no organisation, and publishing is governed by the Queensland Government data-publishing standards for agencies. Unauthenticated organization_create returned an empty body (not a clean denial), so treat the write path as unproven rather than open.
- interface detail: CKAN 2.x action API (200 OK).
- tooling: curl + CKAN key.
- composes with: n/a.
- reliability: large, well-maintained state portal; the account is a 'request data / follow datasets' account, not a publisher account.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 188,887 datasets. No published per-user or per-file quota. Resources split between portal-hosted /download/ paths and agency app endpoints (apps.des.qld.gov.au).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: form fields: Username, Displayed name, Email, Password, Confirm; no invite code, no .gov.au restriction
  - [3] 2026-10-21: 200, count 188887, resource at /dataset/.../download/cds-nrt-storm-tide-data-.txt
  - [4] 2026-10-21: POST unauth — empty response body, so no positive signal of an open write path
- sources:
  - [1] https://www.data.qld.gov.au/
  - [2] https://www.data.qld.gov.au/user/register
  - [3] https://data.qld.gov.au/api/3/action/package_search?rows=1
  - [4] https://data.qld.gov.au/api/3/action/organization_create
