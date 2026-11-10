# Cloudnium

> cloudnium.net | Compute, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudnium/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudnium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloudnium LLC

- `compute/cloudnium-ipv6-1` | qualifies | evidence documented | binding volume-quota | category IPv6-only VPS | tier IPv6-1
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://portal.cloudnium.net/cart/dallas-ipv6-vps/
- disagrees on verdict: `compute/cloudnium` says paid-only, `compute/cloudnium-ipv6-1` says qualifies
- free tier: No free tier. IPv6-1 is USD 1.50 a month: 1 vCPU, 512 MB RAM, 10 GB disk, 1 TB/mo, 1 Gbps uplink, 1 IPv6 address, KVM. The ladder runs to IPv6-6 at USD 3.00 for 4 GB and 20 GB. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: monthly billing; the order page's billing-cycle selector offers 'Monthly' as the selected cycle. No deletion grace period is printed. | source: [1]
- egress: 1 TB/mo on IPv6-1, rising with the rung to 4 TB/mo on IPv6-5 and IPv6-6 | metered: yes | free allowance: 1 TB | source: [1]
- identity: email | detail: an account on portal.cloudnium.net with email and password; the forum offer states 'Please use real information and avoid VPN during checkout' and lists Credit Cards and Alipay as payment methods. No card hold is stated. The checkout form beyond the account login was not reached.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB/mo on IPv6-1 [1]
  - per-ip-shaping: 1 Gbps uplink included; 10 Gbps is a USD 10.00 a month option [1]
- binding note: 1 TB a month is the first ceiling, and because the plan documents a single IPv6 address rather than a prefix, a second service on the box has to share that one address.
- interface detail: KVM guest, OS templates from AlmaLinux 8/9, CentOS 7, Rocky 9, Debian 11/12, Ubuntu 20.04/22.04/24.04, FreeBSD 13 and Fedora 41. The plan delivers '1 IPv6 Address', not a stated prefix, so a routed /64 is not documented.
- tooling: any SSH client over IPv6; the order flow is a multi-step cart with an OS-template picker and a location picker
- composes with: the cheapest monthly-billed IPv6 row among evaluated providers, so the one to take if paying a year up front is the obstacle rather than the price.
- reliability: no reliability event observed; a LowEndTalk reply in the provider's own offer thread links two Chinese-language complaint posts, which is a third-party report and not verified here.
- notes: The only row among evaluated providers under USD 2 that bills monthly, which matters because it is the one a buyer can try for one month rather than a year. USD 1.50 for 512 MB and 1 TB is a worse shape per dollar than VDS6 at USD 0.49 for 2 GB, but VDS6 is annual-only and reads zero stock. The weakness is the network detail: the page says '1 IPv6 Address' and the knowledgebase says the address is 'generated from your control panel', which reads as an address out of a shared pool rather than a routed /64. For a WireGuard listener that is still enough (one address, all ports), but it is not a subnet. Not established: whether a /64 is available on request, the account fields past the login, any card hold, and stock per location.
- evidence note: the whole price ladder, the shapes, the billing cycle, the OS list and the '1 IPv6 Address' statement are read from the vendor's own order page. The payment methods are from the provider's LowEndTalk offer, which is first-party but a different channel. The cart URL is the location-specific order page the provider links, and it renders the product selector directly.
- evidence:
  - [1] 2026-10-24: quoted: 'IPv6-1 $1.50 USD / Monthly Processor Type Intel (E5-2699v4) Number of Cores 1 vCPU Memory 512MB RAM Storage 10 GB Bandwidth 1TB/mo. Uplink 1 Gbps Subnet/IP 1 IPv6 Address' and 'IPv6- 6 $3.00 USD / Monthly ... 4 GB RAM 20GB ... 4TB/mo.'
  - [1] 2026-10-24: quoted billing and totals: 'Change billing cycle $1.50 USD Monthly ... Total Recurring: $1.50 USD Monthly ... Total Due Today: $1.50 USD' - so the row is monthly billed, not annual prepay
  - [1] 2026-10-24: quoted option prices: 'Port Speed 1 Gbps / 10 Gbps ($10.00 USD Monthly)' and 'High availability (Auto failover) Disabled / Enabled ($1.00 USD Monthly)'
  - [2] 2026-10-24: provider's own offer post: 'Payment Methods: Credit Cards, Alipay' and 'Please use real information and avoid VPN during checkout', with cart links for Dallas, Buffalo, Seattle and Los Angeles
  - [3] 2026-10-24: quoted: 'Yes, we do provide IPV6 and its enabled by default. You can generate your IPV6 from your control panel.' - 'generate' suggests an address out of a pool, not a routed prefix
