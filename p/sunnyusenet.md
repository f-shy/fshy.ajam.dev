# Sunny Usenet

> sunnyusenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sunnyusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/sunnyusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sunny Usenet

- `debrid/sunny-usenet` | trial-only | evidence documented | binding none | category usenet provider (Omicron/Highwinds backbone, EU retail) | tier Sunny UNL
- identity a placeholder: card and phone unknown | verified 2026-11-25T09:47:09.199Z (live) | stale on 2026-12-26
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
- limits note: UNL: 1 week free, 1 month EUR 7.79 on the signup form. Account sharing with family and friends is allowed. Payment methods per the vendor KB: credit cards, PayPal, SEPA Direct Debit, iDEAL, PaySafe Card and Bitcoin.
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
  - [1] 2026-11-25: the free trial is one week | capture: sha256:a9a3e8fd5f07e83cd1ed07c8ab23680e2eb5377f2f64940a4d99d55b98bac8f4 | quote: Every package can be tested with a one-week free trial period
  - [1] 2026-11-25: unlimited downloads on UNL | capture: sha256:a9a3e8fd5f07e83cd1ed07c8ab23680e2eb5377f2f64940a4d99d55b98bac8f4 | quote: No data transfer limit
  - [1] 2026-11-25: retention is 4100 days | capture: sha256:a9a3e8fd5f07e83cd1ed07c8ab23680e2eb5377f2f64940a4d99d55b98bac8f4 | quote: - 4100 days retention
  - [1] 2026-11-25:  | capture: sha256:a9a3e8fd5f07e83cd1ed07c8ab23680e2eb5377f2f64940a4d99d55b98bac8f4 | quote: - Share your account with family and friends
  - [3] 2026-11-25: the signup form now lists Sunny UNL at EUR 7.79 for one month | capture: sha256:264200f231e2e21e71970e2c3168c2ebb6be5e34c5e321fcf0c205333f6cc678 | quote: €7,79/mo
  - [2] 2026-11-25: the vendor accepts six named payment methods | capture: sha256:9c98ba3a4296ad539a9eae3e43554af148e7a32ac38d71ed893193bb2d53bf14 | quote: We accept credit cards, PayPal, SEPA Direct Debit, iDEAL, PaySafe Card, and Bitcoin.
- sources:
  - [1] https://www.sunnyusenet.com/en/packages/sunny-unl
  - [2] https://support.sunnyusenet.com/kb/article/930-what-payment-methods-can-i-use/
  - [3] https://www.sunnyusenet.com/en/signup/form?package=SunnyUNLAnnualRecurringWithTrial
