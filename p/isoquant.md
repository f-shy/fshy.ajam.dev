# Isoquant

> isoquant.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/isoquant/ | JSON https://fshy.ajam.dev/api/v1/entity/isoquant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Isoquant

- `inference/isoquant` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://isoquant.ai/docs
- free tier: No free inference allowance is stated. Create an API key in the console and add credit in Billing; public model discovery via GET /v1/models needs no key. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an API key in the console and add credit in Billing before calling a model
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit added in Billing; a 402 insufficient credit response on an empty balance [1]
- endpoint: https://api.isoquant.ai/v1
- tooling: an OpenAI-compatible base URL with an ISOQUANT_API_KEY; OpenAI Chat Completions, Messages and Responses are supported
- composes with: the prepaid credit and API key bind; model discovery is public but calls are not free
- reliability: usage and billing metadata are recorded even when zero data retention is required; a 429 capacity limit requires honoring Retry-After
- notes: no standing free inference allowance is published; public model discovery is the only key-free route
- evidence:
  - [1] 2026-11-18: an API key is created in the console and credit is added in Billing; public model discovery needs no key, but calls need credit | capture: sha256:2a88e06000cbe57d7297e7d0e794b9c202fee217f7d0d6769b2efe90aaa1d33e | quote: Add credit in [Billing](https://console.isoquant.ai/billing) when you need more.
- sources:
  - [1] https://isoquant.ai/docs
