# KUB.ua File Cloud

> kub.ua | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kub/ | JSON https://fshy.ajam.dev/api/v1/entity/kub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KUB.ua File Cloud (Ukraine) — Nextcloud-backed flat per-TB with unlimited traffic

- `storage/kub-ua-file-cloud-nextcloud-backed-flat-per-tb-with-unli` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category storage-vps-managed-nas
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://kub.ua/file-cloud/
- price $8.16/TB/mo at 5 TB ($40.81/mo), $19.28/TB/mo at 1 TB ($19.28/mo). At 20 TB: $8.16/TB/mo if 4× the 5 TB plan is allowed, derived. UAH at 0.022177 USD/UAH. Egress $0. | parsed USD 8.16/TB-mo
- free tier: FILE CLOUD 1: 869.57 ₴/mo for 1 TB; FILE CLOUD 5: 1,840.36 ₴/mo for 5 TB. Unlimited users, unlimited traffic, 50 concurrent connections, 7-day trial, Nextcloud platform. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: «Трафік не обмежений» (traffic unlimited), stated in the plan table. No meter or overage rate on the page. | metered: yes
- identity: card | detail: card
- interface: s3, webdav, sftp, rclone
- limits:
  - per-ip-shaping (binding): 50 concurrent connections [1]
- limits note: 50 concurrent connections at 1 TB. The 1 TB tier is poor value ($19.28/TB); the product only becomes interesting at 5 TB ($8.16/TB).
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: webdav + sftp
- tooling: Nextcloud. So WebDAV, and with the Nextcloud desktop client or rclone `webdav`. Nextcloud's own S3-primary-object-store is configurable only server-side, so from the client's side this is WebDAV.
- composes with: Two sizes on the public page (1 TB, 5 TB); 20 TB needs a sales conversation. 5 TB is the only competitive point.
- reliability: Nextcloud-on-managed-infrastructure; the vendor's own platform claim, no independent benchmark. Business-oriented (rights management, backup) rather than storage-farm. The per-TB discount from 1 TB to 5 TB is 2.36×, which is unusually steep and suggests the 1 TB price is a headline rather than a rate.
- notes: the same as the free tier
- extras:
  - price_verbatim: $8.16/TB/mo at 5 TB ($40.81/mo), $19.28/TB/mo at 1 TB ($19.28/mo). At 20 TB: $8.16/TB/mo if 4× the 5 TB plan is allowed, derived. UAH at 0.022177 USD/UAH. Egress $0.
- evidence:
  - [1] 2026-10-21: «FILE CLOUD 1 869.57₴/міс — Дисковий простір 1 Tb — Користувачів необмежено — Трафік не обмежений — Одночасні підключення: 50 — Платформа Nextcloud»; «FILE CLOUD 5 1840.36₴/міс — Дисковий простір 5 Tb»; «Тестовий період 7 днів»
  - withheld 2026-10-21: snippet surfaced «kub.ua/file-cloud — FILE CLOUD 1 869.57₴/міс … Трафік не обмежений», which is what prompted opening the page
- sources:
  - [1] https://kub.ua/file-cloud/
