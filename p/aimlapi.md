# AI/ML API

> aimlapi.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aimlapi/ | JSON https://fshy.ajam.dev/api/v1/entity/aimlapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AI/ML API

- `inference/ai-ml-api` | paid-only | evidence documented | binding write-gated | category inference gateway, paused free tier
- identity a placeholder: card and phone unknown | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://docs.aimlapi.com/faq/free-tier
- free tier: none: the vendor's free-tier FAQ reads 'The Free Tier is currently paused' | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: the pricing page is a per-model price list with no free allowance
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: unverified: the sign-up requirements for the paid tier were not captured; with the free tier paused the first request needs a funded balance, which is assumed to need a payment method
- interface: rest
- limits:
  - write-gated (binding): no free tier is issued while it is paused [1]
- binding note: no free allowance is issued; usage needs a funded account
- endpoint: https://api.aimlapi.com/v1/chat/completions
- tooling: any OpenAI-compatible client against the AI/ML API base URL
- composes with: paid aggregator of many models; useful only once a balance exists
- reliability: the free tier is paused and the page states no resumption date
- notes: check the FAQ page again for a resumption date.
- evidence note: the pause is quoted from the vendor's FAQ; sign-up and payment requirements were not captured.
- evidence:
  - [1] 2026-10-28: the vendor states the Free Tier is paused | capture: sha256:fcf780b30c8095390cf590ac2f0c5780d688a828d1ffc6bfffe262367c941107 | quote: The Free Tier is currently paused.
- sources:
  - [1] https://docs.aimlapi.com/faq/free-tier
