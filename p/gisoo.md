# Gisoo

> gisoo.pro | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gisoo/ | JSON https://fshy.ajam.dev/api/v1/entity/gisoo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gisoo

- `inference/gisoo` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://gisoo.pro/docs/models
- free tier: No free model exists: every model is priced by metered usage. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a funded account is needed before any model call
- interface: rest
- limits:
  - volume-quota (binding): every model is priced by consumption; no free model [1]
- endpoint: https://gisoo.pro/api/v1
- tooling: an OpenAI-compatible key against the Persian-language gateway
- composes with: all models are metered, so no standing free text allowance exists
- reliability: a discontinued model returns 404 model_discontinued rather than a silent failure
- evidence:
  - [1] 2026-11-18: no free model exists and every model is priced by usage | capture: sha256:afc23c1dccd1086bde5ee93d413c3afe2052d77058e49fcf80d5112b19e1b214 | quote: مدل رایگان در گیسو نیست؛
- sources:
  - [1] https://gisoo.pro/docs/models
