# Yandex 360

> yandex.ru | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yandex-3/ | JSON https://fshy.ajam.dev/api/v1/entity/yandex-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yandex 360 "Для профи" (Profi) 3 TB

- `storage/yandex-360-3-tb-the-regional-price-floor-with-unlimited` | qualifies-with-caveat | evidence reported | binding per-object-cap | category consumer-cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:22.711Z (live) | stale on 2026-12-04
- url https://360.yandex.ru/premium-plans/
- price RUB sheet (Russian card): $2.00/TB/mo at 3 TB ($5.99/mo); $3.83/TB/mo at 5 TB ($19.17/mo); $7.27/TB/mo at 10 TB ($72.67/mo). USD sheet (foreign card — the real price): $4.17/TB/mo at 3 TB ($12.50/mo); $4.25/TB/mo at 5 TB ($21.25/mo); $3.17/TB/mo at 1 TB. Family variant: $3.03/TB/mo per… | parsed USD 2/TB-mo
- free tier: Profi 3 TB: 990 ₽/mo when paid annually as 11 880 ₽/year. Upload per file: 100 GB. Monthly upload ceiling: 3× Disk size. The wider tier ladder and the former discounted annual rate are no longer shown on the public plan table; the table's other published capacities are 200 GB, 1 TB and 2 TB. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
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
- notes: Read through a browser-rendering provider, the premium-plans page rendered a plan table that stops at 2 TB; the «Для профи» tier and its monthly prices are absent.
- extras:
  - price_verbatim: RUB sheet (Russian card): $2.00/TB/mo at 3 TB ($5.99/mo); $3.83/TB/mo at 5 TB ($19.17/mo); $7.27/TB/mo at 10 TB ($72.67/mo). USD sheet (foreign card — the real price): $4.17/TB/mo at 3 TB ($12.50/mo); $4.25/TB/mo at 5 TB ($21.25/mo); $3.17/TB/mo at 1 TB. Family variant: $3.03/TB/mo per member. At 20 TB: not published on either sheet — the 20 TB and 30 TB options exist in the tier selector but render no price without a logged-in account, so no 20 TB figure is claimed.
- evidence:
  - [1] 2026-10-21: «Место на Диске 3 ТБ 990 ₽ 495 ₽/мес -50% … 5 ТБ 1 583 ₽/мес … Подключить за 11 880 ₽ 5 940 ₽/год первый год»; comparison table rows «Неограниченное скачивание по публичным ссылкам», «Месячный лимит загрузки на Диск до 3 объёмов Диска», «Загрузка больших файлов до 100 ГБ»
  - [2] 2026-10-21: same product, English/USD sheet: 1 TB $3.17, 2 TB $5.07, 3 TB Pro $12.50, 5 TB Pro $21.25 per month. This is the price a foreign card actually pays.
  - [1] 2026-10-21: «Оплата картой другой страны / Перейдите на страницу с доступными тарифами для вашей карты» block present in the page payload, confirming a separate non-RUB tariff path exists
  - [3] 2026-10-21: probe: curl -o /dev/null -w '%{http_code}' -> 302 (WebDAV mount live)
  - [4] 2026-10-21: «Для профи на 5 ТБ … 11 880 ₽» annual list
  - [5] 2026-11-10: the rendered plan table stops at 2 TB and lists no «Для профи» tier | capture: sha256:93101d4e07e1e48fb8943b2cb28df5f4e2dfe40723b2a62007992246eb399942 | quote: до 2 ТБ
  - [5] 2026-11-10: the footnote states large-file uploads up to 100 GB are available only on the «Для профи» plan | capture: sha256:93101d4e07e1e48fb8943b2cb28df5f4e2dfe40723b2a62007992246eb399942 | quote: Возможности загрузки файлов большого размера до 100 ГБ и увеличенный месячный лимит загрузки файлов на Диск доступны только для пользователей, подключивших новый тариф "Для профи" после 13 ноября 2025 года
  - [1] 2026-11-19: Profi 3 TB is 990 ₽/mo paid as 11 880 ₽ per year | capture: sha256:ee8609c597199e4fbe82e1afbbe1dbb6fc99034ebd35fb2c542d44e4bf4c68a9 | quote: 990 ₽/мес При оплате 11 880 ₽ за год Дополнительное место 3 ТБ
  - [1] 2026-11-19: Profi 3 TB annual price is unchanged from the previous read at 990 ₽/mo / 11 880 ₽ per year, while the 495 ₽ figure is gone | capture: sha256:ee8609c597199e4fbe82e1afbbe1dbb6fc99034ebd35fb2c542d44e4bf4c68a9 | quote: 990 ₽/мес При оплате 11 880 ₽ за год Дополнительное место 3 ТБ
  - [1] 2026-11-19: Profi monthly upload ceiling is 3× Disk size | capture: sha256:ee8609c597199e4fbe82e1afbbe1dbb6fc99034ebd35fb2c542d44e4bf4c68a9 | quote: Загрузка до 3 объёмов Диска в месяц
  - [1] 2026-11-19: Profi plan carries a 3× Disk monthly upload allowance | capture: sha256:3d9379a4ede3f118f8bb13f5b84ad5cd50a78fb9a7d6ca4feaa25d804b229b8c | quote: В тарифе «Для профи» лимит увеличен и составляет три объёма от вашего размера диска.
