# PremiumInRupees

> premiuminrupees.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiuminrupees/ | JSON https://fshy.ajam.dev/api/v1/entity/premiuminrupees.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PremiumInRupees

- `debrid/premiuminrupees-com` | qualifies-with-caveat | evidence documented | binding none | category premium-account reseller (Indian: INR pricing, AllDebrid and other hosts) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T15:05:36.570Z (live) | stale on 2026-12-04
- url https://premiuminrupees.com/product-by-category/alldebrid
- price INR 500 per 30 days for AllDebrid | parsed USD 5.26/mo
- free tier: No free tier. 'Alldebrid 1 month premium account 1 month premium account Available ₹500.00 30 Days Validity.' Longer AllDebrid terms are listed above and below it in the same category. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The price is read from the vendor's rendered category page; a plain read of the page returns a shell with no listing.
- per-object cap: not applicable; AllDebrid's own cap applies | source: [1]
- retention: not applicable: 30-day entitlement | days: 30 | source: [1]
- egress: AllDebrid's own terms, resold; the listing's speed line is generic ('Download Upto Mbps Speed For Downloading', with the number missing). | metered: yes | free allowance: none | source: [1]
- identity: card | detail: The site advertises an SSL secure payment gateway and its secure payment page names 'Using Visa/Mastercard'; it describes itself as 'a part of AT Solutions ... provider of cloud hosting premium accounts'. Whether an Indian wallet is also accepted is unverified: the payment icons carry no text. | country: India
- interface: rest
- limits:
  - write-gated: manual store checkout; 30-day validity per unit [1]
- limits note: No limit of its own; only validity is stated.
- binding note: The reseller adds no constraint; AllDebrid's fair-use and host quotas bind afterwards.
- interface detail: Web shop; the buyer activates the AllDebrid entitlement and then uses AllDebrid's own web app and API.
- tooling: AllDebrid's API and community tools (rclone via WebDAV bridges, JDownloader); the reseller adds nothing technical.
- composes with: A second Indian rupee route to a European debrid at ₹500/month, which undercuts the Debrid-Link reseller on entry price. It buys the same thing: an entitlement, not a service.
- reliability: The category listing renders only through a browser-rendering read; a plain read returns a shell that shows Loading in place of the listing. The business identity is a single line about AT Solutions and an Altis Infonet design credit.
- notes: Kept despite the weaker rung because it sets the Indian price floor: ₹500/month for a full multi-hoster is cheaper than paying AllDebrid in euros at list. The caveat is the rung, not the price. Trigger condition: the storefront renders and the price is confirmed or corrected.
- evidence note: The INR 500 for 30 days figure is read from the vendor's rendered category page; a plain read of the same page returns a shell, so only a browser-rendering read shows it.
- extras:
  - catalogue: AllDebrid and other premium accounts
- evidence:
  - [1] 2026-10-23: 'Alldebrid 1 month premium account ... Available ₹500.00 30 Days Validity' (search-index read; live page returned an empty shell)
  - [2] 2026-10-23: 'www.premiuminrupees.com is a part of AT Solutions. It is a world leading provider of cloud hosting premium accounts'; 'Secure Payment 256 SSL Secure Payment Gateway'
  - [3] 2026-10-23: the earlier product listing returned an 788-byte shell with no prices; recorded so the failed route is visible
  - [1] 2026-11-03: a plain read of the category page returns a shell that shows Loading in place of the listing | capture: sha256:658764d04540821f7d814223b786a364bd7639c79ef4e3df667e4f65b3283182
  - [1] 2026-11-03: the vendor's rendered category page lists the 1-month AllDebrid account at INR 500.00 with 30 days validity | capture: sha256:2d26e2941f6fa74bc7953137982bc903383a5d2b4a800025e1b8f2f00cf5fbc1 | quote: [1 month premium accountAvailable ₹500.0030 Days Validity. Download Upto** Mbps Speed** For Downloading.]
  - [4] 2026-11-03: the vendor's secure payment page names Visa/Mastercard | capture: sha256:5cd1e88ab519bd54827acf47ef61e12e392bb39008e9c53c06ef2a00f76ddfa0 | quote: ### Using Visa/Mastercard
- sources:
  - [1] https://premiuminrupees.com/product-by-category/alldebrid
  - [2] https://www.premiuminrupees.com/
  - [3] https://premiuminrupees.com/68-alldebrid
  - [4] https://premiuminrupees.com/secure-payment
