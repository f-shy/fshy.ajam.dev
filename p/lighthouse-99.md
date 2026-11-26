# Lighthouse 99

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lighthouse-99/ | JSON https://fshy.ajam.dev/api/v1/entity/lighthouse-99.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lighthouse 99

- `compute/lighthouse-99` | paid-only | evidence reported | binding volume-quota | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-11-25T16:38:11.710Z (live) | stale on 2026-12-10
- url https://www.v2ex.com/t/1179248
- free tier: An overseas Lighthouse instance at CNY 99 a year: 2 cores, 2GB RAM, 30M bandwidth, 1 TB traffic a month, open to new and existing users, with one same-price renewal so CNY 198 covers two years. The next shape is 2 cores, 4GB RAM, 30M bandwidth, 1.5 TB traffic a month at CNY 199 a year, also with one same-price renewal. The poster tested Silicon Valley, Singapore, Seoul and Tokyo. | unit: TB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
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
  - [2] 2026-11-25: the thread states the 99-yuan overseas 2-core/2GB/30M/1TB offer, no restriction on new or existing users, the one-year same-price renewal to 198 yuan over two years, the 199-yuan 2-core/4GB/1.5TB shape and the tested regions | capture: sha256:484bdbff453e975749f6f8d914a1f94c16d3669022d9eac94af8be76d4550387 | quote: 腾讯云 3 月份的时候推出 99 元境内/境外轻量应用服务器活动，这个活动不限制腾讯云新老用户，而且购买后还可以 99 元再续费一年。 ... 境外 2 核心 2GB 内存 30M 带宽每月 1TB 流量仅 99 元，可同价续费 1 年即 198 元 / 2 年 ... 境外 2 核心 4GB 内存 30M 带宽每月 1.5TB 流量仅 199 元，可同价续费 1 年即 398 元 / 年 ... 楼主测试了硅谷、新加坡、首尔和东京
  - [2] 2026-11-25: the thread still states the 99-yuan overseas offer, its new/existing-user eligibility, the same-price renewal, the 199-yuan shape and the tested regions | capture: sha256:484bdbff453e975749f6f8d914a1f94c16d3669022d9eac94af8be76d4550387 | quote: 腾讯云 3 月份的时候推出 99 元境内/境外轻量应用服务器活动，这个活动不限制腾讯云新老用户，而且购买后还可以 99 元再续费一年。 ... 境外 2 核心 2GB 内存 30M 带宽每月 1TB 流量仅 99 元，可同价续费 1 年即 198 元 / 2 年 ... 境外 2 核心 4GB 内存 30M 带宽每月 1.5TB 流量仅 199 元，可同价续费 1 年即 398 元 / 年 ... 楼主测试了硅谷、新加坡、首尔和东京
  - [2] 2026-11-25: the headline overseas 99-yuan shape has 1 TB of monthly traffic, so the allowance's unit is TB | capture: sha256:484bdbff453e975749f6f8d914a1f94c16d3669022d9eac94af8be76d4550387 | quote: 境外 2 核心 2GB 内存 30M 带宽每月 1TB 流量仅 99 元，可同价续费 1 年即 198 元 / 2 年
  - [2] 2026-11-25: the thread still states the overseas 99-yuan shape with 1 TB of monthly traffic | capture: sha256:484bdbff453e975749f6f8d914a1f94c16d3669022d9eac94af8be76d4550387 | quote: 境外 2 核心 2GB 内存 30M 带宽每月 1TB 流量仅 99 元，可同价续费 1 年即 198 元 / 2 年
- sources:
  - [1] https://www.v2ex.com/t/1179248
  - [2] https://www.v2ex.com/t/1125596
  - [3] https://www.v2ex.com/t/1198372
  - [4] https://cloud.tencent.com/act/pro/campus2026
