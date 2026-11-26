# Reddit native media

> reddit.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reddit/ | JSON https://fshy.ajam.dev/api/v1/entity/reddit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Reddit native media (i.redd.it)

- `storage/reddit-native-media` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:17.919Z (live) | stale on 2026-12-10
- url https://reddit.com
- free tier: Reddit accepts images up to 20 MB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Maximum upload size: 20 MB. | source: [1] | note: The developer docs state a maximum upload size of 20 MB.
- retention: Devvit does not currently provide an API to delete a media asset after it has been uploaded with `media.upload()`. | source: [1] | note: To stop showing uploaded media, remove the app's references to the asset and update or delete the Reddit content that embeds it.
- egress: media.upload() returns a Reddit CDN URL for use in rich text or UI. | metered: no
- identity: institution
- interface: rest
- limits note: 20 MB/image; media must go through the subreddit's native uploader (no arbitrary file types at all. Images and video only); spam filters and per-subreddit karma gates bite long before any byte cap.
- interface detail: rest
- tooling: official Reddit API has a /api/submit image path (submit_image + image_path / upload lease); PRAW and Late/Zernio wrappers expose it
- composes with: 20 MB x unlimited posts x unlimited subreddits x N accounts. 500 GB = 25,000 image posts; OAuth rate limits (100 QPM) make that ~4 hours of posting, far faster than a human, which is exactly what gets flagged
- reliability: i.redd.it is Fastly-backed and 404s cleanly (probe returned a 2016-dated 404 with x-amz-version-id), i.e. real object storage behind CDN; but media is tied to the post lifecycle and API-scoped uploads are heavily moderated
- notes: Reddit accepts videos up to 1 GB, and .mp4 or .mov files work most reliably.
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Reddit accepts images up to 20 MB' / 'Reddit accepts videos up to 1 GB'
  - [2] 2026-10-21: probe: HEAD -> 404 with 'Fastly-Restarts' and 'x-amz-version-id' headers (Fastly + S3-style origin, image/png content-type on 404)
  - [3] 2026-10-21: /api/submit documented; submit_image present in PRAW (github.com/praw-dev/praw issue 1359 shows the API path in use)
  - [1] 2026-11-11: Reddit accepts images up to 20 MB, unchanged | capture: sha256:ff21472d904aaf1f3db3953061aaa3ca1c2a5fd4119985bbded8dd5d9f2da9bb | quote: Reddit accepts images up to 20 MB.
  - [1] 2026-11-11: Reddit accepts videos up to 1 GB and .mp4 or .mov files work most reliably | capture: sha256:ff21472d904aaf1f3db3953061aaa3ca1c2a5fd4119985bbded8dd5d9f2da9bb | quote: Reddit accepts videos up to 1 GB, and .mp4 or .mov files work most reliably.
  - [4] 2026-11-25: the first-party developer docs state the maximum upload size | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: - Maximum upload size: 20 MB.
  - [4] 2026-11-25: the first-party developer docs state a 20 MB upload cap under notes and limits | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: - Maximum upload size: 20 MB.
  - [4] 2026-11-25: the first-party developer docs state that uploaded media has no delete API | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: Devvit does not currently provide an API to delete a media asset after it has been uploaded with `media.upload()`.
  - [4] 2026-11-25: the first-party developer docs state how uploaded media stops being shown | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: If your app needs to stop showing uploaded media, remove your app's references to the asset and update or delete the Reddit content that embeds it.
  - [4] 2026-11-25: the first-party developer docs state that uploaded media is served from a Reddit CDN URL | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: - `mediaUrl`: Reddit CDN URL (use this in rich text or UI).
  - [4] 2026-11-25: the first-party developer docs still state the 20 MB upload cap | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: - Maximum upload size: 20 MB.
  - [4] 2026-11-25: the first-party developer docs still state that uploaded media has no delete API | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: Devvit does not currently provide an API to delete a media asset after it has been uploaded with `media.upload()`.
  - [4] 2026-11-25: the first-party developer docs still tie media removal to the embedding content | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: If your app needs to stop showing uploaded media, remove your app's references to the asset and update or delete the Reddit content that embeds it.
  - [4] 2026-11-25: the first-party developer docs still state the Reddit CDN URL form | capture: sha256:f159df05edb2318841a57acef386b47e5b890323e553187b47b1c029bdc8a23f | quote: - `mediaUrl`: Reddit CDN URL (use this in rich text or UI).
  - [3] 2026-11-25: the first-party API documentation lists post-kind form fields including image and video | capture: sha256:ebb5bc4316bc6535b29cb5db822ef30c8f575f7f9e44ed219c4159d1717ea5cf | quote: | kind | one of (`link`, `self`, `image`, `video`, `videogif`) |
- sources:
  - [1] https://help.postpone.app/platforms/reddit/media-limits
  - [2] https://i.redd.it/
  - [3] https://www.reddit.com/dev/api/
  - [4] https://developers.reddit.com/docs/capabilities/server/media-uploads
