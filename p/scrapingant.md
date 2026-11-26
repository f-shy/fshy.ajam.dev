# ScrapingAnt

> scrapingant.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapingant/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapingant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ScrapingAnt

- `crawler-scraper/scrapingant` | qualifies-with-caveat | evidence documented | binding per-object-cap | category access helper and proxy
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://scrapingant.com/
- free tier: 10,000 credits a month, no credit card, refreshed monthly | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: credits refresh monthly | source: [1]
- egress: not applicable: HTML, Markdown or text answers | metered: no | source: [1]
- identity: email | detail: no credit card required, stated twice on the page
- interface: rest
- limits:
  - per-object-cap (binding): the default request costs 10 credits, so 10,000 credits is 1,000 pages [1]
  - request-rate: most requests cost between 1 and 25 credits depending on proxy type and rendering [1]
- limits note: the default request is 10 credits, so the 10,000-credit free tier is 1,000 pages and the credit headline overstates the tier tenfold
- interface detail: REST with three agent-callable MCP tools: get_web_page_html, get_web_page_markdown, get_web_page_text
- tooling: not established
- composes with: A rendered page at 10 credits is ten times Firecrawl's 1 credit, so it is the wrong first leg and a reasonable last one
- reliability: no reliability event recorded
- notes: The clearest arithmetic trap in the class: the headline is 10,000 and the usable figure is 1,000, because the default request is a rendered page at 10 credits. A page that quotes 10,000 has overstated the tier tenfold.
- evidence:
  - [1] 2026-10-22: 10K free credits, no card; 10,000 free credits every month; the default request, Chrome rendering with standard proxies, costs 10 credits; most requests cost 1 to 25
- sources:
  - [1] https://scrapingant.com/
