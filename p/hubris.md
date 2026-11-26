# Hubris

> hubris.pw | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hubris/ | JSON https://fshy.ajam.dev/api/v1/entity/hubris.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hubris

- `inference/hubris` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://hubris.pw/docs/concepts/free-models
- free tier: Models with pricing.is_free are 0 RUB per 1M tokens and work without a deposit (even at a 0 RUB balance), with a limit of 100 requests per user per day in a rolling 24-hour window. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a human creates the key in the account cabinet; free models work with a 0 RUB balance and no deposit
- interface: rest
- limits:
  - request-rate (binding): 100 free requests per user per day, rolling 24h window, shared across all free models [1]
- endpoint: https://api.hubris.pw/v1
- tooling: an OpenAI/Anthropic-compatible key (sk-gw-) created in the account
- composes with: the 100-requests-per-day shared free limit and provider-side 429s are the scarce links
- reliability: provider-side free pools are shared and can return 429 even before the 100/day limit is reached
- evidence:
  - [1] 2026-11-18: free models need no deposit and are limited to 100 requests per user per day | capture: sha256:996d36d75a57912216bbd4c7602762a71cf8fb42d3341ee87375707f08907a9c | quote: Лимит 100 запросов в сутки
- sources:
  - [1] https://hubris.pw/docs/concepts/free-models
