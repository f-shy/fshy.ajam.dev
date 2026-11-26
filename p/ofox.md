# Ofox

> ofox.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ofox/ | JSON https://fshy.ajam.dev/api/v1/entity/ofox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ofox

- `inference/ofox` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://ofox.ai/docs/develop/observability/pricing
- free tier: Pure pay-as-you-go: no subscriptions, no plans, no monthly fees and no minimum spend; the balance never expires, and no free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: funds are added through the OfoxAI console; no free tier is stated
- interface: rest
- limits:
  - volume-quota (binding): prepaid pay-as-you-go balance, no minimum spend [1]
- endpoint: https://api.ofox.ai/v1
- composes with: the prepaid balance is the scarce link
- reliability: no standing free tier is published
- evidence:
  - [1] 2026-11-18: pricing is pure pay-as-you-go with no subscription and no free allowance | capture: sha256:8825a4f7b9935e1554b97f35f80b50fe0dcb84941030c4a0359f1ee9430c9084 | quote: No subscriptions, no plans, no hidden fees. Top up and start using immediately. Balance never expires.
- sources:
  - [1] https://ofox.ai/docs/develop/observability/pricing
