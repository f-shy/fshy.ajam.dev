# IT-garage

> it-garage.pro | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/it-garage/ | JSON https://fshy.ajam.dev/api/v1/entity/it-garage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IT-garage

- `compute/it-garage` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://it-garage.pro/
- free tier: RUB 218 per month for 10 GB SSD, 1 GB RAM, 1 core at 2 GHz, 150 Mbit/s port, Germany, per the index row; the vendor homepage carries no plan table. The vendor states the hardware: AMD Ryzen 9 5950X overclocked to 5 GHz on the RZ-W line, Intel Xeon Gold 6138 and Intel Xeon 2697v4 on the PROMO line, Intel Xeon W-2295 in Finland, in European Union data centres, with a 120-second provisioning claim and free basic DDoS protection. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 150 Mbit/s port per the index row; no byte allowance stated on either page read | metered: no | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): The index row states a 150 Mbit/s port and no byte allowance, so the port is the wall; the vendor page states neither a port speed nor an allowance, so what happens at saturation is unverified. [1]
- limits note: The index row states a 150 Mbit/s port and no byte allowance, so the port is the wall; the vendor page states neither a port speed nor an allowance, so what happens at saturation is unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: self-service panel at my.it-garage.pro for OS install and resource change; no API documented on the page read
- composes with: A Ryzen 9 5950X core at RUB 218 is the highest single-core clock among evaluated providers, which matters for a single-threaded scraper that cannot parallelise.
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor homepage. The homepage sells and does not price, so the record is reported. verification criteria: the order form's cheapest configuration. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
- evidence:
  - [1] 2026-10-23: homepage read renders no price table: it lists 'Тарифы виртуальных серверов' and then the hardware 'AMD Ryzen 9 5950x OC до 5 ГГц (RZ-W), а также Intel Xeon Gold 6138 и Intel Xeon 2697v4 на тарифах линейки PROMO и Intel Xeon(R) W-2295 в Финляндии', 'Современные серверы в лучших дата-центрах Европейского Союза', 'Создайте виртуальный сервер за 120 секунд'
  - [2] 2026-10-23: index row quoted: 'IT-garage | 10 GB SSD | 1 GB | 1 x 2 GHz | 150 Mbit/s | Германия KVM IPv6 DDoS | 218 руб.'
- sources:
  - [1] https://it-garage.pro/
  - [2] https://vps.today/
