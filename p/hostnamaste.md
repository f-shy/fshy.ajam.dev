# HostNamaste

> hostnamaste.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostnamaste/ | JSON https://fshy.ajam.dev/api/v1/entity/hostnamaste.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostNamaste (Compute)

- `compute/hostnamaste` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:33.037Z (live) | stale on 2026-12-08
- url https://www.hostnamaste.com/openvz-vps.php
- price parsed USD 3.49/mo
- free tier: OpenVZ-512 at USD 3.49/month: 1 CPU, 512 MB RAM plus 512 MB vSwap, 20 GB SSD, 1 TB bandwidth, SolusVM panel, 1 IPv4 and 1 IPv6, in Los Angeles, Dallas, Mumbai/Pune, Paris or Quebec. The page states "Plans starting at $3.49/Month", with the same plan at USD 10.47 quarterly, USD 20.94 semi-annually and USD 41.88 annually. The tracker lists a cheaper row, OpenVZ_256 at USD 2.00/month billed yearly (1 Intel core shared, 256 MB RAM, 10 GB HDD, 256 GB/month, 0.1 Gbps, Los Angeles) and states "starting at $24.00 per year", but no 256 MB plan appears anywhere on the vendor page read, so this record leads with the plan the vendor actually sells. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: bandwidth is a plan line item, 1 TB a month on OpenVZ-512, with no overage rate and no post-quota shaping policy published on the page read | metered: yes | free allowance: 1024 GB per month on OpenVZ-512 | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on OpenVZ-512 is about 33 GB a day, and the 256 MB tracker row carries 256 GB a month, which is 8.5 GB a day. [1]
- limits note: 1 TB a month on OpenVZ-512 is about 33 GB a day, and the 256 MB tracker row carries 256 GB a month, which is 8.5 GB a day.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: root OpenVZ container with a SolusVM panel and TUN/TAP/PPP enabled, so any client runs inside it and no wrapper is needed; the vendor documents no API on the page read. OpenVZ is container virtualisation, not KVM, so the kernel is shared and a custom kernel module will not load.
- composes with: At USD 41.88 a year this holds a public IPv4 with root and a SolusVM panel, which makes it a DNS secondary, a mail relay or a cron box; 512 MB of RAM and 20 GB of disk cannot hold a working set, and 1 TB a month moves control traffic only, so the data path belongs on a volume-quota host or an unmetered one.
- reliability: no reliability event recorded
- notes: The tracker and the vendor disagree on the floor: the tracker sells an OpenVZ_256 row at USD 2.00 a month, and the vendor's own OpenVZ page says plans start at USD 3.49 and lists no 256 MB plan. A record that led with USD 2.00 would have quoted a plan nobody could order from the page read. verification criteria: a read of the vendor's order form to confirm the 256 MB plan is withdrawn rather than filed under another product page, and the post-quota behaviour once 1 TB is spent.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 20
  - term: monthly USD 3.49, quarterly USD 10.47, semi-annually USD 20.94, annually USD 41.88
  - monthly_usd: 3.49
  - annual_usd: 41.88
  - renewal_usd: not published: no renewal price is printed on the order page or the cart
  - stock: orderable: the cart renders the product block (512 MB RAM, 15 GB RAID10, 1 TB bandwidth)
  - cart_url: https://www.hostnamaste.com/clients/cart.php?a=add&pid=43
