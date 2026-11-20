# VDS6.NET

> vds6.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vds6/ | JSON https://fshy.ajam.dev/api/v1/entity/vds6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VDS6.NET (BREEZLE LLC)

- `compute/vds6-v6-1` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category IPv6-only VPS | tier V6-1
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:26:37.000Z (live) | stale on 2026-11-24
- url https://vds6.net/v6
- price parsed USD 0.49/mo
- free tier: No free tier. V6-1 is USD 0.49 a month: 1 CPU core, 2 GB RAM, 20 GB NVMe, one IPv6 address plus a /64, no IPv4 and no NATed IPv4, KVM. Billed yearly, so the shop prints USD 5.88 annually. The V6-2 rung doubles RAM and disk for USD 0.99 a month, USD 11.88 a year. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: yearly prepay; the shop lists orders, renewals, invoices and cancellation in the billing panel. No deletion grace period is printed on any page read. | source: [1]
- egress: the bandwidth table prints 'V6-1 - Not limited' and 'V6-2 - Not limited'; no byte figure and no shaping threshold is published | metered: no | free allowance: not limited, per the vendor's own table | source: [1]
- identity: email | detail: a billing-panel account; the order page and registration form were not reachable through the text extractor or the headless browser, so the fields are not read. No card hold is stated anywhere read. Payment is '3D Secure Credit Cards - Visa, MasterCard, etc.', Bitcoin and several altcoins, Alipay, and WebMoney Z / MIR cards per the vendor's knowledge base, so a debit card on the 3-D Secure rail should work.
- interface: ssh
- limits:
  - volume-quota: bandwidth 'Not limited' with no published threshold; the vendor reserves the right to act on abuse [1]
  - per-ip-shaping (binding): no IPv4 at all: 'These servers do not include IPv4 connectivity or NATed IPv4 access', so there is no port-forwarding layer and every port on the /64 is reachable [1]
  - pull-count: yearly prepay: USD 5.88 is the first payment, not USD 0.49 [2]
- binding note: IPv6-only is the constraint that decides the whole row: a WireGuard peer without IPv6 cannot reach it at all, and no IPv4 add-on is offered on this plan.
- interface detail: KVM guest with Linux install options from the billing panel; the plan carries a /64 as well as a single address, so a listener can bind any port on any address in the prefix. There is no IPv4 at all, and no NAT layer.
- tooling: any SSH client over IPv6; a host without IPv6 needs a tunnel or a dual-stack jump host to reach it, which the vendor does not supply
- composes with: 2 GB of RAM for USD 0.49 a month is the most memory per dollar found in the band, but it is reachable only over IPv6, so it is a WireGuard node where IPv6 is already in place, or a monitor that reports outward
- reliability: no reliability event observed; the vendor states the service has run 'since 2011' and operates AS210779; a LowEndTalk poster in 2026 called the merchant 'very new' and recommended monthly payments, which the yearly-only billing on this rung does not allow
- notes: The best shape per dollar in the band by a wide margin and the least usable of the cheap rows. 2 GB and 20 GB for USD 0.49 a month is four times the RAM of the next cheapest NAT row and 0.23 of the per-GiB price of the C-Servers row (USD 0.245 a GiB against USD 1.06), and because there is no NAT layer, every port on the /64 is reachable, so the port-mapping problem that governs the other NAT sellers does not exist here. The price is IPv6: no IPv4 address, no NATed IPv4, and the vendor offers no add-on, so a WireGuard peer on an IPv4-only access network cannot reach it. For the two stated uses that splits the row: as a health monitor that reports outward it is excellent, and as a WireGuard node it works only where IPv6 is already in place. Two things pull the confidence down. The stock count on the order page read '0 Available' for both rungs at the Poland datacenter, so the row is priced and documented but not demonstrably in stock today. And the entity needed correcting: the vendor names BREEZLE LLC of Brandon, Florida, but a Florida entity search returns no such company, while the RIPE organisation record for the AS the vendor claims gives 'reg-nr = 4921432 (Delaware)' - so the entity is a Delaware LLC mailing from a Florida address, the Florida register is the wrong place to look, and the Delaware number was not checked against the Delaware register in verification. That is a real entity with a real AS and a domain-age story, not the dissolved-company pattern this category was warned about, but it is also not a completed registry check. Not established: the registration form's fields, the payment gateway list at checkout, the renewal price after year one, and whether stock exists at any location.
- evidence note: price, shape, stock, the IPv6-only statement and the payment methods are quoted from pages read; the entity is a RIPE organisation record plus the vendor's own contact page, both read, and the Delaware registration number is the one RIPE holds, not a register lookup
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 20
  - billing_model: annual prepay
  - term: 12 months
  - m24h_usd: 0.49
  - m10h_usd: 0.49
  - price_arithmetic: USD 0.49 a month x 12 = USD 5.88 a year, which is the figure the shop prints. A VPS bills whether it runs or not, so the 24/7 and 10 h/day figures are the same. The V6-2 rung is USD 0.99 x 12 = USD 11.88.
  - out_of_pocket_usd: 5.88
  - first_payment_usd: 5.88
  - renewal_usd: not published; the tariff prints one monthly figure and the shop prints the matching annual total
  - stock: the order page read 'v6-1 0 Available' and 'v6-2 0 Available' at the Poland datacenter on 2026-10-24
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all ports on the /64; there is no IPv4 and no NAT forwarding layer
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - udp: not stated as such and none is needed: with no NAT layer, a UDP listener needs only the guest firewall open. Inferred from the architecture, not measured.
  - payment_rails: 3-D Secure cards (Visa, MasterCard), Bitcoin, Litecoin, BNB, Solana, BCH, Matic, Ethereum, Alipay, WebMoney Z and MIR cards
  - card_hold: not stated on any page read
  - checkout_fields: not read; the billing panel's registration form was not reachable through either route tried
  - nat_config: not applicable: there is no NAT layer
  - fx: no conversion used; every figure is quoted in USD
  - price_on_page: USD 5.88/yr
  - price_in_cart: USD 5.88/yr, but 0 available
  - cart_works: no
  - cart_url: https://my.vds6.net/store/v6-ipv6-vps-vds
  - signup_url: https://my.vds6.net/store/v6-ipv6-vps-vds
  - cart_evidence: store page renders 'v6-1 0 Available 1 CPUs 0 IPv4 and /64 IPv6 2 GB RAM 20 GB SSD/NVMe Fair Use Bandwidth Starting from $5.88 USD Annually'
  - needs_account_first: no
