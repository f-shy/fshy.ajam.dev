# CSTServer

> cstserver.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cstserver/ | JSON https://fshy.ajam.dev/api/v1/entity/cstserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CSTServer

- `compute/cstserver` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://cstserver.com/index.php?rp=/announcements
- free tier: A sale posted 2026-08-20 lists E5 bare metal at USD 17.9 a month for an E5-2620 with 16 GB, in four locations at the same price with different ports: Frankfurt 80 Mbps, Japan 50 Mbps, Los Angeles 30 Mbps, Hong Kong 30 Mbps. The ladder runs to a Dual E5-2680 at 40 cores with 32 GB for USD 89.9. A 60 percent code applies and a three-year prepay brings the entry machine to USD 9.8 a month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bandwidth is priced per Mbps of dedicated China routing rather than per terabyte. | metered: yes | source: [1]
- identity: email
- interface: unknown
- limits:
  - per-ip-shaping (binding): Bandwidth is sold as a port, not a volume: 30 Mbps in Hong Kong or Los Angeles is about 9.7 TB a month at line rate, and that is the first thing a high-transfer workload exhausts. [1]
- limits note: Bandwidth is sold as a port, not a volume: 30 Mbps in Hong Kong or Los Angeles is about 9.7 TB a month at line rate, and that is the first thing a high-transfer workload exhausts.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the only lane found that sells a China-optimised route on a whole machine for under USD 20, and the route is what makes a Hong Kong box usable from the mainland side of a crawl; the port cap makes the same machine a poor choice for bulk transfer.
- reliability: no reliability event recorded
- notes: Two label traps are worth carrying forward. The vendor writes '12C' for an E5-2620, which is the thread count of a 6-core, 12-thread part, so a core count taken from this table is double the real one; that reading is inferred from the model number and not measured. And the same USD 17.9 buys 80 Mbps in Frankfurt against 30 Mbps in Hong Kong, so the location column is part of the price. The sale prices are dated 2026-08-20 and the codes may have expired by the read date. Real-name requirements were not tested: no signup was started.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: Intel Xeon E5-2620
  - facets.shape.ram_gib: 16
  - facets.shape.disk: 120 GB SSD
  - facets.shape.bandwidth_mbit: 80
  - facets.shape.price_usd_month: 17.9
  - facets.shape.price_usd_month_3y_prepay: 9.8
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: announcement index states 'Bare Metal! 60% OFF discount code CSTOU4 Premium Network Bare Metal Monthly plans from $17.9, Flash Sale: 3-year plan only $9.8/month' with Hong Kong, Japan, Los Angeles and Frankfurt test IPs, dated 20th August 2026
  - [2] 2026-08-20: table row 'E5-2620 (12C) | 16G | $17.9//month' with purchase links labelled 'Buy DE-120G SSD-80M', 'Buy LA-120G SSD-30M', 'Buy JP-120G SSD-50M', 'Buy HK-120G SSD-30M', 'Buy HK-1T SAS-30M'
  - [2] 2026-08-20: the same table lists 'Dual E5-2680 (40C) | 32G | $89.9//month' and 'Dual E5-2650 (32C) | 32G | $79.9//month'
- sources:
  - [1] https://cstserver.com/index.php?rp=/announcements
  - [2] https://cstserver.com/index.php?rp=/announcements/46/
