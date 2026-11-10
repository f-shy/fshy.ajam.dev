# 兔子盘

> tuzipan.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tuzipan/ | JSON https://fshy.ajam.dev/api/v1/entity/tuzipan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 兔子盘 (tuzipan.com)

- `debrid/tuzipan` | qualifies-with-caveat | evidence documented | binding volume-quota | category debrid-style 代下 / 中转 with per-host multipliers | tier traffic pack
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:56:12.304Z (live) | stale on 2026-11-23
- url https://www.tuzipan.com/shop_php.html
- price CNY 598 per TB sticker (500 GB pack); CNY 897 per TB for a 1.5x host
- free tier: No free allowance. The smallest pack is 2.5 GB for ¥3; the site advertises 12小时自助充值自助下载, so the pack is bought and used without a subscription. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Not stated. No per-file ceiling is published. | source: [1]
- retention: Not stated on the pages read. The pack itself does not expire within the published terms; the fetched file's lifetime was not found. | source: [1]
- egress: Consumption is not the file size: '消耗流量=流量倍数*文件实际大小'. Each host carries a multiplier - rapidgator 1.5, nitroflare 1.5, keep2share 1.5, takefile 1.6, fboom 1.4, katfile 1.0, uploadgig 1.0 - so the effective price per GB depends on which host the link points at. | metered: yes | free allowance: none; prepaid traffic, charged at file size times the host multiplier | source: [1]
- identity: card | detail: No account was proven necessary: the flow is top-up then download, with a QQ contact for payment problems. The gate is the payment rail, and the rails are Chinese wallets.
- interface: rest
- limits:
  - volume-quota (binding): 2.5/35/65/140/300/500 GB packs; consumption = size x host multiplier (1.0 to 2.0) [1]
  - per-object-cap: not published [2]
- binding note: The multiplier is what binds: the 500 GB pack is ¥0.598/GB sticker, but a rapidgator terabyte costs 1.5x that, ¥897. Still the cheapest per-GB 代下 found among debrid providers.
- interface detail: No API. Ordering is a browser; the deliverable is a direct download URL.
- tooling: Web UI, 80+ foreign hosts listed, self-service top-up. Host status is published per host (正常 / 不再支持).
- composes with: The multiplier table makes this the only Chinese 代下 whose price is per host: a rapidgator terabyte costs 1.5x the sticker, a katfile terabyte costs 1.0x.
- reliability: Host support churns: filejoker is listed at multiplier 2 but marked 不再支持, so a multiplier table entry is not a promise of service.
- notes: Sticker per GB: 1.20 (2.5G), 0.83 (35), 0.75 (65), 0.71 (140), 0.66 (300), 0.60 (500). The '35 流量' row prints no unit; read as 35 GB it is ¥0.83/GB, which fits the ladder.
- evidence note: Both the price table and the multiplier table were read off the vendor's own pages. No file was fetched, so speed and per-file cap stay unmeasured.
- extras:
  - multiplier_range: 1.0-2.0
  - sticker_per_gb_cny: 0.598
- evidence:
  - [1] 2026-10-23: 2.5G 流量 ¥3; 35 流量 ¥29; 65G ¥49; 140G ¥99; 300G ¥199; 500G ¥299; '消耗流量=流量倍数*文件实际大小'
  - [2] 2026-10-23: multiplier table: rapidgator 1.5, katfile 1, takefile 1.6, nitroflare 1.5, keep2share 1.5, fboom 1.4, uploadgig 1, filejoker 2 不再支持; '支持下载80多个国外网盘的文件'; '12小时自助充值自助下载'
- sources:
  - [1] https://www.tuzipan.com/shop_php.html
  - [2] https://www.tuzipan.com/
