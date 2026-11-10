# Nhost

> nhost.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nhost/ | JSON https://fshy.ajam.dev/api/v1/entity/nhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nhost

- `storage/nhost` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nhost.io
- free tier: 1 GB storage + 1 GB database on Starter (free); 1 project | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 5 GB egress/month included on Starter. | metered: no
- identity: email
- interface: s3-compatible, rest, graphql, cli
- limits note: 1 project, project paused after 1 week inactivity; 1 GB storage + 1 GB database share the same small envelope.
- interface detail: rest
- tooling: Hasura GraphQL + PostgREST-style REST, Nhost SDKs, `nhost` CLI, S3-compatible storage (MinIO) with presigned URLs
- composes with: 1 project x 1 GB. No multiplication: project limit is explicitly 1 on Starter. Effectively a single 1 GB bucket.
- reliability: Paused after 1 week idle; project count hard-capped at 1.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB storage + 1 GB database on Starter (free); 1 project
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Limit of 1 project. Project paused after 1 week of inactivity. | 1 GB database | 1 GB storage | 5 GB egress'
- sources:
  - [1] https://nhost.io/pricing
