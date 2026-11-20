# KeyOneClick

> keyoneclick.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keyoneclick/ | JSON https://fshy.ajam.dev/api/v1/entity/keyoneclick.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KeyOneClick

- `debrid/keyoneclick` | paid-only | evidence reported | binding per-ip-shaping | category debrid resale - voucher shop claiming official-reseller status | tier resale
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:55.821Z (live) | stale on 2026-11-18
- url https://keyoneclick.com/real-debrid-premium.html
- free tier: No free tier. Four price points, all 'In stock': $8.90, $17.50, $28.90, $46.90. Only the first carries a term in the extracted text ('Debrid Premium 30 days'); the other three repeat the same feature list without a day count. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the four prices step in the same ratio as 30/90/180/365 days at vendor prices (2x each), so the mapping is inferred from the vendor's own ladder, not read
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: the shop advertises 'Download speed up to 300Mbps / Unlimited Traffic / Parallel downloads possible' per SKU; those are the vendor's features restated | metered: no | free allowance: not published | source: [1]
- identity: card | detail: PayPal, Visa/MasterCard, crypto and local payment methods, one-time payment, delivery by email; the buyer also needs a Real-Debrid account to redeem the voucher.
- interface: rest
- limits:
  - write-gated: voucher must be converted at real-debrid.com/voucher with the reseller name selected [1]
  - per-ip-shaping (binding): one holder per account; connections recorded [2]
- binding note: A voucher bought here is redeemed on the buyer's own account, so the IP constraint is the ordinary one-holder rule; the price is what loses, not the access.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: The voucher route is the least fragile resale form found: the account stays the buyer's and the seller never sees the password.
- notes: Vendor baseline, third-party: comparative listings lists Real-Debrid at EUR 3 / 15 days, EUR 4 / 30 days, EUR 9 / 90 days, EUR 16 / 180 days. real-debrid.com/premium returned 403 to read (exa, browserless, contextdev) and to fetch, so the vendor's own table was not read on 2026-11-03. $8.90 for 30 days is about 1.9x the vendor's EUR 4; $17.50 for 90 days about 1.7x EUR 9. Every term is a markup, and the shop's own 'official' claim cannot be checked before purchase because the vendor's authorised-reseller list is served inside the logged-in interface.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: the four prices, 'In stock' on each, the 'Official Reseller' header, and the redemption path at real-debrid.com/voucher
  - [2] 2026-10-23: resale requires the vendor's explicit permission; voucher redemption is the sanctioned form of a third-party sale
  - [3] 2026-10-23: the vendor baseline (EUR 4 / 30 days, EUR 9 / 90, EUR 16 / 180) that makes $8.90 a 1.9x markup
  - [1] 2026-11-03: the shop accepts crypto and local methods besides cards | capture: sha256:fadde9d3e79460aa0d7cc9208deb8cfc9266558443fe67488378b39397875614 | quote: Payment Flexibility: We accept local payment methods, Crypto and cards that international sites often reject.
  - [1] 2026-11-03: the page title lists PayPal and Visa/MasterCard | capture: sha256:fadde9d3e79460aa0d7cc9208deb8cfc9266558443fe67488378b39397875614 | quote: Real Debrid Premium via Paypal, Visa/MasterCard | KeyOneClick Official Reseller
  - [1] 2026-11-03: one-time payment, instant delivery, four In stock price points | capture: sha256:fadde9d3e79460aa0d7cc9208deb8cfc9266558443fe67488378b39397875614 | quote: Official Reseller - One Time Payment - Instant Delivery
  - [1] 2026-11-03: entry price unchanged | capture: sha256:fadde9d3e79460aa0d7cc9208deb8cfc9266558443fe67488378b39397875614 | quote: $8.90
  - [2] 2026-11-03: resale needs the vendor's explicit permission | capture: sha256:e304594fe96172746bad06bf29f97bc2973d87ec63ec9ea7f85da4a9e29cfe9a
- sources:
  - [1] https://keyoneclick.com/real-debrid-premium.html
  - [2] https://real-debrid.com/terms
  - [3] https://github.com/fynks/debrid-services-comparison
