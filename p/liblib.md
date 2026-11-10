# liblibai

> liblib.art | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/liblib/ | JSON https://fshy.ajam.dev/api/v1/entity/liblib.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## liblibai (liblib.art)

- `storage/liblibai` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.liblib.art/api/www/model/getModelDownloadUrl
- free tier: none reachable: Front-end loads but every model API path 404s anonymously: POST /api/www/model/list -> 200 with body {"code":500,"msg":"服务异常，请稍后重试"} (trailing 500-in-200)… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Front-end loads but every model API path 404s anonymously: POST /api/www/model/list -> 200 with body {"code":500,"msg":"服务异常，请稍后重试"} (trailing 500-in-200)…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Front-end loads but every model API path 404s anonymously: POST /api/www/model/list -> 200 with body {"code":500,"msg":"服务异常，请稍后重试"} (trailing 500-in-200)…
- sources:
  - [1] https://www.liblib.art/api/www/model/getModelDownloadUrl
