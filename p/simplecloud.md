# SIMPLE CLOUD

> simplecloud.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simplecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/simplecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SIMPLE CLOUD

- `compute/simple-cloud` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T06:08:49.242Z (live) | stale on 2026-12-08
- url https://simplecloud.ru/price/
- free tier: RUB 216 per month: 512 MB RAM, 1 CPU core, 5 GB SSD, 250 GB traffic, no hourly billing. The first paid step after that is RUB 360 per month (RUB 0.58 per hour) for 1 GB RAM, 1 core, 20 GB SSD and unlimited traffic. Above the 250 GB allowance the page states traffic is charged at RUB 1 per GB. The largest row is RUB 23,040 per month for 64 GB RAM, 8 cores and 400 GB SSD. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 250 GB a month on the RUB 216 row counted in both directions, then RUB 1 per GB; all larger rows unlimited | metered: yes | free allowance: 250 GB per month on the smallest row | price per TB: RUB 1 per GB beyond the allowance | source: [1]
- identity: email | detail: the order button opens a registration popup asking for an email address and a password; no card or phone field
- interface: unknown
- limits:
  - volume-quota (binding): 250 GB a month on the RUB 216 row, counted in both directions, then RUB 1 per GB. Every row above the first states unlimited traffic, so the smallest plan is also the only metered one. [1]
- limits note: 250 GB a month on the RUB 216 row, counted in both directions, then RUB 1 per GB. Every row above the first states unlimited traffic, so the smallest plan is also the only metered one.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: RUB 216 for 512 MB is the lowest monthly floor among documented hosts and needs no hourly commitment, which makes it the cheapest place to keep a tiny always-on poller that must not be reaped
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor price page. The page names no location, so the location of this row is unverified. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 5
  - monthly_price: RUB 216 per month for the 512 MB / 1 core / 5 GB SSD / 250 GB traffic row; the ladder runs RUB 360, 720, 1,440, 2,880, 5,760, 11,520 and 23,040 per month
  - annual_price: not published: the page prints only monthly and hourly rates
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: monthly; the RUB 216 row has no hourly billing, the larger rows also print hourly rates
  - stock: no stock state is printed on the page; every row shows a live select link
  - cart_price: unverified: behind a sign-up - the select buttons open a registration popup email, password
- evidence:
  - [1] 2026-10-23: cheapest row quoted: '216 рублей в месяц почасовая тарификация отсутствует', '512MB RAM', '1 ядро CPU', '5GB SSD диск', '250GB трафик'; second row '360 рублей в месяц 58 копеек в час' with '1GB RAM', '20GB SSD диск', 'Безлимитный трафик'
  - [1] 2026-10-23: footnote quoted: 'Учитывается входящий и исходящий трафик. При достижении лимита, трафик рассчитывается из учета 1 рубль за 1GB'; top row '23040 рублей в месяц' with '64GB RAM', '8 ядер CPU', '400GB SSD диск'
  - [1] 2026-11-07: the cheapest row prints 216 рублей в месяц with no hourly billing | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: 216 рублей в месяц почасовая тарификация отсутствует
  - [1] 2026-11-07: the next row prices by month and by hour; no annual figure appears | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: 360 рублей в месяц 58 копеек в час
  - [1] 2026-11-07: the cheapest row's block carries no renewal figure | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: 216 рублей в месяц почасовая тарификация отсутствует
  - [1] 2026-11-07: the larger rows print hourly rates beside the monthly one | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: 360 рублей в месяц 58 копеек в час
  - [1] 2026-11-07: every plan card ends in a live select link | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: Выбрать
  - [1] 2026-11-07: choosing a plan opens a registration popup, not a cart with a price | capture: sha256:c5d866159fdf48a250e20d272a318e16b1921f5ae442e793267e242e55f3d140 | quote: Простая регистрация
  - [1] 2026-11-07: the popup's account-type rule, read 2026-11-07 | capture: sha256:c5d866159fdf48a250e20d272a318e16b1921f5ae442e793267e242e55f3d140 | quote: Смена типа аккаунта с юридического лица на физическое будет невозможна.
  - [1] 2026-11-07: the traffic footnote and the row prices are unchanged on 2026-11-07 | capture: sha256:9c4c3992d487dd1c8d5db6d482efbc3f5c24bc65eaaf47db61515f86776b848c | quote: * Учитывается входящий и исходящий трафик. При достижении лимита, трафик рассчитывается из учета 1 рубль за 1GB
- sources:
  - [1] https://simplecloud.ru/price/