- evidence:
  - [1] 2026-10-22: the plan block quoted: "HostNamaste OpenVZ VPS OpenVZ-512" / "$3.49/Month" / "1 x CPUs" / "512 MB Memory" / "512 MB vSwap" / "20 GB SSD Storage" / "1 TB Bandwidth" / "1 x IPv4 Address" / "1 x IPv6 Address"
  - [1] 2026-10-22: "Plans starting at $3.49/Month", and the ladder above it: OpenVZ-1024 $4.99/month, OpenVZ-1536 $6.99, OpenVZ-2048 $9.99, OpenVZ-3072 $14.99, each with quarterly, semi-annual and annual prices
  - [2] 2026-10-22: the tracker row quoted: "HostNamaste - $2.00 / month" / "yearly Service" / "cpu 1 Intel Cores (shared)" / "ram 256 MB RAM" / "disk 10 GB HDD" / "bandwidth 256 GB/month bandwidth" / "rj45 0.1 Gbps port speed" / "city Los Angeles California U.S.A.", under the line "starting at $24.00 per year"
  - [1] 2026-11-07: the OpenVZ page still states plans start at USD 3.49 a month | capture: sha256:98f65ea4b407db0ee439927a6ce9dabca457561bf87f8f87b720c183a111f1a6 | quote: Plans starting at $3.49/Month
- sources:
  - [1] https://www.hostnamaste.com/openvz-vps.php
  - [2] https://vpspricetracker.com/provider/HostNamaste/vps

## HostNamaste, KVM 1GB (Diwali annual)

- `egress/hostnamaste-kvm-1gb` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Los Angeles, KVM, IPv4 and IPv6) | tier KVM 1GB (Diwali annual)
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:42.856Z (live) | stale on 2026-12-04
- url https://www.hostnamaste.com/
- price USD 17.99 per year with 2TB/month included | parsed USD 0.7496/TB-mo
- free tier: No free tier. KVM 1GB is USD 17.99 a year (about USD 1.50 a month) on annual billing until 8 November 2026: 1 vCPU, 1 GB RAM, 20 GB NVMe, 2TB/month of bandwidth, Los Angeles. The standing KVM ladder starts at USD 3.99 a month (KVM-512: 512 MB, 15 GB SSD, 1 TB premium bandwidth, 1 IPv4 and 1 IPv6 address). | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a virtual server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 2TB/month on KVM 1GB and 1 TB/month on KVM-512, on a premium port of 1-10Gbps; extra bandwidth is sold at USD 2.00 a month per 1 TB. No overage rate and no post-allowance policy is published on the pages read. | metered: yes | free allowance: 2TB/month included in KVM 1GB | price per TB: USD 2.00 per 1 TB per month (KVM upgrade add-on) | source: [1]
- identity: email | detail: unverified: the client-area register page says an account is made by placing an order, and the order-form fields were not read; the pages list 'Multi Currency Payment Supported & Accepted' without naming a method.
- interface: ssh
- limits:
  - volume-quota (binding): 2TB/month on KVM 1GB [2]
- binding note: 2TB/month is the only published ceiling on KVM 1GB; the first failure for a high-volume job is the allowance, after which extra bandwidth is a USD 2.00 a month add-on per 1 TB.
- interface detail: Root SSH on a full KVM guest; SolusVM or Virtualizor panel on the standing ladder, a VPS control panel and Docker Manager on the Diwali plans.
- tooling: ssh, any VPN or tunnel daemon the guest kernel supports; the OpenVZ line states TUN/TAP/PPP.
- composes with: A KVM guest with one IPv4 and one IPv6 address per plan is a UDP-capable endpoint in Los Angeles; the pages read state no NAT, no port-forward count and no inbound filter, and no routed IPv6 prefix (one IPv6 address is listed).
- reliability: The annual price is a promotion that ends on 8 November 2026; the renewal price is not stated on the pages read.
- notes: Cheapest annual plan on the vendor page, with a standing monthly KVM ladder that includes an IPv6 address. Inbound port policy, NAT and IPv6 prefix size are not stated on any page read.
- evidence note: The price, the 2TB/month allowance and the IPv4 and IPv6 lines are vendor sentences read on 2026-11-03. Identity, the renewal price and whether the IPv6 line is one address or a prefix are not stated, so the record is not raised above documented for those fields.
- extras:
  - nat: not stated; the plan lists one IPv4 address
  - ipv6: one IPv6 address per KVM plan; routed prefix not stated
  - inbound: no inbound filter or port limit stated
  - udp: not stated; a KVM guest with root
