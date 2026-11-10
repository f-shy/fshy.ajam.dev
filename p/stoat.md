# Stoat

> stoat.chat | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stoat/ | JSON https://fshy.ajam.dev/api/v1/entity/stoat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stoat (formerly Revolt) — official instance

- `storage/stoat-official-instance` | qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://stoat.chat
- disagrees on verdict: `storage/stoat-autumn-file-service` says fails-quota, `storage/stoat-official-instance` says qualifies-with-caveat
- free tier: 20,000,000 bytes (20 MB) per attachment as the server-enforced default, no paid tier to raise it, and no documented total storage cap. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: | Critically different from Discord: attachment URLs are UNSIGNED and permanent | source: [1] | note: not stated
- egress: Free and unmetered via cdn.stoatusercontent.com on Cloudflare. CDN responses specify `Cache-Control: public, max-age=2073600`, providing 24 days of edge caching. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 20 MB per file [1]
- limits note: 20 MB per file; 5 attachments per message; body_limit_size 20,000,000 bytes globally. Live limits object also gives: emojis 500 KB, icons 2.5 MB, banners/backgrounds 6 MB, avatars 4 MB. Those are separate, smaller buckets.
- interface detail: rest
- tooling: Autumn file service: `POST {autumn}/attachments` with multipart `file` and `X-Bot-Token`/`X-Session-Token`. Documented at stoatchat/stoatchat `docs/docs/developers/api/uploading-files.md`. Bots are first-class; 5 bots per account.
- composes with: 100 servers per account x 200 channels per server (from the live `/` limits object) = 20,000 channels, each with unlimited messages. Servers are capped at 100 for existing accounts / 50 for new ones.
- reliability: Critically different from Discord: attachment URLs are UNSIGNED and permanent. The platform renamed Revolt->Stoat in Oct 2025 and moved the CDN (autumn.revolt.chat -> cdn.revoltusercontent.com) in May 2025 with 301s still in place; old IDs from the pre-refactor Autumn do 404.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: probe: GET -> features.limits.default.file_upload_size_limits.attachments = 20000000 (20 MB), server_channels = 200, servers = 100, message_attachments = 5
  - [2] 2026-10-21: probe: GET -> 200 OK, Content-Length 10886, Cache-Control: public, max-age=2073600 — no ex/is/hm, no expiry
  - [3] 2026-10-21: probe: POST with no auth -> 401 (upload requires a token; read does not)
  - [4] 2026-10-21: 'Custom emojis, a 20MB file upload limit and a server-specific profile picture with no subscription required.'
- sources:
  - [1] https://api.stoat.chat/
  - [2] https://cdn.stoatusercontent.com/attachments/f749zVPTYPo_id3VY9IwZYMY83hgm9WV61MqWUV54D/image.png
  - [3] https://cdn.stoatusercontent.com/attachments
  - [4] https://stoat.chat/

## revolt/stoat public instance as bulk storage

- `storage/revolt-stoat-public-instance-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://stoat.chat/
- free tier: none reachable: 20 MB per file with no paid tier and no public way to raise it, and the public instance runs signup human-verification step. 1 TiB = 52,000 files. Only self-hosting removes the cap, which is no longer free | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 20 MB per file with no paid tier and no public way to raise it, and the public instance runs signup human-verification step. 1 TiB = 52,000 files. Only self-hosting removes the cap, which is no longer free
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 20 MB per file with no paid tier and no public way to raise it, and the public instance runs signup human-verification step. 1 TiB = 52,000 files. Only self-hosting removes the cap, which is no longer free
  - [2] 2026-10-21: cited as the basis of the rejection: 20 MB per file with no paid tier and no public way to raise it, and the public instance runs signup human-verification step. 1 TiB = 52,000 files. Only self-hosting removes the cap, which is no longer free
- sources:
  - [1] https://stoat.chat/
  - [2] https://github.com/revoltchat/self-hosted/issues/53

## Stoat (formerly Revolt) + Autumn file service

- `storage/stoat-autumn-file-service` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://stoat.chat/
- disagrees on verdict: `storage/stoat-autumn-file-service` says fails-quota, `storage/stoat-official-instance` says qualifies-with-caveat
- free tier: 20 MB per file, no subscription: 'Custom emojis, a 20MB file upload limit and a server-specific profile picture with no subscription required.' No published total-storage cap and no paid tier that raises the file size. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and. Importantly. UNSIGNED. Autumn 301s to cdn.stoatusercontent.com and the object URL is a bare path with no expiry parameters, unlike Discord. So a stored URL stays valid and is trivially Cloudflare-cacheable. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 20 MB per file [1]
- limits note: 20 MB per file is fixed and low; there is no path to a bigger unit. Upload limits are server-configurable only on SELF-hosted instances ('Upload limits are controlled via the Autumn config'), so on the public instance you are stuck at 20 MB.
- interface detail: rest
- tooling: Genuinely open: 'Our public API is so powerful that we use it ourselves for the official apps', API root answers live (GET https://api.revolt.chat/ -> {"stoat":"0.16.2","revolt":"0.16.2", features...}). Backend is open source (revoltchat/autumn, stoatchat/*). Self-hostable, which is both the appeal and the caveat.
- composes with: Unlimited servers x unlimited channels with a 20 MB cap, so 1 TB needs ~52,000 uploads. With no signed URLs, the reads are the easy part; the writes are the bottleneck.
- reliability: Smaller operator, recent rebrand to Stoat, and the public instance runs human-verification step on signup. Data longevity is a real question for a 20 TiB cold archive; treat as experimental.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 MB per file, no subscription: 'Custom emojis, a 20MB file upload limit and a server-specific profile picture with no subscription required.' No published total-storage cap and no paid tier that raises the file size.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Custom emojis, a 20MB file upload limit and a server-specific profile picture with no subscription required'
  - [2] 2026-10-21: probe: curl -D - -> 301 location: https://cdn.stoatusercontent.com/attachments/abc123 (no signature, no expiry params)
  - [3] 2026-10-21: probe: curl -> 200, {"stoat":"0.16.2",...} — public API live
- sources:
  - [1] https://stoat.chat/
  - [2] https://autumn.revolt.chat/attachments/abc123
  - [3] https://api.revolt.chat/
