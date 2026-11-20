# 帮你下

> bangnixia.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bangnixia/ | JSON https://fshy.ajam.dev/api/v1/entity/bangnixia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 帮你下 (bangnixia.com)

- `debrid/bangnixia` | qualifies-with-caveat | evidence documented | binding volume-quota | category debrid-style 代下 / leeching platform | tier traffic pack
- needs card yes, phone yes, ID no, institution no | verified 2026-10-23T01:56:12.303Z (live) | stale on 2026-11-23
- url https://bangnixia.com/upgrade
- price CNY 741 per TB retrieved (one-off, 270 GB pack)
- free tier: No free allowance. The smallest pack is 1 GB for ¥1.2; every fetched byte is charged against a purchased pack. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Not stated. No per-file ceiling is published on the pricing or home page. | source: [1]
- retention: 文件存储十天: the fetched file is held on the service's server for 10 days. | days: 10 | source: [1]
- egress: Traffic packs are 永久 (permanent, no expiry) and are consumed per byte fetched. Storage of the fetched file is 10 days. Download back to the user is over the service's CN2 line and is not separately metered. | metered: yes | free allowance: none; each pack is prepaid traffic | source: [2]
- identity: card | detail: No account was proven necessary to buy: the checkout is a payment for a traffic pack that activates on success. The gate is therefore payment, not registration - and the rails are Chinese wallets, which need a mainland phone-bound account in practice.
- interface: rest
- limits:
  - volume-quota (binding): prepaid traffic packs of 1/25/55/100/270 GB; permanent validity [1]
  - retention-clamped: fetched files are deleted after 10 days [2]
- binding note: The prepaid pack is the wall: at ¥0.74/GB, 1 TiB costs ¥758, which is 76x the 迅雷 SVIP membership for the same byte count. In exchange, no account on the source host is needed.
- interface detail: No published API. The ordering step is a browser; the product is an HTTP(S) URL that aria2, curl or a browser can fetch, so the transfer itself is programmatic.
- tooling: Web UI plus a returned direct URL. aria2/IDM consume the URL; 断点续传 and 并行下载 are advertised features.
- composes with: The no-account path for a one-off foreign-host download: buy 25 GB for ¥24 and fetch without owning a rapidgator or keep2share account.
- reliability: Hosts are added and dropped without notice: the page states xubster, filejoker, novafile, icerbox, tezfiles and mega are no longer supported. A pack bought for one host can lose that host.
- notes: ¥200/270 GB = ¥0.741/GB = ¥758/TB. The 1 GB entry pack is ¥1.2/GB, a 62% premium for trying it. The site describes itself in English as a 'debrid leeching platform', which is the only self-description of its kind found in Chinese retail.
- evidence note: Prices, pack sizes, the 10-day storage term and the dropped-host list were read off the vendor's own two pages. No download was run, so the per-file cap and the real speed are unmeasured.
- extras:
  - per_gb_cny: 0.741
  - entry_pack_cny_per_gb: 1.2
- evidence:
  - [1] 2026-10-23: 1 GB ¥1.2, 25 GB ¥24, 55 GB ¥50, 100 GB ¥80, 270 GB ¥200, each 有效期 永久 and 存储期限 永久; dropped hosts listed
  - [2] 2026-10-23: title reads 'debrid leeching platform'; '文件存储十天'; 'CN2专属线路'; '断点续传 并行下载'; 80+ host names in the meta description
- sources:
  - [1] https://bangnixia.com/upgrade
  - [2] https://bangnixia.com/
