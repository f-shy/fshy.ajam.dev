# opendata.swiss

> opendata.swiss | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opendata/ | JSON https://fshy.ajam.dev/api/v1/entity/opendata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## opendata.swiss

- `storage/opendata-swiss` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.275Z (live) | stale on 2026-12-04
- url https://opendata.swiss/api/3/action/package_search?rows=0
- free tier: The CKAN package_search API answered with success and a dataset count of 16211; the endpoint is a dataset catalogue API, not a user file store. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: CKAN API reachable: package_search returned success with a dataset count of 16211.
- notes: The platform is operated by the Federal Statistical Office / cantonal offices and admits Swiss federal, cantonal and commun
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The platform is operated by the Federal Statistical Office / cantonal offices and admits Swiss federal, cantonal and commun
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: the platform is operated by the Federal Statistical Office / cantonal offices and admits Swiss federal, cantonal and commun
  - [2] 2026-10-21: the platform is operated by the Federal Statistical Office / cantonal offices and admits Swiss federal, cantonal and commun
  - [1] 2026-11-19: the API now returns success with a dataset count of 16211 rather than 403 | capture: sha256:8071dd5c6a4d458ecd0ccd06bea3afa512e8508b05629eb59665ae7e830921dc | quote: "success": true, "result": {"count": 16211
  - [1] 2026-11-19: the API is reachable and returns dataset metadata, re-dating the record | capture: sha256:8071dd5c6a4d458ecd0ccd06bea3afa512e8508b05629eb59665ae7e830921dc | quote: "success": true, "result": {"count": 16211
  - [1] 2026-11-19: the API is reachable with a dataset count of 16211 | capture: sha256:8071dd5c6a4d458ecd0ccd06bea3afa512e8508b05629eb59665ae7e830921dc | quote: "success": true, "result": {"count": 16211
- sources:
  - [1] https://opendata.swiss/api/3/action/package_search?rows=0
  - [2] https://opendata.swiss/user/register
