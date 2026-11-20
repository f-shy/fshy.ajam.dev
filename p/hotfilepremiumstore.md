# HotFilePremiumStore

> hotfilepremiumstore.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hotfilepremiumstore/ | JSON https://fshy.ajam.dev/api/v1/entity/hotfilepremiumstore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HotFilePremiumStore (reseller)

- `debrid/hotfilepremiumstore-com` | qualifies-with-caveat | evidence reported | binding none | category premium-account reseller (Indian: INR pricing for Real-Debrid and other hosts) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-07
- url https://www.hotfilepremiumstore.com/en/real-debrid/112-official-reseller-of-real-debrid-30-days-premium-account.html
- price INR 900 per 30 days for Real-Debrid (reported) | parsed USD 9.47/mo
- disagrees on verdict: `debrid/hotfilepremiumstore` says dead, `debrid/hotfilepremiumstore-com` says qualifies-with-caveat
- free tier: No free tier. Listed as 'Real- Debrid 30 Days Premium Account ... ₹900.00 ... In Stock' on the product page as indexed. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The store refused every fetch route tried, so the price is a search-index read and is carried at the reported rung.
- per-object cap: not applicable; Real-Debrid's own cap applies | source: [1]
- retention: not applicable: 30-day entitlement | days: 30 | source: [1]
- egress: Real-Debrid's own terms, resold. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Unresolved: the store refused all fetch routes, so no payment-method list was read. An Indian reseller of this shape typically takes card or UPI; that is an expectation, not a finding. | country: India
- interface: rest
- limits:
  - write-gated: store checkout; 30-day term [1]
- limits note: Nothing technical was readable; the page refused every route.
- binding note: No constraint readable at the reseller; Real-Debrid's quotas bind after activation.
- interface detail: Web store; entitlement or voucher delivered after checkout. Nothing on the page was readable to confirm the delivery mechanism.
- tooling: Real-Debrid's own API and clients after activation.
- composes with: A third rupee price point for the same European debrid, which matters only for comparison: ₹750 (Debrid-Link), ₹900 (Real-Debrid), ₹500 (AllDebrid).
- reliability: unverified: https://www.hotfilepremiumstore.com/en/real-debrid/112-official-reseller-of-real-debrid-30-days-premium-account.html answered HTTP 404 on 2026-11-03 (a 302 to the same path with SubmitCurrency=1&id_currency=2, then 404, 65053 bytes); routes tried: a rendered page read (404, page text 'The page you are looking for was not found.'), direct probe (404)
- notes: Carried at the reported rung on purpose: the Indian price set is more useful with a third point even when one is weaker, provided the weakness is stated. Trigger condition: the store renders, or the price is contradicted.
- evidence note: Price comes from the search index of the vendor's own product page; the page itself returned a proxy failure on two routes. A rendered read or a cart test would move this to documented.
- extras:
  - price_list_india: AllDebrid ₹500 (premiuminrupees), Debrid-Link ₹750 (247premiumcart), Real-Debrid ₹900 (this store)
- evidence:
  - [1] 2026-10-23: 'Real- Debrid 30 Days Premium Account ... ₹900.00 ... In Stock' (search-index read; direct read failed)
  - probe:https://www.hotfilepremiumstore.com/en/real-debrid/112-official-reseller-of-real-debrid-30-days-premium-account.html 2026-11-03: on 2026-11-03 a direct GET of the product page answered HTTP 302 to the same path with ?SubmitCurrency=1&id_currency=2, then HTTP 404 with 65053 bytes | capture: sha256:37962a36ae6c37a44f0c89d1e1d6036604333ef9f46afaead5b60f170249da09 | quote: "status": 404
- sources:
  - [1] https://www.hotfilepremiumstore.com/en/real-debrid/112-official-reseller-of-real-debrid-30-days-premium-account.html

## HotFilePremiumStore (resale)

- `debrid/hotfilepremiumstore` | dead | evidence reported | binding write-gated | category debrid resale - Indian shop whose Real-Debrid pages are gone | tier resale
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:59.771Z (live) | stale on 2026-11-18
- url https://www.hotfilepremiumstore.com/en/real-debrid/
- disagrees on verdict: `debrid/hotfilepremiumstore` says dead, `debrid/hotfilepremiumstore-com` says qualifies-with-caveat
- free tier: No free tier. A search-engine snippet of the product page reads 'Real- Debrid 30 Days Premium Account ... ₹900.00 ... In Stock' and 'Real- Debrid 360 Days ... ₹3,800.00'; on 2026-10-23 both the product URL and the category URL return 404 with 'No products available yet'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the ₹900 / ₹3,800 figures are from the snippet only; no page carrying them would load today
- per-object cap: not applicable to the resale: the single-object cap is the debrid vendor's, not the shop's | source: [2]
- retention: not applicable to the resale: cached-item retention is the debrid vendor's | source: [2]
- egress: not applicable: no live product page remains to state terms | metered: no | free allowance: none | source: [2]
- identity: card | detail: store checkout in Dehradun, India; card, netbanking, wallets or UPI | country: India
- interface: rest
- limits:
  - write-gated (binding): product and category pages both 404 on 2026-11-03 [2]
- binding note: The shop's Real-Debrid line has been withdrawn; the constraint is that there is nothing to buy.
- interface detail: the shop delivers a voucher code or a login by email; the capacity itself is reached through the debrid vendor's REST API
- tooling: any client that takes the vendor's API key: rclone, JDownloader, Stremio/Torrentio, pyload
- composes with: a resold voucher only changes how the days are paid for; the stack above it is unchanged
- reliability: An Indian 'official reseller' page that indexed at ₹900 for 30 days and ₹3,800 for 360 days, then disappeared. The disappearance is the finding.
- notes: Kept because a dead reseller is a finding: the ₹900 price point that search still surfaces cannot be bought. Do not cite it as a live Indian price without re-checking the store.
- evidence note: the seller's page was read; a seller is not the vendor, so nothing here is at the documented rung except the vendor terms quoted in evidence
- evidence:
  - [1] 2026-10-23: 404 today, with 'No products available yet' on the store page
  - [2] 2026-10-23: the category page also 404s; the store's own payment rails (card, netbanking, wallets, UPI) are still printed in the footer
  - probe:https://www.hotfilepremiumstore.com/en/real-debrid/ 2026-11-03: the category URL answers HTTP 404 on 2026-11-03 | capture: sha256:3c1f3c0288e9b3d19013c74d3498828bed0ceb25e2d3831e5adf09d2823dca4b | quote: "status": 404
  - [2] 2026-11-03: the Real-debrid category and product URLs answer 404 with 'No products available yet' | capture: sha256:20ddfa948d211844aa1e682f24e72300a85a169b18a882c3edc08165712e5d96 | quote: No products available yet
  - [2] 2026-11-03: the store still prints card, netbanking, wallet and UPI payment rails | capture: sha256:20ddfa948d211844aa1e682f24e72300a85a169b18a882c3edc08165712e5d96 | quote: 100% Secure Credit/Debit Card, NetBanking, Wallets, or UPI
  - [3] 2026-11-03: the store's home page navigation still lists a Real-debrid entry although its category page is empty | capture: sha256:428d1ceb743f0cabaa75487b62dc30eea1107f297886e67dbc39dec1d5e95a95 | quote: Real-debrid
- sources:
  - [1] https://www.hotfilepremiumstore.com/en/real-debrid/112-official-reseller-of-real-debrid-30-days-premium-account.html
  - [2] https://www.hotfilepremiumstore.com/en/real-debrid/
  - [3] https://www.hotfilepremiumstore.com/
