# Macaulay Library

> macaulaylibrary.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macaulaylibrary/ | JSON https://fshy.ajam.dev/api/v1/entity/macaulaylibrary.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Macaulay Library / eBird (Cornell Lab of Ornithology)

- `storage/macaulay-library-ebird` | qualifies-with-caveat | evidence reported | binding per-object-cap | category biodiversity media archive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.macaulaylibrary.org
- free tier: No published per-account byte quota. Tens of millions of assets, and Cornell explicitly positions it as backup: 'the archive serves as your personal cloud storage and backup of your media files.' Capacity is bounded by per-file and per-checklist caps, not by an account quota. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB/file | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: originals are downloadable BY THE OWNER ONLY ('your original uploaded files are available for you to download at any time by clicking the Download original link'). Public read is view/embed only; bulk research access is a manual request queue. | metered: no
- identity: email | detail: Email. EBird account is a Cornell Lab account with an email address; no institutional requirement documented.
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
- sources:
  - [1] https://support.ebird.org/en/support/solutions/articles/48001064551-using-and-requesting-media
  - [2] https://support.ebird.org/en/support/solutions/articles/48000825713-uploading-media
  - [3] https://support.ebird.org/en/support/solutions/articles/48001064314
  - [4] https://search.macaulaylibrary.org/api/v1/search?taxonCode=norcar&count=1
