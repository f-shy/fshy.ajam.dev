# Roblox Open

> roblox.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roblox/ | JSON https://fshy.ajam.dev/api/v1/entity/roblox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Roblox Open Cloud Assets

- `storage/roblox-open-cloud-assets` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:30.560Z (live) | stale on 2026-11-25
- url https://create.roblox.com/docs/cloud/guides/usage-assets
- free tier: For each call, you can only create or update one asset with the file size up to 20 MB | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB/asset | bytes: 20000000 | source: [1] | note: not stated
- retention: 20 MB/asset for models, images, decals, animation; video 3.75 GB but capped at 20/day and 5 min; audio hard-capped monthly; all uploads land in moderation; assets are permanently tied to a creator account. | source: [1] | note: not stated
- egress: Free. Asset delivery is served by Roblox's own CDN (assetdelivery.roblox.com / rbxcdn), never metered to the uploader. | metered: no
- identity: anonymous
- interface: rest, rclone
- limits:
  - request-rate: 100 uploads/month [1]
  - per-object-cap (binding): 20 MB/asset [1]
- limits note: 20 MB/asset for models, images, decals, animation; video 3.75 GB but capped at 20/day and 5 min; audio hard-capped monthly; all uploads land in moderation; assets are permanently tied to a creator account.
- interface detail: rest
- tooling: Documented Open Cloud REST: POST https://apis.roblox.com/assets/v1/assets (multipart, x-api-key header), plus asset delivery API. API keys scoped to a user or group; no rclone.
- composes with: 20 videos/day x 3.75 GB = 75 GB/day per ID-verified account = ~2.2 TB/month; unlimited accounts (each needing ID verification) and unlimited assets per account since there is no total quota. Non-video types: 20 MB x unlimited assets x 100-upload monthly audio cap.
- reliability: Moderation removes assets silently and irreversibly; read-back needs an authenticated assetdelivery call (anonymous GET -> 401), so it is not a public cacheable fetch path.
- notes: Per-asset caps only, no aggregate quota: 20 MB for most asset types; Video up to 3.75 GB each, up to 20 video uploads/day for ID-verified 13+ accounts (5 min duration, 4096x2160 max). Audio: 100 uploads/month if ID-verified, 10/month if not.
- evidence note: the Open Cloud usage-assets guide states a 20 MB per-asset file-size limit
- evidence:
  - [1] 2026-10-21: limits table: 'file size up to 20 MB', Video 'Up to 3.75 GB', 'Up to 20 uploads per day if you're 13+ and ID-verified', Audio 'Up to 100 uploads per month if you're ID-verified'
  - withheld 2026-10-21: probe: GET assetdelivery.roblox.com/v1/asset?id=10334973820 -> 401 Unauthorized
  - withheld 2026-10-21: probe: GET apis.roblox.com/assets/v1/assets/10334973820 -> 403 Forbidden
  - [1] 2026-11-09: the usage guide states a 20 MB file-size limit per asset call | capture: sha256:4baa7ebb68ce120324fc96eecb33b769c3a99696fb0c5e52be4d6b9e499f7911 | quote: For each call, you can only create or update one asset with the file size up to 20 MB
  - [1] 2026-11-09: the limits table caps audio uploads at 100 per month for ID-verified accounts | capture: sha256:4baa7ebb68ce120324fc96eecb33b769c3a99696fb0c5e52be4d6b9e499f7911 | quote: Up to 100 uploads per month if you're ID-verified.
- sources:
  - [1] https://create.roblox.com/docs/en-us/cloud/guides/usage-assets.md

## roblox open cloud assets api

- `storage/roblox-open-cloud-assets-api` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:39.275Z (live) | stale on 2026-12-04
- url https://create.roblox.com/docs/cloud/guides/usage-assets
- free tier: None reachable: 20 MB per asset; audio allows up to 100 uploads/month when ID-verified and 10 total uploads/month otherwise, video up to 20 uploads/day when 13+ and ID-verified. Asset delivery requires auth. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: the same as the free tier
- notes: the same as the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: 20 MB per asset, and the asset types that matter are throttled monthly: audio 10 total uploads/month without ID verification (100 with), video 20/day. Asset delivery requires auth…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 20 MB per asset, and the asset types that matter are throttled monthly: audio 10 total uploads/month without ID verification (100 with), video 20/day. Asset delivery requires auth…
  - [2] 2026-10-21: cited as the basis of the rejection: 20 MB per asset, and the asset types that matter are throttled monthly: audio 10 total uploads/month without ID verification (100 with), video 20/day. Asset delivery requires auth — anonymou
  - [1] 2026-11-19: a single asset upload is capped at 20 MB | capture: sha256:39e34a95ddf2411b677c9103534c4c53e0040a7d503d2c36ae2ca7584488238b | quote: For each call, you can only create or update one asset with the file size up to 20 MB with the following limits:
  - [1] 2026-11-19: audio uploads are throttled monthly and the allowance grows with ID verification | capture: sha256:39e34a95ddf2411b677c9103534c4c53e0040a7d503d2c36ae2ca7584488238b | quote: Up to 100 uploads per month if you're ID-verified.Up to 10 total uploads per month if you aren't ID-verified.
  - [1] 2026-11-19: video uploads are limited to 20 per day for ID-verified users aged 13+ | capture: sha256:39e34a95ddf2411b677c9103534c4c53e0040a7d503d2c36ae2ca7584488238b | quote: Up to 20 uploads per day if you're 13+ and ID-verified.
- sources:
  - [1] https://create.roblox.com/docs/cloud/guides/usage-assets
  - [2] https://assetdelivery.roblox.com/v1/asset/?id=1818
