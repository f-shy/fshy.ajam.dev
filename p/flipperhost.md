# FlipperHost

> flipperhost.com | Compute, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flipperhost/ | JSON https://fshy.ajam.dev/api/v1/entity/flipperhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FlipperHost (Compute)

- `compute/flipperhost` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.flipperhost.com/
- free tier: USD 29.99/year for a 2 GB KVM VPS in Los Angeles or New York: 2 vCPU, 35 GB SSD, 5 TB monthly transfer, 1 Gbps port, 1 IPv4. The same table prices 4 GB at USD 59.99/year or USD 5.99/month (3 vCPU, 60 GB SSD, 8 TB), 6 GB at USD 79.99/year or USD 7.99/month (5 vCPU, 100 GB, 12 TB) and 8 GB at USD 99.99/year or USD 9.99/month (7 vCPU, 150 GB, 20 TB). The vendor's own homepage carries no 2 GB KVM row: its cheapest KVM-shaped entries are USD 9.99/month for 1 GB, 40 GB and 3 TB and USD 14.95/month for 2 GB, 60 GB and 6 TB, both on a 100 Mbps public uplink and both fully managed with cPanel included. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB a month on the 2 GB plan; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 5 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 5 TB a month on the 2 GB plan, 8 TB on the 4 GB, 12 TB on the 6 GB and 20 TB on the 8 GB, all stated per plan in the offer table. No overage price and no post-allowance throttle are stated, so what happens at the cap is unverified; the 1 Gbps port is a second wall behind the byte allowance. [1]
- limits note: 5 TB a month on the 2 GB plan, 8 TB on the 4 GB, 12 TB on the 6 GB and 20 TB on the 8 GB, all stated per plan in the offer table. No overage price and no post-allowance throttle are stated, so what happens at the cap is unverified; the 1 Gbps port is a second wall behind the byte allowance.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the homepage names a Virtualizor control panel and advertises cPanel/WHM on the VPS lines; no API or CLI is documented on the page read
- composes with: USD 29.99/year is USD 2.50/month for 2 GB and 35 GB of SSD with 5 TB of transfer, which is the cheapest per-year 2 GB offer among evaluated providers; the same host sells a fully managed 2 GB with cPanel at USD 14.95/month, so the promo line is the unmanaged one and the chaining decision is whether a managed panel is worth six times the price.
- reliability: no reliability event recorded
- notes: The record is reported because the headline annual price exists only in the offer post: the vendor homepage carries neither that SKU nor a list price to compare it with, so whether USD 29.99/year renews at USD 29.99 is unverified. verification criteria: the renewal rate on the promotions store, and whether the Atlanta location carries the same plans as Los Angeles and New York, since the post names all three but only the KVM table names two.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 35
- evidence:
  - [2] 2026-10-22: third-party offer post, published 2026-10-19, quoted from its table: '2 GB KVM VPS 2 vCPU Cores 35 GB SSD Storage 2 GB RAM 5 TB Monthly Transfer 1Gbps Network Port Full Root Access 1 IPv4 Address 29.99 USD/Year'; body text: '$29.99 gets you a full year of a 2GB VPS with 5TB transfer!'; the 4 GB row prints '59.99 USD/Year 5.99 USD/Month'
  - [1] 2026-10-22: the vendor homepage lists no 2 GB KVM plan at any term; its VPS blocks quote '$9.99/month ... 40GB RAID-10 Disk Space ... 1024 MB Dedicated RAM ... 3000 GB Premium Bandwidth ... 100Mbps Public Uplink' and '$14.95/month ... 60GB ... 2048 MB Dedicated RAM ... 6000 GB ... 2 X Dedicated CPU Cores'
- sources:
  - [1] https://www.flipperhost.com/
  - [2] https://lowendbox.com/blog/get-cheap-hosting-in-la-ny-or-atlanta-from-flipperhost-only-29-99-year-for-a-2gb-vps/

## FlipperHost (2 GB KVM)

