# DG AI API

> dg-ai.scriptsnsenses.workers.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dg-ai-scriptsnsenses-workers-dev/ | JSON https://fshy.ajam.dev/api/v1/entity/dg-ai-scriptsnsenses-workers-dev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DG AI API (dg-ai.scriptsnsenses.workers.dev)

- `inference/dg-ai-api` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, keyless free public beta
- identity a placeholder: card and phone unknown | verified 2026-11-10T01:21:20.503Z (live) | stale on 2026-12-11
- url https://dg-ai.scriptsnsenses.workers.dev/v1
- free tier: Free public beta with no key required: 18 models live, auth is optional and a placeholder of dashes is accepted; the anonymous tier is 8 requests per 10 s | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: GET /v1/models lists 18 ids; the page labels three backends (Cloudflare Workers AI, freeAI gateways, SurfSense) plus NVIDIA NIM, and which model actually serves an id with another vendor's name is not observed
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: none for the anonymous tier: auth is optional, and a placeholder or no header is accepted as anonymous. A verified tier raises the quota; what verifying needs was not read: unverified
- interface: rest
- limits:
  - request-rate (binding): anonymous tier 8 requests per 10 s; a verified tier is 16 per 10 s (stated as "anon 8/10s · verified 16/10s") [1]
- binding note: the anonymous tier ceiling of 8 per 10 s binds; what verification requires was not read
- endpoint: https://dg-ai.scriptsnsenses.workers.dev/v1/chat
- tooling: POST /v1/chat with {"model": id, "messages": [...]}; the chat route is /v1/chat, not /v1/chat/completions, which answers "Route not found" to a GET. A placeholder Authorization or X-API-Key of dashes, or no header, is accepted
- composes with: pairs with prototypes that need a free OpenAI-shaped call; image and voice routes exist beside chat
- reliability: the page claims 98.7% uptime over 90 days; no x-ratelimit header is returned on GET /v1/models, only CORS headers
- notes: ids such as claude-sonnet-3.5 and gemini-2.5-pro are labelled by their upstream vendor in the listing and are served through the freeAI gateway backend named on the page; the served model is unverified
- evidence note: the model list was read by a keyless GET; no completion was sent because probe issues GET and HEAD only, so the echoed model and the answer are unverified
- probe:
  - records[0].probe_id: dgai-v1-models-get
  - records[0].method: GET
  - records[0].url: https://dg-ai.scriptsnsenses.workers.dev/v1/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].model_count: 18
  - records[0].probed_at: 2026-10-28T04:47:35.797Z
  - records[0].chat_completion_tested: no
  - records[1].probe_id: dgai-chat-completions-get
  - records[1].method: GET
  - records[1].url: https://dg-ai.scriptsnsenses.workers.dev/v1/chat/completions
  - records[1].http: 404
  - records[1].error_message: Route not found: GET /v1/chat/completions
  - records[1].probed_at: 2026-10-28T04:48:01.537Z
- evidence:
  - [1] 2026-10-28: the page states a free public beta with no key required | capture: sha256:4b9965c9b012a7b854dd593f4c343b901adeed442592f84471ddde0b71e2623e | quote: Free public beta — no key required · placeholders like \---------- are accepted
  - [1] 2026-10-28: auth is optional and no header at all is accepted as anonymous | capture: sha256:4b9965c9b012a7b854dd593f4c343b901adeed442592f84471ddde0b71e2623e | quote: Auth is optional. Send `Authorization: Bearer ----------` (any number of dashes), `X-API-Key: ----------`, or nothing — all accepted as anonymous.
  - [1] 2026-10-28: the published rate limit is 8 per 10 s anonymous and 16 per 10 s verified | capture: sha256:4b9965c9b012a7b854dd593f4c343b901adeed442592f84471ddde0b71e2623e | quote: `anon 8/10s · verified 16/10s`
  - [1] 2026-10-28: the page counts 18 models live | capture: sha256:4b9965c9b012a7b854dd593f4c343b901adeed442592f84471ddde0b71e2623e | quote: 18models live
  - [2] 2026-10-28: a keyless GET /v1/models answered 200 with the model list | capture: sha256:e728e2b02f3e1d30a1f89e6625f99362cb3ed6a56f0e9b84a5989dfd6c2ae5ac | quote: {"object":"list","data":[{"id":"gpt-oss","object":"model","owned_by":"OpenAI"}
  - probe:https://dg-ai.scriptsnsenses.workers.dev/v1/chat 2026-11-10: a keyless POST on 2026-11-10 answered 200 with ok true, model gpt-oss and an empty reply | capture: sha256:5444a50d2649097e7ee78b5545442679c2e5815f52754800eb808e68f5c0cac6 | quote: "status": 200
- sources:
  - [1] https://dg-ai.scriptsnsenses.workers.dev/
  - [2] https://dg-ai.scriptsnsenses.workers.dev/v1/models
