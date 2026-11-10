# Mail.ru Cloud

> mail.ru | Netdisk and pan, Storage; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mail/ | JSON https://fshy.ajam.dev/api/v1/entity/mail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloud Mail.ru (cloud.mail.ru)

- `netdisk-pan/mail-ru-cloud` | paid-only | evidence documented | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T01:23:08.569Z (live) | stale on 2026-11-26
- url https://cloud.mail.ru/
- free tier: a promotional plan: 1 TB for the first year at RUB 1,560, then RUB 3,000 from the second year, with nine months added; no free terabyte tier is offered on the page read | unit: TB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 2 GB per file on a free account, unlimited on paid accounts, as documented by the rclone mailru backend; the vendor landing page states no per-file cap | source: [1]
- retention: not stated on the landing page | source: [1]
- egress: not stated on the landing page; recorded as metered:false because no per-GB price or cap was found, which is an absence of evidence and not evidence of absence | metered: no | source: [1]
- identity: any-phone | detail: a Mail.ru account
- interface: rest, webdav
- limits:
  - per-object-cap (binding): not stated on the landing page [1]
- binding note: The offer is a paid plan, so the verdict is about price before any cap; the cap is unrecorded because the landing page does not state it.
- tooling: a WebDAV endpoint (https://webdav.cloud.mail.ru) that the vendor documents, and an rclone mailru backend; both need a Mail.ru app password, and the account password does not work. No vendor REST API is documented on the pages read
- composes with: a RUB-priced 1 TB tier, which is a paid answer and not a free one
- reliability: The page read offers 1 TB as a paid annual plan with a promotional first year, not as a free tier.
- notes: The landing page read on 2026-10-22 offers 1 TB at RUB 1,560 for the first year and RUB 3,000 from the second, with nine months added, under a promotion running 2026-10-15 to 2026-11-19.
- extras:
  - access_mode: paid-pan
  - promo_window: 2026-10-15 to 2026-11-19
  - price_first_year: RUB 1,560
  - price_from_second_year: RUB 3,000
- evidence:
  - [1] 2026-10-22: the page offers '1 TB' with 'Цена за первый год — 1 560 ₽, со второго года — 3 000 ₽' and '9 месяцев в подарок' under a promotion dated 15.10.26 to 19.11.26; it states no free storage tier
  - [2] 2026-11-03: the rclone backend documentation states a 2 GB per-file limit for a free account | capture: sha256:3b8bfed70ee99f8bdc194e75e2e82ba928f02bcc592c3f6e2ff5cd647b91bd2c | quote: Maximum file size is limited to 2G for a free account, unlimited for paid accounts
  - [1] 2026-11-03: the landing page still offers a paid 1 TB plan at RUB 1,560 for the first year and RUB 3,000 from the second, with no free tier stated | capture: sha256:20fc04044690463e0d4cc943ef49d3d372bdc0f50f53a2ea97a360b91b930632 | quote: Цена за первый год — 1 560 ₽, со второго года — 3 000 ₽
  - [3] 2026-11-04: the vendor documents a WebDAV endpoint that takes an app password and not the account password | capture: sha256:2acc2e508f12c9af8d02464e168ddcdc931a26bb70b990194065b5e5a6c94465 | quote: С 1 января 2022 для подключения по WebDAV нужно использовать пароль для внешнего приложения.
  - [2] 2026-11-04: the rclone mailru backend also needs an app password | capture: sha256:3b8bfed70ee99f8bdc194e75e2e82ba928f02bcc592c3f6e2ff5cd647b91bd2c | quote: Rclone will not work with your normal username and password
- sources:
  - [1] https://cloud.mail.ru/
  - [2] https://rclone.org/mailru/
  - [3] https://help.mail.ru/cloud/desktop/webdav/

## Mail.ru Cloud

- `storage/mail-ru-cloud` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloud.mail.ru
- disagrees on identity_kind: `storage/mail-ru-cloud` says any-phone, `storage/mail-ru-cloud-mail-1-tb-with-free-public-link-download` says card
- disagrees on identity_kind: `storage/mail-ru-cloud` says any-phone, `storage/mail-ru-cloud-mail-space` says email
- free tier: 8 GB free, now a single pool shared between Почта and Облако | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No per-GB fee on the free tier; paid tier lifts quota | metered: no
- identity: any-phone
- interface: rest, rclone
- limits note: 8 GB shared across mail and cloud; phone-first registration
- interface detail: rest
- tooling: Unofficial web API + rclone backend 'mailru'
- composes with: 8 GB x N phone-verified accounts; not worth the identity cost
- reliability: 8 GB and a shared mail/cloud counter; free tier has been shrinking for years
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 8 GB free, now a single pool shared between Почта and Облако
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: read -> 504, raw HTML 226 KB containing recaptcha; crawl rendered 0 pages (signup is a client-rendered VK-style app)
  - withheld 2026-10-21: 
- sources:
  - [1] https://cloud.mail.ru/
  - [2] https://account.mail.ru/signup

## Mail.ru Cloud (Облако Mail) + Mail Space

- `storage/mail-ru-cloud-mail-space` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloud.mail.ru
- disagrees on identity_kind: `storage/mail-ru-cloud` says any-phone, `storage/mail-ru-cloud-mail-space` says email
- disagrees on identity_kind: `storage/mail-ru-cloud-mail-1-tb-with-free-public-link-download` says card, `storage/mail-ru-cloud-mail-space` says email
- free tier: 8 GB free per account; 1 TB only as a paid Mail Space plan (1 560 RUB first year, 3 000 RUB/yr after) | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Direct/share links unmetered, no egress pricing published. | metered: no
- identity: email
- interface: s3, rest, rclone
- limits note: free 8 GB shared with Mail attachments; 'without-limit' phone auto-upload requires a paid Mail Space tariff of 256 GB+; heavy-file send up to 100 GB only on paid plans
- interface detail: rest
- tooling: rclone backend 'mailru' (rclone/rclone backend/mailru, in core); web/desktop clients; S3 backend exists only on the enterprise VK Cloud product
- composes with: 8 GB x unlimited free accounts = 125 accounts per TB. Worst yield in the niche; the historical 1 TB gift was cut ~12.5x in 2024.
- reliability: Quota was cut from 1 TB to 8 GB for grandfathered accounts (Oct 2024); unlimited auto-upload stops being unlimited the moment the paid tariff lapses and already-uploaded files start consuming quota.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 8 GB free per account; 1 TB only as a paid Mail Space plan (1 560 RUB first year, 3 000 RUB/yr after)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '8 ГБ доступны бесплатно', 'Безлимитная автозагрузка фото и видео с телефона' listed as a subscription feature
  - [2] 2026-10-21: 'Безлимитная автозагрузка доступна по подписке Mail Space с тарифом от 256 ГБ' (updated 9 Oct 2026)
  - [3] 2026-10-21: '9 месяцев в подарок ... Цена за первый год — 1 560 ₽, со второго года — 3 000 ₽' (1 TB is the paid tier)
- sources:
  - [1] https://help.mail.ru/cloud/size/storage/
  - [2] https://help.mail.ru/cloud/files/unlimited/
  - [3] https://cloud.mail.ru/

## Mail.ru Cloud / Облако Mail (VK) — 1 TB with free public-link download

- `storage/mail-ru-cloud-mail-1-tb-with-free-public-link-download` | fails-quota | evidence documented | binding none | category consumer-cloud-drive
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T15:03:47.540Z (live) | stale on 2026-12-04
- url https://cloud.mail.ru/
- price 224 RUB per month for the +2 TB tier (2.01 TB total with the free space) bought for a year = 112 RUB per TB-month; the +1 TB tier is 133 RUB per month bought for a year = 133 RUB per TB-month. The largest tier listed totals 2.01 TB, so 10 TiB is not reachable on one account. No USD figure was computed. | parsed USD 1.64/TB-mo
- disagrees on identity_kind: `storage/mail-ru-cloud` says any-phone, `storage/mail-ru-cloud-mail-1-tb-with-free-public-link-download` says card
- disagrees on identity_kind: `storage/mail-ru-cloud-mail-1-tb-with-free-public-link-download` says card, `storage/mail-ru-cloud-mail-space` says email
- free tier: Free tier 8 GB with uploads up to 1 GB per file; a Mail Space subscription raises the per-file limit to 100 GB. Purchase page tiers: +256 GB, +512 GB, +1 TB and +2 TB (2.01 TB total). | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unverified: no download-volume or egress term appears on the purchase page or the help pages read. | metered: no
- identity: card | detail: A bank card is bound in the tariff payment window to buy a subscription (promotion terms); the sign-up form was not readable (shell page): unverified.
- interface: rest, webdav, rclone, webdav-proxy
- limits note: The unlimited feature on the purchase page is unlimited auto-upload of phone photos and videos, which do not count against the space; it is not unlimited storage. The largest purchasable tier listed totals 2.01 TB. Free tier is 8 GB with a 1 GB per-file ceiling.
- interface detail: webdav + rest
- tooling: WebDAV endpoint live (`https://webdav.cloud.mail.ru/` -> 302 to auth). rclone `mailru` backend, alist/OpenList `mailru` driver, desktop sync client, official REST API. Upload up to 100 GB/file on paid tiers.
- composes with: One account = one Cloud; the largest tier listed totals 2.01 TB, so the stored need takes several accounts; no documented route for that.
- reliability: VK-owned, so politically exposed for a foreign user but technically stable for a decade. The ₽1,560 first-year price IS a trial price. Steady state from year two is ₽3,000, a 92 % increase, and must be budgeted at ₽3,000. Plan maximum 4 TB means it cannot host 20 TiB at any price.
- notes: 1 TB plan. Landing promo (2026-10-15 to 2026-11-19): first year ₽1,560, from the second year ₽3,000 («Цена за первый год. 1 560 ₽, со второго года. 3 000 ₽»). Free tier 8 GB, 2 GB max file. Paid 1-4 TB.
- evidence note: documented: the 8 GB free tier, the 1 GB per-file limit and the 100 GB limit with a subscription are quoted from https://help.mail.ru/cloud/files/upload/; the 2.01 TB largest tier total and the 224 rubles per month price from https://cloud.mail.ru/promo/quota/; the bank card requirement of the promotion from https://blog.mail.ru/terms_cloud_autumn_26/ (vendor pages read 2026-11-03); egress and the sign-up form were not read
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB plan. Landing promo (2026-10-15 to 2026-11-19): first year ₽1,560, from the second year ₽3,000 («Цена за первый год — 1 560 ₽, со второго года — 3 000 ₽»). Free tier 8 GB, 2 GB max file. Paid 1-4 TB.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $3.03/TB/mo at 1 TB steady state (₽3,000/yr = $36.33/yr). Trial year: $1.58/TB/mo (₽1,560 = $18.89). At 5 TB and 20 TB: NOT AVAILABLE — the product ceiling is 4 TB, so no 5 TB or 20 TB price exists. Egress free.
- evidence:
  - [1] 2026-10-21: «Акция: 15.10.26 — 19.11.26 … Цена за первый год — 1 560 ₽, со второго года — 3 000 ₽»; «1 терабайт пригодится для других файлов»; «С безлимитной автозагрузкой все файлы загрузятся, а в Облаке у вас по-прежнему будет 217 ГБ для любых других файлов»
  - [2] 2026-10-21: «Бесплатный объём — 8 ГБ. Максимальный размер одного файла в бесплатной версии — 2 ГБ. Платные тарифы: от 1 до 4 ТБ»
  - [3] 2026-10-21: probe: curl -o /dev/null -w '%{http_code}' -> 302
  - [4] 2026-10-21: «Купить 1 ТБ … Загрузка файлов до 100 Г»
  - [4] 2026-11-03: the +2 TB tier is 224 rubles per month when bought for a year | capture: sha256:584e9e8284815838d7ea3e049c90698b0f28c8b6d6c15c374da9cd075ccc5e39 | quote: 224 ₽ в месяц при покупке на год
  - [5] 2026-11-03: the free tier is 8 GB with 1 GB per file; a Mail Space subscription raises the file limit to 100 GB | capture: sha256:b59d3c78cd97171aec47aa7fd510cfb13726ca25c953d8daf360fe2e87b4a7cc | quote: В Облаке Mail вам бесплатно доступно 8 ГБ и вы можете загружать файлы объёмом до 1 ГБ. Увеличить место и загружать файлы объёмом до 100 ГБ можно с подпиской Mail Space.
  - [4] 2026-11-03: the largest tier on the purchase page totals 2.01 TB, below the 10 TiB stored need | capture: sha256:584e9e8284815838d7ea3e049c90698b0f28c8b6d6c15c374da9cd075ccc5e39 | quote: Общий объём составит 2.01 ТБ
  - [6] 2026-11-03: the promotion terms require a bank card bound in the tariff payment window | capture: sha256:550b76f45aa983a6accbf3d15c74196b06460c822dcefd01ae0facdb8f589a00 | quote: Участнику необходимо привязать данные своей банковской карты в окне оплаты тарифов в Сервисе
  - [4] 2026-11-03: the vendor page was read and quoted on 2026-11-03: the +2 TB tier is 224 rubles per month when bought for a year | capture: sha256:584e9e8284815838d7ea3e049c90698b0f28c8b6d6c15c374da9cd075ccc5e39 | quote: 224 ₽ в месяц при покупке на год
- sources:
  - [1] https://cloud.mail.ru/
  - [2] https://hl.ru/shops/cloud-mail
  - [3] https://webdav.cloud.mail.ru/
  - [4] https://cloud.mail.ru/promo/quota/
  - [5] https://help.mail.ru/cloud/files/upload/
  - [6] https://blog.mail.ru/terms_cloud_autumn_26/

## Облако Mail.ru (VK)

- `storage/mail-ru` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloud.mail.ru
- free tier: 8 GB free: 'Сколько в Облаке бесплатного места — 8 ГБ'. The historic 100 GB-for-beta-testers grant was cancelled in Nov 2024; accounts drop to 8 GB after 6 months of inactivity. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: The historic 100 GB-for-beta-testers grant was cancelled in Nov 2024; accounts drop to 8 GB after 6 months of inactivity | days: 180 | source: [1] | note: not stated
- egress: No egress fee; sync across devices remains free (unlike Yandex). | metered: no
- identity: email
- interface: rest, webdav, rclone
- limits note: 8 GB free. Auto-freeze and shrink-to-8GB after 6 months without login.
- interface detail: rest
- tooling: WebDAV historically; Disk-O is the desktop aggregator client. No rclone backend.
- composes with: 8 GB x N accounts is irrelevant at this scale. 1 TB 'Safe' vault exists but is capped at 3 months and does not count as storage.
- reliability: Mail.ru also revoked the free permanent 100 GB it gave its 2013 beta cohort, with file deletion after a 3-month grace period. A direct precedent for 'free tier that was real and then was taken away'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 8 GB free: 'Сколько в Облаке бесплатного места — 8 ГБ'. The historic 100 GB-for-beta-testers grant was cancelled in Nov 2024; accounts drop to 8 GB after 6 months of inactivity.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Сколько в Облаке бесплатного места — 8 ГБ'; 'Если не заходить в облако больше 6 месяцев, оно автоматически заморозится, и уменьшится до 8 ГБ'
  - [2] 2026-10-21: 'Mail.ru отменила бесплатные вечные 100 ГБ для первых пользователей «Облако Mail.ru»', effective 2024-11-11, deletion after 2025-02-11
- sources:
  - [1] https://help.mail.ru/cloud/faq/space/size/
  - [2] https://habr.com/ru/news/854870/

## mail.ru '1 tb free' offer (historical)

- `storage/mail-ru-1-tb-free-offer` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.mail.ru/cloud/size/storage/
- free tier: none reachable: The 1 TB giveaway is gone: current free volume is 8 GB and the 1 TB is an annual paid plan (1 560 RUB year one). Any 2013-2019 blog claiming 1 TB free is stale. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The 1 TB giveaway is gone: current free volume is 8 GB and the 1 TB is an annual paid plan (1 560 RUB year one). Any 2013-2019 blog claiming 1 TB free is stale.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 1 TB giveaway is gone: current free volume is 8 GB and the 1 TB is an annual paid plan (1 560 RUB year one). Any 2013-2019 blog claiming 1 TB free is stale.
  - [2] 2026-10-21: cited as the basis of the rejection: The 1 TB giveaway is gone: current free volume is 8 GB and the 1 TB is an annual paid plan (1 560 RUB year one). Any 2013-2019 blog claiming 1 TB free is stale.
- sources:
  - [1] https://help.mail.ru/cloud/size/storage/
  - [2] https://cloud.mail.ru/
