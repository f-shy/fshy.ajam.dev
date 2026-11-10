# Ultralytics HUB

> ultralytics.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ultralytics/ | JSON https://fshy.ajam.dev/api/v1/entity/ultralytics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ultralytics HUB / Ultralytics Platform

- `storage/ultralytics-hub-ultralytics-platform` | fails-quota | evidence reported | binding per-object-cap | category model-hub
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ultralytics.com
- free tier: Free: 100 GB storage, 10 GB per dataset upload, unlimited number of datasets and models. Pro ($29/seat/mo): 500 GB storage, 20 GB per upload. Enterprise: unlimited storage, 50 GB per upload. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 GB per upload | bytes: 20000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered. Storage is the only billed dimension, and models/datasets download without a per-GB charge. No egress line on the pricing page. | metered: yes
- identity: email | detail: email (Google/GitHub OAuth available).
- interface: rest, cli
- limits:
  - per-object-cap (binding): 20 GB per upload [1]
  - per-object-cap (binding): 50 GB per upload [1]
- limits note: 100 GB total storage; individual file limits Images 50 MB, Videos 1 GB, dataset archives 10 GB on Free. That 50 MB image cap is the real killer for bulk image corpora, and the 1 GB video cap kills video datasets outright.
- interface detail: rest
- tooling: The `ultralytics` Python package itself (YOLO) is the client: `model.train(data=..., project=...)` pushes datasets and weights to the platform; there is also a documented REST API and CLI. Extremely well maintained (the YOLO package is one of the most-installed ML packages).
- composes with: Unlimited datasets × but 100 GB account total, so dataset count does not add bytes. The only multiplier is N accounts. Note the asymmetry: 'You can upload unlimited datasets across all plans .. There's no cap on the number of datasets themselves, only on total storage'. So the cap is total, cleanly.
- reliability: Stable commercial vendor with a huge user base. Data is tied to the training platform, so it is a walled garden rather than a general-purpose store. But downloads of your own artifacts are not paywalled.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 100 GB storage, 10 GB per dataset upload, unlimited number of datasets and models. Pro ($29/seat/mo): 500 GB storage, 20 GB per upload. Enterprise: unlimited storage, 50 GB per upload.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Storage Store datasets, model weights, and training artifacts — Free 100 GB · Pro 500 GB · Enterprise Unlimited'; 'Dataset Upload Maximum file size for a single dataset upload (ZIP, TAR, or NDJSON) — 10 GB / 20 GB / 50 GB'
  - [1] 2026-10-21: read live FAQ: 'You can upload unlimited datasets across all plans. Storage limits vary by plan: Free includes 100 GB ... There's no cap on the number of datasets themselves, only on total storage'
  - [2] 2026-10-21: read live: 'Individual file limits: Images 50MB, Videos 1GB, datasets 10GB on Free / 20GB on Pro / 50GB on Enterprise'
- sources:
  - [1] https://www.ultralytics.com/plans
  - [2] https://docs.ultralytics.com/platform/data/
