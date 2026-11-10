# Leechall.io

> leechall.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leechall-2/ | JSON https://fshy.ajam.dev/api/v1/entity/leechall-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leechall.io

- `debrid/leechall-io` | paid-only | evidence reported | binding volume-quota | category premium-link generator (paid, one-time) | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:55.821Z (live) | stale on 2026-11-18
- url https://leechall.io/
- price USD 2.99 entry, period unverified
- free tier: No free tier: 'LEECHALL.IO is a paid service that allows you to download files instantly at the best Internet speed.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The free sibling is leechall.com, which is a separate tier with its own caps.
- per-object cap: not stated on the page read | source: [1]
- retention: not applicable: links are generated and consumed, not stored | source: [1]
- egress: Downloads are served from Leechall's own network at 'the best Internet speed'. The only price the page states is the entry point, 'Price from $2.99', referenced from the free site's banner; the checkout page was not opened, so the period that $2.99 buys is unverified. | metered: yes | free allowance: none | source: [1]
- identity: email | detail: A purchase through a payment processor; the page shows no free account path. Card, PayPal or crypto at checkout. The exact fields at signup were not read.
- interface: unknown
- limits:
  - volume-quota (binding): unknown: no byte or file allowance was published on the page read [1]
- limits note: The page advertises 'a lower price than the majority of file hosters' and no allowance. Whether it meters bytes, files or time is unstated, which is the gap a buyer needs closed before paying.
- binding note: Named as volume-quota because that is the shape a one-time leecher purchase almost always takes, not because the number was read. The number is unverified.
- interface detail: Web interface. Payments accepted: 'Card, Paypal, Cryptocurrency, Payeer, Binance Pay, WebMoney'. No API endpoint is published on the page read.
- tooling: browser only as read; no client library, no rclone backend.
- composes with: A paid per-download leecher that removes the ads from the free sibling. At $2.99 it is the cheapest way to test whether an otherwise unsupported host can be pulled at all before paying that host's own premium.
- reliability: One-time payment, no subscription, so there is no recurring charge to cancel; that also means no refund path stated on the page read.
- notes: Two records for one operator because the tiers differ in kind: the free site caps bytes per host, the paid site sells a one-time ad-free allowance. A reader acts on one of them.
- evidence note: The price comes from the vendor's own cross-link on leechall.com ('Price from $2.99') and the paid-site homepage; the checkout was not opened. Reading the checkout page would move the period and allowance to documented.
- extras:
  - payment_methods: Card, Paypal, Cryptocurrency, Payeer, Binance Pay, WebMoney
- evidence:
  - [1] 2026-10-23: paid-only service, one-time payment, the payment-method list, and 'Leechall.com has been trusted since 2016'
  - [2] 2026-10-23: the banner 'Leechall.io - Download File Instantly Without Any Ads - Price from $2.99', which is where the entry price is stated
  - [1] 2026-11-03: paid-only service, unchanged | capture: sha256:32b03debd9ad1cf270191fafa9981044b79158fd0ad5710427c61821433507ae | quote: LEECHALL.IO is a paid service that allows you to download files instantly at the best Internet speed.
  - [1] 2026-11-03: payment method list unchanged | capture: sha256:32b03debd9ad1cf270191fafa9981044b79158fd0ad5710427c61821433507ae | quote: Now accepting Card, Paypal, Cryptocurrency, Payeer, Binance Pay, WebMoney ...and more.
  - [2] 2026-11-03: the entry price 'Price from $2.99' is still the only price stated | capture: sha256:e84c300476217086e5c5520066523963a39329436dceab3c3019eaab8d16d271 | quote: [Leechall.io - Download File Instantly Without Any Ads - Price from $2.99](https://leechall.io/)
- sources:
  - [1] https://leechall.io/
  - [2] https://leechall.com/
