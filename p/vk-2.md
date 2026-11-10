# VK Video

> vk.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vk-2/ | JSON https://fshy.ajam.dev/api/v1/entity/vk-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VK Video (video hosting as bulk store)

- `storage/vk-video` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://vk.com/video
- free tier: up to 256 GB per single uploaded file; no per-account total published on the page read | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 256 GB per single upload | bytes: 256000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free to viewers. Playback is served from VK's own streaming CDN, no per-GB charge to the uploader. | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 256 GB per single upload [1]
- limits note: 256 GB single file; video must be a real playable video container (arbitrary bytes only survive if 'original file download' is enabled by the uploader); retrieval goes through the player/extractor path
- interface detail: wrapper-only
- tooling: yt-dlp VK extractor (yt_dlp/extractor/vk.py) for retrieval; VK API video.save / video upload for pushing files
- composes with: Per-upload limit is 256 GB with unlimited video uploads per account, allowing dataset distribution across discrete video files on a single identity.
- reliability: Uploaded media may be transcoded; non-video payloads die on transcode; VK periodically changes the playback protocol and breaks yt-dlp (yt-dlp issues 16070/11715 track exactly this churn), and content can be removed for complaints.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Видео ВКонтакте теперь поддерживает загрузку «тяжёлых» файлов размером до 256 Гбайт'
  - [2] 2026-10-21: maintained VK extractor (working retrieval client)
  - [3] 2026-10-21: '[VK Video] supposedly updated protocol inhibits downloads' (retrieval breaks periodically)
- sources:
  - [1] https://vk.com/press/new-video
  - [2] https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/vk.py
  - [3] https://github.com/yt-dlp/yt-dlp/issues/16070
