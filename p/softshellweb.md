# SoftShellWeb

> softshellweb.com | Compute, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/softshellweb/ | JSON https://fshy.ajam.dev/api/v1/entity/softshellweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SoftShellWeb (lxc ipv6 only)

- `compute/softshellweb-lxc-ipv6-only` | qualifies | evidence documented | binding volume-quota | category LXC VPS | tier LXC IPv6 Only
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T01:56:37.000Z (live) | stale on 2026-11-24
- url https://softshellweb.com/specials
- price parsed USD 0.83/mo
- disagrees on verdict: `compute/softshellweb` says paid-only, `compute/softshellweb-lxc-ipv6-only` says qualifies
- free tier: No free tier. The cheapest plan is USD 9.95 a year, described as 'Cheapest Los Angeles' and 'Works out to $0.83 / month'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: The container persists while the annual term is paid. A 7-day money-back guarantee is stated; there is no published deletion schedule for non-payment. | source: [1]
- egress: 750 GB a month at 10 Gbps on the 1 GB plan. The page states no throttle and no price after the allowance. | metered: yes | free allowance: 750 GB | source: [1]
- identity: email | detail: Self-service order with an email account and a $0 setup fee. The specials page read states no card hold and does not list accepted payment methods, so the card, PayPal or crypto routes are not established.
- interface: ssh
- limits:
  - volume-quota (binding): 750 GB a month of transfer on the 1 GB plan [1]
  - per-ip-shaping: no IPv4 at all on this plan; IPv4 is USD 24 a year extra, so any IPv4-only peer cannot reach it [1]
- binding note: 750 GB a month is the first hard number; the missing IPv4 is a reachability limit rather than a quota, and it fails on the first IPv4-only peer instead.
- interface detail: Root SSH into an LXC container; OS chosen at checkout from Debian, Ubuntu, AlmaLinux or Rocky.
- tooling: Any SSH client. LXC shares the host kernel, so no custom kernel and no wireguard module of your own.
- composes with: A 1 GB container with a routed /64 and 750 GB a month for USD 9.95 a year: an IPv6 WireGuard endpoint, a status page or a monitoring probe from a US West Coast address.
- reliability: LXC containers share the host kernel; the vendor says so plainly and prices accordingly. no suspension or data-loss event was observed.
- notes: The vendor advertises the IPv6-only line as suitable for 'tunnel endpoints' and 'monitoring probes', which is the category's use. A WireGuard listener on a public port therefore has a stated route over IPv6; an IPv4 peer needs the USD 24/yr address. Not measured: whether the host kernel exposes the wireguard module to the container.
- evidence note: Price, monthly equivalent, shape, traffic, IPv6 block, IPv4 surcharge and the annual billing term are all quoted from the vendor's specials page read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 15
  - billing_model: annual
  - term: 12 months
  - m24h_usd: 0.83
  - m10h_usd: 0.83
  - price_arithmetic: USD 9.95 a year / 12 = USD 0.8292 a month, which the vendor itself prints as '$0.83 / month'. Out of pocket at order: USD 9.95.
  - first_payment_usd: 9.95
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all, over IPv6 only
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - payment_methods: not established on the page read
  - session_cap.restart_required: no
  - session_cap.note: none; it is a container
  - payment_rails: PayPal, credit and debit cards, crypto via NOWPayments, Alipay, iDeal, UPI
- evidence:
  - [1] 2026-10-24: quoted: 'LXC IPv6 Only', '1 GB · 1 core · 15 GB NVMe', '$9.95/year', 'Works out to $0.83 / month'
  - [1] 2026-10-24: quoted: '750 GB @ 10 Gbps', '/64 IPv6 subnet', 'No IPv4 - add one for $24/yr'
  - [1] 2026-10-24: quoted: '$0 setup fee The annual price is the total due today.' and 'Billed once a year No monthly invoices to keep track of.'
  - [1] 2026-10-24: quoted: 'These are Linux containers (LXC), not full virtual machines. A container runs directly on the host's Linux kernel'
- sources:
  - [1] https://softshellweb.com/specials

## SoftShellWeb (compute/softshellweb)

