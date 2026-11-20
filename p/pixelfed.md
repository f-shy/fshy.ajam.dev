# pixelfed.de

> pixelfed.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixelfed/ | JSON https://fshy.ajam.dev/api/v1/entity/pixelfed.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pixelfed.de — Pixelfed, 15 MB per object, unlimited per account

- `storage/pixelfed-de-pixelfed-15-mb-per-object-unlimited-per-acco` | fails-quota | evidence reported | binding per-object-cap | category fediverse-pixelfed
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:32.526Z (live) | stale on 2026-11-19
- url https://pixelfed.de
- free tier: Per-account unlimited (Pixelfed has no per-user storage counter). Per-file image_size_limit = video_size_limit = 15360000 bytes (14.6 MiB); 12 attachments per status; image_matrix_limit 2,073,600 px (1920x1080). | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file image_size_limit = video_size_limit = 15360000 bytes (about 14.65 MiB) | bytes: 15360000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, plain CDN path, no meter. | metered: no
- identity: email | detail: the registration form asks name, username, email, password and a box confirming the user is at least 16 years old; no phone or card field
- interface: rest
- limits:
  - per-object-cap (binding): Per-file image_size_limit = video_size_limit = 15360000 bytes (about 14.65 MiB) [1]
- limits note: Per-object-cap 14.6 MiB; per-account unlimited; supported MIME restricted to image/jpeg,png,gif,webp + video/mp4. No arbitrary blobs (PNG/JPEG wrapper needed).
- interface detail: rest
- tooling: Pixelfed is a Mastodon-API derivative: POST /api/v1/media (multipart) then POST /api/v1/statuses with media_ids[]. OAuth2 via /api/v1/apps. Any Mastodon client library mostly works.
- composes with: Per-object uploads are limited to 14.6 MiB and restricted to image and video formats (JPEG, PNG, GIF, WebP, MP4). Federation across open Pixelfed instances provides distribution across nodes, though single-file limits remain small.
- reliability: pixelfed.social itself returned HTTP 521 (origin down) throughout this probe; pixelfed.art also 521. The software is fine, the flagship host was not.
- notes: the same as the free tier
- evidence note: reported: the pages read on 2026-11-03 are https://pixelfed.de/api/v1/instance, which states registrations true with approval_required false, image_size_limit and video_size_limit of 15360000, the MIME types image/jpeg, image/png, image/gif, image/webp and video/mp4, and max_media_attachments 12, and https://pixelfed.de/register, which shows a form with an age-confirmation box. Neither page states a per-account storage quota, so the 'unlimited per account' value of free_tier.stated is not confirmed by them and the rung stays reported.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-account unlimited (Pixelfed has no per-user storage counter). Per-file image_size_limit = video_size_limit = 15360000 bytes (14.6 MiB); 12 attachments per status; image_matrix_limit 2,073,600 px (1920x1080).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: probe: GET -> 200, configuration.media_attachments.image_size_limit=15360000, video_size_limit=15360000, image_matrix_limit=2073600, statuses.max_media_attachments=12, registrations=true, version 3.5.3 (Pixelfed 0.15.1)
  - [2] 2026-10-21: probe: GET -> 521 (Cloudflare origin down); pixelfed.art -> 521
  - [1] 2026-11-03: image and video per-file limits are both 15360000 bytes | capture: sha256:14ad22a43be72916f3ac1b14b8677bc571da4ab4815a58a01076af512ba7afbc | quote: "image_size_limit":15360000,"supported_mime_types":["image/jpeg","image/png","image/gif","image/webp","video/mp4"],"video_frame_rate_limit":120,"video_matrix_limit":2073600,"video_size_limit":15360000
  - [3] 2026-11-03: the registration form carries a 16-years-old box after the name, username, email and password fields | capture: sha256:8cac50b5f8d0e4862ed0cb20ee61b741f1593f893bd6e7ea4b990d943a8fbea7 | quote: I am at least 16 years old
  - [1] 2026-11-03: registrations are open and need no approval | capture: sha256:14ad22a43be72916f3ac1b14b8677bc571da4ab4815a58a01076af512ba7afbc | quote: registrations":true,"approval_required":false,"contact_account"
  - [1] 2026-11-04: the instance JSON states the per-file image limit of 15360000 bytes | capture: sha256:11b7fd45263b79799ced3671a3867c9f6794640eb664c37d1199685b589981be | quote: "image_size_limit":15360000
- sources:
  - [1] https://pixelfed.de/api/v1/instance
  - [2] https://pixelfed.social/api/v1/instance
  - [3] https://pixelfed.de/register
