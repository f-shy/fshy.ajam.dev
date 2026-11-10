# notion

> notion.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/notion/ | JSON https://fshy.ajam.dev/api/v1/entity/notion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Notion (free plan) - file blocks & Files property

- `storage/notion-file-blocks-files-property` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.notion.com
- disagrees on identity_kind: `storage/notion` says email, `storage/notion-file-blocks-files-property` says institution
- disagrees on verdict: `storage/notion` says fails-quota, `storage/notion-file-blocks-files-property` says qualifies-with-caveat
- free tier: No total storage cap: 'Unlimited file uploads' on Free, but each file is capped at 5 MiB on Free (5 GiB on paid). Block limit is unlimited for a single-member Free workspace. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 MiB per file | bytes: 5242880 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; Notion serves via S3/presigned URLs on Cloudflare-fronted notion.com. File objects return 'An authenticated HTTP GET URL... valid for one hour', so links must be re-minted - no CDN you can pin a cache to without re-signing. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-ip-shaping: 1 TB/day [1]
  - per-object-cap (binding): 5 MiB per file [1]
- limits note: 5 MiB per file on Free (hard, enforced by API); 20 MiB per single-part API upload; parts must be 5-20 MiB; 600 requests/min per workspace (avg 10/s) shared across all connections; only whitelisted MIME types (audio/document/image/video/CAD) - arbitrary binary is rejected
- interface detail: rest
- tooling: Official Notion API file-upload endpoints (single-part <=20 MiB, multi-part above with 5-20 MiB parts) + PlakarKorp/integration-notion and many notion-backup repos for bulk extraction; no rclone backend
- composes with: Per-record unlimited: 5 MiB per file across unlimited files, blocks, and free workspaces. Sharding large datasets into 5 MiB objects requires approximately 200,000 objects per terabyte at the 600 requests per minute API rate limit.
- reliability: The MIME whitelist is the killer: no generic octet-stream blobs, so archival datasets must be packed as .zip/.7z/.tar which Notion does accept. Signed URLs expire in one hour, so serving 1 TB/day out of Notion means re-minting continuously.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Free workspaces are limited to 5 MiB (binary megabytes) per file'; 'Files larger than 20 MiB must be split into parts'; supported-types table lists .zip, .7z, .tar, .bz2, .rar
  - [2] 2026-10-21: 'Unlimited file uploads'; 'On the Free plan, you can upload images, videos and file attachments up to 5MB each. Upgrade to a paid plan for unlimited file uploads with a ~5GB max per file.'
  - [3] 2026-10-21: 'An authenticated HTTP GET URL to the file. The URL is valid for one hour.'
  - [4] 2026-10-21: probe: GET -> HTTP 401 (API live, auth-gated)
- sources:
  - [1] https://developers.notion.com/guides/data-apis/working-with-files-and-media
  - [2] https://www.notion.com/pricing
  - [3] https://developers.notion.com/reference/file-object
  - [4] https://api.notion.com/v1/users

## notion (free workspace as file store)

- `storage/notion` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.notion.com/guides/data-apis/working-with-files-and-media
- disagrees on identity_kind: `storage/notion` says email, `storage/notion-file-blocks-files-property` says institution
- disagrees on verdict: `storage/notion` says fails-quota, `storage/notion-file-blocks-files-property` says qualifies-with-caveat
- free tier: None reachable: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour. 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a…
  - [2] 2026-10-21: cited as the basis of the rejection: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o
  - [3] 2026-10-21: cited as the basis of the rejection: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o
- sources:
  - [1] https://developers.notion.com/guides/data-apis/working-with-files-and-media
  - [2] https://developers.notion.com/reference/file-object
  - [3] https://www.notion.com/help/understanding-block-usage
