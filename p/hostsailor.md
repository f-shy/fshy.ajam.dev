# HostSailor

> hostsailor.com | Compute, Egress and tunnels, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostsailor/ | JSON https://fshy.ajam.dev/api/v1/entity/hostsailor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostSailor (Compute)

- `compute/hostsailor` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://hostsailor.com/
- free tier: USD 17.96/year for the MINISAILOR NVMe VPS in Amsterdam after coupon SAVE70%, which the vendor describes as a 70 percent discount for life: 1 GB RAM, 1 GB vSwap, 1 core on an AMD EPYC 9534, 30 GB RAID10 NVMe, 1 TB bandwidth, 1 Gbps uplink, 1 IPv4 and a /64 IPv6, annual billing only. The same table prices 4 GB at USD 57.56/year, 6 GB at USD 82.76/year, 8 GB at USD 115.16/year and 16 GB at USD 183.56/year, with 4 TB, 6 TB, 8 TB and 12 TB of bandwidth. The coupon window closed on 31 August 2026; every figure in the table is a post-coupon figure and no list price is printed. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on the entry plan, 12 TB on the 16 GB plan; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 1 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 1 TB a month on the entry plan, rising to 12 TB on the 16 GB plan, so the counter binds before the 1 Gbps uplink on every row. No overage price and no post-allowance throttle are stated, and the post does not say whether the 1 TB is inbound-plus-outbound or outbound only. [1]
- limits note: 1 TB a month on the entry plan, rising to 12 TB on the 16 GB plan, so the counter binds before the 1 Gbps uplink on every row. No overage price and no post-allowance throttle are stated, and the post does not say whether the 1 TB is inbound-plus-outbound or outbound only.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the post names a SolusVM control panel and a looking glass at hostsailor.com/NLGDNLookingGlass; no API or CLI is documented on the pages read
- composes with: USD 17.96 a year for a 1 GB NVMe box in Amsterdam is the cheapest annual plan among evaluated providers and the discount is described as for life, so it is the record to re-read first if the coupon returns; 1 TB a month and a single core make it a DNS or monitor node, not a crawler.
- reliability: no reliability event recorded
- notes: json and storage/feral-hosting-radon match on the string for unrelated reasons. The offer window closed eleven days after the post was published, so the price is not orderable today as written, and the record is kept with that stated rather than dropped: a lifetime discount that recurs is exactly the sort of offer that comes back. verification criteria: whether SAVE70% reapplies at the next flash sale, and the pre-coupon list price, which no page read prints.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 30
- evidence:
  - [2] 2026-10-22: third-party offer post, published 2026-08-29, quoted from its table: 'MINISAILOR NVMe VPS RAM 1GB VSwap 1GB Cores 1 CPU: AMD EPYC 9534 RAID10 storage 30GB NVMe Bandwidth 1TB 1Gbps uplink ... Use Coupon: SAVE70% New Price after Discount: $17.96/year'; body text: '70% Discount for Life', 'Annual Billing only', 'Limited time, flash deal ... until August 31st'; datacenter 'Amsterdam, Netherlands'
  - [1] 2026-10-22: the vendor homepage was read and carries no VPS price table: the extracted page is a features and services page whose VPS section is prose ('Experience high-performance VPS hosting with fast NVMe storage and dedicated resources') with a cart link and no figures
  - [3] 2026-10-22: the path answers HTTP 200 and extracts to 133 bytes: the title, then the headings 'features', 'products' and 'testimonials' with no body text under any of them
  - [4] 2026-10-22: a second path on the same host extracts to 117 bytes of the same shape, so the plan tables are script-rendered on both
  - [1] 2026-10-22: the homepage carries web-hosting prices only ('yearlyPrice: $35.88', 'monthlyPrice: $2.99', 'yearlyPrice: $11.40', 'monthlyPrice: $2.45') and links no storage product
- sources:
  - [1] https://hostsailor.com/
  - [2] https://lowendbox.com/blog/flash-deal-hostsailors-70-lifetime-discount-is-on-until-august-31st-get-a-1gb-vps-for-less-than-18-year/
  - [3] https://hostsailor.com/storage-vps/
  - [4] https://hostsailor.com/vps/

## HostSailor (MINISAILOR NVMe VPS)

