# Host Hong Kong

> hosthongkong.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hosthongkong/ | JSON https://fshy.ajam.dev/api/v1/entity/hosthongkong.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Host Hong Kong

- `compute/host-hong-kong-nat-vps` | dead | evidence documented | binding per-ip-shaping | category NAT VPS | tier NAT-VPS (256 MB)
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T06:03:49.000Z (live) | stale on 2026-11-24
- url https://hosthongkong.net/?page=NAT-VPS
- free tier: No free tier. The NAT-VPS page describes the plan as 256 MB of RAM with 21 forwarded ports on the shared IPv4 and a native /64 IPv6 subnet, but publishes no price and carries no order link: the page has no cart.php target at all. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the page states 'Our NAT based VPS offers no refunds, no guarantees, and no backups' and 'A hard drive failure will result in a loss of all data' | source: [1]
- egress: no byte allowance published. The page states hard caps of 'Network Bandwidth (50Mbit/s)' and 'disk I/O (20MB/s)', and warns that 'the server will perform below these limits as the fair usage of resources by all the VMs on the node would mean something like 1MB/s of disk I/O and 400Kbit/s of network bandwidth' | metered: no | free allowance: unmetered with a 50 Mbit/s port cap and a fair-use expectation of about 400 Kbit/s | source: [1]
- identity: card | detail: not established. There is no order path to follow, so the checkout and its fields were unreachable; the billing area exists at hosthongkong.net/billing with a standard WHMCS login. No ID requirement is published anywhere read.
- interface: ssh
- limits:
  - per-ip-shaping (binding): 21 forwarded ports on the shared IPv4 plus a native /64 IPv6 subnet [1]
  - per-ip-shaping (binding): hard caps of 50 Mbit/s network and 20 MB/s disk I/O, with 2 OS reinstalls a month and an expectation of about 400 Kbit/s under fair use [1]
- binding note: the effective network is about 400 Kbit/s under the vendor's own fair-use statement, which is far below the 50 Mbit/s headline and makes anything but a tunnel impractical.
- interface detail: NAT KVM guest; the page names a 256 MB NAT KVM plan and says the OS may be reinstalled twice a month
- tooling: any SSH client; the WHMCS billing area at hosthongkong.net/billing
- composes with: not usable as a purchase because no price and no order path are published; the specification would suit a WireGuard endpoint if it could be bought
- reliability: the vendor's own page states there is no SLA, no guarantee, no backup and no refund under any circumstances, that a dispute carries a HK$500 handling charge, that as many as 128 VPS may run on one server, and that 'there may be no VPS services provided at all'
- notes: While the port has a 50 Mbit/s ceiling, vendor documentation states fair-use throughput averages approximately 400 Kbit/s.
- evidence note: the specification, the port count, the /64, the hard caps, the oversubscription figure and the no-refund terms are all quoted from the vendor's own NAT-VPS page read. The price is not documented because the page does not publish one, and the absence of an order link was checked in the page source rather than assumed.
- extras:
  - shape.ram_gib: 0.25
  - billing_model: unknown
  - term: unknown
  - price_arithmetic: not computed: the vendor publishes no price for the NAT plan, so no monthly figure exists to derive. A dash rather than a guess.
  - renewal_usd: not published
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 21 forwarded ports on the shared IPv4, plus a native /64 IPv6 subnet reachable natively
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /64
  - udp: not stated: the page names no protocol for the 21 ports, though it recommends the plan as a VPN or tunnel, which implies UDP works
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - payment_rails: not established: no order path exists to a checkout
  - card_hold: not stated on any page read
  - checkout_fields: not established: no order path exists
  - stock: not stated: the page publishes no stock control and no cart entry
  - cart_works: no cart exists: the page source carries no cart.php target
  - product_url: https://hosthongkong.net/?page=NAT-VPS
  - signup_url: https://hosthongkong.net/billing/clientarea.php
  - cart_url_note: recorded as null because the page that describes the product carries no order link at all; this is not a broken link but a missing one.
- evidence:
  - [1] 2026-10-24: quoted: 'Your VPS will be accessible over the internet natively over IPv6, or via port forwarding for IPv4. A total of 21 ports from the SHARED IP are allocated to each NAT VPS. Dedicated IPv4 addresses are not available with the NAT VPS. ... We do however include a native /64 IPv6 subnet.'
  - [1] 2026-10-24: quoted: 'The NAT-VPS plan includes only 256MB RAM, and this will impact the performance of resource intensive applications.' and 'The most common use for the NAT-VPS is to use as a VPN / Tunnel.'
  - [1] 2026-10-24: quoted caps: 'Hard limitations include disk I/O (20MB/s), OS Reinstallation (2 times per month), Network Bandwidth (50Mbit/s)' and 'the server will perform below these limits as the fair usage of resources by all the VMs on the node would mean something like 1MB/s of disk I/O and 400Kbit/s of network bandwidth'
  - [1] 2026-10-24: quoted: 'Our NAT based VPS offers no refunds, no guarantees, and no backups!' and 'There may be as many as 128VPS running on a single server.' and 'A dispute handling charge is levied in the amount of HK$500.'
  - [1] 2026-10-24: the page source carries no cart.php?a=add target and no price for the NAT product: the only HK$ figure in the body is the HK$500 dispute charge. Its navigation points to /billing/clientarea.php, and the five billing product groups read (gid 1 to 5) are shared hosting, reseller, KVM VPS, dedicated servers and colocation - none is the NAT plan.
- sources:
  - [1] https://hosthongkong.net/?page=NAT-VPS
