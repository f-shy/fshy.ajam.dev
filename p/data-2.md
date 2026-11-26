# data.govt.nz

> data.govt.nz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-2/ | JSON https://fshy.ajam.dev/api/v1/entity/data-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.govt.nz (New Zealand)

- `storage/data-govt-nz` | fails-identity | evidence inferred | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://data.govt.nz/
- free tier: CKAN API answers 200 but the payload is replaced by an Incapsula/Imperva JS challenge wrapper on the HTML side; dataset count not machine-readable through this path. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: public. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Identity gate not determinable. /user/register returned 200 but with the Incapsula interstitial. Publishing on data.govt.nz is for NZ government agencies under the NZ Data Catalogue / open-data programme.
- interface detail: CKAN 2.x action API (partially reachable).
- tooling: curl (API), browser (UI).
- composes with: n/a.
- reliability: unverified: blocked by challenge (Incapsula).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: CKAN API answers 200 but the payload is replaced by an Incapsula/Imperva JS challenge wrapper on the HTML side; dataset count not machine-readable through this path.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: HTTP 200
  - [3] 2026-10-21: HTTP 200 but body is '<META NAME="robots" CONTENT="noindex,nofollow"><script src="/_Incapsula_Resource?..."' challenge page
- sources:
  - [1] https://data.govt.nz/
  - [2] https://data.govt.nz/api/3/action/package_search?rows=0
  - [3] https://data.govt.nz/user/register
