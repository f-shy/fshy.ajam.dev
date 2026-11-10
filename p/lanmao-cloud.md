# Lanmao Cloud

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lanmao-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/lanmao-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lanmao Cloud

- `compute/lanmao-cloud` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.nodeseek.com/post-620036-1
- free tier: The lowest absolute price found among evaluated providers: a Hong Kong NAT instance at CNY 2.62 a month with 2 TB of traffic, tested and posted by a user in a 75-percent-off promotion. A Singapore StarHub-shape instance at 1 vCPU / 256 MB / 500 GB renews at CNY 12 a month. The merchant also issues free machines, mostly a Japanese line it calls 狗妈, and resale listings trade those free instances at CNY 180 to CNY 600, which is the market's own valuation of a perpetual-free box. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: A NAT instance shares one IPv4 with other tenants and is reached by port mapping, so the first thing that fails is inbound service, not bandwidth; the 2 TB allowance sits behind a shared address and a reseller-priced coupon, and a coupon that is not renewed ends the machine. | metered: yes | source: [1]
- identity: institution | detail: Not established. The merchant sells through its own panel and the forum threads describe purchases and transfers, not the signup fields.
- interface: unknown
- limits:
  - per-ip-shaping (binding): A NAT instance shares one IPv4 with other tenants and is reached by port mapping, so the first thing that fails is inbound service, not bandwidth; the 2 TB allowance sits behind a shared address and a reseller-priced coupon, and a coupon that is not renewed ends the machine. [1]
- limits note: A NAT instance shares one IPv4 with other tenants and is reached by port mapping, so the first thing that fails is inbound service, not bandwidth; the 2 TB allowance sits behind a shared address and a reseller-priced coupon, and a coupon that is not renewed ends the machine.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: CNY 2.62 a month for a Hong Kong NAT box with 2 TB is the cheapest egress-heavy node found, and it composes with a tunnel for inbound; the shared IPv4 and the coupon dependency are what break it.
- reliability: no reliability event recorded
- notes: New to earlier readings, and the cheapest monthly figure in evaluated offerings. Two cautions are recorded in the entry itself: the 2.62 figure came from a promotion code and is not the list price, and the free machines are a marketing device whose renewal depends on the merchant continuing to hand out coupons. The resale prices are the most useful datum, because they show what the market pays for a perpetual-free instance when it cannot be obtained directly.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: perpetual
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.25
- evidence:
  - [1] 2026-10-22: a test post is titled 懒猫云香港1区NAT湾仔Basic ￥2.62/月 2TB and states the buyer used a 75-percent-off code, quoted from the snippet
  - [2] 2026-10-22: a resale listing gives a StarHub Nano shape at 1 core / 256 MB / 500 GB with 续费价格 ￥12.00 / 1个月 and a permanent 20-percent discount, quoted
  - [3] 2026-10-22: free machines are traded as inventory: 日本免费机...每台 550, 日本 kddi 二区 免费机...每台 180, quoted
  - [4] 2026-10-22: the merchant is described as 新起的Nat小鸡商家 that issues free machines from time to time, which dates the operation to a recent entrant
- sources:
  - [1] https://www.nodeseek.com/post-620036-1
  - [2] https://www.nodeseek.com/post-944640-1
  - [3] https://www.nodeseek.com/post-966472-1
  - [4] https://www.nodeseek.com/post-470939-1
