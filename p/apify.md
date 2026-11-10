# Apify

> apify.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apify/ | JSON https://fshy.ajam.dev/api/v1/entity/apify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apify

- `crawler-scraper/apify` | qualifies-with-caveat | evidence documented | binding per-object-cap | category crawl API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://apify.com/pricing
- free tier: USD 5 of platform usage a month on the Free plan, 5 concurrent runs | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a compute unit | source: [1]
- retention: included usage resets monthly | source: [1]
- egress: not applicable: dataset records | metered: no | source: [1]
- identity: email | detail: the Free plan is a signup; no card stated
- interface: rest
- limits:
  - request-rate: USD 5 included usage a month; USD 0.2 per compute unit on Free; 5 concurrent runs [1]
  - request-rate: proxy traffic USD 8 a gigabyte on Free with 5 IPs included; SERP USD 2.50 per 1,000 [1]
  - per-object-cap (binding): USD 5 of included usage a month buys about 25 compute units at USD 0.20 a unit, so the run length is what the plan buys, not the run count [1]
- limits note: the per-unit price is the binding number: an actor's memory and run time decide how many runs a plan buys
- interface detail: REST and a large Actor store; actors run on the platform's compute
- tooling: not established
- composes with: A place to run somebody else's scraper, which is a different shape from a crawl API that returns pages
- reliability: no reliability event recorded
- notes: The unit is a compute unit, not a page, so the free allowance buys an unknown number of pages before an Actor's own price is counted. The cheapest thing here is the Actor store, not the compute.
- evidence:
  - [1] 2026-10-22: Free USD 0 with USD 5 of included usage a month, USD 0.2 per compute unit, 16 GB memory, 5 concurrent runs; proxy USD 8 a GB; SERP USD 2.50 per 1,000
- sources:
  - [1] https://apify.com/pricing
