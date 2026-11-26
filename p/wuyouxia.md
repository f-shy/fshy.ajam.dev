# 无忧下

> wuyouxia.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wuyouxia/ | JSON https://fshy.ajam.dev/api/v1/entity/wuyouxia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 无忧下 (wuyouxia.net)

- `debrid/wuyouxia` | qualifies | evidence documented | binding volume-quota | category debrid-style 代下 / 中转 with WebDAV | tier traffic pack
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:36.209Z (live) | stale on 2026-12-26
- url https://www.wuyouxia.net/
- price CNY 525 per TB retrieved (600 GB pack)
- free tier: No free allowance. '最低1元起购' and the smallest pack is 5 GB for ¥7 (list ¥10). | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Not stated. | source: [1]
- retention: 链接有效期24小时: the generated download link lives 24 hours. The fetched file's own lifetime on the server was not stated. | days: 1 | source: [1]
- egress: '仅按实际使用流量付费' - prepaid packs with 永久 validity, no monthly subscription. Download back to the user runs over the service's CN2 line with 断点续传. | metered: yes | free allowance: none; prepaid traffic | source: [1]
- identity: card | detail: Purchase, no account proven. Chinese payment rails are the gate.
- interface: webdav, rest
- limits:
  - volume-quota (binding): 5/25/120/240/600 GB packs; ¥7 to ¥315; permanent validity [1]
  - retention-clamped: generated link valid 24 hours [1]
- binding note: Prepaid traffic binds at any scale: ¥525/TB is the cheapest sticker found, but 1 TiB of monthly transfer is still ¥525 one-off, against ¥9.93 for 迅雷 SVIP. The WebDAV mount is the feature that buys that premium.
- interface detail: '支持通过 WebDAV 协议挂载到系统' - the service mounts, so a file can be streamed instead of downloaded twice. The direct URL is also a plain HTTP(S) fetch.
- tooling: WebDAV mount, browser UI, parallel multi-link submission. Same platform as the same operator's 帮你下 storefront.
- composes with: The only 代下 among debrid providers that offers WebDAV: mount it and a media player streams from the service's copy without a second transfer.
- reliability: Two storefronts (wuyouxia.com family, 帮你下) sell the same traffic under different prices; the 24-hour link is the operational limit to plan around.
- notes: Per GB: 1.40, 0.80, 0.642, 0.583, 0.525. Page markup renders the discounted price beside the list price ('10 7元'), which is how the sale ladder was read.
- evidence note: Pack prices read from the vendor page; the sale price was recovered from the struck-through list price in the same markup. The zh-TW storefront quotes the same packs in USD ($1 for 5 GB), which corroborates ¥7 at about 7.1 CNY/USD.
- extras:
  - webdav: yes
  - link_hours: 24
  - per_gb_cny: 0.525
- evidence:
  - [1] 2026-10-23: '50+ 优质网盘 • 不限带宽 • 仅按实际流量付费'; '最低1元起购'; packs 5 GB (10→7元), 25 GB (30→20元), 120 GB (100→77元), 240 GB (200→140元), 600 GB (400→315元); '链接有效期24小时'; '支持通过 WebDAV 协议挂载'
  - [2] 2026-10-23: same packs quoted in USD: '最低$0.3起購', 基本款 5.0 GB $1.00 - corroborates the CNY ladder
  - [1] 2026-11-25: the generated download link is still valid for 24 hours | capture: sha256:03d580159f804ef253c413b753c79d43d323ea22136a522f155d3af101d77fbd | quote: 链接有效期24小时
  - [1] 2026-11-25: the service still offers a WebDAV mount | capture: sha256:03d580159f804ef253c413b753c79d43d323ea22136a522f155d3af101d77fbd | quote: 支持通过 WebDAV 协议挂载到系统
  - [1] 2026-11-25: the smallest pack shown on the home page is 5 GB | capture: sha256:03d580159f804ef253c413b753c79d43d323ea22136a522f155d3af101d77fbd | quote: 5.0 GB
  - [3] 2026-11-25: the purchase page lists a 20 GB pack plus 5 GB bonus | capture: sha256:acd8ea1779745b5a3a288462e4f942d165152a610f187d447e50116b496f069f | quote: 20.0 GB 赠送+5.0 GB
  - [4] 2026-11-25: a registered user can earn 20 percent of a referred user's top-up or redemption as bonus traffic | capture: sha256:d70d9730a857658d2c8848897f5cd561d237a71ada19c5d96cb1bef787cb46d2 | quote: 被推荐人每次充值或兑换流量，你立即获得该笔流量的 20%
  - [5] 2026-11-25: the HTTP download-client API is keyed and restricted to JDownloader by default | capture: sha256:83e9f79e00a970c637f4afdcbb156b58cc12ef610acae4232459b52b56685bde | quote: By default, only JDownloader is allowed.
- sources:
  - [1] https://www.wuyouxia.net/
  - [2] https://www.wuyouxia.net/zh-TW
  - [3] https://www.wuyouxia.net/purchase
  - [4] https://www.wuyouxia.net/free
  - [5] https://www.wuyouxia.net/docs/download-client-api
