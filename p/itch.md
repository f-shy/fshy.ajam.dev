# itch.io

> itch.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/itch/ | JSON https://fshy.ajam.dev/api/v1/entity/itch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## itch.io (butler / Wharf)

- `storage/itch-io` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://itch.io/docs/butler/pushing.html
- free tier: 30 GB uncompressed per build ('the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB'). No documented total-account storage cap; project pages have a soft limit of 20, raisable on request. Free to host, unlimited downloads. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 30 GB | bytes: 30000000000 | source: [1] | note: not stated
- retention: per-object-cap: 30 GB uncompressed per build/channel; per-object-cap on HTML5 embeds: 500 MB total extracted and 200 MB per single extracted file; web uploader caps at 2 GB (500 MB default) but butler has no such limit; request-rate not a practical constraint. Retention: builds persist until deleted; no TTL. | source: [1] | note: not stated
- egress: Free and unmetered. 'There is no limit to downloads' (itch.io support reply). Files served from itch.zone CDN. | metered: no
- identity: institution
- interface: rest, rsync, cli
- limits:
  - per-object-cap (binding): per-object-cap: 30 GB [1]
- limits note: per-object-cap: 30 GB uncompressed per build/channel; per-object-cap on HTML5 embeds: 500 MB total extracted and 200 MB per single extracted file; web uploader caps at 2 GB (500 MB default) but butler has no such limit; request-rate not a practical constraint. Retention: builds persist until deleted; no TTL.
- interface detail: rest
- tooling: `butler` CLI (butler push / butler download / butler status) plus the Wharf HTTP API. GET https://api.itch.io/wharf/latest?target=user/game&channel_name=X returns the build manifest. butler does rsync-style block diffing so re-pushes are cheap.
- composes with: 30 GB per build x unlimited channels per project (channel name is arbitrary: windows, osx, bonus, dlc-1, shard-01...) x up to 20+ projects per free account. 1 project x 20 channels = 600 GB on one free account. Each build is independently addressable and downloadable.
- reliability: Pushing the same directory twice is a no-op, so versions accumulate as distinct builds rather than overwriting; butler auth uses an API key, and a project can be taken down by moderation (technical effect: URL 404s, data gone).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.'
  - [2] 2026-10-21: 'butler is a more advanced uploader and has no such technical limits'; web uploader 2 GB ceiling
  - [3] 2026-10-21: 'There is no limit to downloads'; butler raises per-project limit to 2 GB instantly, further on request
  - [4] 2026-10-21: probe: GET -> 200 {"errors":["invalid game"]} — endpoint is live and validating, i.e. the manifest read path is public
  - [5] 2026-10-21: probe: GET -> 200, 39871 bytes, image/png — itch.zone CDN serves originals anonymously, no referer chain
- sources:
  - [1] https://itch.io/docs/butler/pushing.html
  - [2] https://itch.io/t/46291/uploading-large-games-faq
  - [3] https://itch.io/t/6077449/more-project-space
  - [4] https://api.itch.io/wharf/latest?target=test/test&channel_name=windows
  - [5] https://img.itch.zone/aW1nLzE2ODI3NDY4LnBuZw==/original/ljN55Y.png
