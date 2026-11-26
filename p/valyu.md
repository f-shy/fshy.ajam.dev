# Valyu

> valyu.ai | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/valyu/ | JSON https://fshy.ajam.dev/api/v1/entity/valyu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Valyu

- `crawler-scraper/valyu` | trial-only | evidence documented | binding request-rate | category search API
- needs card no, phone no, ID no, institution no | verified 2026-11-02T01:02:19.439Z (live) | stale on 2026-12-03
- url https://docs.valyu.ai/pricing.md
- free tier: USD 10 of free credits on signup, USD 20 with a company email, no card; the free credits expire 12 months after signup | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: Search is billed per result returned, not per request, and priced per source: a 10-result web search is 1 credit, and pay-as-you-go buys 1,600 credits per USD 10. The nearest metered_on term is request-count; the true basis is the count of results returned (result-count), a term the vocabulary lacks.
- per-object cap: not applicable: the unit is a search result | source: [1]
- retention: one-time signup credit; it expires 12 months after signup and does not renew | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: signup by email, Google or GitHub with no card; a company email doubles the signup credit to USD 20
- interface: rest
- limits:
  - request-rate (binding): USD 10 one-time (USD 20 with a company email), about 1,600 ten-result web searches at 1 credit each; a request the balance cannot cover answers 402 and nothing is billed as overage [1]
  - request-rate (binding): 5 search requests a second on the Pay-as-you-go plan and 10 on Ridiculously Cheap, per the documented 429 example; limits are per organisation and per endpoint, with no daily quota; unverified: the plan and search rate of an account that holds only signup credits, which the billing page, `valyu account whoami` and the plan field of a keyed 429 body show, behind a sign-up [2]
  - request-rate (binding): 10 requests per second with bursts up to 20 and 86,400 requests per day by default, an over-limit request answered 403, per the OpenAPI description on the Search reference page; the API overview documents per-plan limits answered 429 with no daily quota instead [3]
