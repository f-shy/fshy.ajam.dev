# transloadit

> transloadit.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transloadit/ | JSON https://fshy.ajam.dev/api/v1/entity/transloadit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## transloadit

- `storage/transloadit` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:29.929Z (live) | stale on 2026-12-04
- url https://www.transloadit.com/pricing/
- free tier: None reachable: Free 'Community' is 5 GB of processing per month, 0.5 GB per file, watermarked output images and trimmed A/V. It is a transcoding pipeline with a hard stop at 5 GB, not a store. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free 'Community' is 5 GB of processing per month, 0.5 GB per file, watermarked output images and trimmed A/V — it is a transcoding pipeline with a hard stop at 5 GB, not a store
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free 'Community' is 5 GB of processing per month, 0.5 GB per file, watermarked output images and trimmed A/V — it is a transcoding pipeline with a hard stop at 5 GB, not a store
  - [1] 2026-11-19: Transloadit's first-party pricing page confirms GB is processing allowance, not storage | capture: sha256:8fbc716d636dc12610400e0bc2952c9bacaa5ab795da24aed6cd13fe66636ec4 | quote: Think of GB as your monthly processing allowance, not as cloud storage.
  - [1] 2026-11-19: the Community free tier processing stops at 5 GB | capture: sha256:8fbc716d636dc12610400e0bc2952c9bacaa5ab795da24aed6cd13fe66636ec4 | quote: Service stops at 5 GB
- sources:
  - [1] https://www.transloadit.com/pricing/
