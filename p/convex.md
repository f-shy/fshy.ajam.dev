# Convex

> convex.dev | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/convex/ | JSON https://fshy.ajam.dev/api/v1/entity/convex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Convex

- `storage/convex` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:09.483Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the free file storage allowance is still 1 GB total per team | capture: sha256:4e72369254f43fe541522f2fb5dd8ea78886325ef4e6bd2cd0202b405e28a101 | quote: Free: 1 GB total<br />Starter: 1 GB included;<br />$0.033/month per additional GB
  - [1] 2026-11-19: the free monthly data egress allowance is still 1 GB | capture: sha256:4e72369254f43fe541522f2fb5dd8ea78886325ef4e6bd2cd0202b405e28a101 | quote: Data egress | Free: 1 GB/month total
  - [2] 2026-11-19: file URLs remain public bearer URLs accessible without app-level authorization | capture: sha256:ac4409cde04db029bcd892d5f56b5b52f2ab71f4f7ddd42c3b1ca970de390412 | quote: anyone with the URL can access the file without another app-level authorization check
- sources:
  - [1] https://docs.convex.dev/production/state/limits
  - [2] https://docs.convex.dev/file-storage/overview
