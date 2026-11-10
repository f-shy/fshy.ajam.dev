# Koara Cloud

> koara.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/koara/ | JSON https://fshy.ajam.dev/api/v1/entity/koara.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Koara Cloud

- `compute/koara-cloud` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:47.347Z (live) | stale on 2026-12-08
- url https://koara.io/ru/products/vds
- free tier: RUB 279 per month for START-1 in Germany: 1 core of a Ryzen 9 3900, 1 GB RAM, 15 GB NVMe, unlimited traffic, 100 Mbps port, KVM, L3/L4 DDoS protection included. The next rows are START-2 at RUB 479 (1 core / 2 GB / 30 GB / 250 Mbps) and DE-1 at RUB 459 (Ryzen 9 5950X, 1 core / 2 GB / 32 GB / 1000 Mbps). The largest DE row is RUB 2,199 for 6 cores, 16 GB, 128 GB and 1000 Mbps. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic on every row, 100 Mbps on START-1; no throttle-after-allowance term stated | metered: no | source: [1]
- identity: email | detail: unverified: the order entry is a registration redirect and the register form sits behind a JavaScript challenge; its fields are not established (read 2026-11-07)
- interface: rest
- limits:
  - per-ip-shaping (binding): Traffic is stated as unlimited on every row, so the wall is the port: 100 Mbps on START-1 against 250 Mbps and 1000 Mbps further up the table, with no byte allowance and no throttle term stated. [1]
- limits note: Traffic is stated as unlimited on every row, so the wall is the port: 100 Mbps on START-1 against 250 Mbps and 1000 Mbps further up the table, with no byte allowance and no throttle term stated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: control panel with OS reinstall, 1-2 minute provisioning, custom ISO; no API documented on the page read
- composes with: A Ryzen 9 3900 core, 15 GB of NVMe and an unlimited 100 Mbps port in Germany for RUB 279 is a better per-ruble shape than any metered German row among evaluated providers, if the port is enough.
- reliability: no reliability event recorded
- notes: Source: vps.today index row ('Koara Cloud | 15 GB NVMe | 1 GB | 1 x 3.1 GHz | 100 Mbit/s | KVM DDoS | 279 .'), then the vendor page, which prices the same row at RUB 279. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - monthly_price: RUB 279 per month for START-1 (Ryzen 9 3900, 1 vCore) in Germany; the vendor's own plans API prices the same row 279 RUB monthly and marks it available
  - annual_price: not published: no page read prints an annual figure; the plans API names only price_monthly and the BILLmanager cart sits behind registration and a JavaScript challenge
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: monthly: the page prices every row '₽/ мес' (per month) and the plans API names only price_monthly
  - stock: in stock: the plans API states unavailable: false for START-1 and the page renders an active order button
  - cart_price: unverified: behind a sign-up - the order entry is a registration redirect on the vendor's BILLmanager panel and the panel answers a JavaScript challenge to every text reader; a warmed-cookie cart read answered with no price; routes tried 2026-11-07: the direct capture, six reader pins, three further pins, and the Wayback and Cloudflare archive
- evidence:
  - [1] 2026-10-23: cheapest row quoted: 'START-1', 'CPU Ryzen 9 3900 vCPU 1 ядро RAM 1 ГБ NVMe SSD 15 ГБ Трафик∞ Скорость 100 Mbps', '279 ₽/ мес', location 'Германия'
  - [1] 2026-10-23: rows 'START-2 … 250 Mbps … 479 ₽/ мес', 'DE-1 … Ryzen 9 5950X … 1000 Mbps … 459 ₽/ мес', 'DE-4 … 6 ядер RAM 16 ГБ NVMe SSD 128 ГБ … 2199 ₽/ мес'; 'Бесплатная защита от DDoS-атак на уровне L3/L4 на всех тарифах без ограничений по трафику'
  - [1] 2026-11-07: the plan card prices START-1 at 279 RUB per month | capture: sha256:82378388b705694672a1764fadb1fe7185c3066aa0b3c6a1a55d53cd2ff8c0d9 | quote: 279 ₽/ мес
  - [2] 2026-11-07: the vendor's plans API carries one monthly price for the row and no annual figure | capture: sha256:f55f0cbd6ceb493ee9902c13dc7c4edaba7ecebc284c1ee39776c112624642d5 | quote: "price_monthly":279,"ram_mb":1024,"vcpu":1,"port_speed_mbps":100,"unavailable":false,"cpu_model":"Ryzen 9 3900","name":"START-1"
  - [2] 2026-11-07: the plans API prints a monthly price and no renewal figure | capture: sha256:f55f0cbd6ceb493ee9902c13dc7c4edaba7ecebc284c1ee39776c112624642d5 | quote: "price_monthly":279,"ram_mb":1024,"vcpu":1,"port_speed_mbps":100,"unavailable":false,"cpu_model":"Ryzen 9 3900","name":"START-1"
  - [1] 2026-11-07: the page prices the plan per month | capture: sha256:82378388b705694672a1764fadb1fe7185c3066aa0b3c6a1a55d53cd2ff8c0d9 | quote: 279 ₽/ мес
  - [2] 2026-11-07: the vendor's plans API marks START-1 available | capture: sha256:f55f0cbd6ceb493ee9902c13dc7c4edaba7ecebc284c1ee39776c112624642d5 | quote: "price_monthly":279,"ram_mb":1024,"vcpu":1,"port_speed_mbps":100,"unavailable":false,"cpu_model":"Ryzen 9 3900","name":"START-1"
  - probe:cart-koara-pricelist 2026-11-07: a warmed-cookie read of the BILLmanager pricelist answered 200 with no price string | capture: sha256:631526d51573e01186159bfc03eb3260261191a2021439a5fa6a27d03954e266 | quote: "verdict": "no-price"
  - [2] 2026-11-07: the order entry is a registration redirect | capture: sha256:f55f0cbd6ceb493ee9902c13dc7c4edaba7ecebc284c1ee39776c112624642d5 | quote: "url":"https://my.koara.io/billmgr?func=register&redirect=startpage%3Dvds%26startfrom%3Dvds%252Eorder%26pricelist%3D339%26project%3D2"
  - [2] 2026-11-07: the vendor's own plans API sends the START-1 order button to a registration redirect (pricelist 339) | capture: sha256:f55f0cbd6ceb493ee9902c13dc7c4edaba7ecebc284c1ee39776c112624642d5 | quote: "url":"https://my.koara.io/billmgr?func=register&redirect=startpage%3Dvds%26startfrom%3Dvds%252Eorder%26pricelist%3D339%26project%3D2"
  - [3] 2026-11-07: the BILLmanager panel serves a JavaScript challenge that computes a cookie before content | capture: sha256:d403ea289f4b4efcb19d7d3744a3525bd56dc189d54ebd393e9cee5add9ead42 | quote: document.cookie = "__jhash_=" + jhash
  - [1] 2026-11-07: the entry plan's price is unchanged on 2026-11-07 | capture: sha256:82378388b705694672a1764fadb1fe7185c3066aa0b3c6a1a55d53cd2ff8c0d9 | quote: 279 ₽/ мес
- sources:
  - [1] https://koara.io/ru/products/vds
  - [2] https://api.koara.io/products/vds/de
  - [3] https://my.koara.io/billmgr?func=vds.order.pricelist
