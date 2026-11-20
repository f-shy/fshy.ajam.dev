# Axivora Cloud

> axivora.net | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/axivora/ | JSON https://fshy.ajam.dev/api/v1/entity/axivora.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Axivora Cloud

- `compute/axivora-mci-n-b-ipv6` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category IPv6-only VPS | tier MCI-N-B (IPv6 Only)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://store.axivora.net/products/MCI-IPv6-Only/mci-n-b
- free tier: No free tier. MCI-N-B is EUR 1.25 a month: 1 shared vCPU, 1024 MiB RAM, 20 GB HDD, 10 Gbps fair-use bandwidth, one dedicated IPv6 address (/128), IPv6 only. A second rung, MCI-N-C, is EUR 1.25 a quarter for 384 MiB and 5 GB. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: no retention statement is printed; the page instead carries 'No data safety guarantee - Please ensure your own backups' | source: [1]
- egress: 10 Gbps fair-use bandwidth with no byte allowance published | metered: no | free allowance: not published; 'Fair Use bandwidth' | source: [1]
- identity: email | detail: an account on store.axivora.net (a register link exists); the form itself was not read. No card hold is stated on any page read. Payment rails were not read.
- interface: ssh
- limits:
  - per-ip-shaping (binding): one IPv6 /128 per instance; no prefix, so a second address needs an additional instance [1]
  - volume-quota: '10 Gbps Fair Use bandwidth' with no byte figure and no published threshold [1]
- binding note: a single /128 is the hard ceiling: there is no routed prefix, so anything needing more than one address needs another instance.
- interface detail: an instance with one dedicated IPv6 address as a /128; there is no IPv4 at all and no NAT layer, so every port on that single address is reachable and nothing else is.
- tooling: any SSH client over IPv6; BGP is available up to 20 routes with downstream support after a ticket
- composes with: 1 GiB for EUR 1.25 a month is the second-best shape per dollar among evaluated providers, but a /128 rather than a prefix means the box has exactly one address to listen on.
- reliability: no reliability event observed; the vendor states 'No data safety guarantee - Please ensure your own backups'
- notes: The best RAM-per-euro among the rows whose cart can be found, and the only one that states the delivery form outright: a single /128. That is enough for a WireGuard endpoint or a monitor (one address, every port open) but it is not a routed prefix, so the 'every port on the guest's own address' advantage stops at one address. The caveats stack: no data-safety guarantee, no published traffic ceiling, no published payment rails, and an entity that the store does not name on any page reached. BGP up to 20 routes on a /128 is a routing-lab feature rather than a requirement. Not established: who operates Axivora, the registration and checkout fields, payment rails, card hold, and whether 'per quarter' on MCI-N-C is the minimum term for MCI-N-B too.
- evidence note: shape, the /128 statement, the fair-use bandwidth line, the two prices and the billing periods are quoted from the vendor's product page read. The cart is the product page itself: the 'Order Now' button is an anchor to the same product path and the add-to-cart is a Livewire action, so there is no GET cart URL to give a buyer.
- evidence:
  - [1] 2026-10-24: quoted: 'MCI-N-B (IPv6 Only) Starting at €1.25 per month ... 1 Shared vCPU ... 1024 MiB RAM ... 20 GB HDD ... 10000 Mbps (10Gbps) Fair Use bandwidth ... IPv6-only environment' and 'MCI-N-C (IPv6 Only) Starting at €1.25 per quarter ... 384 MiB RAM ... 5 GB HDD'
  - [1] 2026-10-24: quoted: 'Only IPv6 is supported; you cannot access any IPv4 internet.' and 'Each instance is assigned one dedicated IPv6 address (/128).' and 'No data safety guarantee - Please ensure your own backups'
  - [1] 2026-10-24: quoted BGP terms: 'Up to 20 BGP routes with downstream support' and 'A ticket must be submitted to enable the BGP session.'
  - [2] 2026-10-24: the cart page renders 'Your cart is empty' at 200, so the store is live; the add-to-cart itself is a Livewire wire:click action on the product page, not a link with a product id
