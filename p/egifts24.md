# eGifts24

> egifts24.co.za | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/egifts24/ | JSON https://fshy.ajam.dev/api/v1/entity/egifts24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## eGifts24

- `debrid/egifts24` | paid-only | evidence documented | binding write-gated | category South African voucher retailer (ZAR; a gift-card rail accepted by TorBox) | tier voucher
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://www.egifts24.co.za/egifts24-choice-voucher/
- free tier: not applicable: a voucher retailer. The instrument is a choice voucher exchangeable for 20+ brands on eGifts24.co.za and usable only on that site. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: TorBox lists 'eGifts24 [ZAR]' among the gift cards it accepts, with a USD 20 minimum value.
- per-object cap: not applicable. | source: [1]
- retention: not applicable: a voucher code, not stored bytes. | source: [1]
- egress: not applicable. | metered: no | source: [1]
- identity: email | detail: An eGifts24 account to link the voucher ('log in or create a new account'), plus the TorBox account the credit lands on. | country: South Africa
- interface: unknown
- limits:
  - write-gated (binding): TorBox verifies the card's value and legitimacy before crediting an account, and gift cards are accepted for one-time payments only, not subscriptions [2]
- limits note: The voucher itself is 'Valid for use in South Africa only', so the rail is closed to a buyer outside South Africa even though TorBox is not.
- binding note: Nothing is metered at this layer; the gate is a human verification step at the debrid vendor and a geographic restriction on the voucher.
- interface detail: A web checkout delivering a voucher code by email; the TorBox side of the rail is an email to support with the code, not an automated redemption.
- tooling: Browser checkout; the TorBox redemption is a support ticket.
- composes with: This is the only documented path among debrid providers where a local African currency buys a global debrid subscription without a foreign card: buy the ZAR voucher locally, send it to TorBox support, and receive account credit.
- reliability: Manual redemption means days of delay and a support decision: the code is checked for value and legitimacy before the plan is applied, and the article's own terms make the voucher non-returnable.
- notes: The one local rail in the sector that a global debrid service explicitly accepts. It is a voucher, not a card rail: it does not generalise to Egypt, Nigeria, Kenya, the Gulf or Iran, none of which appears in TorBox's gift-card list.
- evidence note: Both sides were read: the voucher's terms on eGifts24 (through a provider that returned the page despite a 403 to the direct reader) and TorBox's gift-card paragraph naming eGifts24 ZAR. What would raise it: one completed redemption with the credit landing on an account.
- evidence:
  - [1] 2026-10-23: The Choice Card is a digital voucher exchangeable for 20+ brands on eGifts24.co.za only, 'Valid for use in South Africa only', non-returnable
  - [2] 2026-10-23: Gift cards are accepted after support verifies value and legitimacy, minimum USD 20 equivalent in ZAR/AUD/CAD, and the list names 'eGifts24 [ZAR]'
- sources:
  - [1] https://www.egifts24.co.za/egifts24-choice-voucher/
  - [2] https://support.torbox.app/en/articles/9835794-what-payment-types-can-i-use
