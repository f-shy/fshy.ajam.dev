# OpenRelay

> openrelay.inc | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openrelay/ | JSON https://fshy.ajam.dev/api/v1/entity/openrelay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenRelay

- `compute/openrelay` | paid-only | evidence documented | binding none | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://openrelay.inc/gpus
- free tier: no free GPU tier is published; list rates per GPU-hour from the GPU catalog read on 2026-11-03: RTX 3090 USD 0.18, RTX 4090 USD 0.35, RTX 5090 USD 0.50, A100 80GB USD 1.10, RTX Pro 6000 USD 1.55, H100 SXM USD 2.60, B200 USD 6.30, AMD Instinct MI355X USD 6.30, B300 USD 8.49. The catalog lists no L40S and no L4. 'No commitment, no quota request, no reservation.' | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: multi-GPU VMs multiply the per-GPU rate; the aggregator shows a community and a verified lane for some cards (L4 at USD 0.43 community, USD 0.55 verified) that the provider catalog page does not list
- per-object cap: not applicable | source: [1] | note: a VM with the GPU passed through, or a bring-your-own-container pod
- retention: not applicable | source: [1] | note: a machine record
- egress: not published on the pages read | metered: no | source: [1]
- identity: card | detail: The catalog says 'Add a card and make a deposit to test.' The terms page says an account must be registered; no phone or ID document is stated on the pages read. The sign-up page itself answered 404 and was not read.
- interface: rest
- limits note: No quota is stated; the rate list is the constraint, and capacity is on distributed hardware that can go down.
- binding note: the same as limits note
- interface detail: inferred from the index, which names a /v1 API and an OpenAI-compatible gateway; not probed
- tooling: GPU VMs and container pods from a web console; an OpenAI- and Anthropic-compatible inference gateway at inference.openrelay.inc/v1; the index says the service was formerly VectorLay and is in early access
- composes with: Per-GPU hourly rates for A100 80GB, H100 SXM and RTX 4090 with no commitment, next to an OpenAI-compatible inference API on the same account.
- reliability: The terms page states 'Our Services run on distributed consumer hardware, and individual nodes may experience downtime.' The index states early access.
- notes: Found via computeprices.com (provider slug openrelay). Not to be confused with Metered Open Relay (storage/metered-open-relay-at-the-advertised-20-gb), a different service. Not read: the L4 and L40S rows, which the aggregator lists but the provider catalog does not, and the sign-up and deposit minimum.
- evidence:
  - [1] 2026-11-03: RTX 4090 list rate USD 0.35 per GPU-hour | capture: sha256:6ccb308d048f6d6e69e73c4ba703ad3ba13f532d16882fb3c762209666887070 | quote: | NVIDIA RTX 4090 | 24GB GDDR6X | $0.35/hr | $252/mo |
  - [1] 2026-11-03: A100 80GB list rate USD 1.10 per GPU-hour | capture: sha256:6ccb308d048f6d6e69e73c4ba703ad3ba13f532d16882fb3c762209666887070 | quote: | NVIDIA A100 80GB | 80GB HBM2e | $1.10/hr | $792/mo |
  - [1] 2026-11-03: H100 SXM list rate USD 2.60 per GPU-hour | capture: sha256:6ccb308d048f6d6e69e73c4ba703ad3ba13f532d16882fb3c762209666887070 | quote: | NVIDIA H100 SXM | 80GB HBM3 | $2.60/hr | $1,872/mo |
  - [1] 2026-11-03: no commitment or quota; a card and a deposit are needed | capture: sha256:6ccb308d048f6d6e69e73c4ba703ad3ba13f532d16882fb3c762209666887070 | quote: No commitment, no quota request, no reservation. Add a card and make a deposit to test.
  - [2] 2026-11-03: capacity is distributed hardware with node downtime | capture: sha256:688c679169d78a3f1af309b188100a8a5845b8e0f2364b012aabdc6f9f0c58f1 | quote: Our Services run on distributed consumer hardware, and individual nodes may experience downtime.
  - [3] 2026-11-03: the aggregator lists an L4 community lane at USD 0.430 an hour | capture: sha256:1c089c0085635e0e5db46098046ad0eb0b98ece732f6ae5aaa1866709fbbdaa3 | quote: | [L4](https://computeprices.com/providers/openrelay/gpus/l4) | $0.430/hrcommunity | 24GB | 1× | 11/3/2026 | [Rent](https://openrelay.inc/gpus?utm_source=computeprices&utm_medium=referral&utm_campaign=gpu-pricing) |
- sources:
  - [1] https://openrelay.inc/gpus
  - [2] https://openrelay.inc/terms
  - [3] https://computeprices.com/providers/openrelay
