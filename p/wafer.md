# Wafer

> wafer.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wafer/ | JSON https://fshy.ajam.dev/api/v1/entity/wafer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wafer

- `inference/wafer-ai` | paid-only | evidence documented | binding volume-quota | category serverless inference, pay-per-token
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://www.wafer.ai/
- free tier: no free tier stated: pay per token for open models through an OpenAI-compatible API; a keyless GET /v1/models lists the catalog and list prices, but no free-token allowance is published | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is used for inference and account rates; the public model catalog needs no key; signup fields not stated on the pages read
- interface: rest
- limits:
  - volume-quota (binding): per-token pricing in US cents per million tokens; no free allowance [2]
- binding note: no free tokens stated, so payment binds first
- endpoint: https://pass.wafer.ai/v1
- tooling: an OpenAI-compatible key at pass.wafer.ai/v1; the model list is public and the key is optional for catalog reads
- composes with: pairs with an OpenAI-compatible agent on a pay-per-token balance
- reliability: no reliability event recorded
- notes: models.dev id is wafer.ai; A public keyless catalog is a discovery route, not a free inference allowance; inference is pay per token.
- evidence:
  - [1] 2026-11-18: inference is pay per token through an OpenAI-compatible API | capture: sha256:1964465ca5556f5d2048d9c922043befbf6951bedc059c23194e64867e8d7632 | quote: Pay per token for open models through an OpenAI-compatible API.
  - [2] 2026-11-18: the model list is public and the key is optional for catalog reads | capture: sha256:1695893f4842e182c6a19af16c26eb2ce6bbca6dafb3c68dc7bf5f9c43ecea78 | quote: The model list is public, so the API key is optional.
- sources:
  - [1] https://www.wafer.ai/
  - [2] https://docs.wafer.ai/serverless/models
