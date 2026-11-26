# Arcee

> arcee.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arcee/ | JSON https://fshy.ajam.dev/api/v1/entity/arcee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arcee

- `inference/arcee` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.arcee.ai
- free tier: No free text allowance stated; pricing lists paid per-1M-token rates (e.g. glm-5.3-flash USD 0.15 input / USD 0.50 output) and signup asks for a wallet top-up if needed. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: register on the Arcee Platform, create an API key, top up the wallet if needed
- interface: rest
- limits:
  - volume-quota (binding): per-token billing; no free tier stated [2]
- endpoint: https://api.arcee.ai/api/v1
- tooling: OpenAI-compatible client against api.arcee.ai/api/v1/chat/completions
- composes with: no free tier published; models are billed per token after an API key is created
- reliability: the wallet can be topped up but no free credit grant is documented
- notes: -
- evidence:
  - [1] 2026-11-18: the platform requires an account, API key and possible wallet top-up | capture: sha256:b85296e95c77f1607b205685f815ca22c4be0873a44869a02928264374ec2667 | quote: Access [Arcee Platform](https://platform.arcee.ai/), Register or Login.
  - [2] 2026-11-18: models are listed at paid per-1M-token rates | capture: sha256:198eda4e4e107b35ae7a1f6f8d3f2dbdf015de0e36e0f64a0ea2f468d9e2372d | quote: All prices are in USD.
- sources:
  - [1] https://docs.arcee.ai
  - [2] https://docs.arcee.ai/get-started/pricing
