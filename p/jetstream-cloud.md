# NSF ACCESS

> jetstream-cloud.org | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jetstream-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/jetstream-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NSF ACCESS / Jetstream2 object store (OpenStack Swift, S3-compatible) — 1 TB default storage per allocation

- `storage/nsf-access-jetstream2-object-store-1-tb-default-storage` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.jetstream-cloud.org/general/quotas/
- free tier: 'By default, all allocations receive 1 TB (1000 GB) of Jetstream2 Storage quota.' Additional storage is bought with ACCESS credits at '1 ACCESS credit == 1 GB', and the default is a floor, not additive: 'the default 1 TB is replaced by a discrete allocation, not added on top of it.' Explore projects carry 400,000 credits; Discover 1,500,000; Accelerate 3,000,000. So storage up to hundreds of TB is purchasable with credits, subject to justification review. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered within the NSF cloud; temp URLs and public containers serve objects over HTTPS. | metered: no
- identity: institution
- interface: s3-compatible, cli
- limits:
  - write-gated (binding): review [1]
  - write-gated (binding): reviewed but not a full panel) [1]
- limits note: per-object-cap: Swift, so large objects need segmentation; no single documented byte cap. Retention: storage is allocation-lifetime. request-rate: not published. Gate: ACCESS allocation (institutional email required; Explore is the lightest at 'Overview' requirements, reviewed but not a full panel).
- interface detail: s3
- tooling: 'The Jetstream2 object store utilizes OpenStack Swift and is S3 compatible. You can utilize it via Horizon or the command line interface (CLI). From the CLI, you can use the OpenStack CLI's container and object commands, the AWS CLI's s3api, or other compatible tools.' Temp-URL keys give signed GET and signed PUT for a single object.
- composes with: 1 TB default per allocation, but storage is credit-purchased, so the multiplier is ACCESS credits across project types (Explore 400k / Discover 1.5M / Accelerate 3M) and multiple requests (Explore and Discover explicitly allow 'Multiple requests allowed'). A 400k-credit Explore project = 400 GB above the default if spent purely on storage. The credit exchange rate, not a per-account cap, is the ceiling.
- reliability: Docs state plainly 'Jetstream2 is not primarily a storage service; large-capacity storage is beyond the scope of Jetstream2'. Treat as a 1-50 TB tier, not an archive.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'By default, all allocations receive 1 TB (1000 GB) of Jetstream2 Storage quota', '1 ACCESS credit == 1 GB', 'the default 1 TB is replaced by a discrete allocation, not added on top of it'
  - [2] 2026-10-21: 'The Jetstream2 object store utilizes OpenStack Swift and is S3 compatible', temp URL for GET and PUT
  - [3] 2026-10-21: Explore 400,000 / Discover 1,500,000 / Accelerate 3,000,000 credit limits; 'Multiple requests allowed' for the first three tiers
  - [4] 2026-10-21: 
- sources:
  - [1] https://docs.jetstream-cloud.org/general/quotas/
  - [2] https://docs.jetstream-cloud.org/general/object/
  - [3] https://allocations.access-ci.org/project-types
  - [4] https://allocations.access-ci.org/get-your-first-project

## Jetstream2

