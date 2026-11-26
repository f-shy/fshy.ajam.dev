# Neon

> neon.com | Compute, Databases and KV, Inference, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neon/ | JSON https://fshy.ajam.dev/api/v1/entity/neon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neon (Compute)

- `compute/neon` | qualifies-with-caveat | evidence reported | category managed database
- needs card no, phone no, ID no, institution no | verified 2026-11-18T04:58:12.815Z (live) | stale on 2026-12-03
- url https://neon.com/pricing
- duplicate of `databases-kv/neon`
- free tier: a free plan with 100 compute unit-hours a month per project and 1 GB of storage per project, no time limit and no credit card | unit: hours | metered on: wall-clock | read on: 2026-10-06 | source: [1] | note: the free plan does not auto-delete, but 100 CU-hours is exhaustible
- per-object cap: not applicable
- retention: data is retained; the compute allowance, not the data, is the limit | source: [1]
- egress: Egress is metered as public network transfer. | metered: yes | free allowance: 5 GB per project per month (Free); 500 GB per project per month (Launch/Scale) | price per TB: USD 0.10 per GB above 500 GB | source: [1]
- identity: email | detail: 'no credit card required' on the free plan, quoted
- interface: ssh
- limits:
  - request-rate: 100 compute unit-hours a month per project [1]
  - per-object-cap: 1 GB of storage per project [1]
- limits note: scale-to-zero is what makes the allowance last; a database kept awake consumes the whole month
- binding note: compute suspends on exhausting 100 CU-hours or 5 GB of transfer in a project-month, and the suspension lasts until the period resets
- interface detail: a PostgreSQL connection string; scale-to-zero and autosuspend
- tooling: any Postgres client; the Neon API and CLI; branching
- composes with: 100 CU-hours a month is the clock, and a database that never sleeps exhausts it
- reliability: no reliability event recorded
- notes: Neon Serverless Postgres provides a free tier with 100 Compute Unit (CU) hours per project per month. A continuous always-on database consuming 1 CU consumes 730 hours monthly, exhausting the 100 CU-hour monthly allowance in approximately four days. Compute automatically pauses when idle.
- evidence note: re-read live on 2026-10-22 for the free-tier and limit figures
- extras:
  - billing_model: wall-clock
  - session_cap.restart_required: no
  - session_cap.note: scales to zero when idle
  - persistent_storage.included_gib: 1
  - persistent_storage.price_gib_month: 1 GB included
  - persistent_storage.durability: Postgres
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while the project exists
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: the Postgres port
  - network_out.ipv6: yes
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-06: free plan: 100 CU-hours a month per project, 1 GB storage per project, no time limit, no credit card
  - [1] 2026-10-22: read live: 100 CU-hours a month per project, permanent free plan
  - [2] 2026-10-22: '100 CU-hours of compute per project per month, 1 GB of Postgres storage per project (up to 20 GB total across all projects), and 5 GB of public network transfer per project per month', with 'Compute quotas are measured per project, so 100 projects each get their own 100 CU-hour bucket' and 'Running out of CU-hours or egress (5 GB) suspends compute until the next billing period', quoted
  - [1] 2026-11-18: not stated | capture: sha256:8632e5161232e811f5f3aa4c55f1982dbbf3e97cad0475a5406a92864f2ffd09 | quote: # Neon Pricing Plans > Neon is a complete set of cloud backend primitives built around Lakebase Postgres, for developers, startups, and agent platforms, from Databricks. Services include Lakebase Postgres, Managed Better Auth, a Data API, Functions, Object Storage, and an AI Gate
- sources:
  - [1] https://neon.com/pricing
  - [2] https://neon.com/faqs/free-plan-limits-and-quotas

## Neon (Lakebase Postgres)

