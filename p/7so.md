# 七嗖云盘

> 7so.top | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/7so/ | JSON https://fshy.ajam.dev/api/v1/entity/7so.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 七嗖云盘 / 长青云盘 (7so.top)

- `storage/provider` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:06.369Z (live) | stale on 2026-12-04
- url https://cloud.7so.top/api/v3/site/config
- free tier: none reachable: Marketed as 1 TB free with WebDAV; its own Cloudreve site config now returns title '长青云盘·11月19下线' (shutting down Nov 19) and registerEnabled=false. Dead mid-flight. The sibling 银杏云盘… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Marketed as 1 TB free with WebDAV; its own Cloudreve site config now returns title '长青云盘·11月19下线' (shutting down Nov 19) and registerEnabled=false. Dead mid-flight. The sibling 银杏云盘…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Marketed as 1 TB free with WebDAV; its own Cloudreve site config now returns title '长青云盘·11月19下线' (shutting down Nov 19) and registerEnabled=false. Dead mid-flight. The sibling 银杏云盘 cloud.7
  - [2] 2026-10-21: cited as the basis of the rejection: Marketed as 1 TB free with WebDAV; its own Cloudreve site config now returns title '长青云盘·11月19下线' (shutting down Nov 19) and registerEnabled=false. Dead mid-flight. The sibling 银杏云盘 cloud.7
  - [1] 2026-11-19: the site config still shows registration disabled | capture: sha256:5dd5fb570131117ea791c1e2dc927c51ff4bf9a670cfe9b8bda865e2d36c2c1e | quote: "registerEnabled":false
- sources:
  - [1] https://cloud.7so.top/api/v3/site/config
  - [2] https://www.nodeloc.com/t/topic/24202

## 七嗖云盘 / 长青云盘 (7so.top, cloud.7so.top)

- `netdisk-pan/seven-so-cloud` | dead | evidence documented | binding retention-clamped | category public-benefit pan on resold OneDrive, dead
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:15:15.159Z (live) | stale on 2026-12-18
- url https://cloud.7so.top
- free tier: 1 TB free on registration per the forum, with the sibling 银杏云盘 at 200 GB. Its own site configuration now reads '长青云盘·11月19下线' with registerEnabled false, so the offer is closed | unit: TiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Advertised as unlimited per file while the service ran | source: [1]
- retention: Shutting down: the site's own title is '长青云盘·11月19下线'. Data loss on shutdown is near-certain | days: 0 | source: [2]
- egress: Unmetered while it ran: '下载文件无需登录' and '不限速' were advertised, and downloads worked without an account | metered: no | source: [1]
- identity: email | detail: an email address and no phone while registration was open. Registration is now disabled
- interface: webdav
- limits:
  - retention-clamped (binding): the service is shutting down and registration is disabled [2]
  - write-gated: WebDAV, offline download and the rest of the useful features are paid-tier only [1]
- binding note: Service officially announced shutdown with new user registration disabled, establishing complete retention expiry.
- tooling: WebDAV on the paid tier only: '注意：上面三个网盘免费版不支持WebDAV'. The backend is described by third parties as OneDrive-based, making it a white-label reseller
- composes with: Nothing to chain. One account was 1 TB with email registration and no phone, and the operator is shutting down, so the whole point was that account multiplication was trivial and each one was a single operator's resold quota
- reliability: unverified: https://cloud.7so.top/api/v3/site/config returned no HTTP status with a TLS hostname mismatch on 2026-11-26; no config body was read
- notes: Documented service shutdown following an initial 1 TB free offering. Published site configuration confirms the formal termination date and closure of new registrations.
- extras:
  - access_mode: registration-gated
  - closed: 2026-11-19, per the site's own configuration
  - registration_disabled: yes
  - backend: resold OneDrive
  - aliases: 七嗖云盘 / 长青云盘 (7so.top → cloud.7so.top); 七嗖云盘 / 长青云盘 (7so.top); 银杏云盘 (cloud.7so.top) at 200 GB
- evidence:
  - probe:https://cloud.7so.top/api/v3/site/config 2026-10-21: {"title":"长青云盘·11月19下线","registerEnabled":false,"emailActive":true}, so the site says it is closing and has closed registration
  - [1] 2026-10-21: '1TB免费空间 / 下载文件无需登录 / 支持WebDAV / 不限速', with the caveat '上面三个网盘免费版不支持WebDAV'
  - [3] 2026-10-21: '七嗖云盘/银杏云盘是由鄢杰与荣6呀运营的公益云盘，注册后将有1TB大容量存储（银杏云盘有200GB）'
  - probe:https://cloud.7so.top 2026-10-21: HTTP 200 with 7,120 bytes in 2026-10, so the landing page still answers while registration is closed
  - [2] 2026-11-19: the site config on 2026-11-19 still declares the shutdown and registration is disabled | capture: sha256:5da221c3b46618b7bd4dd9b171159cb6c593b2e257e77aea68ed71d2e24ede79 | quote: "title": "长青云盘·11月19下线"
  - [4] 2026-11-19: the landing page shows a server error notice on the declared shutdown date | capture: sha256:bda8a25238bc24051d9a87c30cb18afe5500aaa80c466c26428be2b069fce77c | quote: 请检查网络，如果一切正常，那么可能是服务器出现了问题
  - probe:https://cloud.7so.top/api/v3/site/config 2026-11-26: the probe recorded a TLS verification error and no HTTP status | capture: sha256:4a5ef7325a24b64140c2dfd9ccd2a79907dd32cc6128598897f78f0b5b3957e5 | quote: "error": "tls_untrusted"
- sources:
  - [1] https://linux.do/t/topic/306810
  - [2] https://cloud.7so.top/api/v3/site/config
  - [3] https://www.nodeloc.com/t/topic/24202
  - [4] https://cloud.7so.top
