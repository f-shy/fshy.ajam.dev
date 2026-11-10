# TakeFile.link

> takefile.link | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/takefile/ | JSON https://fshy.ajam.dev/api/v1/entity/takefile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TakeFile.link

- `debrid/takefile-link` | qualifies-with-caveat | evidence documented | binding none | category file host sold only through third-party premium resellers | tier Premium (reseller-only)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:12:49.395Z (live) | stale on 2026-11-23
- url https://takefile.link/
- free tier: 'Free with a short wait', limited speed, one file at a time, countdown before download. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No byte allowance stated for the free tier.
- per-object cap: not stated on the pages read | source: [1] | note: unstated
- retention: not stated on the pages read | source: [1] | note: unstated
- egress: Premium is sold as 'no limits, no captcha, resume support', 'instant start, no timer', 'maximum speed'. No byte quota published. | metered: no | free allowance: free tier at limited speed | source: [1]
- identity: card | detail: A reseller account and a card or PayPal; takefile.link itself does not run a checkout. The reseller list names filesharingshop.com, premiumkeyshop.com, premiumkey.co, plusinstant.com and others.
- interface: unknown
- limits:
  - write-gated: uploads are restricted to affiliate partners; a normal account cannot upload [1]
  - request-rate: free tier: one file at a time with a countdown [1]
- limits note: The premium price is not published on takefile.link at all; the site answers /premium with a 404.
- binding note: No limit could be measured for a paying client: the price and the traffic rule both live at third-party resellers. The real constraint is commercial - who will sell a key - and that is not in the vocabulary.
- interface detail: Web download page with free/premium split. Upload is not open: 'Uploading is available for partners' - the host only accepts files from affiliates.
- tooling: Browser; premium keys are delivered by third-party shops, so the purchase path is off-site.
- composes with: A source host that appears in Russian-language release posts; a client needs it only when a wanted file is hosted there, and then the only way to buy is a reseller.
- reliability: Because every key comes from a reseller, the buyer's counterparty is the shop, not the host; one reseller in the list (filesharingshop) accepts YooMoney, so the same key has both a card rail and a Russian rail.
- notes: The reseller-only model is the finding: a user can pay with a card, but only by trusting a shop that the host lists without a contract. The payments offered by the shops span PayPal, cards, WebMoney, Bitcoin and YooMoney, which makes this one of the few hosts in the sector payable from both sides of the payment wall. No price is included because none is published.
- evidence note: The free/premium split, the partner-only upload rule and the full reseller list with their payment methods are quoted from live pages today. The price is not published anywhere readable and stays unverified.
- evidence:
  - [1] 2026-10-23: 'Uploading is available for partners', the free-vs-premium table ('Countdown before download', 'Limited speed', 'One file at a time'), and 'All payment methods ... Bank cards, alternative and regional options'
  - [2] 2026-10-23: the reseller list and each shop's methods: filesharingshop (Paypal, Credit Cards, JCB, Webmoney, Bitcoin, Dotpay, ... Yandex), premiumkeyshop (PayPal, Visa, MasterCard, ...), premiumkey.co (Visa, Master, JCB, AMEX, Paypal, ...)
  - [3] 2026-10-23: HTTP 404 'Page not found' - there is no vendor premium page, which is why the reseller list is the only purchase route
- sources:
  - [1] https://takefile.link/
  - [2] https://takefile.link/resellers
  - [3] https://takefile.link/premium