- `egress/flipperhost-kvm-2gb` | paid-only | evidence reported | binding volume-quota | category vps (hosted, USA, one IPv4) | tier 2 GB KVM
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:43.137Z (live) | stale on 2026-11-18
- url https://www.flipperhost.com/
- price USD 29.99 per year for 5 TB per month | parsed USD 0.4998/TB-mo
- free tier: No free plan. The offer post lists a 2 GB KVM VPS in Los Angeles or New York at 29.99 USD a year with '5 TB Monthly Transfer', a 1 Gbps port and one IPv4 address. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 5 TB monthly transfer on the 2 GB KVM plan, 8 TB on the 4 GB plan, on a 1 Gbps port; behaviour past the quota is not stated on the pages read | metered: yes | free allowance: 5 TB per month on the 2 GB KVM plan, paid, no free tier | source: [1]
- identity: email | detail: unverified: the registration page read renders no form fields; the offer post lists credit cards, PayPal, Alipay and Bitcoin among the payment methods, and no card, phone or ID requirement is stated on a page read | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB per month on the 2 GB KVM plan [1]
- binding note: 5 TB per month is the only published ceiling, and it is stated by a third-party post, not by the vendor's own pages.
- interface detail: a KVM guest with full root access, ordered through the provider's billing store
- tooling: any SSH client; the provider's client area
- composes with: a plain KVM guest on one IPv4 address with no stated NAT, IPv6 or port policy; an IPv6 or routed-prefix hosted offer is a better fit where a prefix is needed
- reliability: no reliability event recorded
- notes: Not free, and a plain one-IPv4 guest: no NAT, no IPv6 and no inbound-port statement was found. Listed so the host has an egress record with its allowance, 5 TB per month, and the unknowns named.
- evidence note: Every figure is from a third-party offer post and no vendor page confirms the plan. Inbound ports, UDP and IPv6 are not stated on any page read.
- extras:
  - wg_path: unknown
  - wg_detail: a KVM guest with root access would run wg-quick natively; not stated by the vendor and not tried
  - ingress: unverified: one IPv4 address is stated; no page read lists open or blocked inbound ports or protocols
  - volume_stated: 5 TB Monthly Transfer
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own IPv4 address on the provider's network
- evidence:
  - [1] 2026-11-03: the 2 GB plan is 29.99 USD for a year with 5 TB of transfer | capture: sha256:d52e76558c6f45c0012f66070261d79446e36ca972830a630a16764e3cdf86b1 | quote: $29.99 gets you a full year of a 2GB VPS with 5TB transfer!
  - [1] 2026-11-03: the 2 GB KVM row lists 5 TB monthly transfer, a 1 Gbps port, root access and one IPv4 address | capture: sha256:d52e76558c6f45c0012f66070261d79446e36ca972830a630a16764e3cdf86b1 | quote: 2 GB KVM VPS2 vCPU Cores35 GB SSD Storage2 GB RAM5 TB Monthly Transfer1Gbps Network PortFull Root Access1 IPv4 Address29.99 USD/Year
  - [1] 2026-11-03: the payment methods include cards, PayPal, Alipay and Bitcoin | capture: sha256:d52e76558c6f45c0012f66070261d79446e36ca972830a630a16764e3cdf86b1 | quote: They accept 2Checkout, Paypal, Credit Cards (All Types), Alipay, Unionpay, Yandex.Money, Boleto Brasil, WebMoney, QIWI and Bitcoin.
- sources:
  - [1] https://lowendbox.com/blog/get-cheap-hosting-in-la-ny-or-atlanta-from-flipperhost-only-29-99-year-for-a-2gb-vps/

## FlipperHost (KVM Basic)

