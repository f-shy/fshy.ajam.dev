# Seedbox.org.ua

> seedbox.org.ua | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedbox-4/ | JSON https://fshy.ajam.dev/api/v1/entity/seedbox-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedbox.org.ua

- `debrid/seedbox-org-ua` | qualifies-with-caveat | evidence documented | binding none | category Ukrainian seedbox (uTorrent on SSD/HDD, unlimited traffic) | tier ssd17 / DSK14 lines
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:14:50.663Z (live) | stale on 2026-11-23
- url http://seedbox.org.ua/
- free tier: None published. The page sells SSD and HDD plans only; no trial or free box is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The vendor counts 458 boxes running and 4,257 clients over 9 years.
- per-object cap: not applicable: disk plan sizes are 90/180/360 GB (SSD) and 300-2700 GB (HDD); no single-file cap published | source: [1] | note: unstated
- retention: 'сидбокс вместе с файлами будет удален по истечении срока действия' when renewal does not arrive 5 days before expiry - files are deleted with the box. | source: [1] | note: Deletion on expiry, exact grace period not stated
- egress: 'неограниченный трафик' on the SSD plan; the uplink is described as 8x10 Gbit/s in total, not per client. | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: Cabinet registration plus a payment; support is by Skype, ICQ and Gmail. No phone or document was asked for on the page read.
- interface: ftp, unknown
- limits:
  - per-object-cap: disk plan 90/180/360 GB SSD or 300-2700 GB HDD [1]
  - request-rate: manual activation within 24 hours of confirmed payment [1]
- limits note: 'неограниченное количество активных торрентов' on the SSD plan; 99.4% average uptime claimed over 9 years, vendor-reported.
- binding note: Traffic is unlimited and no byte quota is published, so at 1 TiB/month the only constraints are the disk size bought and the 24-hour manual activation. Neither is a rate limit in the vocabulary.
- interface detail: uTorrent 2.0.4 WebUI on the box, dedicated IPv4, automatic start; delivery for a user is by FTP/HTTP from the seedbox. No API is documented.
- tooling: uTorrent WebUI and a client cabinet. Activation is manual: 'в течении 24 часов с момента подтверждения получения платежа'.
- composes with: A Ukrainian-billable seedbox for the swarm side; it has no file-host downloading, so it pairs with a per-GB generator and does not replace one.
- reliability: Files are deleted with the box if renewal is late by more than five days; the site's figures (458 boxes, 99.4% uptime, 4,257 clients) are self-reported and were not measured.
- notes: The Ukrainian equivalent the sector asked for, and the only.ua retrieval service found that still sells capacity. Payment is PayPal, WebMoney, bank transfer or card transfer - all reachable from outside Ukraine, which is the opposite of the Russian pattern. No price could be read; the vendor quotes per box in the cabinet. A direct fetch of the site returned HTTP 522 twice (server-side); the page content quoted here came from a reader that did render it.
- evidence note: Plan shapes, the payment list, the deletion rule and the activation delay are quoted from the live page. The prices are not rendered on the public page and the tariff page answered 522 to a direct fetch, so no price is recorded. Reading the cabinet tariff would raise it.
- evidence:
  - [1] 2026-10-23: 'Мы принимаем Paypal и Webmoney. Также мы готовы принять банковский перевод, перевод на карту', the SSD/HDD plan sizes, 'неограниченный трафик', the 24-hour activation and the deletion-on-expiry rule
  - [1] 2026-10-23: self-reported operating figures: 458 boxes running, 4,257 clients, 9 years, 99.4% average uptime
- sources:
  - [1] http://seedbox.org.ua/
