# Appwrite Cloud

> appwrite.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appwrite/ | JSON https://fshy.ajam.dev/api/v1/entity/appwrite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Appwrite Cloud

- `storage/appwrite-cloud` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://appwrite.io
- free tier: 2 GB storage + 5 GB bandwidth on Free; 2 projects | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 5 GB bandwidth/month on Free. 2.5x the storage, so it is a real wall but not as lopsided as Supabase. | metered: no
- identity: email
- interface: s3-compatible, rest, graphql, cli
- limits note: 1 bucket per project on Free; 1 member; 750K executions; free projects paused after 1 week inactivity; 2-project cap.
- interface detail: rest
- tooling: Appwrite SDKs (web, flutter, node, python, dart), REST + GraphQL API, `appwrite` CLI; storage buckets expose file preview/download endpoints; S3-compatible adapter exists for self-host
- composes with: 2 projects x 2 GB = 4 GB per account; per-project caps on buckets ('1 Database, 1 Bucket, 2 Functions per project') mean a bucket cannot be sharded inside a project. Accounts are the only multiplier. Self-hosting is free and unlimited but that is paid compute, not a free tier.
- reliability: Same inactivity-pause pattern as Supabase/Nhost (1 week). Project limit of 2 is enforced per account.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 2 GB storage + 5 GB bandwidth on Free; 2 projects
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
- sources:
  - [1] https://appwrite.io/pricing