- `databases-kv/neon` | qualifies-with-caveat | evidence measured | binding request-rate | category serverless Postgres with scale-to-zero
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:21:21.176Z (live) | stale on 2027-01-09
- url https://neon.com/pricing
- free tier: 100 projects; 100 CU-hours per project; 1 GB Postgres storage per project and 20 GB per account; 10 branches per project; 5 GB public network transfer per project per month; 5 GB object storage | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: Free autoscales to 2 CU (8 GB RAM); scale-to-zero after 5 min is always on and cannot be disabled
- per-object cap: 1 GB of Postgres storage per project; exceeding it blocks writes rather than billing | source: [1] | note: 999 GiB is the branch logical size limit on the claimed project, not the free allowance
- retention: no deletion on the free plan: "none of them delete your data". Exceeding 100 CU-hours or 5 GB of network transfer for the month suspends compute until the next billing period; exceeding 1 GB of Postgres storage per project fails operations that increase storage until space is freed; idle compute scales to zero after 5 minutes and restarts on the next query. | source: [1] | note: null is indefinite: the free plan does not delete data when a limit is reached; it suspends compute or fails storage-growing operations instead, and compute resumes at the next billing period or on upgrade. The only countdown on the page is the 72-hour deadline to claim an unclaimed Claimable Neon project, which is a separate anonymous path, not the free plan.
- egress: 5 GB public network transfer per project per month included; exceeding it suspends compute until the next billing period | metered: yes | free allowance: 5 GB per project per month | price per TB: USD 0.10/GB on Launch and Scale after 500 GB | source: [2]
- identity: email | detail: email signup for a normal account; the Claimable path provisions a project with no signup, no card and no email, and the project expires in 72 hours unless claimed
- interface: rest, cli
- limits:
  - request-rate (binding): 100 CU-hours per project per month; a 0.25 CU minimum means about 400 wall-clock hours of a minimum-size database, and autoscaling to 2 CU quarters that [1]
  - retention-clamped: compute suspends after 5 minutes idle on Free and the setting cannot be disabled [3]
  - per-object-cap: 1 GB storage per project, 20 GB per account; writes are blocked at the cap [1]
  - request-rate (binding): 5 GB public network transfer per project per month; exceeding it suspends compute [2]
