# kartaview

> openstreetcam.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openstreetcam/ | JSON https://fshy.ajam.dev/api/v1/entity/openstreetcam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## kartaview (openstreetcam, grab)

- `storage/kartaview` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://api.openstreetcam.org/2.0/photo/?itemsPerPage=2
- free tier: None reachable: Read API is closed to unauthenticated clients: `GET /2.0/photo/?itemsPerPage=2` returns HTTP 200 with the body {"apiCode":400,"apiMessage":"Restricted access!"}. A 200 carrying an error, ex. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Read API is closed to unauthenticated clients: `GET /2.0/photo/?itemsPerPage=2` returns HTTP 200 with the body {"apiCode":400,"apiMessage":"Restricted access!"} — a 200 carrying an error…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Read API is closed to unauthenticated clients: `GET /2.0/photo/?itemsPerPage=2` returns HTTP 200 with the body {"apiCode":400,"apiMessage":"Restricted access!"} — a 200 carrying an error…
  - [2] 2026-10-21: cited as the basis of the rejection: Read API is closed to unauthenticated clients: `GET /2.0/photo/?itemsPerPage=2` returns HTTP 200 with the body {"apiCode":400,"apiMessage":"Restricted access!"} — a 200 carrying an error, ex
  - [3] 2026-10-21: cited as the basis of the rejection: Read API is closed to unauthenticated clients: `GET /2.0/photo/?itemsPerPage=2` returns HTTP 200 with the body {"apiCode":400,"apiMessage":"Restricted access!"} — a 200 carrying an error, ex
- sources:
  - [1] https://api.openstreetcam.org/2.0/photo/?itemsPerPage=2
  - [2] https://github.com/koito19960406/ZenSVI/issues/146
  - [3] https://www.trekview.org/blog/playing-with-kartaview-api/
