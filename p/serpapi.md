# SerpApi

> serpapi.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serpapi/ | JSON https://fshy.ajam.dev/api/v1/entity/serpapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SerpApi

- `crawler-scraper/serpapi` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://serpapi.com/pricing
- free tier: 250 searches a month on the Free plan, 50 an hour | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a search | source: [1]
- retention: allowance resets monthly | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: the Free plan is a signup; no card is stated for it
- interface: rest
- limits:
  - request-rate (binding): 250 searches a month and 50 an hour on Free [1]
  - request-rate (binding): Searcher USD 725 a month for 100,000 searches and 20,000 an hour [1]
- interface detail: REST, Google and other engines as JSON
- tooling: not established
- composes with: A price reference for what a Google-backed search costs at volume, which is the ceiling a free tier is measured against
- reliability: no reliability event recorded
- notes: 250 a month is 8 a day. Only successful searches count, and a response with 100 results costs the same as an empty one.
- evidence:
  - [1] 2026-10-22: Free plan USD 0 with 250 searches a month and 50 a hour throughput; Searcher USD 725 a month for 100,000
- sources:
  - [1] https://serpapi.com/pricing
