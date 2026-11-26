# Netlen

> netlen.com.tr | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netlen/ | JSON https://fshy.ajam.dev/api/v1/entity/netlen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Netlen

- `compute/netlen-vps-2` | qualifies | evidence documented | binding per-ip-shaping | category VPS | tier VPS - 2
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T19:44:20.937Z (live) | stale on 2026-12-07
- url https://www.netlen.com.tr/vps-sunucu
- price parsed USD 3.96/mo
- free tier: no free tier; the entry plan is 'VPS - 1 ... 147 TL/Aylik' for 1 GB | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; no deletion clock is published on the plan page
- egress: 'Limitsiz Trafik' - unlimited traffic on a 10 Gbit/s port, stated on every plan card | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: the order page was not opened on 2026-10-24, so card acceptance, debit acceptance and any hold are unverified. The vendor publishes an Istanbul address and an 0850 support number.
- interface: ssh
- limits:
  - per-ip-shaping (binding): unlimited traffic on a 10 Gbit/s shared port; no fair-use figure is published [1]
- binding note: traffic is unlimited and the port is 10 Gbit/s, so the shared CPU is the only published throttle; 2 GB is the real ceiling at this price.
- interface detail: the plan card states 'Tam Root Erisimi' (full root access), a /64 IPv6, rDNS management and API access
- tooling: any SSH client; the vendor's own order panel
- composes with: a 2 GB box on a 10 Gbit/s port with unlimited traffic in Istanbul; the cheapest shape here with a port that large, which suits a VPN node better than the RAM figure suggests
- reliability: no reliability event recorded
- notes: The vendor shows both currencies; 197 TRY and USD 3.99 are the same price at the rate used here, which is a useful check that the TRY figure is not a stale cache. Netlen is the only host that publishes a 10 Gbit/s port on a sub-USD-4 plan. Not established: payment rails and any card hold, and whether the 10 Gbit/s is per-VM or a shared uplink.
- evidence note: shape, the TRY price, the USD price the vendor also displays, and the traffic term are quoted from the vendor's own plan list read. The identity and payment fields are unverified.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 25
  - billing_model: monthly or hourly
  - term: monthly
  - m10h_usd: 3.9611
  - m24h_usd: 3.9611
  - price_arithmetic: 197 TRY/Aylik, times 0.020107 USD per TRY = USD 3.96 a month. The hourly alternative is 0.30 TRY x 730 = 219 TRY, so the monthly cap binds and is cheaper.
  - out_of_pocket_usd: 3.9611
  - renewal_usd: 3.9611
  - renewal_note: no promo is shown on the plan card; 197 TRY is the list price
  - promo: no
  - over_line: no
  - fx.pair: TRY/USD
  - fx.rate: 0.02010724
  - fx.date: 2026-10-24
  - fx.source: open.er-api.com/v6/latest/USD
  - gib_per_usd: 0.5049
  - locations: Istanbul, Turkey
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none; it is a VPS
- evidence:
  - [1] 2026-10-24: quoted: 'VPS - 2 ... 197 TL/Aylik veya 0.30 TL/saat ... CPU 1 Core RAM 2GB DISK 25GB SSD PORT 10 Gbit/s ... Limitsiz Trafik ... Tam Root Erisimi'
  - [1] 2026-10-24: quoted: 'VPS - 4 ... 640 TL/Aylik ... 2 Core RAM 8GB DISK 70GB SSD' - the 8 GB rung is over the line at USD 12.87
  - [2] 2026-10-24: quoted: 'Isletme Adi: NETLEN INTERNET HIZMETLERI LIMITED SIRKETI' and 'ETBIS'e Kayit Tarihi: 20.09.2023'
  - [3] 2026-11-06: the vendor's archived plan card lists VPS - 2 at USD 3.99 a month on a 10 Gbit/s port with unlimited traffic | capture: sha256:fab486bda7216406a6bfc236976f30a194bdb759c13e08a3a5709e7543b56184 | quote: ### VPS - 2 Intel® Xeon® Platinum$3.99/Aylıkveya $0.006/saat CPU1 CoreRAM2GBDİSK25GB SSDPORT10 Gbit/s
  - [4] 2026-11-06: the vendor publishes an Istanbul address | capture: sha256:3fbee1481a8f57df2672f05efe76ea0476b2223b1a9fb9373f8e27cf0055c146 | quote: Atatürk Mh. Ertuğrul Gazi Sk. No: 2E/331 Ataşehir/İstanbul, TÜRKİYE
- sources:
  - [1] https://www.netlen.com.tr/vps-sunucu
  - [2] https://etbis.ticaret.gov.tr/tr/Home/SearchSiteResult?siteId=3d2063e9-7d1c-4ce8-a0dc-ed2a681f690d
  - [3] https://web.archive.org/web/20260929152621/https://www.netlen.com.tr/vps-sunucu
  - [4] https://www.netlen.com.tr/iletisim
