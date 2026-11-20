# 奶牛快传 cowtransfer

> sina.com.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sina/ | JSON https://fshy.ajam.dev/api/v1/entity/sina.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 奶牛快传 cowtransfer

- `storage/cowtransfer` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:11.211Z (live) | stale on 2026-12-04
- url https://finance.sina.com.cn/tech/digi/2026-01-07/doc-inhfmyct6395611.shtml
- free tier: none reachable: Shut down 2026-01-10 and wiped server data. Was the canonical 'free 40 GB, never throttled' transfer host; now simply gone. Do not let an old blog post resurrect it. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: a first-party shutdown notice states the service stopped on 2026 年 1 月 10 日 with all functions disabled and server data wiped, so the transfer host is gone
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Shut down 2026-01-10 and wiped server data. Was the canonical 'free 40 GB, never throttled' transfer host; now simply gone. Do not let an old blog post resurrect it.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Shut down 2026-01-10 and wiped server data. Was the canonical 'free 40 GB, never throttled' transfer host; now simply gone. Do not let an old blog post resurrect it.
  - [2] 2026-10-21: cited as the basis of the rejection: Shut down 2026-01-10 and wiped server data. Was the canonical 'free 40 GB, never throttled' transfer host; now simply gone. Do not let an old blog post resurrect it.
  - [1] 2026-11-19: the shutdown notice states the service stopped on 2026-01-10 with server data wiped | capture: sha256:4c5ce75911e2f474cdb0577ce387f9310a9cf3f8cd944253320dbb5f485f3582 | quote: 奶牛快传将于 2026 年 1 月 10 日起正式停止服务。届时，所有功能（包括账号登录、文件上传 / 下载、历史传输记录等）都将无法使用，服务器数据将被清除。
  - [1] 2026-11-19: a first-party shutdown notice relayed by the article states the service stopped on 2026-01-10 and that all functions and server data were removed | capture: sha256:4c5ce75911e2f474cdb0577ce387f9310a9cf3f8cd944253320dbb5f485f3582 | quote: 奶牛快传将于 2026 年 1 月 10 日起正式停止服务。届时，所有功能（包括账号登录、文件上传 / 下载、历史传输记录等）都将无法使用，服务器数据将被清除。
  - probe:https://www.cowtransfer.com/ 2026-11-19: a live probe of the site answered HTTP 405 after redirecting to cowtransfer.com, so no transfer service is served | capture: sha256:aed73d4beaeeff29e14ab49612c4a02f1a580c460264109a71cefc509cf40090 | quote: "status": 405
- sources:
  - [1] https://finance.sina.com.cn/tech/digi/2026-01-07/doc-inhfmyct6395611.shtml
  - [2] https://mp.weixin.qq.com/s/XVZ7_aN83w09kVVlGSOzCw
