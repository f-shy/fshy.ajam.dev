# VPS_Panda

> vpspanda.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpspanda/ | JSON https://fshy.ajam.dev/api/v1/entity/vpspanda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPS_Panda

- `compute/vps-panda` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T17:40:47.147Z (live) | stale on 2026-12-08
- url https://vpspanda.com/pricing
- price parsed USD 4.5/mo
- free tier: KVM-1G at USD 4.50 per month (store: 'Starting from $4.50 USD Monthly'): 1 vCore, 1 GB RAM, 15 GB NVMe, 2 TB bandwidth, in Phoenix US or Dhaka Bangladesh at USD 0.00 location fee. Order page read 2026-11-07: monthly USD 4.50, quarterly USD 13.50, semi-annually USD 27.00, annually USD 54.00, biennially USD 108.00, triennially USD 162.00; no setup fee; renewal price not published; plan in stock (the configuration summary totals USD 4.50 due today). The marketing page read 2026-10-22 printed a struck list price beside a lower per-month figure at the annual cycle; that lower figure appears on no store or order page read 2026-11-07, where the annual term costs exactly twelve times the monthly price. KVM-2G sits above it (prices in the record's evidence rows). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month included on the entry plan; no overage price stated on the page read | metered: yes | free allowance: 2 TB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month on a 1 Gbps port. The disk is 15 GB, the smallest among documented hosts, so the plan is a front end and not a store. [1]
- limits note: 2 TB a month on a 1 Gbps port. The disk is 15 GB, the smallest among documented hosts, so the plan is a front end and not a store.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a client area at cloud.vpspanda.com is linked; no API or client is documented on the page read
- composes with: the Dhaka location is the unusual part: USD 4.50 for a Bangladesh-facing box is cheap latency to a South Asian audience, and the 2 TB allowance covers a small API or mirror without touching the storage budget
- reliability: no reliability event recorded
- notes: The marketing page read 2026-10-22 printed a struck list price beside a lower per-month figure at the annual cycle, and a tracker row shows the list price; the order page read 2026-11-07 shows the annual term at exactly twelve times the monthly price, no discount, and the lower figure appears on no store or order page read that day. The cart shows the monthly price with no setup fee. The tracker's list price agrees with the store.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - price_on_page: USD 4.50/month for KVM-1G
  - renewal_usd: not published: the order page prices six billing cycles and prints no renewal price
- evidence:
  - [1] 2026-10-22: Basic Plans card: '1 vCore / 1 GB RAM / 15 GB NVMe / 2 TB Bandwidth' with '$4.5' carrying class 'line-through' beside '$4.05/mo'
  - [1] 2026-10-22: billing cycle control: '1 Month', '12 Month' marked '10% Off' and 'checked', with '24 Month' and '36 Month' following, so the USD 4.05 is the 12-month prepay and USD 4.50 the monthly list
  - [2] 2026-10-22: tracker shows the list price: '$4.50 / month 1 Intel Cores (shared) 1,024 MB RAM 15 GB NVMe 2,048 GB/month bandwidth 1 Gbps port speed IPv4' in the U.S.A. and Dhaka
  - [3] 2026-11-07: the order page prints six billing cycles for KVM-1G, the annual term at USD 54.00 | capture: sha256:7df14fc09bfe26de2e42932c37b340381d0ab2a1f22b4608e2caf90d8f20f431 | quote: Monthly $4.50 USD Quarterly $13.50 USD Semi-Annually $27.00 USD Annually $54.00 USD Biennially $108.00 USD Triennially $162.00 USD
  - [3] 2026-11-07: the configuration summary names the due-today total, USD 4.50 in the same block | capture: sha256:7df14fc09bfe26de2e42932c37b340381d0ab2a1f22b4608e2caf90d8f20f431 | quote: Configuration Total Due Today
  - [4] 2026-11-07: the store index prices KVM-1G from USD 4.50 monthly | capture: sha256:b8d8618c4eb4c5cc3b3615b58cf06c171c40d86016305008cfbcdeaa81f3a44e | quote: KVM-1G Starting from $4.50 USD Monthly
  - [4] 2026-11-07: the store index states 2 TB bandwidth for KVM-1G | capture: sha256:b8d8618c4eb4c5cc3b3615b58cf06c171c40d86016305008cfbcdeaa81f3a44e | quote: **2 **TB Bandwidth
  - [3] 2026-11-07: the cart-side annual price contradicts the lower per-month figure the earlier notes described | capture: sha256:7df14fc09bfe26de2e42932c37b340381d0ab2a1f22b4608e2caf90d8f20f431 | quote: Annually $54.00 USD
  - [4] 2026-11-07: the entry plan price is unchanged on the store index | capture: sha256:b8d8618c4eb4c5cc3b3615b58cf06c171c40d86016305008cfbcdeaa81f3a44e | quote: KVM-1G Starting from $4.50 USD Monthly
- sources:
  - [1] https://vpspanda.com/pricing
  - [2] https://vpspricetracker.com/provider/VPS_Panda/vps
  - [3] https://cloud.vpspanda.com/store/basic-vps/kvm-1g
  - [4] https://cloud.vpspanda.com/store
