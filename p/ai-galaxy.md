# AI Galaxy

> ai-galaxy.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ai-galaxy/ | JSON https://fshy.ajam.dev/api/v1/entity/ai-galaxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI Galaxy

- `compute/ai-galaxy` | paid-only | evidence reported | binding none | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-06T18:39:12.189Z (live) | stale on 2026-11-21
- url https://www.ai-galaxy.com/stu
- free tier: A registration coupon on the vendor's student page, in CNY: the sign-up box reads '新注册用户 1000元优惠券' (CNY 1,000 coupon for new users). The low-price tier on the same page prices RTX 3080 at CNY 0.77 an hour, RTX 3090 at CNY 1.10, RTX 4090 24G at CNY 1.65, RTX 4090 48G at CNY 2.53 and RTX 5090 32G at CNY 3.16. At the RTX 4090 24G rate the coupon is 606 GPU-hours. | unit: GiB | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Not established: the signup flow was not entered. The vendor is a mainland company ( per its own pages) selling in CNY.
- interface: unknown
- limits note: Nothing throttles a job; the constraint is the hourly meter plus availability, since the cheapest tier is a shared pool and the vendor's own business page prices the same cards higher for dedicated use.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: CNY 1.65 an hour is the middle of the Chinese 4090 market and the 48 GB card at CNY 2.53 is the cheap route past the 24 GB limit, which is what decides whether a 32B model fits.
- reliability: no reliability event recorded
- notes: Per-card hourly rates on the vendor's low-price tier, CNY per hour: RTX 3080 CNY 0.77, RTX 3090 CNY 1.10, RTX 4090 24G CNY 1.65, RTX 4090 48G CNY 2.53, RTX 5090 32G CNY 3.16. H100, A100 80 GB, L40S and L4: not listed, since the tier names none of them. The individual-developer page states the coupon at CNY 500 ('注册即领500元优惠券'), not the CNY 1,000 of the student page, and at CNY 1.65 an hour that is 303 RTX 4090 24G GPU-hours. A third-party aggregator lists the same 4090 at USD 0.192 per card-hour on an annual rate for CN-华东 with eight cards per instance, a different billing mode from the hourly tier.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: the page's price cards, captured by the search index because the page extractor returned only navigation text: RTX 3080 ¥0.77/小时, RTX 3090 ¥1.10/小时, RTX 4090 24G ¥1.65/小时, RTX 4090 48G ¥2.53/小时, quoted
  - [2] 2026-10-22: the individual-developer page carries the same four prices, which shows the student label does not change the rate
  - [3] 2026-10-22: an independent aggregator lists 智星云 4090 at USD 0.192 per card-hour on an annual rate for CN-华东 with eight cards per instance, a different billing mode from the hourly student price
  - [1] 2026-11-06: the low-price tier prices a fifth card, the RTX 5090 32G, at CNY 3.16 an hour | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ¥3.16/小时
  - [1] 2026-11-06: the student page's low-price tier prints the RTX 4090 24G rate | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ¥1.65/小时
  - [1] 2026-11-06: the low-price tier names an RTX 5090 32G card the note did not list | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ### RTX 5090 32G
  - [1] 2026-11-06: the RTX 4090 48G is CNY 2.53 an hour on the low-price tier | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ¥2.53/小时
  - [1] 2026-11-06: the RTX 5090 32G is CNY 3.16 an hour on the low-price tier | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ¥3.16/小时
  - [2] 2026-11-06: the individual-developer page still states the CNY 500 registration coupon, against the CNY 1,000 of the student page | capture: sha256:815e36e1cbcae440ba6eefd350a285915a58bba918ec0532be2493a49ead5b63 | quote: 低价稳定/预装环境/注册即领500元优惠券
  - [1] 2026-11-06: the RTX 4090 24G is CNY 1.65 an hour on the low-price tier | capture: sha256:7b32e7b6310122791f0423d9afff35e5e3ccef9a3a7db032be1fdcfe7dd510a2 | quote: ¥1.65/小时
- sources:
  - [1] https://www.ai-galaxy.com/stu
  - [2] https://www.ai-galaxy.com/user
  - [3] https://www.suanli.ai/provider/33