- `egress/hostsailor-minisailor` | paid-only | evidence reported | binding volume-quota | category vps (hosted, Amsterdam, KVM-class NVMe, one IPv4 plus an IPv6 /64) | tier MINISAILOR NVMe VPS
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.497Z (live) | stale on 2026-11-19
- url https://hostsailor.com/
- price USD 17.96 per year with 1 TB bandwidth included (coupon price, window closed)
- free tier: No free tier. MINISAILOR is USD 17.96 a year after coupon SAVE70% (annual billing only): 1 GB RAM, 1 GB vSwap, 1 core on an AMD EPYC 9534, 30 GB RAID10 NVMe, 1 TB bandwidth, a 1 Gbps uplink, one IPv4 and an IPv6 /64, in Amsterdam. The offer post says the coupon ran until August 31st; the list price now is unverified: the vendor pages carry no plan table in a plain read. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1 TB bandwidth on MINISAILOR (2 TB, 4 TB, 6 TB, 8 TB and 12 TB on the larger plans) at a 1 Gbps uplink. Overage price and post-allowance behaviour: not published in the pages read. | metered: yes | free allowance: 1 TB | source: [1]
- identity: email | detail: unverified: behind a sign-up. The post lists many payment options (PayPal, Bitcoin, Skrill, Samsung Pay, Western Union); no card, phone or ID requirement is stated in the pages read.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB bandwidth on MINISAILOR; overage rule not published [1]
- binding note: The 1 TB bandwidth line is the only stated limit; the overage rule is not published.
- interface detail: Root access on an NVMe VPS; the control panel was not read.
- tooling: ssh; the panel and the guest tooling were not read.
- composes with: One IPv4 and an IPv6 /64 on a 1 Gbps uplink; no NAT or port filter is stated. The post lists free DDoS protection.
- reliability: The USD 17.96 coupon window closed on 31 August 2026 per the offer post, so the entry price is unverified today; the vendor terms page returned no text in a plain read.
- notes: Amsterdam NVMe VPS with an IPv6 /64 per server. Entry price after the closed coupon is not read.
- evidence note: All values come from a third-party offer post; the vendor pages rendered no plan table or terms text.
- extras:
  - nat: none stated; one IPv4 is listed
  - ipv6: IPv6 /64 per server
  - inbound: not stated
  - udp: not stated
- evidence:
  - [1] 2026-11-04: MINISAILOR is USD 17.96 a year after the coupon with 1 TB bandwidth, a 1 Gbps uplink, one IPv4 and an IPv6 /64 | capture: sha256:6a5b302d21327d9c5db37f4e7fddda86b8ea16c7ad83d4d3e37ee744cd4f0a8e | quote: RAM 1GBVSwap 1GBCores 1CPU: AMD EPYC 9534RAID10 storage 30GB NVMeBandwidth 1TB1Gbps uplinkIPV4 Addresse(s) 1IPV6 Addresse(s) /64Use Coupon: SAVE70%New Price after Discount: $17.96/year
  - [1] 2026-11-04: the deal is annual billing only | capture: sha256:6a5b302d21327d9c5db37f4e7fddda86b8ea16c7ad83d4d3e37ee744cd4f0a8e | quote: Annual Billing only
  - [1] 2026-11-04: the post lists PayPal, Bitcoin, Skrill, Samsung Pay and Western Union among the payment options | capture: sha256:6a5b302d21327d9c5db37f4e7fddda86b8ea16c7ad83d4d3e37ee744cd4f0a8e | quote: 100+ Payment options (PayPal, Bitcoin, Skrill, Samsung Pay, Western Union & more)
  - [1] 2026-11-04: the deal is described as a lifetime discount | capture: sha256:6a5b302d21327d9c5db37f4e7fddda86b8ea16c7ad83d4d3e37ee744cd4f0a8e | quote: 70% Discount for Life
- sources:
  - [1] https://lowendbox.com/blog/flash-deal-hostsailors-70-lifetime-discount-is-on-until-august-31st-get-a-1gb-vps-for-less-than-18-year/

## hostsailor (Storage)

- `storage/hostsailor` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.hostsailor.com/seedbox.html
- free tier: none reachable: Site renders entirely client-side; /seedbox.html returned only the section headings ('features', 'products', 'testimonials') with no plan data, and the homepage is a JS spec sheet. No price | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Site renders entirely client-side; /seedbox.html returned only the section headings ('features', 'products', 'testimonials') with no plan data, and the homepage is a JS spec sheet. No price
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Site renders entirely client-side; /seedbox.html returned only the section headings ('features', 'products', 'testimonials') with no plan data, and the homepage is a JS spec sheet. No price
- sources:
  - [1] https://www.hostsailor.com/seedbox.html
