# Yandex 360

> yandex.ru | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yandex-3/ | JSON https://fshy.ajam.dev/api/v1/entity/yandex-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yandex 360 "Для профи" (Profi) 3 TB

- `storage/yandex-360-3-tb-the-regional-price-floor-with-unlimited` | qualifies-with-caveat | evidence reported | binding per-object-cap | category consumer-cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://360.yandex.ru/premium-plans/
- price RUB sheet (Russian card): $2.00/TB/mo at 3 TB ($5.99/mo); $3.83/TB/mo at 5 TB ($19.17/mo); $7.27/TB/mo at 10 TB ($72.67/mo). USD sheet (foreign card — the real price): $4.17/TB/mo at 3 TB ($12.50/mo); $4.25/TB/mo at 5 TB ($21.25/mo); $3.17/TB/mo at 1 TB. Family variant: $3.03/TB/mo per… | parsed USD 2/TB-mo
- free tier: 3 TB / 5 TB / 10 TB / 20 TB / 30 TB tiers under Profi. 3 TB is the value tier: 990 ₽/mo list, 495 ₽/mo when paid annually (50 % annual discount is the steady state, not a short promo. The crossed-out 990 ₽ is the monthly rate). Upload per file: 100 GB. Monthly upload ceiling: 3× your Disk size. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per file: 100 GB | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: FREE and explicitly unlimited: the plan comparison table states «Неограниченное скачивание по публичным ссылкам» (unlimited downloading via public links) and «Неограниченный доступ по вашим публичным ссылкам». No per-GB egress line exists anywhere in Yandex 360 consumer pricing. You cannot buy extra traffic because none is metered. | metered: no
- identity: email | detail: email
- interface: rest, webdav, rclone, webdav-proxy
- limits:
  - per-object-cap (binding): per file: 100 GB [1]
- limits note: Upload traffic is bounded by terms stating monthly upload limits up to three times disk capacity (9 TB per month upload limit on a 3 TB plan). Per-object upload cap is 100 GB on Profi tiers. Public shared-link downloads are unthrottled and served directly from Yandex edge infrastructure.
- interface detail: webdav + rest
- tooling: WebDAV endpoint live: `curl https://webdav.yandex.ru/` -> HTTP 302 to auth (expected; the mount is up). rclone `yandex` backend, rclone `webdav` with an app password, alist/OpenList `yandex` driver, official REST Disk API at cloud-api.yandex.net, plus the desktop client for Linux/Windows/macOS.
- composes with: Cannot be pooled: one Yandex ID = one Disk. But the Family plan gives 1 TB to each of up to 8 members on one subscription (250 ₽/mo annual ≈ $3.03/TB), which is the cheapest legitimate multiplication path of the storage providers compared. Profi and Family can be stacked. Yandex's own FAQ says the Disk volume sums across two plans on one account.
- reliability: Two real risks. (1) PRICE DISCRIMINATION IS DOCUMENTED AND MEASURABLE: the same page carries a «Оплата картой другой страны» (payment by a foreign card) block that routes to a separate tariff sheet, and the USD sheet at 360.yandex.com/premium-plans publishes $12.50/mo for 3 TB Pro versus 495 ₽ (~$5.99) on the RUB sheet. A 2.09× markup for a foreign card. Budget the USD number, not the rouble one. (2) Non-payment locks access progressively and then fully at 44 days (yandex.ru/support/disk/enlarge/disk-space.html). So this is not a set-and-forget archive unless the card keeps working.
- notes: the same as the free tier
- extras:
  - price_verbatim: RUB sheet (Russian card): $2.00/TB/mo at 3 TB ($5.99/mo); $3.83/TB/mo at 5 TB ($19.17/mo); $7.27/TB/mo at 10 TB ($72.67/mo). USD sheet (foreign card — the real price): $4.17/TB/mo at 3 TB ($12.50/mo); $4.25/TB/mo at 5 TB ($21.25/mo); $3.17/TB/mo at 1 TB. Family variant: $3.03/TB/mo per member. At 20 TB: not published on either sheet — the 20 TB and 30 TB options exist in the tier selector but render no price without a logged-in account, so no 20 TB figure is claimed.
