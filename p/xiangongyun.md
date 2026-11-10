# Xiangongyun

> xiangongyun.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xiangongyun/ | JSON https://fshy.ajam.dev/api/v1/entity/xiangongyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xiangongyun

- `compute/xiangongyun` | paid-only | evidence reported | binding none | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.xiangongyun.com/
- free tier: Per-minute GPU rental with a public price list. An aggregator that polls the vendor daily records RTX 4090D 48GB stock in Zhejiang at USD 0.194 per card-hour on a monthly rate and USD 0.238 on demand, and RTX 4090 24GB at a minimum of USD 0.231 per card-hour. The vendor page states 按量计费，部署不计费，用多少付多少 (metered by usage, deployment is not billed, you pay for what you use), quoted. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The registration form was not read; the provider sells in CNY to a mainland audience, and the gate is not established here.
- interface: unknown
- limits note: Nothing throttles per job. The first thing to fail is availability: the aggregator's cheapest row for this vendor is monthly-rate 4090D stock in one region, and third-party price tables note queueing at peak.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 48 GB card at USD 0.20 an hour changes which models fit: a 32B model in 4-bit needs more than 24 GB, and this is the cheapest listed way to rent past that line.
- reliability: no reliability event recorded
- notes: New to documented records. Two third-party price tables disagree with the aggregator on this vendor: hcit.com.cn lists a 24 GB 4090 at CNY 1.78 an hour and datalearner lists CNY 2.37 an hour, both older. The vendor renders its price table in client-side script, so the CNY figure could not be read from the page itself; the aggregator's USD figure is recorded and the CNY disagreement is left in place rather than resolved by picking one. Open question: the CNY list price on 2026-10-22.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 4090D 48GB
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 48
- evidence:
  - [1] 2026-10-22: front page states 按量计费，部署不计费，用多少付多少 and 即刻开始部署, quoted
  - [2] 2026-10-22: aggregator price page for 仙宫云 lists RTX 4090D 48GB at USD 0.194 per card-hour monthly and USD 0.238 on demand in CN 浙江一区, and RTX 4090 minimum USD 0.231
  - [3] 2026-10-22: a 4090D 48GB modified card is sold by this vendor, so the 24 GB and 48 GB rows are different products
- sources:
  - [1] https://www.xiangongyun.com/
  - [2] https://www.suanli.ai/provider/175
  - [3] https://www.suanli.ai/gpu/20732
