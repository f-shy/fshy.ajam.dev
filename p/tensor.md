# tensorart

> tensor.art | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensor/ | JSON https://fshy.ajam.dev/api/v1/entity/tensor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tensorart

- `storage/tensorart` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.961Z (live) | stale on 2026-11-19
- url https://tensor.art/
- disagrees on verdict: `storage/tensorart` says fails-egress, `storage/tensorart-2` says fails-quota
- free tier: none reachable: Bot-walled beyond use: tensor.art/ returns 403 with the extraction flagging paywall:status, /models likewise, /upload returns 422. Its landing page claims 'model hosting' but no limits page | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: unverified: the landing page, the models page and the terms page read on 2026-11-03 state no storage, bandwidth or egress figure | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: no limits page found on tensor.art/, /models or the terms page; /upload shows 'This content is unavailable' to an anonymous read
- notes: part of the free tier
- evidence note: read 2026-11-03: https://tensor.art/ answered and shows no storage, bandwidth or egress figure; the /models and /upload pages were not read, so the read-gated verdict carries the 2026-10-21 evidence rows only.
- extras:
  - dead_end.failure_class: read-gated
  - dead_end.why: Bot-walled beyond use: tensor.art/ returns 403 with the extraction flagging paywall:status, /models likewise, /upload returns 422. Its landing page claims 'model hosting' but no limits page
  - dead_end.retry_when: if the read path opens anonymously
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Bot-walled beyond use: tensor.art/ returns 403 with the extraction flagging paywall:status, /models likewise, /upload returns 422. Its landing page claims 'model hosting' but no limits page
  - [2] 2026-10-21: cited as the basis of the rejection: Bot-walled beyond use: tensor.art/ returns 403 with the extraction flagging paywall:status, /models likewise, /upload returns 422. Its landing page claims 'model hosting' but no limits page
  - [3] 2026-10-21: cited as the basis of the rejection: Bot-walled beyond use: tensor.art/ returns 403 with the extraction flagging paywall:status, /models likewise, /upload returns 422. Its landing page claims 'model hosting' but no limits page
  - [1] 2026-11-03: the landing page read with HTTP 200 and lists no storage, bandwidth or egress figure | capture: sha256:90b6a04c24bae691bc3a9d29b7d1f69761c5753ff3c749385fbc74bc90b0f913 | quote: # Tensor.Art
  - [1] 2026-11-04: the landing page was read and carries no storage, bandwidth or egress figure | capture: sha256:5fd99bfc7e187d604bb02bc2dda00c5f5a848a7fc1552914f23f303f3b120493 | quote: # Tensor.Art
- sources:
  - [1] https://tensor.art/
  - [2] https://tensor.art/models
  - [3] https://tensor.art/upload

## tensorart (tensor.art)

- `storage/tensorart-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://tensor.art/models/806909589372248366
- disagrees on verdict: `storage/tensorart` says fails-egress, `storage/tensorart-2` says fails-quota
- free tier: api.tensor.art returns HTTP 405 with a JSON body… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Api.tensor.art returns HTTP 405 with a JSON body…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Api.tensor.art returns HTTP 405 with a JSON body…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: api.tensor.art returns HTTP 405 with a JSON body {"code":200
  - [2] 2026-10-21: api.tensor.art returns HTTP 405 with a JSON body {"code":200
  - [3] 2026-10-21: api.tensor.art returns HTTP 405 with a JSON body {"code":200
- sources:
  - [1] https://tensor.art/models/806909589372248366
  - [2] https://api.tensor.art/v1/model/detail
  - [3] https://tensor.art/api/v1/model/download/806909589372248366
