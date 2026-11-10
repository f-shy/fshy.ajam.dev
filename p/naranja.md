# Naranja

> naranja.tech | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/naranja/ | JSON https://fshy.ajam.dev/api/v1/entity/naranja.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Naranja

- `compute/naranja-kvm-nvme-2gb` | paid-only | evidence documented | binding volume-quota | category VPS | tier KVM-NVME-2GB
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://naranja.tech/
- price parsed USD 5.6/mo
- free tier: no free tier; the cheapest listed plan is 'KVM-NVME-2GB EUR 5 month' | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid
- egress: '5 TB Traffic' on a '1 Gbps port speed' | metered: yes | free allowance: 5 TB | source: [1]
- identity: card | detail: an account and a payment method at order; cart checkout unverified against checkout pages; debit acceptance and hold amounts are unconfirmed.
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB a month of traffic [1]
  - per-ip-shaping: 1 Gbps port [1]
- binding note: 5 TB at 1 Gbps is reachable in about 11 hours of saturation, and it is the only published ceiling.
- interface detail: root SSH on KVM; ordering is through the vendor's WHMCS cart
- tooling: any SSH client
- composes with: a 2 GiB box whose IPv4 plus /64 IPv6 and 5 TB are the selling point; the price just misses the line
- reliability: no reliability event recorded
- notes: EUR 5.00 is USD 5.60, so the entry plan misses the line by USD 0.60 and the 4 GiB plan is double. The card is unusually explicit about IPv4 and IPv6, which most cheap hosts leave ambiguous.
- evidence note: the two plan cards' shape, price, traffic, port and addresses are quoted from the vendor's home page read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 30
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 5.6
  - m24h_usd: 5.6
  - price_arithmetic: EUR 5.00/month x 1.1193 = USD 5.60/month
  - out_of_pocket_usd: 5.6
  - renewal_usd: 5.6
  - renewal_note: list price, monthly
  - promo: no
  - over_line: yes
  - fx.pair: EUR/USD
  - fx.rate: 1.1193
  - fx.date: 2026-10-23
  - port_mbps: 1000
  - ipv4_included: yes
  - ipv6: /64
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted: 'KVM-NVME-2GB EUR 5 month - 2 GB RAM - 1 CPU Core - 30 GB NVMe SSD - 5 TB Traffic - 1 Gbps port speed - 1 IPv4 - /64 IPv6'
  - [1] 2026-10-24: quoted: 'KVM-NVME-4GB EUR 10 month - 4 GB RAM - 2 CPU Cores - 60 GB NVMe SSD - 10 TB Traffic'
- sources:
  - [1] https://naranja.tech/

## naranja.tech

- `storage/naranja-tech` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://naranja.tech/
- free tier: none reachable: No storage product is offered. All lines are NVMe 30-120 GB with 5-20 TB transfer. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: All lines are NVMe 30-120 GB; the generous part is transfer (5-20 TB), not disk.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: All lines are NVMe 30-120 GB; the generous part is transfer (5-20 TB), not disk.
  - [2] 2026-10-21: All lines are NVMe 30-120 GB; the generous part is transfer (5-20 TB), not disk.
- sources:
  - [1] https://naranja.tech/
  - [2] https://clients.naranja.tech/store/kvm-nvme
