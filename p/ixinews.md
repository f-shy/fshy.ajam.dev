# Ixinews

> ixinews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ixinews/ | JSON https://fshy.ajam.dev/api/v1/entity/ixinews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ixinews

- `debrid/ixinews` | paid-only | evidence documented | binding volume-quota | category usenet provider (French-language, volume plans and paid trials) | tier IXI3
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.ixinews.com/
- price USD 249.99 for 1000 GB on the one-year plan (USD 0.25 per GB as the page states it)
- free tier: No free tier. Paid test offers, limited to one per customer: 5 GB for 5 days at USD 0.99 and 10 GB for 10 days at USD 1.99. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The test offers are priced, so they are not free.
- per-object cap: source: [1]
- retention: More than 1500 days of binary retention | days: 1500 | source: [1]
- egress: Metered on seven monthly volume plans from 3 GB; an unlimited plan exists | metered: yes | free allowance: none | source: [1]
- identity: card | detail: The monthly plans say 'Renouvellement automatique via PayPal'. The signup form was not opened, so any further fields are unverified: behind a sign-up.
- interface: nntp
- limits:
  - volume-quota (binding): monthly plans 3 GB to 75 GB, an unlimited plan, and one-year volume plans of 50 GB to 1000 GB [1]
  - request-rate: up to 30 simultaneous connections [1]
  - retention-clamped: 1500 days of binary retention [1]
- limits note: Monthly: IXI3 3 GB USD 2.99, IXI5 5 GB USD 3.99, IXI10 10 GB USD 5.99, IXI25 25 GB USD 9.99, IXI50 50 GB USD 14.99, IXI75 75 GB USD 19.99, IXIFULL unlimited USD 24.99. The page quotes prices in US dollars as the billed amount.
- binding note: All but the IXIFULL plan are bounded by a fixed volume.
- interface detail: NNTP with 256-bit SSL on ports 563, 80, 81, 465 and 993
- composes with: Cheap entry for a small volume (3 GB for USD 2.99 a month); the per-GB price falls as the plan grows, and a 1000 GB yearly volume plan is the bulk route.
- reliability: Backbone is not stated on the page read; completion is unmeasured.
- notes: Volume-metered; the one-year volume plans are USD 29.99 for 50 GB up to USD 249.99 for 1000 GB.
- evidence note: Prices, volumes, retention and connections are from the vendor plan page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the smallest monthly plan is 3 GB at USD 2.99 | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: | IXI3 | 3 Go | 2,99 $ | *(1,00 $)* | [>](https://www.ixinews.com/abonnement.html?plan=IXI3) |
  - [1] 2026-11-03: the unlimited monthly plan is USD 24.99 | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: | IXIFULL | Ilimité | 24,99 $ | *(Ilimité)* | [>](https://www.ixinews.com/abonnement.html?plan=IXIFULL) |
  - [1] 2026-11-03: the test offer is 5 GB for 5 days at USD 0.99 | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: | IXITEST5 | 5 Go (5 jours) | 0,99 $ | *(0,20 $)* | [>](https://www.ixinews.com/abonnement.html?plan=IXITEST5) |
  - [1] 2026-11-03: binary retention is more than 1500 days | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: - Plus de 1500 jours [1] de rétention binaire
  - [1] 2026-11-03: 30 simultaneous connections | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: - Jusqu'à 30 connexions simultanées
  - [1] 2026-11-03: the test offers are limited to one per customer | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: | Offres de test .: Limité à un par client :. | | | | |
  - [1] 2026-11-03: the 1000 GB one-year volume plan is USD 249.99, USD 0.25 per GB | capture: sha256:76f8624d53a1ae543fc7ceae8e166aaa8ac00415bf8a6191c794041528bbbf40 | quote: | IXI1000Go | 1000 Go | 249,99 $ | *(0,25 $)* | [>](https://www.ixinews.com/abonnement.html?plan=IXI1000Go) |
- sources:
  - [1] https://www.ixinews.com/abonnement-newsgroups.html
