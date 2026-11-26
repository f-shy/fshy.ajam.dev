# WebHOST1

> webhost1.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webhost1/ | JSON https://fshy.ajam.dev/api/v1/entity/webhost1.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WebHOST1

- `compute/webhost1` | trial-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T05:18:26.148Z (live) | stale on 2026-12-26
- url https://webhost1.ru/vps-vds/test
- free tier: Two free routes rather than a free tier. The first is a 30-day money-back trial: an individual registers, fills the profile and pays for the chosen tariff, then requests a refund inside 30 days of the order; the refund is 100 percent in the first month and from the second month covers only the unspent remainder, once per account, excluding PROMO tariffs. Legal entities register, send a scan of the taxpayer number and a letter on company letterhead to obtain a 30-day test. The second route is 60 days free, described as two months at no charge, when migrating from another hosting company. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: money-back-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a paid order up front and a card to make it, because the trial is a refund rather than a free period: 'individuals pay for the service and get a 100 percent refund within 30 days once per account'. Payment runs through Robokassa, which takes foreign bank cards with a minimum of RUB 1,000, and the vendor lists the countries whose cards it refuses, including Azerbaijan, the United States, Ukraine, Turkey and Venezuela. No hold amount is stated, and whether a debit or prepaid card is accepted is not stated. A legal entity instead sends a taxpayer-number scan and a company letter for a 30-day test.
- interface: unknown
- limits:
  - per-ip-shaping (binding): The 100 Mbit/s port is the ceiling on every tariff up to the top of the range, so a 24/7 transfer job tops out at about 1.08 TB a day before anything else binds; the free part is a refund window rather than capacity, and it is once per account. [1]
- limits note: The 100 Mbit/s port is the ceiling on every tariff up to the top of the range, so a 24/7 transfer job tops out at about 1.08 TB a day before anything else binds; the free part is a refund window rather than capacity, and it is once per account.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A foreign-card payment path plus a refund window is the useful composition: RUB 1,000 is the minimum top-up and covers 3.5 months of the cheapest plan, so a 30-day paid month that is then refunded costs a card authorisation and nothing else, and the migration route adds a second free 60 days if there is an older invoice to show.
- reliability: no reliability event recorded
- notes: The 'free VPS on 60 days' banner is a migration offer, not a tier: it needs an existing service elsewhere, which is a real constraint rather than a detail. Arithmetic: 336 x 12 = 4,032; 285.60 x 12 = 3,427.20; 1,000 / 285.60 = 3.5 months. Not established: whether the refund is paid back to a foreign card or only to the internal balance, and whether the migration offer requires proof of the previous invoice.
- extras:
  - facets.class: regional-low-floor
  - facets.free_tier_kind: money-back-trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 20
  - facets.shape.port_mbit: 100
- evidence:
  - [1] 2026-10-22: individuals pay for the service and get a 100 percent refund within 30 days once per account, legal entities send a taxpayer-number scan and a company letter for a 30-day test, and migration from another host gives two months free, quoted and translated
  - [2] 2026-10-22: RU SSD 20 at RUB 285.60 a month for 1 core at 2.8 GHz, 2 GB RAM, 20 GB disk and a 100 Mbit/s port, listed at RUB 4,032 for 12 months before a 15 percent discount to RUB 3,427.20; extra IP RUB 157.50 a month, +1 GB RAM RUB 300 a month, +1 core RUB 300 a month, quoted
  - [3] 2026-10-22: payment through Robokassa includes foreign bank cards with a minimum of RUB 1,000, the commission was removed, and the article lists the countries whose cards are refused, including Azerbaijan, the United States, Ukraine, Turkey and Venezuela, quoted and translated
  - [1] 2026-11-25: registration, payment up front, the 30-day request, the first-month 100 percent refund, the second-month unspent-remainder refund and the once-per-account limit | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: - Зарегистрируйтесь, заполните профиль и оплатите услугу по выбранному тарифу; - Если вы хотите сделать возврат, необходимо в течении 30 дней с момент оформления услуги, написать запрос в поддержку в личном кабинете; - В течении первого месяца осуществляем 100% возврат средств. На втором месяце и далее, осуществляется возврат только остатка неизрасходованных средств; - 100% возврат осуществляется один раз на лицевой счет и только для клиентов с заполненным профилем лицевого счета.
  - [1] 2026-11-25: the service is paid up front and a full refund is available if the customer is dissatisfied within 30 days | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: Оплатите услугу VDS/VPS. Сделаем полный возврат средств, если в течение 30 дней вас что-то не устроит.
  - [1] 2026-11-25: the test is available once per account | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: С одного лицевого счета можно однократно протестировать услугу VDS/VPS.
  - [1] 2026-11-25: the refund does not apply to PROMO plans | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: Не распространяется на тарифы PROMO.
  - [1] 2026-11-25: individuals register, fill the profile and pay for the chosen plan before the refund applies | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: - Зарегистрируйтесь, заполните профиль и оплатите услугу по выбранному тарифу;
  - [1] 2026-11-25: legal entities send a taxpayer-number scan and a letter on company letterhead for a 30-day test | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: - Пришлите скан-копию ИНН и заявление на фирменном бланке в произвольной форме о предоставлении VDS с тестовым периодом 30 дней.
  - [2] 2026-11-25: the second route is two months free when moving from another hosting company | capture: sha256:dd0a2ceb3e7a82ab7b4f158d43daab687e5030caab7fdcb06b0803b1a7d2f9a9 | quote: Бесплатный VDS на 60 дней При переезде из другой хостинг компании 2 месяца бесплатно.
  - [2] 2026-11-25: the RU SSD 20 plan is listed at RUB 607.75 per month | capture: sha256:dd0a2ceb3e7a82ab7b4f158d43daab687e5030caab7fdcb06b0803b1a7d2f9a9 | quote: Тариф «RU SSD 20» 607.75 ₽ Цена за месяц
  - [1] 2026-11-25: the refund is 100 percent in the first month and only the unspent remainder from the second month, unchanged | capture: sha256:d80dbb1f94da0303f21418fc84c0bc221b5e50d419b1684c637b4270c7be2976 | quote: В течении первого месяца осуществляем 100% возврат средств. На втором месяце и далее, осуществляется возврат только остатка неизрасходованных средств;
- sources:
  - [1] https://webhost1.ru/vps-vds/test
  - [2] https://webhost1.ru/vds/ssd/vps-vds-ru
  - [3] https://webhost1.ru/help/articles/general-information/webhost1-oplata-serverov-cherez-robokassa-teper-bez-komissii.html
