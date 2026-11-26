# lancedb cloud

> usagepricing.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usagepricing/ | JSON https://fshy.ajam.dev/api/v1/entity/usagepricing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## lancedb cloud

- `storage/lancedb-cloud` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:01.974Z (live) | stale on 2026-12-04
- url https://www.usagepricing.com/blueprint/activity/lancedb-2026-08-28-cloud-tier-folded-enterprise
- free tier: none reachable: Self-serve cloud tier joined the Enterprise product line and the free credits program ended. Service provides vector database tables rather than arbitrary object storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: It is a vector/lance-format database, not a blob…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is a vector/lance-format database, not a blob store
  - [2] 2026-10-21: It is a vector/lance-format database, not a blob store
  - [1] 2026-11-19: the self-serve Cloud tier is gone and only free OSS plus sales-led Enterprise remain | capture: sha256:82f92ed9537eb1c03ebe8087d4383d7839f4c0b28776bdbfe8e9375d84f6194a | quote: Two tiers: free OSS, and LanceDB Enterprise (sales-led, annual commit) offered as either a Managed (LanceDB-hosted) or BYOC deployment.
  - [3] 2026-11-19: LanceDB's own docs now present only Enterprise (private cloud/BYOC) as the production option | capture: sha256:47066908fbf41420a5e77f055fbdf7d2ab37052db08d75fb9306326d9d969c26 | quote: LanceDB Enterprise** is the production deployment option for teams that want to run LanceDB as a private cloud or
- sources:
  - [1] https://www.usagepricing.com/blueprint/activity/lancedb-2026-08-28-cloud-tier-folded-enterprise
  - [2] https://startupperks.co/programs/lancedb-lancedb-cloud-free-credits
  - [3] https://docs.lancedb.com/enterprise
