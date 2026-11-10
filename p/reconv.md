# ReconV

> reconv.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reconv/ | JSON https://fshy.ajam.dev/api/v1/entity/reconv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ReconV

- `compute/reconv-vps-nat512mb` | qualifies | evidence documented | binding per-ip-shaping | category NAT VPS | tier VPS LXC 512 MB (vps-nat512mb)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:01:00.000Z (live) | stale on 2026-11-24
- url https://dash.reconv.pl/en/order/vps/vps-nat512mb
- price parsed USD 0.958/mo
- free tier: No free tier. The smallest LXC plan is PLN 4.00 a month or PLN 45.12 a year: 1 Intel vCPU, 0.5 GB RAM, 6 GB NVMe, unlimited transfer, NAT IPv4 with 10 ports and one /128 IPv6. The order page's period selector offers 4 Month, 11.76 Quarter, 23.04 Semester and 45.12 One Year. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: not stated on any page read; the service is bought in blocks of 1 week to 1 year and no deletion window for an unpaid service is published on the pages read | source: [1]
- egress: unlimited transfer, printed as the infinity symbol in the plan table; the uplink is 150 Mbit per the Server Hunter listing and no rate is published by the vendor for exceeding anything, because nothing is capped | metered: no | free allowance: unlimited | source: [2]
- identity: email | detail: no card at registration. The account page at dash.reconv.pl/en/auth asks for an email address and a password only - the form's two inputs are placeholder 'Enter your email address' and 'Please enter your password' - and no card, address, phone or ID field appears. Payment is a separate vPLN balance top-up after the account exists; the payment rails the vendor accepts are Credit card, PayPal, SEPA, UnionPay and Wire transfer per the Server Hunter listing of the vendor's own feed, which was not confirmed on a first-party checkout page because the checkout is behind the account. No card hold or authorisation amount is stated anywhere read.
- interface: ssh, cli
- limits:
  - per-ip-shaping (binding): NAT IPv4 with 10 forwarded ports; the ports are assigned and listed in the panel's Network tab, not chosen [2]
  - volume-quota: none: transfer is printed as unlimited on every LXC plan [2]
  - pull-count: payment is made in vPLN, a prepaid balance held on the vendor's site: 'Every time you order our service or make a renewal payment, you use our vPLN virtual currency from your balance on ReconV site.' [3]
