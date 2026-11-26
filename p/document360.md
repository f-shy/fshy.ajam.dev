# document360

> document360.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/document360/ | JSON https://fshy.ajam.dev/api/v1/entity/document360.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## document360

- `storage/document360` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.671Z (live) | stale on 2026-12-04
- url https://docs.document360.com/docs/adding-folders-and-files
- free tier: none reachable: Drive limits uploads to 150 MB per single file and 5,000 files per folder; pricing is quote-only and no free plan is published. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free plan provides 1 GB media storage, 150 MB per upload, and 5,000 files per folder. Higher tiers require custom sales quotes.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan is 1 GB media storage (Startup 50 GB, Business 'Unlimited'), 150 MB per upload, 5,000 files per folder.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan is 1 GB media storage (Startup 50 GB, Business 'Unlimited'), 150 MB per upload, 5,000 files per folder.
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan is 1 GB media storage (Startup 50 GB, Business 'Unlimited'), 150 MB per upload, 5,000 files per folder.
  - [1] 2026-11-19: a Drive upload is capped at 150 MB by default and folders hold up to 5,000 files | capture: sha256:22f29cc6ed3b560e8750e7296ad4da35517c24f3a173ee122592129d2fd820ee | quote: - Maximum file size for a single upload: 150 MB by default. This limit can be customized for your project.
  - [3] 2026-11-19: pricing is given per configuration rather than as published tiers | capture: sha256:adaadc073dc3298d97d1b60559a737ea8a7135a2e1831122f9c0cfdf54c30560 | quote: Why don't you show flat pricing?
- sources:
  - [1] https://docs.document360.com/docs/adding-folders-and-files
  - [2] https://saufter.io/document360-pricing/
  - [3] https://www.document360.com/pricing
