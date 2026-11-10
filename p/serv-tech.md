# ServTech

> serv-tech.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serv-tech/ | JSON https://fshy.ajam.dev/api/v1/entity/serv-tech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ServTech

- `compute/servtech` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T08:51:31.856Z (live) | stale on 2026-12-08
- url https://serv-tech.ru/vps/
- free tier: RUB 500 per month for MSK-PRO-1: 1 vCPU at 2.50 GHz, 2 GB RAM, 25 GB NVMe, up to 500 Mbit/s, Moscow, KVM, with administration help included. The page's own floor is RUB 400 per month when 24 months are paid up front. The three larger rows are RUB 1,000 (2 vCPU / 4 GB / 50 GB), RUB 1,900 (4 vCPU / 8 GB / 100 GB) and RUB 3,600 (8 vCPU / 16 GB / 200 GB), all at 2.50 GHz and 500 Mbit/s. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: up to 500 Mbit/s per row, no byte allowance and no overage price stated | metered: no | source: [1]
- identity: any-phone | detail: the register form asks for a name, an email address, a password and a phone number, plus payer country, ZIP, city and address; the phone field carries a country selector; no card or ID…
- interface: rest
- limits:
  - per-ip-shaping (binding): Every row is stated as a 500 Mbit/s channel with no per-byte payment and no monthly volume cap; the channel is shared, constant maximum load 24/7 is not allowed, and a speed restriction is possible after prolonged excessive load. [1]
- limits note: Every row is stated as a 500 Mbit/s channel with no per-byte payment and no monthly volume cap; the channel is shared, constant maximum load 24/7 is not allowed, and a speed restriction is possible after prolonged excessive load.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order through my.serv-tech.ru (BILLmanager); no API documented on the page read
- composes with: Two gigabytes and 25 GB of NVMe in Moscow at RUB 500 with administration included is the cheapest row among documented hosts that carries a support commitment, which matters where a broken box costs a day
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor page. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 25
  - monthly_price: RUB 500 per month for MSK-PRO-1 ('500 ₽ за 1 месяц'); RUB 1,000 (MSK-PRO-2), RUB 1,900 (MSK-PRO-3) and RUB 3,600 (MSK-PRO-4)
  - annual_price: not published: the page prints the 24-month floor and the 1-month price only; the footnote says the term and the total are confirmed in the personal cabinet at checkout
  - renewal_price: not published: no page read prints a renewal price
  - billing_term: 1 to 24 months; the page prints the 1-month price (RUB 500 for MSK-PRO-1) and the 24-month floor (RUB 400 per month); the term total is confirmed at checkout
  - stock: no stock state is printed on the page; every row shows a live order link
  - cart_price: unverified: behind a sign-up - the BILLmanager order form answers an Authorization page with no price (probe:cart-servtech-3448)
- evidence:
  - [1] 2026-10-23: cheapest row quoted: 'MSK-PRO-1', '500 ₽ / мес.', '1 vCPU × 2.50 GHz', '2 ГБ RAM', '25 ГБ NVMe', 'до 500 Мбит/с', 'Помощь с администрированием', 'Россия · Москва'
  - [1] 2026-10-23: floor quoted: 'от 400 ₽ / мес. при оплате за 24 месяца'; larger rows 'MSK-PRO-2 1000 ₽ / мес.', 'MSK-PRO-3 1900 ₽ / мес.', 'MSK-PRO-4 3600 ₽ / мес.'
  - [1] 2026-11-07: the MSK-PRO-1 card prices the 1-month term at 500 ₽ | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: 500 ₽ за 1 месяц
  - [1] 2026-11-07: the page defers the term total to the checkout | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: Показана стоимость за месяц и за весь выбранный период. Срок оплаты и итоговую сумму подтвердите в личном кабинете при оформлении.
  - [1] 2026-11-07: the footnote lists what the checkout confirms; a renewal price is not among them | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: Показана стоимость за месяц и за весь выбранный период. Срок оплаты и итоговую сумму подтвердите в личном кабинете при оформлении.
  - [1] 2026-11-07: the page prints the 24-month floor | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: от 400 ₽ / мес.при оплате за 24 месяца
  - [1] 2026-11-07: the MSK-PRO-1 order link is live | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: [Заказать сервер](https://my.serv-tech.ru/billmgr?func=register&redirect=startpage%3Dvds%26startform%3Dvds%252Eorder%26pricelist%3D3448%26project%3D1)
  - probe:cart-servtech-3448 2026-11-07: the cart answers an Authorization page and prints no price | capture: sha256:4f9e1941fdf126c005d298cc3116d69525f44d930051dc4fb09af2840095dbef | quote: "title": "Authorization"
  - [2] 2026-11-07: the register form requires a phone number | capture: sha256:8900c97c5649e929da06e9cef95353c7bea4f9b7817329eca1f1218d1743f042 | quote: Name\* Email address \* Password\* Re-enter the password Phone number \*
  - [2] 2026-11-07: the register form's required fields, read 2026-11-07 | capture: sha256:8900c97c5649e929da06e9cef95353c7bea4f9b7817329eca1f1218d1743f042 | quote: Name\* Email address \* Password\* Re-enter the password Phone number \* ZIP code\* City\* Address\*
  - [1] 2026-11-07: the MSK-PRO-1 shape and port are unchanged on 2026-11-07 | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: 1 vCPU × 2.50 GHz Память 2 ГБ RAM Накопитель 25 ГБ NVMe Канал до 500 Мбит/с
  - [1] 2026-11-07: the channel footnote: no per-megabyte payment and no monthly volume cap; the channel is shared, constant maximum load 24/7 is barred, and prolonged excessive load may bring a speed restriction | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: Без помегабайтной оплаты и ежемесячного лимита объёма. Канал общий: постоянная максимальная загрузка 24/7 не допускается, при длительной чрезмерной нагрузке возможно ограничение скорости.
  - [1] 2026-11-07: the MSK-PRO-1 card: 1 vCPU at 2.50 GHz, 2 GB RAM, 25 GB NVMe, channel up to 500 Mbit/s | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: 1 vCPU × 2.50 GHz Память 2 ГБ RAM Накопитель 25 ГБ NVMe Канал до 500 Мбит/с
  - [1] 2026-11-07: the MSK-PRO-1 card prices 500 ₽ for 1 month with the 1 vCPU / 2 GB RAM / 25 GB NVMe shape and the up-to-500-Mbit/s channel | capture: sha256:f7cd26c24837d51f1908f98f9c9de77404a9411f91af50843abe2a2bfc579366 | quote: MSK-PRO-1 500₽ / мес. 500 ₽ за 1 месяц Процессор 1 vCPU × 2.50 GHz Память 2 ГБ RAM Накопитель 25 ГБ NVMe Канал до 500 Мбит/с
- sources:
  - [1] https://serv-tech.ru/vps/
  - [2] https://my.serv-tech.ru/billmgr?func=register&lang=en&redirect=pricelist%3D3448%26project%3D1%26startform%3Dvds%252Eorder%26startpage%3Dvds
