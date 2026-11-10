# tmhhost

> tmhhost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tmhhost/ | JSON https://fshy.ajam.dev/api/v1/entity/tmhhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tmhhost

- `compute/tmhhost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.tmhhost.com/
- free tier: CNY 33 per month for a Los Angeles VPS on the three-network AS9929 return path: 1 core, 1 GB RAM, 10 GB SSD, 800 GB a month, a 30 Mbps port, one IPv4, on an E5-2680v4. The CN2 GIA row of the same shape is CNY 40 a month, the dual-ISP residential-IP row on AS9929 is CNY 44 a month at 30 Mbps, the dual-ISP AS4837 row is CNY 44 a month at 50 Mbps, and the Hong Kong direct row is CNY 39 a month for the same 1 GB shape on a 5 Mbps port. Quarterly rows start at CNY 120 and annual rows at CNY 388 for 2 cores, 4 GB, 40 GB and 2 TB a month. The offer states the discount code is recurring, that the renewal price does not rise, and that no real-name registration is required. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 800 GB a month on the cheapest rows at 30 to 50 Mbps, 2 TB on the CNY 388 annual row; no overage price stated | metered: yes | free allowance: 800 GB per month | source: [2]
- identity: email | detail: not read: signup requirements unverified; the review article states the vendor requires no real-name registration, and that statement is quoted in the evidence row
- interface: rest
- limits:
  - volume-quota (binding): 800 GB a month at 30 to 50 Mbps is the stated allowance on the cheapest rows, and 2 TB on the CNY 388 annual row; no overage price is stated, so what happens at 800 GB is unverified. [1]
- limits note: 800 GB a month on a 30 Mbps port, which is about 59 hours of saturation, so the monthly byte allowance is reached long before the month ends on a busy host; no overage price is stated, so what happens at 800 GB is unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: WHMCS-style cart (cart?fid=6&gid=...), Alipay accepted per the article; no API documented
- composes with: A dual-ISP residential IP on AS9929 at CNY 44 with 800 GB is the cheapest residential-egress box among documented hosts, and residential egress is what a target that blocks datacentre ranges will accept
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing and article, then the vendor homepage. The vendor prices on cart pages that were not fetched, so the record is reported. The article's title claims a CNY 33 floor while its own table's cheapest row is CNY 44, and the title figure may be the annual-rate equivalent; the table is what is recorded. Rendering and provenance: currency written as CNY.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [2] 2026-10-23: cheapest monthly rows quoted: '1核 | 1G | 10G | 800G/月 | 30Mbps | 44元/月' and '1核 | 1G | 10G | 800G/月 | 50Mbps | 44元/月'; quarterly '1核 | 1G | 10G | 800G/月 | 50Mbps | 120元/季度'; annual '2核 | 4G | 40G | 2000G/月 | 50Mbps | 388元/年'
  - [2] 2026-10-23: identity statement quoted: '无需实名、无需备份、可支付宝等付款！'; discount '8.8折，优惠码 20261111，循环优惠'
  - [1] 2026-10-23: vendor homepage read renders no price: it lists the cart groups ('海外VPS', 'US美国 4837', 'US美国 CN2 GIA', 'US ISP 美国 9929') and links them to cart?fid=6 without a price on the page
- sources:
  - [1] https://www.tmhhost.com/
  - [2] https://www.zhujiceping.com/100906.html