- binding note: 10 NAT ports is the tightest number on the offer and the one a WireGuard-plus-web-server combination will run out of first; transfer is unlimited and the price is not a constraint.
- interface detail: Root in an LXC container over SSH, with the vendor's own panel for start/stop/restart, real-time CPU/RAM/bandwidth charts, snapshots and firewall rules. The panel's Sieć (Network) tab is where the assigned NAT ports are listed, per the vendor's own wiki.
- tooling: any SSH client; the vendor's custom panel; no API documented. The vendor states Docker runs on these plans.
- composes with: PLN 3.76 a month at the annual rate, or USD 0.958, for 512 MB and 6 GB with unlimited transfer, which is the only provider among documented hosts that publishes unlimited traffic at this price; the 10 NAT ports and the vendor's own TeamSpeak-over-UDP wiki page make it usable as a voice or tunnel endpoint.
- reliability: no reliability event observed. The vendor states DDoS protection on every plan and no SLA is published.
- notes: Two prices exist and they disagree: the vendor's own order page charges PLN 4.00 a month, while Server Hunter lists PLN 3.80 for the semi-annual interval and PLN 3.68 for the annual one. The vendor's page is the authority and the Server Hunter figures are recorded as the mirror of the vendor's feed, not as the price. The monthly figure was taken as the headline because it needs no prepay; the annual is PLN 45.12, which is PLN 3.76 a month. The vendor's own order page states its own conversion, '1 USD ~= 3.92 PLN', which is within 0.2 percent of the rate used here, so the conversion is not doing any work the vendor would dispute. Not established: the exact count of UDP ports among the 10 (the wiki implies at least one UDP port is forwarded but does not state the split), and the checkout payment rails first-hand, because the confirmation step needs an account. The order flow is a two-step wizard whose second step is 'Login / Registration', so a human reaches registration from the order page itself.
- evidence note: the PLN 4.00 monthly and PLN 45.12 annual figures, the shape and the 10-port NAT are read from the vendor's own order page and plan table. The signup fields are read from the vendor's own auth page markup. The payment rails are from Server Hunter's mirror of the vendor's feed and are marked as such rather than claimed first-party. UDP on the NAT ports is inferred from the vendor's own TeamSpeak installation guide, which configures a UDP voice port on this exact product; the guide does not say the word UDP applies to the forward.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 6
  - billing_model: monthly or prepaid term
  - term: 1 week, 1 month, 3 months, 6 months or 1 year
  - m10h_usd: 0.958
  - m24h_usd: 0.958
  - price_arithmetic: Annual: PLN 45.12 a year / 12 = PLN 3.76 a month, paid in one go; 3.76 / 3.926013 = USD 0.9577, rounded to USD 0.958. Monthly alternative: PLN 4.00 / 3.926013 = USD 1.0188. Rate: 1 USD = PLN 3.926013, open.er-api.com/v6/latest/USD, time_last_update_utc Sat, 24 Oct 2026 00:02:31 +0000. A VPS bills whether it runs or not, so 24/7 and 10 h/day are the same.
  - out_of_pocket_usd: 11.49
  - first_payment_usd: 11.49
  - renewal_usd: same PLN 45.12 a year; the 'You Save 6%' is a term discount, not a first-term promo, so the renewal is the same figure
  - stock: in stock: the Server Hunter mirror shows 'Stock In stock' with an unbroken stock history since 2024-12-04, and the vendor's order page presents the plan for configuration rather than refusing it
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 10 ports on a shared NAT IPv4, assigned and listed in the panel's Network tab; plus one /128 IPv6 with all ports
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - network_out.ipv6_prefix: /128
  - signup_url: https://dash.reconv.pl/en/auth
  - cart_url: https://dash.reconv.pl/en/order/vps/vps-nat512mb
  - ipv6_only: no
  - nat_config.ports_tcp: 10
  - nat_config.ssh_port_included: yes
  - nat_config.ports_assigned_or_chosen: assigned; the vendor's wiki directs the buyer to 'the VPS panel, under the Network tab' for 'the list of available ports assigned to your server'. The total is 10 and the vendor does not publish a TCP/UDP split; its own TeamSpeak guide configures a UDP voice port on this product, so at least one UDP forward exists.
  - payment_methods: vPLN prepaid balance; the rails per the Server Hunter mirror of the vendor feed are 'Credit card, PayPal, SEPA, UnionPay, Wire transfer' - not confirmed on a first-party checkout page
  - card_hold: none stated; the balance is prepaid
  - checkout_fields: email and password at registration; the order page's step 2 is 'Login / Registration'
  - udp: at least one UDP port forwards, inferred from the vendor's own TeamSpeak (UDP voice) guide written for this exact product; the split between TCP and UDP among the 10 ports is not published
  - fx: open.er-api.com/v6/latest/USD read 2026-10-24T00:02Z: 1 USD = PLN 3.926013; the vendor's own order page prints '1 USD ~= 3.92 PLN'
- evidence:
  - [1] 2026-10-24: quoted order page: 'CPU 2 vCPU / RAM 0.5 GB RAM / Drive 6 GB NVME SSD / Data transfer Unlimited' and the period selector '4 Month / 11.76 Quarter You Save: 2% / 23.04 Semester You Save: 4% / 45.12 One Year You Save: 6%'
  - [2] 2026-10-24: quoted plan table: '#### 512 MB | 1 | vCPU Intel | 0.5 GB | RAM | 6 GB | Drive | infinity | Transfer | NAT (10) | IPv4 | 1 (/128) | IPv6 | GAME | DDoS protection'
  - [3] 2026-10-24: quoted: 'VPS LXC ... from 4.00 PLN' and 'Every time you order our service or make a renewal payment, you use our vPLN virtual currency from your balance on ReconV site.' and 'Current exchange rate: 1 USD ~= 3.92 PLN'
  - [4] 2026-10-24: the form's two inputs, read from the markup: type='email' placeholder='Enter your email address' and type='password' placeholder='Please enter your password' - no card, address, phone or ID field
  - [5] 2026-10-24: quoted: 'Handbook compatible with VPS LXC (NAT)' and 'default_voice_port=<default voice connection port to the server> (UDP type)' with 'List of available ports assigned to your server can be found in the VPS panel, under the Network tab'
  - [6] 2026-10-24: quoted listing: 'Monthly price z 3.80 PLN ... Stock In stock ... Provider name ReconV ... Uplink 150 Mbit ... Traffic Unlimited ... Payment methods Credit card, PayPal, SEPA, UnionPay, Wire transfer ... Features ... Native IPv6, NAT IPv4' and 'This offer has been in stock since the 4th of December 2024'
- sources:
  - [1] https://dash.reconv.pl/en/order/vps/vps-nat512mb
  - [2] https://www.reconv.pl/en/vps/lxc-shared-resources
  - [3] https://dash.reconv.pl/en/order/vps
  - [4] https://dash.reconv.pl/en/auth
  - [5] https://wiki.reconv.pl/en/vps/jak-zainstalowac-i-skonfigurowac-serwer-teamspeak-nat
  - [6] https://www.serverhunter.com/offer/reconv-vps-nat-512-ipv6-pl-2/
