# Redis Cloud

> redis.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/redis/ | JSON https://fshy.ajam.dev/api/v1/entity/redis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Redis Cloud (free tier)

- `storage/redis-cloud` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://redis.io/pricing/

## redis cloud (redis.io)

- `storage/redis-cloud-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:53.246Z (inherited) | stale on 2026-11-14
- url https://redis.io/pricing/
- free tier: Free plan with no end date stated ('Always'): up to 30 MB in a single database on a shared cloud deployment, with a best-effort SLA and community support. | unit: MB | metered on: stored-bytes | read on: 2026-10-30 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
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
- sources:
  - [1] https://redis.io/pricing/
