# Discord

> discord.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/discord/ | JSON https://fshy.ajam.dev/api/v1/entity/discord.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Discord + ddrive (Discord as a datastore)

- `storage/discord-ddrive` | qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://discord.com
- free tier: No total storage cap on free accounts; 10 MB per file on free (20 MB per Discord's own File Attachments FAQ), 50 MB Nitro Basic, 1 GB Nitro; attachments upload up to 500 MiB per file via the cloud-upload endpoint before the message-time limit applies | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and CDN-served; every attachment URL is signed with `ex`/`is`/`hm` params, so links are time-limited but re-mintable via the API at zero cost | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 10 MB per file [1]
  - per-object-cap (binding): 500 MiB per file [1]
- limits note: 24 MB chunk size in ddrive; 500 MiB per-file ceiling on the cloud-upload path; aggressive per-channel message and upload rate limits (ddrive moves to webhooks specifically to route around them); attachment URLs expire (hex `ex` timestamp) and must be re-fetched
- interface detail: rest
- tooling: forscht/ddrive (533 stars, MIT, active 4.x line, Docker image, OpenAPI 3.1 REST front end, Postgres metadata, webhook-based to avoid rate limits) - explicitly 'unlimited file size and unlimited storage'; also theseyan/distore, iShibi/discord-drive
- composes with: Per-file cap x shard count is irrelevant because ddrive splits into 24 MB chunks. Author reports 'tested with storing 4000 GB of data on single discord channel'. Several free Discord accounts, servers and channels each carry a separate allowance, and a bot token can span many channels.
- reliability: Highest operational risk of the set: Discord rate-limits uploads hard, CDN URLs expire, and the reference demo (ddrive.forscht.dev) is currently down (HTTP 522), so the wrapper is battle-tested but its hosted instance is not.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'For non-Nitro subscribers, the maximum file upload is 20MB.' (page updated 2026-09-30)
  - [2] 2026-10-21: 'Supports an unlimited file size and unlimited storage... Tested with storing 4000 GB of data on single discord channel'; 'splitting the file in 24mb chunks'; 'Now uses webhooks instead of bot/user tokens to bypass the discord rate limit' (the author's own phrase for moving uploads to a webhook, which is outside the per-channel message limit)
  - [3] 2026-10-21: 'upload up a file up to 500 MiB directly to Google Cloud'; reference.mdx documents `ex` as 'Hex timestamp indicating when an attachment CDN URL will expire'
  - [4] 2026-10-21: probe: GET -> 200 image/png via Cloudflare edge; GET https://ddrive.forscht.dev/ -> 522 (demo down)
- sources:
  - [1] https://support.discord.com/hc/en-us/articles/25444343291031-File-Attachments-FAQ
  - [2] https://raw.githubusercontent.com/forscht/ddrive/master/README.md
  - [3] https://raw.githubusercontent.com/discord-userdoccers/discord-userdoccers/main/pages/topics/cloud-uploads.mdx
  - [4] https://cdn.discordapp.com/embed/avatars/0.png

## Discord free account (attachment CDN)

- `storage/discord-free-account` | qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://discord.com
- free tier: No total storage cap documented anywhere. Per-file only: 20 MiB per attachment on a free account since 2026-09-03 (raised from 10 MiB). 10 files per message. Server Boost tiers raise it for all members in that server: Tier 2 = 50 MB, Tier 3 = 100 MB; Nitro Basic 50 MB, Nitro 500 MB (1 GB per the Nitro marketing page). | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MiB per file | bytes: 20971520 | source: [1] | note: not stated
- retention: | Attachment CDN URLs are signed and expire in exactly 24 h; the bytes stay on Discord's servers indefinitely but the link must be re-derived via `POST /api/v10/attachments/refresh-urls` (401 without a token) or by re-reading the message | source: [1] | note: not stated
- egress: Unmetered and free. Cdn.discordapp.com is Cloudflare-fronted and there is no bandwidth metering or egress billing of any kind. This is the strongest egress position in the whole survey. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 20 MiB per file [1]
- limits note: 20 MiB per file is the hard bite. Message create is ~5 messages / 5 s per channel; global ~50 req/s per token; 10,000 invalid requests per 10 min triggers a 24 h Cloudflare ban. Attachment URLs carry `ex`/`is`/`hm` and stop working after 24 h. See reliability_note.
- interface detail: rest
- tooling: Official Bot HTTP API (`POST /channels/{id}/messages` with files[], or the two-step cloud-upload path). Mature wrappers: forscht/ddrive (533 stars, Discord-as-filesystem with REST + OpenAPI 3.1), missuo/discord-image (212 stars, Go, refreshes CDN links), ShufflePerson/Discord_CDN (link refresher proxy), DisboxApp/server. No rclone backend.
- composes with: 100 servers per free account (200 with Nitro) x 500 channels per server = 50,000 text channels per account, and every channel takes unlimited messages. This is the multiplier: not per-file size but per-message count. ddrive's author reports storing 4,000 GB in a single Discord channel, so the practical ceiling is account count x rate limit, not storage.
- reliability: Attachment CDN URLs are signed and expire in exactly 24 h; the bytes stay on Discord's servers indefinitely but the link must be re-derived via `POST /api/v10/attachments/refresh-urls` (401 without a token) or by re-reading the message. Any un-refreshed link returns 404 'This content is no longer available.'
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'September 3, 2026 — Default File Upload Limit Increase: The default file upload limit has been increased from 10 MiB to 20 MiB for users, bots, webhooks, and interaction responses'
  - [2] 2026-10-21: 'Attachments uploaded to Discord's CDN have signed URLs with a preset expiry time'; example `?ex=65d903de&is=65c68ede&hm=...`; 'ex — Hex timestamp indicating when an attachment CDN URL will expire'
  - withheld 2026-10-21: probe: decoded ex/is from a real signed URL (ex=66424c96, is=6640fb16) -> ex-is = 86400 s = exactly 24.0 h; GET that URL today -> 404; GET the same path with no query string -> 404 'This content is no longer available.'
  - [3] 2026-10-21: 'Number of servers: 100 | Number of servers Nitro: 200 | Channels (includes voice/text/categories): 500 | Upload Base 10MB, Level 2 50MB for all members, Level 3 100MB for all members'
- sources:
  - [1] https://docs.discord.com/developers/change-log
  - [2] https://docs.discord.com/developers/reference
  - [3] https://support.discord.com/hc/en-us/articles/33694251638295

## discord as a durable cdn origin

- `storage/discord-as-a-durable-cdn-origin` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.discord.com/developers/resources/message#signed-attachment-cdn-urls
- free tier: none reachable: Signed attachment URLs expire in exactly 24 hours (measured ex-is = 86400) and unsigned fetches 404. A URL cannot be stored in a catalog and reused; every read needs an authenticated… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Signed attachment URLs expire in exactly 24 hours (measured ex-is = 86400) and unsigned fetches 404. A URL cannot be stored in a catalog and reused; every read needs an authenticated…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Signed attachment URLs expire in exactly 24 hours (measured ex-is = 86400) and unsigned fetches 404. A URL cannot be stored in a catalog and reused; every read needs an authenticated…
- sources:
  - [1] https://docs.discord.com/developers/resources/message#signed-attachment-cdn-urls
