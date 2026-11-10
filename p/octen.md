# Octen

> octen.ai | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/octen/ | JSON https://fshy.ajam.dev/api/v1/entity/octen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Octen

- `crawler-scraper/octenai` | trial-only | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://octen.ai/pricing
- free tier: USD 5 in free balance on signup | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: the balance does not renew | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: signup is an account
- interface: rest
- limits:
  - request-rate (binding): USD 5 one-time balance; the page describes pay-as-you-go or a QPS subscription after it [1]
- interface detail: REST search API
- tooling: not established
- composes with: High quality score on search benchmark evaluations, making the USD 5 trial balance practical for selective queries.
- reliability: no reliability event recorded
- notes: One-time signup balance. Multi-account residual balances do not constitute an official recurring vendor tier.
- evidence:
  - [1] 2026-10-22: sign up and get USD 5 in free balance; plans are pay-as-you-go or a QPS subscription
- sources:
  - [1] https://octen.ai/pricing
