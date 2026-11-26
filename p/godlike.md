# Godlike.Host

> godlike.host | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/godlike/ | JSON https://fshy.ajam.dev/api/v1/entity/godlike.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Godlike.Host (Compute)

- `compute/godlike-host` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:43.797Z (live) | stale on 2026-12-08
- url https://godlike.host/leb-offer-vps/
- free tier: USD 2.00/month for Nitro 1 on a 1 Gbps port, printed on the vendor's own LEB page against a struck-through USD 4.00: 1 vCPU on an AMD EPYC 75F3, 2 GB RAM, 30 GB NVMe. The Nitro ladder continues: Nitro 2 USD 4.00 (2 vCPU, 4 GB, 50 GB), Nitro 3 USD 8.00 (4 vCPU, 8 GB, 100 GB), Nitro 4 USD 16.00 (8 vCPU, 16 GB, 200 GB), Nitro 5 USD 32.00 (12 vCPU, 32 GB, 400 GB); the Ryzen 9 9950X3D line is USD 2.50/month for Ultra 1 (1 vCPU, 2 GB, 30 GB), USD 5.00 for Ultra 2, USD 10.00 for Ultra 3, USD 20.00 for Ultra 4 and USD 40.00 for Ultra 5 (same shapes). The page prints monthly prices only and no annual or renewal price; the offer post's annual figures are third-party and not carried here. The Deploy buttons do not open the VirtFusion panel: each plan's button carries its own cart link at godlike.host/cart-vps with productId, billingCycle=monthly, the LEB50 promo and a 50 discount; the cart page renders for an anonymous visitor and loads its prices with a script call this toolchain cannot make (a POST to the site's own preinstall API; the WHMCS order form for the plan answers 200 with no price in its static HTML), so the cart's own prices are unverified: behind a script. No sold-out marker and no coming-soon flag on any of the ten plan cards. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB of outbound transfer a month, stated on the LEB page beside 'Unmetered Inbound Traffic'; no overage price is printed | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): no monthly byte allowance appears on either page read, so nothing volume-shaped is binding: the 1 Gbps port is the only stated limit and throughput is therefore the wall. That is an inference from the plan card, which prints 'Network 1 Gbps' and no traffic figure, and not a vendor statement about shaping. [1]
- limits note: no monthly byte allowance appears on either page read, so nothing volume-shaped is binding: the 1 Gbps port is the only stated limit and throughput is therefore the wall. That is an inference from the plan card, which prints 'Network 1 Gbps' and no traffic figure, and not a vendor statement about shaping.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor page names a VirtFusion control panel and one-click backups; no API, rclone backend or CLI is documented on the page read
- composes with: USD 2.00/month for 2 GB and 30 GB on an EPYC 75F3 with a 1 Gbps port is one of the lowest 2 GB rates among evaluated providers, and Los Angeles plus New Jersey plus Amsterdam on one account makes it a candidate for a small always-on worker near the bytes it fetches; the missing traffic figure is the reason to test before committing a crawler to it.
- reliability: no reliability event recorded
- notes: verification criteria: whether the USD 2.00/month card price renews at USD 2.00 or reverts to the struck USD 4.00, and whether any monthly transfer allowance exists at all. The two pages disagree on the annual arithmetic: USD 1.83 x 12 is not USD 21.99 and USD 2.00 x 12 is USD 24.00, so the card and the post are pricing different billing terms and only the post says which. The offer post prints no bandwidth row, so the record carries no allowance rather than a guessed one.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 30
- evidence:
  - [1] 2026-10-22: plan cards quoted: 'Nitro 1', '$4.00 $2.00 / mon', 'RAM 2 GB', 'vCPU 1 core', 'SSD (NVMe) 30 GB', 'Network 1 Gbps'; 'Nitro 2' at '$8.00 $4.00 / mon' with '4 GB' and '2 core'; the page header reads 'Standard Epyc 75F3 | 64 Cores | 2.95 GHz' and 'Highest Ryzen 9 9950x3D | 16 Cores | 4.3 GHz'
  - [2] 2026-10-22: third-party offer post, published 2026-10-10, quoted from its table: 'Nitro 1 ... 1 vCPU 2GB RAM 30GB NVMe Standard price: $87.96/year LEB price: $43.99/year LEB first year price: $21.99 Coupon Code: LEB50'; body text: 'Get a 2GB VPS for only $1.83/month on annual contract for the first year, and $3.67/month on annual after that'; test IPs given for 'Los Angeles', 'New Jersey' and 'Amsterdam'
  - [1] 2026-11-07: the LEB page renders Nitro 1 at USD 2.00 per month against a struck USD 4.00 | capture: sha256:08253a0bf51a8033a13b43baa14141b46f6ffdc2d7ce0eda57fbf1ed0899ab70 | quote: $4.00$2.00/ mon
  - [1] 2026-11-07: the LEB offer page prints a 5 TB monthly outbound allowance | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: 5 TB outbound per month
  - [1] 2026-11-07: the LEB page's plan cards re-read on 2026-11-07 at the same prices | capture: sha256:08253a0bf51a8033a13b43baa14141b46f6ffdc2d7ce0eda57fbf1ed0899ab70 | quote: $4.00$2.00/ mon
  - probe:https://panel.godlike.host/ 2026-11-07: the VirtFusion panel at panel.godlike.host answers a 4.6 kB login page, so the cart's term prices sit behind a login | capture: sha256:5db3dbd8a583df33197e77d2360a9495de93af72d859508a4119138057ae29f8 | quote: "status": 200
  - [1] 2026-11-07: the LEB page prices Nitro 1 at USD 2.00 a month against a struck USD 4.00 | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: $4.00 $2.00 / mon
  - [1] 2026-11-07: the page re-states the 5 TB monthly outbound allowance with unmetered inbound | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: 5 TB outbound per month
