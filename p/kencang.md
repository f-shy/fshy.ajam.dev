# Kencang

> kencang.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kencang/ | JSON https://fshy.ajam.dev/api/v1/entity/kencang.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kencang

- `compute/kencang-k3` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier K-3
- needs card unknown, phone no, ID no, institution no | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://kencang.com/vps-iix-murah
- price parsed USD 4.61/mo
- free tier: no free tier; K-1 at Rp29.900 a month is the entry plan | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the service policy describes a prepaid balance that must stay funded
- egress: 'Unlimited bandwidth dengan kecepatan jaringan sesuai paket yang dipilih' - unlimited, at the plan's port speed, 100 Mbps on K-3 | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: a prepaid-balance account. The vendor's service policy, as returned by search, states 'Kencang Cloud menggunakan sistem prepaid balance'; the payment-methods page itself was not read, so card acceptance, debit acceptance and any hold are unverified.
- interface: ssh
- limits:
  - per-ip-shaping (binding): bandwidth unlimited at the plan's port speed: 50 Mbps on K-1 and K-2, 100 Mbps on K-3, 1 Gbps on K-4 and above [1]
- binding note: the RAM and core count are fixed and the traffic is unlimited, so the port speed is what constrains throughput.
- interface detail: KVM with an OS reinstall and a start/stop panel; the page states 'Kontrol VPS' and 'Full SSD' but does not spell out root
- tooling: any SSH client; the vendor's own order panel
- composes with: 4 GiB and 4 vCPU in Jakarta for USD 4.61 a month on the annual term; the highest core count under the line among evaluated providers.
- reliability: no reliability event recorded
- notes: The monthly price is Rp99.900, USD 5.52, over the line; only the annual prepay of Rp999.900 brings it to USD 4.61, costing USD 55.27 out of pocket once. The annual table lists '1 CPU' on K-3 where the monthly table lists '4 CPU' for the same plan name, a defect on the vendor's page; the shape recorded is the monthly one because it is the more specific.
- evidence note: shape, the monthly and annual prices and the port speeds are quoted from the vendor's own price table read. The payment rails and the legal entity are unverified.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 4
  - shape.disk_gib: 50
  - billing_model: annual prepay
  - term: annual
  - m10h_usd: 4.6061
  - m24h_usd: 4.6061
  - price_arithmetic: Rp999.900 a year divided by 12 = Rp83.325 a month, times 0.00005528 USD per IDR = USD 4.61 a month. The monthly alternative is Rp99.900 = USD 5.52, over the line.
  - out_of_pocket_usd: 55.2737
  - renewal_usd: 4.6061
  - renewal_note: the annual table carries no separate renewal column; the same Rp999.900 is assumed to renew
  - promo: no
  - over_line: no
  - fx.pair: IDR/USD
  - fx.rate: 5.528e-05
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - gib_per_usd: 0.8684
  - locations: Jakarta and Surabaya, Indonesia
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted: 'K-3 | 4 CPU | 4 GB | 50 GB | Hingga 100Mbps | Rp99.900 / bulan'
  - [1] 2026-10-24: quoted from the annual table: 'K-3 ... 4 CPU | 4 GB | 50 GB | Rp999.900 / tahun' - which is USD 4.61 a month
  - [1] 2026-10-24: quoted: 'Unlimited bandwidth dengan kecepatan jaringan sesuai paket yang dipilih.'
- sources:
  - [1] https://kencang.com/vps-iix-murah
