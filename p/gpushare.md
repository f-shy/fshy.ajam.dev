# gpushare

> gpushare.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpushare/ | JSON https://fshy.ajam.dev/api/v1/entity/gpushare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gpushare

- `compute/gpushare` | paid-only | evidence reported | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://gpushare.com/docs/product/price/
- free tier: Per-second metered GPU rental with an unusual funding gate. The vendor's own price document states that an account with no deposit may run one instance with one card, a deposit under CNY 100 raises that to three instances with one card each, and a deposit of CNY 100 or more removes the per-instance card limit. Each instance carries 50 GB of free local disk at /hy-tmp, with extra space at CNY 0.0004 per GB-hour. Third-party price pages that poll the vendor list RTX 4090 at CNY 2.00 an hour in east China, a 4090D at CNY 1.10 in the north-west, a 48 GB 4090 at CNY 3.45 in the south-west and an RTX 3090 at CNY 0.98, and one of them marks the vendor 免实名 (no real-name check) with Alipay and WeChat accepted. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: A third-party listing states (no real-name verification), which if true makes this the only cheap mainland GPU host among evaluated providers that a person without a Chinese identity document can use. The claim is from a price directory, not from the vendor, so it is classified as the reason to check rather than as established.
- interface: unknown
- limits note: The first thing to fail is the funding tier, not a quota: with less than CNY 100 on the account the run is capped at one card per instance, so a multi-card job needs the deposit before it can be started at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Per-second billing with a free 50 GB local scratch disk means a checkpoint-heavy job costs only the seconds it runs, and the CNY 100 deposit that unlocks multi-card is the same money spent on the run.
- reliability: no reliability event recorded
- notes: New to earlier readings. The vendor's own document carries the billing and funding mechanics but its per-card price table is rendered in script and did not extract, so the rates come from two independent price directories and are reported. The claim is the most consequential single fact in this record: it is the difference between a cheap GPU host a foreign client can use and one more fails-identity entry, and it is unverified. Open question: what the vendor's own order page asks for at registration.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: the document states the funding ladder 未充值 1 instance and 1 card, 充值小于100 3 instances and 1 card, 充值大于等于100 no card limit, and per-second billing settled hourly with a one-hour freeze, quoted
  - [1] 2026-10-22: the document states 50 GB of /hy-tmp per instance free and extra capacity at 每GB 0.0004元/小时, and that a shut-down pay-as-you-go instance has its local disk deleted after 24 hours, quoted
  - [2] 2026-10-22: a price directory lists 华东4090云主机 at ¥2.00/小时 provided by 恒源云, and the same directory entry marks the vendor 免实名 with 支付宝 and 微信 accepted
  - [3] 2026-10-22: a second directory lists 西北4090D云主机 at ¥1.10/小时 provided by 恒源云
- sources:
  - [1] https://gpushare.com/docs/product/price/
  - [2] https://www.gpu114.com/gpu/490.html
  - [3] https://www.dxnt.com/gpu/491.html
