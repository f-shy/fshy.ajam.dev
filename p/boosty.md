# Boosty

> boosty.to | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boosty/ | JSON https://fshy.ajam.dev/api/v1/entity/boosty.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Boosty (RU)

- `storage/boosty` | fails-egress | evidence reported | binding per-object-cap | category Russian creator monetisation / Patreon analogue
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://boosty.to
- free tier: 20 GB per attached video (official FAQ post: 'Вы можете прикреплять к постам видео размером до 20 ГБ'). Community reports the effective limit was cut to 1 GB at one point (2025-07 post: 'Бусти ограничили ... до 1 ГИГА'). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 20 GB | bytes: 20000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Subscriber-gated; no public CDN link. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): per-object-cap 20 GB [1]
- limits note: Per-object cap is 20 GB for video files. Uploaded video is re-encoded for the internal player rather than served in original bit-exact format.
- interface detail: Web + a reverse-engineered API (community downloaders exist: ath31st/boosty_downloader).
- tooling: Unofficial API clients only.
- composes with: 20 GB is attractive but only for video, and video is transcoded. So the ingest number does not translate into storage of arbitrary bytes.
- reliability: Re-encodes video at ingest and does not preserve original binary files. Published upload limits have been reduced in past platform updates.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB per attached video (official FAQ post: 'Вы можете прикреплять к постам видео размером до 20 ГБ'). Community reports the effective limit was cut to 1 GB at one point (2025-07 post: 'Бусти ограничили ... до 1 ГИГА').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: official FAQ: 'Вы можете прикреплять к постам видео размером до 20 ГБ'
  - [2] 2026-10-21: user report 2025-07: limit cut from 20 GB to 1 GB
  - [3] 2026-10-21: announcement of internal video player, i.e. server-side transcoding
  - [4] 2026-10-21: community downloader confirming API-only access
- sources:
  - [1] https://boosty.to/boosty/posts/de1e6f32-3a80-4824-95bd-a264ff1b00aa
  - [2] https://boosty.to/tijoe/posts/16953118-1d49-4556-8e8e-75b7563d513e
  - [3] https://boosty.to/boosty/posts/211aa703-9381-40ac-b22d-9f74cea67836
  - [4] https://github.com/ath31st/boosty_downloader
