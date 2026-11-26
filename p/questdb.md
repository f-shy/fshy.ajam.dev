# QuestDB Cloud

> questdb.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/questdb/ | JSON https://fshy.ajam.dev/api/v1/entity/questdb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## QuestDB Cloud (managed, Enterprise/BYOC)

- `databases-kv/questdb-cloud` | paid-only | evidence documented | binding none | category managed time-series SQL database (Enterprise and Bring Your Own Cloud); the former self-serve QuestDB Cloud is retired | tier Enterprise / BYOC (no self-serve tier)
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T02:46:18.052Z (live) | stale on 2026-12-20
- url https://questdb.com/pricing
- free tier: No self-serve free tier is offered. The first-party pricing/Enterprise page offers a Free Enterprise Trial and a Talk to Sales route, with production offered as self-managed Enterprise or Bring Your Own Cloud (BYOC); no public per-instance price is listed. | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: The first-party page presents only Open Source (self-managed, Apache 2.0) and Enterprise (production, contact sales or trial); the fully managed self-serve 'QuestDB Cloud' plan is not offered as a sign-it-yourself tier.
- per-object cap: unverified: no per-object or storage cap is published on the first-party pricing/Enterprise page | source: [1]
- retention: unverified: no hosted-plan retention period is published on the first-party pricing/Enterprise page; Enterprise supports tiered storage with hot data plus Parquet/Iceberg on object storage and TTL-based deletion or archival. | source: [1] | note: TTL and downsampling are described for the Enterprise engine; no fixed hosted retention window is stated.
- egress: unverified: no first-party hosted egress allowance or price is published; the Enterprise tier offers tiered object storage on Amazon S3, Azure Blob or GCS queried in SQL. | metered: no | source: [1]
- identity: institution | detail: The first-party page routes production users to Talk to Sales or a Free Enterprise Trial and describes Bring Your Own Cloud, in which the user's team deploys inside its own AWS or Azure account. No self-serve signup with email or card is published for a hosted plan.
- interface: rest, cli, browser
- limits:
  - volume-quota: unverified: no published numeric limit for a hosted self-serve tier (no such tier is offered); Enterprise capacity is set by contract [1]
- binding note: No hosted self-serve tier or numeric limit exists; the binding constraint is access: production needs a sales-led Enterprise/BYOC engagement rather than a public free allowance.
- interface detail: QuestDB speaks the PostgreSQL wire protocol for SQL queries and accepts InfluxDB Line Protocol for ingestion; a web SQL console is listed among the features. Enterprise adds TLS on all protocols and OAuth/OIDC SSO.
- tooling: PostgreSQL drivers and psql for SQL; InfluxDB Line Protocol clients for ingest; official QuestDB clients; the self-managed Open Source build is binaries, containers and source code
- composes with: A managed QuestDB deployment is reached with existing PostgreSQL tooling; the open-source QuestDB engine that the user installs and runs on a rented or free machine, or on-premises/hybrid Enterprise, is the last-resort option when no hosted self-serve plan is available.
- reliability: The former self-serve managed QuestDB Cloud is not offered on the first-party pricing page; production is a sales-led Enterprise or BYOC engagement with 99.9% uptime and SLA-backed support. The Open Source edition has basic auth over unencrypted transmission and community-only support.
- notes: QuestDB's first-party page no longer offers a self-serve managed 'QuestDB Cloud'. It lists Open Source (the user installs and runs it) and sales-led Enterprise/BYOC with a Free Enterprise Trial. No hosted price or quota is published; the lack of a public self-serve hosted offer is the finding, with self-hosting only the last resort.
- evidence note: The first-party QuestDB pricing/Enterprise page was captured on 2026-11-19; it lists only Open Source and Enterprise/BYOC with a sales and trial route and no hosted self-serve price. No hosted numeric limits are published, so those fields are unverified.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the hosted production route is sales-led with a trial; no self-serve price is on the page | capture: sha256:8144a5f63456aeed5b4bcc928187c3dd8c1d1eea1c3f2a60158f9a0338d2fc3d | quote: Contact SalesFree Enterprise Trial
  - [1] 2026-11-19: BYOC is an offered deployment model | capture: sha256:8144a5f63456aeed5b4bcc928187c3dd8c1d1eea1c3f2a60158f9a0338d2fc3d | quote: Bring Your Own Cloud
  - [1] 2026-11-19: hosted Enterprise runs in the user's own cloud or premises | capture: sha256:8144a5f63456aeed5b4bcc928187c3dd8c1d1eea1c3f2a60158f9a0338d2fc3d | quote: Self-managed or Bring Your Own Cloud (BYOC), with QuestDB ops team taking care of your deployment, on-premises or cloud-native
  - [2] 2026-11-19: the first-party site advertises an Enterprise trial rather than a self-serve hosted free plan | capture: sha256:0a410297e32cd0217e5ac0bc549bcde29cf84f68c948c3f4c1b45d1d4e558cbf | quote: Free Enterprise Trial
- sources:
  - [1] https://questdb.com/pricing
  - [2] https://questdb.com/
