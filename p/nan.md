# NaN

> nan.builders | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nan/ | JSON https://fshy.ajam.dev/api/v1/entity/nan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NaN

- `inference/nan` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway (community cluster)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://nan.builders/docs/choose-a-model
- free tier: no counter means the model does not draw credits, not that it is infinite: the requests-per-minute limits apply to all of them just the same. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a membership or credit pack is needed for credit models; no-counter models are available on the community plan without credits
- interface: rest
- limits:
  - request-rate (binding): requests-per-minute limits apply to no-counter models [1]
- endpoint: https://api.nan.builders/v1
- composes with: The standing free path is the no-counter model list (gemma4, qwen3.6, embeddings, rerank, kokoro, whisper), not an expiring credit. Image models get 100 requests per month.
- reliability: a 402 insufficient_balance answer when credit models have no credits; a 429 on the glm5.3 window at capacity
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: NaN offers no-counter models such as gemma4 that do not draw credits, still subject to request-rate limits | capture: sha256:48fef4498960f89de0316fdefec97e6543e154b0e5738ea6cbd90b78eca69907 | quote: `no counter` means the model does not draw credits, not that it is infinite: the requests-per-minute limits apply to all of them just the same.
- sources:
  - [1] https://nan.builders/docs/choose-a-model
