# AnyAPI

> anyapi.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anyapi/ | JSON https://fshy.ajam.dev/api/v1/entity/anyapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnyAPI

- `inference/anyapi` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://anyapi.ai/pricing
- free tier: Free plan: $0/month, 100,000 AnyTokens per day, unlimited users, all free models, no credit card required, limited API calls, community support. | unit: tokens | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the free plan requires no credit card; an account is created at dash.anyapi.ai
- interface: rest
- limits:
  - volume-quota (binding): 100,000 AnyTokens per day on the free plan, with limited API calls [1]
- endpoint: https://api.anyapi.ai/v1
- tooling: an OpenAI-compatible key (Bearer $ANYAPI_KEY) against the unified endpoint
- composes with: the 100K-tokens-per-day allowance and limited API calls on the free plan are the scarce links
- reliability: free plan has limited API calls and no SLA; paid tiers unlock all models
- evidence:
  - [1] 2026-11-18: the free plan grants 100,000 AnyTokens per day with no credit card | capture: sha256:1dc8ad10d594c17c7c42bc8014a2fcccf9891ec1a9c0de09d910597d132ed916 | quote: ### Free Getting started $0 / mo Perfect for testing and learning filter icon ANY Tokens: 100K / day users icon Users: Unlimited Core features: Checkbox blue icon All [free models](https://anyapi.ai/ai-models) Checkbox blue icon AnyAPI SDK Checkbox blue icon AnyCLI Checkbox blue icon AnyChat Plan Highlights: dot icon No credit card required
- sources:
  - [1] https://anyapi.ai/pricing
