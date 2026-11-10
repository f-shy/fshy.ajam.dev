# FriendliAI Model APIs

> friendli.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/friendli/ | JSON https://fshy.ajam.dev/api/v1/entity/friendli.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FriendliAI Model APIs

- `inference/friendli-ai` | paid-only | evidence documented | binding volume-quota | category inference API, prepaid credits, no standing free tier
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://friendli.ai/docs/guides/suite/credits
- free tier: none stated: teams use prepaid credits and API requests stop at a zero balance; promotional credits come from promo codes and 'may be restricted to a specific product, model, or GPU' | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: whether a new account receives a promotional credit at sign-up is unverified: behind a sign-up
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: sign-up is an account at Friendli Suite; the pages read state no card requirement at sign-up, but using the API needs purchased credits ($10 minimum) paid by credit or debit card (prepaid cards excluded), ACH on request, or AWS Marketplace
- interface: rest
- limits:
  - volume-quota (binding): prepaid credits only: $10 minimum purchase to continue; requests stop when the balance reaches $0 [1]
  - request-rate: tiered by lifetime spend; adding credits unlocks higher Model APIs rate limits; the per-tier numbers are not in the page text read [2]
- binding note: a prepaid balance is the only way to call the API once any promo credit is gone
- tooling: OpenAI-compatible client; a personal API key is created in Friendli Suite
- composes with: part of the free tier
- reliability: not measured
- notes: no free allowance is stated on the pages read; an account-only promo credit is unverified
- evidence:
  - [1] 2026-11-04: using the platform past promotional credits needs a $10 minimum purchase | capture: sha256:0085853915a5ba9aafe7d4e351c45d277363e4c7bf96e23fa5e421bc248e645b | quote: Purchase credits (\$10 minimum) to continue using the platform.
  - [1] 2026-11-04: prepaid credits come from a purchase of $10 minimum or auto recharge | capture: sha256:0085853915a5ba9aafe7d4e351c45d277363e4c7bf96e23fa5e421bc248e645b | quote: * Source: One-time purchase (\$10 minimum) or Auto Recharge
  - [3] 2026-11-04: prepaid billing stops requests at a zero balance | capture: sha256:819b4968e9e5b90e90a148c43ce9f3aa07c643306323016b71604dfb4c082745 | quote: Teams use prepaid credits: if your team has no remaining credits, API requests stop until you add more credits.
  - [3] 2026-11-04: card payment is the self-serve method | capture: sha256:819b4968e9e5b90e90a148c43ce9f3aa07c643306323016b71604dfb4c082745 | quote: * Credit and debit cards: FriendliAI accepts all major credit and debit cards, excluding prepaid cards.
  - [2] 2026-11-04: rate-limit tiers depend on lifetime spend | capture: sha256:28fd7b85d380334be96025f020fc511345cdeff5abcb8336edf58828d171843d | quote: Tiers are based on lifetime spending and update automatically.
  - [4] 2026-11-04: the quickstart names only an account sign-up and states no card at sign-up | capture: sha256:363708b6c9048404a38590979341ab125c1cfaf1b38b8286a4f41efafe06231b | quote: Create an account or sign in at [Friendli Suite](https://friendli.ai/suite).
- sources:
  - [1] https://friendli.ai/docs/guides/suite/credits
  - [2] https://friendli.ai/docs/guides/model-apis/rate-limits
  - [3] https://friendli.ai/docs/guides/suite/billing-payments
  - [4] https://friendli.ai/docs/guides/model-apis/quickstart
