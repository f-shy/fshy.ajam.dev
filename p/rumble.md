# Rumble

> rumble.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rumble/ | JSON https://fshy.ajam.dev/api/v1/entity/rumble.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rumble

- `storage/rumble` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:20.739Z (live) | stale on 2026-11-19
- url https://rumble.com
- free tier: No published total storage cap. 15 GB per file standard, 30 GB for Premium/monetised channels; up to 8 hours duration. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 15 GB per file | bytes: 15000000000 | source: [1] | note: Third-party documentation reports 15 GB per file; the help centre's upload article states no file-size limit and caps videos played during a livestream at 1 GB.
- retention: source: [1] | note: There's two video types that cannot be deleted, and those are the ones submitted under these licenses:
- egress: Free. Rumble serves its own CDN, no egress billing. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 15 GB per file [1]
  - per-object-cap (binding): 1 GB for video played during a livestream [2]
- limits note: 15 GB/file is mid-tier. Upload is web-form only. This is the automation blocker, since yt-dlp solves retrieval but nothing solves programmatic upload.
- interface detail: rest
- tooling: yt-dlp `Rumble`, `RumbleChannel`, `RumbleEmbed` extractors (verified present). No public upload API; upload is web-only.
- composes with: Unlimited files x unlimited accounts at 15 GB each. No documented daily cap, which is unusual and useful.
- reliability: Direct FAQ documentation was unreachable during testing on 2026-10-21. The 15 GB maximum video upload figure is reported in third-party platform documentation.
- notes: unverified: https://rumble.support/help/how-to-upload-a-video answered HTTP 200 on 2026-11-11 through the environment proxy; its text carries a three-step upload heading, an image, a link reading https://rumble.com/upload and a licence note, and states no file-size or duration limit.
- evidence:
  - [3] 2026-05-22: 'Rumble max file size: 15 GB per upload' (third-party, claims last verified 2026-05-22)
  - [4] 2026-10-21: 'Max File Size 15 GB (standard) / 30 GB (Premium/monetised)'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors` -> Rumble, RumbleChannel, RumbleEmbed present
  - withheld 2026-10-21: unverified: rumble.com/faq and rumble.com/pricing returned 404/410/504 — blocked/unavailable, no first-party page read
  - [5] 2026-11-09: the linked upload article is a three-step guide and states no file-size or duration limit | capture: sha256:c84706deb4bfae5e473b39e91312af4f9e66437267624c33590c1502a48bcf37 | quote: How to upload a video in 3 steps
  - probe:https://rumble.support/help/how-to-upload-a-video 2026-11-11: the page answered HTTP 200 on 2026-11-11 and the 235507-byte body was read in full | capture: sha256:8a974d730ba08f4e2d9573da701dbd565b3b387a3239b27cefae084e25752423 | quote: "status": 200
  - [5] 2026-11-11: the upload article still carries its three-step heading | capture: sha256:024eda21a5811dc3ac082489d228b98906caf9fef834da4b626ecd8f8b093bde | quote: How to upload a video in 3 steps
  - [2] 2026-11-25: the Studio help page answers the large-video upload question with a 1 GB cap | capture: sha256:56a8e65a70c6efb686f1f2df45d5bdd733bdc6da9d2eebe549eb9002f58e7531 | quote: I want to upload a large video file and play it during my livestream. What is the file size limit for video uploads? You can upload video files that are 1 GB or smaller.
  - [6] 2026-11-25: two video types cannot be deleted, by licence | capture: sha256:16cd30ce4b53942d6e4232b1fe12c974cea966c3c3f69d58e35f1367e4cec867 | quote: There's two video types that cannot be deleted, and those are the ones submitted under these licenses:
- sources:
  - [1] https://rumble.support/help/
  - [2] https://rumble.support/help/can-i-stream-to-multiple-rumble-channels-or-rumble-accounts-at-the-same-time
  - [3] https://kompozy.io/specs/rumble-file-size-limit
  - [4] https://allplatforms.io/rumble/
  - [5] https://rumble.support/help/how-to-upload-a-video
  - [6] https://rumble.support/help/delete-videos
