# PPIO GPU

> ppio.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ppio/ | JSON https://fshy.ajam.dev/api/v1/entity/ppio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PPIO Agent Sandbox

- `compute/ppio-sandbox` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:55.000Z (live) | stale on 2026-11-22
- url https://ppio.com/docs/sandbox/pricing.md
- free tier: no free tier: vCPU and RAM bill independently per second, and billing stops when a sandbox stops; any credit is an account voucher described on the billing page | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: vCPU and RAM bill independently per second; billing stops when the sandbox stops [1]
  - write-gated (binding): no published free tier: credit exists only as an account voucher or top-up [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing documentation was read on 2026-10-22 (Chinese). It defines billing per second on vCPU and RAM with billing stopped on sandbox stop, and states no free tier; vouchers are an account balance rather than a published allowance
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: billing stops when a sandbox stops, so stopping is the cost lever; the page states no automatic reap
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'PPIO Sandbox 支持 vCPU 与内存（RAM）按秒独立计费' - vCPU and RAM bill separately per second - with '沙箱停止后不再计费' on both rows: billing stops when a sandbox stops. The page states no free tier and points at an account voucher balance
- sources:
  - [1] https://ppio.com/docs/sandbox/pricing.md

## PPIO GPU

- `compute/ppio-gpu` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone unknown, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ppio.com/ai-computing/gpu-instance
- free tier: RTX 4090 24GB in a 16 vCPU / 62 GiB container at CNY 2.31 per card-hour on demand or CNY 1.16 per card-hour preemptible; H20 96GB at CNY 6.80 or CNY 3.40; H100 SXM 80GB at CNY 23.76 or CNY 11.88; H200 141GB listed as new stock. Storage is free to 100 GB and the page states preemptible capacity saves about 50 percent, quoted. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The GPU page links to ppio.com/user/register, but the form fields were not read, so whether a mainland mobile number or a real-name check is required is not established. The provider is a mainland company with an international storefront.
- interface: unknown
- limits note: Nothing is metered except wall-clock GPU time. The spot lane is the first thing to fail, because a preemptible 4090 at CNY 1.16 is reclaimable and the on-demand price is exactly double.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A preemptible 4090 at CNY 1.16 an hour with 100 GB of free storage is the cheapest way to run a fine-tune that checkpoints often; the reclaim is the price of it.
- reliability: no reliability event recorded
- notes: The aggregator's 0 percent preemption figure is a measurement of the aggregator on 2026-10-22, not a guarantee from the vendor.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 16
  - facets.shape.ram_gib: 62
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: price cards for RTX 4090 24GB at ￥2.31/卡时 on demand and ￥1.16/卡时 preemptible, H20 96GB at ￥6.80 and ￥3.40, H100 SXM 80GB at ￥23.76 and ￥11.88, quoted
  - [1] 2026-10-22: page states 免费存储 100GB (100 GB of free storage) and 成本节省50% for preemptible capacity, quoted
  - [2] 2026-10-22: an independent price aggregator lists PPIO 4090 at USD 0.346 on demand and USD 0.174 spot in CN, with an observed preemption rate of 0 percent, consistent with the vendor figures at CNY 6.67 per USD
- sources:
  - [1] https://ppio.com/ai-computing/gpu-instance
  - [2] https://www.suanli.ai/gpus/RTX-4090
