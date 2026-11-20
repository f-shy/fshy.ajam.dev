# NewsXS

> newsxs.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsxs/ | JSON https://fshy.ajam.dev/api/v1/entity/newsxs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NewsXS

- `debrid/newsxs` | trial-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, unlimited flats and block accounts) | tier 10Mbit
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:25:55.356Z (live) | stale on 2026-12-04
- url https://www.newsxs.nl/
- free tier: A 14-day trial period ('14 dagen proefperiode') is stated on the home page; its data allowance and whether it is charged are not stated on the page read. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The trial allowance is unverified: behind a sign-up.
- per-object cap: source: [1]
- retention: 2625+ days of retention ('2625+ dagen retentie') | days: 2625 | source: [1]
- egress: Unlimited use on the four flat plans (10 Mbit, 24 Mbit, 100 Mbit and unlimited speed); block accounts sold separately | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: The trial account is delivered by e-mail and is limited to residents of the Netherlands whose ISP peers with NL-IX, AMS-IX or private peers; one trial per address, no proxies or tunnels. After 14 days it converts to a paid account, paid by direct debit, iDEAL or PayPal; no card is named as a requirement. The trial form fields were not opened: unverified: behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): speed tiers 10 Mbit, 24 Mbit, 100 Mbit and unlimited speed [1]
  - request-rate: up to 50 connections; 10 on the 10 Mbit plan [1]
  - retention-clamped: 2625+ days of retention [1]
- limits note: Flats from EUR 4.50 (10 Mbit), EUR 5.50 (24 Mbit), EUR 7.50 (100 Mbit) and EUR 9.50 (unlimited speed); blocks from EUR 2.95. The home page does not say whether the prices are monthly.
- binding note: Volume is unlimited on the flats; the speed tier and its connection count bound a month.
- interface detail: NNTP with free SSL and IPv6 support
- composes with: Block accounts start from EUR 2.95 at unlimited speed with 50 connections and are the cheaper fill; the flats are speed-tiered.
- reliability: Backbone is not stated on the vendor page read.
- notes: Verdict rests on the advertised 14-day trial; its cost is unverified.
- evidence note: Prices, retention and the trial line are from the vendor home page read on 2026-11-03; the page is in Dutch.
- evidence:
  - [1] 2026-11-03: a 14-day trial period is advertised | capture: sha256:4718ea0b8e028eb71112eedef34dc25fe968a204e4d14079f8ad983e9ef629e5 | quote: #### **14 dagen **proefperiode
  - [1] 2026-11-03: the cheapest flat, 10 Mbit, starts at EUR 4.50 | capture: sha256:4718ea0b8e028eb71112eedef34dc25fe968a204e4d14079f8ad983e9ef629e5 | quote: € 4.50
  - [1] 2026-11-03: retention is 2625+ days | capture: sha256:4718ea0b8e028eb71112eedef34dc25fe968a204e4d14079f8ad983e9ef629e5 | quote: - 2625+ dagen retentie
  - [1] 2026-11-03: up to 50 connections | capture: sha256:4718ea0b8e028eb71112eedef34dc25fe968a204e4d14079f8ad983e9ef629e5 | quote: - Tot wel 50 connecties
  - [2] 2026-11-03: the trial account is delivered to the user by e-mail; no card is named as a sign-up requirement | capture: sha256:d70a26683bf45dddc3ff4c90cee1bc09cb0972373bfe4981770a0b88e943d0ab | quote: per e-mail, aan de gebruiker ter beschikking gesteld.
  - [2] 2026-11-03: the trial is limited to people resident in the Netherlands | capture: sha256:d70a26683bf45dddc3ff4c90cee1bc09cb0972373bfe4981770a0b88e943d0ab | quote: 3.4 De gratis proefperiode kan niet geactiveerd worden door iemand die buiten Nederland verblijft.
  - [2] 2026-11-03: payment after the trial is by direct debit (bank details), iDEAL or PayPal, not only a card | capture: sha256:d70a26683bf45dddc3ff4c90cee1bc09cb0972373bfe4981770a0b88e943d0ab | quote: In geval van betaling per automatische incasso wordt deze pas uitgevoerd nadat uw bankgegevens
- sources:
  - [1] https://www.newsxs.nl/
  - [2] https://www.newsxs.nl/NewsXS-usenet-provider/Proef-periode.html
