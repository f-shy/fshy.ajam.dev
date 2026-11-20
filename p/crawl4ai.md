# Crawl4AI

> crawl4ai.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crawl4ai/ | JSON https://fshy.ajam.dev/api/v1/entity/crawl4ai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Crawl4AI

- `crawler-scraper/crawl4ai` | qualifies-with-caveat | evidence measured | binding request-rate | category crawl API
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:02:31.718Z (live) | stale on 2027-01-02
- url https://crawl4ai.com/
- free tier: 1,000 credits every month once an email is verified, at 10 requests a minute and 2 at a time; a scrape costs 0.5 credit, so about 2,000 pages a month; 20 guest credits with no signup | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: GET /v1/prices gives the free plan an allowance_per_month of 2500: a cap on all credit spent in a month, plan credits and bought extra credits together, not a second grant; the monthly grant is 1000
- per-object cap: not applicable: the unit is a page | source: [1]
- retention: the monthly free credit resets on the 1st of each calendar month; extra credits bought on a plan never expire | source: [1]
- egress: not applicable: Markdown answers | metered: no | source: [1]
- identity: email | detail: a 7-day pass key is issued with no signup and carries the guest credits; the monthly credits need a verified email, which replaces the pass key with a permanent one; no card
- interface: rest
- limits:
  - request-rate (binding): 10 requests a minute, 5 per 10 seconds, 2 at a time and 20 searches a minute on the free plan [2]
  - per-object-cap: a batch takes at most 50 URLs [3]
  - request-rate (binding): 1,000 credits a month on the free plan: a page costs 0.5 credit at the base price, 1 credit in a real browser and 2 on a hard site, so the month holds 2,000, 1,000 or 500 pages [1]
  - per-object-cap: a bulk job takes at most 10,000 URLs, submitted once and polled while it runs in the background [3]
