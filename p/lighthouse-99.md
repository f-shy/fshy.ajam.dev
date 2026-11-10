# Lighthouse 99

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lighthouse-99/ | JSON https://fshy.ajam.dev/api/v1/entity/lighthouse-99.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lighthouse 99

- `compute/lighthouse-99` | paid-only | evidence reported | binding volume-quota | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.v2ex.com/t/1179248
- free tier: A Lighthouse instance in an overseas region at CNY 99 a year: 2 vCPU, 2 GiB RAM, 30 Mbps, 1000 GB a month, buyable by new and existing Tencent Cloud accounts and renewable once at the same price, so CNY 198 covers two years. The next shape up is 2 vCPU / 4 GiB / 30 Mbps / 1500 GB at CNY 199 a year. Regions named across the threads are Singapore, Tokyo, Seoul, Silicon Valley, Frankfurt, Shanghai, Guangzhou and Beijing, and the plan includes free IP replacement. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id | detail: The promotion runs on the mainland storefront cloud.tencent.com, which requires a real-name verified account before any purchase; the international storefront tencentcloud.com sells Lighthouse separately and is not covered by this price.
- interface: unknown
- limits:
  - volume-quota (binding): One terabyte a month at 30 Mbps is the first thing to bind, and at the stated port speed a full month of saturation would move far more than the cap, so the plan is a service box. The renewal limit is the second: the same price is good for one renewal only, after which the list price applies. [1]
- limits note: One terabyte a month at 30 Mbps is the first thing to bind, and at the stated port speed a full month of saturation would move far more than the cap, so the plan is a service box. The renewal limit is the second: the same price is good for one renewal only, after which the list price applies.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: CNY 99 for two years of a 30 Mbps overseas box is the cheapest credible origin among evaluated providers, and it composes with a free CDN in front to take the 1 TB cap off the serving path; the annual renewal is the only cliff.
- reliability: no reliability event recorded
- notes: earlier readings holds tencent-cloud-international.json, which records the international free trial and marks it fails-identity, but it does not record this domestic promotion, so the cheapest Tencent shape was missing. The promotion recurs and the v2ex threads span several months, each restating the same configuration; no vendor page with the price was read, because the activity page is script-rendered, so this is reported rather than documented. The 528 yuan three-year domestic shape (2C4G 6M) is for first-time Lighthouse buyers only and is noted here rather than given its own record.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
- evidence:
  - [1] 2026-10-22: the post states 境外 CN2/境内轻量服务器：2C+2GB+30Mbps+1000GB/月，不限新老用户，每年 99 元购买后可同价续费 1 年 and 2C+4GB+30Mbps+1500GB/月...每年 199 元, quoted from the snippet
  - [2] 2026-10-22: an earlier post states the offer 不限制腾讯云新老用户 and that the buyer can renew one more year at 99 元, quoted
  - [3] 2026-10-22: a later post lists the selectable regions as 新加坡、东京、首尔、硅谷、法兰克福、上海、广州、北京 and repeats the 99 元 starting price
  - [4] 2026-10-22: the campus page is live and lists 轻量应用服务器 2核2G, 2核4G and CVM 2核4G as the three student shapes, which is a different offer from the 99 yuan plan
- sources:
  - [1] https://www.v2ex.com/t/1179248
  - [2] https://www.v2ex.com/t/1125596
  - [3] https://www.v2ex.com/t/1198372
  - [4] https://cloud.tencent.com/act/pro/campus2026
