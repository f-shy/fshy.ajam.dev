# verypan

> verypan.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/verypan/ | JSON https://fshy.ajam.dev/api/v1/entity/verypan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## verypan (yun.verypan.com)

- `storage/verypan` | fails-identity | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID yes, institution no | verified 2026-11-19T21:15:24.519Z (live) | stale on 2026-12-04
- url https://yun.verypan.com/
- free tier: none reachable: Advertises unlimited storage ('∞ 存储容量') but caps a single file at 500 MB and requires 实名认证 (real-name identity verification) to upload at all. 500 MB x unlimited is a 40,000-object TiB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: national-id | detail: 实名认证 (real-name identity verification) is required for full upload and sharing ability: 注册账号并完成实名认证，享受完整上传与分享能力。
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: Advertises unlimited storage ('∞ 存储容量') but caps a single file at 500 MB and requires 实名认证 (real-name identity verification) to upload at all. 500 MB x unlimited is a 40,000-object TiB.
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Advertises unlimited storage ('∞ 存储容量') but caps a single file at 500 MB and requires 实名认证 (real-name identity verification) to upload at all. 500 MB x unlimited is a 40,000-object TiB.
  - [1] 2026-11-19: the first-party page requires real-name (national-id) verification to gain full upload and sharing ability | capture: sha256:cda874011b57cd0e8ccb5b4f5379f7e4bfce1e49f4d043f57093256eb84f91bd | quote: 注册账号并完成实名认证，享受完整上传与分享能力。
  - [1] 2026-11-19: the stated identity requirement is real-name verification | capture: sha256:cda874011b57cd0e8ccb5b4f5379f7e4bfce1e49f4d043f57093256eb84f91bd | quote: 注册账号并完成实名认证，享受完整上传与分享能力。
  - [1] 2026-11-19: real-name verification is the stated identity gate | capture: sha256:cda874011b57cd0e8ccb5b4f5379f7e4bfce1e49f4d043f57093256eb84f91bd | quote: 注册账号并完成实名认证，享受完整上传与分享能力。
  - [1] 2026-11-19: a single file is still capped at 500MB | capture: sha256:cda874011b57cd0e8ccb5b4f5379f7e4bfce1e49f4d043f57093256eb84f91bd | quote: 支持任意类型文件，单文件最大 500MB，分块上传断点续传。
- sources:
  - [1] https://yun.verypan.com/