- evidence:
  - [3] 2026-11-03: KVM 1GB is USD 17.99 a year with 1 vCPU, 1 GB RAM, 20 GB NVMe and 2 TB monthly bandwidth | capture: sha256:91dd6d3dc8d59b3df91a5b0f69c2b1a66373e58710c52c8f15f09786fd71ca53 | quote: | KVM 1GB | 1 | 1GB | 20GB | 2TB | $17.99/year |
  - [2] 2026-11-03: KVM 1GB at USD 17.99 a year on the vendor offer page, Los Angeles | capture: sha256:6b1bf990452a9b02ff28667d39a298df1c97996c17ff77355c79113abfe07085 | quote: $17.99/year
  - [2] 2026-11-03: the annual Diwali price is a promotion that ends on 8 November 2026 | capture: sha256:6b1bf990452a9b02ff28667d39a298df1c97996c17ff77355c79113abfe07085 | quote: Offer ends 8 November 2026
  - [2] 2026-11-03: the KVM 1GB plan lists 2TB/month of bandwidth | capture: sha256:6b1bf990452a9b02ff28667d39a298df1c97996c17ff77355c79113abfe07085 | quote: - 2TB/month
  - [4] 2026-11-03: the standing KVM ladder starts at USD 3.99 a month (KVM-512) | capture: sha256:67554fca6269a1d56f8dad62c756b9d9b2943153df93fc65ad16069fa4f30f65 | quote: ### Plans starting at $3.99/Month
  - [4] 2026-11-03: KVM-512 lists 1 TB of premium bandwidth | capture: sha256:67554fca6269a1d56f8dad62c756b9d9b2943153df93fc65ad16069fa4f30f65 | quote: - 1 TB Premium
  - [4] 2026-11-03: each KVM plan lists one IPv4 and one IPv6 address | capture: sha256:67554fca6269a1d56f8dad62c756b9d9b2943153df93fc65ad16069fa4f30f65 | quote: - 1 x IPv6 Address
  - [4] 2026-11-03: extra bandwidth on a KVM plan is USD 2.00 a month per 1 TB | capture: sha256:67554fca6269a1d56f8dad62c756b9d9b2943153df93fc65ad16069fa4f30f65 | quote: Bandwidth (Per 1 TB) - $2.00/Month
  - [4] 2026-11-03: the KVM plans are offered in five locations | capture: sha256:67554fca6269a1d56f8dad62c756b9d9b2943153df93fc65ad16069fa4f30f65 | quote: ### Los Angeles, CA, USA | Dallas, TX, USA | Quebec, Canada | Paris, France | Amsterdam, Netherlands
  - [5] 2026-11-03: the OpenVZ line advertises TUN/TAP/PPP, which a tunnel or VPN daemon needs | capture: sha256:98f65ea4b407db0ee439927a6ce9dabca457561bf87f8f87b720c183a111f1a6 | quote: ### Container-based Virtualization | SolusVM | TUN/TAP/PPP | USA, Canada, France, Europe, and India Locations | IP4s/IPv6s
  - [6] 2026-11-03: the client area has no stand-alone sign-up: the account is created at order | capture: sha256:74b3473eeda7bd4141d14a34aed6c9adb3e03a43297ea5f190c3a99dd1b116d3 | quote: place an order with us
- sources:
  - [1] https://www.hostnamaste.com/
  - [2] https://www.hostnamaste.com/special-offers.php
  - [3] https://lowendbox.com/blog/hostnamaste-diwali-2026-early-bird-special-los-angeles-kvm-vps-from-17-99-year/
  - [4] https://www.hostnamaste.com/kvm-vps.php
  - [5] https://www.hostnamaste.com/openvz-vps.php
  - [6] https://www.hostnamaste.com/clients/register.php
