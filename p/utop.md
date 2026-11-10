# UTop.me

> utop.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/utop/ | JSON https://fshy.ajam.dev/api/v1/entity/utop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UTop.me

- `debrid/utop-me` | qualifies | evidence documented | binding none | category voucher reseller (payment rail) | tier reseller
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:30:43.000Z (live) | stale on 2026-11-23
- url https://utop.me/products/torbox-voucher
- price USD 5.75 per month (Standard voucher); USD 3.45 per month (Essential, 3-month voucher) | parsed USD 3.45/mo
- free tier: no free tier; the reseller sells TorBox voucher codes from USD 5.75 to USD 138.00. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: utop.us now redirects to utop.me: 'We've moved to a new domain'
- per-object cap: not applicable to this record: a voucher is not an object. | source: [1]
- retention: not applicable to this record: a voucher code does not expire in a way debrid measured. | source: [1]
- egress: not applicable: the reseller sells a code, not traffic. | metered: no | source: [1]
- identity: email | detail: Checkout with an email for delivery; rails include Alipay, SEPA, Wise, UPI, WebMoney and 50+ cryptocurrencies, so a card is not required. The rail list is quoted by TorBox in its own voucher terms, not by the reseller page debrid could open.
- interface: unknown
- limits:
  - write-gated: voucher redemption; 30-180 day terms [2]
- limits note: no payment-vocabulary limit. Purchase cap imposed by the vendor: 'TorBox does not allow any payments for vouchers over the total cost of $500 USD.'
- binding note: Nothing in the seven-kind vocabulary applies; the constraint here is price, about 15 percent over the vendor's own rate.
- interface detail: web store only; delivery is a code redeemed on torbox.app
- tooling: no API; a browser checkout and an emailed code
- composes with: the approved bridge from a country or an instrument the vendor checkout will not serve into a service that does take crypto: TorBox names this vendor in its own voucher terms.
- reliability: Instant delivery is claimed but the code path is a third party: a failed delivery is the reseller's to fix, and TorBox caps voucher purchases at USD 500.
- notes: Markup is flat at 15 percent on every tier checked: Standard 5.75 vs 5.00, Essential 3-month 10.35 vs 9.00, Essential 1-year 41.40 vs 36.00. That is the cheapest documented markup of any reseller among debrid providers and the reason the voucher path is worth naming at all. Included because it is the only route found where an Indian rail (UPI) buys a euro-priced entitlement at the provider's own price rather than a rupee markup. Trigger condition: UPI is dropped from the rail list.
- evidence note: The vendor's voucher terms name this reseller and its rails; the price ladder comes from the reseller's own product page as indexed, because the page itself answered 403 to the reader. What would raise it: reading utop.me with a session that passes its bot check.
- extras:
  - payment_group: crypto
  - resells: torbox
  - payment.card: unverified
  - payment.paypal: unverified
  - payment.crypto: 50+ cryptocurrencies
  - payment.local_rails: Alipay; SEPA; Wise; UPI; WebMoney
  - payment.markup_vs_direct: +15% on every tier checked
  - payment.example: Standard 1 month USD 5.75 vs USD 5.00 direct; Essential 1 year USD 41.40 vs USD 36.00 direct
  - rails: Alipay, altcoins, Bitcoin, N26, Paysera, Perfect Money, Revolut, SEPA, UPI, Webmoney
  - currency: EUR
  - region: Worldwide
- evidence:
  - [3] 2026-10-23: from the search index of the vendor's own terms: vouchers may be bought 'through the official TorBox website (https://torbox.app) or by the following approved vendor websites ... Utop.us - Accepts: Alipay, SEPA, Wise, UPI, WebMoney, 50+ Cryptocurrencies' and the USD 500 cap. The article body now returns 'that page doesn't exist', so this is an index extract.
  - [1] 2026-10-23: from the search index of the product page: 'Essential 3 Months 10.35 USD ... Essential 6 Months 20.70 USD ... Essential 1 Year 41.40 USD ... Standard 1 Month 5.75 USD', and the range 'Price: 5.75-138.00 USD'. The page itself answered 403 to the reader.
  - [4] 2026-10-23: the domain move: 'We've moved to a new domain ... UTop.us UTop.me'
  - [2] 2026-10-23: price list: '30 Days 5.00 EUR', '90 Days 11.00 EUR', '180 Days 18.38 EUR', '5.00 EUR- 35.33 EUR', 'Region Worldwide'
  - [5] 2026-10-23: 'UTop | English | Alipay, AltCoins, Bitcoin, N26, Paysera, Perfect Money, Revolut, SEPA, UPI, Webmoney' - UPI is the Indian rail and no card is listed
  - [6] 2026-10-23: search-index read: 'we are an official reseller of Real debrid ... pay using local payment options such as UPI or ban...' (live FAQ is client-rendered and returned no text)
- sources:
  - [1] https://utop.me/products/torbox-voucher
  - [2] https://utop.me/products/debrid-link-voucher
  - [3] https://support.torbox.app/en/articles/13262251-vouchers-terms-of-service
  - [4] https://utop.us/torbox-app/torbox-voucher
  - [5] https://www.debrid-link.com/resellers
  - [6] https://utop.me/faq
