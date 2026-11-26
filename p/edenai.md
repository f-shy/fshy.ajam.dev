# Eden AI

> edenai.co | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/edenai/ | JSON https://fshy.ajam.dev/api/v1/entity/edenai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Eden AI

- `inference/edenai` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://www.edenai.co/pricing
- free tier: No free allowance is stated on the pricing page read 2026-11-18: pay-as-you-go at provider prices with no markup plus a 5.5% platform fee when buying credits; no subscription, seat fees or API call limit. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: credits are bought with a credit card or bank transfer (Stripe)
- interface: rest
- limits:
  - volume-quota (binding): provider prices with 0% markup plus 5.5% fee on credit purchase; no API call limit stated [1]
- endpoint: https://api.edenai.run/v3
- tooling: an OpenAI-compatible key against the unified 500+ model endpoint
- composes with: the 5.5% credit-purchase fee is the scarce link; no free text tier is published
- reliability: no subscription or API call limit, but usage needs purchased credits
- evidence:
  - [1] 2026-11-18: pay-as-you-go with a 5.5% credit purchase fee and no subscription | capture: sha256:ca6ffab67175c5309921a3848d0d24f2b3aa0e26b984deaf0a63694e28f3ec89 | quote: Pay-as-you-go: provider prices with no markup, plus a 5.5% platform fee when you buy credits. No subscription.
- sources:
  - [1] https://www.edenai.co/pricing
