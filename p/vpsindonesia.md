# VPS Indonesia

> vpsindonesia.co.id | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsindonesia/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsindonesia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPS Indonesia

- `compute/vpsindonesia-mini` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier Mini
- needs card no, phone no, ID no, institution no | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://www.vpsindonesia.co.id/vps-murah-2gb
- price parsed USD 2.21/mo
- free tier: no free tier; Mini at Rp40.000 is the smallest plan on this page | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; no deletion clock is published
- egress: 'bandwidth unlimited (fair use)' and 'Harga final termasuk IP publik' - the price includes a public IPv4 | metered: no | free allowance: unlimited (fair use) | source: [1]
- identity: email | detail: an account with an e-mail. Payment is by QRIS, the Indonesian QR rail settled from an e-wallet or a mobile-banking app ('Bayar QRIS, aktif otomatis'), so no card is required. No hold is described. No phone or ID step was read.
- interface: ssh
- limits:
  - per-ip-shaping (binding): bandwidth is unlimited under a fair-use clause with no published number [1]
- binding note: the price includes a public IP and unlimited fair-use bandwidth, so the unwritten fair-use clause is the only stated limit.
- interface detail: KVM with a public IPv4 included; the page does not state root or SSH, so the interface is unconfirmed here
- tooling: any SSH client; the vendor's own order panel
- composes with: a 2 GB KVM box in Jakarta with a public IPv4 and a QRIS payment rail; the one row among documented hosts that needs neither a card nor a foreign-currency bank transfer
- reliability: no reliability event recorded
- notes: The second-best GiB per USD in this category after Bulutova, and the only row whose payment rail is a domestic QR code rather than a card. Not established: the legal entity behind vpsindonesia.co.id. No company name, registration number or address appears on the page read, and WHOIS was not checked. Treat the seller as unverified until that is found.
- evidence note: shape, price, the public-IP inclusion and the QRIS rail are all quoted from the vendor page read. The company behind the domain was not established.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 25
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 2.2112
  - m24h_usd: 2.2112
  - price_arithmetic: Rp40.000 a month, times 0.00005528 USD per IDR = USD 2.21 a month.
  - out_of_pocket_usd: 2.2112
  - renewal_usd: 2.2112
  - renewal_note: monthly list price; no promo is shown
  - promo: no
  - over_line: no
  - fx.pair: IDR/USD
  - fx.rate: 5.528e-05
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - gib_per_usd: 0.9045
  - locations: Jakarta, Indonesia
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted: 'Mini 1 vCPU - 2 GB - 25 GB Rp40.000' and 'Basic 2 vCPU - 2 GB - 40 GB Rp65.000'
  - [1] 2026-10-24: quoted: 'Bayar QRIS, aktif otomatis' and 'Harga final termasuk IP publik dan bandwidth unlimited (fair use)'
- sources:
  - [1] https://www.vpsindonesia.co.id/vps-murah-2gb
