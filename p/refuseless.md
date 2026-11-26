# Refuseless

> refuseless.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/refuseless/ | JSON https://fshy.ajam.dev/api/v1/entity/refuseless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Refuseless

- `inference/refuseless` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway (abliterated models)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.refuseless.com/models
- free tier: Free variant of DeepSeek V4.1 Flash Abliterated, with a smaller context window. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key from an account is used for the catalog; the exact signup gate for the free variant is not stated in the captured page
- interface: rest
- limits:
  - per-object-cap: 524,288-token context window on the free variant versus 1,048,576 on the paid variant [1]
  - request-rate (binding): the binding constraint named on the first-party page [1]
- endpoint: https://api.refuseless.com/v1
- composes with: The free model id is deepseek-v4.1-flash-abliterated-free. The captured page proves the free variant and its smaller context; whether an account plus card is needed to use it is unverified.
- reliability: 402 insufficient_credits on a balance that cannot cover a request
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Refuseless lists a free model variant with a 524,288-token context window | capture: sha256:e244cafca17e0afeb48c16ea846de674d59b7266e29ed033e644e5a91d9b405d | quote: Free variant of DeepSeek V4.1 Flash Abliterated, with a smaller context window.
- sources:
  - [1] https://docs.refuseless.com/models