- limits note: over the 10-a-minute limit the API answers 429 and the free plan only limits the pace; at zero credit it answers 402 no_credit, and an account without a plan gets 402 plan_needed from a top-up
- binding note: the monthly grant ends a free month before the pace does: 1,000 credits at 0.5 credit a scrape are 2,000 scrapes, which 10 requests a minute spends in 200 minutes
- interface detail: REST scrape, batch and job routes; per-response cost headers
- tooling: REST with a Bearer key; an MCP server; x-c4-cost, x-c4-balance and x-c4-allowance-left headers on each answer
- composes with: Cheapest page unit in the read ladder at 0.5 credit; a plausible first leg once its free allowance is confirmed
- reliability: no reliability event recorded
- notes: GET /v1/prices declares a 1000-credit monthly grant and a 2500-credit monthly allowance cap for the free plan; at 0.5 credit a scrape the grant is 2,000 pages. x-c4-allowance-left on each answer carries what is left under the month's cap.
- evidence note: free-plan limits and grants read from GET /v1/prices with no key; the homepage and llms.txt read again
- evidence:
  - [1] 2026-10-22: 
  - [1] 2026-10-30: 20 credits come with no signup and 1,000 credits a month after an email is verified | capture: sha256:8df2d270bf827a8f178b7482c204e7e0871243ab422ebdb4687e0e4567cd2b83 | quote: Try it now: 20 free credits, no signup. Verify your email for 1,000 free credits every month.
  - probe:https://api.crawl4ai.com/v1/prices 2026-10-30: the free plan allows 10 requests a minute, 5 per 10 seconds, 2 at a time, 20 searches a minute and 3 keys, under a 2,500-credit monthly allowance | capture: sha256:f5c555341e5f728a3cd3c641edcb29b82059645d63c9a76b8d4365021f5576e0 | quote: "free":{"allowance_per_month":2500,"concurrent":2,"keys":3,"requests_per_10s":5,"requests_per_minute":10,"search_per_minute":20}
  - [3] 2026-10-30: the monthly allowance resets on the 1st | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: it resets on the 1st; a bigger plan lifts it
  - [3] 2026-10-30: a batch takes at most 50 URLs | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: Scrape up to 50 URLs in one call.
  - [3] 2026-10-30: a pass key comes at once; the monthly credit and a permanent key need a verified email | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: issued instantly; verify your email for a permanent key and the monthly free credit
  - [3] 2026-10-30: each answer carries its cost, the balance and the allowance left | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: The response carries `x-c4-cost`, `x-c4-balance` and `x-c4-allowance-left` (credits left under this month's plan allowance) in credits
  - [3] 2026-10-30: the allowance caps plan credits and extra credits together | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: Each plan has a monthly credit allowance that covers the plan's credits and any extra credits
  - [1] 2026-10-30: the free tier needs no card | capture: sha256:8df2d270bf827a8f178b7482c204e7e0871243ab422ebdb4687e0e4567cd2b83 | quote: $0 · no card
  - probe:https://api.crawl4ai.com/search?q=web+scraping 2026-10-30: a keyless GET /search answered 401 with no body: the API wants a key, even a pass key | capture: sha256:bcb37060162066a624070d12b8ff5b3966f76955b079a7fc5575cb3704d9ae5b | quote: "status": 401
  - [1] 2026-11-01: the free plan grants 1,000 credits every month, and a page costs 0.5 credit at the base price, 1 in a real browser and 2 on a hard site | capture: sha256:8df2d270bf827a8f178b7482c204e7e0871243ab422ebdb4687e0e4567cd2b83 | quote: Verify your email for 1,000 free credits every month. ... page 0.5 · search 1 · from our archive 0.25 · real browser 1 · hard site 2
  - [3] 2026-11-01: POST /scrape/jobs takes up to 10,000 URLs in one submission, which drains in the background while the caller polls | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: POST /scrape/jobs — large async jobs ... For big lists (up to 10,000 URLs), or when your code cannot hold a connection open for slow pages. Submit once, get a job id, then poll while it drains in the background.
  - [3] 2026-11-01: the pace limit answers 429 and only slows the free plan, while zero credit answers 402 no_credit and a top-up needs a plan | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: Per-plan rate limits return `429` ... the free plan only limits the pace ... At zero credit the gate answers `402 {"error":"no_credit"}` ... an account without a plan gets `402 {"error":"plan_needed"}` from the top-up.
  - probe:https://api.crawl4ai.com/v1/prices 2026-11-01: the live price table grants 1,000 credits a month, prices a scrape at 0.5 credit and paces the free plan at 10 requests a minute | capture: sha256:f5c555341e5f728a3cd3c641edcb29b82059645d63c9a76b8d4365021f5576e0 | quote: "scrape":"0.50" ... "credit":{"guest":"20.00","monthly":"1000.00" ... "free":{"allowance_per_month":2500,"concurrent":2,"keys":3,"requests_per_10s":5,"requests_per_minute":10,"search_per_minute":20}
  - [3] 2026-11-01: a batch takes at most 50 URLs in one call and bills one unit per URL | capture: sha256:a3fe0fc335f4c5d6958871d4d86cbce9efc249a8741a3741779b521f31a477fc | quote: Scrape up to 50 URLs in one call. Results stream back as NDJSON — one JSON line per URL as it finishes. Bills one unit per URL.
  - probe:https://api.crawl4ai.com/v1/prices 2026-11-01: a scrape is 0.50 at the base level; a page a real browser rendered is 2.0 times and a hard-site page 4.0 times the base | capture: sha256:f5c555341e5f728a3cd3c641edcb29b82059645d63c9a76b8d4365021f5576e0 | quote: "scrape":"0.50" ... {"level":3,"mult":2.0,"name":"heavy","text":"a real browser rendered it"},{"level":4,"mult":4.0,"name":"hard"
  - [4] 2026-11-01: an account holds an email and, when one is used, a Google or GitHub sign-in identifier; card details are handled for paid tiers only | capture: sha256:b0e3c4a7065dfb3c68021216c6c16caf87cdec1f910fcb4d5e2d1092643afe2f | quote: Account - your email, the identifier from your sign-in provider (Google/GitHub) when you use one, and your login. ... Billing - for paid tiers, our processor Stripe handles your card…
  - [1] 2026-11-01: 20 credits come with no signup; the Free tier is $0 with no card and gives 1,000 credits every month once an email is verified, at 10 a minute and 2 at a time | capture: sha256:8df2d270bf827a8f178b7482c204e7e0871243ab422ebdb4687e0e4567cd2b83 | quote: Try it now: 20 free credits, no signup. Verify your email for 1,000 free credits every month. ... Free $0 · no card Prototypes and side projects. 1,000 credits every month, 10 a minute, 2 at a time.
- sources:
  - [1] https://crawl4ai.com/
  - [2] https://api.crawl4ai.com/v1/prices
  - [3] https://crawl4ai.com/llms.txt
  - [4] https://crawl4ai.com/legal/
