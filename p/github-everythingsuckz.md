# TG-FileStreamBot

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-everythingsuckz/ | JSON https://fshy.ajam.dev/api/v1/entity/github-everythingsuckz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TG-FileStreamBot / filestream.bot — HTTP stream front-end over Telegram files

- `storage/tg-filestreambot-filestream-bot-http-stream-front-end-ov` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:22.053Z (live) | stale on 2026-12-04
- url https://github.com/EverythingSuckz/TG-FileStreamBot
- free tier: Inherits Telegram's unlimited storage but solves a different problem: turning a stored Telegram file into a plain HTTP URL that a browser, VLC, or a download manager can range-request. 1,933 stars, pushed 2026-03-07, actively maintained. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB per file | bytes: 20000000 | source: [1] | note: not stated
- retention: Inherits Telegram's unlimited storage but solves a different problem: turning a stored Telegram file into a plain HTTP URL that a browser, VLC, or a download manager can range-request | source: [1] | note: not stated
- egress: Free from Telegram, served as HTTP from your host. So Cloudflare-cacheable. Multi-bot load balancing is the advertised scaling lever. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 20 MB per file [1]
- limits note: Bot-token based, so 20 MB per file via cloud Bot API unless you run the local Bot API server. It streams; it does not cache, so every viewer GET is a Telegram pull unless you add a CDN.
- interface detail: rest
- tooling: Go backend, multi-bot workers. The hosted filestream.bot instance describes the architecture plainly: 'Parallel block downloads with configurable concurrency. Prefetch buffers ensure smooth, uninterrupted playback' and 'Distribute API load across up to 50 bot tokens. Round-robin routing prevents rate limiting.' Same family as TheCaduceus/FileStreamBot (134 stars, 2024) and SpringsFern/tgfilestream.
- composes with: 50 bot tokens x their own per-account flood budgets = roughly 50x the single-account download concurrency, which is the only lever that moves Telegram read throughput.
- reliability: Maintained and the streaming model is sound. The failure mode is a hot file: N concurrent viewers on one file means N independent Telegram pulls, which will hit FLOOD_WAIT quickly without an edge cache.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [2] 2026-10-21: 'Multi-Bot Workers ... up to 50 bot tokens. Round-robin routing prevents rate limiting'
  - [1] 2026-10-21: 1,933 stars, pushed 2026-03-07
  - [1] 2026-10-21: 'instant stream links for telegram files without the need of waiting till the download completes'
  - [2] 2026-11-19: the tool exposes an HTTP streaming URL usable by browsers and download managers | capture: sha256:74eb06b5ca78e6c9a5fb93e7a322bbccc657d465e8b357ca5bd1b8df53ab1129 | quote: Clean, shareable URLs for any Telegram file. Works with video players, download managers, and browsers.
  - [2] 2026-11-19: the user installs and runs the server binary on a rented or free machine | capture: sha256:74eb06b5ca78e6c9a5fb93e7a322bbccc657d465e8b357ca5bd1b8df53ab1129 | quote: Docker, Koyeb, Heroku, or bare metal. Single binary, minimal config. Running in under a minute.
- sources:
  - [1] https://github.com/EverythingSuckz/TG-FileStreamBot
  - [2] https://filestream.bot/
