# SiliconKiwi

> siliconkiwi.nz | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/siliconkiwi/ | JSON https://fshy.ajam.dev/api/v1/entity/siliconkiwi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SiliconKiwi (Compute)

- `compute/siliconkiwi` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:41.345Z (live) | stale on 2026-12-08
- url https://siliconkiwi.nz/vps
- free tier: Kiwi Go at NZD 8.00/month: 2 vCPU, 1 GB RAM, 20 GB storage, 1 TB bandwidth at full speed then unlimited at 2 Mbit/s, 100 Mbit/s port, Wellington New Zealand, free IPv4 and a free /64 IPv6 subnet. Kiwi Run is NZD 15.00 with 4 vCPU, 2 GB, 40 GB, 2 TB and a 200 Mbit/s port. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB included at the plan's port speed; past that the link continues at 2 Mbit/s with no overage charge, so a long transfer is slowed rather than billed | metered: no | free allowance: 1 TB per month at full speed | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 1 TB a month, after which the link continues at 2 Mbit/s instead of being billed, so the wall is throughput and not cost [1]
- limits note: 1 TB a month, after which the link continues at 2 Mbit/s instead of being billed, so the wall is throughput and not cost
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM on NZ-based Proxmox clusters, full root; automated backups, firewall management and monitoring are optional paid add-ons
- composes with: the endless 2 Mbit/s tail after 1 TB means a slow archive sync can run all month without a bill, which no other host among documented hosts offers
- reliability: no reliability event observed; past the 1 TB allowance the port is shaped to 2 Mbit/s by policy rather than suspended
- notes: The cart read 2026-11-07 prices Kiwi Go NZD 8.00 monthly and NZD 80.00 annually, which confirms the annual term the tracker divided into a monthly rate. Residence in New Zealand puts latency to Europe and the US at roughly a quarter second, which is the real cost of this row.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - monthly_nzd: 8.0
  - annual_nzd: 80.0
  - renewal_nzd: not published: the cart prices the monthly cycle at NZD 8.00 and no page names a renewal rate
  - stock: in stock: the cart priced the plan and accepted it
  - price_on_page: NZD 8.00/month (the plan card)
  - term: monthly and annual cycles in the cart
- evidence:
  - [1] 2026-10-22: 'VPS Kiwi Go, 8.00 NZD / month, vCPU 2, RAM 1 GB, Storage 20 GB, Bandwidth 1 TB Max Speed - Endless 2Mbps, Port 100 Mbps, Data Centre Wellington-X, Free IPv4, Free /64 IPv6 subnet' quoted from the plan card
  - [1] 2026-10-22: the page's embedded product data carries "price":"8.00", "priceCurrency":"NZD" for the same plan, which corroborates the card
  - [2] 2026-10-22: tracker row 'NZ$6.67 / month, yearly Service, 2 Intel Cores (shared), 1,024 MB RAM, 20 GB HDD, 1,024 GB/month bandwidth, 0.1 Gbps port speed, Wellington New Zealand', with the page header saying 'starting at NZ$80.00 per year'
  - [1] 2026-11-07: the cart prices Kiwi Go NZD 8.00 monthly and NZD 80.00 annually on 2026-11-07 | capture: sha256:039d2b1c73d5229e5dc8d673e92d2f581ff8710be3a28c03219f93b83f7d8121 | quote: <span class="product-price cycle-m">$8.00 NZD</span><span class="product-price cycle-a">$80.00 NZD</span>
  - [1] 2026-11-07: the plan card prices Kiwi Go at NZD 8.00 a month on 2026-11-07 | capture: sha256:95a27bb7046cc69565c9703f885a49389877c0b30da2f04fd97cada3dda6bb27 | quote: 8.00 NZD / month
- sources:
  - [1] https://siliconkiwi.nz/vps
  - [2] https://vpspricetracker.com/provider/SiliconKiwi/vps

## SiliconKiwi (Kiwi Go)

