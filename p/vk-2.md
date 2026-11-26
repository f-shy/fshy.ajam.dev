# VK Video

> vk.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vk-2/ | JSON https://fshy.ajam.dev/api/v1/entity/vk-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VK Video (video hosting as bulk store)

- `storage/vk-video` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T03:33:10.194Z (live) | stale on 2026-12-10
- url https://vk.com/video
- free tier: up to 256 GB per single uploaded file; no per-account total published on the page read | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 256 GB per single upload | bytes: 256000000000 | source: [1] | note: The first-party press page states a 256 GB per-file upload size for video files.
- retention: source: [1] | note: The press page and the video-upload developer docs publish no retention period.
- egress: Free to viewers. Playback is served from VK's own streaming CDN, no per-GB charge to the uploader. | metered: no
- identity: email
- interface: rest
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
  - [1] 2026-11-19: VK Video supports uploads of files up to 256 GB | capture: sha256:463be48fa3b1f0bfbf381cf32edc07d6a7a69867576ea7b6ac530b588208387a | quote: Видеоролики высокого качества занимают больше места, поэтому Видео ВКонтакте теперь поддерживает загрузку «тяжёлых» файлов размером до 256 Гбайт.
  - [4] 2026-11-25: uploads go through the video.save API call followed by an HTTP multipart POST to the returned upload_url | capture: sha256:1148b896c0d38cf83db3cfd4f6a4c005ee365997edce35ac8716095a5800a1b5 | quote: Чтобы получить адрес для загрузки видеофайла, вызовите метод `video.save`.
  - [1] 2026-11-25: the press page gives the upload cap but states no retention period | capture: sha256:463be48fa3b1f0bfbf381cf32edc07d6a7a69867576ea7b6ac530b588208387a | quote: Видеоролики высокого качества занимают больше места, поэтому Видео ВКонтакте теперь поддерживает загрузку «тяжёлых» файлов размером до 256 Гбайт.
  - [1] 2026-11-25: the per-object cap is 256 GB for a single video upload | capture: sha256:463be48fa3b1f0bfbf381cf32edc07d6a7a69867576ea7b6ac530b588208387a | quote: Видеоролики высокого качества занимают больше места, поэтому Видео ВКонтакте теперь поддерживает загрузку «тяжёлых» файлов размером до 256 Гбайт.
  - [1] 2026-11-25: the first-party press page still states the 256 GB single-upload cap | capture: sha256:463be48fa3b1f0bfbf381cf32edc07d6a7a69867576ea7b6ac530b588208387a | quote: Видеоролики высокого качества занимают больше места, поэтому Видео ВКонтакте теперь поддерживает загрузку «тяжёлых» файлов размером до 256 Гбайт.
  - [4] 2026-11-25: video uploads use the documented video.save API and multipart upload_url | capture: sha256:1148b896c0d38cf83db3cfd4f6a4c005ee365997edce35ac8716095a5800a1b5 | quote: Чтобы получить адрес для загрузки видеофайла, вызовите метод `video.save`.
- sources:
  - [1] https://vk.com/press/new-video
  - [2] https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/vk.py
  - [3] https://github.com/yt-dlp/yt-dlp/issues/16070
  - [4] https://dev.vk.com/ru/api/upload/video-in-profile
