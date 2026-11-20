# morb0/tgbucket

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-morb0/ | JSON https://fshy.ajam.dev/api/v1/entity/github-morb0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## morb0/tgbucket, two/telegram-fuse, demidko/telegram-storage and the long ta

- `storage/morb0-tgbucket-two-telegram-fuse-demidko-telegram-storag` | self-hosted, last resort | verdict dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.636Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-morb0.md
- free tier: none reachable: Real projects but abandoned (tgbucket last pushed 2022-05-06, 8 stars). gh search repos 'telegram storage' returns 20+ repos with a median of ~10 stars, most unmaintained since 2022-2023.… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Max file size - 2000MiB (files uploaded to Telegram up to 2GB with a bot token). | note: not applicable
- retention: stated-absent: the first-party page states no a retention period; the README describes upload and download only
- egress: stated-absent: the first-party page states no egress terms in the first-party README | metered: no
- identity: email
- interface: rest
- interface detail: HTTP API using MTProto: POST / to upload, GET /:id to download
- tooling: the user installs and runs the tgbucket server (node, postgres and pnpm on a rented or free machine) against a Telegram bot token and chat
- composes with: Uses Telegram as its storage backend through the MTProto protocol; requires an application ID, hash, bot token and chat ID.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Real projects but abandoned (tgbucket last pushed 2022-05-06, 8 stars). gh search repos 'telegram storage' returns 20+ repos with a median of ~10 stars, most unmaintained since 2022-2023.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Real projects but abandoned (tgbucket last pushed 2022-05-06, 8 stars). gh search repos 'telegram storage' returns 20+ repos with a median of ~10 stars, most unmaintained since 2022-2023.…
  - [1] 2026-11-19: the project is software the user installs and runs locally rather than a hosted offer | capture: sha256:7b8b6ac4725f879c69d1505a52fec7bce72875f89c2d68c0fb930596d8494ea8 | quote: Open `localhost:3000` and see `ok` message *(default port: 3000)*
  - [1] 2026-11-19: the offer is an open-source project the user runs, with no hosted instance offered | capture: sha256:7b8b6ac4725f879c69d1505a52fec7bce72875f89c2d68c0fb930596d8494ea8 | quote: Open source project that provide simple HTTP API to upload and download files to/from Telegram.
  - [2] 2026-11-19: the tgbucket first-party README describes an HTTP upload/download API over Telegram | capture: sha256:7b8b6ac4725f879c69d1505a52fec7bce72875f89c2d68c0fb930596d8494ea8 | quote: Open source project that provide simple HTTP API to upload and download files to/from Telegram.
  - [2] 2026-11-19: the tgbucket first-party README states a 2000 MiB per-file maximum | capture: sha256:7b8b6ac4725f879c69d1505a52fec7bce72875f89c2d68c0fb930596d8494ea8 | quote: Max file size - 2000MiB
- sources:
  - [1] https://github.com/Morb0/tgbucket
  - [2] https://github.com/morb0/tgbucket
