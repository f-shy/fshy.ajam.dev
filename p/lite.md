# LITE.HOST

> lite.host | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lite/ | JSON https://fshy.ajam.dev/api/v1/entity/lite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LITE.HOST

- `compute/lite-host` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T17:40:53.065Z (live) | stale on 2026-12-08
- url https://lite.host/vds
- price parsed USD 3.51/mo
- free tier: RUB 285 per month for the Kallisto row: 1 vCPU, 1024 MB RAM, 10 GB SSD, up to 200 Mbit/s, Moscow. Pluto is RUB 350 for the same shape with 20 GB. The page's configurator shows '5 GB SSD' at RUB 252.5 per month, and the page's meta description states a floor of RUB 159.38 per month; no row at that floor was found on the page read. The page states unlimited traffic at up to 200 Mbit/s, weekly backups to a separate data centre, and a free WAF+ plan. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic at up to 200 Mbit/s; no byte allowance and no overage price stated | metered: no | source: [1]
- identity: email | detail: the order page's account section requires first name, last name, email and password; an optional company branch asks for entity name, phone, INN and KPP (read 2026-11-07)
- interface: rest
- limits:
  - per-ip-shaping (binding): Traffic is stated as unlimited at up to 200 Mbit/s, so the port is the wall; the page publishes no byte allowance and no throttle-after-allowance term. [1]
- limits note: Traffic is stated as unlimited at up to 200 Mbit/s, so the port is the wall; the page publishes no byte allowance and no throttle-after-allowance term.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: own control panel with power control, OS reinstall and a resource-health view; no API documented on the page read
- composes with: The 5 GB configurator row at RUB 252.5 is the cheapest Moscow box that still states a backup copy in a second data centre, which is the difference between a lost disk and a lost day
- reliability: no reliability event recorded
- notes: Source: vps.today index row ('LITE.HOST | 10 GB SSD | 1 GB | 1 x 2.4 GHz | 200 Mbit/s | ( ) KVM IPv6 DDoS ! | 285 .'), then the vendor page. The RUB 159.38 floor in the meta description has no matching row on the page read and stays unverified. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - monthly_price: RUB 285 per month for the Callisto plan in Moscow; the order page prices the same plan 285 RUB monthly
  - annual_price: RUB 2907 per year: the order page with the annual cycle prints 'Стоимость сервера 2907 ₽ в год'
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: monthly by default; the order form's cycle selector offers quarterly at 5 percent off, semi-annual at 10 percent and annual at 15 percent
  - stock: orderable: the order form renders the plan with its cycle selector and continue button, and no out-of-stock marker
  - cart_price: RUB 285 per month at the monthly cycle: the order page is the checkout (account data and payment on the same page) and prices the plan before an account exists
  - price_on_page: RUB 285/month for the Kallisto VPS (Callisto)
  - renewal_usd: not published: the order page prints the cycle price and no renewal figure
- evidence:
  - [1] 2026-10-23: cheapest named row quoted: 'Каллисто … 1 vCPU … 1024 МБ … 10 ГБ SSD … до 200 мбит/с … 285 ₽ / мес.', 'Плутон … 20 ГБ SSD … 350 ₽ / мес.'; configurator 'ДИСКОВОЕ ПРОСТРАНСТВО - 5 ГБ SSD 252.5 ₽ в месяц'
  - [1] 2026-10-23: meta description quoted: 'стоимостью от 159.38 рублей в месяц'; body 'Размещение в проверенных дата-центрах Москвы', 'Неограниченный трафик на скорости до 200 мбит/с'; hardware 'HP и SuperMicro с процессорами Intel и SSD корпоративного уровня'
  - [2] 2026-11-07: the Callisto order page prices the server 285 RUB per month | capture: sha256:9f6105c8b70ef32bc8f06ca49040917c130a9abd81ee2e8b46fb23f1b921a880 | quote: Стоимость сервера 285 ₽ в месяц
  - [3] 2026-11-07: the order page prices the annual term 2907 RUB | capture: sha256:35bfd72812e614d205ac1ee210b45d6515500ad914839dc7c05bdd5161af993b | quote: Стоимость сервера 2907 ₽ в год
  - [2] 2026-11-07: the order page prints the cycle price and no renewal figure | capture: sha256:9f6105c8b70ef32bc8f06ca49040917c130a9abd81ee2e8b46fb23f1b921a880 | quote: Стоимость сервера 285 ₽ в месяц
  - [2] 2026-11-07: the cycle selector prints the annual option at 15 percent off | capture: sha256:bd4f6fcb675de54c3d310425e54ad981699b020fce639aa6f745a162e8c4804c | quote: <option value="annually" >Ежегодно (15% скидка)</option>
  - [3] 2026-11-07: the order form renders its continue button; no out-of-stock marker | capture: sha256:35bfd72812e614d205ac1ee210b45d6515500ad914839dc7c05bdd5161af993b | quote: Продолжить
  - [2] 2026-11-07: the checkout page prices the plan 285 RUB monthly | capture: sha256:9f6105c8b70ef32bc8f06ca49040917c130a9abd81ee2e8b46fb23f1b921a880 | quote: Стоимость сервера 285 ₽ в месяц
  - [2] 2026-11-07: the order form's required email field | capture: sha256:bd4f6fcb675de54c3d310425e54ad981699b020fce639aa6f745a162e8c4804c | quote: <input type="email" name="mail" required="" placeholder="Почтовый ящик" autocomplete="off">
  - [1] 2026-11-07: the entry plan's shape and price are unchanged on 2026-11-07 | capture: sha256:f0dae3fb0cc3d4f7e43d35d2c7845f3501d748da96c2e1595f860f2b3916c610 | quote: - 1 vCPU - 1024 МБ - 10 ГБ SSD - до 200 мбит/с - 285 ₽ / мес.
  - [2] 2026-11-07: the order page prices the Kallisto server RUB 285 per month | capture: sha256:9f6105c8b70ef32bc8f06ca49040917c130a9abd81ee2e8b46fb23f1b921a880 | quote: Стоимость сервера 285 ₽ в месяц
- sources:
  - [1] https://lite.host/vds
  - [2] https://lite.host/order/vds/callisto/monthly
  - [3] https://lite.host/order/vds/callisto/annually
