# Redis

> redis.io | Storage, Databases and KV; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/redis/ | JSON https://fshy.ajam.dev/api/v1/entity/redis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Redis Cloud (free tier)

- `storage/redis-cloud` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.551Z (live) | stale on 2026-12-04
- url https://redis.io/cloud/
- free tier: 30 MB single database, free forever | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: until the instance is recycled; not persistent | source: [1] | note: not stated
- egress: Not metered on the free plan (bandwidth is bundled), but 30 MB of storage makes egress moot. | metered: yes
- identity: email
- interface: rest, cli
- limits note: 30 MB memory; single DB; no persistence guarantees on the free tier beyond snapshotting; eviction policy applies under memory pressure
- interface detail: rest
- tooling: redis-cli, any Redis client (redis-py, ioredis), RESP over TLS; RedisInsight GUI
- composes with: 30 MB x 1 DB. Creating multiple free databases is the only path, and Redis Cloud's free plan is one 30 MB DB per subscription. You would need ~17,000 free subscriptions for 500 GB. This is the weakest structured store on bytes.
- reliability: Redis Cloud free is a real managed instance and stable, but with 30 MB it is a cache, not storage. Data can be evicted under maxmemory pressure.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 30 MB single database, free forever
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free | Up to 30 MB | 30 MB single DB | From $0/hour'; Essentials from $0.007/hour; Pro from $0.014/hour
  - [1] 2026-11-19: Redis Cloud's live pricing page still states a free 30 MB single database | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: 30 MB single DB
- sources:
  - [1] https://redis.io/pricing/

## redis cloud (redis.io)

