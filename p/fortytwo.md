# Fortytwo

> fortytwo.network | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fortytwo/ | JSON https://fshy.ajam.dev/api/v1/entity/fortytwo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fortytwo

- `inference/fortytwo` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.fortytwo.network/docs/models
- free tier: A model whose ID ends in :free is free: requests cost nothing and work with any balance. The Free tier allows 5 requests per minute, 150 per hour, 500,000 uncached input tokens per hour, 100,000 output tokens per hour, 3,000,000 input tokens per day and 1,000,000 output tokens per day. Every request to a free model is collected for data handling. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a network account; the page states no card for the free models
- interface: rest
- limits:
  - request-rate (binding): Free tier: 5 requests/minute, 150/hour, 500,000 uncached input tokens/hour, 100,000 output tokens/hour, 3,000,000 input tokens/day, 1,000,000 output tokens/day [2]
  - request-rate (binding): an unpublished concurrency cap fails a request at once with 429 concurrency_limit_exceeded [2]
- binding note: the Free tier is rate-limited on all four windows; the 5 requests/minute and 1,000,000 output tokens/day bind before any other constraint
- endpoint: https://api.fortytwo.network/v1
- composes with: the free model list is the scarce link, and it is a fixed set rather than the whole catalogue
- reliability: free requests are logged for data handling, so the allowance is paid for with the prompt text
- evidence:
  - [1] 2026-11-18: free models cost nothing and work with any balance, with separate limits and every request collected | capture: sha256:bf98390889c7aaf1d31f62425fb9742900d6ce94f41fa8bb8f6bc47db41ab05e | quote: A model whose ID ends in `:free` is free: requests cost nothing and work with any balance. Free models have their own limits — see [Tiers and limits](https://docs.fortytwo.network/docs/limits.md). Every request to a free model is collected — see [Data handling](https://docs.fortytwo.network/docs/data-handling.md#free-models).
  - [2] 2026-11-18: the Free tier publishes exact request and token limits | capture: sha256:ed3975ff3e5c7be3e804a6c25f2a4032646291b054aaa42e0afae2e6e079344a | quote: | Free | 5 | 150 | 500,000 | 100,000 | 3,000,000 | 1,000,000 |
- sources:
  - [1] https://docs.fortytwo.network/docs/models
  - [2] https://docs.fortytwo.network/docs/limits
