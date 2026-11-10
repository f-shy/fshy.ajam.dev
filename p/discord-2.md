# Discord cloud uploads

> discord.food | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/discord-2/ | JSON https://fshy.ajam.dev/api/v1/entity/discord-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Discord cloud uploads (direct-to-GCS, 500 MiB reservation)

- `storage/discord-cloud-uploads` | qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.discord.food/topics/cloud-uploads
- free tier: Reserve an upload slot with `POST /channels/{id}/attachments` and PUT the body straight into Discord's Google Cloud Storage bucket. The reservation path accepts up to 500 MiB per file, independent of the 20 MiB message-time limit. Note the file still hits the per-message limit when you actually send it, so 500 MiB only helps if the channel/boost tier allows it. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MiB per file | bytes: 524288000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, unmetered, served from cdn.discordapp.com. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 500 MiB per file [1]
- limits note: 1-10 files per reservation call; `is_clip` flag grants a 100 MiB default; requires same permissions as normal attach; `DELETE /attachments/{upload_filename}` to clean up unused reservations.
- interface detail: rest
- tooling: Documented unofficial-API reference (docs.discord.food, formerly 'userdoccers'); Python pseudocode in the page; used in production by large bots. No dedicated library needed. Two HTTP calls.
- composes with: Upload slots are per-channel, so the 500 MiB ceiling multiplies by channel count (500/server) rather than by account.
- reliability: Endpoints are undocumented-but-stable and have moved URL shape before; a reservation you do not consume needs explicit deletion or it lingers.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [1] 2026-10-21: 'This allows you to upload up a file up to 500 MiB directly to Google Cloud. Note that file size limits will still apply when sending the attachment in a message.'
  - [1] 2026-10-21: 'When uploading a clip, an increased default file size limit of 100 MiB applies.'
- sources:
  - [1] https://docs.discord.food/topics/cloud-uploads
