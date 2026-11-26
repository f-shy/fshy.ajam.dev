# NetX

> netx.hosting | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netx/ | JSON https://fshy.ajam.dev/api/v1/entity/netx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetX

- `compute/netx-vps-0` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier VPS-0
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T19:33:06.062Z (live) | stale on 2026-12-07
- url https://netx.hosting/store/vps-vds-hosting
- price parsed USD 4.07/mo
- free tier: no free tier; VPS-0 is the entry tariff | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; no deletion clock is published
- egress: the tariff table lists a shared 10 Gbps channel; no traffic number is published for VPS-0 on the page read | metered: no | free allowance: not published on the page read | source: [1]
- identity: card | detail: the order page was not opened on 2026-10-24, so card acceptance, debit acceptance and any hold are unverified.
- interface: ssh
- limits:
  - per-ip-shaping (binding): KVM on a shared 10 Gbps channel; no traffic allowance is stated for this tariff [1]
- binding note: no traffic number is published, so the shared channel and the 2 GB of RAM are what bound it.
- interface detail: KVM with a choice of CentOS, Debian or Ubuntu; root is not spelled out on the tariff table
- tooling: any SSH client; the vendor's own order panel
- composes with: a 2 GiB Ukrainian box on a shared 10 Gbps channel; the cheapest entry into the Ukrainian market found, but poor value per GiB
- reliability: no reliability event recorded
- notes: The headline 184 UAH is the 12-month term price; month-to-month is 215.28 UAH. Even on the annual term the row is only 0.49 GiB per USD, which is the worst value apart from LumaDock, and the traffic allowance is not published.
- evidence note: the tariff ladder and every term price are parsed from the vendor's live page HTML today. The identity and payment fields are unverified.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 20
  - billing_model: monthly, term-discounted
  - term: 12 months
  - m10h_usd: 4.0707
  - m24h_usd: 4.0707
  - price_arithmetic: 2208 UAH for 12 months divided by 12 = 184 UAH a month, times 0.022123 USD per UAH = USD 4.07 a month. Month-to-month is 215.28 UAH = USD 4.76.
  - out_of_pocket_usd: 48.8481
  - renewal_usd: 4.7627
  - renewal_note: the 184 UAH rate is the 12-month term; month-to-month is 215.28 UAH and is the renewal if the term is not renewed
  - promo: yes
  - over_line: no
  - fx.pair: UAH/USD
  - fx.rate: 0.02212322
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - gib_per_usd: 0.4913
  - locations: Ukraine
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted: 'VPS-0 | ot | 184 grn | v mesyats' with the term table '1 | 215.28 | 215 | 0% ... 12 | 2208 | 184 | 15%'
  - [1] 2026-10-24: quoted: 'AMD EPYC 2.8GHz, 2 yadra ... 2GB ... 20GB SSD ... KVM 10 Gbps shared'
  - [1] 2026-10-24: quoted: 'VPS-1 | ot | 322 grn ... 3 yadra ... 4GB' and 'VPS-2 ... 561 grn ... 8GB' - the 8 GB rung is USD 12.41 a month, over the line
  - [1] 2026-11-06: the store page's FAQ states that no special documents are needed to rent a VPS | capture: sha256:cdb15bcb8aa56c4d4ac8e50c8217c10888157f31cb11db7800fada463df0ceb8 | quote: Нет, как и для покупки обычного хостинга в Украине, для аренды виртуального выделенного сервера не нужны специальные документы.
- sources:
  - [1] https://netx.hosting/store/vps-vds-hosting
