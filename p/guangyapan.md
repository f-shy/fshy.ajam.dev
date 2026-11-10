# 光鸭云盘

> guangyapan.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/guangyapan/ | JSON https://fshy.ajam.dev/api/v1/entity/guangyapan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 光鸭云盘 / GuangYaPan (Xunlei subsidiary)

- `netdisk-pan/guangyapan` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category consumer-pan, TV-first media drive, launched 2026-04-20
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.guangyapan.com/
- price CNY 108/yr promotional and CNY 480/yr list for 500 TB of capacity, but the 1 TB a month member egress makes a per-terabyte price meaningless
- free tier: 2 TB free at registration: '注册即享 2T 空间，会员畅享 500T 空间'. 100 GB per file free and 1 TB for members | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB per file on the free tier, 1 TB for members, with a 1,000,000-file batch transfer | bytes: 100000000000 | source: [2]
- retention: No stated expiry for stored files; a 30-day recycle bin | source: [2]
- egress: 2 GB a day of high-speed traffic on the free tier, then throttled to an undisclosed low speed. Members get 1 TB a month down and 1 TB a month up, and self-download, online playback and third-party mount all count against the same terabyte, with no overage package | metered: yes | free allowance: 2 GB per day at high speed | source: [3]
- identity: any-phone | detail: SMS only. POST /v1/auth/verification returns 400 'Email or phone_number must be set' when empty, and every email-shaped path returns 404, and the driver's own code only ever sends phone_number. So there is no email-only path
- interface: rest, webdav
- limits:
  - per-ip-shaping (binding): 2 GB a day of high-speed traffic on the free tier, then throttled [4]
  - per-object-cap: 100 GB per file on the free tier [5]
  - request-rate: 3 free offline or magnet cloud-adds a day [4]
- binding note: 2 TB of capacity is the largest free allocation in this survey after Ctfile, and 2 GB a day at high speed is. The traffic cap is what decides the plan, and as a cold archive it never binds.
- tooling: a merged OpenList driver, guangyapan, which gives WebDAV and 302 direct links once mounted; two-stage SMS login needing a client id, an X-Captcha-Token and an X-Device-Sign; CloudDrive2 v1.0.11 or later reads it
- composes with: Provides 2 TB of free storage per account with OpenList driver integration, WebDAV support, and TV streaming clients. For active content distribution, the 2 GB daily bandwidth limit is prohibitive. For cold archival storage, the daily limit does not impede initial single-pass uploads.
- reliability: Auth is SMS-only, so an account with only an email address cannot register. The OpenList docs carry an explicit danger block: use for multi-person sharing, image hosting, software hosting or video external links causes the provider to close accounts, which is the exact workload this survey targets. Xunlei's two previous netdisks both died, and the price rose from CNY 108 to 188 within months of launch
- notes: The two numbers the marketing merges are capacity and traffic, and they are ten thousand times apart in practical effect. The SMS-only registration is what closes it.
- extras:
  - access_mode: registration-gated
  - launched: 2026-04-20
  - per_file_cap_bytes_derived: 100000000000
  - aliases: 光鸭云盘 / GuangYaPan (Xunlei subsidiary 深圳市光闪云科技有限公司)
  - ban_warning: OpenList docs: sharing, image hosting, software hosting and video links cause the provider to close accounts
- evidence:
  - [1] 2026-10-21: '注册即享 2T 空间，会员畅享 500T 空间', '不限速极速上传下载', and a client list ending '下载电脑端下载移动端下载电视端'
  - [3] 2026-10-21: a six-month reality check: free 2 GB a day high speed, member 1 TB a month down and up, 'online playback and third-party mount all count toward the 1 TB', no overage package, 4K billed at full file size
  - [5] 2026-10-21: the maintained driver, '100GB 单文件上传', and the closure warning for hosting workloads
  - [6] 2026-10-21: launch coverage: '永久免费 2TB', '100GB 单文件上传及 100 万文件批量转存'
  - probe:POST https://account.guangyapan.com/v1/auth/verification 2026-10-21: 400 with {"error":"invalid_argument","error_description":"Email or phone_number must be set"}; the email variant returned 404 not_found; /v1/auth/email/register returned 404
  - probe:GET https://api.guangyapan.com/v1/user/info 2026-10-21: HTTP 410 with {"code":128,"msg":"路径不允许访问"}, so the old path is closed and it says so
- sources:
  - [1] https://www.guangyapan.com/
  - [2] https://app.guangyapan.com/pan
  - [3] https://post.smzdm.com/p/a82plxq0/
  - [4] https://www.freeaday.com/2026/04/guangyapan/
  - [5] https://docs.oplist.org/guide/drivers/guangyapan
  - [6] https://www.ithome.com/0/941/203.htm
