# ganso

> stackrater.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stackrater/ | JSON https://fshy.ajam.dev/api/v1/entity/stackrater.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## thunderdrive

- `storage/thunderdrive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.436Z (live) | stale on 2026-12-04
- url https://stackrater.io/cloud/lifetime-cloud-storage-scams/
- free tier: none reachable: a paid-only lifetime/annual cloud storage service; Pro 2 TB at $1200/life or $10/month, Personal 500 GB at $600/life or $5/month, with 30-day trash recovery. No free tier is offered. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The thunderdrive.io host still answers and presents a live sales page offering Pro 2 TB at $1200/life and Personal 500 GB at $600/life, paid annually at $10/month and $5/month, with 30-day trash recovery. A third-party article reports ThunderDrive collapsed and was rebranded to PrismDrive with lost data and no support; that report is not confirmed by the first-party site.
- notes: Collapsed, and its customer base was reportedly migrated/rebranded into Prism Drive. Documented as a pattern of deceptive offers, with lost data and no support.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Collapsed, and its customer base was reportedly migrated/rebranded into Prism Drive. Documented as a pattern of deceptive offers, with lost data and no support.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Collapsed, and its customer base was reportedly migrated/rebranded into Prism Drive. Documented as a pattern of deceptive offers, with lost data and no support.
  - [2] 2026-11-19: the thunderdrive.io host answers with a live page still selling lifetime storage plans | capture: sha256:d0ee0bf4e59035205e9e1ce23c039a1306022eefa4bb7e295c3734d86275c7f6 | quote: Personal Lifetime $600 /life Best for individuals and personal projects - 500GB of Space
  - [2] 2026-11-19: the first-party page offers only paid 2 TB and 500 GB plans, with no free tier | capture: sha256:d0ee0bf4e59035205e9e1ce23c039a1306022eefa4bb7e295c3734d86275c7f6 | quote: Pro Lifetime $1200 /life Best for storing and sharing very large files regularly. - 2 TB of Space
  - [2] 2026-11-19: the host answers and the paid-only offer is unchanged on a fresh read | capture: sha256:d0ee0bf4e59035205e9e1ce23c039a1306022eefa4bb7e295c3734d86275c7f6 | quote: Personal Lifetime $600 /life Best for individuals and personal projects - 500GB of Space
- sources:
  - [1] https://stackrater.io/cloud/lifetime-cloud-storage-scams/
  - [2] https://thunderdrive.io/

## ganso

- `storage/ganso` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:44.552Z (live) | stale on 2026-12-04
- url https://stackrater.io/cloud/lifetime-cloud-storage-scams/
- free tier: None reachable: Shut down entirely. Cited alongside ThunderDrive as a completed instance of the 'cheap lifetime terabytes then vanish' script. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Shut down entirely — cited alongside ThunderDrive as a completed instance of the 'cheap lifetime terabytes then vanish' script.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Shut down entirely — cited alongside ThunderDrive as a completed instance of the 'cheap lifetime terabytes then vanish' script.
  - [2] 2026-10-21: cited as the basis of the rejection: Shut down entirely — cited alongside ThunderDrive as a completed instance of the 'cheap lifetime terabytes then vanish' script.
  - [1] 2026-11-19: the Ganso lifetime-storage service has shut down | capture: sha256:947dde57f3278181a4c428d5dfc7508a990346f07649c85e86b48af5d6c054a4 | quote: already shut down
- sources:
  - [1] https://stackrater.io/cloud/lifetime-cloud-storage-scams/
  - [2] https://www.techradar.com/pro/grab-1-54tb-free-
