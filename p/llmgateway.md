# LLM Gateway

> llmgateway.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/llmgateway/ | JSON https://fshy.ajam.dev/api/v1/entity/llmgateway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LLM Gateway

- `inference/llm-gateway` | paid-only | evidence documented | binding request-rate | category inference gateway, free-model mechanism with an empty catalogue
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://llmgateway.io/pricing
- free tier: free models (zero input and output price) carry their own limits: 5 requests per 10 minutes per free model for an organization with zero credits, 20 requests per minute per free model once any credits are purchased; the live model list shows 0 Free Models on the day read | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the pricing page still says free models are available on the free tier without buying credits; managed cloud is prepaid credits with a $10 minimum top-up and a 5% platform fee
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free models need a verified email address, and unverified accounts receive a 403; no card is named for the free models
- interface: rest
- limits:
  - request-rate (binding): per organization per free model: 5 requests per 10 minutes with zero credits; 20 requests per minute once any credit has been purchased; credits are not deducted for free models [1]
- binding note: 5 requests per 10 minutes per model is the ceiling if a free model is listed
- endpoint: https://api.llmgateway.io/v1/chat/completions
- tooling: any OpenAI-compatible client at https://api.llmgateway.io/v1
- composes with: paid gateway with a documented free-model lane; only worth a key if free models are listed again
- reliability: the free-model lane is documented but the model directory lists none, so a key may have nothing free to call
- notes: verdict is paid-only because the directory lists no free model; it moves up if free models reappear.
- evidence note: limits and the verified-email rule are quoted from the vendor's rate-limit page and the empty free list from the model directory; no call was made.
- evidence:
  - [1] 2026-10-28: zero-credit organizations get 5 requests per 10 minutes per free model | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: - 5 requests per 10 minutes per free model
  - [1] 2026-10-28: organizations that purchased credits get 20 requests per minute per free model | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: - 20 requests per minute per free model
  - [1] 2026-10-28: free models require a verified email address | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: Using free models also requires a verified email address — unverified accounts receive a `403`.
  - [2] 2026-10-28: the pricing page states free models exist on the free tier | capture: sha256:bd8807b703e0aae0c309dff2d568b80a7702abd39047eb189c82abb6c353a202 | quote: - Free models are available on the free tier without buying credits.
  - [3] 2026-10-28: the model directory counts 0 free models | capture: sha256:7dcc87a8eec63431dcb883aaaf071f41bc7af64b3c65166704d01015e97a0b8d | quote: Tool-enabled 0 Free Models
- sources:
  - [1] https://docs.llmgateway.io/resources/rate-limits
  - [2] https://llmgateway.io/pricing
  - [3] https://llmgateway.io/models
