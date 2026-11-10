# Requesty

> requesty.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/requesty/ | JSON https://fshy.ajam.dev/api/v1/entity/requesty.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Requesty

- `inference/requesty` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, free models
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://docs.requesty.ai/features/free-models
- free tier: Free plan: access to all free models at no token charge, 200 requests per day and 20 requests per minute for a new organization, counted across all free models combined; free models include nvidia/nemotron-3-ultra-550b-a55b, nvidia/nemotron-3-super-120b-a12b, google/gemma-4-31b-it and poolside/laguna-m.1 | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the docs mark the models 'free for now' and announce any price change in the changelog ahead of time; paying organizations get 1,000 requests per day and 60 per minute
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no credit card required for the free models, quoted from the pricing and FAQ pages; the sign-up form at app.requesty.ai was not captured, so any further check on it is not established
- interface: rest
- limits:
  - request-rate (binding): new organizations: 200 requests per day and 20 requests per minute across all free models combined; paying organizations: 1,000 per day and 60 per minute; daily limit resets daily [1]
- binding note: the 200 requests per day budget is shared across all free models and binds long before any per-minute figure
- endpoint: https://router.requesty.ai/v1/chat/completions
- tooling: any OpenAI-compatible client at https://router.requesty.ai/v1 with the model id written provider/model; an Anthropic-style /anthropic/v1/messages path also exists
- composes with: the free models route through the same gateway as the 600+ paid ones, so a fallback policy can move to a paid model when the daily limit is hit
- reliability: free models are labelled free for now and the limit is shared across all of them, so one busy model exhausts the budget for the others
- notes: per-model limits do not exist: the figures are per organization across all free models.
- evidence note: limits and the no-card statement are quoted from the vendor's docs and pricing pages; no call was made.
- evidence:
  - [2] 2026-10-28: the Free plan needs no credit card | capture: sha256:ce7ae919f4743231267d29cd539cf61e475b694365468481561011d3767869c1 | quote: No credit card required
  - [2] 2026-10-28: the Free plan allows 200 requests per day | capture: sha256:ce7ae919f4743231267d29cd539cf61e475b694365468481561011d3767869c1 | quote: 200 requests per day
  - [1] 2026-10-28: new organizations get 200 requests per day and 20 per minute on free models | capture: sha256:19cac103610f8be92010bb3c4ca1e53e53d78bd8ee5909c63454f5ddbf24cef0 | quote: | New organizations | 200 | 20 |
  - [1] 2026-10-28: paying organizations get 1,000 requests per day and 60 per minute on free models | capture: sha256:19cac103610f8be92010bb3c4ca1e53e53d78bd8ee5909c63454f5ddbf24cef0 | quote: | Paying organizations | 1,000 | 60 |
  - [1] 2026-10-28: the limit is shared across every free model rather than per model | capture: sha256:19cac103610f8be92010bb3c4ca1e53e53d78bd8ee5909c63454f5ddbf24cef0 | quote: The limits apply across all free models combined.
  - [1] 2026-10-28: the free status is explicitly provisional | capture: sha256:19cac103610f8be92010bb3c4ca1e53e53d78bd8ee5909c63454f5ddbf24cef0 | quote: These models are free for now.
  - probe:https://router.requesty.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:5536a81e3c38af46484f5973ae9a8e33d76a18b9372b75bb3491b12b93163603 | quote: "status": 401
- sources:
  - [1] https://docs.requesty.ai/features/free-models.md
  - [2] https://requesty.ai/pricing