- sources:
  - [1] https://store.axivora.net/products/MCI-IPv6-Only
  - [2] https://store.axivora.net/cart

## Axivora Cloud (AXIVORA CONNECT LTD)

- `compute/axivora-mci-n-c-ipv6` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category IPv6-only VPS | tier MCI-N-C (IPv6 Only)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://store.axivora.net/products/MCI-IPv6-Only
- price parsed USD 0.47/mo
- free tier: No free tier. MCI-N-C is EUR 1.25 billed quarterly on the group page, printed 'Starting at €1.25 per quarter'; the product page shows 'In stock' and the same EUR 1.25 without naming a cycle. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Quarterly prepay; the product page states 'No data safety guarantee — Please ensure your own backups'. No deletion interval after non-payment was published on the pages read. | source: [2]
- egress: no byte allowance: '10000 Mbps (10Gbps) Fair Use bandwidth', so the limit is a discretionary fair-use policy rather than a quota | metered: no | free allowance: unmetered under fair use at a 10 Gbps port | source: [2]
- identity: email | detail: email, first name, last name and password only. The registration form source carries exactly these fields plus a terms tick: email, first_name, last_name, password, password_confirm, tos. No card field, no phone field, no address field and no national ID field at registration. Whether a card is required at the payment step was not established, because the store was not taken to checkout.
- interface: ssh
- limits:
  - volume-quota: no byte allowance; 10 Gbps port under a fair-use policy, so the throttle is discretionary and has no published ceiling [2]
  - per-ip-shaping (binding): one dedicated IPv6 address as a /128, and no IPv4 at all: 'you cannot access any IPv4 internet' [2]
- binding note: a single /128 with no IPv4 means anything that needs to reach an IPv4-only host, including most package mirrors and most APIs, is unreachable without a NAT64 or proxy in front.
- interface detail: IPv6-only instance with one dedicated /128; up to 20 BGP routes available on a ticket
- tooling: any SSH client over IPv6; a web store with an account area; BGP session on request by ticket
- composes with: an IPv6-only box with a routed /128 and optional BGP at USD 0.47 a month, which is the cheapest genuinely IPv6-only machine among evaluated providers that is in stock and sold by a company that exists in a state register.
- reliability: The vendor states on the product itself 'No data safety guarantee — Please ensure your own backups'; the company was incorporated on 13 October 2025, so it is under a year old at the time of reading; no uptime figure published.
- notes: Companies House registration records distinguish AXIVORA LTD from the seller entity AXIVORA CONNECT LTD.
- evidence note: shape, price, the /128, the no-IPv4 rule, the fair-use bandwidth, the stock state and the registration fields are quoted from the vendor's own pages read; the legal entity, its status and its incorporation date are quoted from the Companies House record read. The billing cycle is the one soft field: the group page says 'per quarter' for this plan and 'per month' for the larger MCI-N-B, while the product page prints EUR 1.25 with no cycle. Both readings are recorded in the arithmetic.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.375
  - shape.disk_gib: 5
  - billing_model: quarterly
  - term: quarterly on the group-page reading
  - m10h_usd: 0.47
  - m24h_usd: 0.47
  - price_arithmetic: Two readings, both recorded. As quarterly: EUR 1.25 / 3 = EUR 0.4167 a month, / 0.89342 EUR per USD = USD 0.4664 a month, and EUR 1.25 = USD 1.3991 out of pocket every quarter. As monthly: EUR 1.25 / 0.89342 = USD 1.3991 a month. The group page states 'per quarter' for MCI-N-C and 'per month' for MCI-N-B, which is the reading used for the headline figure. Rate from api.frankfurter.app read 2026-10-24, rate date 2026-10-23. VPS billing: the machine bills whether it runs or not.
  - out_of_pocket_usd: 1.4
  - renewal_usd: same rate; no separate renewal price published
  - fx: EUR 0.89342 per USD, api.frankfurter.app/latest read 2026-10-24, rate date 2026-10-23
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: one dedicated IPv6 /128 with no port restriction stated; no IPv4 of any kind
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /128
  - udp: not stated explicitly, but a /128 with no port restriction and an offered BGP session implies all protocols; no page read says so in words
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not established: the store was not taken to checkout
  - card_hold: not stated on any page read
  - checkout_fields: email, first name, last name, password and a terms tick at registration; no card, phone, address or ID
  - stock: MCI-N-C reads 'In stock' on its product page on 2026-10-24; MCI-N-B reads 'is out of stock'
  - cart_url: https://store.axivora.net/products/MCI-IPv6-Only/mci-n-c
  - cart_works: unknown
  - product_url: https://store.axivora.net/products/MCI-IPv6-Only
  - signup_url: https://store.axivora.net/register
  - cart_url_note: the Order Now button targets the mci-n-c product page, which is the add-to-cart step; it was not taken to checkout, so the cart was never seen to price the line.
  - other_plans: MCI-N-B at EUR 1.25 per month: 1 shared vCPU, 1024 MiB RAM, 20 GB HDD, same /128 and 10 Gbps fair use, currently out of stock
  - why_this_row_matters: the only sub-USD-1.50 IPv6-only row whose seller appears in a state register under its trading name