- `compute/softshellweb` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:41.346Z (live) | stale on 2026-12-08
- url https://softshellweb.com/vps-hosting
- price parsed USD 5/mo
- disagrees on verdict: `compute/softshellweb` says paid-only, `compute/softshellweb-lxc-ipv6-only` says qualifies
- free tier: USD 5.00/month in Amsterdam: 1 core, 1 GB ECC RAM, 20 GB SSD, 1,000 GB at 1 Gbps, full root, KVM. The Los Angeles Ryzen entry is USD 9.00 with 2 GB DDR5, 50 GB NVMe and 5 TB at 10 Gbps. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1,000 GB per month on the Amsterdam entry plan; overage is not priced on the page read | metered: yes | free allowance: 1,000 GB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1,000 GB a month in Amsterdam; the 1 Gbps port exhausts that allowance in about three hours of saturation, so the byte cap bites long before the port [1]
- limits note: 1,000 GB a month in Amsterdam; the 1 Gbps port exhausts that allowance in about three hours of saturation, so the byte cap bites long before the port
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: Virtualizor panel with custom ISO upload and an HTML5 console, documented in the FAQ; no API mentioned
- composes with: the LA Ryzen row at USD 9 gives 5 TB on a 10 Gbps port, which is the better bytes-per-dollar plan here even though it is not the cheapest
- reliability: no reliability event observed; the FAQ states TCP and UDP ports 17, 19, 1900 and UDP 53413 and 11211 are permanently blocked and SMTP 25 is blocked by default pending a ticket
- notes: The cart read 2026-11-07 priced the plan USD 5.00 monthly and accepted it; the cart prices four unlabeled cycles (USD 5.00, 15.00, 30.00, 60.00).
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - monthly_usd: 5.0
  - annual_usd: not published: the cart prices four unlabeled cycles (USD 5.00, 15.00, 30.00, 60.00) and no page prints an annual total
  - renewal_usd: not published: no page names a renewal rate
  - stock: in stock: the cart priced the plan USD 5.00 monthly and accepted it
  - term: monthly, with three longer cycles priced in the cart
