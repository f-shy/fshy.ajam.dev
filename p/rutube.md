# RUTUBE

> rutube.ru | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rutube/ | JSON https://fshy.ajam.dev/api/v1/entity/rutube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RUTUBE

- `storage/rutube` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:30.563Z (live) | stale on 2026-11-25
- url https://rutube.ru
- free tier: Размер: не более 25 Гб | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: не более 25 Гб | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free playback from Rutube's own CDN, no charge to uploader | metered: no
- identity: institution
- interface: unknown
- limits note: 25 GB and 300 minutes per video; 5 simultaneous uploads; formats limited to video containers (MP4/AVI/MOV/WebM/HEVC/ProRes...); re-encode on ingest
- interface detail: wrapper-only
- tooling: rutube/php-api-client (github.com/rutube/php-api-client, explicitly unmaintained); yt-dlp has a Rutube extractor
- composes with: per-record: 25 GB per video x unlimited videos per free account. 20 TiB = ~820 uploads, no new accounts needed.
- reliability: Ingest re-encodes, so this only stores video, not arbitrary bytes; official API client is abandoned, retrieval depends on yt-dlp staying current.
- notes: 25 GB max per video, 5 concurrent uploads; no total per-account cap stated on the FAQ page read
- evidence note: the upload FAQ states the per-video size limit
- evidence:
  - [1] 2026-10-21: 'Размер: не более 25 Гб', 'Длительность: не более 5 часов', 'Одновременно можно загружать до 5 видеороликов'
  - [2] 2026-10-21: 'Внимание! Данный репозиторий более не поддерживается.'
  - [1] 2026-11-09: the upload FAQ states a per-video size limit of no more than 25 Gb | capture: sha256:529c891356d2afb0897d47ce20a0b6c6d14a2829009f366d9755db5ffc30dd0d | quote: Размер: не более 25 Гб
- sources:
  - [1] https://rutube.ru/info/upload/
  - [2] https://github.com/rutube/php-api-client
