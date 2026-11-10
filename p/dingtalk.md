# DingTalk Drive

> dingtalk.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dingtalk/ | JSON https://fshy.ajam.dev/api/v1/entity/dingtalk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DingTalk Drive (DingTalk Docs / 钉盘)

- `storage/dingtalk-drive` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.dingtalk.io
- free tier: 100 GB of permanently free Drive capacity per organization by default; 8 GB max per uploaded file | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 8 GB max per upload | bytes: 8000000000 | source: [1] | note: not stated
- retention: 100 GB of permanently free Drive capacity per organization by default; 8 GB max per uploaded file | 8 GB per file (upload); 20 MB per file for 'import' to online docs; only pdf/office/zip/image/AV media preview - other binaries upload fine but get no preview; attachments inside online docs count toward quota since 2023-07-30 | source: [1] | note: not stated
- egress: No egress line item; files are served from DingTalk's own CDN/OSS, share links only | metered: no
- identity: email
- interface: rest, cli
- limits:
  - per-object-cap (binding): 8 GB per file [1]
  - per-object-cap (binding): 20 MB per file [1]
  - write-gated: review - other binaries upload fine but get no preview [1]
- limits note: 8 GB per file (upload); 20 MB per file for 'import' to online docs; only pdf/office/zip/image/AV media preview - other binaries upload fine but get no preview; attachments inside online docs count toward quota since 2023-07-30
- interface detail: rest
- tooling: Official OpenAPI (api.dingtalk.com, media upload + drive) plus the first-party CLI DingTalk-Real-AI/dingtalk-workspace-cli (3,766 stars, pushed 2026-10-21) exposing `dws drive upload|download|list|stats`
- composes with: 100 GB x N free organizations. The grant is per organization, not per account, so N orgs is linear; also supports org-internal knowledge bases so a single org can be subdivided without extra accounts.
- reliability: Quota accounting changed in 2023 to count in-document attachments, so a previously-fine account can silently blow its 100 GB; CLI is brand new (same-day commits) and unversioned.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'DingTalk grants every organization 100 GB of permanently free Drive capacity by default. If this is insufficient, the organization can purchase additional capacity.'
  - [1] 2026-10-21: 'maximum size of 8 GB per file' (upload), '20 MB per file' (import)
  - [2] 2026-10-21: probe: POST (via fetch proxy) -> HTTP 400 - API live, keyless reachable
- sources:
  - [1] https://help.dingtalk.io/docs/admin-guide/storage-quota
  - [2] https://api.dingtalk.com/v1.0/oauth2/accessToken