- `storage/redis-cloud-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:52.047Z (live) | stale on 2026-12-04
- url https://redis.io/pricing/
- free tier: Free plan with no end date stated ('Always'): up to 30 MB in a single database on a shared cloud deployment, with a best-effort SLA and community support. | unit: MB | metered on: stored-bytes | read on: 2026-10-30 | source: [1]
- per-object cap: stated-absent: the Redis Cloud pricing page states a 30 MB database size but no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the Redis Cloud pricing page states no retention period for stored data | source: [1]
- egress: Data transfer is included in the price, limited | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the Redis Cloud pricing page states a shared cloud deployment and a single Redis database but names no object/file storage interface
- tooling: not documented
- composes with: stated-absent: the Redis Cloud pricing page states no way to chain the offer with other storage services
- reliability: Free tier provides a single 30 MB database per account without account multiplication options.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: the Free plan is listed as Always, at no charge, up to 30 MB | capture: sha256:6eab673878eb7200c6af2dda101ff1616223ff240ac0772f0e50a7910bbb9347 | quote: Free Always $0 Up to 30 MB
  - [1] 2026-10-30: the Free plan is one database of 30 MB | capture: sha256:6eab673878eb7200c6af2dda101ff1616223ff240ac0772f0e50a7910bbb9347 | quote: 30 MB single DB
  - [1] 2026-11-19: the Free plan is still listed as Always at $0 and up to 30 MB | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: Up to 30 MB
  - [1] 2026-11-19: the Free plan is still one database of 30 MB | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: 30 MB single DB
  - [1] 2026-11-19: the Free plan is a shared cloud deployment | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: Shared cloud deployment
  - [1] 2026-11-19: the plan table states data transfer is included in the price but limited | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: Data transfer | Included in price, limited
- sources:
  - [1] https://redis.io/pricing/

## RedisLabs (Redis Cloud Free)

- `databases-kv/redislabs` | fails-quota | evidence documented | binding per-object-cap | category fully managed Redis and Redis Stack, free 30 MB Essentials plan on shared infrastructure | tier Free (30 MB Essentials)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T01:13:44.791Z (live) | stale on 2026-12-20
- url https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details/
- free tier: Free plan: Always $0, up to 30 MB, a 30 MB single database on a shared cloud deployment, best-effort SLA and community support. The 30 MB Essentials plan is free and is designed for learning and building test projects. | unit: MB | metered on: stored-bytes | read on: 2026-11-19 | source: [1] | note: Free plans are a type of Essentials plan, which gives an upgrade path to paid Essentials. Since Jan 2024 a new Essentials subscription supports only one database.
- per-object cap: 30 MB database size on the free plan; the database size includes replication where applicable | bytes: 31457280 | source: [2] | note: bytes is the decimal reading of 30 MB as the vendor states it; the size includes replication where applicable, so the usable dataset is smaller when replication is on.
- retention: no expiry or inactivity deletion clock is stated on the pages read; the free database persists while the account and subscription are kept | source: [2] | note: null is indefinite: the pages read state no automatic expiry for the free database.
- egress: Data transfer is included in the price but limited on the Free plan; the free 30 MB Essentials plan has a 5 GB monthly total network bandwidth limit applied to the whole plan. | metered: yes | free allowance: 5 GB monthly total network bandwidth on the 30 MB free plan | source: [2]
- identity: email | detail: Signup offers two options: enter your information in the form and select Get Started, or sign up with Google or Github. After entering your information you receive an activation email from Redis and select Activate account. No card is requested for the free database; a card is added only when a paid tier is chosen.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 30 MB database size, single database per Essentials subscription since Jan 2024 [3]
  - request-rate: Maximum throughput 100 ops/sec on the 30 MB free plan; 30 concurrent connections [2]
  - volume-quota: 5 GB monthly total network bandwidth on the free plan; 1 CIDR allow rule [2]
- binding note: the 30 MB single database is the hard ceiling that stops any workload first; the 100 ops/sec throughput and 5 GB transfer are generous relative to that 30 MB
- interface detail: the Redis protocol over TLS for clients; a REST API for subscription and database management
- tooling: redis-cli, Redis Insight, and Redis client libraries for .NET, node.js, Python, Java, Go and PHP
- composes with: a free Redis Cloud database can be added to a project through the Vercel Redis Cloud integration or the Heroku add-on, or reached directly from an application; the 30 MB and 100 ops/sec caps are the ceiling
- reliability: best-effort SLA and community support on the free plan; Redis notifies the user before limiting database usage when the bandwidth or throughput limits are exceeded
- notes: The free Redis Cloud plan is 30 MB with one database, 30 connections, 100 ops/sec and 5 GB of transfer. It clears identity (no card) and interface (a real Redis protocol with clients), but the 30 MB ceiling is a hard wall, so the verdict is fails-quota. This is the RedisLabs hosted service, not the Redis Software that a user installs and runs; self-hosted Redis is not the offer here.
- evidence note: four first-party Redis pages were captured and quoted on 2026-11-19: the pricing page, the Essentials plan details table, the quick start, and the RedisLabs support knowledge-base article. No probe was run; every figure is from a first-party page.
- evidence:
  - [1] 2026-11-19: the free plan is a 30 MB single database | capture: sha256:1e13e3ae0e35d5d553f367c6421e9e970a68d70f18c8c63ca74c69d1cf7708e7 | quote: 30 MB single DB
  - [2] 2026-11-19: the 30 MB plan is the free tier within Essentials | capture: sha256:2b9df66df5e1124f87facac621e536417e20f5d01fc35b1f0c104ed528147062 | quote: The 30 MB Essentials plan is free; it's designed for learning and building test projects.
  - [2] 2026-11-19: the free plan allows 30 concurrent connections per database | capture: sha256:2b9df66df5e1124f87facac621e536417e20f5d01fc35b1f0c104ed528147062 | quote: | Concurrent connections per database | 30 | 256 | 1024 | 2500 | 5000 | 10000 |
  - [2] 2026-11-19: the free plan has a 5 GB monthly total network bandwidth limit | capture: sha256:2b9df66df5e1124f87facac621e536417e20f5d01fc35b1f0c104ed528147062 | quote: | Monthly total network bandwidth[2] | 5 GB | 100 GB | 200 GB | 400 GB | 800 GB | 2000 GB |
  - [2] 2026-11-19: the free plan has a 100 ops/sec maximum throughput | capture: sha256:2b9df66df5e1124f87facac621e536417e20f5d01fc35b1f0c104ed528147062 | quote: | Maximum throughput[3] | 100 ops/sec | 1000 ops/sec | 2000 ops/sec | 4000 ops/sec | 8000 ops/sec | 16000 ops/sec |
  - [3] 2026-11-19: the RedisLabs support article states 30 MB memory and 30 connections on the free tier | capture: sha256:f2faaa03b1294786b6abd692f26760f461be3e6aaba915f7282fb93361d22720 | quote: - Free: 30MB memory, 30 connections
  - [3] 2026-11-19: only one database is allowed per Essentials subscription since Jan 2024 | capture: sha256:f2faaa03b1294786b6abd692f26760f461be3e6aaba915f7282fb93361d22720 | quote: As of Jan 2024, new Essentials subscriptions support only one database. Create a second subscription or upgrade to Pro to add more.
  - [4] 2026-11-19: the quick start states there are two signup options | capture: sha256:5749c727f76a7d9f58a7464dc02203156f4f4da62443d7232e185dcfd3dc6d8b | quote: There are two options available to get started with Redis Cloud:
  - [4] 2026-11-19: email verification is required to activate the account; no card is asked for the free path | capture: sha256:5749c727f76a7d9f58a7464dc02203156f4f4da62443d7232e185dcfd3dc6d8b | quote: After you enter your information, you should receive an activation email from Redis. Select Activate account to go to the Create your database page in the Redis Cloud console.
- sources:
  - [1] https://redis.io/pricing
  - [2] https://redis.io/docs/latest/operate/rc/subscriptions/view-essentials-subscription/essentials-plan-details/
  - [3] https://support.redislabs.com/hc/en-us/articles/27361653454098-Choosing-a-Subscription-and-Creating-Your-First-Database
  - [4] https://redis.io/docs/latest/operate/rc/rc-quickstart/
