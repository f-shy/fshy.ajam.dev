# DuckDuckGo HTML endpoint

> duckduckgo.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/duckduckgo/ | JSON https://fshy.ajam.dev/api/v1/entity/duckduckgo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DuckDuckGo HTML endpoint

- `crawler-scraper/duckduckgo-html` | dead | evidence measured | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://html.duckduckgo.com/html/
- free tier: no key required; no allowance published | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a query | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable: HTML | metered: no | source: [1]
- identity: anonymous | detail: no key
- interface: rest
- limits:
  - request-rate (binding): unpublished; a 202 with a challenge body was the answer [1]
- interface detail: an HTML search page meant for programmatic use
- tooling: not established
- composes with: Direct web retrieval receives anti-bot challenges identical to origin endpoints.
- reliability: no reliability event recorded
- notes: 202 is the shape to distrust: not a 429, not a 403, and the body carries no results. A scraper that checks the status records a win.
- evidence:
  - [2] 2026-10-22: 202, 14,258 bytes, zero result nodes (result__a count 0), a challenge page
- sources:
  - [1] https://html.duckduckgo.com/html/
  - [2] https://html.duckduckgo.com/html/?q=cloudflare+workers
