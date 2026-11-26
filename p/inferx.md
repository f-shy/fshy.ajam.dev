# InferX

> inferx.net | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inferx/ | JSON https://fshy.ajam.dev/api/v1/entity/inferx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InferX

- `inference/inferx` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://inferx.net
- free tier: No free endpoint remains at capture time. The DeepSeek V4.1 Flash 1017 endpoint was temporarily moved from free to 70% off while GPU capacity is added; hosted endpoints are pay per token. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: log in to get a tenant-scoped endpoint URL and inference API key
- interface: rest
- limits:
  - volume-quota (binding): formerly free endpoint moved to 70% off; hosted endpoints pay per token [1]
- endpoint: https://model.inferx.net/v1
- tooling: OpenAI-compatible hosted endpoints and an API key from the tenant login; a self-hosted InferX Platform is also offered
- composes with: the closure of the formerly free endpoint is the scarce link; hosted endpoints are now paid
- reliability: the formerly free endpoint was moved to 70% off because of high demand and limited GPU capacity
- notes: the only free endpoint documented was moved to 70% off at capture time, so no standing free inference allowance remains; endpoint disagreement: models.dev lists the api as https://model.inferx.net/endpoints/v1, while the vendor's live SDK guide at inferx.net documents base_url https://model.inferx.net/v1 (https://model.inferx.net/v1 in the capture). The vendor-documented /v1 endpoint is kept here because a first-party page shows it.
- evidence:
  - [1] 2026-11-18: the DeepSeek V4.1 Flash 1017 endpoint was moved from free to 70% off, so no free endpoint remains at capture time | capture: sha256:8f61e45a31ab06b478eb63bf285bd2640471fe977a83f83631cdc7dc0a15bc61 | quote: We temporarily moved this endpoint from free to 70% off while we add GPU capacity and keep service reliable during high demand.
- sources:
  - [1] https://inferx.net
