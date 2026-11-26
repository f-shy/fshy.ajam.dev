# Newsgroup Ninja

> newsgroup.ninja | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsgroup/ | JSON https://fshy.ajam.dev/api/v1/entity/newsgroup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Newsgroup Ninja

- `debrid/newsgroup-ninja` | paid-only | evidence documented | binding none | category usenet provider (Omicron/Highwinds backbone, retail) | tier Yearly
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:47:09.200Z (live) | stale on 2026-12-26
- url https://www.newsgroup.ninja/en/signup
- price USD 5.83 (yearly)
- free tier: No free tier and no free trial; a 30-day money-back guarantee is the only risk reversal. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 6,676+ days of article retention, in the plan table | days: 6676 | source: [1]
- egress: Unlimited Data, Unlimited Speed, Unlimited Bandwidth, Unmetered Access | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Email, country and credit card are the fields on the signup form; there is no trial, so a card is required before the first byte.
- interface: nntp
- limits:
  - request-rate: 50 connections [1]
  - retention-clamped: 6,676+ days of article retention [1]
- limits note: Monthly $7.99; yearly $5.83/mo at a 55% discount with unlimited VPN included. The monthly plan sells the VPN separately at $4.99.
- binding note: Unlimited volume and speed, 50 connections, no published fair-use cap.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: An alternative front end to the Omicron spool for a client who wants the VPN bundled; it does not add a second feed to another Omicron subscription.
- reliability: Omicron spool served as sslusenet.com (us.sslusenet.com and nl.sslusenet.com) - the same hosts Fastusenet uses. No VPN bundling on the monthly tier.
- evidence note: Prices and limits read from the live signup page, including the visible payment form.
- extras:
  - backbone: Omicron (Highwinds Media), servers us.sslusenet.com / nl.sslusenet.com
- evidence:
  - [1] 2026-10-23: $7.99/mo monthly; $5.83/mo yearly at 55% off; 50 connections; 6,642+ days; payment form asks for credit card, cardholder name
  - [1] 2026-10-23: Account Information block asks for Email Address and Country before payment
  - [1] 2026-11-25: the signup page now states 6,676+ days of retention | capture: sha256:7fa5e66e77d8d6d2651314de7d004bd5f7a8ab3db43fd0d2228206ad32fb9c83 | quote: - 6,676+ Days Article Retention
  - [1] 2026-11-25: the monthly plan is USD 7.99 per month | capture: sha256:7fa5e66e77d8d6d2651314de7d004bd5f7a8ab3db43fd0d2228206ad32fb9c83 | quote: $7.99 /mo
  - [1] 2026-11-25: the yearly plan carries a 55% discount | capture: sha256:7fa5e66e77d8d6d2651314de7d004bd5f7a8ab3db43fd0d2228206ad32fb9c83 | quote: 55% Special Discount
  - [1] 2026-11-25: 50 connections on both plans | capture: sha256:7fa5e66e77d8d6d2651314de7d004bd5f7a8ab3db43fd0d2228206ad32fb9c83 | quote: - 50 Connections
  - [1] 2026-11-25: unlimited data and speed are still published | capture: sha256:7fa5e66e77d8d6d2651314de7d004bd5f7a8ab3db43fd0d2228206ad32fb9c83 | quote: - Unlimited Data
- sources:
  - [1] https://www.newsgroup.ninja/en/signup
