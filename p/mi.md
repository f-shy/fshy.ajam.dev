# 小米云服务

> mi.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mi/ | JSON https://fshy.ajam.dev/api/v1/entity/mi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 小米云服务 / Xiaomi Cloud (Mi Cloud Drive)

- `netdisk-pan/xiaomi-cloud` | fails-quota | evidence reported | binding per-object-cap | category phone-vendor cloud, China mainland
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:53.784Z (inherited) | stale on 2026-11-19
- url https://i.mi.com/
- price 2 TB at CNY 408/yr promotional is about USD 2.4/TB/month, and CNY 816/yr list about USD 4.8/TB/month | parsed USD 4.8/TB-mo
- free tier: 5 GB free: the vendor's own manual reads 免费 5G, 黄金 50G, 白金 200G, 钻石 2048G. Membership is CNY 72, 252 and 816 a year, with promos putting 2 TB at CNY 239 to 408 | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published; the drive is sync-oriented and does not expose a single-file ceiling | source: [1]
- retention: Account ownership is not transferable; the global-region Gallery sync and all memberships were terminated on 2022-10-25 outside the mainland, with stored Gallery data deleted by mid-2023 | source: [2]
- egress: No published cap, and the drive is deliberately not share-oriented: the community notes 不能对外分享. Third-party clients download at full speed with concurrency 20 | metered: no | source: [3]
- identity: email | detail: a Xiaomi account. Xiaomi's own FAQ says a non-mainland account 'can only be created through email', which is an open door into the region where the storage product was killed. Only a mainland account still has the 2 TB tier | country: 86
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [1]
  - write-gated: family sharing is capped at 8 members and shares quota and not data [1]
- binding note: Free storage is limited to 5 GB. Global email registration routes accounts to international regions where consumer drive sync features have been phased out. Total account quota is the binding constraint.
- tooling: a reverse-engineered REST interface at i.mi.com with a Go CLI, wangbjun/go-micloud, doing login, list, upload, download, share and tree at concurrency 5 up and 20 down; an unmerged OpenList driver pull request 1391 implements list, link, put and mkdir but its body says 还没写完
- composes with: The API is real and a wrapper exists, so it would be the cleanest phone-vendor target. 5 GB free means about 410 accounts per 2 TB and the 2 TB tier is CNY 239 to 408 a year, which is not a stacking play
- reliability: Global-region Gallery sync and all memberships were terminated outside mainland China in three regional waves by 2023-02-01, with Gallery data deleted by mid-2023. An email signup works and lands in the region where the product no longer exists, which is a worse outcome than a closed gate because it looks open
- notes: Email registration succeeds internationally but maps accounts to global regions lacking active drive storage sync. Unofficial client tooling includes experimental Go wrapper scripts and community OpenList driver integrations.
- extras:
  - access_mode: registration-gated
  - region_gate_inverted: yes
  - terminated_outside_mainland: 2022-10-25 onwards
  - aliases: 小米云服务 / Xiaomi Cloud (Mi Cloud Drive); 小米云服务 Xiaomi Cloud
- evidence:
  - [1] 2026-10-21: the tier table 免费 5G, 50G, 200G, 2048G at CNY 72, 252 and 816 a year
  - [2] 2026-10-21: 'Syncing of Gallery items to Xiaomi Cloud and Xiaomi Cloud membership services will be terminated' outside the Chinese mainland, and 'These services will not be terminated on the Chinese mainland at this time'
  - [4] 2026-10-21: 'The Xiaomi account outside the Chinese mainland can only be created through email'
  - [5] 2026-10-21: a full CLI, '登录采用模拟小米云服务Web端的登录逻辑', upload concurrency 5 and download 20
  - [6] 2026-10-21: 'Xiaomi Cloud Dirve', list, link, put and mkdir implemented, body says 还没写完
  - probe:https://i.mi.com/file/full?type=note_ 2026-10-21: HTTP 200, 102 bytes, {"result":"error","reason":"fileid参数不能为空","code":10016}, which is a 200 that carries an error
  - probe:https://i.mi.com/storage/web/v2/storage 2026-10-21: HTTP 404, 211 bytes, a Resin/4.0.61 MicloudWeb HTML error page
  - [1] 2026-11-03: the membership page still gives ordinary users 5G of cloud storage, against 50G, 200G and 2048G for the paid tiers | capture: sha256:a04001e359170f45c6564dafcfa5049fa5bf3634d8134d69b49d7521bddf029c | quote: | 云存储空间 | 5G | 50G | 200G | 2048G |
  - [1] 2026-11-03: the membership page still prices the paid tiers at 72, 252 and 816 yuan a year | capture: sha256:a04001e359170f45c6564dafcfa5049fa5bf3634d8134d69b49d7521bddf029c | quote: | 会员价格 | 免费 | 72元/年 | 252元/年 | 816元/年 |
  - [2] 2026-11-03: the notice still says the Gallery sync and membership termination does not apply on the mainland | capture: sha256:fc31d226b1398d7ddec129c34360319c0d72eea8173cdf0f242c0cf922322c3f | quote: These services will not be terminated on the Chinese mainland at this time.
  - [2] 2026-11-03: the notice gives the three regional termination dates | capture: sha256:fc31d226b1398d7ddec129c34360319c0d72eea8173cdf0f242c0cf922322c3f | quote: | Before December 1, 2022 | Before January 1, 2023 | Before February 1, 2023 |
  - [3] 2026-11-03: the portal answers 200 and asks for a Xiaomi Account sign-in | capture: sha256:76ea69cb1bdbde2e6f2ef4a8272f6bbf1ed649877122b0c82fe8cb965d79f999 | quote: Sign in with Xiaomi Account
  - [5] 2026-11-03: the Go client still documents upload concurrency 5 and download concurrency 20 | capture: sha256:263ed9529b009a871c34ff2fa130e0540d726e9e1a38a1937a89ea338ac430b6 | quote: 上传和下载采用异步方式，默认上传并发5，下载并发20
  - probe:https://i.mi.com/file/full?type=note_ 2026-11-03: the file endpoint answers 200 with a JSON error body (102 bytes), a 200 that carries an error | capture: sha256:a81eb88f28b3b65bb54245632c88edb1561b358a08a9f528bee2a6b737753e52 | quote: "reason":"fileid参数不能为空"
  - probe:https://i.mi.com/storage/web/v2/storage 2026-11-03: the storage path answers 404 from a Resin/4.0.61 server | capture: sha256:875df53cc2022138b5de87de28d4fa32ed88a1e195d1138a909f37d3b1015550 | quote: Resin/4.0.61
- sources:
  - [1] https://i.mi.com/guide/zh-CN/membership/overview
  - [2] https://i.mi.com/announcement/stop_service
  - [3] https://i.mi.com/
  - [4] https://www.mi.com/global/support/faq/details/KA-547873/
  - [5] https://github.com/wangbjun/go-micloud
  - [6] https://github.com/OpenListTeam/OpenList/pull/1391
