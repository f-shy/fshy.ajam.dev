# CedarLLM

> cedarllm.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cedarllm/ | JSON https://fshy.ajam.dev/api/v1/entity/cedarllm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CedarLLM

- `inference/cedarllm` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://cedarllm.com/docs
- free tier: No free allowance is stated. Credit is prepaid in US dollars with a card minimum of USD 5; qwen3.8-27b is USD 0.03 per million input tokens. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: create an account and confirm email, then add credit with a card, minimum USD 5
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit with a card minimum of USD 5; USD 0.03 per million input tokens on qwen3.8-27b [1]
  - request-rate: up to 60 successful requests per minute per account [1]
- endpoint: https://api.cedarllm.com/v1
- tooling: an OpenAI-compatible base URL with the official OpenAI SDK or any custom-URL client
- composes with: the card-funded prepaid balance is the scarce link; no free text tier is published
- reliability: account availability is restricted to US residents; at busy times requests queue and there is no uptime guarantee; one coding model handles one request at a time
- notes: no free text allowance; a card-funded balance and US residency are required
- evidence:
  - [1] 2026-11-18: an account and email confirmation are required, then a card top-up of at least USD 5; no free allowance is stated | capture: sha256:a182e258b03678be1138c3360be64701e10ebcd514098504e41edec1ea2a37c0 | quote: add credit with a card (minimum $5)
- sources:
  - [1] https://cedarllm.com/docs
