# IranGet

> iranget.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iranget/ | JSON https://fshy.ajam.dev/api/v1/entity/iranget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IranGet (ایران‌گت)

- `debrid/iranget` | paid-only | evidence documented | binding write-gated | category account shop and virtual-card seller (Iran; US Visa/MasterCard virtual cards, gift cards, host premium accounts) | tier retail
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://iranget.com/shop/gift-card
- free tier: not applicable: a shop. It sells virtual US Visa and MasterCard cards, Google Play and Apple gift cards, and premium accounts for foreign services. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The gift-card category holds four products; the shop's own summary says the cards exist so that 'خرید از فروشگاه های خارجی' and 'پرداخت هزینه سرویس های بین المللی' can be done from Iran.
- per-object cap: not applicable: a card or an account, not stored bytes. | source: [1]
- retention: not applicable: the card balance or the account term is the upstream issuer's. | source: [1]
- egress: not applicable: the shop sells the instrument, not transfer. | metered: no | source: [1]
- identity: email | detail: A customer account on the shop; the registration form was not read, so email as the minimum is inferred. | country: Iran
- interface: unknown
- limits:
  - write-gated (binding): the card or account is released after the shop's order step; the buyer must supply the shop's own account details first [1]
- limits note: The page tells the buyer to check the card's use, currency and region on the product page before buying, which is an admission that a card can be wrong for the intended checkout.
- binding note: No byte quota exists at this layer; the constraint is that the instrument is issued by a third party and can be refused by the merchant that is actually being paid.
- interface detail: Web storefront with a product catalogue; the card is delivered as card details, the account as credentials. Delivery mechanics were not read.
- tooling: Browser only.
- composes with: The card is the missing piece for a client in Iran: a virtual US Visa bought for Toman turns any card-only checkout, including a debrid service's, into a payable one. That is the rail, and it is bought like a product rather than held like a bank account.
- reliability: The card is issued to the shop, not to the buyer, so a fraud hold or a balance clawback lands on the shop's float; the buyer's only recourse is the shop, not the card network.
- notes: The Iranian answer to a card-only foreign checkout is not a bank product; it is a shop that sells a US card. This composes with the AllDebrid record (card + Bitcoin) and with any service that refuses Iranian-issued cards: payment is in Toman, the shop pays the foreign merchant with a US card.
- evidence note: The category contents, the four-product count and the shop's own sentence about foreign payments were read. Which issuer backs the virtual cards, and whether they pass 3-D Secure at a debrid checkout, were not established.
- evidence:
  - [1] 2026-10-23: 'ویزا کارت آمریکا، مستر کارت آمریکا، گیفت کارت گوگل پلی، گیفت کارت اپل', four products, and the sentence that virtual payment cards make foreign purchases and international service payments easier from Iran
  - [2] 2026-10-23: The shop positions itself as a premium-account and gift-card store ('خرید اکانت پرمیوم و گیفت کارت')
- sources:
  - [1] https://iranget.com/shop/gift-card
  - [2] https://iranget.com/
