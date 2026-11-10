# SambaNova Cloud

> sambanova.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sambanova/ | JSON https://fshy.ajam.dev/api/v1/entity/sambanova.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SambaNova Cloud

- `compute/sambanova-cloud` | fails-identity | evidence documented | binding write-gated | category inference API
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T05:38:57.839Z (live) | stale on 2026-12-05
- url https://cloud.sambanova.ai/plans
- free tier: No free lane left. The Free plan now reads 'Add a payment method and purchase credits to run your first requests'; the prior offer was USD 5 of free API credits with no card required, expiring after 30 days, and that grant was dropped on 2026-08-14. The rate-limit documentation still describes a 'Free Tier: Applied when there is no payment method linked with your account', which contradicts the plans page. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a payment method and purchased credits before the first request: the plans page reads "Add a payment method and purchase credits to run your first requests", and the previous USD 5 no-card grant was dropped on 2026-08-14. The record does not name which payment methods are accepted, whether a card is required rather than another rail, any hold, debit or prepaid acceptance, or whether signup asks for an email or a phone. The rate-limit documentation still describes a "Free Tier: Applied when there is no payment method linked with your account", which contradicts the plans page
- interface: rest
- limits:
  - write-gated (binding): the free lane stops at the payment method, not at a quota: a call on an unfunded key returns 402 PAYMENT_METHOD_REQUIRED while /v1/models still answers 200, so a health check that reads the model list looks healthy while every completion is refused. [1]
- limits note: the free lane stops at the payment method, not at a quota: a call on an unfunded key returns 402 PAYMENT_METHOD_REQUIRED while /v1/models still answers 200, so a health check that reads the model list looks healthy while every completion is refused.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing composes: this category needs a card before the first request.
- reliability: no reliability event recorded
- notes: The 20M-tokens-a-day Developer Tier figure is recorded here only as what the docs claim, not as capacity that is available.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: Free plan text: 'Start exploring SambaNova Cloud. Add a payment method and purchase credits to run your first requests', quoted
  - [2] 2026-08-22: the USD 5 no-card free-credit grant was dropped on 2026-08-14; the Free plan is now pay-as-you-go credits requiring a payment method
  - [3] 2026-10-22: documentation still lists 'Free Tier: Applied when there is no payment method linked with your account' and a Developer Tier at 20M tokens per day across all models, which contradicts the plans page
  - [1] 2026-11-03: the Free plan on the plans page still requires a payment method and purchased credits | capture: sha256:9c6e87258527ddaa1c1d2917dc2f7fd7550c005d9076a9e077560f611941c7a2 | quote: Add a payment method and purchase credits to run your first requests.
  - [4] 2026-11-03: a third-party live test on 2026-08-31 of a free account was refused with 402 | capture: sha256:a2400800e62f2a75c6543d2b4b646127198ca13c93234592614a702640c165cd | quote: In our own test on 2026-08-31 a free account got `402 PAYMENT_METHOD_REQUIRED` with a zero balance
- sources:
  - [1] https://cloud.sambanova.ai/plans
  - [2] https://www.usagepricing.com/blueprint/activity/sambanova-2026-08-14-free-credit-grant-dropped
  - [3] https://docs.sambanova.ai/docs/en/models/rate-limits
  - [4] https://toolfreebie.com/sambanova-cloud-free-api/
