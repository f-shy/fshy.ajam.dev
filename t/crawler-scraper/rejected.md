# Crawling: rejected and dead

> Crawl, search, reader and unblocker APIs for reading the web at scale.

59 records: 38 usable, 9 trial, 1 paid only, 3 rejected, 8 dead. This page lists the rejected and dead records, each with the evidence that rejected it; the usable, trial and paid-only ones are on https://fshy.ajam.dev/t/crawler-scraper.md. Each line: provider (its page in Markdown), record id (its JSON is https://fshy.ajam.dev/api/v1/record/<id>), verdict, free tier, identity, card, phone, evidence, stale date, parsed price, summary. In full: https://fshy.ajam.dev/t/crawler-scraper/llms-full.txt.

## Rejected (3)

- [Brave Search API](https://fshy.ajam.dev/p/brave.md) [`crawler-scraper/brave-search`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/brave-search): fails-identity | free tier | card | no phone | documented | stale on 2026-12-03. USD 5 of free credits every month, applied automatically; Search is priced at USD 5.00 per 1,000 requests, so the credit covers about 1,000 Search requests...
- [Mojeek](https://fshy.ajam.dev/p/mojeek.md) [`crawler-scraper/mojeek`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/mojeek): fails-identity | free tier | card | no phone | documented | stale on 2026-12-03. A free credit on the Startup plan, claimed after signup; a bank card is required to open the account; the credit's size and expiry are unverified: not...
- [Scrapingdog](https://fshy.ajam.dev/p/scrapingdog.md) [`crawler-scraper/scrapingdog`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/scrapingdog): fails-quota | free tier | email | no card | no phone | documented | stale on 2026-12-03. 100 free credits on the FREE plan (USD 0, forever), no credit card; a Google search costs 5 credits, so the 100 credits are 20 Google searches

## Dead (8)

- [12ft.io](https://fshy.ajam.dev/p/12ft.md) [`crawler-scraper/12ft`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/12ft): dead | no free tier | anonymous | no card | no phone | measured. None reachable
- [archive.today](https://fshy.ajam.dev/p/archive-2.md) [`crawler-scraper/archive-today`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/archive-today): dead | no free tier | anonymous | no card | no phone | measured. No account and no key stated; a 429 was the answer to the first followed request
- [Bing Search APIs](https://fshy.ajam.dev/p/microsoft.md) [`crawler-scraper/bing-search-api`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/bing-search-api): dead | no free tier | card | no phone | documented. none: retired
- [DuckDuckGo HTML endpoint](https://fshy.ajam.dev/p/duckduckgo.md) [`crawler-scraper/duckduckgo-html`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/duckduckgo-html): dead | no free tier | anonymous | no card | no phone | measured. No key required; no allowance published
- [Google Programmable Search / Custom Search JSON API](https://fshy.ajam.dev/p/google.md) [`crawler-scraper/google-custom-search`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/google-custom-search): dead | no free tier | card | no phone | documented. 100 queries a day for existing customers only
- [Marginalia Search](https://fshy.ajam.dev/p/marginalia-search.md) [`crawler-scraper/marginalia`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/marginalia): dead | no free tier | anonymous | no card | no phone | measured. A free key by email, and a public key with an unpublished shared limit
- [SearXNG public instances](https://fshy.ajam.dev/p/searx.md) [`crawler-scraper/searxng`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/searxng): dead | no free tier | anonymous | no card | no phone | measured. Keyless and anonymous: a public instance takes GET /search?q=...&format=json with no key or account.
- [urlreader.dev](https://fshy.ajam.dev/p/urlreader.md) [`crawler-scraper/urlreader`](https://fshy.ajam.dev/api/v1/record/crawler-scraper/urlreader): dead | no free tier | anonymous | no card | no phone | measured. none: the host does not resolve