- sources:
  - [1] https://portal.cloudnium.net/cart/dallas-ipv6-vps/
  - [2] https://lowendtalk.com/discussion/211158/cloudnium-ipv6-only-vps-dallas-buffalo-seattle-los-angeles
  - [3] https://portal.cloudnium.net/knowledgebase/article/1/do-you-provide-ipv6-/

## Cloudnium (Compute)

- `compute/cloudnium` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:28.415Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Cloudnium/vps
- price parsed USD 1.5/mo
- disagrees on verdict: `compute/cloudnium` says paid-only, `compute/cloudnium-ipv6-1` says qualifies
- free tier: 1 vCPU (shared), 512 MB RAM, 10 GB SSD, 1,024 GB/month on a 1 Gbps port, IPv6 only with no IPv4 address, Dallas Texas, at USD 1.50/month. The tracker's info page marks the offer 'In stock now' and lists port 25 open by default, and it lists the same price in Buffalo New York and Seattle Washington. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read: the tracker states 1,024 GB/month and no overage term was read from the vendor | metered: yes | free allowance: 1,024 GB/month per the tracker | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 1,024 GB a month on a 1 Gbps port, and the plan has no IPv4 address, so every inbound client that is not IPv6-capable is out of reach until a tunnel or a proxy is added [1]
- limits note: 1,024 GB a month on a 1 Gbps port, and the plan has no IPv4 address, so every inbound client that is not IPv6-capable is out of reach until a tunnel or a proxy is added
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: the order path is a WHMCS store at portal.cloudnium.net with one category per city and per address family; the vendor site also documents a looking glass at lg.cloudnium.net and a status board on app.kubecore.net
- composes with: USD 1.50 for 512 MB and 1 TB of transfer is a cheap IPv6-only worker for outbound-only jobs such as a crawler leaf or a scheduler, and it needs a tunnel before anything can be served from it to the IPv4 internet
- reliability: no reliability event recorded
- notes: Confidence stays reported. Walls hit: https://cloudnium.net/ and https://cloudnium.net/hosting/vps both returned 200 with marketing text and no plan table; the store paths https://portal.cloudnium.net/index.php?rp=/store/vps, ?rp=/store/dallas-ipv6-vps and ?rp=/store/dallas-ipv6-vps/ each returned the same 85-line storefront shell with no prices, so the price list sits behind a category selection that did not resolve to a priced page. verification criteria: reading one category page in a browser to get the plan table from the vendor.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 10
  - monthly_usd: 1.5
  - annual_usd: not published: the cart prints a monthly cycle only
  - billing_term: monthly
  - in_stock: yes
  - renewal_usd: not published: no page read prints a renewal or month-13 sentence
- evidence:
  - [1] 2026-10-22: card row quoted: 'Cloudnium - $1.50 / month', '1 Intel Cores (shared)', '512 MB RAM', '10 GB SSD', '1,024 GB/month bandwidth', '1 Gbps port speed', 'IPv6', 'Dallas Texas U.S.A.'
  - [2] 2026-10-22: properties block: 'In stock now', 'IPv4' marked absent and 'IPv6' present, port 25 'Open by default', KVM
  - [3] 2026-10-22: the storefront lists categories 'Dallas, TX. - KVM VPS', 'Dallas IPV6 VPS', 'Buffalo, NY IPV6 VPS', 'Seattle IPV6 VPS', 'Los Angeles IPV6 VPS' and others, and prints no plan price on the index
  - [4] 2026-11-07: the cart prices IPv6-1 at USD 1.50 a month, recurring | capture: sha256:6ba42775025fc22b08304dd2bf61f3758ec53d98c8499ba863e0a2c817168b6f | quote: $1.50 USD
  - [4] 2026-11-07: the vendor's own cart prices IPv6-1 (1 vCPU, 512 MB RAM, 10 GB) at USD 1.50 a month recurring | capture: sha256:6ba42775025fc22b08304dd2bf61f3758ec53d98c8499ba863e0a2c817168b6f | quote: $1.50 USD
  - [4] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:6ba42775025fc22b08304dd2bf61f3758ec53d98c8499ba863e0a2c817168b6f | quote: $1.50 USD
