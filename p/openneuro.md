# OpenNeuro

> openneuro.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openneuro/ | JSON https://fshy.ajam.dev/api/v1/entity/openneuro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenNeuro

- `storage/openneuro` | qualifies | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://openneuro.org
- free tier: Free, no published per-dataset or per-account cap. 'Is this service free to use? Yes!' A 6.4 TB dataset has been deposited (staged incrementally). | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none published; the real cap is a transient staging worker ('files are stored on a worker with relatively limited storage space'), so very large datasets must be uploaded in batches with ~24 h waits between snapshots. Retention: permanent, every version gets its own DOI; 36-month grace before forced public release | days: 1080 | source: [1] | note: not stated
- egress: Free and anonymous. Objects live on Amazon S3 (`s3.amazonaws.com/openneuro.org`), public-read, ranged, CORS-open. No auth, no egress meter. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: s3, git, rclone, cli
- limits note: per-object-cap: none published; the real cap is a transient staging worker ('files are stored on a worker with relatively limited storage space'), so very large datasets must be uploaded in batches with ~24 h waits between snapshots. Retention: permanent, every version gets its own DOI; 36-month grace before forced public release. Binding read limit is per-ip-shaping but weak.
- interface detail: s3
- tooling: Openneuro-cli (`openneuro upload`) + git-annex, and DataLad. Read side is plain anonymous S3 GET. Any S3 client, rclone's s3 remote with no credentials, or plain curl.
- composes with: Unlimited datasets, each a fresh S3 prefix under `openneuro.org/ds<ID>/`. Because the read side is unauthenticated S3, fetch volume never touches OpenNeuro's app tier.
- reliability: Large uploads fail in the staging area and require batch-then-wait choreography; BIDS format is mandatory and undeface-d datasets get deleted after the fact.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Is this service free to use? Yes!', public after 36-month grace, CLI upload supported
  - [2] 2026-10-21: 'The full size is 6.4T', staging worker explanation, a batch-upload alternative route
  - [3] 2026-10-21: probe: GET -> 200, 615 bytes, real BIDS JSON
  - withheld 2026-10-21: probe: 16 parallel ranged GETs of sub-01_T1w.nii.gz -> 3,200,000 bytes in 2.65s (1.21 MB/s) vs 1 connection 200,000 bytes in 3.26s (61 KB/s) — 20x linear scaling
- sources:
  - [1] https://docs.openneuro.org/faq.html
  - [2] https://github.com/OpenNeuroOrg/openneuro/issues/3683
  - [3] https://s3.amazonaws.com/openneuro.org/ds000001/dataset_description.json