- limits note: connection pooling accepts up to 10,000 client connections in transaction mode; max_connections was 450 on the observed compute and is capped at 4,000 above 9 CU
- interface detail: Postgres wire protocol over TLS on a -pooler or direct host; a Management API and the Neon CLI; a Data API for HTTP queries
- tooling: any Postgres client (psql, psycopg, pg8000, Prisma, Drizzle); rclone does not apply
- composes with: a free Postgres behind a free Worker or a tunnel gives a public endpoint with no card
- reliability: the unclaimed path is a 72-hour demo: 100 MB storage, 1 GB transfer, then the project expires; commit latency on a cold anonymous project measured 1,750 ms
- notes: Storage is generous and compute is not. 100 projects x 1 GB is 100 GB nominal, but each project also gets 100 CU-hours, so the shape is 100 small workloads and not one 100 GB database. The free tier does not delete data; it suspends compute or blocks writes. The measured 100 MB cap belongs to the anonymous Claimable path, not the free plan, and conflating them is the easy error. The vector extension was installed and queried, not merely listed as available, so `pgvector on a free Postgres` is a working chain and not an inference.
- evidence note: a Postgres 17.11 connection, a write and a read-back were run on 2026-10-22; the 100 MB cap was reached and its SQLSTATE recorded. The free-plan figures are a first-party page.
- evidence:
  - probe:https://claimable.neon.tech/v1/agent/identity 2026-10-22: POST with type anonymous returned 201 in 4.5 s, provisioning project lucky-queen-53359445 in aws-us-east-2 with expires_at 2026-10-25T02:41:43Z; 1480 bytes; no signup, no card, no email
  - probe:https://claimable.neon.tech/v1/oauth2/token 2026-10-22: grant_type urn:ietf:params:oauth:grant-type:jwt-bearer with the identity assertion returned 200 and a 3600-second bearer token; the token-exchange grant type is rejected with a 400
  - probe:https://claimable.neon.tech/v1/projects/lucky-queen-53359445/connection_uri 2026-10-22: 200 with a working postgresql:// URI only when database_name and role_name are supplied; without them the proxy returns 502 with an upstream decode error
  - probe:postgresql://ep-old-hall-b4ghd096-pooler.c-6.us-east-2.aws.neon.tech/neondb 2026-10-22: PostgreSQL 17.11 connected in 2619 ms over TLS; create table, insert and select returned a test string; max_connections 450; idle_in_transaction_session_timeout 5min; vector 0.8.0, postgis 3.5.7, timescaledb 2.17.1 and pg_trgm available
  - probe:neon.max_cluster_size 2026-10-22: SHOW returns 100MB; filling with 500 kB rows failed at SQLSTATE 53100 with 'could not extend file because project size limit (100 MB) has been exceeded', hint naming neon.max_cluster_size and pagestore_smgr.c:throttle_or_fail_extension, after 70 rows and 78 MB of reported database size
  - probe:neon commit latency 2026-10-22: ten single-row autocommit inserts averaged 1,750.6 ms each on a cold anonymous project; 35 MB of bulk insert took 21.8 s, or 1.61 MB/s
  - [1] 2026-10-22: 100 projects, 100 CU-hours/project, 1 GB/project and 20 GB/account storage, 5 GB egress/project, scale-to-zero after 5 min on Free, and the sentence that none of the limits delete data
  - [2] 2026-10-22: 5 GB per project per month included on Free; exceeding it suspends compute until the next billing cycle
  - [4] 2026-10-22: PgBouncer transaction mode accepts up to 10,000 client connections, pools sized at 0.9 x max_connections
  - [5] 2026-10-22: unclaimed projects expire in 72 hours and are capped at 100 MB storage and 1 GB transfer; claim codes expire in 15 minutes
  - probe:create extension vector on the claimable project 2026-10-22: CREATE EXTENSION vector succeeded in 1.1 s and pg_extension reported version 0.8.0; a vector(3) column, an insert of two rows and an ORDER BY e <-> '[1,2,3]' KNN query returned distances 0.0 and 5.196 in order; run after dropping the fill, bulk and lat tables from the cap probe, at which point the database was 7440 kB
  - [4] 2026-10-22: PgBouncer transaction mode accepts up to 10,000 client connections; pool size defaults to 90% of max_connections
  - probe:https://neon.com/pricing 2026-11-09: the free plan is permanent and none of its limits delete data; the same page states the compute-suspend, storage-block and idle scale-to-zero conditions | capture: sha256:1e83d27b91ce9dd1296e8e8688676bbfdbea468dc08e37136031e4cc679606b8 | quote: The Free plan is permanent, not a trial, and doesn't require a credit card. Most limits are per project, and none of them delete your data:
  - probe:https://neon.com/pricing 2026-11-09: free projects are not paused for inactivity; idle compute scales to zero after 5 minutes and restarts on the next query, and the page also gives the 72-hour unclaimed-project deadline | capture: sha256:1e83d27b91ce9dd1296e8e8688676bbfdbea468dc08e37136031e4cc679606b8 | quote: No. Neon doesn't pause Free projects for inactivity, and there's no restore step. When a database is idle, its compute scales to zero after 5 minutes and starts again on the next query
- sources:
  - [1] https://neon.com/pricing
  - [2] https://neon.com/docs/introduction/network-transfer
  - [3] https://neon.com/docs/introduction/scale-to-zero
  - [4] https://neon.com/docs/connect/connection-pooling
  - [5] https://neon.com/docs/reference/claimable-neon

## Neon (Inference)

- `inference/neon` | fails-identity | evidence documented | binding write-gated | category data platform with an inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://neon.com/pricing
- free tier: AI Gateway is available on all Neon plans including Free, but inference needs prepaid credits (USD 5 minimum, card required); the model page states inference is free during the private preview. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: AI Gateway on the Free plan requires adding a card and buying prepaid credits (USD 5 minimum)
- interface: rest
- limits:
  - write-gated (binding): AI Gateway needs prepaid credits (USD 5 minimum), card required, even on the Free plan [1]
- endpoint: ${NEON_AI_GATEWAY_BASE_URL}/v1
- tooling: OpenAI-compatible clients through the Neon AI Gateway with a Neon key
- composes with: the prepaid-credit requirement and card gate are the scarce link, despite a private-preview free period
- reliability: inference is stated free only during the private preview; when that ends, list-price token charges apply
- notes: A card is required to use the AI Gateway even on the Free plan; free inference exists only as a private-preview statement, not a standing tier.
- evidence:
  - [1] 2026-11-18: AI Gateway on the Free plan requires prepaid credits and a card | capture: sha256:8632e5161232e811f5f3aa4c55f1982dbbf3e97cad0475a5406a92864f2ffd09 | quote: AI Gateway | Prepaid credits (no markup), card required
  - [2] 2026-11-18: inference is free during the private preview | capture: sha256:6bc089a4dbbfb017c40db9c74f41ef41d7d6cdb9abcce52f0a7683367dd8004d | quote: Inference is free during the private preview
