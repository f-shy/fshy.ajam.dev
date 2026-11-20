# Account.us

> account.us | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/account/ | JSON https://fshy.ajam.dev/api/v1/entity/account.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Account.us

- `debrid/account-us` | fails-identity | evidence reported | binding per-ip-shaping | category debrid resale - account-only shop (explicitly not a key) | tier resale
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:57.797Z (live) | stale on 2026-11-18
- url https://account.us/real-debrid-paypal-premium.html
- free tier: No free tier. The page states 'We DO NOT sell Real-debrid Premium Key, sell Account only', and on the read date shows 'There are no products matching the selection.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the shop's own rating widget reports '4.5 out of 5 based on 2 reviews'
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [1]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [1]
- egress: the page restates the vendor's feature list including 'Unlimited Traffic (4)' with the vendor's own footnote '(4) Except on some hosters' | metered: no | free allowance: not published | source: [1]
- identity: card | detail: PayPal; delivery of account credentials by email
- interface: rest
- limits:
  - per-ip-shaping (binding): an account created by the seller; the buyer never holds the mailbox [1]
  - write-gated: no stock on 2026-11-03 [1]
- binding note: The product is an account whose email belongs to the seller; the vendor's location PIN goes to that mailbox, so the buyer's access is contingent on a third party at every new network.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: Two reviews is not a rating; the shop is out of stock, and the product it sells is the one shape the vendor's terms name ('managing it for somebody else').
- notes: Included as the explicit statement of the account-only model: the shop tells the buyer the difference between a key and an account, which is the whole risk in one sentence.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: 'We DO NOT sell Real-debrid Premium Key, sell Account only', '4.5 out of 5 based on 2 reviews', and 'There are no products matching the selection.'
  - [2] 2026-10-23: 
  - [1] 2026-11-03: the shop still lists no product | capture: sha256:e3ac8bce8a037060dca8e105a5650548ad1033a2c0e96ad4ef99025c7d957495 | quote: There are no products matching the selection.
  - [1] 2026-11-03: delivery is by email; the page title names a PayPal reseller | capture: sha256:e3ac8bce8a037060dca8e105a5650548ad1033a2c0e96ad4ef99025c7d957495 | quote: We will send Real-debrid premium account to your email address.
  - [1] 2026-11-03: the shop still sells an account only, with no product in stock and 2 reviews | capture: sha256:e3ac8bce8a037060dca8e105a5650548ad1033a2c0e96ad4ef99025c7d957495 | quote: We DO NOT sell Real-debrid Premium Key, sell Account only
- sources:
  - [1] https://account.us/real-debrid-paypal-premium.html
  - [2] https://real-debrid.com/terms
