# Tavily keyless

> tavily.com | Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tavily/ | JSON https://fshy.ajam.dev/api/v1/entity/tavily.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tavily

- `crawler-scraper/tavily` | qualifies-with-caveat | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.tavily.com/pricing
- free tier: 1,000 API credits a month, no credit card, reset on the first of the month | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: credits reset monthly and do not carry over | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: no credit card stated
- interface: rest
- limits:
  - request-rate (binding): 1,000 credits a month; requests stop when they are spent until the reset or an upgrade [1]
  - request-rate (binding): USD 0.008 per credit pay-as-you-go; Project plan USD 30 a month [1]
- interface detail: REST, API key from the dashboard; Python and JavaScript SDKs
- tooling: not established
- composes with: Keyed search leg. The 1,000 requests monthly allowance is limited for large crawls, and the extract endpoint consumes from the same credit pool.
- reliability: no reliability event recorded
- notes: One credit is not one page: the page states credits are consumed by request type, search, extract or crawl.
- evidence:
  - [1] 2026-10-22: 1,000 free API credits per month with no credit card; credits reset on the first of each month; pay as you go USD 0.008 per credit; Project USD 30 a month
- sources:
  - [1] https://www.tavily.com/pricing

## Tavily keyless route

- `crawler-scraper/tavily-keyless` | qualifies-with-caveat | evidence reported | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-30T11:10:02.157Z (live) | stale on 2026-11-14
- url https://www.tavily.com/
- free tier: Search and Extract free with no account and no API key, rate-limited; the keyless cap is not published | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: no allowance is published | source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: anonymous | detail: no account and no API key; each request carries the header X-Tavily-Access-Mode: keyless
- interface: rest
- limits:
  - request-rate (binding): 429 with Retry-After 600 s was measured at 02:04Z and a 200 at 02:26Z in the platform recon
- interface detail: POST https://api.tavily.com/search or /extract with the header X-Tavily-Access-Mode: keyless, or the remote MCP at mcp.tavily.com/mcp/ with the same header; Crawl, Map and Research need a key
- tooling: not established
- composes with: The last search leg, kept for the case where every keyed provider is spent
- reliability: no reliability event recorded
- notes: The clearest measured hold in the topic: 600 seconds. A caller that retries on a shorter clock burns its own budget and learns nothing.
- evidence note: free tier, identity and route quoted from the vendor's keyless page; the hold length in limits is reported and not re-measured, because the route takes POST and a GET probe cannot exercise it
- evidence:
  - withheld 2026-10-22: probe outcome rate, 0 failures, this deployment's keyless leg
  - [1] 2026-10-30: Search and Extract are free with no account and no API key | capture: sha256:11d99270048de1438976b44140444cbc4b36c544b5dee6fe895b940e482b2e56 | quote: Use Tavily Search and Extract for free, with zero setup. No account, no API key, no configuration.
  - [1] 2026-10-30: the keyless route is the ordinary POST to /search or /extract with the X-Tavily-Access-Mode: keyless header, and the remote MCP takes the same header; Crawl, Map and Research need a key | capture: sha256:11d99270048de1438976b44140444cbc4b36c544b5dee6fe895b940e482b2e56 | quote: Send a request with the `X-Tavily-Access-Mode: keyless` header.
  - [1] 2026-10-30: the keyless route is rate-limited and the page publishes no number for the cap | capture: sha256:11d99270048de1438976b44140444cbc4b36c544b5dee6fe895b940e482b2e56 | quote: Keyless access is free and rate-limited, ideal for exploration and light use.
  - [3] 2026-10-30: keyless limits are separate from the keyed 100 and 1,000 requests a minute, and no keyless number is published | capture: sha256:7da8fc1b0ac14b837a53d21997864d459f6f275344d25a53ea2a9ac6ee7cc17f | quote: Keyless access uses a different error format and separate limits.
  - probe:https://api.tavily.com/search?query=wikipedia 2026-10-30: a GET to the keyless search route answers 405 Method Not Allowed: the route takes POST, which a GET probe cannot exercise | capture: sha256:f88325e1df566fb69288eeece906ac64314bb93bef1f1f3d716e9fcd3cfa53af | quote: "status": 405
- sources:
  - [1] https://docs.tavily.com/documentation/keyless
  - [2] https://www.tavily.com/
  - [3] https://docs.tavily.com/documentation/rate-limits