- `compute/jetstream2` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:51.585Z (live) | stale on 2026-12-04
- url https://docs.jetstream-cloud.org/general/vmsizes/
- free tier: Jetstream2 bills every instance in ACCESS service units: 'a service unit (SU) is equivalent to 1 vCPU for 1 hour of wall clock time'. CPU flavours cost 1 SU per vCPU per hour and Large Memory flavours 2 SU per vCPU per hour; GPU flavours list a flat SU rate per hour. A100 (40 GB GPU RAM): g3.xl, 32 vCPU, 120 GB RAM, 64 SU per hour; g3.large, 16 vCPU, 20 GB GPU RAM, 32 SU per hour; g3.medium, 8 vCPU, 10 GB GPU RAM, 16 SU per hour. L40S (48 GB GPU RAM): g4.xl, 12 vCPU, 84 SU per hour. H100 (80 GB GPU RAM): g5.xl, 20 vCPU, 128 SU per hour. The L40S and H100 flavours are not available by default and need a request with justification. The page lists no A100 80 GB, RTX 4090 or L4 flavour and no dollar price, and states no minimum bill. The smallest ACCESS tier, Explore, carries 400,000 credits, so 400,000 / 64 = 6,250 hours of a full A100 card, 12,500 hours of a half card, 3,125 hours of an H100 card at 128 SU per hour, or 400,000 vCPU-hours on CPU flavours. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: credit-converted-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding):  [1]
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the conversion the ACCESS record lacked: an Explore allocation is not 400,000 abstract credits but 6,250 A100-hours or 400,000 vCPU-hours, which turns the ACCESS tier from a benchmark allowance into roughly a year of a single always-on A100 at 16 hours a day. It composes badly with the free GPU vendors, because the same workload that fits a 40 GB card on Jetstream2 fits a 16 GB T4 elsewhere only after splitting.
- reliability: no reliability event recorded
- notes: This finding changes compute/access: that record states the 400,000 credit limit but does not convert it, so a reader cannot tell whether Explore buys an afternoon or a year. The division is shown above and uses only rates from the two vendor pages. The cheapest paid shape is not applicable: Jetstream2 sells nothing for cash, and the credits are not purchasable, so the alternative to the institutional gate is not money. Note that stopped instances are still charged 75 percent and shelved instances are charged nothing, which changes the effective hours for an interactive workload.
- extras:
  - facets.class: academic-cloud
  - facets.free_tier_kind: credit-converted-allocation
  - facets.shape.vcpu: 32
  - facets.shape.ram_gib: 120
  - facets.shape.gpu_class: NVIDIA A100 40 GB
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: "1 ACCESS Credit = 1 Jetstream2 SU"; SU consumption is "1 SU per vCPU_core-hour" on CPU and "2 SUs per vCPU_core-hour" on Jetstream2-GPU and Large Memory, quoted
  - [1] 2026-10-22: g3.xl is 32 vCPU, 120 GB RAM, NVIDIA A100 with 40 GB GPU RAM at 64 SU per hour; g3.large is 16 vCPU, 20 GB GPU RAM at 32 SU per hour; g3.medium is 8 vCPU, 10 GB GPU RAM at 16 SU per hour, quoted from the flavour tables
  - [3] 2026-10-22: "To use Jetstream2, your account must belong to an ACCESS allocation that is active on a Jetstream2 resource", quoted
  - [1] 2026-10-22: "The three instance types are all separate ACCESS resources ... Having access to one does NOT include access to all", quoted
  - [4] 2026-10-22: Explore ACCESS credit limit is 400,000, accepted anytime, quoted
  - [1] 2026-11-03: the H100 flavour g5.xl is 20 vCPU and 128 SU per hour | capture: sha256:305ac0b3227f1f4b448de81dc2661776a2c2860a085123bb6aa6d87a026a04fc | quote: | g5.xl[1]* | 20 | 240 | 60 | H100 | 80 | 128 |
  - [1] 2026-11-03: the L40S flavour g4.xl is 12 vCPU and 84 SU per hour | capture: sha256:305ac0b3227f1f4b448de81dc2661776a2c2860a085123bb6aa6d87a026a04fc | quote: | g4.xl[1]* | 12 | 120 | 60 | L40S | 48 | 84 |
  - [1] 2026-11-03: L40S and H100 flavours need a request to the help desk with justification | capture: sha256:305ac0b3227f1f4b448de81dc2661776a2c2860a085123bb6aa6d87a026a04fc | quote: L40S and H100 flavors are not available by default.
  - [1] 2026-11-03: the billing unit is the vCPU-hour of wall clock time | capture: sha256:305ac0b3227f1f4b448de81dc2661776a2c2860a085123bb6aa6d87a026a04fc | quote: 1 service unit (SU) is equivalent to 1 vCPU for 1 hour of wall clock time
  - [1] 2026-11-03: the A100 flavour g3.xl is 32 vCPU, 40 GB GPU RAM and 64 SU per hour | capture: sha256:305ac0b3227f1f4b448de81dc2661776a2c2860a085123bb6aa6d87a026a04fc | quote: | g3.xl[1] | 32 | 120 | 60 | A100 | 40 | 64 |
- sources:
  - [1] https://docs.jetstream-cloud.org/general/vmsizes/
  - [2] https://docs.jetstream-cloud.org/general/access/
  - [3] https://docs.jetstream-cloud.org/faq/alloc/
  - [4] https://allocations.access-ci.org/project-types
