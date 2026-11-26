# VPSDime

> vpsdime.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsdime/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsdime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPSDime

- `compute/vpsdime` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T17:40:47.147Z (live) | stale on 2026-12-08
- url https://vpsdime.com/linux-vps
- price parsed USD 5/mo
- free tier: Linux VPS (order product Linux4GB) at USD 5.00 per month: 2 vCPU, 4 GB fully dedicated memory, 20 GB SSD in RAID10, 1 TB traffic limit, 1 public IPv4, orderable in Dallas, Los Angeles, Amsterdam and London. Order page read 2026-11-07: monthly USD 5.00, quarterly USD 15.00, semi-annually USD 30.00, annually USD 60.00; setup fee USD 0.00; recurring charge USD 5.00 monthly; renewal price beyond that not published; plan in stock ('Deploy Now', no out-of-stock marker). The next plan is USD 7.00 for 6 GB ECC and 2 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB a month included; no overage rate is published on the page read | metered: yes | free allowance: 1 TB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 1 TB a month on a 10 Gbps uplink. The port is ten times what the allowance can carry in a day of sustained use, so the monthly byte count is the binding constraint rather than the link speed. [1]
- limits note: 1 TB a month on a 10 Gbps uplink. The port is ten times what the allowance can carry in a day of sustained use, so the monthly byte count is the binding constraint rather than the link speed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor documents no client or API
- composes with: 4 GB of RAM and 2 cores for USD 5 with three U.S. and EU locations is the cheapest way among documented hosts to run a database or an index that must sit near the data, and the 1 TB allowance is enough for a metadata crawler that does not stream bodies
- reliability: no reliability event recorded
- notes: The provider's own pages also sell a Storage VPS and a Windows VPS line that were not read, so the USD 5.00 row is the cheapest Linux plan, not the cheapest product on the site.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 20
  - price_on_page: USD 5.00/month for Linux VPS (Linux4GB)
  - renewal_usd: not published: the order page prices monthly, quarterly, semi-annual and annual terms and prints no renewal price
- evidence:
  - [1] 2026-10-22: first row of the Linux VPS table, under the columns 'CPU / Core / RAM / Storage / Transfer / Uplink / Price': 'Intel Xeon Gold / 2 CPU / 4GB ECC / 20GB SSD / 1TB / 10Gbps / $5.00/mo'
  - [1] 2026-10-22: second row: 'Intel Xeon Gold / 4 CPU / 6GB ECC / 30GB SSD / 2TB / 10Gbps / $7.00/mo'
  - [2] 2026-10-22: tracker agrees: '$5.00 / month 2 Intel Cores (shared) 4,096 MB RAM 20 GB SSD 1,000 GB/month bandwidth 10 Gbps port speed IPv4 + IPv6' in Dallas, Los Angeles and Amsterdam
  - [3] 2026-10-22: plan table quoted: 'Intel Xeon Gold | 4 CPU | 2GB ECC | 1000GB | 8TB | 10Gbps | $14.00/mo' and '4000GB | 32TB | $56.00/mo'; also '100GB | 1TB | $40.00/yr' and '250GB | 2TB | $60.00/yr'
  - [3] 2026-10-22: the page states 'Built with HGST Enterprise-grade HDDs in RAID10 configuration' and lists six locations: Seattle, Los Angeles, Dallas, Piscataway, Maidenhead, Amsterdam
  - [4] 2026-10-22: the trailing-slash path returned 404 from the origin before any extractor ran; the path without the slash answered 403 and was extracted
  - [5] 2026-11-07: the order page's configuration summary prints the four billing cycles and their prices | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Monthly$5.00 USD Quarterly$15.00 USD Semi-Annually$30.00 USD Annually$60.00 USD
  - [5] 2026-11-07: the cart totals USD 5.00 due today for Linux4GB | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Total Due Today$5.00 USD
  - [5] 2026-11-07: no setup fee on the order page | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Setup Fees$0.00 USD
  - [5] 2026-11-07: the plan is orderable, no out-of-stock marker | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Deploy Now
  - [5] 2026-11-07: the order page states the traffic limit for Linux4GB | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: 1TB Traffic Limit
  - [5] 2026-11-07: the order page's location picker offers Dallas among its options | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Dallas, US
  - [1] 2026-11-07: the plan table still prices the next plan at USD 7.00 monthly | capture: sha256:effd39f039e687195bb8d147dcf65095a5420516e6c378f6b6ee44df766afe9f | quote: $7.00/mo
  - [5] 2026-11-07: the entry plan price is unchanged on the order page | capture: sha256:e817cd45308b6c4d06df764a5c6588c143a14cf132bbb742300b4964e876921b | quote: Monthly$5.00 USD Quarterly$15.00 USD Semi-Annually$30.00 USD Annually$60.00 USD
- sources:
  - [1] https://vpsdime.com/linux-vps
  - [2] https://vpspricetracker.com/provider/VPSDime/vps
  - [3] https://vpsdime.com/storage-vps
  - [4] https://vpsdime.com/storage-vps/
  - [5] https://vpsdime.com/buy/linux4gb