- evidence:
  - [1] 2026-10-22: Amsterdam table, first row: '1 Core, 1 GB ECC, 20 GB SSD, 1000 GB @ 1 Gbps, $5.00, Create', quoted from the pricing table
  - [2] 2026-10-22: Los Angeles table, first row: '1 Core, 2 GB DDR5, 50 GB NVMe, 5 TB @ 10 Gbps, $9.00'; the 16-core 64 GB row is USD 149.00
  - [3] 2026-10-22: tracker row 'USD 0.83 / month, yearly Service, 1 Intel Cores (shared), 1,024 MB RAM, 15 GB NVMe, 750 GB/month bandwidth, 10 Gbps port speed, Los Angeles', with 'starting at $9.95 per year'
  - [1] 2026-11-07: the pricing table prices the Amsterdam entry plan USD 5.00 monthly on 2026-11-07 | capture: sha256:3708f76c1c39fdd9e017b42f47e0dc8aca3c44a278a2ae5b6acf8f23736bc77e | quote: <div class="vps-col vps-col-price" data-label="Monthly">$5.00</div>
  - [4] 2026-11-07: the cart prices the pid 75 plan USD 5.00, 15.00, 30.00 and 60.00 across its cycles | capture: sha256:fe97d74ec0dac06e33dd5159f99984b7fbc4b8f39502a93522fb92d8ad94ba8b | quote: "prices": [ "$5.00", "$15.00", "$30.00", "$60.00",
- sources:
  - [1] https://softshellweb.com/vps-hosting
  - [2] https://softshellweb.com/vps-hosting-usa
  - [3] https://vpspricetracker.com/provider/SoftShellWeb/vps
  - [4] https://softshellweb.com/client/cart.php?a=add&pid=75

## SoftShellWeb (lxc ipv6 only la)

- `egress/softshellweb-lxc-ipv6-only-la` | paid-only | evidence documented | binding volume-quota | category vps (hosted, Los Angeles, LXC container, IPv6 only) | tier LXC IPv6 Only
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://softshellweb.com/
- price USD 9.95 per year with 750 GB per month included | parsed USD 1.11/TB-mo
- free tier: No free plan. LXC IPv6 Only is USD 9.95 a year: 1 GB RAM, 1 core, 15 GB NVMe, 750 GB at 10 Gbps, a /64 IPv6 subnet and no IPv4; an IPv4 address is USD 24 a year extra. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: 750 GB per month at 10 Gbps on the IPv6-only entry plan; past the allowance the account can be disabled or suspended until the next allotment or until bandwidth is bought or the plan upgraded | metered: yes | free allowance: 750 GB per month on the entry plan, paid, no free tier | source: [1]
- identity: email | detail: unverified: the order form was not read; the specials page lists PayPal, credit and debit cards, Bitcoin and crypto, Alipay, iDEAL and UPI as payment routes, and no card, phone or ID requirement is stated on a page read
- interface: ssh
- limits:
  - volume-quota (binding): 750 GB per month on the IPv6-only entry plan, then suspension until the next allotment or a purchase [2]
  - per-ip-shaping: no IPv4 address on this plan; IPv4 is USD 24 a year extra [1]
- binding note: 750 GB per month is the stated ceiling; the terms say the account can be disabled or suspended past it and give no overage price.
- interface detail: a Linux container with full root SSH access on a Debian, Ubuntu, AlmaLinux or Rocky template
- tooling: any SSH client; the provider's client portal
- composes with: a container sharing the host kernel with a routed /64 IPv6 subnet and no IPv4, so an IPv4-only peer cannot reach it unless the USD 24 a year address is added; no custom kernel modules and no port policy is stated
- reliability: no reliability event recorded
- notes: Not free. The cheapest container is IPv6 only at USD 9.95 a year with 750 GB a month; the IPv4 plans start at USD 17.95 a year with 1,500 GB.
- evidence note: Plan, price and allowance are on the vendor's specials page and the suspension rule is in its terms. Whether the host kernel exposes network modules to the container is not stated.
- extras:
  - nat: none stated; an IPv4 address is a paid extra, so the plan is reached over IPv6 only
  - ipv6: a routed /64 IPv6 subnet
  - inbound: not stated; no port filter on the pages read
  - udp: not stated
  - volume_stated: 750 GB @ 10 Gbps
  - bytes_transit: yes
  - transit_note: bytes leave from the container's own IPv6 address; IPv4-only peers are out of reach without the extra address
- evidence:
  - [1] 2026-11-04: the transfer allowances run from 750 GB to 10,000 GB by plan | capture: sha256:1b752f3dcafe562edb9281c19b7a35e73bf1058de90a54fa26521a8e80b8395c | quote: A 10 Gbps port on the US West Coast with generous transfer allowances — 750 GB to 10,000 GB depending on the plan.
  - [1] 2026-11-04: the entry container costs USD 9.95 a year | capture: sha256:1b752f3dcafe562edb9281c19b7a35e73bf1058de90a54fa26521a8e80b8395c | quote: which is how we can price a container at $9.95 a year
  - [1] 2026-11-04: the IPv6-only plans carry no IPv4 and an address costs USD 24 a year | capture: sha256:1b752f3dcafe562edb9281c19b7a35e73bf1058de90a54fa26521a8e80b8395c | quote: No IPv4 — add one for $24/yr
  - [1] 2026-11-04: payment routes include crypto | capture: sha256:1b752f3dcafe562edb9281c19b7a35e73bf1058de90a54fa26521a8e80b8395c | quote: PayPal Credit & debit cards Bitcoin & crypto Alipay iDEAL UPI + more local options
  - [2] 2026-11-04: past the allowance the account can be suspended until the next allotment | capture: sha256:1f32964a6b4979fb3f89dc2267886d5c3a3aa0f383215de8ffc3a467e8dc9c00 | quote: If your account exceeds the limit, SoftShellWeb reserves the right to disable or suspend the account until the start of next allotment or until more bandwidth is purchased at an added fee or the account is upgraded to a higher level plan.
- sources:
  - [1] https://softshellweb.com/specials
  - [2] https://softshellweb.com/terms
