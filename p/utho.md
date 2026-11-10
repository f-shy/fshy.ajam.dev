# Utho

> utho.com | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/utho/ | JSON https://fshy.ajam.dev/api/v1/entity/utho.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Utho Archive Storage (India) — ₹0.38/GB/mo cold tier, ₹-denominated, no egress fee

- `storage/utho-archive-storage-0-38-gb-mo-cold-tier-denominated-no` | qualifies-with-caveat | evidence reported | binding none | category object-storage-cold
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://utho.com/archive-storage
- price Archive: $4.10/TB/mo at both 5 TB and 20 TB ($49.16/TB/yr), egress claimed $0. Standard object tier: $20.53/TB/mo at 10 TB ($205.28/mo), $26.32/TB/mo at 5 TB, $37.73/TB/mo at 250 GB — so the standard tier is 5× the archive tier at the same vendor. INR at 0.010527 USD/INR. | parsed USD 4.1/TB-mo
- free tier: ₹0.38/GB/month, no minimum commitment, 11-nines designed durability, 1-4 hour standard retrieval (instant available). The general object tier is quoted separately at ₹4/GB/month above a 100 GB base. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: «No egress fees in India» on the object-storage page and «Zero egress fees» / «No bandwidth overage charges» on the pricing page. The archive page itself says «No hidden retrieval fees». Utho's own pricing API, however, gives no bandwidth allowance per object plan (every plan's `bandwidth` field is 0), so the free-egress claim rests on marketing copy rather than a metered allowance. Record it as a claim, not a contract. | metered: no
- identity: card | detail: card
- interface: s3-compatible, rest, rclone
- limits note: 1-4 hour retrieval on the standard path. This is archive, not the hot 10 TiB. The archive product page carries no S3 endpoint of its own and no explicit statement that it is S3-addressable, so it may be a bucket lifecycle class rather than a separate API. Volume pricing is not published: the ladder from the API stops at 10 TB, and 20 TB requires sales contact.
- interface detail: s3 + rest
- tooling: S3-compatible API with documented REST v2 endpoints (verified live: `GET https://api.utho.com/v2/pricing/objectstorage` -> 200, full plan ladder returned). boto3, rclone `s3`, Datashim. CDN-ready.
- composes with: Per-GB with no cap, so 5 TB and 20 TB are the same rate. India-only regions (Noida/Mumbai).
- reliability: The most important reliability finding here is a PRICE DISCREPANCY INSIDE ONE VENDOR. Utho's marketing pages advertise object storage at «₹4/GB/month above 100 GB» and the pricing-comparison page claims «60-70 % More Affordable Than AWS», while Utho's own plan API returns ₹5.00/GB at 25 GB falling to ₹1.95/GB only at 10 TB. I.e. the advertised headline rate is roughly 2× the actual entry price and only reachable at the top of the ladder. Treat every Utho number as requiring an API cross-check. Node/uptime history not independently verified.
- notes: the same as the free tier
- extras:
  - price_verbatim: Archive: $4.10/TB/mo at both 5 TB and 20 TB ($49.16/TB/yr), egress claimed $0. Standard object tier: $20.53/TB/mo at 10 TB ($205.28/mo), $26.32/TB/mo at 5 TB, $37.73/TB/mo at 250 GB — so the standard tier is 5× the archive tier at the same vendor. INR at 0.010527 USD/INR.
- evidence:
  - [1] 2026-10-21: «Archive Storage ₹0.38/GB/month», «1-4hr Retrieval», «11 Nines Durability», «₹0.34/GB/month. No minimum commitment» (a second, lower figure appears in the FAQ block), «No hidden retrieval fees»
  - [2] 2026-10-21: probe: GET -> 200, full ladder returned: 25 GB ₹125 (₹5.00/GB), 100 GB ₹350 (₹3.50/GB), 500 GB ₹1350 (₹2.70/GB), 1000 GB ₹2800 (₹2.80/GB), 2000 GB ₹5100 (₹2.55/GB), 5000 GB ₹12500 (₹2.50/GB), 10000 GB ₹19500 (₹1.95/GB)
  - [3] 2026-10-21: «Starts at ₹500/month, Includes 100 GB of storage, + ₹4/GB/month above 100 GB» — contradicting the API's ₹350 for 100 GB
  - [4] 2026-10-21: «S3-compatible object storage with 11 nines durability. CDN-ready. Pay-as-you-go. No egress fees in India.»
  - [5] 2026-10-21: «Zero egress fees, zero early termination penalties», «No bandwidth overage charges»
- sources:
  - [1] https://utho.com/archive-storage
  - [2] https://api.utho.com/v2/pricing/objectstorage
  - [3] https://utho.com/pricing?tab=object
  - [4] https://utho.com/object-storage
  - [5] https://utho.com/simple-pricing

## Utho

- `compute/utho` | paid-only | evidence documented | binding none | category cloud VM | tier Basic 1 (India)
- identity a placeholder: card and phone unknown | verified 2026-10-24T02:05:00.000Z (live) | stale on 2026-11-24
- url https://utho.com/pricing
- price parsed USD 15.1/mo
- free tier: no free tier; the smallest cloud plan listed is INR 1,435 a month, or INR 4,305 a quarter | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: monthly or quarterly billing; the server persists while paid | source: [1]
- egress: 1000 GB of transfer a month on Basic 1 | metered: yes | free allowance: 1000 GB | source: [1]
- identity: card | detail: unverified: the pricing page was read and the signup path was not. The vendor is Indian and prices in rupees with GST, so a card and probably an Indian billing address are involved; neither is documented here
- interface: unknown
- limits:
  - volume-quota: 1000 GB a month [1]
