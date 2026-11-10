# Upstash

> upstash.com | Databases and KV, Compute, Storage; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upstash/ | JSON https://fshy.ajam.dev/api/v1/entity/upstash.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Upstash Redis (Databases and KV)

- `databases-kv/upstash-redis` | qualifies | evidence measured | binding request-rate | category serverless Redis and KV
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-12-22
- url https://upstash.com/docs/redis/overall/billing
- price USD 0.20 per 100K commands; storage USD 0.25/GB-month beyond the first 1 GB | parsed USD 250/TB-mo
- free tier: 250 MB data; 500,000 commands per month; 10 GB bandwidth per month; 10,000 commands per second; one database | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: 100 MB per record on Free; 10 MB per request | source: [1]
- retention: a database on a free account persists while the account is active. An anonymous database created with no account is deleted after 3 days unless claimed | days: 3 | source: [2]
- egress: 10 GB bandwidth per month included on Free; pay as you go includes 200 GB then USD 0.03/GB | metered: yes | free allowance: 10 GB per month | price per TB: USD 0.03/GB beyond 200 GB | source: [1]
- identity: anonymous | detail: POST upstash.com/start-redis with an Idempotency-Key provisions a database with no account, no email and no card; the database is deleted after 3 days unless claimed in a browser. A permanent free database needs an email
- interface: rest, cli
- limits:
  - request-rate (binding): 500,000 commands per month on Free, about 16,600 a day [1]
  - per-object-cap: 100 MB per record; 250 MB total data [1]
  - request-rate (binding): 10 GB bandwidth per month [1]
- limits note: adding a payment method moves every database to paid, and 'an account with a payment method cannot have free databases'
- interface detail: a body-style REST API that takes the command as a JSON array; the Redis protocol on the same endpoint; a developer API
- tooling: redis-cli against the TLS endpoint, or any HTTP client against the REST form; @upstash/redis SDKs
- composes with: the cheapest free cache in front of a free Postgres: 100,000 reads a day off the database, if the write path fits 1,000 a day
- reliability: an unclaimed database carries a warning not to store sensitive data because it is not tied to an account; the documented developer API host api.upstash.com did not resolve on 2026-10-22 while the per-database endpoint worked
- notes: The 10,000-commands-per-day figure in circulation is the pre-2025-03 plan. 500,000 a month is 16,600 a day, which is a different shape: a burst is fine and a steady 1/second is not.
- evidence note: a database was provisioned anonymously, PING/SET/GET/DBSIZE were run against it, and the 3-day expiry was read from the response. The free-plan limits are a first-party page.
- evidence:
  - probe:https://upstash.com/start-redis 2026-10-22: POST with Idempotency-Key 5f4fd5c1-7624-43b4-bfc9-94192920d977 returned 200, 3239 bytes, in 7.0 s, with endpoint optimal-spaniel-201484.upstash.io, a bearer token, a console URL and 'Expires: 2026-10-25 (3 days from creation)'
  - probe:https://optimal-spaniel-201484.upstash.io 2026-10-22: body-style REST calls returned PING -> PONG, SET k1 v1 -> OK, GET k1 -> v1, DBSIZE -> 1; each round trip 0.73 to 0.92 s
  - [1] 2026-10-22: Free: 250 MB data, 500K monthly commands, 10 GB monthly bandwidth, 10,000 commands/s, 10 MB request, 100 MB record, 1 database, no credit card
  - probe:https://api.upstash.com/v2/redis/databases 2026-10-22: curl could not resolve api.upstash.com on 2026-10-22, so the documented developer API host is not reachable from this network even though the per-database endpoint is
- sources:
  - [1] https://upstash.com/docs/redis/overall/billing
  - [2] https://upstash.com/start-redis

## Upstash Box

