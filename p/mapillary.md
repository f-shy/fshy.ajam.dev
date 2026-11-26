# Mapillary

> mapillary.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mapillary/ | JSON https://fshy.ajam.dev/api/v1/entity/mapillary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mapillary (Meta)

- `storage/mapillary` | qualifies-with-caveat | evidence reported | binding request-rate | category crowdsourced street-level imagery
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:00.435Z (live) | stale on 2026-12-04
- url https://www.mapillary.com
- free tier: Mapillary offers unlimited storage and makes imagery publicly available through an easy to use application. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: we've set an upper limit of 200 MP to image resolution and 110GB for video file-sizes | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Mapillary is 100% free to use—for any use case! | metered: no
- identity: email | detail: an account is needed to upload images, use the API, and download data
- interface: graph, cli
- limits:
  - request-rate (binding): 50,000 requests/minute [1]
  - request-rate (binding): 50,000 requests/DAY [1]
- limits note: per-image: 200 MP resolution ceiling, landscape orientation, EXIF GPS + timestamp required. Read side: graph.mapillary.com 50,000 requests/minute/app; tiles.mapillary.com 50,000 requests/DAY. The forum thread 'Can and does someone replicate the Mapillary images database?' states outright that the free plan's 50,000-image limit blocks bulk re-download.
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: Graph API at graph.mapillary.com (images, map features, detections); upload via mapillary_tools CLI or Desktop Uploader
- tooling: `mapillary_tools` (pip), Mapillary Desktop Uploader, official Python SDK, MapillaryJS
- composes with: Writes are geographically anchored, so this is a corpus, not a bucket. Read path returns tile/thumb URLs; a normal CDN in front works, but origin fetch is token-gated.
- reliability: Uploads are unmetered, while bulk retrieval is rate-limited to 50,000 vector tile requests per day via API.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 200 with {"error":{"message":"Invalid OAuth 2.0 Access Token","type":"MLYApiException","code":190}} (token-gated read, confirmed live)
  - [3] 2026-10-21: 'No, Mapillary is 100% free to use—for any use case! ... we have open-sourced our imagery'
  - [4] 2026-10-21: 'upper limit of 200 MP to image resolution'
  - [5] 2026-10-21: 50,000 requests/minute/app on graph.mapillary.com
  - [6] 2026-10-21: 'The rate limit for tiles is 50,000 requests per day'
  - withheld 2026-10-21: blog.mapillary.com 2024-07-08 — 'Mapillary offers unlimited storage' search snippet only
  - [1] 2026-11-09: the company blog states unlimited storage | capture: sha256:643171de3f34bcb3b3d787e22d3995cba907eeb245f8d1b8b561752f1c2bd49e | quote: Mapillary offers unlimited storage and makes imagery publicly available through an easy to use application.
  - [4] 2026-11-09: the help article states the image-resolution and video-size ceilings | capture: sha256:86f10b6449c2f832316ae44b6f76c051546a4a1521868fdc8864f487e5754b19 | quote: we've set an upper limit of 200 MP to image resolution and 110GB for video file-sizes
  - [3] 2026-11-09: the FAQ states Mapillary is free for any use case | capture: sha256:81fe9a60e388829d0de3971258679105c5133249e7d152c6333f96d520d0fde0 | quote: No, Mapillary is 100% free to use—for any use case!
  - [1] 2026-11-09: the blog states an account is needed for upload, API use and download | capture: sha256:643171de3f34bcb3b3d787e22d3995cba907eeb245f8d1b8b561752f1c2bd49e | quote: You need to create an account to upload images, use the API, and download data.
  - [5] 2026-11-09: the forum post states the graph API request limit | capture: sha256:660a090bf8ddfc5c605a7bea4d64305b4edb3877733f44046dc37d9971ba56a7 | quote: Requests to graph.mapillary.com are limited to 50,000 per minute per app.
  - [6] 2026-11-09: the forum post states the tile request limit | capture: sha256:2202469e635ab22b508163d6ecf05c9b626425eeee138927365e5d9c4a9c6433 | quote: The rate limit for tiles is 50,000 requests per day.
  - [1] 2026-11-19: the first-party blog confirms unlimited storage | capture: sha256:183f95a7b18afb0ebe2b4a7c89ea0d400d9c700d8ba82a2d28d550cd4d0654de | quote: Mapillary offers unlimited storage and makes imagery publicly available through an easy to use application.
  - [1] 2026-11-19: the blog confirms an account is required to upload, use the API and download | capture: sha256:183f95a7b18afb0ebe2b4a7c89ea0d400d9c700d8ba82a2d28d550cd4d0654de | quote: You need to create an account to upload images, use the API, and download data.
  - [3] 2026-11-19: the first-party FAQ confirms Mapillary is free for any use case | capture: sha256:81fe9a60e388829d0de3971258679105c5133249e7d152c6333f96d520d0fde0 | quote: No, Mapillary is 100% free to use—for any use case!
  - [4] 2026-11-19: the first-party help article confirms the 200 MP and 110 GB ceilings | capture: sha256:86f10b6449c2f832316ae44b6f76c051546a4a1521868fdc8864f487e5754b19 | quote: we've set an upper limit of 200 MP to image resolution and 110GB for video file-sizes
  - [5] 2026-11-19: the forum post states the graph API request limit | capture: sha256:660a090bf8ddfc5c605a7bea4d64305b4edb3877733f44046dc37d9971ba56a7 | quote: Requests to graph.mapillary.com are limited to 50,000 per minute per app.
  - [6] 2026-11-19: the forum post states the daily tile request limit | capture: sha256:2202469e635ab22b508163d6ecf05c9b626425eeee138927365e5d9c4a9c6433 | quote: The rate limit for tiles is 50,000 requests per day.
- sources:
  - [1] https://blog.mapillary.com/update/2024/07/08/expanding-public-street-level-imagery-access.html
  - [2] https://graph.mapillary.com/images?fields=thumb_2048_url&limit=1
  - [3] https://help.mapillary.com/hc/en-us/articles/8348198426396-Mapillary-FAQ
  - [4] https://help.mapillary.com/hc/en-us/articles/115001472029
  - [5] https://forum.mapillary.com/t/hitting-request-limit/5820
  - [6] https://forum.mapillary.com/t/receiving-html-response-instead-of-json/8336
