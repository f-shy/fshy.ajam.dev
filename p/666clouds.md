# 666clouds

> 666clouds.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/666clouds/ | JSON https://fshy.ajam.dev/api/v1/entity/666clouds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 666clouds

- `compute/666clouds` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.666clouds.com/
- free tier: CNY 50 per month for the US dual-ISP residential-IP plan: 1 core, 1 GB RAM, 20 GB SSD, 1 TB a month, 1 Gbps, one IPv4. Germany and the United Kingdom are CNY 60 a month for the same shape, the Philippines is CNY 80 a month for 1 GB, 1 core, 15 GB and 1 TB, Korea CNY 80 a month for 1 GB, 1 core, 20 GB and 1 TB at 200 Mbps, and the 2 GB rows start at CNY 160. The offer states no real-name registration and no ICP filing are required, and Alipay is accepted. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on every row, 1 Gbps on the US, German and UK rows, 200 Mbps on Korea; no overage price stated | metered: yes | free allowance: 1 TB per month | source: [2]
- identity: email | detail: not read: signup requirements unverified; the review article states the vendor requires no real-name registration and no ICP filing, quoted in the evidence row
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on every row, on a 1 Gbps port for the US, German and UK rows and 200 Mbps for Korea, so the byte allowance binds before the port; no overage price is stated. [1]
- limits note: 1 TB a month on every row, on a 1 Gbps port for the US, German and UK rows and 200 Mbps for Korea, so the byte allowance binds before the port; no overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: portal with tickets, docs and a per-region status page; no API documented
- composes with: CNY 50 for a dual-ISP residential IP with 1 TB in the United States, and the same shape at CNY 60 in Germany and the United Kingdom, gives a residential egress point in three jurisdictions from one account
- reliability: no reliability event recorded
- notes: Source: zhujiceping offer listing and article, then the vendor homepage, which defers every price to the order page and prints none. The record is reported. Unverified: the order page's confirmation that the CNY 50 row is monthly and recurring. Rendering and provenance: currency written as CNY.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [2] 2026-10-23: cheapest row quoted: '美国VPS - 双ISP住宅IP … 50元/月、1G内存、1核、20G SSD、1T流量/月、1Gbps带宽、一个IPv4'; '德国VPS … 60元/月、1G内存、1核、20G SSD、1T流量/月'; '菲律宾 … 1G | 1核 | 15G | 1T/月 | 80元/月'
  - [2] 2026-10-23: identity statement quoted: '无需实名、免备案，可支付宝付款！'
  - [1] 2026-10-23: vendor homepage read states '套餐、配置与价格以选购页实时显示为准' (plans, configurations and prices are shown live on the order page) and prints no price
- sources:
  - [1] https://www.666clouds.com/
  - [2] https://www.zhujiceping.com/90618.html