- `compute/upstash-box` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:09.968Z (live) | stale on 2026-12-05
- url https://upstash.com/pricing/box
- price parsed USD 8/mo
- free tier: Free: USD 0, 10 concurrent boxes, 5 CPU hours a month, USD 1 of LLM token budget a month | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: after the LLM limit the API returns 400 Bad Request
- per-object cap: not applicable
- retention: standard boxes auto-pause when idle with no CPU charges; keep-alive boxes run continuously at a fixed monthly price | days: 0
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: Free plan is USD 0; no card stated on the pricing page
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): Free 10 concurrent boxes; pay-as-you-go 1,000 by default [1]
  - per-object-cap: largest size is Large: 8 vCPU / 16 GB / 20 GB disk [1]
- limits note: 5 GB, 10 GB and 20 GB of disk on Small, Medium and Large; disk is the tightest resource on this page
- binding note: 5 CPU hours a month of active CPU is the allowance and the 5 GB disk is the shape
- interface detail: TypeScript and Python SDKs, a Box CLI, and SSH to <box-id>@us-east-1.box.upstash.com; boxes run on AWS us-east-1 only
- tooling: Upstash SDK and REST; BYOK for model providers on every plan
- composes with: the split between active-CPU billing and a fixed keep-alive price is the mechanism, and it makes one page carry two products
- reliability: no reliability event recorded
- notes: Upstash Box provides serverless container sandboxes with a free tier offering 5 CPU hours monthly, alongside metered usage plans starting from USD 3.29 monthly.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 5
  - billing_model: consumed-cpu
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: standard boxes auto-pause when idle; the idle interval was not published on the page read
  - keep_rate.value: 0.0
  - keep_rate.basis: standard boxes auto-pause with no CPU charges
  - keep_rate.source: https://upstash.com/pricing/box
  - persistent_storage.included_gib: 5
  - persistent_storage.price_gib_month: USD 0.10
  - persistent_storage.durability: disk kept while the box exists
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: unpublished
  - free_tier_kind: allowance
  - m10h_usd: 3.29
  - m24h_usd: 8.0
  - price_arithmetic: 5 CPU-h / 2 vCPU = 2.5 h of a Small box a month on Free; pay-as-you-go 0.10 x 2 x 300 h = 60, but a keep-alive Small box is USD 8 a month flat
  - price_note: the page carries two products. Small as a keep-alive box is USD 8 a month flat, which prorates to USD 3.29 at 300 hours. Metered active CPU at 100% is USD 0.20 an hour, or USD 60 for 300 hours.
  - price_basis: 10 h/day x 30 = 300 h; 24/7 x 30 = 730 h
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: Free: 10 concurrent boxes, 5 CPU hours a month, USD 1 LLM budget; Pay as You Go 1,000 concurrent
  - [1] 2026-10-22: Small 2 vCPU/4 GB/5 GB at USD 0.10 per active CPU hour or USD 8 a month keep-alive; storage USD 0.10 per GB-month on pay-as-you-go
  - [1] 2026-10-22: standard boxes auto-pause when idle and bill per active CPU hour; keep-alive boxes run continuously at a fixed monthly price
  - [2] 2026-11-03: SSH access to a box exists | capture: sha256:3125ad5faf0d052a0beb3d7ed9962af7220d724d58221d2d28796ccdf25a9c61 | quote: You can access that shell either through the SDK or directly over SSH.
  - [3] 2026-11-03: a Box CLI exists | capture: sha256:a4e0a7dd8c47d4c266dca9836f6cf97fb25a54046d49d631f1cf8fb5930763bf | quote: Create and manage boxes from your terminal.
- sources:
  - [1] https://upstash.com/pricing/box
  - [2] https://upstash.com/docs/box/overall/shell
  - [3] https://upstash.com/docs/box/overall/quickstart

## Upstash (Redis / Vector / QStash)

