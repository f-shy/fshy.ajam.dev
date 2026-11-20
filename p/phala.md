# Phala Cloud

> phala.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/phala/ | JSON https://fshy.ajam.dev/api/v1/entity/phala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Phala Cloud

- `compute/phala-cloud` | paid-only | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://phala.com/pricing
- free tier: Confidential VMs from USD 0.06 per hour and GPU TEE capacity from USD 4.40 per hour, billed per minute, with storage at USD 0.000139 per GB per hour charged while the CVM exists whether it runs or not. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: card or a balance top-up: signup is 'with GitHub, Google or email', then the first step is 'add a card or top up your Balance to start deploying', so a payment instrument is required before any CVM exists and a prepaid balance is the stated alternative to a card. No authorisation or hold amount is stated, and whether debit is accepted is not stated: unknown.
- interface: unknown
- limits:
  - write-gated (binding): The documentation's first step after signup is 'add a card or top up your Balance to start deploying', so no CVM exists without a payment instrument. [1]
- limits note: The documentation's first step after signup is 'add a card or top up your Balance to start deploying', so no CVM exists without a payment instrument.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Phala is the cheapest attested-TEE lane found among the category's DePIN records, but it is a prepaid invoice rather than a credit, so it does not chain with a zero-budget start.
- reliability: no reliability event recorded
- notes: A promotional credit may exist behind the signup login and was not visible; neither the pricing page nor the quick start shows one. Hourly rates are list prices, not measured.
- extras:
  - facets.class: paid-cloud
  - facets.shape.gpu_class: H100/H200/B300 TEE
- evidence:
  - [1] 2026-10-22: CVM from USD 0.06/hour, GPU TEE from USD 4.40/hour, disk USD 0.000139/GB/hour, storage billed while stopped
  - [2] 2026-10-22: signup with GitHub, Google or email, then 'add a card or top up your Balance to start deploying'
- sources:
  - [1] https://phala.com/pricing
  - [2] https://docs.phala.network/phala-cloud/getting-started