- sources:
  - [1] https://vpspricetracker.com/provider/Cloudnium/vps
  - [2] https://vpspricetracker.com/info/209720/Cloudnium/
  - [3] https://portal.cloudnium.net/index.php?rp=/store
  - [4] https://portal.cloudnium.net/cart/dallas-ipv6-vps/

## Cloudnium (IPv6-1)

- `egress/cloudnium-ipv6-1` | paid-only | evidence reported | binding volume-quota | category IPv6-only VPS (Dallas) | tier IPv6-1
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:17.777Z (live) | stale on 2026-11-19
- url https://portal.cloudnium.net/cart/dallas-ipv6-vps/
- free tier: No free tier. IPv6-1 has 1 vCPU, 512MB RAM, 10 GB, 1TB/mo bandwidth, a 1 Gbps uplink and 1 IPv6 address; the aggregator lists it at USD 0.5 a month with 300 GB. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The vendor cart page prints no price; the aggregator figure of 300 GB differs from the vendor's 1TB/mo.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month on a 1 Gbps uplink per the vendor cart page; the aggregator lists 300 GB for the plan it calls IPv6 VPS-1; the vendor page is the more specific. | metered: yes | free allowance: 1 TB per month | source: [1]
- identity: email | detail: unverified: behind a sign-up. The client area login asks for an email address and a password.
- interface: ssh
- limits:
  - volume-quota (binding): 1TB/mo. [1]
- limits note: The aggregator lists 300 GB for the same name; unresolved.
- binding note: The cart page prints 1TB/mo. as the bandwidth line.
- interface detail: IPv6-only KVM VPS with one IPv6 address and no IPv4.
- tooling: Any SSH client over IPv6.
- composes with: One IPv6 address and no IPv4 address: reachable only from IPv6 clients; no port filter is published on the page read.
- reliability: unverified: stock of the plan was not read.
- notes: IPv6-only: no IPv4 address is included. A compute-topic record exists for the same plan.
- evidence note: Plan values are first-party; the price is an aggregator figure the cart page does not print.
- extras:
  - nat_ports: not applicable: IPv6 only
  - ipv6: 1 IPv6 address
  - udp_forwarding: unverified: not stated
  - routed_ipv6_prefix: unverified: a single address
  - inbound_ipv4_ports: not applicable: no IPv4
  - term: monthly
  - virtualization: KVM
- evidence:
  - [1] 2026-11-04: the IPv6-1 block lists 1TB/mo. of bandwidth | capture: sha256:8628b13a20647d8a20f804f3bffeb6097d35fe984e97fdec1923b2a1295107b6 | quote: 1TB/mo.
  - [1] 2026-11-04: the plan carries one IPv6 address | capture: sha256:8628b13a20647d8a20f804f3bffeb6097d35fe984e97fdec1923b2a1295107b6 | quote: 1 IPv6 Address
  - [2] 2026-11-04: the client area is behind a login with an email address and a password | capture: sha256:8c85fea3bc44db09b4dc9ba182186de3cd9b16abe573938473d0678bf16da631 | quote: Registered Clients Only
  - [3] 2026-11-04: serverdeals lists Cloudnium IPv6 VPS-1 at USD 0.5 a month | quote: #### USD 0.5 / month
- sources:
  - [1] https://portal.cloudnium.net/cart/dallas-ipv6-vps/
  - [2] https://portal.cloudnium.net/clientarea/
  - [3] https://serverdeals.cc/
