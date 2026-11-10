# data.gov.ua

> data.gov.ua | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-ua/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-ua.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.ua (Ukraine national portal)

- `storage/data-gov-ua` | fails-identity | evidence reported | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.ua/
- free tier: No published quota. Files self-hosted at /dataset/<uuid>/resource/<uuid>/download/<file>. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered public GET. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Write-gated: registration is open (email + password form renders 200) but unauth organization_create returns 'У доступі відмовлено'. A 300-dataset sample contained ZERO datasets with an empty owner_org. Every record belongs to a ministry, state enterprise or register authority. That is the structural proof that this is a publishers-only catalog.
- interface detail: CKAN 2.x action API (200 OK).
- tooling: curl + CKAN key; UI at /dataset/new.
- composes with: N/a. No individual write path.
- reliability: operational through wartime; stable API. Same consumer-vs-publisher split as every other national CKAN.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published quota. Files self-hosted at /dataset/<uuid>/resource/<uuid>/download/<file>.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 300 sampled, 0 with empty owner_org, 124 distinct organisations (Національна поліція України, ДП «СЕТАМ», etc.)
  - [3] 2026-10-21: POST (unauthenticated) — success:false, access-denied message
  - [4] 2026-10-21: resources at /dataset/.../download/licplatewanted.json, i.e. portal-hosted bytes
- sources:
  - [1] https://data.gov.ua/pages/pro-portal
  - [2] https://data.gov.ua/api/3/action/package_search?rows=300
  - [3] https://data.gov.ua/api/3/action/organization_create
  - [4] https://data.gov.ua/api/3/action/package_search?rows=1
