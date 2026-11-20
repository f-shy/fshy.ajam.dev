# mts web services

> mts.ru | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mts/ | JSON https://fshy.ajam.dev/api/v1/entity/mts.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mts web services (mws cloud) object storage

- `storage/mts-web-services-object-storage` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:01.974Z (live) | stale on 2026-12-04
- url https://docs.cloud.mts.ru/docum/promo-cdn-s3.html
- free tier: none reachable: No free tier found; S3 is a paid enterprise product sold with a CDN bundle discount. Nothing to multiply. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: No free tier found; S3 is a paid enterprise product sold with a CDN bundle discount. Nothing to multiply.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free tier found; S3 is a paid enterprise product sold with a CDN bundle discount. Nothing to multiply.
  - [1] 2026-11-19: object storage is sold as a paid CDN bundle with a 30% discount for months 1-6, not a free tier | capture: sha256:da6dff112398170bf227e988433748841c28e275082bea496683974204e3fbba | quote: Размер Скидки: 30% от стоимости Услуг ежемесячно с 1 по 6 календарный месяц оказания Услуг
- sources:
  - [1] https://docs.cloud.mts.ru/docum/promo-cdn-s3.html
