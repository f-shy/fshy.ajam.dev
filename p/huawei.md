# 华为云空间 Huawei

> huawei.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/huawei/ | JSON https://fshy.ajam.dev/api/v1/entity/huawei.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 华为云空间 / HUAWEI Mobile Cloud

- `netdisk-pan/huawei-mobile-cloud` | fails-quota | evidence reported | binding per-object-cap | category phone-vendor cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:20:53.783Z (inherited) | stale on 2026-11-19
- url https://cloud.huawei.com/
- price 2 TB at CNY 698/yr is about USD 4.1/TB/month, and it is often unpurchasable on a non-mainland HUAWEI ID | parsed USD 4.1/TB-mo
- free tier: 5 GB free, split between 基础服务 and 会员服务. Paid tiers commonly 50 GB, 200 GB and 2 TB. A 2 TB carpool is priced at CNY 698 split six ways at CNY 120 each | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [2]
- retention: 基础服务 holds contacts, SMS and notes with no fixed size; photos and video need 会员服务. No retention clock published | source: [3]
- egress: No documented cap, but the service is sync-oriented and offers no public sharing of the drive | metered: no | source: [2]
- identity: country-phone | detail: a HUAWEI ID registered in a country where the plan is sold. The vendor's own support page says the purchase prompt fails otherwise | country: cn
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [1]
  - write-gated: the plan purchase fails for a HUAWEI ID registered in a country where the cloud storage plan is not available [3]
- binding note: 5 GB free, and the plan that would fix it is often unpurchasable from outside the mainland, so the quota closes it before the region gate is reached.
- tooling: two distinct APIs. The consumer one is reverse-engineered at driveapis.cloud.huawei.com.cn behind an OAuth bearer token, and RzdPai/Huawei_Cloud_Webdav exposes it as WebDAV, which is the useful part. KooDrive is a separate enterprise product with official documentation and must not be conflated with it
- composes with: A WebDAV bridge exists, so it chains like any drive, but 5 GB free is 400 accounts per terabyte and the free tier is per HUAWEI ID rather than per device. Non-mainland IDs often cannot buy a plan at all
- reliability: The terms now split 基础服务, unmetered for contacts, SMS and notes, from 会员服务, metered for photos, video and app data. The unmetered half holds no bulk data. Free-space farming exists but is territory-locked to app-install tasks on Huawei handsets
- notes: Region-gated cloud service featuring an active WebDAV bridge accessible to mainland accounts. Free storage is limited to 5 GB, and paid subscription pathways require domestic mainland payment verification.
- extras:
  - access_mode: registration-gated
  - webdav_bridge: RzdPai/Huawei_Cloud_Webdav
  - region_gated: yes
  - aliases: 华为云空间 / HUAWEI Mobile Cloud
- evidence:
  - [2] 2026-10-21: a live portal served by Huawei Services Hong Kong; a global portal exists but the storage product is region-gated
  - [1] 2026-10-21: table row 华为云服务, 5G free, no upload limit, no review, no sharing, no speed limit, login required
  - [3] 2026-10-21: the plan purchase fails when the HUAWEI ID's registration country does not support the plan
  - [4] 2026-10-21: a WebDAV service over the Huawei cloud drive API, '可将华为云盘映射为本地磁盘'
  - [5] 2026-10-21: a 2 TB carpool at CNY 698 for six people at CNY 120 each, 330 GB per person
  - [3] 2026-11-03: the vendor support page says the plan purchase depends on the country or region where the HUAWEI ID is registered | capture: sha256:0be8ba2339118a70db5d8ade28fc7b61eee82d67f732bf79a5ec1fd5419e9a2c | quote: Check whether you can purchase a cloud storage plan in the country or region where your HUAWEI ID is registered, as the service is only supported in some countries or regions outside the Chinese mainland.
  - [3] 2026-11-03: the support page lists the purchase prompt that says the plan is not yet available | capture: sha256:0be8ba2339118a70db5d8ade28fc7b61eee82d67f732bf79a5ec1fd5419e9a2c | quote: The user is prompted that the cloud storage plan is not yet available
  - [1] 2026-11-03: the table row still reads 5G free | capture: sha256:87cfd4212b0eaf2bb73b16353c13f114920639a0b2df7d9e3a6465f3bf0ce870 | quote: | 华为云服务 | 5G | 无 | 无 | 无 | 无 | | |
  - [4] 2026-11-03: the WebDAV bridge over the Huawei cloud drive API is still published | capture: sha256:efb04c62a3d11d66e2937bda27947eed3adee0d33cad9de719025aaab0a909fe | quote: 基于华为云盘 API 实现的 WebDAV 服务，可将华为云盘映射为本地磁盘，方便使用 WebDAV 客户端进行文件管理。
  - [2] 2026-11-03: the global portal still answers 200 and offers the cloud app download | capture: sha256:b8022a9fc005aea9e430f283020c13226c981f09d00d19f8ed2eb74e1b58044c | quote: Download Cloud app
- sources:
  - [1] https://zh.wikipedia.org/zh-cn/中国大陆网盘列表
  - [2] https://cloud.huawei.com/
  - [3] https://consumer.huawei.com/en/support/content/en-us15804999/
  - [4] https://github.com/RzdPai/Huawei_Cloud_Webdav
  - [5] https://www.v2ex.com/t/1076365

## 华为云空间 Huawei Cloud Space

- `storage/huawei-cloud-space` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloud.huawei.com
- free tier: About 5 GB free; ~¥6/month for more. Device-backup oriented. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not speed-limited ('不限速') but capacity-bound. | metered: no
- identity: any-phone | detail: any-phone (HUAWEI ID)
- interface: rest, webdav-proxy
- limits note: quota 5 GB. no WebDAV, no direct link.
- interface detail: rest
- tooling: No dedicated OpenList driver found in the 89-driver tree; a third-party macOS client exists (yuanbaobaoo/PetalLink, 10 stars). Wrapper-only.
- composes with: 5 GB per HUAWEI ID. Not a capacity play.
- reliability: Stable; strictly a device-ecosystem backup target.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: About 5 GB free; ~¥6/month for more. Device-backup oriented.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '华为云空间 | 约 5GB | 约 ¥6/月 | 不限速 | 不支持 | 不支持'（核对 2026-10-19）
  - [2] 2026-10-21: third-party macOS client, wrapper-only access
- sources:
  - [1] https://panhunt.com/compare
  - [2] https://github.com/yuanbaobaoo/PetalLink
