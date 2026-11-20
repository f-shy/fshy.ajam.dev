# ArenaStreaming

> arenastreaming.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arenastreaming/ | JSON https://fshy.ajam.dev/api/v1/entity/arenastreaming.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ArenaStreaming

- `compute/arenastreaming-lxc-nat-basic` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS | tier LXC NAT Basic
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:00.000Z (live) | stale on 2026-11-24
- url https://client.arenastreaming.com/store/vps-hosting-lxc-lite-nat
- price parsed USD 0.5541/mo
- free tier: No free tier. LXC NAT Basic is Rp10.000,00 a month for 256 MB RAM, 1 core, 5 GB SSD and 200 GB of bandwidth, on LXC with port forwarding. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the container persists for the paid term; the store page prints no deletion schedule | source: [1]
- egress: 200 GB of bandwidth a month on LXC NAT Basic, 500 GB on Starter, 1 TB on Pro, 1.5 TB on Adv; no overage price is printed | metered: yes | free allowance: 200 GB | source: [1]
- identity: email | detail: no card hold and no payment method is printed on the store page read; the store is a WHMCS client area ('Powered by WHMCompleteSolution') with a cart, so an account is required, but the rails are unverified
- interface: ssh
- limits:
  - volume-quota: 200 GB a month of bandwidth on LXC NAT Basic [1]
  - per-ip-shaping (binding): NAT IPv4 with port forwarding; the number of forwarded ports is not printed [1]
- binding note: the port count is not published at all, so the first thing a reader cannot plan around is how many forwarded ports the plan carries.
- interface detail: LXC container with a web control panel: 'Panel Kontrol Web: Manajemen VPS jadi lebih mudah dan efisien'
- tooling: any SSH client; a web panel the vendor names but does not identify
- composes with: the cheapest per-month NAT container found in Indonesia at Rp10.000 (USD 0.55) for 256 MB, but its order path is broken today
- reliability: no reliability event observed; the order path is broken rather than the service, see notes.
- notes: The price is under the line by a wide margin: IDR 10,000 is USD 0.5541 a month at the CBR rate dated 24.10.2026, for 256 MB, 1 core, 5 GB and 200 GB. The caveat is the order path, not the price. The category page at /store/vps-hosting-lxc-lite-nat renders all four NAT plans and their prices, but every order button and the /store index resolve to an unrelated 'Radio Streaming Live' product: the order button href is '/store/vps-hosting-lxc-lite-nat/lxc-nat-basic' and that URL 200s with x-web-final-url https://client.arenastreaming.com/store/radio-streaming-live, and /store itself does the same. So a buyer reading the price page cannot reach the NAT cart through the links the page prints. Not established: the number of forwarded ports, whether SSH is one of them, whether they are assigned or chosen, whether UDP is forwarded, the billing cycles offered at checkout, and the payment methods. The same host sells 'RDP NAT' separately, which is a different product and was not read.
- evidence note: price, shape, traffic and the port-forwarding claim are quoted from the vendor's own store page read; the price is in IDR and converted at a dated rate; the port count, the SSH port rule, UDP support and the payment rails are all unpublished
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.25
  - shape.disk_gib: 5
  - billing_model: monthly
  - term: monthly ('/mo' on the plan card)
  - m10h_usd: 0.5541
  - m24h_usd: 0.5541
  - price_arithmetic: IDR 10,000 a month / (44.6269 RUB per IDR 10,000) = 44.6269 RUB; 44.6269 / 80.5381 RUB per USD = USD 0.5541 a month. Both rates from the CBR table dated 24.10.2026. A VPS bills whether it runs or not, so the 24/7 and 10 h/day figures are the same.
  - out_of_pocket_usd: 0.5541
  - renewal_usd: not published
  - renewal_note: one monthly price is printed per plan with no strike-through and no promo code, so Rp10.000 is the ordinary rate
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: NAT IPv4 with port forwarding; the count is not printed
  - network_out.static_ip: no
  - network_out.ipv6: no
  - signup_url: https://client.arenastreaming.com/store/vps-hosting-lxc-lite-nat
  - cart_url_note: the page prints '/store/vps-hosting-lxc-lite-nat/lxc-nat-basic' as the order href, but that URL resolves to /store/radio-streaming-live, an unrelated product, so no working cart URL exists to record
  - nat_config.ports_assigned_or_chosen: unknown
  - udp_forwarding: not stated
  - payment_methods: not stated on the store page
  - stock: unknown: the NAT category page printed no availability count for any of the four plans when read on 2026-10-24, unlike its radio product which printed '44 Available'
  - session_cap.restart_required: no
  - session_cap.note: none; it is a container that persists for the paid term
- evidence:
  - [1] 2026-10-24: quoted plan card: 'LXC NAT Basic / 256 MB RAM / 1 Core Processor / 5 GB SSD Storage / 200 GB Bandwidth / Rp10.000,00 /mo' and 'LXC NAT Starter ... 512 MB RAM ... Rp20.000,00 /mo'
  - [1] 2026-10-24: quoted feature list: 'Port Forwarding: Mendukung akses fleksibel untuk aplikasi tertentu' (port forwarding supports flexible access for particular applications) and 'Panel Kontrol Web' (web control panel)
  - [2] 2026-10-24: quoted FX table dated 'Date="24.10.2026"': 'IDR 10000 44,6269' and 'USD 1 80,5381' RUB, so IDR 10,000 = 44.6269/80.5381 = USD 0.5541
- sources:
  - [1] https://client.arenastreaming.com/store/vps-hosting-lxc-lite-nat
  - [2] https://www.cbr.ru/scripts/XML_daily.asp
