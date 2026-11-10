# Prisma Postgres

> prisma.io | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prisma/ | JSON https://fshy.ajam.dev/api/v1/entity/prisma.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prisma Postgres

- `databases-kv/prisma-postgres` | qualifies-with-caveat | evidence documented | binding request-rate | category serverless Postgres with a compute layer
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://www.prisma.io/pricing
- price USD 8 per million operations; storage USD 2.00/GB beyond 10 GB on Starter
- free tier: 200,000 operations per month, 2 GB storage, 50 databases, 10 direct connections, and Prisma Compute with 1 million requests | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: 2 GB storage on Free; 10 connections direct and 10 pooled | source: [1]
- retention: a database persists while the plan is active; the Accelerate cache retires on 2026-12-01 | source: [1]
- egress: the database itself has no egress fee on any published plan; Prisma Compute includes 10 GB of outbound bandwidth a month and then USD 0.025 per GB | metered: yes | free allowance: no database egress fee; 10 GB per month on Prisma Compute | source: [1]
- identity: email | detail: email signup; no card on Free
- interface: rest, cli
- limits:
  - request-rate (binding): 200,000 operations per month; every query is one operation [1]
  - request-rate (binding): 10 direct connections and 10 pooled connections on Free [1]
  - per-object-cap: 2 GB storage [1]
- limits note: connection idle timeout is 60 minutes
- interface detail: the Postgres wire protocol; the Prisma ORM; a Management API
- tooling: the Prisma ORM, psql, any Postgres client
- composes with: 50 databases on one free account is the widest per-tenant fan-out in this class, if 10 connections per database is enough
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: 200,000 operations a month is 6,667 a day, which is a prototype and not a service. The 10-connection ceiling is the second wall and it is the one that shows up when a pooler is added and the pool itself is the limit.
- evidence note: the pricing page's plan table was read on 2026-10-22, and the 10-connection ceiling is on it beside the operation count and the storage allowance.
- evidence:
  - [1] 2026-10-22: Free: 200k operations, 2 GB storage, 50 databases, connection limit pooled 10, connection limit direct 10, connection idle timeout 60 minutes, data transfer unlimited; Prisma Compute Free 1M requests, 360 GB-hours provisioned memory, 4 vCPU-hours active CPU, 10 GB outbound bandwidth
- sources:
  - [1] https://www.prisma.io/pricing
