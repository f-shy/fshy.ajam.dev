# VirMach

> virmach.com | Compute, Egress and tunnels, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/virmach/ | JSON https://fshy.ajam.dev/api/v1/entity/virmach.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VirMach (compute/virmach)

- `compute/virmach` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.serverhunter.com/offer/virmach-ssd256/
- disagrees on identity_kind: `compute/virmach` says email, `compute/virmach-black-friday-cyber-monday` says card
- disagrees on verdict: `compute/virmach` says paid-only, `compute/virmach-black-friday-cyber-monday` says dead
- free tier: USD 1.25/month for the 'SSD256' plan in Buffalo, New York: 1 core, 384 MB RAM, 10 GB SSD on hardware RAID 10, 100 Mbit uplink, 500 GB traffic, KVM, no setup fee. The provider's own description on the row reads '256-384MB DEDICATED RAM // 1 vCORE // 10GB SSD (HW RAID 10) // DDoS Protection Available // 500GB BANDWIDTH // 100MBPS - 1GBPS'. Stock is 'Stock unknown'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB a month, printed both on the tracker row and in the provider's own description of the plan. No overage price is stated | metered: yes | free allowance: 500 GB per month | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 500 GB a month is the allowance printed on the row and in the provider's own description, so the byte counter is the first wall; 500 GB on a 100 Mbit port is about 11 hours of line-rate traffic, and the port range the description gives runs to 1 Gbit, which shortens that further. No overage price is stated. [1]
- limits note: 500 GB a month is the allowance printed on the row and in the provider's own description, so the byte counter is the first wall; 500 GB on a 100 Mbit port is about 11 hours of line-rate traffic, and the port range the description gives runs to 1 Gbit, which shortens that further. No overage price is stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: USD 1.25 for 384 MB is the cheapest paid machine among documented hosts by a wide margin and it buys an always-on socket, a cron runner or a tiny relay. The stock history is the reason not to build on it: an offer whose last confirmed in-stock date is 2019 is a price on a page, not capacity
- reliability: the tracker's own stock history shows this offer last in stock on 30 November 2019 and 'Stock unknown' since 28 February 2022, so availability is unverified
- notes: Found via serverhunter. Recorded despite the stale stock line because the price is what the index publishes and the staleness is itself the finding. Unverified: an attempt to order the plan, which is the only test of whether USD 1.25 is still a purchasable machine.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.375
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Monthly price USD 1.25, 'Product type VPS', 'Virtualization type KVM', 'Stock Stock unknown', 'Processor cores 1 core', 'Memory amount 384 MB', 'Total SSD Capacity 10 GB', 'Uplink 100 Mbit', 'Traffic 500 GB', 'Location Buffalo, New York, United States of America'; provider description quoted above
  - [1] 2026-10-22: the pages own stock-history table reads This offer was last seen in stock on the 30th of November 2019 at 01:08:13 (UTC) (6 years, 10 months, 2 weeks ago), followed by a Stock unknown' row dated 28 February 2022
  - [2] 2026-10-22: the vendor homepage returns 200 and describes 'cheap VPS (virtual machine cloud hosting) for a few dollars, in 14 global datacenters' with no plan table in the extract; https://virmach.com/kvm-vps/ returned a 404 body
- sources:
  - [1] https://www.serverhunter.com/offer/virmach-ssd256/
  - [2] https://virmach.com/

## VirMach (Ryzen 1 Core 512MB)

- `egress/virmach-ryzen-512mb` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS: KVM VPS with a metered monthly allowance and a 1 Gbps port | tier Ryzen 1 Core 512MB
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:55:17.627Z (live) | stale on 2026-12-05
- url https://virmach.com/amd-ryzen-kvm-vps-with-nvme-ssd/
- free tier: No free tier. The Ryzen 1 Core, 512MB, 15GB NVMe plan lists 1TB of monthly data at 1Gbps for $2.50 a month. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month at 1 Gbps. Going over the allocation suspends the service until the counter resets; a service may not use more than 50% of its monthly allocation in under 14 days or more than 10% in under 24 hours; extra data is sold at 500 GB for a one-time USD 10.00. | metered: yes | free allowance: 1 TB per month, reset on the first day of the month or at the recurring payment date | price per TB: USD 10.00 for 500 GB of extra data, one time | source: [2]
- identity: card | detail: Orders pass through automated fraud protection and need correct billing information; the accepted payment methods are unverified: behind a sign-up.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB per month; exceeding it suspends the service until the reset; extra data 500 GB for USD 10.00 one time [2]
  - per-ip-shaping: no more than 50% of the monthly allocation in under 14 days, no more than 10% in under 24 hours, no more than 50,000 conntrack sessions, no burst at or above 80% of the port speed for more than 5 minutes in a row or 24 hours a month [2]
