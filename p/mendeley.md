# Mendeley Data

> mendeley.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mendeley/ | JSON https://fshy.ajam.dev/api/v1/entity/mendeley.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mendeley Data (Elsevier)

- `storage/mendeley-data` | fails-quota | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.mendeley.com
- free tier: 10 GB per dataset, free, unlimited datasets per account ('you can split your datasets into small sizes'; 'we can reference datasets within datasets'). Institutional Digital Commons Data raises this to 100 GB/dataset. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 10 GB | bytes: 10000000000 | source: [1] | note: not stated
- retention: | Published datasets cannot be edited or deleted (versioning only). A write-once archive, not a mutable store. | source: [1] | note: not stated
- egress: Free, public datasets downloadable without login. Backed by AWS S3 eu-west-1 plus DANS long-term archive (three replicas). | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 10 GB [1]
- limits note: per-object-cap: 10 GB per dataset (100 GB institutional). Retention: published datasets are immutable and 'archived with DANS ... in perpetuity', no expiry. Read path caveat: the download URL pattern returns a JSON envelope rather than bytes for non-existent file IDs, so anonymous bulk scraping needs real file UUIDs from the dataset API.
- interface detail: rest
- tooling: Documented REST API (data.mendeley.com/api/docs) with OAuth2 client-credentials; search endpoint `/api/datasets/v2/search` is anonymous. Download URLs are `/public-files/datasets/<id>/files/<fileid>/file_downloaded`.
- composes with: 10 GB per dataset × unlimited datasets per account = effectively unbounded per identity; multiple free accounts multiply further. This is the cleanest 'per-record unlimited' shape in the niche.
- reliability: Published datasets cannot be edited or deleted (versioning only). A write-once archive, not a mutable store. Download endpoint resolves via JSON for bad IDs, so naive crawlers must parse the API first.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GB per dataset, free, unlimited datasets per account ('you can split your datasets into small sizes'; 'we can reference datasets within datasets'). Institutional Digital Commons Data raises this to 100 GB/dataset.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 100 GB institutional cap, DANS perpetuity archiving, 'once a dataset is published, it is not possible to edit or delete it'
  - [1] 2026-10-21: '10GB per dataset limit', with the vendor's split-and-reference alternative route
  - [3] 2026-10-21: probe: GET -> 200, real dataset JSON with doi 10.17632/...
  - withheld 2026-10-21: probe: GET .../public-files/datasets/jxj8bn2vyf/files/1/file_downloaded -> 200 but Content-Type application/json, code 400 envelope (not bytes) — read path needs real file UUIDs
- sources:
  - [1] https://www.elsevier.support/mendeley/answer/what-can-i-do-when-my-dataset-exceeds-the-10gb-per-dataset-limit
  - [2] https://data.mendeley.com/faq
  - [3] https://data.mendeley.com/api/datasets/v2/search?query=test&limit=1
