# ZenMux

> zenmux.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenmux/ | JSON https://fshy.ajam.dev/api/v1/entity/zenmux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZenMux

- `inference/zenmux` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://zenmux.ai/models
- free tier: Several models are marked limited-time free in the catalog (for example MiMo-V2-Flash and KAT-Coder-Pro V1), and some are free in Studio Chat with rate limits and possible unavailability; no standing free API allowance is published. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a single API key is created for all providers; no card stated for free models
- interface: rest
- limits:
  - request-rate (binding): limited-time free models; Studio Chat free use is rate limited and may be unavailable [1]
- endpoint: https://zenmux.ai/api/v1
- composes with: the limited-time status and the Studio Chat rate limits bind first
- reliability: free models are limited-time and may be temporarily unavailable
- evidence:
  - [1] 2026-11-18: ZenMux catalog marks some models as limited-time free | capture: sha256:ee72eb3aeb770c19e89e176833b43b5efbb780d3fd7eb8d3d1f44f9af2833c3a | quote: Limited time free.
- sources:
  - [1] https://zenmux.ai/models
