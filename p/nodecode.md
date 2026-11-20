# Nodecode

> nodecode.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nodecode/ | JSON https://fshy.ajam.dev/api/v1/entity/nodecode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nodecode

- `inference/nodecode` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway (CLI-only free key)
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://nodecode.ai/docs/models
- free tier: Cyber v1 is free from the Nodecode CLI once your account has topped up at least $2 (or €2). The top-up stays in your balance. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a card top-up of at least USD 2 or EUR 2 is required before the free key is issued
- interface: rest
- limits:
  - volume-quota (binding): 10M tokens per 24 hours; 30 requests per minute; 2 requests at once; one model, CLI only [1]
- endpoint: https://api.nodecode.ai/v1
- composes with: The free allowance is real but gated behind a small payment and limited to one model through the vendor CLI; other clients get 403.
- reliability: 429 free_daily_used and free_rate_limited with Retry-After; 503 free_capacity_busy when paid calls take capacity
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: a free Cyber v1 key exists but requires a USD 2 or EUR 2 top-up and is limited to 10M tokens per day | capture: sha256:12953a6347bceafcf181fcfe286b32b9f667ea6538443947ad1e46686e76671f | quote: Cyber v1 is free from the Nodecode CLI once your account has topped up at least $2 (or €2). The top-up stays in your balance.
- sources:
  - [1] https://nodecode.ai/docs/models
