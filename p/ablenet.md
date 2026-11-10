# ABLENET VPS

> ablenet.jp | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ablenet/ | JSON https://fshy.ajam.dev/api/v1/entity/ablenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ABLENET VPS

- `compute/ablenet-vps` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:24:47.110Z (live) | stale on 2026-12-05
- url https://www.ablenet.jp/vps/
- free tier: A ten-day free trial on every Linux plan, with no automatic conversion to a paid contract, no minimum period, the first month free and no setup fee except on the L0 plan. L0 is 0.5 GB memory with 1 virtual core and 30 GB SSD or 50 GB HDD at JPY 554 a month including tax; L1 is JPY 968; the ladder runs to L7 at 64 GB. The L0 setup fee is JPY 1,130. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: time-boxed-trial
- per-object cap: not applicable | source: [1]
- retention: The trial is ten days and the L0 plan cannot be reached by downgrading an existing larger plan, so the cheap shape is only available to a new order; after ten days the box either converts at full price or is discarded with its contents. | source: [1]
- egress: Data transfer unlimited ('転送量 無制限'), line 200Mbps shared; no overage price | metered: no | free allowance: unlimited | source: [1]
- identity: card
- interface: unknown
- limits:
  - retention-clamped (binding): The trial is ten days and the L0 plan cannot be reached by downgrading an existing larger plan, so the cheap shape is only available to a new order; after ten days the box either converts at full price or is discarded with its contents. [1]
- limits note: The trial is ten days and the L0 plan cannot be reached by downgrading an existing larger plan, so the cheap shape is only available to a new order; after ten days the box either converts at full price or is discarded with its contents.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the Japanese trial that does not convert silently, which makes it the safe half of a pair with Sakura VPS: use ABLENET for a ten-day job you intend to abandon and Sakura for one you intend to keep.
- reliability: no reliability event recorded
- notes: The distinguishing fact against Sakura VPS and XServer VPS is the absence of automatic conversion; the vendor says so in its own copy and a press release repeats it. Prices are tax-inclusive yen as printed. Whether ABLENET accepts a non-Japanese card or address at signup is not stated on the pages read, so the identity cost is recorded as card with that gap named.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: time-boxed-trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page states a ten-day free trial, no minimum period ('最低利用期間もございません'), the first month free, no setup fee except on L0, and a ladder from L0 at 554 円 a month with 0.5 GB to L7 at 64 GB, with 15 plans including Windows; it states that the trial state carries over to a paid contract
  - [2] 2026-10-22: the order form gives L0 at 554 円 a month including tax with a 1,130 円 initial fee, 1 virtual core and 0.5 GB memory, and L1 at 968 円 a month
  - [3] 2026-10-22: a press release states that the Linux VPS line was renewed to eight plans L0 to L7 from 0.5 GB to 64 GB, from 554 円 a month including tax, with a trial of up to ten days and no minimum period; reported
  - [4] 2026-11-03: data transfer is unlimited | capture: sha256:6c916299297f7d2f41b7c467b400126ab5f2a3ebdae946b55573b166ef8321fc | quote: | 転送量 | 無制限 |
- sources:
  - [1] https://www.ablenet.jp/vps/
  - [2] https://www.ablenet.jp/vps/order/index_v.cgi
  - [3] https://news.infoseek.co.jp/article/atpress_616800/
  - [4] https://www.ablenet.jp/vps/spec/index.html
