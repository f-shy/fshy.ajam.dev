# bilibili

> apifox.cn | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apifox/ | JSON https://fshy.ajam.dev/api/v1/entity/apifox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bilibili as a byte store

- `storage/bilibili-as-a-byte-store` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.620Z (live) | stale on 2026-12-04
- url https://bilibili.apifox.cn/api-23693239
- free tier: none reachable: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 文件大小限制为4GB | source: [1] | note: file-size ceiling stated by the upload API documentation
- retention: not stated on the Bilibili upload API documentation page | source: [1] | note: not stated on the Bilibili upload API documentation page
- egress: not stated on the Bilibili upload API documentation page | metered: no
- identity: email
- interface: rest
- interface detail: HTTP POST upload API with a pre-processing endpoint and a chunked upload flow for larger files
- tooling: HTTP POST calls with a signed request to the upload API
- composes with: chunked upload flow feeding the submission API
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 8 GB sounds good but every upload is transcoded and content-reviewed; playback is signed m3u8. Cannot return the uploaded bytes
  - [1] 2026-11-19: Bilibili's upload endpoint specifies a file-size limit and a video duration limit, and is a video submission API rather than a byte store; the rejection stands | capture: sha256:107f93326946fe924ac80170f0aa1b10d3ff4870f1293e7a40e84a759400fbb4 | quote: 文件大小限制为4GB
  - [1] 2026-11-19: the upload uses an HTTP POST API endpoint | capture: sha256:d91c884984b62541b4fcde4e4bcd0b1f8208090f537b41974abc74be63b4feb7 | quote: POST /arcopen/fn/archive/video/init
  - [1] 2026-11-19: the upload API offers a chunked flow above 100M | capture: sha256:d91c884984b62541b4fcde4e4bcd0b1f8208090f537b41974abc74be63b4feb7 | quote: 文件超过100M时，须通过分片上传流程进行交互
  - [1] 2026-11-19: the documented tool is an HTTP client sending a signed POST | capture: sha256:d91c884984b62541b4fcde4e4bcd0b1f8208090f537b41974abc74be63b4feb7 | quote: curl --location --request POST 'https://member.bilibili.com/arcopen/fn/archive/video/init'
  - [1] 2026-11-19: the file-size limit is 4GB | capture: sha256:d91c884984b62541b4fcde4e4bcd0b1f8208090f537b41974abc74be63b4feb7 | quote: 文件大小限制为4GB
  - [1] 2026-11-19: the doc gives a video-duration limit but no retention period | capture: sha256:d91c884984b62541b4fcde4e4bcd0b1f8208090f537b41974abc74be63b4feb7 | quote: 视频时长小于5小时
- sources:
  - [1] https://bilibili.apifox.cn/api-23693239

## zhipu bigmodel files

- `storage/zhipu-bigmodel-files` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:34.054Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the first-party API doc confirms the batch 100 MB per-file and 1000-file caps | capture: sha256:ec286327298ad97849138d78a369c0ef86c851d6901f75844ff00e1953d34b03 | quote: `batch`：用于批量任务处理，支持 `.jsonl` 文件格式，，单个文件大小限制为`100 MB`，文件数不超过
- sources:
  - [1] https://s.apifox.cn/apidoc/docs-site/4012774/391224038e0
  - [2] https://docs.bigmodel.cn/api-reference/%E6%96%87%E4%BB%B6-api/%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9
