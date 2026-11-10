# Scrapfly Cloud

> scrapfly.io | Crawling, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scrapfly/ | JSON https://fshy.ajam.dev/api/v1/entity/scrapfly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Scrapfly

- `crawler-scraper/scrapfly` | qualifies-with-caveat | evidence documented | binding per-object-cap | category fetch relay and proxy
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://scrapfly.io/pricing
- free tier: 1,000 API credits on signup, no credit card, 5 concurrent | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: one-time on Free; extra credits not allowed, so the plan hard-caps | source: [1]
- egress: not applicable: JSON, Markdown or HTML answers | metered: no | source: [1]
- identity: email | detail: no credit card required, stated on the free tier
- interface: rest
- limits:
  - request-rate: 1,000 credits on signup, one-time; Pro USD 100 a month for 1,000,000 credits and 20 concurrent [1]
  - per-object-cap (binding): credit cost per request depends on the features enabled: JavaScript rendering, fetch relay, consumer-connection proxies [1]
- limits note: the per-feature multiplier is unpublished, so the page cap cannot be computed from the credit count and the binding constraint is unknown above the floor
- interface detail: REST with JavaScript rendering, a fetch relay and consumer-connection proxies on one credit balance
- tooling: not established
- composes with: A feature-multiplied credit, so a rendered or proxied page costs more than its headline
- reliability: no reliability event recorded
- notes: One thousand credits is a test, not a lane. The unlimited-concurrency claim does not appear; 5 is the number.
- evidence:
  - [1] 2026-10-22: Free tier 1,000 API credits on signup, no credit card, 5 concurrency, overflow is a quota cap; Pro USD 100 a month for 1,000,000 credits
- sources:
  - [1] https://scrapfly.io/pricing

## Scrapfly Cloud Browser

- `compute/scrapfly` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:22.987Z (live) | stale on 2026-12-05
- url https://scrapfly.io/pricing
- free tier: 1,000 API credits on a $0 plan with 5 concurrent requests, hard-capped at the quota with no overflow, and 1 week of log retention | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://scrapfly.io/pricing states credits per request and no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: 'free credits, no card' at scrapfly.io/register, quoted from the pricing page read 2026-10-22
- interface: rest
- limits:
  - request-rate (binding): 1,000 API credits on the free tier, hard-capped with no pay-as-you-go overflow [1]
  - request-rate (binding): 5 concurrent requests on Free, 20 on Pro and up to 100 on Enterprise [1]
  - retention-clamped: log retention is 1 week on Free and 4 weeks on Enterprise [1]
- interface detail: HTTP API (cURL, OpenAPI spec) on every product; SDKs for Python, TypeScript, Go, Rust and Scrapy; the Cloud Browser API gives CDP access (CDP is not a term of the interface vocabulary)
- tooling: Python, TypeScript, Go, Rust and Scrapy SDKs; OpenAPI spec; MCP server; Playwright, Puppeteer or CDP clients drive the Cloud Browser
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the free row: 1,000 credits, 5 concurrency, quota cap and 1 week of retention. The hard cap with no overflow is the constraint a reader needs
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a scrape is a request; the free tier caps the credit count rather than a session
  - free_tier_kind: allowance
  - burst_x: 1.0
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: proxy traffic is 'not allowed' on the free tier
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| Free | $0 | 1,000 | not allowed | 5 | quota cap |' with 'Discovery and Free hard-cap at quota for predictable bills' and 'Self-serve signup: https://scrapfly.io/register (free credits, no card)', quoted
  - [2] 2026-11-03: the docs list a direct HTTP API with an OpenAPI spec, plus SDKs | capture: sha256:1d5a0b851f1858b1836cb686428a124274b302a4a4143ca6d198a60c8d9472ef | quote: Direct API: [cURL](https://scrapfly.io/docs/scrape-api/getting-started) \| [OpenAPI Spec](https://scrapfly.io/docs/openapi)
  - [1] 2026-11-03: pricing is in API credits per request; no egress allowance or overage price is stated | capture: sha256:e9a18b4bf43ae78663b2151abaea324ce95408bf87d45a2e2c1f1ba0a9c21a9a | quote: Credit cost per request depends on the features you enable (JavaScript rendering, Unblocker, residential proxies, country targeting, etc.).
- sources:
  - [1] https://scrapfly.io/pricing
  - [2] https://scrapfly.io/docs
