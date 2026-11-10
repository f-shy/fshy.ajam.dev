# WhatsApp Cloud

> facebook.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/facebook/ | JSON https://fshy.ajam.dev/api/v1/entity/facebook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## whatsapp cloud api media as archive

- `storage/whatsapp-cloud-api-media-as-archive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media
- free tier: none reachable: 30-day hard deletion plus 5-minute media URLs; the bytes are unrecoverable on day 31. Any 'WhatsApp as free storage' claim found in the wild is wrong about this. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 30-day hard deletion plus 5-minute media URLs; the bytes are unrecoverable on day 31. Any 'WhatsApp as free storage' claim found in the wild is wrong about this.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 30-day hard deletion plus 5-minute media URLs; the bytes are unrecoverable on day 31. Any 'WhatsApp as free storage' claim found in the wild is wrong about this.
- sources:
  - [1] https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media

## WhatsApp Cloud API — Media (upload / media_id)

- `storage/whatsapp-cloud-api-media` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media
- free tier: Per-file caps only, no storage quota: documents 100 MB, images 5 MB, video 16 MB, audio 16 MB, stickers 500 KB (as listed on the reference page). Files persist 30 days. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file caps only, no storage quota: documents 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: 'All media files sent through this API are encrypted and persist for 30 days, unless they are deleted earlier.' Media IDs also expire at 30 days (7 days for IDs arriving in webhooks) | days: 30 | source: [1] | note: not stated
- egress: Download is free of per-GB charge but doubly gated: media URLs EXPIRE AFTER 5 MINUTES and must be re-fetched via the media ID using a Bearer token. There is no public URL at any point. | metered: no
- identity: institution
- interface: rest, graph, rclone
- limits:
  - retention-clamped: expire at 30 days [1]
  - per-object-cap (binding): Per-file caps only, no storage quota: documents 100 MB [1]
- limits note: HARD 30-DAY DELETION. The disqualifier. 'All media files sent through this API are encrypted and persist for 30 days, unless they are deleted earlier.' Media IDs also expire at 30 days (7 days for IDs arriving in webhooks). Media URLs live 5 minutes.
- interface detail: rest
- tooling: Graph API; official SDKs (facebook-business, whatsapp-cloud-api wrappers). No rclone backend. Wrappers exist but cannot beat the 30-day deletion.
- composes with: Does not multiply. Retention, not count, is the wall. Unlimited phone numbers x 30 days each is still a 30-day window, i.e. a cache, not storage.
- reliability: Deterministic deletion, not a fair-use throttle: on day 31 the bytes are gone and only an error remains.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-file caps only, no storage quota: documents 100 MB, images 5 MB, video 16 MB, audio 16 MB, stickers 500 KB (as listed on the reference page). Files persist 30 days.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'All media files sent through this API are encrypted and persist for 30 days, unless they are deleted earlier.'; 'Media IDs returned by the API expire after 30 days. Media IDs in webhooks expire after 7 days.'; 'Media URLs expire after 5 minutes'
  - [1] 2026-10-21: read live: size table 'Text .txt text/plain 100 MB', 'AAC .aac 16 MB', etc.
  - [2] 2026-10-21: probe: GET -> 400 (anonymous call refused; token mandatory)
- sources:
  - [1] https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media
  - [2] https://graph.facebook.com/v21.0/123456/media
