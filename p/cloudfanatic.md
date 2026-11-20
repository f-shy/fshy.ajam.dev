# Cloudfanatic

> cloudfanatic.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudfanatic/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudfanatic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloudfanatic (formerly Servercheap)

- `compute/cloudfanatic-standard-1gb` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier Standard VPS, 1 GB RAM
- needs card yes, phone yes, ID no, institution no | verified 2026-11-06T17:42:09.298Z (live) | stale on 2026-12-07
- url https://cloudfanatic.net/pricing/
- price parsed USD 2.99/mo
- free tier: no free tier; the 1 GB standard plan is USD 2.99 a month with a 7-day money-back window | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the VPS persists while paid; the page states a 7-day money-back policy and no deletion clock | source: [1]
- egress: unmetered fair share on a 1 Gbit/s network; no byte figure is published | metered: no | free allowance: unmetered, fair-share | source: [1]
- identity: card | detail: an account with a phone number and a card or PayPal: the registration form marks 'Phone Number' as a required field ('<label for="inputPhone" class="label-required" > Phone Number </label>'), and payment is 'All major credit and debit cards and PayPal. Additionally customers who have made their first payment via credit card or paypal, can pay via Bitcoin as well.' Charged or verified: charged; no authorisation or deposit is described. Prepaid and virtual cards: not published; account credit is a prepaid route ('The funds you add to your account do not expire and can be used to pay for your future invoices or purchases.').
- interface: ssh
- limits:
  - per-ip-shaping (binding): 1 Gbit/s, unmetered fair share; no published byte cap [1]
  - per-object-cap: 30 GB of NVMe [1]
  - request-rate: 1 vCPU [1]
- binding note: there is no byte quota, so the first real limit is the fair-share clause on a 1 Gbit/s port, whose enforcement threshold is unpublished.
- interface detail: root SSH and VNC console; a dedicated IPv4 and an IPv6 address are listed per plan
- tooling: any SSH client
- composes with: a dedicated-IPv4 VPS under USD 3 with an unmetered port, which a WireGuard node can use without any forwarding arrangement
- reliability: no reliability event observed; the vendor's promotional copy names hosting a personal VPN as a use of the plan.
- notes: The Servercheap name in evaluated offerings brief still resolves but no longer sells under its own domain: a request for servercheap.net returned cloudfanatic.net content with the title 'Affordable VPS Hosting Solutions for everyone'. Whether Cloudfanatic honours old Servercheap plans is not established. The 'unmetered' claim is fair-share, so a 24/7 tunnel at sustained rate is the case most likely to meet the unpublished threshold.
- evidence note: price, shape, address and bandwidth terms quoted from the pricing page read; Servercheap rebranding is inferred from the redirect and not from a statement
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 30
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 2.99
  - m24h_usd: 2.99
  - price_arithmetic: USD 2.99 a month billed monthly; a VPS bills whether it runs, so 10 h/day and 24/7 are the same bill
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all; the IPv4 is dedicated
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
  - ipv6_prefix: an IPv6 address is listed per plan; no prefix width is stated
  - renewal_note: no renewal price is published; the page states one monthly figure and does not mark it as a first-term promo
  - payment_rails: Visa, MC, Amex, PayPal, wire; no hold stated
  - payment_methods: all major credit and debit cards, PayPal, and Bitcoin after a first card or PayPal payment; account credit can be added and is used first
- evidence:
  - [1] 2026-10-24: quoted plan: '1 GB RAM 2.99/mo - 1 GB Ram, 1 vCPU, 30 Ultra-Fast NVME Disk, 1 Gbit/s network, Unmetered fair share network, Linux OS of your choice, Root access via ssh and vnc, Dedicated IPv4 & IPv6 address'
  - [2] 2026-10-24: quoted: 'VPS Hosting - A great place to start your website or blog, host your personal vpn, develop and test applications'
  - [3] 2026-10-24: 
  - [4] 2026-11-06: the card is charged every month, and no authorisation amount is described | capture: sha256:3e57b9e71c87966959cf3a480bd03d37007763914dc1caff724fadf63e319c9d | quote: Subscriber agrees that Cloudfanatic may automatically charge subscriber’s credit card every month.
  - [5] 2026-11-06: the registration form marks the phone number as required | capture: sha256:c4256089280fcde3ffd1b9404a19056514118f4ebb482f057d6f747a9a4e1fb3 | quote: <label for="inputPhone" class="label-required" > Phone Number </label>
  - [1] 2026-11-06: the accepted instruments are the major credit and debit cards, PayPal and Bitcoin after a first card or PayPal payment | capture: sha256:5b6d5fdbe117895e424a58ca360ecb1257f9809982bc3f90b3ffd6be2f6290de | quote: All major credit and debit cards and PayPal. Additionally customers who have made their first payment via credit card or paypal, can pay via Bitcoin as well.
  - [1] 2026-11-06: a card or PayPal is accepted, and the registration form requires a phone number | capture: sha256:5b6d5fdbe117895e424a58ca360ecb1257f9809982bc3f90b3ffd6be2f6290de | quote: All major credit and debit cards and PayPal. Additionally customers who have made their first payment via credit card or paypal, can pay via Bitcoin as well.
- sources:
  - [1] https://cloudfanatic.net/pricing/
  - [2] https://cloudfanatic.net/
  - [3] https://servercheap.net/
  - [4] https://cloudfanatic.net/legal
  - [5] https://my.cloudfanatic.net/register.php
