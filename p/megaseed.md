# Megaseed.kz

> megaseed.kz | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/megaseed/ | JSON https://fshy.ajam.dev/api/v1/entity/megaseed.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Megaseed.kz (Megaseed LLP)

- `debrid/megaseed-kz` | qualifies-with-caveat | evidence documented | binding none | category Kazakh seedbox (BitTorrent host with ruTorrent and FTP) | tier weekly / half-month / monthly / quarterly disk plans
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:38.371Z (live) | stale on 2026-11-23
- url https://megaseed.kz/
- free tier: Withdrawn. The free-seedbox page still describes it (20 GB HDD, 3 active torrents, limited speed, no FTP) but opens with 'Выдача бесплатных сидбоксов остановлена!' (issuance of free seedboxes has stopped). | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The free tier was also restricted to members of the vendor's VK group.
- per-object cap: not applicable: the disk plan is the ceiling; no single-file cap is published | source: [2] | note: unstated
- retention: For the paid period. The order page says access credentials are sent after payment and the plan is billed by week, half-month, month or quarter; no post-expiry retention promise was read. | source: [3] | note: unstated
- egress: 'Трафик не лимитирован' in the tariff comparison table. For subscribers of Kazakhtelecom and its partners (megal ine, idnet) traffic from the seedbox is counted as internal: 'трафик для абонентов АО «Казахтелеком» и его партнеров является «внутренним» и не учитывается.' | metered: no | free allowance: unlimited | source: [2]
- identity: email | detail: Order form plus an emailed invoice; the vendor states it keeps only payment records by login ('ваши личные данные не хранятся в базах, ведется ТОЛЬКО учет платежей по логинам'). No phone or national ID is asked for on the pages read.
- interface: sftp, ftp, cli
- limits:
  - per-object-cap: disk plan size only (SSD and HDD lines); no per-file cap published [2]
  - write-gated: account is created manually: 'В срок не более суток (при наличии технической возможности ...); как правило - в течение часа' [4]
- limits note: Web UI and speed are shared: 'n × 10 Гбит/с' is the uplink, not a per-client guarantee. A dedicated IP is offered per plan.
- binding note: Traffic is unlimited and there is no published byte counter, so a monthly transfer of 1 TiB meets disk size and the manual provisioning delay, neither of which is a rate limit in the vocabulary. The disk plan is the only ceiling and it is bought, not enforced.
- interface detail: ruTorrent v3.10 on rtorrent 0.9.8 in the browser; 'Мы предоставляем полный доступ к файлам сидбокса через FTP/FTPS'. Torrent creation, MediaInfo and screenshots are built in; uploading to file hosts is explicitly not supported yet.
- tooling: ruTorrent web UI, FTP/FTPS, torrent-file creation on the box. The vendor states 'Могу ли я заливать файлы на файлообменники через сидбокс? В данный момент эта функция пока не поддерживается.'
- composes with: A KZT-billable seedbox with unlimited traffic; it supplies the always-on swarm side and FTP delivery, and pairs with Storage Portal for the file-host half that it refuses to do.
- reliability: Provisioning is manual and can take up to a day; the free tier that once made it testable is switched off, so a buyer pays before seeing the UI.
- notes: The Kazakh answer to the sector question: a foreigner can pay by PayPal (USD) or USDT TRC20, a Kazakh by Kaspi/Halyk in KZT, a Russian by Sberbank or YooMoney in RUB. That multi-rail design is unusual and is the reason the record exists. No price is included because none is public; the site sells by invoice. The Kazakhtelecom peering claim is the vendor's own and is not independently verified.
- evidence note: The payment list, the unlimited-traffic statement, the ruTorrent version, the FTP access and the withdrawn free tier are quoted from live pages read. The prices are not on any public page - the order form issues an invoice - so no price is recorded. Reading one invoice would raise the price to documented.
- evidence:
  - [5] 2026-10-23: the seedbox description, ruTorrent, the n×10 Gbit/s uplink, anonymity and dedicated-IP claims, and the payment anchors exposed by the page (advcash-usd, halyk-kzt, kaspi-kzt, pp-usd, qiwi-kzt, qiwi-rub, sber-rub, trc20-usd, ym-rub)
  - [2] 2026-10-23: 'Трафик | не лимитирован', 'ruTorrent v3.10 @ rtorrent 0.9.8', and that the price row is rendered only with the plan table
  - [6] 2026-10-23: the payment page title lists Visa/Mastercard, Tether, Volet, Sber, PayPal, YooMoney, Kaspi, Halyk; PayPal is described as accepting 'Рубли, Доллары США и Евро'; YooMoney only rubles
  - [1] 2026-10-23: 'Выдача бесплатных сидбоксов остановлена!' and the limits of the withdrawn tier (20 GB, 3 torrents, limited speed, no FTP)
  - [4] 2026-10-23: Kazakhtelecom internal-traffic rule and the up-to-24-hour manual account creation
- sources:
  - [1] https://megaseed.kz/seedbox-free/
  - [2] https://megaseed.kz/compare/
  - [3] https://megaseed.kz/order/
  - [4] https://megaseed.kz/faq/
  - [5] https://megaseed.kz/
  - [6] https://megaseed.kz/how-to-pay/
