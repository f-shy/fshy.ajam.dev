# HostEons

> hosteons.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosteons/ | JSON https://fshy.ajam.dev/api/v1/entity/hosteons.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostEons (Compute)

- `compute/hosteons` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.035Z (live) | stale on 2026-12-08
- url https://hosteons.com/kvm_vps.php
- free tier: The cheapest plan the vendor's pages let you order is Gigabit VPS 1 at USD 21 a year: 1 fair-share core, 1 GB RAM, 10 GB SSD, 1 IPv4 plus IPv6, 1 TB of bandwidth, in Los Angeles, Salt Lake City, Portland, New York, Miami and Dallas. The Premium Ryzen page prices RYZEN 512 MB at USD 24 a year with 1 fair-share core at 3.5 GHz+, 512 MB RAM, 10 GB NVMe, 1 IPv4 plus a /64 IPv6 and 500 GB at 1 Gbit, which is the same shape the tracker lists at USD 17.99 a year. The Special Ryzen Promo store page shows every tier 'Out of Stock', including Ryzen SP1 at USD 3.00 a month. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on Gigabit VPS 1 and 500 GB a month on RYZEN 512 MB, at 1 Gbit; no overage rate is published on either page read | metered: yes | free allowance: 1 TB a month on the USD 21 a year plan | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): 1 TB a month on Gigabit VPS 1 and 500 GB on RYZEN 512 MB, both against 10 GB of disk; the byte allowance is small enough that a daytime crawler meets it quickly, and no overage rate is published [1]
- limits note: 1 TB a month on Gigabit VPS 1 and 500 GB on RYZEN 512 MB, both against 10 GB of disk; the byte allowance is small enough that a daytime crawler meets it quickly, and no overage rate is published
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, rDNS and a VPS control panel, on a Singapore-registered company with US and EU locations; SSH and the client area, no API documented on the pages read
- composes with: USD 21 a year works out under USD 2 a month for a machine that can hold a scheduler, a monitor or a small crawler front end in six US cities; the 10 GB disk and 1 TB cap keep it away from anything that stores or serves bulk bytes
- reliability: no reliability event recorded
- notes: The tracker's USD 17.99 a year for the 512 MB Ryzen shape was not found at that price on any vendor page read; the vendor prices the same shape at USD 24 a year, and the separate stock-clearance store that did sell cheaper tiers is out of stock on every line. The headline figure here is the vendor's cheapest orderable plan, which is a different plan from the one the tracker priced. verification criteria: whether the USD 17.99 promo returns, and what the overage charge is above 1 TB.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - term: annually USD 21.00, biennially USD 40.00, triennially USD 55.00; the cart lists no monthly cycle
  - annual_usd: 21.0
  - renewal_usd: not published: no renewal price is printed on the order page or the cart read 2026-11-07
  - stock: orderable: the cart renders the product config with billing cycles and no out-of-stock marker
  - cart_url: https://my.hosteons.com/store/budget-gigabit-ssd-kvm-vps-la-ny-jax-dal-and-lv/gigabit-kvm-vps-1
  - price_on_page: USD 21.00/yr on kvm_vps.php; the cart prices the same plan USD 21.00 annually
- evidence:
  - [1] 2026-10-22: 'Gigabit VPS 1' row quoted: '1 (Fair Share)', '1 GB', '10 GB', 'LINUX', '1', 'YES', '1 TB', 'Los Angeles, Salt Lake City, Portland, New York, Miami & Dallas', '$21/yr'
  - [2] 2026-10-22: 'RYZEN 512 MB' row quoted: '1 (3.5 Ghz+ Fair Share)', '512 MB', '10 GB NVME', '/64', '500 GB (@1 Gbit)', '$24/year'
  - [3] 2026-10-22: the stock clearance page lists Ryzen SP1 at 'From $3.00/mo', Ryzen SP2 at 'From $4.00/mo' and Ryzen SP3 at 'From $6.00/mo', each labelled 'Out of Stock'
  - [4] 2026-11-07: the cart prices Gigabit KVM VPS 1 at USD 21.00 annually, USD 40.00 biennially and USD 55.00 triennially, with no out-of-stock marker | capture: sha256:a11d0d60f23cb91507618f689eeab5ea4acfd07c3998f374d85cef4ac86ab757 | quote: $21.00 USD Annually $40.00 USD Biennially $55.00 USD Triennially
