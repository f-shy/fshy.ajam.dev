# data.gov.ro

> data.gov.ro | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-ro/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-ro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.ro (Romania national portal)

- `storage/data-gov-ro` | fails-identity | evidence reported | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.ro/
- free tier: 5,255 datasets across 181 organisations. Files are hosted on-portal, not linked out: resources resolve to /dataset/<uuid>/resource/<uuid>/download/<name>.xls. No per-user quota is published. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered public GET on the download path, no token, no egress metering. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: write-gated at the organisation level. `/user/register` is a plain open form (username, full name, email, password) with NO invitation code, but `POST /api/3/action/organization_create` unauthenticated returns `Acces interzis: Action organization_create is not authorized`. Publishing is per the national Law 179/2022 open-data regime, i.e. public bodies.
- interface detail: CKAN 2.x action API, fully live (package_search returns 200).
- tooling: curl + CKAN API key. Session-based upload via /dataset/new.
- composes with: None meaningful. The write path is not reachable without an institutional organisation.
- reliability: state-run, stable, but the account you can create is a consumer account: it grants no organisation, and a dataset with no owner_org is not creatable by a non-sysadmin.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5,255 datasets across 181 organisations. Files are hosted on-portal, not linked out: resources resolve to /dataset/<uuid>/resource/<uuid>/download/<name>.xls. No per-user quota is published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: HTTP 200, count 5255; resource URLs are https://data.gov.ro/dataset/.../download/... i.e. self-hosted bytes
  - [3] 2026-10-21: HTTP 200, plain form: Username / Nume complet / E-mail / Parolă / Confirmare, no invite field
  - [4] 2026-10-21: POST (unauthenticated) — {"success": false, "error": {"message": "Acces interzis: Action organization_create"}}
- sources:
  - [1] https://data.gov.ro/pages/publish
  - [2] https://data.gov.ro/api/3/action/package_search?rows=1
  - [3] https://data.gov.ro/user/register
  - [4] https://data.gov.ro/api/3/action/organization_create
