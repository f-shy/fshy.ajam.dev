# BuyPremiumKey

> buypremiumkey.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buypremiumkey/ | JSON https://fshy.ajam.dev/api/v1/entity/buypremiumkey.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BuyPremiumKey

- `debrid/buypremiumkey` | paid-only | evidence reported | binding write-gated | category debrid resale - voucher shop claiming official-reseller status | tier resale
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:55.819Z (live) | stale on 2026-11-18
- url https://buypremiumkey.com/premium-key-view-190/real-debrid-premium-30-days-reseller.html
- free tier: No free tier. 'Real-debrid Premium 30 Days' at $10.50, availability 'Not In Stock'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the page banner reads 'OFFICIAL AUTHORIZED RESELLER'; the claim is the shop's own
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: no byte allowance on the shop page; the description sells 'Maximum download speed', 'NO waiting', 'Resume support' | metered: no | free allowance: not published | source: [1]
- identity: card | detail: PayPal, Visa/MasterCard; delivery by email
- interface: rest
- limits:
  - write-gated (binding): all four Real-debrid vouchers (30, 90, 180 and 360 days) listed 'Not In Stock' on 2026-11-03 [1]
  - per-ip-shaping: one holder per account [2]
- binding note: There is nothing to buy: the only Real-Debrid SKU on the page is out of stock, so the gate is stock rather than any quota.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Out of stock on the read date, which is the observable state of a shop that restocks a 30-day key sporadically.
- notes: Vendor baseline, third-party: comparative listings lists Real-Debrid at EUR 3 / 15 days, EUR 4 / 30 days, EUR 9 / 90 days, EUR 16 / 180 days. real-debrid.com/premium returned 403 to read (exa, browserless, contextdev) and to fetch, so the vendor's own table was not read on 2026-11-03. $10.50 is 2.3x the vendor's own month, and the item cannot be bought. The page has carried 2017 metadata for a decade, which says nothing about current stock either way.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: price $10.50, 'Not In Stock', 'OFFICIAL AUTHORIZED RESELLER' banner, product code real-debrid-30d
  - [3] 2026-10-23: the vendor baseline of EUR 4 / 30 days that makes $10.50 a 2.3x markup
  - [1] 2026-11-03: the 30-day voucher is out of stock | capture: sha256:df2200d136fc6b26a4ebf2c59faf74288e885686abd9d76d088fd6ff299eea12 | quote: Not In Stock
  - [1] 2026-11-03: the 360-day voucher at $45.90 is out of stock | capture: sha256:df2200d136fc6b26a4ebf2c59faf74288e885686abd9d76d088fd6ff299eea12 | quote: [Real-debrid Premium 360 Days](https://buypremiumkey.com/premium-key-view-193/real-debrid-premium-365-days-reseller.html) $45.90 Not In Stock
  - [1] 2026-11-03: 30-day voucher priced $10.50, unchanged | capture: sha256:df2200d136fc6b26a4ebf2c59faf74288e885686abd9d76d088fd6ff299eea12 | quote: - ## $10.50
- sources:
  - [1] https://buypremiumkey.com/premium-key-view-190/real-debrid-premium-30-days-reseller.html
  - [2] https://real-debrid.com/terms
  - [3] https://github.com/fynks/debrid-services-comparison
