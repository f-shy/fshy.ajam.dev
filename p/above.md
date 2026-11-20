# above.dev

> above.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/above/ | JSON https://fshy.ajam.dev/api/v1/entity/above.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## above.dev

- `inference/above` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://above.dev/docs
- free tier: Free-tier routes exist, with the free-tier models glm-5.3-flash-modal and deepseek-v4.1-flash-modal capped at 16,384 output tokens because they share a fixed concurrency pool; paid models run from USD 0.165 to USD 0.33 per 1M input tokens. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is required and the page states no card for the free-tier routes
- interface: rest
- limits:
  - per-ip-shaping (binding): one 500k+ token request per 2 minutes on the free tier [1]
  - per-object-cap: free-tier routes are capped at 16,384 max_tokens [1]
- endpoint: https://api.above.dev/v1
- tooling: an OpenAI-compatible base URL with a model list at GET /v1/models
- composes with: the two-minute window on large-context requests is the scarce link, and the cap is silent because max_tokens is reduced rather than rejected
- reliability: an over-cap max_tokens is reduced silently instead of refused, so a run can return shorter output than it asked for
- evidence:
  - [1] 2026-11-18: free-tier routes are capped at 16,384 max_tokens on a shared concurrency pool and large-context requests are limited to one per two minutes | capture: sha256:d012ddafaa252108d45c22d963ef911cbd31eaf6153318618c1f03601338dea9 | quote: Every model in the catalog accepts up to 131,072 output tokens. The two free-tier routes, `glm-5.3-flash-modal` and `deepseek-v4.1-flash-modal`, are capped at 16,384 instead, because they share a fixed concurrency pool. A `max_tokens` above the cap is reduced to it rather than rejected, and each model reports its own figure as `max_completion_tokens` in `GET /v1/models`.
- sources:
  - [1] https://above.dev/docs