- binding note: The 1 TB allowance is reached first for a transit of 1 TiB a month, and the terms also stop a draw of 10% of it in a day, so a steady 1 TiB a month relay needs the paid extra data.
- interface detail: Root VPS with full virtualization.
- tooling: Any SSH client; the root VPS takes any protocol that its kernel runs.
- composes with: A 1 TB, 1 Gbps KVM box on a public IPv4. The terms cap simultaneous connection tracking at 50,000 sessions and port bursts at 80% of the port speed for 5 minutes in a row or 24 hours a month, which a relay or a WireGuard endpoint has to stay under. The terms print no list of blocked ports.
- reliability: A service that goes over its allocation is suspended and unsuspends at the next reset.
- notes: Monthly price USD 2.50 for 1 TB gives USD 30 a year; the annual RN deals on serverdeals are cheaper per year but were not found on the vendor's pages.
- evidence note: The serverdeals listing RN-768M (USD 9.88 a year, 1 TB, 1 Gbps) was not found on the vendor's pages read.
- extras:
  - ipv6: unverified: not stated on the plan row
  - term: monthly
  - virtualization: KVM, full virtualization
- evidence:
  - [1] 2026-11-04: the Ryzen 1 Core 512MB plan lists 1 TB of monthly data at 1 Gbps for USD 2.50 a month | capture: sha256:9f3bf8b198f41356ee4416bf5a96e92ced50e85306ba907108f28ee4423c36fd | quote: | 1 Core | 512MB | 15GB | 1TB @ 1Gbps | $2.50 | INSTANT |
  - [1] 2026-11-04: the plan is a fully virtualized root VPS | capture: sha256:9f3bf8b198f41356ee4416bf5a96e92ced50e85306ba907108f28ee4423c36fd | quote: Full Virtualization/Root Access
  - [2] 2026-11-04: exceeding the allocation suspends the service | capture: sha256:4d36cce26b1988571e11ca365daef764d9fd9e10370f38cb2b2f464be5e6719b | quote: Going over your allocated bandwidth will result in a Service suspension.
  - [2] 2026-11-04: a draw is shaped by a 14-day and a 24-hour share of the allocation | capture: sha256:4d36cce26b1988571e11ca365daef764d9fd9e10370f38cb2b2f464be5e6719b | quote: Customer’s Service cannot use more than 50% of the monthly allocated bandwidth in under fourteen (14) days, or more than 10% of the monthly allocated bandwidth in under twenty-four (24) hours.
  - [2] 2026-11-04: the connection-tracking ceiling is 50,000 sessions | capture: sha256:4d36cce26b1988571e11ca365daef764d9fd9e10370f38cb2b2f464be5e6719b | quote: Customer’s Service cannot have more than 50,000 conntrack sessions at any given time
  - [2] 2026-11-04: extra data is sold at 500 GB for USD 10.00 one time | capture: sha256:4d36cce26b1988571e11ca365daef764d9fd9e10370f38cb2b2f464be5e6719b | quote: · 500 GB for one-time fee of $10.00.
  - [2] 2026-11-04: orders need billing information and pass automated fraud screening | capture: sha256:4d36cce26b1988571e11ca365daef764d9fd9e10370f38cb2b2f464be5e6719b | quote: VirMach uses automated fraud protection on all orders, so please enter all billing information correctly.
  - [3] 2026-11-04: serverdeals lists a VirMach RN-768M at USD 9.88 a year with 1 TB and a 1 Gbps port, a listing not found on the vendor's pages read | quote: ###### RN-768M
- sources:
  - [1] https://virmach.com/amd-ryzen-kvm-vps-with-nvme-ssd/
  - [2] https://virmach.com/terms-conditions/
  - [3] https://serverdeals.cc/

## virmach storage / cloud storage

