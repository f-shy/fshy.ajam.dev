# ExtremeUsenet

> extremeusenet.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/extremeusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/extremeusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExtremeUsenet

- `debrid/extremeusenet` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, speed-tiered flats) | tier 4 mbit flat
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.extremeusenet.nl/
- free tier: No free tier and no trial on the price page read; plans are priced by maximum speed, from EUR 4 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the price page read does not state retention | source: [1]
- egress: Plans are tiered by maximum speed (4 to 300 mbit); the price table states no download cap | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the order form was not opened, so the fields it asks for are behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): speed tiers from 4 mbit to 120 mbit on the first table [1]
  - request-rate: 4 connections on the 4 and 8 mbit plans, up to 20 on the 120 mbit plan [1]
- limits note: First table, per month: 4 mbit EUR 4, 8 mbit EUR 5, 12 mbit EUR 6, 20 mbit EUR 6.50, 30 mbit EUR 7, 60 mbit EUR 8, 120 mbit EUR 10. A second table with 12 to 60 mbit plans lists EUR 2.50 to EUR 6 a month.
- binding note: Volume is not metered; the maximum speed of the tier decides what a month retrieves.
- interface detail: NNTP; connection counts are tiered by plan
- composes with: The cheapest tier is speed-capped at 4 mbit, so it suits slow background fill; a faster tier costs more per month and the night-time plans cost less.
- reliability: Retention and backbone are not stated on the price page read; the figure on a third-party index is not used here.
- notes: Priced per month and speed tier, not per terabyte.
- evidence note: Prices, speed tiers and connection counts are from the vendor price page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: monthly prices of the seven speed tiers, from EUR 4 | capture: sha256:01389bee55c9cb643eef5b5c6b8f707bd0ee9b81f5d83461374a6ee570d3ae31 | quote: | Price per month: | € 4,- | € 5,- | € 6,- | € 6,50 | € 7,- | € 8,- | € 10,- |
  - [1] 2026-11-03: connections per tier, 4 on the cheapest | capture: sha256:01389bee55c9cb643eef5b5c6b8f707bd0ee9b81f5d83461374a6ee570d3ae31 | quote: | Connections: | 4 | 4 | 8 | 12 | 12 | 12 | 20 |
  - [1] 2026-11-03: monthly prices of the second table of 12 to 60 mbit plans | capture: sha256:01389bee55c9cb643eef5b5c6b8f707bd0ee9b81f5d83461374a6ee570d3ae31 | quote: | Price per month: | € 2,50 | € 4,50 | € 5,- | € 6,- | |
- sources:
  - [1] https://www.extremeusenet.nl/en/cheap_usenet/
