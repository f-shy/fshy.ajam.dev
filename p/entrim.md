# Entrim

> entrim.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/entrim/ | JSON https://fshy.ajam.dev/api/v1/entity/entrim.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Entrim

- `inference/entrim` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://docs.entrim.ai/model-api/
- free tier: No free allowance is stated. Model API usage is paid from prepaid credits checked and added under Billing in the Entrim dashboard. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an API key in the Entrim Dashboard and add prepaid credits under Billing
- interface: rest
- limits:
  - volume-quota (binding): prepaid credits topped up in the dashboard [1]
- endpoint: https://api.entrim.ai/v1
- tooling: an OpenAI-compatible base URL and a dashboard API key
- composes with: the prepaid credit balance is the scarce link; no free text tier is published
- reliability: anyone with the API key can spend the credits, so keys must be kept out of source control and client code
- notes: no standing free inference allowance is published; usage draws from prepaid credits
- evidence:
  - [1] 2026-11-18: the model API is paid from prepaid credits; no free allowance is stated | capture: sha256:f603495402213f2e15d955f8425131eef69400896a669c1cb419c54a1ac7e1f1 | quote: Model API usage is paid from prepaid credits.
- sources:
  - [1] https://docs.entrim.ai/model-api/
