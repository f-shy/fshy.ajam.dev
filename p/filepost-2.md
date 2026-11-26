# filepost

> filepost.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filepost-2/ | JSON https://fshy.ajam.dev/api/v1/entity/filepost-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## filepost / filepost.jp / filepost.com

- `storage/filepost-filepost-jp-filepost-com` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:38.131Z (inherited) | stale on 2026-12-04
- url https://filepost.jp/
- free tier: none reachable: Endpoint filepost.jp returns HTTP 504 with no active upload interface. Endpoint filepost.com operates as an advertising redirect portal. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Two separate corpses. filepost.jp returns 504 through the reader and has no live upload surface; Also note the
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Two separate corpses. filepost.jp returns 504 through the reader and has no live upload surface; Also note the
  - [2] 2026-10-21: cited as the basis of the rejection: Two separate corpses. filepost.jp returns 504 through the reader and has no live upload surface; Also note the
  - probe:https://filepost.jp/ 2026-11-19: the first-party host returned HTTP 403 to a direct probe on 2026-11-19 with an expired certificate | capture: sha256:aae79801da718ceacab3082537e08ea81fe98a8572d4a7512dc4549db20eb9fb | quote: "status": 403
  - probe:https://filepost.jp/ 2026-11-19: the direct probe recorded an http-403 error for the first-party host on 2026-11-19 | capture: sha256:aae79801da718ceacab3082537e08ea81fe98a8572d4a7512dc4549db20eb9fb | quote: "error": "http-403"
- sources:
  - [1] https://filepost.jp/
  - [2] http://muryo.net/storage/
