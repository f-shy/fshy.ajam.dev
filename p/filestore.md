# FileStore.me

> filestore.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filestore/ | JSON https://fshy.ajam.dev/api/v1/entity/filestore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileStore.me

- `debrid/filestore-me` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (premium one-time) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://filestore.me/premium
- price EUR 14.99 per 30 days for 500 GB/day traffic | parsed USD 16.78/mo
- free tier: Free upload and share, 'FREE & always will be', with 'Unlimited files upload ... no limitation in size or speed'; storage and download volume limits are only stated for premium. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The free column is advertised as unlimited upload; the premium plan is what buys 'Unlimited storage' and 'Unlimited download... with no speed restrictions'.
- per-object cap: 'Upload your files with different methods and no limitation in size or speed.' | source: [1] | note: Stated only.
- retention: not stated on the pages read | source: [2]
- egress: Premium: 'Unlimited download ... with no speed restrictions' plus '500 GB traffic/daily'. The daily figure is the real ceiling; 'unlimited' is the marketing word above it. | metered: yes | free allowance: none stated for the free tier; premium carries 500 GB/day | source: [2]
- identity: card | detail: Checkout by card or PayPal, with fees added on top. The page warns 'dont use VPN server for payments', which is an egress restriction at the payment step rather than at download.
- interface: unknown
- limits:
  - volume-quota (binding): 500 GB of traffic per day on premium [2]
- limits note: The payment-rules block adds surcharges: '10% credit card fees are added to card payments', '20% paypal fees are added to paypal payments in USD'. The effective PayPal price of the 30-day plan is therefore about €17.99, not €14.99.
- binding note: 500 GB/day is far above what 1 TiB a month needs, so nothing in the vocabulary actually fails at that scale, but volume-quota is the only metered quantity the vendor states and it is the field a larger client would hit. Treated as the binding kind rather than none because the 20% PayPal surcharge is a price wall, not a byte wall.
- interface detail: Web upload with 'different methods'; no API, FTP or remote-upload endpoint is published on the pages read.
- tooling: Browser only as read. The host is on the Leechall and PrimeLeech generator lists, so a leecher is the only scripted path found.
- composes with: 500 GB/day is fifteen times the 34.1 GB/day 1 TiB of monthly transfer needs, so transfer is not the constraint here. The constraint is that nothing on the page prices storage separately, which makes it a transfer pipe rather than an archive.
- reliability: A payment attempted from a VPN is a stated way to fail the order; the fee surcharge is applied at checkout rather than shown in the advertised price.
- notes: The 365-day plan at €89.99 is €7.40 a month. The 10 GB top-up at €5.00 is the only pay-per-volume item on the page.
- evidence note: Plan prices, the 500 GB/day figure and the fee block are read from the vendor's premium page. The free tier's real storage cap is not printed anywhere read, so 'unlimited' here is the vendor's word and not a measurement.
- extras:
  - plans: 30 days €14.99; 90 days €32.99; 180 days €55.99; 365 days €89.99; 10 GB top-up €5.00
  - surcharges: 10% card, 20% PayPal (USD)
  - annual_effective_monthly: EUR 7.40
- evidence:
  - [2] 2026-10-23: the four prices (30 days €14.99, 90 days €32.99, 180 days €55.99, 365 days €89.99), each with 'Unlimited storage' and '500 GB traffic/daily', plus the 10%/20% card and PayPal surcharges
  - [1] 2026-10-23: 'It's FREE & always will be', 1,000,000+ files, and the free upload claim with 'no limitation in size or speed'
- sources:
  - [1] https://filestore.me/
  - [2] https://filestore.me/premium
