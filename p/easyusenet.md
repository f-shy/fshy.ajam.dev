# EasyUsenet

> easyusenet.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/easyusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/easyusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EasyUsenet

- `debrid/easyusenet` | paid-only | evidence documented | binding request-rate | category usenet provider (EU company) | tier 1 Month Unlimited
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:05:33.300Z (live) | stale on 2026-12-04
- url https://www.easyusenet.nl/
- free tier: No free tier. A 3-day test costs EUR 1.98 and then renews at EUR 5.98 a month unless cancelled; a 14-day money-back guarantee applies to regular plans. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The test is paid, not free: 'Why does the test cost EUR 1.98?'
- per-object cap: source: [2]
- retention: Over 4,000 days (more than eleven years) in every plan | days: 4000 | source: [3]
- egress: Unlimited traffic and full speed on every plan | metered: no | free allowance: unlimited | source: [2]
- identity: card | detail: The test order asks for 'E-mail, country, payment method'; payment is by SEPA direct debit, credit card, cryptocurrencies or iDEAL/Wero, so a card is not the only route. Fields of the regular checkout were not read: unverified: behind a sign-up.
- interface: nntp
- limits:
  - request-rate (binding): 100 connections on every plan [2]
  - retention-clamped: 4,000+ days of retention [2]
- limits note: Monthly EUR 5.98, yearly EUR 3.98 a month, prepaid EUR 6.98 a month or EUR 4.98 a month for a year; the vendor says the price stays for life.
- binding note: Traffic and speed are unlimited, so the 100-connection ceiling is the only technical bound the vendor states.
- interface detail: NNTP over TLS/SSL; the vendor says a newsreader such as SABnzbd or NZBGet is needed
- composes with: Two plans only (monthly and yearly) with the same 100 connections; the yearly price is the cheapest unlimited plan of this vendor and works as a primary behind which a block account on another backbone fills gaps.
- reliability: The backbone is not stated on the vendor pages read; completion is unmeasured.
- notes: Unlimited traffic, so the price is per month, not per terabyte.
- evidence note: Prices, connections, retention and test terms are from the vendor pages read on 2026-11-03.
- extras:
  - payment_methods: SEPA direct debit, credit card, cryptocurrencies, iDEAL/Wero
- evidence:
  - [2] 2026-11-03: the yearly unlimited plan is EUR 3.98 a month, the cheapest paid tier | capture: sha256:2f8be72e967ad8c0dc6278f42fc4f720e703161c134f8ba4eea3f682b00be21b | quote: 3.98€/month−33%
  - [2] 2026-11-03: the monthly unlimited plan is EUR 5.98 a month | capture: sha256:2f8be72e967ad8c0dc6278f42fc4f720e703161c134f8ba4eea3f682b00be21b | quote: 5.98€/month
  - [3] 2026-11-03: retention is 4,000+ days | capture: sha256:1616e43aa5a2a82423b79a5ad3c751ce3fa0534a986e0b703f0b2aab83911d45 | quote: Over 4,000 days – that is more than eleven years.
  - [1] 2026-11-03: the 3-day test converts to the monthly plan unless cancelled | capture: sha256:edaf67e9f9aa2f0f9ae23c72b94739853ebe8ed52f8156eda876991ff1cba0b3 | quote: After three days the access continues at €5.98/month – or you cancel beforehand with one click.
  - [1] 2026-11-03: the test order asks for e-mail, country and a payment method | capture: sha256:edaf67e9f9aa2f0f9ae23c72b94739853ebe8ed52f8156eda876991ff1cba0b3 | quote: E-mail, country, payment method – that is it.
  - [3] 2026-11-03: payment routes include SEPA, card, crypto and iDEAL/Wero | capture: sha256:1616e43aa5a2a82423b79a5ad3c751ce3fa0534a986e0b703f0b2aab83911d45 | quote: Payment is by SEPA direct debit, credit card, various cryptocurrencies or iDEAL/Wero.
  - [1] 2026-11-03: the test order asks for e-mail, country and a payment method, so a payment is part of every route in; there is no free path | capture: sha256:edaf67e9f9aa2f0f9ae23c72b94739853ebe8ed52f8156eda876991ff1cba0b3 | quote: E-mail, country, payment method – that is it.
  - [2] 2026-11-03: the monthly unlimited plan is paid at EUR 5.98 a month | capture: sha256:2f8be72e967ad8c0dc6278f42fc4f720e703161c134f8ba4eea3f682b00be21b | quote: 5.98€/month
- sources:
  - [1] https://www.easyusenet.nl/3day.html
  - [2] https://www.easyusenet.nl/plans.html
  - [3] https://www.easyusenet.nl/index.html?den=usd