- evidence:
  - [1] 2026-10-24: quoted tariff table: 'CPU 1 Core | RAM 2 gb | Disk (NVMe SSD) 20 gb | IPs 1 IPv6 + 1 /64 IPV6 | Price (month) $0.49 | Order V6-1' and '1 core | 4 gb | 40 gb | 1 IPv6 + 1 /64 IPV6 | $0.99 | V6-2'
  - [1] 2026-10-24: quoted: 'These servers do not include IPv4 connectivity or NATed IPv4 access, so they are best for IPv6-ready applications, labs, and services.' and 'V6-1 - Not limited'
  - [2] 2026-10-24: read in a headless browser: 'IPv6 Only VDS/VPS | Datacenter Poland', 'v6-1 0 Available', '1 CPUs 0 IPv4 and /64 IPv6 2 GB RAM 20 GB SSD/NVMe Fair Use Bandwidth', 'Starting from $5.88 USD Annually' - so the annual price is USD 5.88 and the stock count reads zero
  - [3] 2026-10-24: quoted: 'VDS6.NET has provided affordable IPv4 and native IPv6 hosting since 2011. The service is operated by BREEZLE LLC from Brandon, Florida, with infrastructure in the USA, Italy, Poland, and the Netherlands.' and 'BREEZLE LLC 1032 E Brandon Blvd Suite 9798 Brandon, FL, USA'
  - [4] 2026-10-24: quoted: '3D Secure Credit Cards - Visa, MasterCard, etc.' and 'Bitcoin (BTC)' and 'Litecoin, BNB, Solana, BCH, Matic, Ethereum' and 'Alipay' and 'WebMoney Z / WMZ, Cards MIR'
  - [5] 2026-10-24: quoted RIPE organisation record: 'org-name = BREEZLE LLC', 'country = US', 'reg-nr = 4921432 (Delaware)', 'org-type = LIR', address '1032 E BRANDON BLVD, 33511, BRANDON, FL, UNITED STATES', created 2018-10-11
  - [6] 2026-10-24: quoted: 'as-name = BZL', 'org = ORG-BL346-RIPE', 'mnt-by = MNT-BREEZLE' - the AS the vendor claims is registered to the same organisation
  - [7] 2026-10-24: a Florida entity-name search for BREEZLE returns no BREEZLE LLC row, and the RIPE record names Delaware as the state of registration, so Florida is the wrong register for this entity and the search proves nothing either way
- sources:
  - [1] https://vds6.net/v6
  - [2] https://my.vds6.net/store/v6-ipv6-vps-vds
  - [3] https://vds6.net/contacts
  - [4] https://my.vds6.net/knowledgebase/1/What-payment-methods-do-you-accept.html
  - [5] https://rest.db.ripe.net/ripe/organisation/ORG-BL346-RIPE.json
  - [6] https://rest.db.ripe.net/ripe/aut-num/AS210779.json
  - [7] https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults?inquiryType=EntityName&searchTerm=BREEZLE
