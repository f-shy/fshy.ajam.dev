# Convex

> convex.dev | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/convex/ | JSON https://fshy.ajam.dev/api/v1/entity/convex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Convex

- `storage/convex` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.convex.dev
- free tier: 1 GB file storage on Free; 1 GB/month file egress; 0.5 GB database; 40 deployments | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 1 GB/month data egress total on Free (serving user files, accessing files in functions, backups). Equal to the storage size, so a full store can be fetched exactly once per month. | metered: no | free allowance: 1 GB per month
- identity: email
- interface: rest, cli
- limits note: 1 GB storage AND 1 GB egress; HTTP action responses capped at 100 MiB so you cannot proxy large files; file URLs are unrevocable except by deleting the file.
- interface detail: rest
- tooling: Convex client SDKs (JS/Python/Rust), HTTP actions, `npx convex` CLI, `storage.getUrl()` bearer URLs. 'anyone with the URL can access the file' (public, no auth).
- composes with: Free/Starter is per TEAM; 40 deployments per team on Free. But file storage is 1 GB total per team, not per deployment. So deployments do not multiply storage. Multiple teams/accounts is the only axis. Upload URLs are one-time and short-lived, which makes external tools awkward.
- reliability: Free has hard resource caps (Starter can exceed with usage-based billing). Well-behaved, no data loss reported; 100 MiB response cap breaks large-file serving via custom routes.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 1 GB file storage on Free; 1 GB/month file egress; 0.5 GB database; 40 deployments
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'File Storage | Storage: Free: 1 GB total', 'Data egress: Free: 1 GB/month total'
  - [1] 2026-10-21: 'Deployments | 40' on Free/Starter (per team)
  - [2] 2026-10-21: 'anyone with the URL can access the file without another app-level authorization check'
- sources:
  - [1] https://docs.convex.dev/production/state/limits
  - [2] https://docs.convex.dev/file-storage/overview
