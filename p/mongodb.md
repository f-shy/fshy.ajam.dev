# MongoDB Atlas

> mongodb.com | Databases and KV, Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mongodb/ | JSON https://fshy.ajam.dev/api/v1/entity/mongodb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MongoDB Atlas (free cluster, formerly M0)

- `databases-kv/mongodb-atlas-m0` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category document database
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/
- free tier: 0.5 GB of data storage on a shared cluster with three-node replication, one free cluster per project, free forever | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 16 mebibytes per BSON document, which is the MongoDB engine limit and not a tier limit | bytes: 16777216 | source: [2]
- retention: paused automatically after 30 days with zero connections; resumable unless the cluster ran a version Atlas can no longer restore to | days: 30 | source: [1]
- egress: 10 GB in and 10 GB out per rolling seven-day period; exceeding it throttles the cluster and adds a one-second cooldown per connection | metered: yes | free allowance: 10 GB out per 7 days | source: [1]
- identity: email | detail: an Atlas account; no card on Free
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): 100 operations per second, enforced by throttling with a one-second cooldown [1]
  - per-object-cap: 0.5 GB of data storage; storage size is not configurable on a free cluster [1]
  - request-rate: 10 GB in and 10 GB out per rolling 7-day period [1]
  - retention-clamped: paused after 30 days with zero connections [1]
- limits note: 500 connections maximum; replication factor 3; no sharding, no network peering, and only a subset of regions
- interface detail: the MongoDB wire protocol; a Data API for HTTPS access; the Atlas Administration API and the atlas CLI
- tooling: mongosh, any MongoDB driver, the atlas CLI
- composes with: a free document store that survives inactivity for a month, which is the longest idle clock in this class short of Aiven
- reliability: the page is explicit that Atlas may deactivate idle free clusters under its terms, and recommends exporting a copy before a long pause
- notes: 0.5 GB is a hard wall rather than an overage, and 100 ops/s is a throughput cap that no storage allowance can exceed. The 30-day idle clock is the most forgiving in this class and it is still a clock.
- evidence note: both pages were read on 2026-10-22: the Atlas free-tier limits page for the 0.5 GB, the pause and the throttles, and the server limits page for the 16 mebibyte document cap. The storage figure is 0.5 GB as the page states it. 512 MB is the binary rendering of the same quantity and is not a second figure.
- evidence:
  - [1] 2026-10-22: 'Free clusters: 0.5 GB' for Data Storage; 'Atlas automatically pauses Free clusters after 30 days of inactivity where there are zero connections'; 10 GB in and out per rolling seven-day period; 100 operations per second; 500 connections; 'You can't configure storage size for Free clusters'
  - [2] 2026-10-22: 'The maximum BSON document size is 16 mebibytes', which is an engine limit and not an Atlas tier limit
- sources:
  - [1] https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/
  - [2] https://www.mongodb.com/docs/manual/reference/limits/

## MongoDB

- `compute/mongodb` | fails-identity | evidence documented | binding write-gated | category managed database
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.mongodb.com/solutions/startups
- free tier: Free MongoDB Atlas credits and Voyage AI tokens across four tiers: Inspire for bootstrapped startups, Grow for early-funded, Innovate for rising VC-backed, and Scale for rapidly scaling. Base-tier eligibility: less than 7 years old, Series A or earlier, building a single software-based product, not previously accepted, with an active company website and LinkedIn profile. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The base tier asks for a company less than seven years old at Series A or earlier with an active website and a LinkedIn profile, and refuses development shops and agencies. The credit value per tier is not published.
- interface: rest
- limits:
  - write-gated (binding): The company-shaped application fails first, and the amount is undisclosed, so even a successful applicant cannot size the benefit before committing to the platform. [1]
- limits note: The company-shaped application fails first, and the amount is undisclosed, so even a successful applicant cannot size the benefit before committing to the platform.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Atlas credits at the small-cluster scale are worth tens of dollars a month, so even the top tier is a small absolute benefit beside the compute credits in this class. It composes with a Databricks application, since the two programs overlap on Neon.
- reliability: no reliability event recorded
- notes: One partner landing page, cloud.google.com/mongodb/startups, states up to USD 5,000 in Atlas credits, which contradicts the program page's silence and may be a stale Google-specific co-offer. Recording null rather than either number; the vendor program page is the authority and it publishes none.
- extras:
  - facets.class: startup-credit
  - facets.free_tier_kind: one-shot-credit
- evidence:
  - [1] 2026-10-22: four tiers named Inspire, Grow, Innovate and Scale, each described by funding stage, with no dollar amount published, quoted
  - [1] 2026-10-22: base tier is 'Less than 7 years old and Series A or earlier', a single software product, an active company website and LinkedIn profile, quoted
- sources:
  - [1] https://www.mongodb.com/solutions/startups

## MongoDB Atlas (M0 / Free cluster)

- `storage/mongodb-atlas` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mongodb.com/atlas
- free tier: 512 MB data storage per free cluster (0.5 GB, uncompressed BSON + indexes); one free cluster per project; 250 projects per Atlas user and 250 per organization | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Data transfer out is not the metered axis on M0. There is no published egress allowance or overage for Free clusters; the limits that bite are 500 connections and 100 ops/sec. Effectively unmetered for read volume, which makes M0 unusual in this class. | metered: no
- identity: email
- interface: rest
- limits note: 512 MB total is tiny per unit. The whole value is the 250x multiplier. 100 ops/sec, 500 connections, no sharding, no configurable storage. Cluster creation is heavily rate-limited in practice (one free cluster per project, project creation itself throttled).
- interface detail: rest
- tooling: Standard MongoDB drivers (pymongo, motor), `mongosh`, Atlas Data API (HTTPS), `mongodump`/`mongorestore`; GridFS for files >16 MB via pymongo's gridfs
- composes with: 250 projects per user x 1 free cluster each x 512 MB = ~128 GB per Atlas account, and 250 organizations per user gives another axis. GridFS chunks (255 KB default) mean no practical per-object cap beyond the 512 MB total.
- reliability: Free clusters are shared and throttle at 100 ops/sec; a bulk-write workload will be visibly slow rather than failing. Data is 3-node replicated, no vanishing.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 512 MB data storage per free cluster (0.5 GB, uncompressed BSON + indexes); one free cluster per project; 250 projects per Atlas user and 250 per organization
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'M0 | 512 MB | Shared | Shared | Free forever'
  - [1] 2026-10-21: 'Free clusters: 0.5 GB ... all uncompressed BSON documents ... plus the bytes stored in their associated indexes'; 'only one Free cluster per project'
  - [3] 2026-10-21: 'Projects per Atlas User | 250', 'Projects per Atlas Organization | 250'
- sources:
  - [1] https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/
  - [2] https://www.mongodb.com/pricing
  - [3] https://www.mongodb.com/docs/atlas/reference/atlas-limits/

## mongodb atlas free cluster (m0)

- `storage/mongodb-atlas-free-cluster` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mongodb.com/docs/atlas/reference/faq/storage/
- free tier: none reachable: Free cluster storage is hard-capped at 512 MB ('you are over your space quota, using 513 MB of 512 MB'). | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Hard 512 MB, not configurable: 'you are over your space quota, using 513 MB of 512 MB'..
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard 512 MB, not configurable: 'you are over your space quota, using 513 MB of 512 MB'..
- sources:
  - [1] https://www.mongodb.com/docs/atlas/reference/faq/storage/