- sources:
  - [1] https://hosteons.com/kvm_vps.php
  - [2] https://hosteons.com/ryzen_premium_vps.php
  - [3] https://my.hosteons.com/store/ryzen-vps-special
  - [4] https://my.hosteons.com/store/budget-gigabit-ssd-kvm-vps-la-ny-jax-dal-and-lv/gigabit-kvm-vps-1

## HostEONS (Hybrid Server Special 1)

- `egress/hosteons-hybrid-server-special-1` | paid-only | evidence documented | binding volume-quota | category hybrid dedicated VPS | tier Hybrid Server Special 1
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.032Z (live) | stale on 2026-12-05
- url https://my.hosteons.com/store/hybrid-dedicated-server-special
- free tier: No free tier. Hybrid Server Special 1 is from USD 4.99 a month: 1 dedicated vCore (Ryzen 3950x), 4 GB RAM, 50 GB NVMe, 15 TB bandwidth, Salt Lake City. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The page prints no period for the 15 TB and no port speed.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 15 TB bandwidth on Special 1 and 30 TB on Specials 2 to 4, with no period, port speed or overage price on the page read. | metered: yes | free allowance: 15 TB, period not stated | source: [1]
- identity: email | detail: unverified: behind a sign-up. The registration page read shows only the store menu; its fields and the payment methods are not shown to a text read.
- interface: ssh
- limits:
  - volume-quota (binding): 15 TB bandwidth, period and port speed not stated [1]
- binding note: 15 TB is the only published number that can fail; the page states no port speed, no period and no fair-use clause.
- interface detail: A hybrid dedicated-CPU VPS in Salt Lake City; the page names no port or protocol filter.
- tooling: Any SSH client.
- composes with: 15 TB of bandwidth on a dedicated Ryzen core in Salt Lake City at USD 4.99 a month; the port speed is not stated on the page read.
- reliability: Special 3 of the same page is marked 'Out of Stock', so the specials sell out.
- notes: Cheapest of four hybrid specials: USD 4.99, 8.99, 11.99 and 16.99 a month, with 15 TB, 30 TB, 30 TB and 30 TB.
- evidence note: Price and allowance are quoted from the vendor's order page. Port speed, period and identity are not on the page read.
- extras:
  - location: Salt Lake City
- evidence:
  - [1] 2026-11-04: Hybrid Server Special 1 is from USD 4.99 a month | capture: sha256:f962dea20e119ab91375145fac6c95ee50157b3bab68eca7a3b5dd9ab97ea2fb | quote: Hybrid Server Special 1 Price From $4.99/mo
  - [1] 2026-11-04: Special 1 carries 15 TB of bandwidth | capture: sha256:f962dea20e119ab91375145fac6c95ee50157b3bab68eca7a3b5dd9ab97ea2fb | quote: BANDWIDTH 15 TB
  - [1] 2026-11-04: Special 1 has one dedicated Ryzen vCore | capture: sha256:f962dea20e119ab91375145fac6c95ee50157b3bab68eca7a3b5dd9ab97ea2fb | quote: Dedicated CPU 1 vCore (Ryzen 3950x)
  - [1] 2026-11-04: the page prices Special 3 at USD 11.99 a month and marks it out of stock | capture: sha256:f962dea20e119ab91375145fac6c95ee50157b3bab68eca7a3b5dd9ab97ea2fb | quote: Hybrid Server Special 3 Price From $11.99/mo
  - [2] 2026-11-04: the aggregator lists this plan at USD 4.99 a month with 15 TB in its VDS section | quote: ###### Hybrid Special 1
- sources:
  - [1] https://my.hosteons.com/store/hybrid-dedicated-server-special
  - [2] https://serverdeals.cc/
