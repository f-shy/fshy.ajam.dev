# Macaulay Library

> macaulaylibrary.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macaulaylibrary/ | JSON https://fshy.ajam.dev/api/v1/entity/macaulaylibrary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Macaulay Library / eBird (Cornell Lab of Ornithology)

- `storage/macaulay-library-ebird` | qualifies-with-caveat | evidence reported | binding per-object-cap | category biodiversity media archive
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:00.434Z (live) | stale on 2026-12-04
- url https://www.macaulaylibrary.org
- free tier: When you upload media to the Macaulay Library, the archive serves as your personal cloud storage and backup of your media files. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Upload full-resolution images, as long as they are JPG and under 20 MB each. | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: media are not available for personal download unless they belong to you. | metered: no
- identity: email | detail: If the Add Media / Manage Media button doesn’t appear, make sure you are logged into your eBird account.
- interface: cli
- limits:
  - per-object-cap (binding): 20 MB/file [1]
  - per-object-cap (binding): 500 MB/file [1]
- limits note: photo 20 MB/file (JPG); audio 500 MB/file (WAV); video 1 GB/file (MP4/MOV/M4V, ≥720p); 20 photos + 10 audio per species per checklist; 10 video files per species
- interface detail: eBird checklist upload (web + Manage Media page); Macaulay Library catalog pages; no documented public write API
- tooling: no CLI. The uploader is a browser tool. Media search has an API but it sits behind an Anubis proof-of-work wall.
- composes with: Not chainable programmatically. The write path is a UI and the read path returns re-encoded previews, not originals, to anyone but the owner.
- reliability: Classic rule-2 pattern: upload-open, read-gated. Your own originals come back, but nobody else's do, and the media endpoints are behind Anubis PoW (search.macaulaylibrary.org/api/v1/search returned the 'Making sure you're not a bot!' interstitial).
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Upload full-resolution images ... under 20 MB each'; 'Uncompressed .WAV ... up to 500 MB each'; 'maximum 20 photos, 10 audio per species'
  - [3] 2026-10-21: video: 'max 1 GB per file ... up to 10 files per species per checklist'
  - [1] 2026-10-21: 'media are not available for personal download unless they belong to you'
  - [4] 2026-10-21: returned the Anubis PoW interstitial, not JSON
  - [1] 2026-11-09: the media article states the archive is personal cloud storage and backup | capture: sha256:24d449c030655b985de7fa00f8c11cba5233b7171b94e1474cbebd153f33ad95 | quote: When you upload media to the Macaulay Library, the archive serves as your personal cloud storage and backup of your media files.
  - [1] 2026-11-09: the media article states the download restriction to the owner | capture: sha256:24d449c030655b985de7fa00f8c11cba5233b7171b94e1474cbebd153f33ad95 | quote: media are not available for personal download unless they belong to you.
  - [2] 2026-11-09: the upload article requires a logged-in eBird account | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: make sure you are logged into your eBird account
  - [2] 2026-11-09: the upload article states a 20 MB per-image cap | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Upload full-resolution images, as long as they are JPG and under 20 MB each.
  - [2] 2026-11-09: the upload article states a 500 MB per-audio-file cap | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Uncompressed .WAV files, which are higher quality than .mp3 or .m4a, up to 500 MB each.
  - [2] 2026-11-11: the page states the Add Media / Manage Media button requires the reader to be logged into an eBird account | capture: sha256:fb05864fefb439905565ee6ccb45238e2b8f84675cdbbd3b8ebc65c4cf2b3932 | quote: If the Add Media / Manage Media button doesn’t appear, make sure you are logged into your eBird account.
  - [2] 2026-11-11: the page states a 20 MB per-file cap for JPG images, not an unconditional cap for every media file | capture: sha256:fb05864fefb439905565ee6ccb45238e2b8f84675cdbbd3b8ebc65c4cf2b3932 | quote: Upload full-resolution images, as long as they are JPG and under 20 MB each.
  - [1] 2026-11-19: the first-party article confirms the personal-cloud-storage framing | capture: sha256:24d449c030655b985de7fa00f8c11cba5233b7171b94e1474cbebd153f33ad95 | quote: When you upload media to the Macaulay Library, the archive serves as your personal cloud storage and backup of your media files.
  - [1] 2026-11-19: the article confirms originals are downloadable only by the owner | capture: sha256:24d449c030655b985de7fa00f8c11cba5233b7171b94e1474cbebd153f33ad95 | quote: media are not available for personal download unless they belong to you.
  - [2] 2026-11-19: the upload article confirms a 20 MB per-image cap | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Upload full-resolution images, as long as they are JPG and under 20 MB each.
  - [2] 2026-11-19: the upload article confirms a 500 MB per-audio-file cap | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Uncompressed .WAV files, which are higher quality than .mp3 or .m4a, up to 500 MB each.
  - [2] 2026-11-19: the upload article confirms a logged-in eBird account is required to add media | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: make sure you are logged into your eBird account
- sources:
  - [1] https://support.ebird.org/en/support/solutions/articles/48001064551-using-and-requesting-media
  - [2] https://support.ebird.org/en/support/solutions/articles/48000825713-uploading-media
  - [3] https://support.ebird.org/en/support/solutions/articles/48001064314
  - [4] https://search.macaulaylibrary.org/api/v1/search?taxonCode=norcar&count=1
