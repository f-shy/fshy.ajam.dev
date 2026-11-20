# 365Premium

> 365premium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/365premium/ | JSON https://fshy.ajam.dev/api/v1/entity/365premium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 365Premium

- `debrid/365premium-com` | qualifies | evidence documented | binding none | category premium-account reseller (Indian-registered: INR storefront with an explicit domestic payment stack) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://www.365premium.com/Real-Debrid/buy-Real-Debrid-30-Days-Premium-Account-reseller-india.html
- free tier: No free tier. The page sells 'Real-Debrid 30 Days Premium Account' and states delivery rather than price: 'Vouchers codes are automatically delivered to customers email account INSTANTLY'. No price was present in the rendered page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The price sits behind the cart; the record is kept for the payment stack, which is the best-documented Indian rail found.
- per-object cap: not applicable; Real-Debrid's own cap applies | source: [1]
- retention: not applicable: a 30-day voucher | days: 30 | source: [1]
- egress: Real-Debrid's own terms, resold. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Two gateways: an Indian one that processes 'Credit Cards (Visa MasterCard Diners Club), Debit Cards (52 Indian Banks), Net Banking (15 Banks) & Cash Cards (Itz) all in Indian Rupees', and an international one for 'US Dollars/EURO/YEN/INR'. Offline rails: 'Cash deposit, NEFT, Cheque/DD, Offline Net Banking (ICICI, SBI, HDFC) & Western Union'. A card works from either side of the border. | country: India
- interface: rest
- limits:
  - write-gated: voucher redemption on the provider; 30-day term [1]
- limits note: The vendor states it does not auto-debit: 'we do not auto debit/charge your Credit Card or Debit Card, for each renewal you have to make fresh payment'.
- binding note: No technical constraint at the reseller; Real-Debrid's quotas bind after redemption.
- interface detail: Web store with an automated voucher e-mail; the buyer redeems the voucher on Real-Debrid and then uses Real-Debrid's API.
- tooling: Real-Debrid's API and the usual clients; the reseller contributes only the payment leg.
- composes with: The Indian payment adapter with the widest rail list: it converts Indian cards, net banking, NEFT and even cash deposit into a Real-Debrid voucher. That makes it the fallback when a card is refused abroad and a local wallet is not enough.
- reliability: An old-style reseller page (products still listed as FileSonic, Megaupload, Duckload) whose stock and provider relationships are stale; the payment plumbing is documented far better than the catalogue is maintained.
- notes: Recorded for the payment stack, not the price. It is the counter-example to every other market among debrid providers: an Indian reseller that exposes both a domestic and an international gateway, so neither a local buyer without an international card nor a foreign buyer is locked out. Trigger condition: the checkout is found to be dead.
- evidence note: Payment rails read verbatim. The price and stock state were not rendered, so this record proves access rather than cost; a cart test would supply the number.
- extras:
  - local_gateway: Indian cards, 52 banks debit, 15 banks net banking, Itz cash cards, INR
  - international_gateway: Amex, Carte Bleue, Visa, Discover, Diners, Maestro, MasterCard, JCB, Solo; USD/EUR/JPY/INR
  - offline: cash deposit, NEFT, cheque/DD, Western Union
- evidence:
  - [1] 2026-10-23: 'We have integrated secured Indian payment gateway & process Credit Cards (Visa MasterCard Diners Club), Debit Cards (52 Indian Banks) Net Banking (15 Banks) & Cash Cards (Itz) all in Indian Rupees'
  - [1] 2026-10-23: 'We support offline payments by Cash deposit, NEFT, Cheque/DD, Offline Net Banking (ICICI, SBI,HDFC) & Western Union'; 'we do not auto debit/charge your Credit Card or Debit Card'
  - [1] 2026-10-23: 'We are registered company in India & we are authorised resellers/distributors'; automated voucher delivery by email
- sources:
  - [1] https://www.365premium.com/Real-Debrid/buy-Real-Debrid-30-Days-Premium-Account-reseller-india.html
