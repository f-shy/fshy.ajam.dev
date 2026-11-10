# bilibili

> apifox.cn | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apifox/ | JSON https://fshy.ajam.dev/api/v1/entity/apifox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bilibili as a byte store

- `storage/bilibili-as-a-byte-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bilibili.apifox.cn/api-23693239
- free tier: none reachable: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes
- sources:
  - [1] https://bilibili.apifox.cn/api-23693239

## zhipu bigmodel files

- `storage/zhipu-bigmodel-files` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://s.apifox.cn/apidoc/docs-site/4012774/391224038e0
- free tier: none reachable: Batch files are capped at 100 MB per file and 1,000 files total. File extraction is capped at 50 MB. Content downloads are supported only for batch files. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Batch purpose capped at 100 MB/file and 1,000 files; file-extract capped at 50 MB. Content download only supported for `batch` type.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Batch purpose capped at 100 MB/file and 1,000 files; file-extract capped at 50 MB. Content download only supported for `batch` type.
  - [2] 2026-10-21: cited as the basis of the rejection: Batch purpose capped at 100 MB/file and 1,000 files; file-extract capped at 50 MB. Content download only supported for `batch` type.
- sources:
  - [1] https://s.apifox.cn/apidoc/docs-site/4012774/391224038e0
  - [2] https://docs.bigmodel.cn/api-reference/%E6%96%87%E4%BB%B6-api/%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9
