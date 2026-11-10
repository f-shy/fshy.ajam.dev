# Sunny Usenet

> sunnyusenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sunnyusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/sunnyusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sunny Usenet

- `debrid/sunny-usenet` | trial-only | evidence documented | binding none | category usenet provider (Omicron/Highwinds backbone, EU retail) | tier Sunny UNL
- identity a placeholder: card and phone unknown | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.sunnyusenet.com/en/packages/sunny-unl
- price EUR 6.23 (Sunny UNL, 12-month term)
- free tier: '1 Week' is listed as Free in the package price table, and the page says 'Every package can be tested with a one-week free trial period ... without any obligation to pay or order'. | unit: unlimited | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 4100 days retention, in the package feature list | days: 4100 | source: [1]
- egress: No data transfer limit; unlimited speed on UNL | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: The free week is delivered through a signup product named 'SunnyUNLAnnualRecurringWithTrial', which is an annual recurring subscription with a trial attached, so a payment method is captured at signup even though the first week is free. That is inferred from the product id, not observed at checkout.
- interface: nntp
- limits:
  - request-rate: 40 connections [1]
  - per-ip-shaping: Unlimited Mbps on UNL; Sunny 20 and Sunny 60 cap at 20 and 60 Mbit [1]
  - retention-clamped: 4100 days retention [1]
- limits note: UNL: 1 week free, 1 month EUR 14.78, 3 months EUR 7.40/mo, 6 months EUR 7.01/mo, 12 months EUR 6.23/mo. Account sharing with family and friends is allowed. Payment methods per the vendor KB: credit cards, PayPal, SEPA Direct Debit, iDEAL, PaySafe Card and Bitcoin.
- binding note: Unlimited volume and unlimited speed. At 1 TiB/month nothing in the vocabulary binds.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Stacks as a quota-free secondary on the Omicron spool where account sharing is wanted; as a primary it is the same spool as Newshosting at a higher monthly price.
- reliability: Omicron spool. Account sharing is explicitly permitted, which is unusual and is the main reason this storefront exists next to the others.
- notes: Bitcoin is accepted, which matters where a card is the constraint, but the trial itself still runs through the annual recurring product.
- evidence note: Prices, retention, connections and sharing terms are on the package page read. The card requirement for the trial is inferred from the product id and the recurring billing model.
- extras:
  - backbone: Omicron (Highwinds Media), AS33438
  - payment_methods: card, PayPal, SEPA, iDEAL, PaySafe Card, Bitcoin
- evidence:
  - [1] 2026-10-23: '1 Week Free'; EUR 14.78 1 month, EUR 6.23 12 months; 40 connections; 4100 days; 'Share your account with family and friends'
  - [2] 2026-10-23: credit cards, PayPal, SEPA Direct Debit, iDEAL, PaySafe Card and Bitcoin
- sources:
  - [1] https://www.sunnyusenet.com/en/packages/sunny-unl
  - [2] https://support.sunnyusenet.com/kb/article/930-what-payment-methods-can-i-use/
