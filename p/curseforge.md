# CurseForge

> curseforge.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/curseforge/ | JSON https://fshy.ajam.dev/api/v1/entity/curseforge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CurseForge (Overwolf) author file hosting

- `storage/curseforge-author-file-hosting` | qualifies-with-caveat | evidence reported | binding write-gated | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.curseforge.com
- disagrees on verdict: `storage/curseforge-author-file-hosting` says qualifies-with-caveat, `storage/curseforge-author-upload-api` says fails-quota
- free tier: No published total quota and no published per-file number that could be verified on 2026-10-21 - the author docs, the ideas board and the support KB were all behind SSO or Cloudflare. What IS verifiable is the observed size distribution: live file listings show modpacks at 89.1, 101.6 and 468.1 MB, and a single mod file at 66.7 MB. The one hard number surfaced is a media cap of 2 MB for images ('Why is it only 2MB??' - author complaint, still open, 'Future consideration'), and a forum report of a 350 MB mod upload being rejected without an external-URL option. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: retention: indefinite for approved files; 'Files updates in order to increase visibility is not allowed' and files must carry a changelog | source: [1] | note: not stated
- egress: Free and CDN'd via CloudFront in front of S3: edge.forgecdn.net and mediafilez.forgecdn.net return 'X-Cache: Miss from cloudfront' and 'Server: AmazonS3'. No billing. Hotlink-protected - a guessed object path returns 403 from S3 rather than bytes, so URLs must come from the API. | metered: no
- identity: email
- interface: rest, sftp, rclone
- limits:
  - write-gated (binding): approved files [1]
  - write-gated (binding): review gate', not as bulk storage [1]
- limits note: per-object-cap: unverified on 2026-10-21; evidence points below 500 MB for mods (350 MB rejection reported, 468.1 MB modpack published, so the ceiling is game-dependent and enforced client-side per the August release notes: 'Added new client-side validation - preventing upload of large files on unsupported games'). retention: indefinite for approved files; 'Files updates in order to increase visibility is not allowed' and files must carry a changelog. request-rate: not published.
- interface detail: rest
- tooling: Official upload API with `X-API-TOKEN` and multipart `metadata` + `file` (third-party implementations exist, e.g. TeamDman/SuperFactoryManager and BreakBB/DisenchantBuddy shell out to it); `cfwidget` mirrors file metadata (id, filesize, uploaded_at) publicly. No SFTP, no rclone.
- composes with: Unlimited projects per author account, unlimited files per project, unlimited versions. The provider therefore polices project count and not only request rate.
- reliability: Reads are hotlink-gated (403 from S3 on constructed URLs) and the whole author surface is SSO-walled, so this is the least auditable of the game hosts. Moderation is active and rule-driven. Best treated as 'large-ish files with a review gate', not as bulk storage.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: file sizes 89.1 MB, 101.6 MB, 85.5 MB, 83.5 MB in the live listing
  - [3] 2026-10-21: 48.9/49.0/48.0 MB; a 51324367-byte file confirmed via api.cfwidget.com (id 4612979)
  - [4] 2026-10-21: 'Why is it only 2MB??' media cap, status 'Future consideration'
  - [5] 2026-10-21: Jan 2025: >350 MB mod rejected, no external-URL option offered
  - [6] 2026-10-21: 'Added new client-side validation - preventing upload of large files on unsupported games'
  - [7] 2026-10-21: 'It is not allowed to upload multiple similar and/or low effort projects in an attempt to game the system'. In plain terms, the policy puts a ceiling on project count rather than only on request rate.
  - [8] 2026-10-21: probe: GET ... -> 302 then 403 from AmazonS3 via cloudfront (hotlink protection live)
- sources:
  - [1] https://support.curseforge.com/en/support/solutions/articles/9000197241-file-size-limits
  - [2] https://www.curseforge.com/minecraft/modpacks/better-mc-forge-bmc4/files
  - [3] https://www.curseforge.com/minecraft/modpacks/rlcraft/files
  - [4] https://curseforge-ideas.overwolf.com/ideas/CF-I-8110
  - [5] https://nullforums.net/threads/unable-to-upload-mod-file-larger-than-350mb-no-url-link-provided.102087/
  - [6] https://blog.curseforge.com/platform-release-notes-august-26/
  - [7] https://support.curseforge.com/en/support/solutions/articles/9000197279-moderation-policies
  - [8] https://edge.forgecdn.net/files/5000/100/

## CurseForge (Overwolf) author upload API

- `storage/curseforge-author-upload-api` | fails-quota | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.curseforge.com
- disagrees on verdict: `storage/curseforge-author-file-hosting` says qualifies-with-caveat, `storage/curseforge-author-upload-api` says fails-quota
- free tier: No published per-file or total quota. Known caps: project media and gallery images limited to 2 MB. Mod file upload limit is not documented in public terms. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, Cloudflare-fronted (edge.forgecdn.net / mediafilez.forgecdn.net), no auth on downloads. | metered: no
- identity: email
- interface: rest, rclone
- limits note: Every project and every file goes through human moderation before release; media 2 MB; project metadata must be in English and must plausibly describe a mod. Upload limit per file is unverified.
- interface detail: rest
- tooling: Documented Upload API: POST /api/projects/{projectId}/upload-file with multipart `metadata` + `file`, X-Api-Token header; also Maven for some project types. Third-party wrapper: github.com/itsmeow/curseforge-upload. No rclone.
- composes with: Unlimited projects per author account (no documented cap) x unknown per-file size. If the effective cap resembles Modrinth's 500 MiB, 1000 projects = ~500 GB.
- reliability: Manual moderation queue means automated bulk uploads get rejected or the author account locked; releases can be delisted retroactively.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published per-file or total quota. Known caps: project media/gallery images limited to 2 MB (author complaint, Apr 2026).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'POST multipart/form-data request to /api/projects/{projectId}/upload-file'
  - [2] 2026-10-21: token generation + auth details
  - [3] 2026-10-21: 'Why is it only 2MB??' for media uploads, Apr 2026
  - [4] 2026-10-21: 'Improved the ability to upload bigger files to projects' (no number given)
- sources:
  - [1] https://support.curseforge.com/en/support/solutions/articles/9000197321-curseforge-upload-api
  - [2] https://wiki.nemonotfound.com/third-party/curseforge-upload-api
  - [3] https://curseforge-ideas.overwolf.com/ideas/CF-I-8110
  - [4] https://blog.curseforge.com/curseforge-platform-release-notes-march/
