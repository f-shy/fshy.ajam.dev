# AnonyNews

> anonynews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonynews/ | JSON https://fshy.ajam.dev/api/v1/entity/anonynews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnonyNews

- `debrid/anonynews` | paid-only | evidence documented | binding request-rate | category usenet provider (unlimited flat, three billing cycles) | tier 1 Month
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://anonynews.com/
- free tier: No free tier and no trial on the plan page read; three paid cycles only. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: 6570+ days of retention on every plan | days: 6570 | source: [1]
- egress: Unlimited Usenet downloads on every plan | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the checkout was not opened, so the fields it asks for are behind a sign-up; a paid order is required before any access because no trial is offered.
- interface: nntp
- limits:
  - request-rate (binding): up to 60 simultaneous connections [1]
  - retention-clamped: 6570+ days of retention [1]
- limits note: USD 14.99 a month, USD 39.99 per 3 months, USD 139.99 per year.
- binding note: Volume is unlimited, so the 60-connection ceiling is the only technical bound stated.
- interface detail: NNTP over SSL; the vendor page says to connect with your own newsreader
- composes with: A single flat plan in three cycles; useful as a deep-retention primary, with a block account on a different backbone as fill.
- reliability: The vendor says it keeps no history of downloaded articles; backbone is not stated on the page read.
- notes: Unlimited volume, priced per month.
- evidence note: Prices, connections and retention are from the vendor plan page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the 1-month plan is USD 14.99 | capture: sha256:5b0bc097e74bdaf0de63a85b5496be41ff7652de3b5592981e2fb66a3e6013ec | quote: $14.99/month
  - [1] 2026-11-03: the 12-month plan is USD 139.99 | capture: sha256:5b0bc097e74bdaf0de63a85b5496be41ff7652de3b5592981e2fb66a3e6013ec | quote: $139.99/year
  - [1] 2026-11-03: retention is 6570+ days | capture: sha256:5b0bc097e74bdaf0de63a85b5496be41ff7652de3b5592981e2fb66a3e6013ec | quote: 6570+ days of retention
  - [1] 2026-11-03: 60 connections per account | capture: sha256:5b0bc097e74bdaf0de63a85b5496be41ff7652de3b5592981e2fb66a3e6013ec | quote: Up to 60 simultaneous connections
- sources:
  - [1] https://anonynews.com/
