# quora

> quora.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quora/ | JSON https://fshy.ajam.dev/api/v1/entity/quora.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## quora

- `storage/quora` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:49.684Z (inherited) | stale on 2026-11-14
- url https://www.quora.com/about/tos
- free tier: not stated: https://www.quora.com/about/tos prints no storage amount, per-file cap or period; users can add posts, text, photos, videos, links and other files to share with other users | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: no quota, per-file cap or retention period for user content is printed on the cited page
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: No attachment/file hosting at all.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: the terms describe user content including photos, videos and other files, and print no storage amount | capture: sha256:40427a553233ba0c02d2da7817bca29381b4359ba2c16784a61022844ffaba2e | quote: Quora enables you to add posts, text, photos, videos, links, and other files and information to share with other users of Quora.
- sources:
  - [1] https://www.quora.com/about/tos
