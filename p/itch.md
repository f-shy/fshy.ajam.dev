# itch.io

> itch.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/itch/ | JSON https://fshy.ajam.dev/api/v1/entity/itch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## itch.io (butler / Wharf)

- `storage/itch-io` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:10.653Z (live) | stale on 2026-12-10
- url https://itch.io/docs/butler/pushing.html
- free tier: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB. | bytes: 30000000000 | source: [1] | note: - The size of all the extracted content should not be greater than 500MB. - The size any single extracted file should not be greater than 200MB.
- retention: No. You will always fully own your content. You are free to remove it at any time. | source: [1] | note: No. You will always fully own your content. You are free to remove it at any time.
- egress: There is no limit to downloads. | metered: no
- identity: institution
- interface: rest, rsync, cli
- limits:
  - per-object-cap (binding): Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB. [1]
- limits note: the same as the free tier
- interface detail: GET https://api.itch.io/wharf/latest This endpoint does not require authentication.
- tooling: `butler` CLI (butler push / butler download / butler status) plus the Wharf HTTP API. GET https://api.itch.io/wharf/latest?target=user/game&channel_name=X returns the build manifest. butler does rsync-style block diffing so re-pushes are cheap.
- composes with: Pushing to a new channel will make a corresponding file appear on your game's page
- reliability: Pushing the same directory twice is a no-op, so versions accumulate as distinct builds rather than overwriting; butler auth uses an API key, and a project can be taken down by moderation (technical effect: URL 404s, data gone).
- notes: 30 GB uncompressed per build ('the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB'). No documented total-account storage cap; project pages have a soft limit of 20, raisable on request. Free to host, unlimited downloads.
- evidence note: the 30 GB uncompressed per-build ceiling is stated on the butler pushing page
- evidence:
  - [1] 2026-10-21: 'Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.'
  - [2] 2026-10-21: 'butler is a more advanced uploader and has no such technical limits'; web uploader 2 GB ceiling
  - [3] 2026-10-21: 'There is no limit to downloads'; butler raises per-project limit to 2 GB instantly, further on request
  - [4] 2026-10-21: probe: GET -> 200 {"errors":["invalid game"]} — endpoint is live and validating, i.e. the manifest read path is public
  - [5] 2026-10-21: probe: GET -> 200, 39871 bytes, image/png — itch.zone CDN serves originals anonymously, no referer chain
  - [1] 2026-11-09: the backend rejects a build whose total uncompressed size exceeds 30GB | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.
  - [1] 2026-11-25: the backend rejects builds whose total uncompressed size exceeds 30GB | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.
  - [6] 2026-11-25: HTML5 embeds are limited to 500MB extracted total and 200MB per extracted file | capture: sha256:5e2812ba18c12a0232d42abaac5fbf08ac41a1e0929ef441d5ed9d73f4a1d342 | quote: - The size of all the extracted content should not be greater than 500MB. - The size any single extracted file should not be greater than 200MB.
  - [1] 2026-11-25: the binding limit is a 30GB uncompressed build ceiling | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.
  - [1] 2026-11-25: the stated limit is 30GB uncompressed per build | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.
  - [7] 2026-11-25: creators retain ownership and control removal of their content | capture: sha256:6a4162d8711b82a5279854ac325a57b0c442a22e8b46727e88dfb7e67e9de015 | quote: No. You will always fully own your content. You are free to remove it at any time.
  - [7] 2026-11-25: the creator controls removal; no fixed retention period is stated | capture: sha256:6a4162d8711b82a5279854ac325a57b0c442a22e8b46727e88dfb7e67e9de015 | quote: No. You will always fully own your content. You are free to remove it at any time.
  - [3] 2026-11-25: downloads are not limited | capture: sha256:814d090946eec7208721d59755fe53b498afa3690e4898723aa09346a7f37748 | quote: There is no limit to downloads.
  - [1] 2026-11-25: each pushed channel produces a file on the game page | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Pushing to a new channel will make a corresponding file appear on your game's page
  - [1] 2026-11-25: an unauthenticated HTTP GET endpoint exposes the latest build | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: GET https://api.itch.io/wharf/latest This endpoint does not require authentication.
  - [1] 2026-11-25: the 30GB uncompressed build ceiling is unchanged | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Limits: currently, the itch.io backend will reject builds with a total uncompressed size that exceeds 30GB.
  - [6] 2026-11-25: HTML5 embeds have a 500MB extracted total cap and a 200MB per-file cap | capture: sha256:5e2812ba18c12a0232d42abaac5fbf08ac41a1e0929ef441d5ed9d73f4a1d342 | quote: - The size of all the extracted content should not be greater than 500MB. - The size any single extracted file should not be greater than 200MB.
  - [7] 2026-11-25: content stays under creator control and can be removed by the creator | capture: sha256:6a4162d8711b82a5279854ac325a57b0c442a22e8b46727e88dfb7e67e9de015 | quote: No. You will always fully own your content. You are free to remove it at any time.
  - [3] 2026-11-25: downloads have no stated limit | capture: sha256:814d090946eec7208721d59755fe53b498afa3690e4898723aa09346a7f37748 | quote: There is no limit to downloads.
  - [1] 2026-11-25: a new channel yields a separate file on the project page | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: Pushing to a new channel will make a corresponding file appear on your game's page
  - [1] 2026-11-25: the latest-build endpoint is an unauthenticated HTTP GET | capture: sha256:8ffe3cac95c4ac576d8b52a69e2e663c2b32a52a7a3ef337a17921b76a3d7d40 | quote: GET https://api.itch.io/wharf/latest This endpoint does not require authentication.
- sources:
  - [1] https://itch.io/docs/butler/pushing.html
  - [2] https://itch.io/t/46291/uploading-large-games-faq
  - [3] https://itch.io/t/6077449/more-project-space
  - [4] https://api.itch.io/wharf/latest?target=test/test&channel_name=windows
  - [5] https://img.itch.zone/aW1nLzE2ODI3NDY4LnBuZw==/original/ljN55Y.png
  - [6] https://itch.io/docs/creators/html5
  - [7] https://itch.io/docs/creators/faq