- sources:
  - [1] https://360.yandex.ru/premium-plans/
  - [2] https://360.yandex.com/premium-plans/
  - [3] https://webdav.yandex.ru/
  - [4] https://yandex.ru/support/yandex-360/customers/purchase/ru/pay
  - [5] https://360.yandex.ru/premium-plans/?from=landing

## Yandex Disk free tier (post-2026-06 change)

- `storage/yandex-disk-free-tier` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:34.051Z (live) | stale on 2026-12-04
- url https://disk.yandex.ru
- free tier: 5 GB by default for users without a plan: 'По умолчанию пользователям без тарифа доступно 5 ГБ места в хранилище'. Photo/video 'unlimited' auto-upload is a plan feature only. Without a Yandex 360 plan, mobile uploads count against the 5 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Documented over-quota ladder: at 44 days the disk is blocked and access to files is lost; at 90 days the disk may be fully cleared and files are not recoverable. Trash items and deleted mail are removed automatically after 30 days. | source: [1] | note: not stated
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
  - [4] 2026-11-19: the free tier remains 5 GB for users without a plan, unchanged | capture: sha256:8e2fa7b6cf8659a42d5fef662c549b1d6ad4c869b83495196d99df5f18644eb9 | quote: By default, users without a plan get 5 GB of storage space. If you have an active Yandex 360 plan or Yandex Plus option, you receive additional storage.
  - [5] 2026-11-19: unlimited photo auto-upload is a paid-plan feature, not free | capture: sha256:6042d208954fe74240d2363f45a7b65309314d90d0ec7cbf6197a317cbdcf5a8 | quote: Unlimited photo and video auto-uploads are only available with a Yandex 360 plan
  - [1] 2026-11-19: at 90 days the disk may be fully cleared, completing the documented over-quota retention ladder | capture: sha256:795eaae828e780875b32d307a846b107283776096c26d65b29bff6dcf8af9927 | quote: C -->|"через<br/>90 дней"| D["<b>Блокировку не сняли:</b><br/><br/>— Диск может полностью очиститься"]
  - [4] 2026-11-19: the 30-day trash retention is documented on the first-party page | capture: sha256:8e2fa7b6cf8659a42d5fef662c549b1d6ad4c869b83495196d99df5f18644eb9 | quote: Files deleted from Yandex Disk end up in your trash and still take up space. They will be automatically deleted in 30 days.
- sources:
  - [1] https://yandex.ru/support/yandex-360/customers/disk/web/ru/enlarge/disk-space
  - [2] https://www.kommersant.ru/doc/8673080
  - [3] https://yandex.ru/support/yandex-360/customers/disk/web/ru/media-upload.md
  - [4] https://yandex.com/support/yandex-360/customers/disk/web/en/enlarge/disk-space
  - [5] https://www.yandex.com/support/yandex-360/customers/disk/web/en/media-upload
