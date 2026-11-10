# Modrinth

> modrinth.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modrinth/ | JSON https://fshy.ajam.dev/api/v1/entity/modrinth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modrinth

- `storage/modrinth` | qualifies-with-caveat | evidence reported | binding request-rate | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://modrinth.com
- free tier: 500 MiB per version file (hard code-level cap: `read_from_field(field, 500 * (1 << 20), "Project file exceeds the maximum of 500MiB...")`). No stated total-account storage quota. Per-user quotas read from `user_limits`: projects = 256, projects_per_day = 10, versions_per_project = 10000, versions_per_day = 150. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. All files served from cdn.modrinth.com behind Cloudflare with `Accept-Ranges: bytes`, no auth, no signed URLs, no expiry. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - request-rate (binding): 150 uploads/day [1]
- limits note: 500 MiB/version-file; 150 version uploads/day; 10,000 versions per project; 256 projects; version_number must be unique per project (1-32 chars); moderation may reject non-mod content; project file type must be in project_file_type allowlist (jar/zip/mrpack etc.), so arbitrary blobs need wrapping.
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: rest
- tooling: Documented public REST API v2 (api.modrinth.com/v2/project/{id}/version, POST /version with multipart file upload + PAT auth); labrinth OpenAPI spec published at docs.modrinth.com. No rclone backend, but the API is simple enough for a dozen-line client.
- composes with: 256 projects x 10,000 versions/project x 500 MiB = ~1.22 PiB theoretical per account; practically throttled by versions_per_day=150 -> 150 x 500 MiB = 73 GiB/day/account = ~2.2 TiB/month/account. Unlimited free accounts; each new account resets all four counters. Idle accounts keep all existing files downloadable forever (no TTL on published versions).
- reliability: Moderated registry: junk projects can be removed and files hard-deleted; no rate-limit survival guarantee past 150 uploads/day.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [1] 2026-10-21: '500 * (1 << 20)' hard file cap for project version files
  - [2] 2026-10-21: projects_per_day 10, versions_per_project 10000, versions_per_day 50 raised to 150 by 20260917120000_raise_versions_per_day_limit.sql
  - [3] 2026-10-21: default projects 256, organizations 16
  - withheld 2026-10-21: probe: GET api.modrinth.com/v2/version/g6ju16VJ -> 200, files[0].url = cdn.modrinth.com/data/AANobbMI/versions/g6ju16VJ/...jar, size 1912496
  - withheld 2026-10-21: probe: GET cdn.modrinth.com/...jar with Range: bytes=0-0 -> 206 Partial Content, Content-Range bytes 0-0/1912496, Accept-Ranges: bytes, Server: cloudflare
- sources:
  - [1] https://raw.githubusercontent.com/modrinth/code/main/apps/labrinth/src/routes/v3/version_creation.rs
  - [2] https://raw.githubusercontent.com/modrinth/code/main/apps/labrinth/migrations/20260916120000_version_limits.sql
  - [3] https://raw.githubusercontent.com/modrinth/code/main/apps/labrinth/migrations/20250927120742_user_limits.sql
