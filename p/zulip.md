# Zulip Cloud Free

> zulip.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zulip/ | JSON https://fshy.ajam.dev/api/v1/entity/zulip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zulip Cloud Free

- `storage/zulip-cloud-free` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zulip.com/plans/
- free tier: 5 GB total file storage per organization on Cloud Free. Not per user. Standard/Plus are 5 GB/25 GB per user. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered; files served from the realm's upload host. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 10 MB per file [1]
  - per-object-cap (binding): 1 GB per file [1]
- limits note: 10 MB per file on Free (1 GB per file only on paid plans); 10,000 messages of searchable history on Free; large uploads 'may fail to upload using this API endpoint due to network limitations'.
- interface detail: rest
- tooling: Zulip REST API `POST /api/v1/user_uploads` (multipart) and the returned `uri` fetches directly. Python client `zulip`, plus `zulip-terminal` for humans.
- composes with: Orgs are free and self-serve, but each org is a separate Zulip Cloud realm. The multiplier is N orgs x 5 GB, i.e. exactly the 'trivially repeatable at scale' case. Not unlimited.
- reliability: Stable, no expiry on attachments. The 5 GB org cap is a hard wall. Uploads start failing rather than degrading.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB total file storage per organization on Cloud Free — not per user. Standard/Plus are 5 GB/25 GB per user.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The Zulip Cloud Free plan includes a total of 5 GB of file storage. Each uploaded file can be up to 10 MB.'
  - [2] 2026-10-21: 'File storage up to 5 GB total' (Free); '5 GB per user' (Standard); '25 GB per user' (Plus)
- sources:
  - [1] https://zulip.com/help/share-and-upload-files
  - [2] https://zulip.com/plans/
