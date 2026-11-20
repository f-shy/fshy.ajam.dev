# Reflection

> reflection.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reflection/ | JSON https://fshy.ajam.dev/api/v1/entity/reflection.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Reflection

- `inference/reflection` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://developers.reflection.ai/models
- free tier: No free text allowance documented; the Beam model is reached through the Reflection API with an API key, and available models can differ between organizations and plans. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key from the platform; no card or phone gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): per-token pricing not published on this models page; no free tier stated [1]
- endpoint: https://api.reflection.ai/openai/v1
- tooling: OpenAI SDK or Mirror CLI against the OpenAI-compatible endpoint
- composes with: no free tier published; plan and organization decide model availability
- reliability: a plan's per-request output limit applies and reasoning is mandatory on Beam
- notes: -
- evidence:
  - [1] 2026-11-18: models available depend on organization and plan and require a key | capture: sha256:a48d8eb953b185edc61065d5d5241a7aebf927adf3da149fc1dbc3d1ab56a1e9 | quote: The [List models](https://developers.reflection.ai/api-reference/models/list-models.md) endpoint returns the models you can use, which can differ between organizations and plans
- sources:
  - [1] https://developers.reflection.ai/models
