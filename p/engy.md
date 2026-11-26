# engy

> engy.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/engy/ | JSON https://fshy.ajam.dev/api/v1/entity/engy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## engy

- `inference/engy` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://engy.ai/pricing
- free tier: No free allowance is stated. The catalog lists per-token prices, for example DeepSeek V4.1 Flash 1017 at USD 0.03 per million input tokens and USD 0.12 per million output tokens, with discounts of up to 91% against published provider prices. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key are needed; no free inference allowance is stated
- interface: rest
- limits:
  - volume-quota (binding): per-token prices with discounts up to 91% against published provider prices [1]
- endpoint: https://api.engy.ai/v1
- tooling: an OpenAI-compatible endpoint with list prices reported at GET /v1/models
- composes with: the discounted per-token charge is the scarce link; no free tier is published
- reliability: the gateway does not store prompts or outputs; a ZDR flag can be set on a request for end-to-end zero data retention
- notes: no standing free inference allowance is published; all catalog models carry per-token prices
- evidence:
  - [1] 2026-11-18: the pricing page lists per-token prices for the catalog and the API reports the same numbers; no free allowance is stated | capture: sha256:ced2ca28fa5b2c668d5a6b1f977cbf6a55fab8073fbd56f4a0df9780b9385e76 | quote: These are the catalog's list prices. The API reports the same numbers at `https://api.engy.ai/v1/models`.
- sources:
  - [1] https://engy.ai/pricing
