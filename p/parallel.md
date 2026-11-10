# Parallel

> parallel.ai | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/parallel/ | JSON https://fshy.ajam.dev/api/v1/entity/parallel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Parallel

- `crawler-scraper/parallel` | qualifies-with-caveat | evidence documented | binding request-rate | category search API | tier Pay as you go
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T01:02:26.754Z (live) | stale on 2026-12-03
- url https://parallel.ai/pricing
- free tier: USD 5 in free credits each month for an organization with a credit card on file, covering up to 5,000 Search API requests | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the pricing page also offers up to USD 80 in credits at signup, with USD 5 in free credits a month
- per-object cap: not applicable | source: [2]
- retention: a new USD 5 credit each month; unused balance expires at the end of the month | source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: card | detail: the USD 5 monthly credit goes only to an organization with a credit card on file, one card activates it for one organization, and usage past USD 5 is billed to that card, with monthly spend limits that email the organization's admins and never block requests; an account opens with an email address or a Google account, and the vendor states a card is needed only for the monthly credit, so the signup credit of up to USD 80 and the hosted MCP server at mcp.parallel.ai/mcp need none; what sets the signup amount is unverified: behind a sign-up
- interface: rest
- limits:
  - request-rate (binding): up to 5,000 requests a month free as a USD 5 monthly credit; Search API 600 requests a minute and Task API 2,000 a minute by default [2]
