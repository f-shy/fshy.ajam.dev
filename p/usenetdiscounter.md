# Usenetdiscounter

> usenetdiscounter.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetdiscounter/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetdiscounter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Usenetdiscounter

- `debrid/usenetdiscounter` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, flat-fee and night-fee plans) | tier 5 NIGHTFEE
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T15:05:38.914Z (live) | stale on 2026-12-04
- url https://www.usenetdiscounter.com/
- free tier: No free tier on the night plan this record covers. The checkout lists a separate package named 25GB TRIALFEE (150 Mbit, 30 connections, SSL) with the price Free; its limits beyond the name are unverified: behind a sign-up. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The try-out terms are unverified: behind a sign-up.
- per-object cap: source: [2]
- retention: 1200 days of retention on the plans listed | days: 1200 | source: [2]
- egress: Unlimited download volume in several speed tiers up to 1 Gbit/s; night plans are limited to 00:00 to 12:00 CET | metered: no | free allowance: unlimited | source: [2]
- identity: card | detail: The paid checkout creates an account with email, password, name, surname and country, then asks for a payment provider (Mollie) and a payment method; the methods it offers are not shown before a sign-up, so whether a card is required is unverified: behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): flat plans 20, 100, 250, 500 and 1000 Mbit; night plans 5, 20, 100, 250 and 1000 Mbit [2]
  - request-rate: 10 connections on the 20 Mbit plan, up to 70 on the 1000 Mbit plan [2]
  - retention-clamped: 1200 days [2]
- limits note: Flat fee per month: 20 Mbit EUR 2.80, 100 Mbit EUR 5.40, 250 Mbit EUR 4.50, 500 Mbit EUR 12.30, 1000 Mbit EUR 5.50. Night fee per month: 5 Mbit EUR 1.00, 20 Mbit EUR 1.65, 100 Mbit EUR 1.75, 250 Mbit EUR 2.00, 1000 Mbit EUR 2.25. The page's prices are not monotonic in speed.
- binding note: Volume is unlimited, so the speed tier and the night window bound a month.
- interface detail: NNTP with free 256-bit SSL
- composes with: The night plans cost from EUR 1.00 a month and only download between 00:00 and 12:00 CET, which suits scheduled bulk retrieval.
- reliability: Backbone is not stated on the page read; a third-party index lists Abavia.
- notes: Priced per month and speed tier; the night window is 00:00 to 12:00 CET per a third-party index.
- evidence note: Prices, retention and connections are from the vendor plans page read on 2026-11-03.
- evidence:
  - [2] 2026-11-03: the 20 Mbit flat fee is EUR 2.80 a month | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: € 2,80 p.m.
  - [2] 2026-11-03: a 5 Mbit night plan exists | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: ### 5 NIGHTFEE
  - [2] 2026-11-03: the 5 Mbit night plan is EUR 1.00 a month | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: € 1,00 p.m.
  - [3] 2026-11-03: a third-party index gives the night window as 00:00 to 12:00 CET | capture: sha256:3703ffed3a9f3b9894fd55ae0699d5cb2713a16bbdff10cd136bd5a45453f086 | quote: Usenetdiscounter is a Dutch Usenet provider with two parallel plan models: Flatfee for unrestricted round-the-clock access, and Nightfee for downloading between 00:00 and 12:00 CET at a considerably lower price.
  - [2] 2026-11-03: retention is 1200 days | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: * Retention 1200 days
  - [2] 2026-11-03: 10 connections on the 20 Mbit plan | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: 20 Mbit 10 Connections
  - [4] 2026-11-03: the paid checkout step asks for a payment provider and a payment method | capture: sha256:32fe5f2e458bf01391b80270e52b82eb65a6ce00b5dc8be47e49933ac273a4cf | quote: Select your payment provider
  - [4] 2026-11-03: the checkout asks for account credentials before payment | capture: sha256:32fe5f2e458bf01391b80270e52b82eb65a6ce00b5dc8be47e49933ac273a4cf | quote: Choose your desired username and password to log in to our services.
  - [5] 2026-11-03: a package named 25GB TRIALFEE at 150 Mbit and 30 connections is listed as Free | capture: sha256:0ecae25975d00ec31b1816b7d76339bd4c9e5c9863e520b32659b7aa4bf9b642 | quote: 25GB TRIALFEE 150MBit \| 30 connections \| SSL Free
  - [2] 2026-11-03: the 5 NIGHTFEE plan this record covers is a paid plan at EUR 1.00 a month | capture: sha256:c811903bb7fb7645d3d1b0d30ad6ded4b1b8ebc45ee0908a71d964657ea680f2 | quote: € 1,00 p.m.
- sources:
  - [1] https://www.usenetdiscounter.com/
  - [2] https://www.usenetdiscounter.com/cheap-usenet-plans/
  - [3] https://www.usenet.org/providers/usenetdiscounter
  - [4] https://www.usenetdiscounter.com/checkout?product_variation=14&locale=en
  - [5] https://www.usenetdiscounter.com/checkout?product_variation=6&locale=en
