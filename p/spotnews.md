# Spotnews

> spotnews.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spotnews/ | JSON https://fshy.ajam.dev/api/v1/entity/spotnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spotnews

- `debrid/spotnews` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, unlimited plans and non-expiring blocks) | tier Premium 10 Mbit/s
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://spotnews.nl/
- free tier: No free tier and no trial on the plans page read; the cheapest plan is EUR 4.49 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: about 4000 days of retention ('Retentie: ± 4000 dagen') | days: 4000 | source: [1]
- egress: Unlimited data on three plans of 10 Mbit/s, 50 Mbit/s and unlimited speed; non-expiring block quotas on a separate page | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the page offers an automatic-renewal or one-time payment choice and the payment form was not opened, so its fields are behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): 10 Mbit/s and 50 Mbit/s tiers, plus an unlimited-speed tier [1]
  - request-rate: 10 connections on the 10 Mbit/s plan, 50 on the 50 Mbit/s plan [1]
  - retention-clamped: about 4000 days [1]
- limits note: 10 Mbit/s EUR 4.49 a month (EUR 40.95 a year); 50 Mbit/s EUR 7.55 a month (EUR 72.50 a year); unlimited speed EUR 8.35 a month (EUR 79.99 a year). Yearly prices are shown as a monthly equivalent of EUR 3.41, EUR 6.04 and EUR 6.67.
- binding note: Data is unlimited; the speed tier and its connection count bound a month.
- interface detail: NNTP with encryption included
- composes with: Block quotas from 150 GB to 1,100 GB that do not expire are listed on a separate page (third-party index); the plans are speed-tiered.
- reliability: A third-party index lists the Abavia backbone; the vendor page read does not state one.
- notes: Priced per month and speed tier; block prices were not read.
- evidence note: Prices, retention and connections are from the vendor plans page read on 2026-11-03; the page is in Dutch.
- evidence:
  - [1] 2026-11-03: the cheapest plan is EUR 4.49 a month | capture: sha256:5bdff7faacbdfb369af3873ba64091cceef66eaeb73f654d91706ec8fec2b5bf | quote: € 4,49/maand
  - [1] 2026-11-03: retention is about 4000 days | capture: sha256:5bdff7faacbdfb369af3873ba64091cceef66eaeb73f654d91706ec8fec2b5bf | quote: - Retentie: ± 4000 dagen
  - [1] 2026-11-03: 10 connections on the cheapest plan | capture: sha256:5bdff7faacbdfb369af3873ba64091cceef66eaeb73f654d91706ec8fec2b5bf | quote: - 10 verbindingen
  - [1] 2026-11-03: data is unlimited | capture: sha256:5bdff7faacbdfb369af3873ba64091cceef66eaeb73f654d91706ec8fec2b5bf | quote: - Onbeperkte data
  - [2] 2026-11-03: a third-party index lists blocks of 150 GB to 1,100 GB and the Abavia backbone | capture: sha256:b7e69be3b79712a5f5875f68db3e51c281a266031e0a8d6b232e379d5b76d1d8 | quote: Spotnews is a Dutch Usenet provider with servers in the EU and retention of over eleven years. Alongside three subscription tiers with unlimited volume — from 10 Mbit/s up to unrestricted speed — there are non-expiring block quotas from 150 GB to 1,100 GB. All plans offer up to 50 connections, Abavia backbone.
- sources:
  - [1] https://spotnews.nl/premium-plannen
  - [2] https://www.usenet.org/providers/spotnews
