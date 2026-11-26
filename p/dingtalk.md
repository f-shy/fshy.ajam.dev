# DingTalk Drive

> dingtalk.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dingtalk/ | JSON https://fshy.ajam.dev/api/v1/entity/dingtalk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DingTalk Drive (DingTalk Docs / 钉盘)

- `storage/dingtalk-drive` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T04:14:20.835Z (live) | stale on 2026-12-10
- url https://www.dingtalk.io
- free tier: DingTalk grants every organization 100 GB of permanently free Drive capacity by default. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 8 GB max per upload | bytes: 8000000000 | source: [1] | note: 8 GB maximum per uploaded file; imported document files are capped at 20 MB.
- retention: 100 GB of permanently free Drive capacity per organization by default; 8 GB max per uploaded file | 8 GB per file (upload); 20 MB per file for 'import' to online docs; only pdf/office/zip/image/AV media preview - other binaries upload fine but get no preview; attachments inside online docs count toward quota since 2023-07-30 | source: [1] | note: 100 GB of Drive capacity is permanently free per organization; in-document attachments count toward that capacity since 2023-07-30. No file expiry period is stated.
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
- notes: 100 GB of permanently free Drive capacity per organization by default; 8 GB max per uploaded file
- evidence note: the storage-quota guide states the permanently free Drive capacity granted to every organization
- evidence:
  - [1] 2026-10-21: 'DingTalk grants every organization 100 GB of permanently free Drive capacity by default. If this is insufficient, the organization can purchase additional capacity.'
  - [1] 2026-10-21: 'maximum size of 8 GB per file' (upload), '20 MB per file' (import)
  - [2] 2026-10-21: probe: POST (via fetch proxy) -> HTTP 400 - API live, keyless reachable
  - [1] 2026-11-09: the storage-quota guide states every organization receives 100 GB of permanently free Drive capacity | capture: sha256:6e1b1561d414e2ff7e802c04bd2bcf5de77a1814725445d9f291d4b898c3cd9c | quote: DingTalk grants every organization 100 GB of permanently free Drive capacity by default.
  - [1] 2026-11-09: the guide caps an uploaded file at 8 GB and an imported document at 20 MB | capture: sha256:6e1b1561d414e2ff7e802c04bd2bcf5de77a1814725445d9f291d4b898c3cd9c | quote: Uploaded files support previews for multiple file types, with a maximum size of 8 GB per file. Import only supports document types, with a maximum size of 20 MB per file.
  - [1] 2026-11-25: The quota guide states the 8 GB upload and 20 MB import per-file ceilings. | capture: sha256:6e1b1561d414e2ff7e802c04bd2bcf5de77a1814725445d9f291d4b898c3cd9c | quote: Uploaded files support previews for multiple file types, with a maximum size of 8 GB per file. Import only supports document types, with a maximum size of 20 MB per file.
  - [1] 2026-11-25: Storage accounting for in-document attachments changed on 2023-07-30. | capture: sha256:6e1b1561d414e2ff7e802c04bd2bcf5de77a1814725445d9f291d4b898c3cd9c | quote: **Attachments (images, videos, files, etc.) within DingTalk online documents will officially count toward organization storage capacity starting July 30, 2023.
  - [1] 2026-11-25: The permanently free 100 GB per-organization grant is unchanged. | capture: sha256:6e1b1561d414e2ff7e802c04bd2bcf5de77a1814725445d9f291d4b898c3cd9c | quote: DingTalk grants every organization 100 GB of permanently free Drive capacity by default.
- sources:
  - [1] https://help.dingtalk.io/docs/admin-guide/storage-quota
  - [2] https://api.dingtalk.com/v1.0/oauth2/accessToken
