# Server Mikro

> servermikro.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/servermikro/ | JSON https://fshy.ajam.dev/api/v1/entity/servermikro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Server Mikro

- `compute/servermikro-nat-lxc-1gb` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS | tier VPS NAT LXC 1gb ram
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:20:00.000Z (live) | stale on 2026-11-24
- url https://my.servermikro.com/products/vps-nat-lxc/vps-nat-lxc-1gb-ram
- price parsed USD 0.5541/mo
- free tier: No free tier. VPS NAT LXC 1gb ram is Rp10.000,00 a month for 1 vCPU, 1 GB RAM, 512 MB swap, 10 GB SSD, LXC, shared IPv4 with 4 forwarded ports, unlimited bandwidth at 300 Mbps, in Beauharnois, Canada. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the container persists for the paid month; the store prints no deletion schedule and no refund term | source: [1]
- egress: 'Unlimited Bandwidth (300 Mbps)' on the plan body, i.e. a port cap rather than a byte allowance; no overage price is printed because there is no meter | metered: no | free allowance: unlimited at 300 Mbps | source: [1]
- identity: email | detail: no card hold and no payment method is printed on the product page or the checkout page read; checkout is a Laravel/Livewire cart that requires an account, and the rails are unverified
- interface: ssh
- limits:
  - per-ip-shaping (binding): shared IPv4 with 4 forwarded ports; a dedicated IPv4 is sold as an option at Rp50.000,00 [1]
  - request-rate: 300 Mbps port; unlimited bytes [1]
- binding note: 4 forwarded ports is the smallest port block among documented hosts and the first thing that fails: a WireGuard listener, SSH and one web port already use three of the four.
- interface detail: LXC container with root; the store prints no control panel, and Docker is explicitly unsupported on this plan
- tooling: any SSH client; the vendor provisions in 10-30 minutes ('Setup 10-30 menit') rather than instantly
- composes with: the best shape per dollar among documented hosts: 1 GB of RAM, 10 GB of disk and unmetered 300 Mbps for USD 0.5541 a month, at the cost of only 4 forwarded ports
- reliability: no reliability event observed; the vendor states a 10-30 minute manual setup rather than instant provisioning
- notes: The strongest shape under the line: 1 GB of RAM, 512 MB of swap, 10 GB of SSD and unmetered traffic at 300 Mbps for IDR 10,000, which is USD 0.5541 a month at the CBR rate dated 24.10.2026. The caveat is the port block. Four forwarded ports is the smallest found anywhere, and the vendor sells a dedicated IPv4 as a paid option at IDR 50,000, which is USD 2.77 a month and would take the plan over the line. The checkout selector also lists two cheaper 'Custom - month recurring' plans on the same product at IDR 6,499 (USD 0.3602) and IDR 7,000 (USD 0.3879); their shapes were not read, so they are recorded here as a lead rather than a price. Not established: whether the 4 ports are assigned by the host or chosen by the buyer, whether SSH is one of the 4 or additional, whether UDP is forwarded, and the payment methods. Docker is explicitly unsupported, which matters if container-in-container is needed.
- evidence note: price, billing period, shape, port count and location are quoted from the vendor's own product and checkout pages read; the price is in IDR and converted at a dated rate; the port assignment rule, UDP support, the SSH port rule and the payment rails are unpublished
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1.0
  - shape.disk_gib: 10
  - billing_model: monthly
  - term: monthly ('Monthly - Rp10.000,00' in the checkout plan selector)
  - m10h_usd: 0.5541
  - m24h_usd: 0.5541
  - price_arithmetic: IDR 10,000 a month x (44.6269 RUB per IDR 10,000 / 80.5381 RUB per USD) = USD 0.5541 a month. Both rates from the CBR table dated 24.10.2026. A VPS bills whether it runs or not, so the 24/7 and 10 h/day figures are the same. Cheaper sibling plans on the same product: IDR 6,499 = USD 0.3602/mo and IDR 7,000 = USD 0.3879/mo, shapes unread.
  - out_of_pocket_usd: 0.5541
  - renewal_usd: not published
  - renewal_note: the checkout selector prints 'Monthly' as the period with no strike-through and no promo code, so IDR 10,000 is the ordinary rate; no renewal cycle is stated separately
  - port_mbps: 300
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: shared IPv4 with 4 forwarded ports; a dedicated IPv4 is an option at IDR 50,000
  - network_out.static_ip: no
  - network_out.ipv6: no
  - signup_url: https://my.servermikro.com/products/vps-nat-lxc/vps-nat-lxc-1gb-ram
  - cart_url: https://my.servermikro.com/products/vps-nat-lxc/vps-nat-lxc-1gb-ram/checkout
  - nat_config.ports_tcp: 4
  - nat_config.ports_assigned_or_chosen: unknown
  - udp_forwarding: not stated
  - payment_methods: not stated on the product or checkout page
  - stock: in stock: the product page renders a live price and an 'Add to cart' / checkout link, and no out-of-stock marker appears on 2026-10-24
  - session_cap.restart_required: no
  - session_cap.note: none; it is a container that persists for the paid month
  - dedicated_ipv4_option_usd: 2.7731
- evidence:
  - [1] 2026-10-24: quoted plan body: '1vCPU / 1GB RAM / 512MB SWAP RAM / 10GB SSD DISK / LXC Virtualization / IPV4 Shared(Dedicated IPV4 Available) / 4 Port Forwarding / Unlimited Bandwidth (300 Mbps) / Docker is not supported / North America (Canada - East - Beauharnois) / Setup 10-30 menit' at 'Rp10.000,00'
  - [2] 2026-10-24: quoted billing-period selector: '<option value="53">Monthly - Rp10.000,00</option>', alongside 'Custom - month recurring - Rp6.499,00' and 'Custom - month recurring - Rp7.000,00'; and the dedicated-IPv4 option renders '1x - Rp50.000,00'
  - [3] 2026-10-24: quoted FX table dated 'Date="24.10.2026"': 'IDR 10000 44,6269' and 'USD 1 80,5381' RUB, so IDR 10,000 = 44.6269/80.5381 = USD 0.5541
- sources:
  - [1] https://my.servermikro.com/products/vps-nat-lxc/vps-nat-lxc-1gb-ram
  - [2] https://my.servermikro.com/products/vps-nat-lxc/vps-nat-lxc-1gb-ram/checkout
  - [3] https://www.cbr.ru/scripts/XML_daily.asp