- limits note: The two offers contradict each other: the landing page advertises INR 1,800 with no card, while the same page's footnote says the USD 25 30-day trial requires a valid credit card, and a third-party catalogue reports INR 1,000 with no card.
- binding note: the price binds: there is no shape under USD 5 on the pricing page read
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: INR 1,800 at the Utho ladder is a few weeks of a small instance, and it is a signup credit rather than a recurring allowance, so it composes with nothing durable.
- reliability: no reliability event recorded
- notes: INR 1,435 / 95.036492 = USD 15.10. The quarterly price is the same rate (4,305/3 = 1,435). Nothing on this page is near the line, so the identity question does not need answering to close the lead.
- evidence note: price, shape and transfer from the vendor's pricing page today; identity unverified
- extras:
  - facets.class: regional-credit
  - facets.free_tier_kind: one-shot-credit
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 80
  - billing_model: monthly or quarterly
  - term: monthly, quarterly
  - m10h_usd: 15.1
  - m24h_usd: 15.1
  - price_arithmetic: INR 1,435 a month / 95.036492 INR per USD = USD 15.10
  - renewal_usd: 15.1
  - fx.pair: USD/INR
  - fx.rate: 95.036492
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS that bills whether it runs or not
  - english: yes
  - payment_methods: not read
- evidence:
  - [2] 2026-10-22: 'Deploy Cloud Servers with industry leading price-performance and predictable costs. Try MicroHost Cloud free with Rs.1800 Credit.' and the footnote 'USD 25, 30-day free trial requires valid credit card', quoted from one page
  - [2] 2026-10-22: a legacy FAQ block on the same host states the trial needs 'a valid credit card ... to validate your identity' and that 'Unused service credits will automatically expire', and that the credit applies 'within the first 30 days', quoted
  - [3] 2026-10-22: a third-party catalogue read on 2026-10-16 reports 'INR 1,000 in free cloud credits for new users without a credit card', which contradicts both vendor figures, reported
  - [1] 2026-10-24: quoted: '| 2 vCPU, 4 GB RAM<br>80 GB NVMe, 1000 GB Transfer | ₹1,435<br>/month |' and '| Basic 1 | 2 vCPU | 4 GB | 80 GB NVMe | 1000 GB | ₹4,305/qtr |'
- sources:
  - [1] https://utho.com/pricing
  - [2] https://utho.com/lp/
  - [3] https://startupperklist.com/offers/utho/free-signup-credits

## utho object storage (in)

- `storage/utho-object-storage` | paid-only | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:39.699Z (live) | stale on 2026-12-04
- url https://utho.com/pricing?tab=object
- free tier: none reachable: ₹500/mo for 100 GB then ₹4/GB = $42.34/TB. 'No egress fees in India' is genuinely attractive but the storage rate is 20x the floor. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: No egress fees in India; the pricing page lists free bandwidth included. No egress cap is stated for other regions. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: pages read on 2026-11-03: utho.com/pricing?tab=object (plan starts at ₹500/ month, includes 100 GB of storage, + ₹4/ GB / month above 100 GB, free bandwidth included) and utho.com/object-storage (No egress fees in India.). The verdict and the egress terms rest on those captures; the identity cost was not read on a vendor page and stays as recorded.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: ₹500/mo for 100 GB then ₹4/GB = $42.34/TB. 'No egress fees in India' is genuinely attractive but the storage rate is 20x the floor.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: ₹500/mo for 100 GB then ₹4/GB = $42.34/TB. 'No egress fees in India' is genuinely attractive but the storage rate is 20x the floor.
  - [2] 2026-10-21: cited as the basis of the rejection: ₹500/mo for 100 GB then ₹4/GB = $42.34/TB. 'No egress fees in India' is genuinely attractive but the storage rate is 20x the floor.
  - [2] 2026-11-03: egress is free in India | capture: sha256:f2c0cddb13c0c3d283acd5ef8c8520316c57c51653b1aa979aac44a867ef17f6 | quote: No egress fees in India.
  - [1] 2026-11-03: object storage starts at 500 INR / month including 100 GB; there is no free object-storage allowance | capture: sha256:022348f04da7d990a35adfd589ff615771b4c89c3576420dddd982d50eacf3cf | quote: Includes 100 GB of storage
  - [1] 2026-11-03: the pricing page includes bandwidth at no charge | capture: sha256:022348f04da7d990a35adfd589ff615771b4c89c3576420dddd982d50eacf3cf | quote: Free bandwidth included
  - [1] 2026-11-03: the object-storage plan starts at ₹500 per month | capture: sha256:022348f04da7d990a35adfd589ff615771b4c89c3576420dddd982d50eacf3cf | quote: ₹500/ month
  - [1] 2026-11-03: object storage is billed at ₹4 per GB beyond the 100 GB base | capture: sha256:022348f04da7d990a35adfd589ff615771b4c89c3576420dddd982d50eacf3cf | quote: Flat ₹4/GB beyond the base
- sources:
  - [1] https://utho.com/pricing?tab=object
  - [2] https://utho.com/object-storage
