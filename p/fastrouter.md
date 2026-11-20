# FastRouter

> fastrouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/fastrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FastRouter

- `inference/fastrouter` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://fastrouter.ai/pricing
- free tier: A free Starter plan ($0/month) with 200+ models, $0 model markup and 1M BYOK requests/month; the model catalog also lists free ':free' models at $0/1M tokens. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign-up is free; no card is stated for the Starter tier
- interface: rest
- limits:
  - volume-quota (binding): free Starter: 1 BYOK key at 1M requests/month, 200K logs/month with 7-day retention; free models at $0/1M [1]
- endpoint: https://go.fastrouter.ai/api/v1
- tooling: an OpenAI-compatible key; the free Starter plan passes model costs through with $0 markup
- composes with: the free Starter tier plus the free ':free' model pool are the scarce links
- reliability: free ':free' models share an upstream pool and can return 429 under load
- evidence:
  - [1] 2026-11-18: the Starter plan is free forever with the core gateway | capture: sha256:2302f0cd2477afd9d01c454989c00da1f1b3a9aeccc51312deddf0a1bb1e3b6c | quote: Starter is free forever and still includes the core gateway: 200+ models
- sources:
  - [1] https://fastrouter.ai/pricing
