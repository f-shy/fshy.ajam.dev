# notion

> notion.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/notion/ | JSON https://fshy.ajam.dev/api/v1/entity/notion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Notion (free plan) - file blocks & Files property

- `storage/notion-file-blocks-files-property` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:27.598Z (live) | stale on 2026-11-25
- url https://www.notion.com
- disagrees on verdict: `storage/notion` says fails-quota, `storage/notion-file-blocks-files-property` says qualifies-with-caveat
- free tier: Free workspaces are limited to 5 MiB (binary megabytes) per file. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 MiB per file | bytes: 5242880 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; Notion serves via S3/presigned URLs on Cloudflare-fronted notion.com. File objects return 'An authenticated HTTP GET URL... valid for one hour', so links must be re-minted - no CDN you can pin a cache to without re-signing. | metered: no
- identity: email | detail: Sign up with your work email
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
- evidence note: the guide states the Free per-file limit and the API example gives the byte count
- evidence:
  - [1] 2026-10-21: 'Free workspaces are limited to 5 MiB (binary megabytes) per file'; 'Files larger than 20 MiB must be split into parts'; supported-types table lists .zip, .7z, .tar, .bz2, .rar
  - [2] 2026-10-21: 'Unlimited file uploads'; 'On the Free plan, you can upload images, videos and file attachments up to 5MB each. Upgrade to a paid plan for unlimited file uploads with a ~5GB max per file.'
  - [3] 2026-10-21: 'An authenticated HTTP GET URL to the file. The URL is valid for one hour.'
  - [4] 2026-10-21: probe: GET -> HTTP 401 (API live, auth-gated)
  - [1] 2026-11-09: a Free workspace file is capped at 5 MiB | capture: sha256:8fc159ffc3217c25730d204f1bacae95435f5f3a998427e96ab35554472d3fed | quote: Free workspaces are limited to 5 MiB (binary megabytes) per file
  - [5] 2026-11-09: the sign-up page asks for a work email address | capture: sha256:8b172a5e0ce4097a72108a106fce33e9a54c88ad9f9b2976472f335c4d423027 | quote: Sign up with your work email
  - [1] 2026-11-09: the API example gives 5242880 bytes for a free workspace | capture: sha256:8fc159ffc3217c25730d204f1bacae95435f5f3a998427e96ab35554472d3fed | quote: "max_file_upload_size_in_bytes": 5242880
- sources:
  - [1] https://developers.notion.com/guides/data-apis/working-with-files-and-media
  - [2] https://www.notion.com/pricing
  - [3] https://developers.notion.com/reference/file-object
  - [4] https://api.notion.com/v1/users
  - [5] https://www.notion.com/signup

## notion (free workspace as file store)

- `storage/notion` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:54.751Z (live) | stale on 2026-12-04
- url https://developers.notion.com/guides/data-apis/working-with-files-and-media
- disagrees on verdict: `storage/notion` says fails-quota, `storage/notion-file-blocks-files-property` says qualifies-with-caveat
- free tier: None reachable: 'Free workspaces are limited to 5 MiB (binary megabytes) per file' on the Free plan. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour. 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a…
  - [2] 2026-10-21: cited as the basis of the rejection: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o
  - [3] 2026-10-21: cited as the basis of the rejection: 5 MiB per file on Free (API and UI), and every Notion-hosted file URL is a signed S3 URL valid for one hour — 'Don't cache or statically reference these URLs'. Unlimited blocks on a single-o
  - [1] 2026-11-19: the Free plan caps files at 5 MiB | capture: sha256:8fc159ffc3217c25730d204f1bacae95435f5f3a998427e96ab35554472d3fed | quote: Free workspaces are limited to 5 MiB (binary megabytes) per file
  - [1] 2026-11-19: the 5 MiB Free cap is the published limit | capture: sha256:8fc159ffc3217c25730d204f1bacae95435f5f3a998427e96ab35554472d3fed | quote: Paid workspaces are limited to 5 GiB per file.
  - [2] 2026-11-19: Notion-hosted file URLs are signed and expire after one hour | capture: sha256:b822c6af477c1fa7858f3fc479d4cc24b0fc0bd4b3082f95540e9c1c2009738a | quote: Each time you fetch a Notion-hosted file, it includes a temporary public url valid for 1 hour.
- sources:
  - [1] https://developers.notion.com/guides/data-apis/working-with-files-and-media
  - [2] https://developers.notion.com/reference/file-object
  - [3] https://www.notion.com/help/understanding-block-usage
