# AsiaVM

> asiavm.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/asiavm/ | JSON https://fshy.ajam.dev/api/v1/entity/asiavm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AsiaVM (PT Media Creative Technology)

- `compute/asiavm-nat-eu-hetzner-1gb` | dead | evidence documented | binding per-ip-shaping | category NAT VPS | tier NAT VPS EU Hetzner - 1GB
- needs card yes, phone yes, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://portal.asiavm.net/index.php?rp=/store/nat-vps-eu-hetzner
- price parsed USD 1/mo
- free tier: No free tier. The 1 GB Hetzner plan is USD 12.00 a year, printed '$12.00 USD Annually'. The marketing page advertises it as '$1 /month12$ /year'. The cart returned 'Out of Stock' for it. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: annual prepay; no deletion interval after expiry was published on the pages read. The store states 'No Backup' on every plan. | source: [1]
- egress: 2 TB a month on the 1 GB plan, printed '2 TB Bandwidth', on a 1 Gbps port | metered: yes | free allowance: 2 TB a month | source: [1]
- identity: card | detail: a WHMCS account whose registration form requires first name, last name, street address, city, postcode and email, with phone present and not marked required and no national ID field. Payment rails and any authorisation hold are unestablished, because the cart refuses every NAT product before a payment step.
- interface: ssh
- limits:
  - volume-quota: 2 TB a month [1]
  - per-ip-shaping (binding): 20 forwarded records on the shared IPv4 plus a dedicated IPv6 /112; the KVM group states the same ports as '20 Ports (TCP/UDP)' [2]
- binding note: 20 forwarded records is a workable budget, but the binding constraint is that no group in this store can be ordered: the cart refused all four NAT groups read.
- interface detail: OpenVZ 7 container on the Hetzner group, with a shared IPv4 carrying 20 forwarded records and a dedicated IPv6 /112
- tooling: any SSH client; a WHMCS client area
- composes with: a 1 GB Hetzner-backed container with a /112 and 2 TB at USD 1.00 a month, which would be a strong row if it were buyable; the cart refuses every group
- reliability: every plan states 'No Technical Support' and 'No Backup'; no uptime figure published
- notes: The marketing page displays '$1 /month' and '$12 /year' side by side, but the store bills annually; total cost is USD 12.00 and the monthly figure is a division rather than an independent billing option.
- evidence note: price, shape, traffic, the /112, the port count, the TCP/UDP wording on the KVM group and the out-of-stock refusal are quoted from the vendor's own store and cart read; the entity name is quoted from the vendor's own site footer; the registration form fields are quoted from the form source read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 15
  - billing_model: annual
  - term: annual
  - m10h_usd: 1.0
  - m24h_usd: 1.0
  - price_arithmetic: USD 12.00 a year / 12 = USD 1.00 a month, which is the figure the marketing page prints as '$1 /month'. The money out of pocket is USD 12.00 once a year. No conversion needed. VPS billing: the machine bills whether it runs or not, so the 10 h/day and 24/7 figures are identical.
  - out_of_pocket_usd: 12.0
  - renewal_usd: USD 12.00 a year; no separate renewal price published
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 20 forwarded records on the shared IPv4 plus a dedicated IPv6 /112
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /112
  - udp: stated for the KVM group in words: '20 Ports (TCP/UDP)'. The Hetzner and Indonesia groups name the same '20 VDF Records' without a protocol, so UDP is documented on the KVM group and a dash on this one.
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not established: the cart refuses every NAT product before a payment step
  - card_hold: not stated on any page read
  - checkout_fields: first name, last name, street address, city, postcode and email required; phone and company present but optional; no national ID
  - stock: out of stock across every NAT group: Indonesia '0 Available' on all three, KVM '0 Available' on all three, Singapore '0 Available', and the Hetzner group's cart returns 'Out of Stock' although its page shows no marker
  - cart_url: https://portal.asiavm.net/cart.php?a=add&pid=1
  - cart_works: refused: the cart answered 'Out of Stock ... orders for it have been suspended'
  - product_url: https://portal.asiavm.net/index.php?rp=/store/nat-vps-eu-hetzner
  - signup_url: https://portal.asiavm.net/register.php
  - cart_url_note: the Hetzner group's Order Now button targets a per-product cart route; that route resolved and refused with an out-of-stock message, which is how the refusal was established rather than inferred.
  - other_plans: Hetzner 2GB USD 24 a year for 25 GB NVMe and 4 TB; Hetzner 4GB USD 45 a year for 50 GB NVMe and 6 TB. KVM 1GB USD 24 a year, 2GB USD 39.60, 4GB USD 78, all with '20 Ports (TCP/UDP)'. The Singapore group is USD 12 a year for 1 GB but states 'No IPv6'.
- evidence:
  - [1] 2026-10-24: quoted plan: 'NAT VPS EU Hetzner - 1GB Shared IPv4 20 VDF Records /112 IPv6 1GB RAM 1 vCPU 15GB SSD NVMe 2 TB Bandwidth 1Gbps Port Speed No Technical Support No Backup $12.00 USD Annually'
  - [3] 2026-10-24: quoted marketing page: 'NAT-1GB NAT VPS 1$ /month12$ /year ... 1GB Ram, 15GB SSD, 1 vCPU, /112 IPv6, 20 VDF Records, 2TB Bandwidth, 1Gbps Port Speed, OpenVZ7 Virtualization, Located in Jakarta, Indonesia'
  - [2] 2026-10-24: quoted explicit protocol wording: 'NAT KVM 1GB 0 Available ... 20 VDF Records Shared IPv4 /112 IPv6 1Gbps Port Speed No Technical Support No Backup KVM Virtualization 20 Ports (TCP/UDP) $24.00 USD Annually'
  - [4] 2026-10-24: the cart refused the product: 'Out of Stock We are currently out of stock on this item so orders for it have been suspended until more stock is available.' - for the 1 GB Hetzner plan, whose group page carries no stock marker at all
  - [5] 2026-10-24: the Indonesia group reads '0 Available' on all three plans, with 'NAT ID 1GB 0 Available ... $12.00 USD Annually' and the same 'No Technical Support No Backup' line
  - [6] 2026-10-24: 
  - [7] 2026-10-24: the form source marks firstname, lastname, address1, city and postcode as required; email is present; phonenumber is present without a required marker; no national ID field exists
- sources:
  - [1] https://portal.asiavm.net/index.php?rp=/store/nat-vps-eu-hetzner
  - [2] https://portal.asiavm.net/index.php?rp=/store/nat-vps-kvm
  - [3] https://asiavm.net/nat-vps-indonesia/
  - [4] https://portal.asiavm.net/cart.php?a=add&pid=1
  - [5] https://portal.asiavm.net/index.php?rp=/store/nat-vps-id
  - [6] https://asiavm.net/
  - [7] https://portal.asiavm.net/register.php
