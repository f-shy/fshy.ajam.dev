# Zorocloud

> zorocloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zorocloud/ | JSON https://fshy.ajam.dev/api/v1/entity/zorocloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zorocloud

- `compute/zorocloud` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://my.zorocloud.com/
- free tier: CNY 39 per month for a US VPS on the CN2 plus 9929 plus CMIN2 network: 1 core, 1 GB RAM, 20 GB disk, 100 Mbps, 500 GB a month. The same line steps to CNY 56 for 1 TB, CNY 74 for 2 cores, 4 GB, 40 GB and 2 TB, CNY 149 for 4 cores, 4 GB, 80 GB and 4 TB, and CNY 306 for 4 cores, 8 GB, 120 GB at 200 Mbps and 6 TB. The Singapore residential line starts at CNY 188 a month, Japan at CNY 108 and Malaysia at CNY 149. The article's coupon is 'zoroyear'. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB to 6 TB a month depending on the row, at 100 to 200 Mbps; no overage price stated | metered: yes | free allowance: 500 GB per month on the CNY 39 row | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 500 GB a month on the CNY 39 row, 1 TB on the CNY 56 row and 2 TB on the CNY 74 row, so the allowance is bought with the plan; no overage price is stated. [1]
- limits note: 500 GB a month on the CNY 39 row, 1 TB on the CNY 56 row and 2 TB on the CNY 74 row, so the allowance is bought with the plan; no overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: store at my.zorocloud.com/store/... with per-line product pages; no API documented
- composes with: CNY 39 for a three-network-optimised US box with 500 GB is the cheapest entry among documented hosts to a route that splits across CN2, 9929 and CMIN2, which is what changes latency from the mainland
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing and article, then the vendor homepage, which prints no price. The record is reported. The article quotes a CNY 39 figure without a billing period on the row; every other row in the same table is a monthly price, and the row is recorded as monthly on that basis. Unverified: the store page's billing period. Rendering and provenance: currency written as CNY.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [2] 2026-10-23: cheapest row quoted: '1核 | 1G | 20G | 100M | 500G | ¥39' under '美国CNC云服务器(三网极致优化)'; '1核 | 1G | 20G | 100M | 1T | ¥56'; '2核 | 4G | 40G | 100M | 2T | ¥74'; Singapore '1核 | 1G | 20G | 200M | 1T | ¥188'
  - [1] 2026-10-23: vendor homepage read renders no price table: it carries capability statements only ('99.99% 网络与电力稳定性', '云服务器3秒内交付')
- sources:
  - [1] https://my.zorocloud.com/
  - [2] https://www.zhujiceping.com/96734.html
