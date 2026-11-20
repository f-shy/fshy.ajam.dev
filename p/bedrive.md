# BeDrive.ru

> bedrive.ru | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bedrive/ | JSON https://fshy.ajam.dev/api/v1/entity/bedrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BeDrive.ru

- `debrid/bedrive-ru` | fails-identity | evidence documented | binding none | category Russian file host with a ruble-only premium tier | tier Премиум аккаунт
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:17:03.493Z (live) | stale on 2026-11-23
- url https://bedrive.ru/upgrade.html
- price RUB 250 one-off, period unstated
- free tier: Free upload and download with ads, a wait, limited simultaneous downloads and limited speed; the premium page sells the removal of each. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No free storage quota is printed; premium is described as 'Безлимитное пространство без ограничений'.
- per-object cap: not stated on the pages read | source: [1] | note: unstated
- retention: not stated on the pages read | source: [1] | note: unstated
- egress: Premium buys 'Прямые загрузки. Без ожидания', 'Возможна максимальная скорость загрузки', 'Нет ограничений на количество скачиваний' and 'Неограниченное хранилище'. No byte quota. | metered: no | free allowance: free tier with waits and caps | source: [1]
- identity: card | detail: Only one rail is named: 'Безопасная оплата через ЮMoney' (secure payment via YooMoney), under a button that says 'Оплатить картой и получить доступ'. YooMoney is a Russian wallet, so the practical gate is a Russian payment method. | country: Russia
- interface: unknown
- limits:
  - per-ip-shaping: free tier: wait plus limited speed; premium removes both [1]
  - volume-quota: premium is sold flat at RUB 250 with 'Неограниченное хранилище' - no byte or time unit is stated [1]
- limits note: The page does not say whether RUB 250 buys a month, a year or forever; 'Без подписок' (no subscriptions) is the only term given.
- binding note: Nothing at 1 TiB/month can be named from the vendor's text because no unit or period is attached to the RUB 250. The decisive constraint is the payment rail, recorded below.
- interface detail: Web upload page (index.html?upload=1), account, link checker. No API or mount documented.
- tooling: Browser only as documented; the premium pitch names 'Поддержка менеджера загрузок' (download manager support), which is the one programmatic-ish path.
- composes with: A small Russian host; it is useful only as a place a Russian-language release was posted, and it does not fetch from anywhere else.
- reliability: A RUB 250 one-off payment with no stated period and no subscription is unverifiable from the page; a buyer cannot tell what they are buying beyond 'access'.
- notes: The cleanest example of the debrid payment wall on the Russian side: a host that sells unlimited everything for RUB 250 and cannot take a foreign card at all. For a user outside Russia the price is irrelevant because the rail is closed. No conversion is offered because the vendor states no period.
- evidence note: The price, the single payment rail and the feature list are quoted from the live page today. What the price buys in time is not stated by the vendor, so it is not inferred here.
- evidence:
  - [1] 2026-10-23: 'К оплате: 250 руб.', 'Безопасная оплата через ЮMoney.', 'Без подписок.', and the premium feature list including unlimited storage and unlimited download count
- sources:
  - [1] https://bedrive.ru/upgrade.html
