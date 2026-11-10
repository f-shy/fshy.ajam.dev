# Umami

> umami.is | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/umami/ | JSON https://fshy.ajam.dev/api/v1/entity/umami.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Umami

- `dev-services/umami-cloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category web analytics (hosted Umami Cloud) | tier Hobby
- identity a placeholder: card and phone unknown | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://umami.is/pricing
- free tier: Hobby plan at $0 a month: up to 100K events per month, 1 website, 6 months of data retention and community support; API access starts on the Pro plan | unit: requests | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The unit is the event. The vocabulary has no events term, so requests is the nearest. The Pro plan is $20 a month with a 14-day free trial, 1 million events a month, up to 20 websites, 2 years of retention and API and MCP access.
- per-object cap: unverified: no per-event size is stated on the pricing page
- retention: 6 months of data retention on Hobby, against 2 years on Pro and 5 years on Business | source: [1]
- egress: unverified: the pricing table lists data export without showing which plans include it; API access is listed from the Pro plan | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up page at cloud.umami.is answered a login wall to every page reader and its form was not read; the pricing page states no credit card term for Hobby, whose button is Get started where the paid plans say Try 14-day free trial.
- interface: unknown
- limits:
  - volume-quota (binding): up to 100K events per month and 1 website on Hobby [1]
  - retention-clamped: 6 months of data retention on Hobby [1]
- binding note: The 1-website cap is reached first by an account with several sites, and 100K events a month by one busy site.
- interface detail: The pricing page lists API access and MCP access from the Pro plan, so the Hobby plan is reached through the tracking script and the web dashboard; the interface vocabulary has no term for a browser-only service.
- tooling: part of interface detail
- composes with: Event counting for one site on any free host, up to 100K events a month, with 6 months of history.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 6-month retention; what happens past 100K events is unverified: not stated on the pricing page
- evidence note: Plan limits are quoted from the first-party pricing page. No account was opened and the sign-up page could not be read, so the sign-up fields, the card term and the overage behaviour are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Hobby plan costs $0 a month | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: ## Hobby $0/ month
  - [1] 2026-11-01: the Hobby plan has up to 100K events a month, 1 website, 6 months of retention and community support | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: - Up to 100K events per month - 1 website - 6 month data retention - Community support
  - [1] 2026-11-01: Hobby includes 100K events a month, Pro 1 million and Business 10 million | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: | Events (included) | 100K | 1 million | 10 million | Custom |
  - [1] 2026-11-01: retention is 6 months on Hobby, 2 years on Pro and 5 years on Business | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: | Data retention | 6 months | 2 years | 5 years | Custom |
  - [1] 2026-11-01: Hobby has 1 website against up to 20 on Pro | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: | Websites | 1 | Up to 20 | Unlimited | Unlimited |
  - [1] 2026-11-01: API access and MCP access are listed from the Pro plan, which adds to everything in Hobby | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: Everything in Hobby, plus: - 1 million events per month included - $0.00003 per additional event - Up to 20 websites - Up to 10 team members - 2 year data retention - API access - MCP…
  - [1] 2026-11-01: the Pro plan costs $20 a month with a 14-day free trial | capture: sha256:47915a17c2f8c8960e83e46d60f3302724b579c9e412ec13f13233bf1940ea63 | quote: ## Pro $20/ month [Try 14-day free trial]
- sources:
  - [1] https://umami.is/pricing
