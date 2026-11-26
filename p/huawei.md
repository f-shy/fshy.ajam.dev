# 华为云空间 Huawei

> huawei.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/huawei/ | JSON https://fshy.ajam.dev/api/v1/entity/huawei.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 华为云空间 / HUAWEI Mobile Cloud

- `netdisk-pan/huawei-mobile-cloud` | fails-quota | evidence reported | binding per-object-cap | category phone-vendor cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T15:23:48.017Z (inherited) | stale on 2026-12-10
- url https://cloud.huawei.com/
- price 2 TB at CNY 698/yr is about USD 4.1/TB/month, and it is often unpurchasable on a non-mainland HUAWEI ID | parsed USD 4.1/TB-mo
- free tier: In the new cloud space, 基础服务 is unlimited free storage, which replaced the former free 5 GB, and holds fixed system data: contacts, notes, calendar, browser, apps and SMS | unit: mixed | metered on: stored-bytes | read on: 2026-11-25 | source: [1]
- per-object cap: Not published | source: [2]
- retention: 基础服务 holds contacts, SMS and notes with no fixed size; photos and video need 会员服务. No retention clock published | source: [3]
- egress: No documented cap, but the service is sync-oriented and offers no public sharing of the drive | metered: no | source: [2]
- identity: country-phone | detail: Check whether you can purchase a cloud storage plan in the country or region where your HUAWEI ID is registered, as the service is only supported in some countries or regions outside the Chinese mainland. | country: cn
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [4]
  - write-gated: Check whether you can purchase a cloud storage plan in the country or region where your HUAWEI ID is registered, as the service is only supported in some countries or regions outside the Chinese mainland. [3]
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
  - [4] 2026-10-21: table row 华为云服务, 5G free, no upload limit, no review, no sharing, no speed limit, login required
  - [3] 2026-10-21: the plan purchase fails when the HUAWEI ID's registration country does not support the plan
  - [5] 2026-10-21: a WebDAV service over the Huawei cloud drive API, '可将华为云盘映射为本地磁盘'
  - [6] 2026-10-21: a 2 TB carpool at CNY 698 for six people at CNY 120 each, 330 GB per person
  - [4] 2026-11-03: the table row still reads 5G free | capture: sha256:87cfd4212b0eaf2bb73b16353c13f114920639a0b2df7d9e3a6465f3bf0ce870 | quote: | 华为云服务 | 5G | 无 | 无 | 无 | 无 | | |
  - [5] 2026-11-03: the WebDAV bridge over the Huawei cloud drive API is still published | capture: sha256:efb04c62a3d11d66e2937bda27947eed3adee0d33cad9de719025aaab0a909fe | quote: 基于华为云盘 API 实现的 WebDAV 服务，可将华为云盘映射为本地磁盘，方便使用 WebDAV 客户端进行文件管理。
  - [2] 2026-11-03: the global portal still answers 200 and offers the cloud app download | capture: sha256:b8022a9fc005aea9e430f283020c13226c981f09d00d19f8ed2eb74e1b58044c | quote: Download Cloud app
  - [1] 2026-11-25: the vendor support page says the new cloud space's 基础服务 replaces the former free 5GB with unlimited free storage for fixed system data | capture: sha256:863aa6cc21de407cc7d9d9f73a155dba98cf798e3c1f5d8ea6190c2af4bac34a | quote: 基础服务：原免费5GB空间升级为无限免费存储空间，且在云空间首页不展示云存储空间大小；免费空间可存储联系人、备忘录、日历、浏览器、应用程序、短信等固定的系统基础数据。
  - [1] 2026-11-25: the original cloud space still gives a free 5GB | capture: sha256:863aa6cc21de407cc7d9d9f73a155dba98cf798e3c1f5d8ea6190c2af4bac34a | quote: 进入云空间，即可获得免费5GB空间，您可以通过云备份、使用云的应用、云盘等功能，将您的照片、视频、联系人、备忘录等重要数据安全存储在云端。
  - [7] 2026-11-25: the vendor plan page lists annual 50GB, 200GB and 2TB plans at 58, 198 and 698 CNY a year | capture: sha256:0887aae9eed7bf9da4f2f42830e1c9f8536ec244bc2ef8387ac5fece5921d524 | quote: | 连续包年 | 58元/年 | 198元/年 | 698元/年 | 不支持 | 不支持 |
  - [1] 2026-11-25: the vendor page states the cloud space has no rate limit | capture: sha256:863aa6cc21de407cc7d9d9f73a155dba98cf798e3c1f5d8ea6190c2af4bac34a | quote: 华为云空间没有速率限制，上传和下载的速率取决于您的网络环境，具体速率请以您实际使用为准。
  - [3] 2026-11-25: the vendor support page states this value | capture: sha256:85df0f52b7d4770f5011f866ca6ead76cfddc5c92fdef403ba4602765cf1addf | quote: Check whether you can purchase a cloud storage plan in the country or region where your HUAWEI ID is registered, as the service is only supported in some countries or regions outside the Chinese mainland.
  - [3] 2026-11-25: an unsupported region shows a plan-not-available prompt | capture: sha256:85df0f52b7d4770f5011f866ca6ead76cfddc5c92fdef403ba4602765cf1addf | quote: The user is prompted that the cloud storage plan is not yet available
- sources:
  - [1] https://consumer.huawei.com/cn/support/content/zh-cn16009327/
  - [2] https://cloud.huawei.com/
  - [3] https://consumer.huawei.com/en/support/content/en-us15804999/
  - [4] https://zh.wikipedia.org/zh-cn/中国大陆网盘列表
  - [5] https://github.com/RzdPai/Huawei_Cloud_Webdav
  - [6] https://www.v2ex.com/t/1076365
  - [7] https://consumer.huawei.com/cn/support/content/zh-cn16037399/

## 华为云空间 Huawei Cloud Space

- `storage/huawei-cloud-space` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T21:14:04.250Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the comparison table still lists Huawei Cloud Space at about 5 GB free and about 6 yuan per month | capture: sha256:438b4473320869f2d16db28adaf999e1a09c6266b6102b93c8209be369da3ad6 | quote: | [华为云空间](https://panhunt.com/pan-platforms/huawei-cloud) | 约 5GB | 约 ¥6/月 | 不限速 | 不支持 | 不支持 | 不支持 | 华为设备系统备份 |
- sources:
  - [1] https://panhunt.com/compare
  - [2] https://github.com/yuanbaobaoo/PetalLink