- `egress/siliconkiwi-kiwi-go` | paid-only | evidence documented | binding per-ip-shaping | category vps (hosted, Wellington New Zealand, KVM, IPv4 and IPv6) | tier Kiwi Go
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://siliconkiwi.nz/
- price NZD 8.00 per month with 1 TB per month included
- free tier: No free plan. Kiwi Go is NZD 8.00 a month: 2 vCPU, 1 GB RAM, 20 GB storage, 1 TB at full speed then an endless 2 Mbps, 100 Mbps port, a free IPv4 and a free /64 IPv6 subnet. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1 TB per month at up to 100 Mbps, then the link continues at 2 Mbps with no overage bill; the 100 Mbps port is a plan limit | metered: yes | free allowance: 1 TB per month at full speed on Kiwi Go, paid, no free tier | source: [1]
- identity: email | detail: the signup form lists an Organization and an Address 1 field marked required and an image captcha; the offer post names no payment methods and no card, phone or ID requirement is stated on a page read | country: New Zealand
- interface: ssh
- limits:
  - volume-quota: 1 TB per month at full speed on Kiwi Go [1]
  - per-ip-shaping (binding): after the allowance the link continues at 2 Mbps; the port is 100 Mbps [2]
- binding note: Past 1 TB a month the wall is a 2 Mbps throughput clamp and no bill; the 100 Mbps port binds before that.
- interface detail: a KVM guest on Proxmox with full root access, ordered in a HostBill portal
- tooling: any SSH client; the HostBill client portal
- composes with: a KVM guest with one IPv4 address and a /64 IPv6 subnet on a 100 Mbps port; after 1 TB the link continues at 2 Mbps, and no inbound-port policy is stated
- reliability: no reliability event recorded
- notes: Not free. A Wellington KVM plan on a 100 Mbps port; the price is in NZD and no conversion is made here.
- evidence note: Allowance, port and clamp are on the vendor's own page and restated by the offer post. Payment methods are not stated on a page read.
- extras:
  - nat: not stated; the plan lists a free IPv4 address and a /64 IPv6 subnet
  - ipv6: a free /64 IPv6 subnet
  - inbound: not stated
  - udp: not stated; a KVM guest with root
  - volume_stated: 1 TB Max Speed - Endless 2Mbps
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own address in Wellington
- evidence:
  - [1] 2026-11-04: the Kiwi Go bandwidth is 1 TB at full speed then 2 Mbps | capture: sha256:32b7c9a1f176f4f3e4e45f0fadd3f64d8fb12e98554b40470ed3e1722a7bdcb3 | quote: 1 TB Max Speed - Endless 2Mbps
  - [1] 2026-11-04: the plan includes a /64 IPv6 subnet | capture: sha256:32b7c9a1f176f4f3e4e45f0fadd3f64d8fb12e98554b40470ed3e1722a7bdcb3 | quote: Free /64 IPv6 subnet
  - [2] 2026-11-04: after the allowance the link continues at 2 Mbps | capture: sha256:1f960da2fc86c8f6e25e8c30a6f16e42aac3f2a84c8df8dd2be121b8c4c34e33 | quote: Listed port speeds are plan limits. After the included high-speed transfer allowance, connectivity continues at 2 Mbps.
  - [2] 2026-11-04: Kiwi Go is NZD 8.00 a month or NZD 80.00 a year | capture: sha256:1f960da2fc86c8f6e25e8c30a6f16e42aac3f2a84c8df8dd2be121b8c4c34e33 | quote: NZ$8.00/month or NZ$80.00/year
  - [3] 2026-11-04: the signup form requires an address | capture: sha256:1efe1ab56a6f15c04a73f7f4968217e30b9b1f39366509b6803743d1c5062890 | quote: Address 1 *
  - [3] 2026-11-04: the signup form carries an image captcha | capture: sha256:1efe1ab56a6f15c04a73f7f4968217e30b9b1f39366509b6803743d1c5062890 | quote: Type the characters you can see in the image below
- sources:
  - [1] https://siliconkiwi.nz/vps
  - [2] https://lowendbox.com/blog/siliconkiwi-brings-budget-vps-coolify-apps-and-s3-storage-to-wellington-new-zealand/
  - [3] https://hb.btit.nz/index.php?/signup/
