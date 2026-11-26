# roboflow

> roboflow.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roboflow/ | JSON https://fshy.ajam.dev/api/v1/entity/roboflow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## roboflow (free tier)

- `storage/roboflow` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:03.330Z (live) | stale on 2026-12-04
- url https://roboflow.com/pricing
- free tier: None reachable: Datasets are 'Uncapped; On-demand' in size, which looks like a win, but the free tier meters storage through a credit system (10 credits/month) and every operation. Storage, labelling, trai. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Datasets are 'Uncapped; On-demand' in size, which looks like a win, but the free tier meters storage through a credit system (10 credits/month) and every operation — storage, labelling…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Datasets are 'Uncapped; On-demand' in size, which looks like a win, but the free tier meters storage through a credit system (10 credits/month) and every operation — storage, labelling…
  - [1] 2026-11-19: the free tier provides 10 credits per month, metering usage | capture: sha256:568a3f344ccabef6d62b9493587e6173c8dcdf2f0ca0eb9714de73fbda3dbca2 | quote: 10 credits included a month
  - [1] 2026-11-19: dataset size is uncapped on-demand while operations consume credits | capture: sha256:568a3f344ccabef6d62b9493587e6173c8dcdf2f0ca0eb9714de73fbda3dbca2 | quote: Dataset Size Limit | Uncapped; On-demand | Uncapped; On-demand
- sources:
  - [1] https://roboflow.com/pricing
