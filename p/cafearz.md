# Cafe Arz

> cafearz.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cafearz/ | JSON https://fshy.ajam.dev/api/v1/entity/cafearz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cafe Arz (کافه ارز)

- `debrid/cafe-arz` | paid-only | evidence documented | binding write-gated | category cross-border payment intermediary (Iran; pays foreign subscriptions on the customer's behalf) | tier service
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://cafearz.com/blog/purchase-premium-accounts/
- free tier: not applicable: a payment service, not a retrieval service. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The article is dated 2023-11-29; the firm's current fee schedule was not read.
- per-object cap: not applicable. | source: [1]
- retention: not applicable. | source: [1]
- egress: not applicable: the firm pays a foreign merchant, it does not carry the traffic. | metered: no | source: [1]
- identity: email | detail: A customer account with the firm. Iranian exchange businesses normally verify identity, but the KYC fields were not read here, so the tier is recorded as email and flagged as probably higher. | country: Iran
- interface: unknown
- limits:
  - write-gated (binding): every purchase is an order a human or a compliance step must accept before the foreign charge is made [1]
- limits note: The firm's own article frames the problem as structural: buying a foreign subscription from Iran 'has many challenges' and requires a company of this kind.
- binding note: There is no byte quota to bind; what binds is the intermediary's willingness and capacity to settle the charge, which is an approval rather than a counter.
- interface detail: A web service with a subscription-purchase page (cafearz.com/buy-subscription) and a blog; the order form itself was not opened.
- tooling: Browser only.
- composes with: For a client in Iran this is the substitute for a card: the firm takes Toman and settles the foreign charge, so a debrid subscription priced in euro becomes payable without a foreign card and without a reseller's markup on the account itself.
- reliability: The subscription depends on the intermediary's own foreign accounts staying open; when an intermediary loses its settlement path, every subscription it paid for lapses at once.
- notes: Iranian domestic payment service providing account settlement without international cards. No published fee schedule.
- evidence note: The article's statement of the problem and the existence of the subscription service were read. Fees, settlement time and the identity fields are unread, so the record documents the rail's existence rather than its price.
- evidence:
  - [1] 2026-10-23: 'خرید اشتراک از سایت های خارجی در ایران چالش زیاد دارد و ما برای پرداخت هزینه آن باید از شرکت‌هایی نظیر کافه ارز کمک بگیریم', plus the link to its subscription-purchase service
- sources:
  - [1] https://cafearz.com/blog/purchase-premium-accounts/
