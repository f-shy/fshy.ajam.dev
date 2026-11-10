# Ollama Cloud

> ollama.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ollama-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ollama-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ollama Cloud

- `inference/ollama-cloud` | paid-only | evidence documented | binding write-gated | category inference endpoint, pay-as-you-go cloud models
- identity a placeholder: card and phone unknown | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://ollama.com/pricing
- free tier: none listed: the Pay as you go plan is $0 a month with every cloud model billed per token; included usage credits belong to the Pro, Max and Team plans | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: a third-party list still shows 'starter usage credits; starter models only' for Ollama Cloud; the vendor pricing page lists no such allowance
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: unverified: the sign-up flow was not captured; usage credits are purchased, so a payment method is expected for any cloud request
- interface: rest
- limits:
  - write-gated (binding): no included usage on the Pay as you go plan: each request is paid with usage credits that are purchased [1]
  - request-rate: 3 concurrent requests on Pay as you go and Pro, 10 on Max and Team; requests beyond the limit are queued and rejected when the queue is full [1]
- binding note: usage requires purchased credits
- endpoint: https://ollama.com/api/chat
- tooling: native API at https://ollama.com/api/chat with a bearer key, or OpenAI-compatible and Anthropic-compatible clients
- composes with: paid cloud models; no free allowance is listed
- reliability: no included usage on the pay-as-you-go plan; every cloud request draws on purchased credits
- notes: re-check the pricing page for a free allowance before relying on the third-party report.
- evidence note: the absence of a free allowance is read from the vendor pricing page, which lists no free tier; a third-party list disagrees.
- evidence:
  - [1] 2026-10-28: Pay as you go bills every cloud model per token | capture: sha256:e0666db3754a1814a35650dbf79822beae8cb1afd286386804ee3dbde61f7369 | quote: Pay per token for every cloud model.
  - [1] 2026-10-28: only Pro, Max and Team include monthly credits; Pay as you go pays per request | capture: sha256:e0666db3754a1814a35650dbf79822beae8cb1afd286386804ee3dbde61f7369 | quote: Pro, Max, and Team plans include a set dollar amount of usage credits each month. Pay as you go accounts pay for each request with usage credits.
  - [1] 2026-10-28: Pay as you go includes 3 concurrent requests | capture: sha256:e0666db3754a1814a35650dbf79822beae8cb1afd286386804ee3dbde61f7369 | quote: Pay as you go and Pro include 3 concurrent requests, and Max and Team 10.
  - [2] 2026-10-28: a third-party list reports starter credits that the vendor pricing page does not show | capture: sha256:b145b110ad322fbf10dea6e89cabc51fc04d3bbe80221c36fa1fe5d27045341a | quote: Starter usage credits; starter models only (add credits to unlock all models)
- sources:
  - [1] https://ollama.com/pricing
  - [2] https://free-llm.com/free-llm-api-keys