- `storage/upstash` | fails-quota | evidence reported | binding retention-clamped | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://upstash.com
- free tier: Redis Free: 250 MB max data, 10 GB bandwidth/month, 1 database. Vector Free: 1 GB total data, 200M vectors x dims. QStash Free: 1,000 messages/day, 50 GB bandwidth, 1 MB message. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Unclaimed ephemeral DBs deleted after 3 days. | days: 3 | source: [1] | note: not stated
- egress: Redis Free caps bandwidth at 10 GB/month with max data 250 MB. A 40x fetch amplification before the egress meter binds. Vector Free: bandwidth free/unmetered, storage 1 GB is the wall. | metered: no | free allowance: 10 GB per month
- identity: anonymous
- interface: rest
- limits:
  - retention-clamped (binding): deleted after 3 days [1]
  - retention-clamped (binding): delete at 3 days [1]
- limits note: 250 MB is tiny. 1 database per account. QStash 1 MB max message size makes it useless as storage. Request size 10 MB (upgradeable). Unclaimed ephemeral DBs deleted after 3 days.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Redis protocol (any redis client), REST API for all three products, `@upstash/redis` SDK; QStash is HTTP-only
- composes with: One free database per account on Redis Free ('Max databases | 1'). No per-project multiplication. BUT: `GET https://upstash.com/start-redis` mints a keyless, unauthenticated free Redis with no signup (deleted after 3 days unless claimed); claimed ones become normal free DBs. Vector's 1 GB with 1 MB per vector and 200M vectors is the better storage shape: unlimited vector COUNT, only total bytes capped.
- reliability: Ephemeral DBs (unclaimed) hard-delete at 3 days. Data vanishes by design. Claimed free DBs are durable.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Redis Free: 250 MB max data, 10 GB bandwidth/month, 1 database. Vector Free: 1 GB total data, 200M vectors x dims. QStash Free: 1,000 messages/day, 50 GB bandwidth, 1 MB message.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free | $0/month | - | 250 MB | 10 GB', 'Max databases | 1' on Free
  - [2] 2026-10-21: 'Free | $0 | 200M | 10K | 1 GB', 'Max total data/metadata size: 1 GB'
  - [3] 2026-10-21: 'Free | $0/month | 1,000 | 50 GB | 1 MB'
  - [4] 2026-10-21: probe: GET -> 200, documents zero-signup POST with Idempotency-Key; 'Databases live for 3 days unless claimed'
- sources:
  - [1] https://upstash.com/pricing/redis
  - [2] https://upstash.com/pricing/vector
  - [3] https://upstash.com/pricing/qstash
  - [4] https://upstash.com/start-redis

## Upstash Redis (Storage)

- `storage/upstash-redis` | fails-quota | evidence reported | binding retention-clamped | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://upstash.com/redis
- free tier: 250 MB max data size on Free; 500K commands per month; 10 GB bandwidth/month | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Free DBs minted anonymously are DELETED after 3 days unless claimed. | days: 3 | source: [1] | note: not stated
- egress: Free up to 10 GB per month on the Free plan (~333 MB per day), followed by metered bandwidth billing on paid tiers. | metered: no | free allowance: 10 GB per month
- identity: anonymous
- interface: rest, cli
- limits:
  - retention-clamped (binding): DELETED after 3 days [1]
