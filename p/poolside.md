# Poolside

> poolside.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/poolside/ | JSON https://fshy.ajam.dev/api/v1/entity/poolside.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Poolside

- `inference/poolside` | dead | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.poolside.ai
- free tier: No self-serve free API offer: 'Poolside Platform inference will shut down on 31 October 2026. You can download our models from Hugging Face and host them yourself.' | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no self-serve free tier
- interface: rest
- limits:
  - volume-quota (binding): inference service shut down 2026-10-31 [1]
- endpoint: https://inference.poolside.ai/v1
- tooling: self-hosted models from Hugging Face; no hosted API after shutdown
- composes with: the hosted inference route is gone; only self-hosted weights remain
- reliability: inference endpoint retired on 31 October 2026
- notes: The platform page announces a shutdown and points to self-hosted weights, so no hosted free or paid API remains.
- evidence:
  - [1] 2026-11-18: the hosted inference service is shut down | capture: sha256:2a870a953f561f977e416b916b0a3ea5feb5225f9127ac443d7159f49d641ab4 | quote: Poolside Platform inference will shut down on 31 October 2026.
- sources:
  - [1] https://platform.poolside.ai