- binding note: the monthly USD 5 credit, up to 5,000 Search requests, is spent long before 600 requests a minute binds
- interface detail: REST Task, Search, Extract, Responses, Monitor and Find All APIs
- tooling: not established
- composes with: the same as tooling
- reliability: no reliability event recorded
- notes: The monthly credit needs a card on file. A hosted MCP server at mcp.parallel.ai/mcp serves web_search, web_fetch and web_decisions free with no API key at lower rate limits, a separate keyless route.
- evidence note: free tier, rate limits and the card condition quoted from first-party pages; the vendor states a card is needed only for the monthly credit; what sets the signup credit amount, up to USD 80, is behind a sign-up
- evidence:
  - [2] 2026-10-22: Run up to 5,000 requests per month for free; Search API latency 200 ms to 3 s
  - [1] 2026-10-30: the USD 5 monthly credit goes to an organization with a credit card; one card activates one organization; usage past USD 5 is billed to the card; USD 5 covers up to 5,000 Search requests | capture: sha256:1d77792581f7564cad16e1a20ac13856b0ad8cf54f52afc721dd1b530cd842a6 | quote: Starting this week, every eligible Parallel organization with a credit card receives $5 in free credits each month.
  - [2] 2026-10-30: up to USD 80 in credits at signup and USD 5 in free credits a month | capture: sha256:f87ebb86392637478b5e3bc81634ddba06c7163c0054612f66f7b719e3168787 | quote: Earn up to $80 at signup + $5 in free credits per month
  - [1] 2026-10-30: a new credit arrives each month and unused balance expires at month end | capture: sha256:1d77792581f7564cad16e1a20ac13856b0ad8cf54f52afc721dd1b530cd842a6 | quote: Any unused balance expires at the end of the month.
  - [2] 2026-10-30: up to 5,000 requests a month free; the same page lists 600 requests a minute for Search and 2,000 for Task | capture: sha256:f87ebb86392637478b5e3bc81634ddba06c7163c0054612f66f7b719e3168787 | quote: Run up to 5,000 requests per month for free
  - [3] 2026-10-30: the hosted MCP server serves web_search, web_fetch and web_decisions free with no API key, at lower rate limits | capture: sha256:82904beb52f68df64f39abddf4c966d35d9375b859ddad432b0525070c4bde1d | quote: No API key is required to get started: `web_search`, `web_fetch`, and `web_decisions` are free at lower rate limits.
  - [4] 2026-10-30: the default Search quota is 600 requests a minute, counted per POST to /v1/search | capture: sha256:c3c59662a0675b44838ec5dc73584a664fcbaaab506bd301d3524cab905aa161 | quote: | Search | 600 per min | Each POST to `/v1/search` |
  - [2] 2026-11-01: the pricing page names the metered plan that carries the USD 5 monthly credit Pay as you go | capture: sha256:f87ebb86392637478b5e3bc81634ddba06c7163c0054612f66f7b719e3168787 | quote: Pay as you go
  - [5] 2026-11-01: the vendor's comparison table states the hosted MCP server needs no account, up to USD 80 is earned at signup, and a card is needed only for the monthly credit | capture: sha256:98bf4564c875b71f5ddf2fceb6f8bb9e50ff37d981ab17f46eb999935bd958a4 | quote: | Parallel | Hosted MCP server (no account), up to $80 to earn at signup, $5/month | Only for the monthly credit | Lower limits for anonymous MCP use. API: 600 Search requests/min (default for all accounts) | Monthly |
  - [6] 2026-11-01: the platform sign-up page offers sign-up with an email address or with a Google account | capture: sha256:47d094eb9e8c20322c7d07186fc522e906d64849b127d3705b9bca261f7b03e8 | quote: Sign up with email Sign up with Google
  - [7] 2026-11-01: monthly spend limits email the organization's admins and never block requests | capture: sha256:83a273ea535410b9b778b8ea0098706b351018b6d8839a90cbdf2df3fd4ea34a | quote: Limits are notify-only; they never block requests.
  - [1] 2026-11-01: the unused part of the monthly credit expires at the end of the month | capture: sha256:1d77792581f7564cad16e1a20ac13856b0ad8cf54f52afc721dd1b530cd842a6 | quote: Any unused balance expires at the end of the month.
  - [2] 2026-11-01: the pricing page states up to 5,000 requests a month free | capture: sha256:f87ebb86392637478b5e3bc81634ddba06c7163c0054612f66f7b719e3168787 | quote: Run up to 5,000 requests per month for free
  - [4] 2026-11-01: the default Search quota is 600 requests a minute, counted per POST to /v1/search | capture: sha256:c3c59662a0675b44838ec5dc73584a664fcbaaab506bd301d3524cab905aa161 | quote: | Search | 600 per min | Each POST to `/v1/search` |
  - [4] 2026-11-01: the default Task quota is 2,000 runs a minute | capture: sha256:c3c59662a0675b44838ec5dc73584a664fcbaaab506bd301d3524cab905aa161 | quote: | Tasks/TaskGroups | 2,000 per min | Each Task Run created through `/v1/tasks/runs` or `/v1/tasks/groups/{taskgroup_id}/runs` |
  - [3] 2026-11-01: the hosted MCP server at mcp.parallel.ai/mcp serves web_search, web_fetch and web_decisions free with no API key, at lower rate limits | capture: sha256:fe7b669c6776a130eec48ce9a7ab8cc8fc928f8fd8645101550c56f6f6c881e7 | quote: No API key is required to get started: `web_search`, `web_fetch`, and `web_decisions` are free at lower rate limits.
  - [8] 2026-11-01: the vendor states it does not publish the anonymous rate limit of the hosted MCP server | capture: sha256:ab133a1144f9c18135a09681952140bd349f3ca06a5b26e6692c44a79a4808f3 | quote: we don’t publish the anonymous rate limit, and mode and domain overrides only work once you authenticate.
  - probe:https://mcp.parallel.ai/mcp 2026-11-01: a GET to the hosted MCP endpoint without credentials answers HTTP 405: the route takes POST | capture: sha256:80b121e1a6bbcb8962a87da42495069f93000e4e152939f414ca1689e9dbcd8a | quote: "status": 405
  - probe:https://mcp.parallel.ai/mcp?login 2026-11-01: a GET to the key-gated /mcp?login endpoint without credentials answers HTTP 401 | capture: sha256:06730629ba48edb56fca7fcc3f62946d2c2b3bf050e80ffa064c7d8f1347ebe5 | quote: "status": 401
  - probe:https://mcp.parallel.ai/mcp?login 2026-11-01: the /mcp?login endpoint answers that it needs a Parallel API key or a sign-in | capture: sha256:a775c841d441f63e15de6ad10c8ddbaba969edd1042406b41e0766b1c118f6c3 | quote: This endpoint needs a Parallel API key. Sign in, or send x-api-key or Authorization: Bearer.
  - [1] 2026-11-01: the USD 5 monthly credit goes to each eligible organization with a credit card | capture: sha256:1d77792581f7564cad16e1a20ac13856b0ad8cf54f52afc721dd1b530cd842a6 | quote: Starting this week, every eligible Parallel organization with a credit card receives $5 in free credits each month.
- sources:
  - [1] https://parallel.ai/blog/free-tier-parallel
  - [2] https://parallel.ai/pricing
  - [3] https://docs.parallel.ai/integrations/mcp/quickstart
  - [4] https://docs.parallel.ai/resources/rate-limits
  - [5] https://parallel.ai/articles/best-free-web-search-api
  - [6] https://platform.parallel.ai/signup
  - [7] https://docs.parallel.ai/resources/faqs
  - [8] https://parallel.ai/articles/best-free-web-search-mcp