- sources:
  - [1] https://godlike.host/leb-offer-vps/
  - [2] https://lowendbox.com/blog/exclusive-lowendbox-pricing-2gb-kvm-vps-for-1-83-month-first-year-godlike-host-is-back/

## Godlike.Host (Nitro 1)

- `egress/godlike-host-nitro-1` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Los Angeles, New Jersey, Amsterdam, KVM) | tier Nitro 1
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://godlike.host/
- price USD 2.00 per month with 5 TB outbound per month
- free tier: No free plan. Nitro 1 (2 GB RAM, 1 vCPU, 30 GB NVMe, 1 Gbps) is USD 2.00 a month on the vendor page against a struck USD 4.00; the offer post prices the same plan at USD 1.83 a month on an annual term for the first year and USD 3.67 after. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: unmetered inbound traffic and 5 TB outbound per month on a 1 Gbps port; behaviour past the 5 TB is not stated on the pages read | metered: yes | free allowance: 5 TB outbound per month, paid, no free tier | source: [1]
- identity: email | detail: unverified: the signup form was not read; the terms list bank cards, Apple Pay, Google Pay, PayPal, Stripe and cryptocurrency via CoinPayments as payment methods, and no card, phone or ID requirement is stated on a page read
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB outbound per month, inbound unmetered [1]
  - per-ip-shaping: 1 Gbps port on every Nitro and Ultra plan [1]
- binding note: 5 TB outbound per month is the only published ceiling and no post-allowance behaviour is stated.
- interface detail: a KVM guest managed in the VirtFusion panel with one-click backups
- tooling: any SSH client; the VirtFusion control panel
- composes with: a plain KVM guest on a 1 Gbps port with unmetered inbound traffic; no NAT, IPv6 or port policy is stated on the pages read
- reliability: no reliability event recorded
- notes: Not free. A 2 GB plan on a 1 Gbps port with 5 TB outbound a month included; no NAT or inbound-port policy is stated.
- evidence note: The 5 TB outbound figure and the 1 Gbps port are on the vendor's own plan page; the first-year price is from a third-party offer post and the two pages price the plan differently. Ports, UDP and IPv6 are not stated.
- extras:
  - nat: not stated
  - ipv6: not stated on the pages read
  - inbound: unmetered inbound traffic; no port filter stated
  - udp: not stated; a KVM guest
  - volume_stated: 5 TB outbound per month
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own address on the provider's network
- evidence:
  - [1] 2026-11-04: the plan page includes 5 TB outbound per month | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: 5 TB outbound per month
  - [1] 2026-11-04: inbound traffic is unmetered | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: Unmetered Inbound Traffic
  - [1] 2026-11-04: Nitro 1 is USD 2.00 a month against a struck USD 4.00 | capture: sha256:0092d2d806e3da492c882369896fea88bd0c08a785fa765a284a371de801b0d0 | quote: $4.00 $2.00 / mon
  - [2] 2026-11-04: the offer post prices a 2 GB Epyc VPS at USD 1.83 a month for the first annual year | capture: sha256:41520ddd5479cf419deba52a6484931cc3426a9040f4c914667004ca7c66bc9e | quote: Get a 2GB VPS for only $1.83/month on annual contract for the first year, and $3.67/month on annual after that!
  - [3] 2026-11-04: payment methods include crypto | capture: sha256:74649ec19668e32c32319eab835eba9e03a9f2fbbf533c6eac3ab12ba9ee5cd1 | quote: The Provider supports the following methods of payment for adding funds: bank cards (Visa, MasterCard), Apple Pay, Google Pay, payment providers PayPal and Stripe, cryptocurrencies via the CoinPayments service
- sources:
  - [1] https://godlike.host/leb-offer-vps/
  - [2] https://lowendbox.com/blog/exclusive-lowendbox-pricing-2gb-kvm-vps-for-1-83-month-first-year-godlike-host-is-back/
  - [3] https://godlike.host/terms
