# data.boston.gov

> data.boston.gov | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-boston-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/data-boston-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.boston.gov (City of Boston, Socrata/CKAN hybrid)

- `storage/data-boston-gov` | fails-identity | evidence reported | binding none | category municipal-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.boston.gov/
- free tier: 235 datasets, 32 organisations, 0 unowned. Portal-hosted /download/ paths (tmp05gz_hzf.csv etc.). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered public GET. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: write-gated: unauth organization_create -> 'Access denied: Action organization_create'; /user/register is behind a Cloudflare 'Just a moment...' challenge (403). Organisation-only publishing.
- interface detail: CKAN action API returns 200 on package_search; the CKAN API surface is present alongside Socrata-style asset pages.
- tooling: curl.
- composes with: n/a.
- reliability: Cloudflare interstitial will block scripted registration entirely; not a viable deposit target.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 235 datasets, 32 organisations, 0 unowned. Portal-hosted /download/ paths (tmp05gz_hzf.csv etc.).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 235 sampled, 0 unowned, 32 orgs (Planning Department, Boston 311, Licensing Board)
  - [3] 2026-10-21: POST unauth — Authorization Error, 'Access denied'
  - [4] 2026-10-21: 403 'Just a moment... Enable JavaScript and cookies to continue'
- sources:
  - [1] https://data.boston.gov/
  - [2] https://data.boston.gov/api/3/action/package_search?rows=300
  - [3] https://data.boston.gov/api/3/action/organization_create
  - [4] https://data.boston.gov/user/register
