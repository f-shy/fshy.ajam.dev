# Browserless

> browserless.io | Compute, Crawling; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browserless/ | JSON https://fshy.ajam.dev/api/v1/entity/browserless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Browserless (Compute)

- `compute/browserless` | qualifies-with-caveat | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:20.760Z (live) | stale on 2026-12-05
- url https://www.browserless.io/pricing
- free tier: Free plan at USD 0 a month, no card required: 1,000 units a month, 2 max concurrent browsers, 2-minute max session time, 1 day of persisted sessions and replays, consumer-connection proxies at 6 units per MB and datacenter at 2 units per MB, automatic human-verification handling, and Chrome, WebKit and Firefox on San Francisco, London and Amsterdam endpoints. One unit is a block of browser time of up to 30 seconds per browser connection | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: 1,000 units at up to 30 s each is 8.3 browser hours a month, and the 2-minute session cap forces a new connection per 2 minutes. Paid plans are Prototyping USD 25, Starter USD 140 and a USD 350 tier above those
- per-object cap: not applicable
- retention: not stated in catalogue documentation.
- egress: no general data-transfer allowance or per-GB price published; only proxy traffic is metered, at 6 units per MB (residential) and 2 units per MB (datacenter) from the same unit pool, with units over the pool at USD 0.0020 on Prototyping | metered: yes | source: [1]
- identity: email | detail: the free plan needs an email signup and no card; a paid plan needs a payment method
- interface: rest
- limits:
  - request-rate: 2 concurrent browsers on Free, 10 on Prototyping, 40 on Starter [1]
  - retention-clamped (binding): 2-minute maximum session time on Free; session reconnects bill a fresh unit [1]
  - per-object-cap: consumer-connection proxy is 6 units per MB and datacenter 2 units per MB, drawn from the same 1,000-unit pool [1]
- limits note: the entry paid plan is USD 350 a month, and the free plan is not a trial: it renews monthly with no card
- binding note: the 2-minute session cap and the unit-per-reconnect rule bind before the 1,000-unit pool does, because a crawl that needs a longer session pays twice for the same page
- interface detail: a REST API of single-action HTTP endpoints, plus Playwright and Puppeteer over a CDP WebSocket
- tooling: Playwright and Puppeteer over CDP; a REST API
- composes with: none at this price: a crawl that can use a USD 19 plan should
- reliability: no reliability event recorded
- notes: The USD 350 tier is above Prototyping and Starter, not below them. The row is a small free allowance rather than a paid-only row.
- extras:
  - billing_model: wall-clock
  - session_cap.wall_clock_min: 2
  - session_cap.restart_required: yes
  - session_cap.note: 2 min maximum session on Free; a reconnect bills a fresh unit
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.static_ip: no
  - network_out.per_session_bytes: consumer-connection proxy 6 units per MB
  - free_tier_kind: allowance
  - reclassified_from: paid-only
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: a Free plan at USD 0/month, 'No card required', 1k units/month, 2 max concurrent browsers, 2 min max session time; 'A Unit is a block of browser time of up to 30 seconds per browser connection'
  - [1] 2026-11-03: proxy traffic is metered in units per MB; no other transfer allowance is listed | capture: sha256:dc85a4b3308599fcff2be66a1d8aadf0366c4ca60f20374a26a1f4a3b3977a54 | quote: 6 Unitsper MB for Residential Proxy
  - [2] 2026-11-03: a REST API exists | capture: sha256:500db399727539a7fb4b49e039f86d43aaa3e2fd7c4ca239bc49bf7ead3f9614 | quote: Browserless REST APIs provide HTTP endpoints for common browser tasks like
  - [1] 2026-11-03: Playwright and Puppeteer connect by changing the endpoint | capture: sha256:dc85a4b3308599fcff2be66a1d8aadf0366c4ca60f20374a26a1f4a3b3977a54 | quote: Quick endpoint change enables connection with existing scripts.
- sources:
  - [1] https://www.browserless.io/pricing
  - [2] https://docs.browserless.io/rest-apis/intro

## Browserless (Crawling)

- `crawler-scraper/browserless` | qualifies-with-caveat | evidence documented | binding retention-clamped | category headless browser
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.browserless.io/pricing
- free tier: 1,000 units a month, no card, 2 concurrent browsers, 2 minutes maximum session | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is browser time | source: [1]
- retention: unit is 30 seconds of browser connection; longer runs bill another unit | source: [1]
- egress: 1 day of persisted sessions and replays on Free | metered: no | source: [1]
- identity: email | detail: no card required, stated on the Free plan
- interface: rest
- limits:
  - request-rate: 1 unit per 30 seconds of browser connection; 1,000 units is about 8.3 hours a month [1]
  - request-rate: 2 concurrent browsers and a 2 minute maximum session on Free [1]
  - per-object-cap: a consumer-connection proxy costs 6 units a megabyte, a datacenter proxy 2, handling one human-verification step 10 [1]
  - retention-clamped (binding): a unit is 30 seconds of browser connection and a Free session ends at 2 minutes, so it is the session length and not the request count that caps the work [1]
- limits note: the 30-second unit and the 2-minute maximum session bind first: 1,000 units is about 8.3 browser-hours a month and no single session may run past 2 minutes
- interface detail: REST and WebSocket; BrowserQL; crawls are a job plus a poll
- tooling: not established
- composes with: Reserve lane behind Browser Rendering; the only third-party browser with a recurring monthly grant and no card
- reliability: no reliability event recorded
- notes: The unit is time, not pages, so a fast page is cheap and a slow one is not. 1,000 units is 8.3 hours of browser time a month, which is more than it reads as.
- evidence note: pricing page read; the 1,000 units a month figure is stated on the page
- evidence:
  - [1] 2026-10-22: Free USD 0 a month, no card, 1k units, 2 max concurrent browsers, 2 min max session; a unit is up to 30 seconds of browser connection; 6 units per MB consumer-connection proxy, 10 units per human-verification step handled
- sources:
  - [1] https://www.browserless.io/pricing