- evidence:
  - [1] 2026-10-21: «Место на Диске 3 ТБ 990 ₽ 495 ₽/мес -50% … 5 ТБ 1 583 ₽/мес … Подключить за 11 880 ₽ 5 940 ₽/год первый год»; comparison table rows «Неограниченное скачивание по публичным ссылкам», «Месячный лимит загрузки на Диск до 3 объёмов Диска», «Загрузка больших файлов до 100 ГБ»
  - [2] 2026-10-21: same product, English/USD sheet: 1 TB $3.17, 2 TB $5.07, 3 TB Pro $12.50, 5 TB Pro $21.25 per month. This is the price a foreign card actually pays.
  - [1] 2026-10-21: «Оплата картой другой страны / Перейдите на страницу с доступными тарифами для вашей карты» block present in the page payload, confirming a separate non-RUB tariff path exists
  - [3] 2026-10-21: probe: curl -o /dev/null -w '%{http_code}' -> 302 (WebDAV mount live)
  - [4] 2026-10-21: «Для профи на 5 ТБ … 11 880 ₽» annual list
- sources:
  - [1] https://360.yandex.ru/premium-plans/
  - [2] https://360.yandex.com/premium-plans/
  - [3] https://webdav.yandex.ru/
  - [4] https://yandex.ru/support/yandex-360/customers/purchase/ru/pay

## Yandex Disk free tier (post-2026-06 change)

- `storage/yandex-disk-free-tier` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://disk.yandex.ru
- free tier: 5 GB by default for users without a plan: 'По умолчанию пользователям без тарифа доступно 5 ГБ места в хранилище'. Photo/video 'unlimited' auto-upload is a plan feature only. Without a Yandex 360 plan, mobile uploads count against the 5 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress fee, but the free tier just lost desktop sync entirely. | metered: no
- identity: email
- interface: rest, webdav, rclone
- limits note: 5 GB total shared with Mail. As of 2026-06-03, desktop sync for Windows/macOS requires a paid subscription. Free users keep only local files in the client.
- interface detail: rest
- tooling: WebDAV + REST API + rclone backend exist, which is why this matters despite the quota.
- composes with: Free tier provides 5 GB storage per registered account. Unlimited photo storage features require paid subscription plans.
- reliability: This is the round's clearest negative finding: Yandex removed free desktop synchronisation in June 2026 citing 'files of large volume' load, and the 'unlimited photo auto-upload' that used to be a free loophole now requires a Yandex 360 tariff. Kommersant frames it as the first radical free-tier cut of its kind in Russia.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB by default for users without a plan: 'По умолчанию пользователям без тарифа доступно 5 ГБ места в хранилище'. Photo/video 'unlimited' auto-upload is a plan feature only — without a Yandex 360 plan, mobile uploads count against the 5 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: (2026-05-20) — 'с начала июня отключает возможность бесплатно использовать десктопную версию «Яндекс Диска»'; 'С 3 июня ... отключает облачную синхронизацию файлов ... для десктоп-пользователей, использующих его бесплатно'
  - [1] 2026-10-21: 'По умолчанию пользователям без тарифа доступно 5 ГБ места в хранилище'
  - [3] 2026-10-21: 'Безлимитная автозагрузка — это одна из возможностей в тарифах Яндекс 360. Если у вас не подключен тариф ... фото и видео ... будут занимать место'
- sources:
  - [1] https://yandex.ru/support/yandex-360/customers/disk/web/ru/enlarge/disk-space
  - [2] https://www.kommersant.ru/doc/8673080
  - [3] https://yandex.ru/support/yandex-360/customers/disk/web/ru/media-upload.md
