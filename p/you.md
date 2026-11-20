# You.com

> you.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/you/ | JSON https://fshy.ajam.dev/api/v1/entity/you.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## You.com

- `crawler-scraper/youdotcom` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://you.com/pricing
- free tier: 100 Web Search API queries a day through the hosted MCP route, with no API key, no account and no credit card | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a query | source: [1]
- retention: the keyless daily allowance resets daily | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: the free route states no key, no account and no credit card; the paid route is an account
- interface: rest, rest
- limits:
  - request-rate (binding): Express tier is keyless and metered on an unknown budget [1]
  - request-rate (binding): USD 100 credit with a 60-day expiry. [1]
- interface detail: REST Web Search API and a hosted MCP server; the keyless route is MCP only
- tooling: not established
- composes with: The one anonymous search leg a reader can use before registering anywhere
- reliability: no reliability event recorded
- notes: The keyless route is the only one in this topic with a stated daily number and no identity at all. It is MCP, not a plain HTTP search endpoint, so it needs an MCP client.
- evidence:
  - [1] 2026-10-22: Free: no API key, no account, no credit card, 100 Web Search API queries a day via MCP; pay as you go with no minimums; a call is USD 5 per 1,000
- sources:
  - [1] https://you.com/pricing
