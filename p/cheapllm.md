# cheapllm.shop

> cheapllm.shop | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cheapllm/ | JSON https://fshy.ajam.dev/api/v1/entity/cheapllm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cheapllm.shop

- `inference/cheapllm` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://cheapllm.shop/docs
- free tier: During beta every account is free with no rate limit; after beta a permanent free tier with no card of at least 5,000 input tokens and 1,000 output tokens per hour (5,000 and 1,000 today), counted per account over a rolling hour across all keys. | unit: tokens | metered on: wall-clock | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account and a dashboard key; the permanent free tier needs no card
- interface: rest
- limits:
  - volume-quota (binding): at least 5,000 input and 1,000 output tokens per hour per account, rolling hour, all keys together [1]
  - request-rate: one request at a time per account; 429 while a request is running [1]
- endpoint: https://cheapllm.shop/v1
- tooling: an OpenAI-compatible base URL with an sk-cheap- key; Anthropic Messages and OpenAI Responses formats also work
- composes with: the rolling-hour token allowance and the one-request-at-a-time rule bind before the per-token price
- reliability: a 429 is returned while another request from the account is running; traffic spikes queue for up to 30 seconds before a 503
- notes: a real standing card-free free tier exists, bounded by a rolling-hour token allowance and a one-request-at-a-time rule
- evidence:
  - [1] 2026-11-18: a permanent card-free free tier of at least 5,000 input and 1,000 output tokens per hour, counted per account over a rolling hour | capture: sha256:0e620efc3b414cf06e1c874578d2f34fe75342457b5eedabd7af008e8ee4f382 | quote: every account keeps a permanent free tier, with no card: at least 5,000 input tokens and 1,000 output tokens per hour
- sources:
  - [1] https://cheapllm.shop/docs
