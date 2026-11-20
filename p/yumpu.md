# yumpu

> yumpu.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/yumpu/ | JSON https://fshy.ajam.dev/api/v1/entity/yumpu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## yumpu

- `storage/yumpu` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:35.531Z (live) | stale on 2026-12-04
- url https://www.yumpu.com/de
- free tier: none reachable: Free plan allows 3 total document uploads with a 600 MB maximum size per PDF. Plan detail and documentation pages returned HTTP 404 or 422 on 2026-10-21. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free plan is 3 uploads total (not per day) with 600 MB per PDF; the free tier is a demo of a paid publishing product, and every plan/FAQ page returned 404/422.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is 3 uploads total (not per day) with 600 MB per PDF; the free tier is a demo of a paid publishing product, and every plan/FAQ page returned 404/422.
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan is 3 uploads total (not per day) with 600 MB per PDF; the free tier is a demo of a paid publishing product, and every plan/FAQ page returned 404/422.
  - [3] 2026-10-21: cited as the basis of the rejection: Free plan is 3 uploads total (not per day) with 600 MB per PDF; the free tier is a demo of a paid publishing product, and every plan/FAQ page returned 404/422.
  - [1] 2026-11-19: the first-party Yumpu homepage lists the FREE plan as 3 uploads | capture: sha256:c17742b55a026267de25f1f0dea5a9c54cc18de836a3c99564e22f2fadb72d92 | quote: - 3 Uploads
  - [2] 2026-11-19: the first-party Yumpu help center states a 600 MB per-PDF cap and 3 PDFs total for FREE users | capture: sha256:8feb633d0b1a712f9340e63210b40d4456dedee09e0a42a036e1c8dbd5752d2e | quote: Each uploaded PDF must not exceed 600 MB.
- sources:
  - [1] https://www.yumpu.com/de
  - [2] http://helpcenter.yumpu.com/en/articles/1101958-pdf-upload-limits
  - [3] https://www.yumpu.com/en/info/subscription_plans
