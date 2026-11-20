# abliteration.ai

> abliteration.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abliteration/ | JSON https://fshy.ajam.dev/api/v1/entity/abliteration.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## abliteration.ai

- `inference/abliteration-ai` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://abliteration.ai/pricing
- free tier: No standing free tier is stated. Monthly plans start at USD 20 a month with USD 20 in usage credit, and one-time credit costs USD 100. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account at signup for a paid plan; the page states no free text tier
- interface: rest
- limits:
  - volume-quota (binding): plans from USD 20 a month with USD 20 usage credit; no free text allowance stated [1]
- endpoint: https://api.abliteration.ai/v1
- tooling: OpenAI- and Anthropic-compatible APIs and a signup console
- composes with: the paid credit plans are the scarce link; no free text allowance is published
- reliability: the free allowance is absent from the pricing page, so a text client pays from the first call
- notes: no free text allowance appears on the pricing page; the doc URL https://docs.abliteration.ai/models resolved to the pricing page
- evidence:
  - [1] 2026-11-18: the pricing page offers monthly credit plans and pay-as-you-go credit purchases, with no stated standing free allowance | capture: sha256:92b1dd2e8bddbd9895bfdd7255710b9047bfd1d5c91d2a4796cf8ce2db4c46b9 | quote: Choose monthly credits and usage discounts, or pay as you go.
- sources:
  - [1] https://abliteration.ai/pricing
