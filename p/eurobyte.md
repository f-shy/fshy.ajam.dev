# Eurobyte

> eurobyte.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eurobyte/ | JSON https://fshy.ajam.dev/api/v1/entity/eurobyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Eurobyte

- `compute/eurobyte` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:43.797Z (live) | stale on 2026-12-08
- url https://eurobyte.ru/services/vds/
- free tier: RUB 14 per day, RUB 290 per month or RUB 2900 per year for K-512 Lite: 1 core, 512 MB RAM, 10 GB NVMe, KVM, 1 dedicated IP, unlimited traffic, CentOS/Debian/Ubuntu, with a ten-day minimum on a first order; the page's own per-card data prints the month and year price of every tariff. The ladder, day / month / year in RUB: K-512 20 / 400 / 4000 (512 MB, 15 GB, five-day minimum), K-1024 Lite 22 / 430 / 4300 (1 GB, 20 GB), K-1024 30 / 645 / 6450 (1 GB, 30 GB), K-2048 Lite 34 / 666 / 6660 (2 GB, 40 GB), K-2048 46 / 999 / 9990 (2 GB, 60 GB), K-4096 Lite 60 / 1190 / 11900 (4 GB, 80 GB), K-4096 82 / 1780 / 17800 (4 GB, 120 GB), K-8192 Lite 114 / 2270 / 22700 (8 GB, 160 GB), K-8192 160 / 3405 / 34050 (8 GB, 240 GB). The page's prose states a monthly floor of 145 rubles and its meta description a daily floor of 6.75, which no row matches. Renewal price: not published on the page read. No sold-out marker; every card renders an order button. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: stated as unlimited; 1.5 Tbps is an aggregate data-centre figure, not a per-server port; no allowance or overage price | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): Traffic is stated as unlimited and the page describes a 1.5 Tbps aggregate uplink without a per-port figure, so the wall is unstated; no byte allowance and no port cap appear on the page read. [1]
- limits note: Traffic is stated as unlimited and the page describes a 1.5 Tbps aggregate uplink without a per-port figure, so the wall is unstated; no byte allowance and no port cap appear on the page read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: ispmanager panel offered, FastPanel installable by hand; no API documented on the page read
- composes with: RUB 14 a day with a five-day minimum is the cheapest way among evaluated providers to hold a 512 MB box for a week, which is the shape of a one-off crawl.
- reliability: no reliability event recorded
- notes: Source: vps.today index row (' | 10 GB NVMe | 0.5 GB | 1 x 2.2 GHz | 100 Mbit/s | ( ) KVM DDoS TEST | 290 .'), then the vendor page. The vendor page does not name the city; Moscow comes from the index. The RUB 6.75 floor in the meta description is unverified against the rows read. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 15
- evidence:
  - [1] 2026-10-23: cheapest row quoted: 'K-512 Lite', '14 ₽/день', '1 CORE CPU', '512 MB RAM', '15 GB NVME', 'KVM', '1 выделенный IP', 'Первый заказ - минимум на 5 дней'; 'K-1024 Lite 20 ₽/день … 1 GB RAM … 20 GB NVME'
  - [1] 2026-10-23: meta description quoted: 'от 6.75 ₽ в день'; body 'Безлимитный трафик', 'Наш дата-центр имеет суммарную ширину каналов 1.5 Tbps', largest row 'K-8192 160 ₽/день … 4 CORE CPU … 8 GB RAM … 240 GB NVME'
  - [1] 2026-11-07: the entry plan's daily price is unchanged at RUB 14 per day and the page states безлимитный трафик (unlimited traffic) | capture: sha256:3c1420b52d5dfe2bc6b6a291bf370b3434af611965571cc113a40f1bc649de57 | quote: K-512 Lite 14 ₽/день
  - [1] 2026-11-07: the page states that an annual order is cheaper without printing a figure, and its prose states a monthly floor of 145 rubles that no row matches | capture: sha256:3c1420b52d5dfe2bc6b6a291bf370b3434af611965571cc113a40f1bc649de57 | quote: При годовом заказе цена на услугу будет меньше
  - [1] 2026-11-07: the page's own per-card data prices K-512 Lite at 14 a day, 290 a month and 2900 a year with a 10 GB NVMe disk | capture: sha256:f74b87b9044e26ebf410eac007eaff8e973fcc0e5ce022ff8f9b4dc11dcca571 | quote: window.tariff = {"id":"25","title":"K-512 Lite","description":["1 CORE CPU","512 MB RAM","10 GB NVME","KVM"],"type":"vds","is_popular":"0","price_day":"14","price_month":"290","price_3_month":"870","price_6_month":"1650","price_year":"2900","price_3_year":"0","price_install":"0","active":"1"}
  - [1] 2026-11-07: the registration popup asks an e-mail address and nothing else on the form read | capture: sha256:f74b87b9044e26ebf410eac007eaff8e973fcc0e5ce022ff8f9b4dc11dcca571 | quote: <input placeholder="[address removed]" class="input-form__input" type="email">
- sources:
  - [1] https://eurobyte.ru/services/vds/
