# Diffbot

> diffbot.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/diffbot/ | JSON https://fshy.ajam.dev/api/v1/entity/diffbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Diffbot

- `crawler-scraper/diffbot` | qualifies-with-caveat | evidence documented | binding request-rate | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.diffbot.com/pricing/
- free tier: 10,000 credits a month on the Free plan, 5 requests a minute, no credit card | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: credits reset monthly | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: no credit card required, stated on the Free plan
- interface: rest
- limits:
  - request-rate (binding): 5 requests a minute on Free [1]
  - request-rate (binding): 10,000 credits a month; Startup USD 299 a month [1]
- interface detail: REST Article, Product, Discussion and Knowledge Graph APIs
- tooling: not established
- composes with: The structured extractor; its Knowledge Graph queries cost 25 credits each, so a KG lookup is 25 pages of budget
- reliability: no reliability event recorded
- notes: 5 a minute is 300 an hour, so 10,000 credits is 33 hours of continuous work and the month ends before the credits do.
- evidence note: page read; the platform report records the page carrying 9,500 as well as 10,000, which this read did not reproduce
- evidence:
  - [1] 2026-10-22: Free: 10,000 credits a month, all four APIs, no credit card, 5 requests a minute; Startup USD 299 a month
- sources:
  - [1] https://www.diffbot.com/pricing/
