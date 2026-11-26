# Jalapeno Cloud

> jalapeno-cloud.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jalapeno-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/jalapeno-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jalapeno Cloud

- `inference/jalapeno` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://www.jalapeno-cloud.ai/docs/
- free tier: No free inference allowance is stated. The quick start requires registration and login, then selecting a model and creating an API key; the model marketplace shows per-token pricing. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: register and log in with credentials or a verification code, then create an API key
- interface: rest
- limits:
  - volume-quota (binding): per-token prices shown per model in the marketplace; no free allowance stated [1]
- endpoint: https://api.jalapeno-cloud.ai/v1
- tooling: OpenAI Chat Completions, OpenAI Responses and Anthropic Messages formats with an API key
- composes with: the account and per-token marketplace pricing are the scarce links; no free tier is published
- reliability: usage statistics are available in the Usage page; no free tier, quota or rate limit is published on the quick start page
- notes: no standing free inference allowance is published; registration and per-token paid models are the offer
- evidence:
  - [1] 2026-11-18: the quick start requires registration and login before creating an API key; no free inference allowance is stated | capture: sha256:c4f16807ecb5771a25d360757b89a95bd2a7540bfab802c5c55e667183c08b73 | quote: Register and log in to your Jalapeno Cloud account
- sources:
  - [1] https://www.jalapeno-cloud.ai/docs/