- `storage/virmach-storage-cloud-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://virmach.com/storage-vps/
- free tier: none reachable: Cheap headline ($3/mo for 250 GB) that inverts at scale: $10/TB at 500 GB, and the STORAGE-1T rung on the live page shows 'OR $4.80 PER YEAR', which is a clear page bug rather than a price. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cheap headline ($3/mo for 250 GB) that inverts at scale: $10/TB at 500 GB, and the STORAGE-1T rung on the live page shows 'OR $4.80 PER YEAR', which is a clear page bug rather than a price.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cheap headline ($3/mo for 250 GB) that inverts at scale: $10/TB at 500 GB, and the STORAGE-1T rung on the live page shows 'OR $4.80 PER YEAR', which is a clear page bug rather than a price.
  - [2] 2026-10-21: cited as the basis of the rejection: Cheap headline ($3/mo for 250 GB) that inverts at scale: $10/TB at 500 GB, and the STORAGE-1T rung on the live page shows 'OR $4.80 PER YEAR', which is a clear page bug rather than a price.
- sources:
  - [1] https://virmach.com/storage-vps/
  - [2] https://virmach.com/cloud-storage-servers/

## VirMach (black friday cyber monday)

- `compute/virmach-black-friday-cyber-monday` | dead | evidence documented | binding volume-quota | category VPS | tier Hannukah Candle offers, USD 18.88 per two years
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T06:20:13.000Z (live) | stale on 2026-11-24
- url https://virmach.com/black-friday-cyber-monday/
- disagrees on identity_kind: `compute/virmach` says email, `compute/virmach-black-friday-cyber-monday` says card
- disagrees on verdict: `compute/virmach` says paid-only, `compute/virmach-black-friday-cyber-monday` says dead
- free tier: no free tier; the page offers 1 GB / 1 core / 25 GB SSD at USD 18.88 per two years | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the term is paid; no deletion clock stated
- egress: 2 TB of bandwidth, stated in the offer line as '2TB BW' | metered: yes | free allowance: 2 TB | source: [1]
- identity: card | detail: card at signup through billing.virmach.com; no hold stated
- interface: ssh
- limits:
  - volume-quota (binding): 2 TB of bandwidth on the Candle offers [1]
- binding note: The order pids. All four cart links on the page resolve to a support-level store or to Out of Stock.
- interface detail: root SSH; the page names LowEndSpirit as the place offer details live
- tooling: any SSH client
- composes with: At USD 18.88 for two years the machine is USD 0.79 a month, which would beat everything else among documented hosts; the carts do not sell it.
- reliability: no reliability event recorded
- notes: The page is live and specific - it names eight dated candles, each USD 18.88 for two years - but none of the four order links reaches a Candle product. Three repoint to the account support-level store, where the cheapest line is USD 60.00 a year for support, and the fourth is Out of Stock. The page also says the offers are discussed on LowEndSpirit, which is where the detail lives, so the page may be a permanent stub that never carried a working cart. Not verified: whether the candles are claimable at all through a route this category did not try, such as a LowEndSpirit thread link.
- evidence note: The page and four cart pids were read. The prices are quoted from the page; the cart outcomes are quoted from each pid.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 25
  - billing_model: biennial
  - term: two-year prepay
  - price_arithmetic: USD 18.88 over 24 months is USD 0.7867 a month, paid once. Not recorded as a live price because no cart sells it.
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - sale_page_year: undated; the candles run Dec. 25 to Jan. 1 and the page carries no year
  - order_links_tested: 4
  - order_links_out_of_stock: 1
  - order_links_repointed: 3
- evidence:
  - [1] 2026-10-24: quoted: 'Candle #1 (Dec. 25) $18.88 PER TWO YEARS 1GB, 1 Core, 25GB SSD, 2TB BW, 1 IPv4', repeated for Candles 2 to 8; also 'Custom Plan Sale (2-Year) ... 50% off, limit one per customer'
  - [2] 2026-10-24: repoints to /store/account-support-level, which lists $60.00, $300.00, $1200.00 and $9600.00 annually - support tiers, not the Candle offer
  - [3] 2026-10-24: same repoint to /store/account-support-level
  - [4] 2026-10-24: same repoint to /store/account-support-level
  - [5] 2026-10-24: quoted: 'Out of Stock'
- sources:
  - [1] https://virmach.com/black-friday-cyber-monday/
  - [2] https://billing.virmach.com/cart.php?a=add&pid=155
  - [3] https://billing.virmach.com/cart.php?a=add&pid=180
  - [4] https://billing.virmach.com/cart.php?a=add&pid=3
  - [5] https://billing.virmach.com/cart.php?a=add&pid=268
