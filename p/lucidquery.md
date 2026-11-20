# LucidQuery

> lucidquery.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lucidquery/ | JSON https://fshy.ajam.dev/api/v1/entity/lucidquery.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LucidQuery

- `inference/lucidquery` | paid-only | evidence documented | binding volume-quota | category inference gateway (prepaid)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://lucidquery.com/docs
- free tier: The AGI 01 family covers general and flagship intelligence. Switch models with a single string; pricing is per million tokens, billed from your prepaid balance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: keys are created in a dashboard and kept server-side; no free signup credit stated
- interface: rest
- limits:
  - request-rate: default new-key limits are 100 requests and 1,000,000 tokens per minute [1]
  - volume-quota (binding): the binding constraint named on the first-party page [1]
- endpoint: https://api.lucidquery.com/v1
- composes with: No free text inference allowance is published in the fetched docs or pricing page.
- reliability: 429 rate_limit_error on a per-key window; 402 insufficient_quota when credits run out
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: LucidQuery bills per million tokens from a prepaid balance with no free allowance stated | capture: sha256:33e98086167cfde3730ba1e73c635546ae38817e9d4e94a92fb24198340e181d | quote: The AGI 01 family covers general and flagship intelligence. Switch models with a single string; pricing is per million tokens, billed from your prepaid balance.
- sources:
  - [1] https://lucidquery.com/docs
