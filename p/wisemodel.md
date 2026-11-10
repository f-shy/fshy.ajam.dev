# wisemodel

> wisemodel.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wisemodel/ | JSON https://fshy.ajam.dev/api/v1/entity/wisemodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wisemodel (wisemodel.cn)

- `storage/wisemodel` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wisemodel.cn/DeepSeek/DeepSeek-V3.git/info/refs?service=git-upload-pack
- free tier: none reachable: Public model catalog index returns HTTP 200, but individual model detail pages and Git LFS endpoints returned HTTP 504 gateway timeout on 2026-10-21. Model downloads require authentication. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Reads are Chinese-market and mostly login-gated for the interesting parts: /models -> 200, but every model detail page returned 504 through the reader (2 attempts), the git LFS ref
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Reads are Chinese-market and mostly login-gated for the interesting parts: /models -> 200, but every model detail page returned 504 through the reader (2 attempts), the git LFS ref
- sources:
  - [1] https://wisemodel.cn/DeepSeek/DeepSeek-V3.git/info/refs?service=git-upload-pack
