# infosec.exchange

> infosec.exchange | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infosec/ | JSON https://fshy.ajam.dev/api/v1/entity/infosec.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## infosec.exchange — Mastodon with a 1.35 GiB per-file upload limit

- `storage/infosec-exchange-mastodon-with-a-1-35-gib-per-file-uploa` | fails-quota | evidence reported | binding per-object-cap | category fediverse-mastodon
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://infosec.exchange
- free tier: Per-account storage is UNLIMITED (stock Mastodon has no per-user media quota at all. Media_attachment has only a per-file size validator, no account-level counter). Per FILE: image_size_limit = video_size_limit = 1419430400 bytes = 1.32 GiB. That is a 84x relaxation of Mastodon's compiled defaults (IMAGE_LIMIT 16 MB / VIDEO_LIMIT 99 MB). | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per FILE: image_size_limit = video_size_limit = 1419430400 bytes = 1.32 GiB | bytes: 1417339207 | source: [1] | note: not stated
- retention: infosec.exchange is one of the largest and best-funded Mastodon instances (Glitch fork 4.8.0-alpha.3) and explicitly runs a relaxed upload policy; still a single volunteer operator, and a 1.3 GiB upload is exactly the kind of thing that gets noticed. Media is permanent by Mastodon semantics (no TTL, no GC), which cuts both ways. | source: [1] | note: not stated
- egress: Free. No egress meter on the instance; media sits behind the instance CDN (often S3/Wasabi/B2-compatible behind a CNAME). | metered: no
- identity: institution
- interface: rest, rclone, cli
- limits:
  - per-ip-shaping: 1.9 TB/day [1]
  - per-object-cap (binding): Per FILE: image_size_limit = video_size_limit = 1419430400 bytes = 1.32 GiB [1]
- limits note: Request-rate is THE binding limit, and it is severe: stock Mastodon rack_attack ships `throttle('throttle_api_media', limit: 30, period: 30.minutes)` per authenticated user. 30 media uploads per half hour = 1,440/day. At 1.32 GiB each that is a theoretical 1.9 TB/day/account, so realistically you hit GB-scale throughput only by running many accounts in parallel. Also: 8 media per status (MAX_MEDIA_ATTACHMENTS), 4 statuses/30 min soft on some instances, MAX_VIDEO_FRAMES 36,000 (≈5 min at 120 fps) and MAX_VIDEO_MATRIX_LIMIT 8,294,400 px cap video dimensions, and non-image/video MIME types are rejected by the upload validator.
- interface detail: rest
- tooling: Mastodon REST API v1: POST /api/v1/media (multipart `file` -> returns media id + `url`), then POST /api/v1/statuses with media_ids[] to make it permanent. OAuth2 app registration via POST /api/v1/apps (no manual approval on most instances). Any of the many existing clients work; `toot` CLI, `Mastodon.py`. Upload-from-URL: POST /api/v2/media with `url` param. rclone has no Mastodon backend but the API is 3 calls.
- composes with: The key structural fact: NO per-account quota means the ceiling is the instance's disk, and the operator absorbs it. Combined with a 1.32 GiB per-file cap and 8 attachments per status, one status carries 10.6 GiB in a single API call chain. Multiple accounts on the same instance each get the same unlimited-account treatment. Multiply over instances for isolation.
- reliability: infosec.exchange is one of the largest and best-funded Mastodon instances (Glitch fork 4.8.0-alpha.3) and explicitly runs a relaxed upload policy; still a single volunteer operator, and a 1.3 GiB upload is exactly the kind of thing that gets noticed. Media is permanent by Mastodon semantics (no TTL, no GC), which cuts both ways.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-account storage is UNLIMITED (stock Mastodon has no per-user media quota at all — media_attachment has only a per-file size validator, no account-level counter). Per FILE: image_size_limit = video_size_limit = 1419430400 bytes = 1.32 GiB. That is a 84x relaxation of Mastodon's compiled defaults (IMAGE_LIMIT 16 MB / VIDEO_LIMIT 99 MB).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: GET -> 200, configuration.media_attachments.image_size_limit=1419430400, video_size_limit=1419430400, registrations.enabled=true
  - [2] 2026-10-21: probe: GET -> 200, max_toot_chars=11000, registrations=true
  - [3] 2026-10-21: `IMAGE_LIMIT = 16.megabytes`, `VIDEO_LIMIT = 99.megabytes`, `validates_attachment_size :file, less_than: ...` — confirms the cap is a per-file validator with NO per-account quota anywhere in the model
  - [4] 2026-10-21: `throttle('throttle_api_media', limit: 30, period: 30.minutes) { |req| req.authenticated_user_id if req.post? && req.path.match?(%r{\A/api/v\d+/media\z}i) }`
- sources:
  - [1] https://infosec.exchange/api/v2/instance
  - [2] https://infosec.exchange/api/v1/instance
  - [3] https://raw.githubusercontent.com/mastodon/mastodon/main/app/models/media_attachment.rb
  - [4] https://raw.githubusercontent.com/mastodon/mastodon/main/config/initializers/rack_attack.rb