- limits note: 250 MB data; 10 MB max request size (LIVE-VERIFIED: a 20 MB SET returned 'ERR max request size exceeded. Limit: 10485760 bytes'); 100 MB max record size listed but the 10 MB request cap binds first; 10,000 max cmd/sec; 500K commands/month; 1 database
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: redis-cli over TLS, any Redis client, plus a body-style REST API (`POST` a JSON array command). Verified live: a free database can be minted with no signup via `POST https://upstash.com/start-redis` with an `Idempotency-Key` header.
- composes with: Free tier is 1 database per account (pricing table: 'Max databases | 1'). 250 MB x N accounts. The command quota, not storage, is the wall: 500K commands/month = 16,667/day, and each GET returns at most 10 MB (verified), so max read throughput is 16,667 x 10 MB = 167 GB/day. 3x short of 500 GB/day even with a mythical 250 MB dataset read 667 times a day.
- reliability: Works and is fast; the killer is the command meter. Every GET, SET, EXISTS, and even pipelined command counts. Operational commands (PING, AUTH, INFO, CONFIG, SELECT, COMMAND, RESET, QUIT) are explicitly not charged. Free DBs minted anonymously are DELETED after 3 days unless claimed.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 250 MB max data size on Free; 500K commands per month; 10 GB bandwidth/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free | $0/month | 250 MB | 10 GB' (Max Data / Max Bandwidth); FAQ: 'Free tier includes 250MB data size and 500K commands per month.'; 'Max databases | 1'
  - [2] 2026-10-21: probe: POST (Idempotency-Key header) -> 200, credentials returned, 'Expires: 2026-10-24 (3 days from creation)'
  - withheld 2026-10-21: probe: SET of a 1,000,000-byte value -> {"result":"OK"}; GET -> 1,000,013 bytes returned; STRLEN -> 1000000; 9 MB and 10,000,000-byte SETs also OK; a 20 MB SET -> {"error":"ERR max request size exceeded. Limit: 10485760 bytes"}
  - withheld 2026-10-21: probe: INFO memory on the freshly minted free DB -> maxmemory:67108864 (64 MB), maxmemory_policy:noeviction — i.e. the anonymous/agent database is provisioned at 64 MB, well under the advertised 250 MB
  - withheld 2026-10-21: arithmetic: 500,000 commands/month / 30 = 16,667 commands/day; x 10 MB max request = 167 GB/day ceiling. At a realistic 1 KB per command it is 16.7 MB/day — 30,000x short of 500 GB/day.
- sources:
  - [1] https://upstash.com/pricing/redis
  - [2] https://upstash.com/start-redis

## Upstash Vector

- `storage/upstash-vector` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://upstash.com/vector
- free tier: 1 GB total data+metadata on Free; 10K daily queries; 200M vectors x dimensions | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free (bandwidth price $0 on Free), but 1 GB of stored data makes it moot. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB cap [1]
- limits note: 1 GB total; 10K queries/day (resets daily); 1 MB max per vector; 48 KB max metadata per vector; 1,536 max dimensions; 100 namespaces; 1 index
- interface detail: rest
- tooling: REST API, Python/TypeScript/Go SDKs; vectors are float arrays with up to 48 KB of metadata per vector, 1 MB max data per vector
- composes with: 1 GB per database, 100 namespaces per index and 1 index on Free. Namespaces share the 1 GB, so they do not multiply. 500 GB needs 500 free accounts.
- reliability: Stable managed service; queries are semantically searched rather than key-addressed, so it is a poor fit for blob retrieval anyway. You would use a 1-dimension vector as a pure key-value hack, which still hits the 1 GB cap.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB total data+metadata on Free; 10K daily queries; 200M vectors x dimensions
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: 'Max Total Data | 1 GB'; 'Daily query limit | 10K'; 'Max data per vector | 1 MB'; 'Max metadata per vector | 48 KB'; 'Max namespaces | 100'
- sources:
  - [1] https://upstash.com/pricing/vector

## upstash kafka

- `storage/upstash-kafka` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://upstash.com/blog/workflow-kafka
- free tier: none reachable: Discontinued. Deprecated 2024-09-11, shut down 2025-03-11. Do not plan around it; Upstash now points users at Workflow/QStash instead. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Discontinued. Deprecated 2024-09-11, shut down 2025-03-11. Do not plan around it; Upstash now points users at Workflow/QStash instead.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Discontinued. Deprecated 2024-09-11, shut down 2025-03-11. Do not plan around it; Upstash now points users at Workflow/QStash instead.
  - [2] 2026-10-21: cited as the basis of the rejection: Discontinued. Deprecated 2024-09-11, shut down 2025-03-11. Do not plan around it; Upstash now points users at Workflow/QStash instead.
- sources:
  - [1] https://upstash.com/blog/workflow-kafka
  - [2] https://community.fly.io/t/deprecation-notice-for-upstash-kafka/21775/1
