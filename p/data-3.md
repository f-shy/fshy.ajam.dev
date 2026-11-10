# data.world

> data.world | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-3/ | JSON https://fshy.ajam.dev/api/v1/entity/data-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.world

- `storage/data-world` | fails-quota | evidence reported | binding none | category data-marketplace
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.world
- price Community free (100 GB aggregate, 1-3 GB per unit). Professional Community plan $12/month for 20 private projects — ~$120/TB/month against a 100 GB pool, though the per-unit 1 GB cap makes the pool theoretical. | parsed USD 120/TB-mo
- free tier: 100 GB total storage on the free Community plan, but with a 3 GB limit per dataset or project. And their own docs are stricter still: 'Dataset ingested to data.world: 1 GB'; 'Size of a file in a dataset: 1 GB'; 'Number of files in a dataset: 250'; 'Project: 1 GB'. The 100 GB aggregate is therefore unreachable in practice because each unit can only be 1 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free but rate-shaped: 'Number of burst streams API calls: 5 in the first second … then 1 per second'; streamed records capped at 1 MiB; streamed request 1 GB. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: fails-quota by ~500x for the requirement, and the platform is mid-acquisition ('ServiceNow to acquire data.world'), which is a reliability signal. Free tier is aimed at public data projects, not private bulk storage.
- interface detail: rest
- tooling: A real developer API (developer.data.world) plus SQL over datasets, so it is programmatically clean. The API surface is the best part of the product and the quota is the worst.
- composes with: 20 private projects/datasets × 3 GB, or the 100 GB aggregate if per-unit limits were the only constraint. In practice 1 GB per dataset × 100 units is the ceiling, so sharding to 500 GB means 500 units. Three times the published unit count.
- reliability: Ownership change in progress (ServiceNow). The docs' 1 GB ingest limit contradicts the marketing 3 GB figure. Believe the docs.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 GB total storage on the free Community plan, but with a 3 GB limit per dataset or project — and their own docs are stricter still: 'Dataset ingested to data.world: 1 GB'; 'Size of a file in a dataset: 1 GB'; 'Number of files in a dataset: 250'; 'Project: 1 GB'. The 100 GB aggregate is therefore unreachable in practice because each unit can only be 1 GB.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: Community free (100 GB aggregate, 1-3 GB per unit). Professional Community plan $12/month for 20 private projects — ~$120/TB/month against a 100 GB pool, though the per-unit 1 GB cap makes the pool theoretical.
- evidence:
  - [1] 2026-10-21: opened: 'Dataset ingested to data.world: 1 GB'; 'Project: 1 GB'; 'Size of a file in a dataset: 1 GB'; 'Number of files in a dataset: 250'; rate limiting table.
  - [2] 2026-10-21: opened: '20 private projects/datasets', '20 live tables', '3GB limit per dataset or project', '100GB total storage size'; and the banner 'ServiceNow to acquire data.world'.
  - [2] 2026-10-21: same page: the free tier is framed around 'Open Data' access, i.e. read-side value, not storage.
- sources:
  - [1] https://docs.data.world/en/99147-data-size-limit-and-timeout-specifications.html
  - [2] https://data.world/product/community/
