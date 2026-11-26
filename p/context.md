# Context.dev

> context.dev | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/context/ | JSON https://fshy.ajam.dev/api/v1/entity/context.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Context.dev

- `crawler-scraper/contextdev` | qualifies | evidence documented | binding request-rate | category reader and extractor API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://context.dev/pricing
- free tier: 1,000 credits a month, no credit card, 10 requests a minute | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a scrape | source: [1]
- retention: credits reset monthly | source: [1]
- egress: not applicable: Markdown answers | metered: no | source: [1]
- identity: email | detail: no credit card stated
- interface: rest
- limits:
  - request-rate (binding): 1,000 credits a month and 10 requests a minute on the free tier; the minute binds first [1]
  - request-rate (binding): Starter USD 19 a month buys 7,500 credits, overage USD 2.20 per 1,000 [1]
- interface detail: REST scrape endpoint; one credit a call at the base rate, 5 with JSON extraction
- tooling: not established
- composes with: Acts as an escalation target for protected origins when standard HTTP retrieval receives an anti-bot challenge.
- reliability: No failure observed across test calls on 2026-10-22.
- notes: Observed reading two Cloudflare-protected forums successfully on 2026-10-22. An allowance of 1,000 credits a month at 10 a minute provides 100 minutes of continuous retrieval.
- evidence note: The verdict rests on the 1,000-credit monthly tier, which is documented from the pricing page. Three live reads were measured and are recorded as evidence; the quota itself was not probed.
- evidence:
  - [1] 2026-10-22: 1,000 free credits a month, no credit card; 1 credit per scrape at the base rate, 5 with JSON extraction; Starter USD 19 a month for 7,500 credits
  - [2] 2026-10-22: 200, 18,041 bytes, x-reader-upstream-status 403, x-reader-fallback challenge, x-web-provider contextdev: the walled forum read came from this provider
  - [3] 2026-10-22: 200, 5,806 bytes, 257 words, final_url the post itself: the pinned read returns the real page where the unpinned one returned an IPv6 notice
- sources:
  - [1] https://context.dev/pricing
  - [2] https://linux.do/
  - [3] https://www.nodeseek.com/post-918318-1?__provider=contextdev
