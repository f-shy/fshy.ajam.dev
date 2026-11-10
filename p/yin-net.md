# YinNet

> yin-net.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yin-net/ | JSON https://fshy.ajam.dev/api/v1/entity/yin-net.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YinNet

- `compute/yinnet` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.yin-net.com/
- free tier: USD 48 per year for the United Kingdom row: 1 core, 1 GB RAM, 10 GB SSD, 1 TB a month, 500 Mbps, dual-ISP residential IPv4 with no IPv6. Japan is USD 50 a year for the same shape, Singapore USD 58 a year with 2 TB a month at 1 Gbps and native IPv4 plus IPv6, and Taiwan USD 58 a year with 1 TB a month and native IPv4 plus IPv6. The offer is a limited annual release with no mainland route optimisation. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on the UK, Japan and Taiwan rows, 2 TB on Singapore, at 500 Mbps to 1 Gbps; no overage price stated | metered: yes | free allowance: 1 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on the UK, Japan and Taiwan rows and 2 TB on Singapore, all annual-only at these prices; no overage price is stated, and the page's own FAQ says top-ups are available only where the service supports them. [1]
- limits note: 1 TB a month on the UK, Japan and Taiwan rows and 2 TB on Singapore, all annual-only at these prices; no overage price is stated, and the page's own FAQ says top-ups are available only where the service supports them.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS cart and client area; no API documented
- composes with: USD 48 a year for a UK residential IP with 1 TB a month is the cheapest European residential egress among documented hosts, and residential is what a datacentre-blocking target accepts
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing and article, then the vendor homepage, which prints no price. The record is reported, and the price is annual-only. Rendering and provenance: currency written as USD.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [2] 2026-10-23: cheapest row quoted: '英国 | 1G | 1核 | 10G | 1T/月 | 500Mbps | $48/年'; '日本 … $50/年'; '新加坡 | 1G | 1核 | 10G | 2T/月 | 1Gbps | $58/年'; '台湾 … $58/年'
  - [2] 2026-10-23: line statement quoted: '默认纯国际线路，无中国大陆路由优化'; IP statement '台湾和新加坡为原生的IPv4+IPv6；英国和日本为双ISP住宅属性的IPv4/不提供IPv6'
  - [1] 2026-10-23: vendor homepage read renders no price: it routes to cart.php and states '實際配置與供應情況以訂購頁為準' (actual configuration and availability are as shown on the order page)
- sources:
  - [1] https://www.yin-net.com/
  - [2] https://www.zhujiceping.com/99971.html
