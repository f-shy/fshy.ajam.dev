# Zettabyte

> zettabyte.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zettabyte/ | JSON https://fshy.ajam.dev/api/v1/entity/zettabyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zettabyte (zCLOUD)

- `compute/zettabyte` | paid-only | evidence documented | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:22.537Z (live) | stale on 2026-12-04
- url https://zettabyte.com/
- free tier: No free tier. On-demand H100 GPUs from USD 3.59 per GPU-hour on the vendor page, and USD 2.51 per GPU-hour on the index read 2026-10-27. Rates are indicative floors set at allocation by a bid and ask across 40 or more supply providers; H200 and Blackwell are by request through sales. The index lists no A100, L40S, RTX 4090 or L4. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: not applicable | source: [1]
- egress: not published on the pages read | metered: no | source: [1]
- identity: email | detail: unverified: no self-service signup page was read. The on-demand page carries a contact form asking for full name, work email, company and a message, and states that pricing can be seen without signing anything. Whether a card, KYC or a sales contract is needed to allocate on-demand capacity is not stated.
- interface: unknown
- limits note: No quota is stated: the published rate is an indicative floor and the exact rate is set at allocation, so the price is the open variable.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: unverified: no API, CLI or SSH detail on the pages read; the vendor states on-demand instances launch in seconds.
- composes with: An aggregator of other hosts' capacity with a floor price that moves at allocation; the H100 is the only self-serve card. It is not a source for the A100, L40S, RTX 4090 or L4.
- reliability: The index notes dependency on third-party hardware providers and no stated support options; the vendor states a 99.9% uptime SLA target. No outage was observed.
- notes: Found via computeprices, which links zettabytecloud.com; the vendor's own pages are on zettabyte.com and zettabytecloud.com. The index price (USD 2.51) and the vendor from-rate (USD 3.59) differ by 43 percent; the vendor calls its rates indicative floors set at allocation.
- evidence:
  - [2] 2026-11-03: the index lists the H100 SXM 80 GB at USD 2.51 per GPU-hour, collected 2026-10-27; it lists no A100, L40S, RTX 4090 or L4 for this provider | capture: sha256:2036e42f3d0cfb1da30b0421dee4aa92d35ee7b411d84bce8254ec98926f8dcc | quote: | [H100 SXM](https://computeprices.com/providers/zettabytecloud/gpus/h100)1× | $2.51/hr |
  - [1] 2026-11-03: the vendor page states a from-rate of USD 3.59 per GPU-hour for the on-demand H100, above the index's USD 2.51 | capture: sha256:3267cfb68a9d3ee68206c4fc671b9122659d4e03e977581db38d9bc2ad249248 | quote: On-Demand H100 GPUs from $3.59 / GPU-hour
  - [1] 2026-11-03: published rates are floors; the rate is set at allocation by bid and ask | capture: sha256:3267cfb68a9d3ee68206c4fc671b9122659d4e03e977581db38d9bc2ad249248 | quote: Published rates are indicative floors. Your exact rate is set at allocation from live bid/ask supply.
  - [3] 2026-11-03: only the H100 is self-serve; H200 and Blackwell go through sales | capture: sha256:595291aeb929ea09393a04d24765304bec780c750ae76bb1f59dcf9fc7c869a2 | quote: H100 is available today at the rates shown above. H200 and Blackwell are available on request through sales.
  - [3] 2026-11-03: on-demand has no commitment; reserved capacity is a term commitment | capture: sha256:595291aeb929ea09393a04d24765304bec780c750ae76bb1f59dcf9fc7c869a2 | quote: On-demand has no commitment. Reserved capacity is a term commitment.
  - [1] 2026-11-03: the only form on the on-demand page is a sales contact form with name, work email, company and message | capture: sha256:3267cfb68a9d3ee68206c4fc671b9122659d4e03e977581db38d9bc2ad249248 | quote: Work email
- sources:
  - [1] https://zettabyte.com/zcloud/on-demand
  - [2] https://computeprices.com/providers/zettabytecloud
  - [3] https://zettabytecloud.com/pricing