- `egress/flipperhost-kvm-basic` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Los Angeles, Miami, Dallas, Atlanta, Amsterdam, KVM) | tier KVM Basic
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:42.856Z (live) | stale on 2026-12-04
- url https://www.flipperhost.com/
- price USD 6.90 per month with 1000 GB/month included | parsed USD 6.9/TB-mo
- free tier: No free tier. The Basic KVM plan is USD 6.90 a month: 768 MB dedicated RAM, 25GB RAID-10 disk, 1000 GB premium bandwidth, 1 dedicated CPU core, 100Mbps public uplink, full root and SSH. A third-party post quotes a promotion of USD 29.99 a year for a 2 GB KVM VPS with 5 TB monthly transfer, a 1Gbps port and 1 IPv4 address, in Los Angeles and New York. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 1000 GB premium bandwidth on Basic at a 100Mbps public uplink; extra premium bandwidth is sold as add-ons from USD 1.00 per 1000 GB, and Unmetered is USD 10.00. | metered: yes | free allowance: 1000 GB/month included in Basic | price per TB: USD 1.00 per 1000 GB add-on | source: [1]
- identity: email | detail: unverified: the registration page rendered no field list. A third-party post lists 2Checkout, Paypal, Credit Cards, Alipay, Unionpay, Yandex.Money, Boleto Brasil, WebMoney, QIWI and Bitcoin as accepted payment methods.
- interface: ssh
- limits:
  - volume-quota (binding): 1000 GB/month on Basic [1]
  - per-ip-shaping: 100Mbps public uplink on Basic [1]
- binding note: 1000 GB/month is far below what a 100Mbps uplink can move in a month, so the allowance fails first.
- interface detail: SolusVM control panel and full root SSH on a KVM guest.
- tooling: ssh; any daemon the KVM guest supports.
- composes with: The vendor page read is a 100Mbps uplink with 1000 GB; the 1Gbps promotion is quoted only by a third party. IPv6 and inbound policy are not stated.
- reliability: The 2 GB promotion plan is quoted by a third-party post and was not found on the vendor pages read.
- notes: The vendor sells extra bandwidth per 1000 GB, a published marginal price per TB. The cheap promotion is not on the vendor page read.
- evidence note: The Basic plan price, bandwidth and uplink are vendor page lines read on 2026-11-03; the promotion is third-party. Identity, IPv6 and inbound policy are not stated.
- extras:
  - nat: not stated
  - ipv6: not stated
  - inbound: not stated
  - udp: not stated
- evidence:
  - [1] 2026-11-03: the Basic KVM plan is USD 6.90 a month | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: $6.90/month
  - [1] 2026-11-03: Basic lists 1000 GB premium bandwidth | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: - 1000 GB Premium Bandwidth
  - [1] 2026-11-03: Basic lists a 100 Mbps public uplink | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: - 100MbpsPublic Uplink
  - [1] 2026-11-03: the plan lists full root and SSH access | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: - Full Root / SSH Access
  - [1] 2026-11-03: the vendor sells 1000 GB of extra premium bandwidth at USD 1.00 | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: - 1000 GB $1.00
  - [1] 2026-11-03: the vendor sells an Unmetered bandwidth add-on at USD 10.00 | capture: sha256:6c5b48b65199db4bbfa30bec39aa277d62c8c9fab87b52c7ba4c276aec915018 | quote: - Unmetered $10.00
  - [2] 2026-11-03: the vendor lists five datacenter locations including Amsterdam | capture: sha256:5a517915e7e757f9de6699527b04d4957535109fe53c52de132e92cb29d67763 | quote: - Amsterdam NEW!
  - [3] 2026-11-03: the promotion is USD 29.99 a year for a 2 GB VPS with 5 TB transfer | capture: sha256:d52e76558c6f45c0012f66070261d79446e36ca972830a630a16764e3cdf86b1 | quote: $29.99 gets you a full year of a 2GB VPS with 5TB transfer!
  - [3] 2026-11-03: payment methods accepted | capture: sha256:d52e76558c6f45c0012f66070261d79446e36ca972830a630a16764e3cdf86b1 | quote: They accept 2Checkout, Paypal, Credit Cards (All Types), Alipay, Unionpay, Yandex.Money, Boleto Brasil, WebMoney, QIWI and Bitcoin.
  - [4] 2026-11-03: the registration page rendered no field list | capture: sha256:13c3439cef160175bd94844931c7b9722bd35be6ea59e5db13b13acf31154e28 | quote: Register Create an account with us . . .
- sources:
  - [1] https://www.flipperhost.com/kvm-vps.php
  - [2] https://www.flipperhost.com/
  - [3] https://lowendbox.com/blog/get-cheap-hosting-in-la-ny-or-atlanta-from-flipperhost-only-29-99-year-for-a-2gb-vps/
  - [4] https://www.flipperhost.com/billing/register.php
