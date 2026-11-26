# pastebin.com

> pastebin.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pastebin/ | JSON https://fshy.ajam.dev/api/v1/entity/pastebin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pastebin.com

- `storage/pastebin-com` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.424Z (live) | stale on 2026-12-04
- url https://pastebin.com/faq
- free tier: none reachable: 512 KB per paste (10 MB only on paid PRO), guests limited to 10 new pastes per 24h and cannot create private pastes, plus human-verification step-triggering spam filtering. Three hard caps at once. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: 512 KB per paste (10 MB only on paid PRO), guests limited to 10 new pastes per 24h and cannot create private pastes, plus human-verification step-triggering spam filtering. Three hard caps at once.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 512 KB per paste (10 MB only on paid PRO), guests limited to 10 new pastes per 24h and cannot create private pastes, plus human-verification step-triggering spam filtering. Three hard caps at once.
  - [1] 2026-11-19: guests are limited to 10 new pastes per 24 hours and free members to 20 | capture: sha256:b8f1a081adcd7b5d39155847d44dabf4631437104b948b850ce83cd8c5352747 | quote: Guests can create up to 10 new pastes per 24 hours. Free members can create up to 20 new pastes per 24 hours.
  - [1] 2026-11-19: free paste cap of 512 kilobytes, with 10 megabytes for paid PRO | capture: sha256:b8f1a081adcd7b5d39155847d44dabf4631437104b948b850ce83cd8c5352747 | quote: The maximum size a paste can be is 512 kilobytes (0.5 megabytes).
- sources:
  - [1] https://pastebin.com/faq