- sources:
  - [1] https://neon.com/pricing
  - [2] https://neon.com/docs/ai-gateway/overview.md

## Neon (Object Storage + Postgres)

- `storage/neon` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:48.162Z (live) | stale on 2026-12-04
- url https://neon.com
- free tier: 5 GB object storage per project + 1 GB Postgres per project (20 GB account total); 100 projects on Free | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: object size 5 GiB | bytes: 5368709120 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 5 GB/month public network transfer per project, shared across Postgres, object storage and functions; then $0.10/GB on paid only. Free is a hard 5 GB. | metered: yes | free allowance: 5 GB per month
- identity: institution
- interface: s3-compatible, cli
- limits:
  - per-object-cap (binding): object size 5 GiB [1]
- limits note: Max object size 5 GiB; throttling returns 503 SlowDown under load; path-style only, no virtual-host buckets; ACL/policy must be set via Console/API, not S3 wire. 5 GB egress/project/month is the real wall for serving.
- interface detail: s3
- tooling: Real S3 API (`forcePathStyle: true`, path-style only), AWS SDK/boto3/aws CLI, `neon buckets` CLI, files-sdk.dev `neon` adapter. Endpoint is per-branch: https://br-<name>.storage.<cell>.<region>.aws.neon.tech
- composes with: 100 projects/org (Free) x 5 GB object storage = 500 GB; x 20 GB Postgres cap = only 20 GB of DB storage, but object storage is NOT under that 20 GB cap. It is per project. Add branches: 10 branches/project, objects branch without copying. Multiple orgs per account are allowed ('one Neon account can belong to multiple orgs on different plans').
- reliability: Compute scale-to-zero after 5 min (Free, cannot disable); project data persists. Rate limiting is documented and retryable.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB object storage per project + 1 GB Postgres per project (20 GB account total); 100 projects on Free
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Storage 1 GB/project, 20 GB account total | Object Storage 5 GB per project included | Public network transfer (egress) 5 GB per project included | Projects 100'
  - [2] 2026-10-21: 'Free plan object storage 5 GB per project'
  - [3] 2026-10-21: 'compatible with the AWS SDK..., forcePathStyle: true, path-style addressing only'
  - [1] 2026-11-19: the Free plan still includes 5 GB per project of public network transfer and $0.10/GB applies only on paid plans | capture: sha256:0f652f75a4e552f89c9c83104f3bca6c4132cc262b20103500c71e75be31215f | quote: | [Public network transfer](https://neon.com/docs/introduction/plans#public-network-transfer) | 5 GB per project included | 500 GB per project included, then $0.10/GB | 500 GB per project included, then $0.10/GB |
  - [2] 2026-11-19: the single-request object size maximum on Neon Object Storage is 5 GiB | capture: sha256:f099519ccaf0088d5d37eb27939456b12a04d1a2dcb71fa1b167615b070a6ebb | quote: | Object size, single-request upload (maximum) | 5 GiB |
  - [2] 2026-11-19: multipart upload allows objects up to 10 GiB, a larger cap than the single-request 5 GiB | capture: sha256:f099519ccaf0088d5d37eb27939456b12a04d1a2dcb71fa1b167615b070a6ebb | quote: | Object size, [multipart upload](https://neon.com/docs/storage/objects#multipart-upload) (maximum) | 10 GiB |
  - [3] 2026-11-19: the S3-compatible interface and SDK/CLI tooling are still documented | capture: sha256:2874c3467b571a7672484ca33a8300b19ab8b0512532758de47ded9c2bf993cb | quote: Neon Object Storage is compatible with the S3 API for core operations. It works with the AWS SDK for JavaScript (@aws-sdk/client-s3), boto3, the AWS CLI, and other S3-compatible tools.
- sources:
  - [1] https://neon.com/docs/introduction/plans
  - [2] https://neon.com/docs/storage/overview
  - [3] https://neon.com/docs/storage/s3-compatibility
