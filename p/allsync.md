# Allsync

> allsync.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/allsync/ | JSON https://fshy.ajam.dev/api/v1/entity/allsync.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Allsync (managed Nextcloud, pay-as-you-go)

- `netdisk-pan/allsync` | qualifies | evidence documented | binding per-object-cap | category managed Nextcloud, paid only
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:06:37.166Z (live) | stale on 2026-11-13
- url https://allsync.com/pricing
- price From EUR 4/TB/month on the 1 to 10 TB pool, excluding any tax an EU resident pays; the per-tier ladder above 1 TB is not published | parsed USD 4.51/TB-mo
- free tier: No free tier. Pay-as-you-go in two pools: a GB pool from 10 to 1,000 GB starting at EUR 0.10 per GB billed annually, and a TB pool from 1 to 10 TB starting at EUR 4 billed monthly or annually | unit: TiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1] | note: EUR 4 is the TB pool's stated starting price. The page does not publish a per-tier price ladder beyond that floor, so the 10 TB figure is not established from the vendor page
- per-object cap: 'File size Unlimited' is stated as a plan property, and 'Devices Unlimited', 'Users Unlimited', 'Bandwidth Unlimited' and 'Speed Unlimited' are stated beside it. There is no published per-file ceiling | source: [1] | note: an unlimited file size claim is a claim about the absence of a limit and it is not a measured number; a Nextcloud instance still chunks uploads
- retention: Cancel any time; a refund may be requested within 14 days. No retention clock stated | source: [1]
- egress: 'Bandwidth Unlimited' as a plan property. The FAQ narrows it: 'We've set our bandwidth limits so high that 99% of our customers don't even come close', which is a fair-use statement and not an unmetered guarantee | metered: no | free allowance: unlimited, subject to a fair-use sentence | source: [1]
- identity: card | detail: a card, PayPal, SEPA direct debit or cryptocurrency. The FAQ lists 'Paypal, Mastercard, Visa, American Express, Ideal, Cryptocurrency, Bancontact, KBC/CBC, Belfius, SOFORT, paysafecard, CartaSi, Cartes Bancaires, SEPA Direct Debit, SEPA bank transfer'. The account itself needs only an email address, browser information and an IP address per the privacy answer
- interface: webdav, rest, rclone
- limits:
  - per-object-cap (binding): 'File size Unlimited', per the plan page, with no number behind it [1]
- binding note: Nothing is published that can bind: bandwidth, file size, users and devices are all stated as unlimited. The per-file cap is therefore unestablished rather than absent, and a plan built on it needs a chunker until one upload over 100 GB has been tried.
- tooling: rclone webdav, the Nextcloud clients for Windows, macOS, Linux, iOS and Android, and the Nextcloud AppStore. End-to-end encryption is optional and needs a master password
- composes with: Per-terabyte billing with no published egress line is the best-shaped contract of the five for a hot working set, because the cost tracks the bytes stored and not the bytes served. End-to-end encryption and server-side Office are mutually exclusive in Nextcloud, so choosing the encryption costs the collaboration features
- reliability: Registered Dutch company, EU storage. Crypto is accepted, which is unusual and which some buyers need. The 'Unlimited' claims are marketing-page assertions with no published quota table; the FAQ answers the bandwidth question with a fair-use sentence rather than a number
- notes: What is not verified is the price ladder above 1 TB: the page states a starting price and no per-tier table, so a buyer pricing 10 TB gets EUR 40/month only if the floor scales linearly, which the page does not say. That arithmetic is flagged as unconfirmed rather than published as a number.
- evidence note: The plan properties and the two pools are from the live page. The per-tier price above 1 TB is published nowhere, so `price_per_tb_month` carries the floor and the note says it is a floor. `documented`, not `measured`: nothing was ordered.
- extras:
  - access_mode: paid
  - free_tier_exists: no
  - region: Netherlands, EU storage
  - gb_pool: 10 to 1,000 GB, from EUR 0.10/GB billed annually
  - tb_pool: 1 to 10 TB, from EUR 4/TB billed monthly or annually
  - price_ladder_published: no
  - payment_methods_include_crypto: yes
  - e2ee: optional, master-password, and incompatible with server-side Office
- evidence:
  - [1] 2026-10-22: 'Users Unlimited', 'Bandwidth Unlimited', 'File size Unlimited', 'Devices Unlimited', 'Speed Unlimited' in the plan-property block
  - [1] 2026-10-22: 'Allsync GB ... Location: EU ... 10 - 1000 GB ... Free subdomain ... Starting from EUR 0,10 billed annually' and 'Allsync TB ... 1 - 10 TB ... Custom domain ... Starting from EUR 4 monthly or annually'
  - [1] 2026-10-22: FAQ: 'What is the bandwidth limit? We've set our bandwidth limits so high that 99% of our customers don't even come close'; 'If you're not satisfied, you can request a refund waiting 14 days'; payment methods list includes Cryptocurrency
  - [2] 2026-10-22: the TB product is orderable: 'Selected Product: Pay-As-You-Go - TB', a subdomain field, and a domain-or-subdomain choice, so the product page is a live order flow and not a marketing page
  - [1] 2026-10-21: the GB pool at EUR 0.10/GB billed annually and the TB pool at EUR 4, plus the same four 'Unlimited' claims
- sources:
  - [1] https://allsync.com/pricing
  - [2] https://allsync.com/store/pay-as-you-go/tb