- evidence:
  - [1] 2026-10-24: quoted group page: 'MCI-N-C (IPv6 Only) Starting at €1.25 per quarter' and 'MCI-N-B (IPv6 Only) Starting at €1.25 per month'
  - [2] 2026-10-24: quoted product summary: 'In stock MCI-N-C (IPv6 Only) €1.25' with '1 Shared vCPU', '384 MiB RAM', '5 GB HDD', '10000 Mbps (10Gbps) Fair Use bandwidth', 'IPv6-only environment'
  - [2] 2026-10-24: quoted notices: 'No data safety guarantee - Please ensure your own backups', 'Only IPv6 is supported; you cannot access any IPv4 internet', 'Each instance is assigned one dedicated IPv6 address (/128)', 'Up to 20 BGP routes with downstream support', 'A ticket must be submitted to enable the BGP session.'
  - [3] 2026-10-24: the larger plan is out of stock: 'Product MCI-N-B (IPv6 Only) is out of stock', for EUR 1.25 with 1024 MiB RAM and 20 GB HDD
  - [4] 2026-10-24: quoted: 'AXIVORA CONNECT LTD', 'Company status Active', 'Company type Private limited Company', 'Incorporated on 13 October 2025', with SIC '61100 - Wired telecommunications activities' and '63110 - Data processing, hosting and related activities'
  - [5] 2026-10-24: 
  - [6] 2026-10-24: the registration form source carries the fields email, first_name, last_name, password, password_confirm and tos, and no card, phone, address or ID field
  - [7] 2026-10-24: quoted: 'Axivora Connect LTD' in the page metadata, with 'Cloud VPS in Amsterdam (DC01/DC02) - Edge, Node, Flex and Archive series from €2.50/month. IPv4 /32 + IPv6 /128 on every plan'
  - [2] 2026-10-24: quoted notices: 'No data safety guarantee — Please ensure your own backups', 'Only IPv6 is supported; you cannot access any IPv4 internet', 'Each instance is assigned one dedicated IPv6 address (/128)', 'Up to 20 BGP routes with downstream support', 'A ticket must be submitted to enable the BGP session.'
  - [7] 2026-10-24: quoted: 'Axivora Connect LTD' in the page metadata, with 'Cloud VPS in Amsterdam (DC01/DC02) — Edge, Node, Flex and Archive series from €2.50/month. IPv4 /32 + IPv6 /128 on every plan'
- sources:
  - [1] https://store.axivora.net/products/MCI-IPv6-Only
  - [2] https://store.axivora.net/products/MCI-IPv6-Only/mci-n-c
  - [3] https://store.axivora.net/products/MCI-IPv6-Only/mci-n-b
  - [4] https://find-and-update.company-information.service.gov.uk/company/16780591
  - [5] https://find-and-update.company-information.service.gov.uk/search/companies?q=Axivora+Connect
  - [6] https://store.axivora.net/register
  - [7] https://axivora.net/
