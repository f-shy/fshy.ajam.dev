# Zenrows Browser

> zenrows.com | Crawling, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenrows/ | JSON https://fshy.ajam.dev/api/v1/entity/zenrows.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZenRows

- `crawler-scraper/zenrows` | qualifies-with-caveat | evidence documented | binding per-object-cap | category fetch relay and proxy
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.zenrows.com/pricing
- free tier: 5,000 credits a month, no card, 5 concurrent requests, monthly refresh with no rollover | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: credits refresh monthly; top-up credits roll over one period on paid plans | source: [1]
- egress: not applicable: Markdown, HTML or JSON answers | metered: no | source: [1]
- identity: email | detail: no card, stated on the Free plan
- interface: rest
- limits:
  - request-rate: a standard page is 1 credit, with JavaScript rendering 5, premium proxies 10, both 25 [1]
  - request-rate: 5 concurrent on Free, 20 on Build at USD 19 a month for 45K credits on monthly billing, USD 16 annual [1]
  - per-object-cap (binding): one credit is one plain page, so the effective page cap is the credit count divided by 1, 5, 10 or 25 [1]
- limits note: the credit multiplier is the binding constraint: a plan quoted in credits buys a fifth to a twenty-fifth of its headline in pages, and the multiplier is what decides a plan
- interface detail: REST fetch, extract and batch; crawl is a job plus a poll
- tooling: not established
- composes with: The fetch-relay lane in the platform's read ladder; 1 credit plain makes it cheaper than ScrapingAnt for a page that needs no render
- reliability: no reliability event recorded
- notes: The credit multiplier is the whole story: 5,000 plain pages, 1,000 rendered, 500 behind a premium proxy, 200 with both. Extract is free on top of the fetch it uses. Every per-1,000 figure in the paid lane uses the monthly-billing price, USD 69 for Launch and USD 19 for Build; quoting the annual rate as the price is 20% low.
- evidence:
  - [1] 2026-10-22: Free USD 0 with 5,000 credits a month and no card; standard page 1 credit, JavaScript rendering 5, premium proxies 10, both 25; Build 45,000 to 120,000 credits a month at USD 16 to 33 annual monthly and USD 19 to 39 monthly; Launch 250,000 to 700,000 at USD 58 to 108 annual monthly and USD 69 to 129 monthly; the page states that its headline price is the annual monthly rate, ten months paid for twelve
- sources:
  - [1] https://www.zenrows.com/pricing

## Zenrows Browser Sessions

- `compute/zenrows` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:22.990Z (live) | stale on 2026-12-05
- url https://www.zenrows.com/pricing
- free tier: Free at $0/mo with 5,000 credits a month and 5 concurrent requests, no card | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no egress allowance published at https://www.zenrows.com/pricing; residential proxy bandwidth is metered at 25,000 credits per GB | metered: no | source: [1]
- identity: email | detail: '5,000 credits/month · no card', quoted from the pricing page read 2026-10-22
- interface: rest, cli
- limits:
  - request-rate (binding): 5,000 credits a month on Free; 5 concurrent requests [1]
- interface detail: HTTP API at api.zenrows.com with an OpenAPI 3.1 spec; CLI (npx @zenrows/cli); SDKs; MCP server; the Browser primitive takes Puppeteer or Playwright code over WebSocket
- tooling: CLI (npx -y @zenrows/cli), SDKs, MCP server (npx -y @zenrows/mcp), OpenAPI spec
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states 5,000 credits a month with no card
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; 5 concurrent requests bounds a free account
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$ 0 /mo · 5,000 credits/month · no card · 5 concurrent requests', quoted
  - [2] 2026-11-03: the documentation index says every primitive is reachable over the API, CLI, MCP or an SDK | capture: sha256:d45a94f46d45b33ad45472e058ba8ca8ca4b5579f94ec85ffaa8833061bbf53d | quote: each over the API, CLI, MCP or an SDK.
  - [1] 2026-11-03: residential proxy bandwidth is metered in credits per GB; no egress allowance or overage price is stated | capture: sha256:31d2f29083f1dfeddda5ab6212d522136fbc1989ab98d2006efa465c8655f60e | quote: Residential bandwidth draws 25,000 credits per GB. Browser draws 5 credits a minute.
- sources:
  - [1] https://www.zenrows.com/pricing
  - [2] https://docs.zenrows.com/llms.txt
