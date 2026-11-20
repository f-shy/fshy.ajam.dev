# ScraperAPI

> scraperapi.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scraperapi/ | JSON https://fshy.ajam.dev/api/v1/entity/scraperapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ScraperAPI

- `crawler-scraper/scraperapi` | qualifies-with-caveat | evidence documented | binding per-object-cap | category fetch relay and proxy
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.scraperapi.com/pricing/
- free tier: 1,000 API credits on signup, 5 concurrent connections | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: one-time on the free plan | source: [1]
- egress: not applicable: HTML or JSON answers | metered: no | source: [1]
- identity: email | detail: signup; no card stated for the free credits
- interface: rest
- limits:
  - per-object-cap (binding): a standard page is 1 credit; Amazon 5, Google and Bing 25, LinkedIn 30; an automated-traffic filter adds 10 [1]
  - request-rate: 5 concurrent on the free plan [1]
- limits note: the credit multiplier is the binding constraint: a defended page costs 11 credits and a Google SERP 25, so the plan's page count is a fifth to a twenty-fifth of its credit count
- interface detail: REST with a domain-level cost estimator and a per-request max_cost cap
- tooling: not established
- composes with: The clearest published multiplier table in the class, which makes it the reference for what a defended page really costs
- reliability: no reliability event recorded
- notes: A Google SERP costs 25 credits here, so the free grant is 40 searches on the engine that matters most. max_cost per scrape is the one feature worth copying.
- evidence:
  - [1] 2026-10-22: 1,000 free API credits with a maximum of 5 concurrent connections; a standard page costs 1 credit, Amazon 5, Google and Bing 25, LinkedIn 30; sites behind an automated-traffic filter add 10 credits a request
- sources:
  - [1] https://www.scraperapi.com/pricing/
