# Easynews

> easynews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/easynews/ | JSON https://fshy.ajam.dev/api/v1/entity/easynews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Easynews

- `debrid/easynews` | paid-only | evidence documented | binding volume-quota | category Usenet provider with web-to-Usenet interface (United States) - no free trial | tier Big Gig
- needs card yes, phone no, ID no, institution no | verified 2026-10-30T13:11:55.967Z (live) | stale on 2026-11-30
- url https://www.easynews.com/usenet-plans/
- free tier: None. The vendor's own help centre says: "Easynews does not offer a traditional free trial. Instead, it provides a 30-day money back guarantee on all new plans." The plans page sells "30-Day Money-Back Guarantee" as the risk-free route. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Affiliate pages advertise "14 days or 10 GB of data from Easynews"; the vendor's own knowledge base denies a free trial. The vendor page is the evidence and the affiliate claim is false.
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [2]
- retention: "6432+ Days Article Retention" on the Big Gig row; a checkout page read the same day said "6643+ Days". The conservative figure is kept. | days: 6432 | source: [2] | note: Two vendor surfaces give different day counts on the same day; the smaller is recorded.
- egress: Metered by monthly data allowance on the Big Gig plan (150 GB/month); the unlimited-data plan is priced separately. No per-TB overage price is published on the page read. | metered: yes | free allowance: none | source: [2]
- identity: card | detail: Every plan is a paid subscription; the 30-day guarantee is a refund against a charge, not a free tier. The checkout asks for an email address and one of three payment methods: a credit card (first name, last name, zip code, country and card number), PayPal, or cryptocurrency (BTC and other coins); a cryptocurrency purchase is not refundable. The form has no phone field.
- interface: rest, unknown
- limits:
  - volume-quota (binding): 150 GB/month on Big Gig; unlimited on the unlimited plan [2]
  - retention-clamped: 6432+ days on Big Gig [2]
- binding note: 150 GB/month on the entry plan is 15% of 1 TiB of monthly transfer; the unlimited plan removes the counter but requires the $9.99 monthly relationship. A card is required either way.
- interface detail: Web-to-Usenet browser interface plus NNTP (200+ days on the mail-in Classic, 6432+ days on Big Gig, 60 connections). The web interface is the distinguishing feature; the schema has no nntp token, so the second token is unknown.
- tooling: browser (no client needed); NNTP clients also work
- composes with: Not a free step. It is the fallback when a Usenet indexer returns an article wanted in a browser: pay $9.99 for month one and use the 30-day refund as the trial, which still means a card.
- reliability: The refund requires a request inside 30 days; the vendor KB documents the policy. No suspension report was read.
- notes: Repeatability: not applicable, because there is no free trial to repeat. Abandonment: if a free trial appears in the help centre, this becomes a trial record. PayPal is listed, but PayPal guest checkout still requires a funding card, and Easynews presents PayPal as a subscription authorisation rather than a one-off, so it is not a cardless route.
- evidence note: Both the absence of a trial and the plan numbers are quoted from vendor pages read. The vendor's own KB contradicts the affiliate claim of a 10 GB trial.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
  - affiliate_claim_refuted: "Click here for 14 days or 10 GB of data from Easynews" (shareconnector.net) against the vendor KB's "does not offer a traditional free trial"
  - payment_group: card
  - payment.card: yes
  - payment.paypal: yes
  - payment.voucher: no
  - payment.entry_price: not read
- evidence:
  - [1] 2026-10-23: "Easynews does not offer a traditional free trial. Instead, it provides a 30-day money back guarantee on all new plans."
  - [2] 2026-10-23: "30-Day Money-Back Guarantee", "Big Gig Plan" at "$29.94 / $9.99 /mo First 3 Months", "150 GB/Month Data", "6432+ Days Article Retention", "60 Connections"
  - [3] 2026-10-23: "6643 days of article retention" in the body - the higher of two vendor figures for the same day
  - [4] 2026-10-23: 'Easynews accepts Visa, Mastercard, Discover, and American Express' and 'PayPal: Subscriptions can be managed through PayPal', plus the region caveat
  - [5] 2026-10-23: 
  - [5] 2026-10-30: the unlimited-plan checkout asks for an email address and offers three payment methods, Credit Card, PayPal and Cryptocurrency; a cryptocurrency purchase is not refundable | capture: sha256:da40ce6da9b01755e141daa24d07c0530119ab2af2f79bd2956417536803fcbc | quote: Purchases with cryptocurrency are not eligible for refund.
  - [5] 2026-10-30: the checkout form's account field is an email address; the card option asks for first name, last name, zip code, country and card number, and the form has no phone field | capture: sha256:da40ce6da9b01755e141daa24d07c0530119ab2af2f79bd2956417536803fcbc | quote: placeholder="Your Email Address"
- sources:
  - [1] https://help.easynews.com/kb/article/1589-no-free-trial-refund-available-in-30-days/
  - [2] https://www.easynews.com/usenet-plans/
  - [3] https://www.easynews.com/
  - [4] https://help.easynews.com/kb/article/44-payment-methods/
  - [5] https://signup.easynews.com/checkout/unlimited-special-deal/
