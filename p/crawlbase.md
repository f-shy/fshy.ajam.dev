# Crawlbase

> crawlbase.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crawlbase/ | JSON https://fshy.ajam.dev/api/v1/entity/crawlbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Crawlbase

- `crawler-scraper/crawlbase` | qualifies-with-caveat | evidence documented | binding per-object-cap | category fetch relay and proxy
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://crawlbase.com/pricing
- free tier: up to 5,000 successful requests free, no credit card | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a successful request | source: [1]
- retention: only successful requests are billed | source: [1]
- egress: not applicable: JSON or HTML answers | metered: no | source: [1]
- identity: email | detail: no credit card required, stated on the page
- interface: rest
- limits:
  - request-rate: USD 0.76 per 1,000 successful requests at 100,000 a month, falling to USD 0.15 at 10,000,000 [1]
  - per-object-cap (binding): Site difficulty and JavaScript rendering multiply group costs by up to a factor of 40. [1]
- interface detail: REST Crawling API, Crawler, Smart AI Proxy and Cloud Storage on one rate card
- tooling: not established
- composes with: Its cb_status field is one of the few provider-level block markers the platform report trusts
- reliability: no reliability event recorded
- notes: The 5,000 is one-time. The multiplier is the trap: a ladder price per 1,000 says nothing about what one defended, rendered page costs.
- evidence:
  - [1] 2026-10-22: up to 5,000 requests free with no credit card; USD 0.76 blended per 1,000 requests at 100,000; site difficulty and JavaScript rendering multiply the rate card
- sources:
  - [1] https://crawlbase.com/pricing