- limits note: The pricing page lists the signup credit in its Pay As You Go plan card, priced Free, with every data source while the free credits last and then web, arXiv and PubMed on pay-as-you-go, and the academia page says new accounts get the credits across every source and then pay as you go; the documented plan IDs are tier_0 Pay-as-you-go, tier_1 Ridiculously Cheap, tier_2 Comfortably Pro and tier_3 Serious Business, with no plan named for signup credits
- binding note: the one-time signup balance is exhausted long before the 5-a-second rate limit is reached
- interface detail: POST https://api.valyu.ai/v1/search with an x-api-key header; Contents, Answer and DeepResearch endpoints draw on the same key and balance; a hosted MCP server is offered
- endpoint: part of interface detail
- tooling: Python SDK (pip install valyu), TypeScript SDK (valyu-js), Rust SDK, a CLI and a hosted MCP server
- composes with: A bounded search leg whose one key also reaches SEC filings, arXiv, PubMed, patents and clinical trials, priced per result; the signup balance is spent once, so it suits a finite job rather than a standing crawl
- reliability: a keyless GET to /v1/search answered 403 with a missing-token message, so there is no anonymous route; no throttle or ban event recorded
- notes: Search is priced per result by source: 0.1 credit per web or news result, 0.05 for arXiv and PubMed, 1.92 for SEC filings, 4.8 for Wiley publications. Monthly plans start at USD 29 for 5,000 credits. The free balance reaches every source on the standard plans while it lasts.
- evidence note: the signup credit, its 12-month expiry, the no-card statement and the per-result price are quoted from first-party documentation; no keyed search was made, so the read path is unprobed; a keyed call that returns results would raise it to measured
- evidence:
  - [1] 2026-10-30: the signup credit is one-time and expires 12 months after signup | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: Free credits expire 12 months after signup.
  - [1] 2026-10-30: USD 10 free on signup, USD 20 with a company email, no card | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: New accounts get \$10 of free credits, or \$20 when you sign up with a company email. No card is required.
  - [1] 2026-10-30: a 10-result web search costs 1 credit | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: A web search that returns 10 results uses 1 credit, and a `standard` DeepResearch task uses 100.
  - [1] 2026-10-30: pay-as-you-go buys 1,600 credits per USD 10, which is 1,600 ten-result web searches | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: | Pay-as-you-go | 1,600 per \$10 | 1,600 | 16 |
  - [2] 2026-10-30: the documented 429 example sets 5 search requests a second on the Pay-as-you-go plan | capture: sha256:d068625575a023ea4db8a86f9bfb223f344b383e79be5dd3c637b088bbcf0b6c | quote: Search rate limit reached: your Pay-as-you-go plan allows 5 requests per second.
  - [2] 2026-10-30: rate limits are per second with no daily quota | capture: sha256:d068625575a023ea4db8a86f9bfb223f344b383e79be5dd3c637b088bbcf0b6c | quote: There is no daily quota.
  - [4] 2026-10-30: the signup page offers email, Google or GitHub with free credits and no card | capture: sha256:4af3a59ebb4f2c042a3088fdf1847d471cce73920dda4a90175388218ce77619 | quote: Free credits on signup · no card required
  - [5] 2026-10-30: an exhausted balance pauses requests rather than billing overage | capture: sha256:16efefb6579935b281711f692429c18fad8efad203afe6558182d2ddf6de54d3 | quote: When your balance hits zero, new requests are paused until you add credits, so you never get a surprise overage bill.
  - probe:api.valyu.ai/v1/search 2026-10-30: a keyless GET to the search endpoint answered 403 with a missing-token body | capture: sha256:f249b63cb2fcb66b47e86f906c98f8fd912e82dd035b4e53d7e72fc1960cfd16 | quote: {"message":"Missing Authentication Token"}
  - [2] 2026-11-01: the documented 429 example gives the Pay-as-you-go plan 5 search requests a second and Ridiculously Cheap 10 | capture: sha256:984e865768830fa44c84cb71f49fc2a066dff030bd6ef7dd16f1a2dc69fd2354 | quote: Search rate limit reached: your Pay-as-you-go plan allows 5 requests per second. Retry after 2 seconds. Upgrade to Ridiculously Cheap for 10 requests per second:
  - [3] 2026-11-01: the OpenAPI description on the Search reference states a default of 10 requests per second, bursts up to 20 and 86,400 requests a day | capture: sha256:8a0b22d7008a4f900e2f961ffda4c1b238701d1364c126d76330521ba1c2c0b8 | quote: Limits apply per organisation: 10 requests per second with bursts up to 20, and 86,400 requests per day by default.
  - [6] 2026-11-01: the documented plan IDs are tier_0 Pay-as-you-go to tier_3 Serious Business, with no plan named for signup credits | capture: sha256:9218d746fb737bbb10c4c314f0d945af5fd556ac22550144e1a2722fda9fd87a | quote: Plan IDs map to plans as follows: `tier_0` Pay-as-you-go, `tier_1` Ridiculously Cheap (\$29/mo), `tier_2` Comfortably Pro (\$99/mo), `tier_3` Serious Business (\$499/mo).
  - [1] 2026-11-01: Search is charged per result returned, priced per source, and not as a flat fee per query | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: Search charges credits for the results it returns, priced per source. It is not a flat fee per query and is not based on tokens.
  - [5] 2026-11-01: the Pay As You Go plan card of the pricing page is priced Free and holds the signup credit of USD 10, or USD 20 with a work email, with no card | capture: sha256:11e3952e89ecc66f606c4374e09b8be797b8689940fc31724b3fc41c0028f348 | quote: Pay As You Go1,600 CREDITS PER $10 Free $10 free credits on signup, $20 with a work email. No card required.
  - [7] 2026-11-01: new accounts get the signup credit across every source and then pay as you go, which covers web search, arXiv and PubMed | capture: sha256:286a550ec5bdaac8c0c017edc3295f07f8b517f94fcaf2448044ab17d03752ac | quote: New accounts get $10 in free credits ($20 with a work email) across every source, then pay as you go. Pay-as-you-go covers web search, arXiv and PubMed.
  - [8] 2026-11-01: the changelog entry of October 21, 2026 states that rate limits scale with the plan and that there is no daily quota | capture: sha256:43908308815234b8742cca21731d22583b81d255ac3b5df02c9acccacf0bf97a | quote: Search, Contents, Answer, and creating or polling DeepResearch tasks each have their own limit, lower on cheaper plans and higher on paid plans. There is no daily quota.
  - [9] 2026-11-01: the OpenAPI file itself carries the same default-rate sentence | capture: sha256:e8b8d9e9ecd8627c2f69b448fd7b62586099648a3821f75fee089c79d719dff2 | quote: Limits apply per organisation: 10 requests per second with bursts up to 20, and 86,400 requests per day by default.
  - [2] 2026-11-01: rate limits apply per organisation and per endpoint, and are lower on cheaper plans | capture: sha256:984e865768830fa44c84cb71f49fc2a066dff030bd6ef7dd16f1a2dc69fd2354 | quote: Limits apply per organisation and per endpoint. Search, Contents, Answer, and creating or polling DeepResearch tasks each have their own limit. The limit is lower on cheaper plans and higher on paid plans.
  - [1] 2026-11-01: USD 10 of free credits on signup, USD 20 with a company email, no card | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: New accounts get \$10 of free credits, or \$20 when you sign up with a company email. No card is required.
  - [1] 2026-11-01: the signup credit expires 12 months after signup | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: Free credits expire 12 months after signup.
  - [1] 2026-11-01: a request that the balance cannot cover answers 402 and is not run, with no overage charge | capture: sha256:ae12968c52ddd9186c828089f7eabf23e44126359e8b7cf03df0f6828a8f7114 | quote: There are no overage charges. When your balance cannot cover a request, the API returns `402 Payment Required` and does not run it.
  - [4] 2026-11-01: the sign-in page offers sign-up by email, Google or GitHub and states free credits with no card | capture: sha256:2b1b664f663a7d717a166b89fa3804d0e92db40cd5e6fa8b82d2272f5821e5b1 | quote: Email Continue with email or Google GitHub Free credits on signup · no card required
  - [2] 2026-11-01: requests go to api.valyu.ai with the key in an x-api-key header and JSON bodies | capture: sha256:984e865768830fa44c84cb71f49fc2a066dff030bd6ef7dd16f1a2dc69fd2354 | quote: Every request goes to `https://api.valyu.ai` and carries your API key in the `x-api-key` header. Request and response bodies are JSON, except Answer, which streams server-sent events.
  - probe:api.valyu.ai/v1/search 2026-11-01: a keyless GET to the search endpoint answered 403 with a missing-token body | capture: sha256:f249b63cb2fcb66b47e86f906c98f8fd912e82dd035b4e53d7e72fc1960cfd16 | quote: {"message":"Missing Authentication Token"}
- sources:
  - [1] https://docs.valyu.ai/pricing.md
  - [2] https://docs.valyu.ai/api-reference/overview.md
  - [3] https://docs.valyu.ai/api-reference/endpoint/search.md
  - [4] https://platform.valyu.ai/
  - [5] https://www.valyu.ai/pricing
  - [6] https://docs.valyu.ai/api-reference/warnings.md
  - [7] https://www.valyu.ai/academia-research
  - [8] https://docs.valyu.ai/changelog/sdk-and-api.md
  - [9] https://docs.valyu.ai/api-reference/openapi.json
