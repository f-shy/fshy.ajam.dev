# Scrape.do

> scrape.do | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrape/ | JSON https://fshy.ajam.dev/api/v1/entity/scrape.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrape.do

- `crawler-scraper/scrapedo` | qualifies-with-caveat | evidence reported | binding request-rate | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://scrape.do/
- free tier: 1,000 successful calls a month | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a call | source: [1]
- retention: allowance resets monthly | source: [1]
- egress: not applicable: Markdown or JSON answers | metered: no | source: [1]
- identity: email | detail: signup is an account; no card stated
- interface: rest
- limits:
  - request-rate (binding): 1,000 successful calls a month and 5 concurrent
- interface detail: REST, 5 concurrent on the free tier
- tooling: not established
- composes with: the same as tooling
- reliability: no reliability event recorded
- notes: Only successful calls are counted, which makes a retry free but a failure invisible in the quota.
- evidence note: Unverified against live pricing pages on 2026-10-22.
- evidence:
  - [1] 2026-10-22: 
- sources:
  - [1] https://scrape.do/
