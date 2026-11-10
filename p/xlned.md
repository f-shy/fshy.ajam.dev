# XLned

> xlned.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xlned/ | JSON https://fshy.ajam.dev/api/v1/entity/xlned.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XLned

- `debrid/xlned` | paid-only | evidence documented | binding per-ip-shaping | category Usenet provider (Netherlands) - no current trial | tier XL Small
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://www.xlned.com/en/order/xl-small
- free tier: None today. The order page starts at "€ 4.99" for one month of XL Small and offers no trial line; the company's own about page describes free trial accounts only as history: "XLned is in 2007 begonnen met het aanbieden van gratis proefaccounts. Met deze accounts konden bezoekers van onze website ruim vier maanden lang onbeperkt gebruik maken van onze diensten." (XLned began in 2007 offering free trial accounts, usable without limit for more than four months.) | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The about page is the reason this provider keeps appearing in trial lists: the offer existed and ended. Recording it as a current trial would be false.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "4100 days" in the XL Small order table. | days: 4100 | source: [1]
- egress: No byte counter is shown on the order page; the plan is defined by speed (5 Mbit) and connections (2). No traffic price is published. | metered: no | free allowance: none | source: [1]
- identity: card | detail: The order flow is four steps: "enter your personal data, check your order and select a payment method", then credentials arrive by email within 1 hour to 5 days. A payment method is part of the order.
- interface: unknown
- limits:
  - per-ip-shaping (binding): 5 Mbit on XL Small, 2 connections [1]
  - retention-clamped: 4100 days [1]
- binding note: At 5 Mbit the line carries about 1.6 TB/month, so the speed is only 1.6x the 1 TiB monthly volume and is the first thing to fail for a user trying to move more. No byte counter appears on the order page.
- interface detail: NNTP; the order page names speed, connections and retention, not the protocol port. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: 5 Mbit is about 1.6 TB/month of ceiling, which is just above the 1 TiB monthly volume; it is a cheap slow pipe rather than a free step.
- reliability: Account credentials arrive after payment clears, between 1 hour and 5 days depending on the method - a delay, not a suspension.
- notes: Repeatability: not applicable today; the historical free accounts were tied to a 2007 launch and no rule survives on the current site. Abandonment: if a trial line appears on the order page, add a tier.
- evidence note: The current price table and the absence of a trial line are quoted from the order page today; the historical free-account sentence is quoted from the Dutch about page and is labelled as history.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no current trial
  - historical_trial: 2007, more than four months, unlimited, per the Dutch about page
- evidence:
  - [1] 2026-10-23: XL Small: 5 Mbit, 2 connections, 4100 days, "€ 4.99" for 1 month; four-step order with no trial option
  - [2] 2026-10-23: "XLned is in 2007 begonnen met het aanbieden van gratis proefaccounts ... ruim vier maanden lang onbeperkt" - the free trial is historical, not current
- sources:
  - [1] https://www.xlned.com/en/order/xl-small
  - [2] https://www.xlned.com/nl/about-us
