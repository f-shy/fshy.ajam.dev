# Rumble

> rumble.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rumble/ | JSON https://fshy.ajam.dev/api/v1/entity/rumble.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rumble

- `storage/rumble` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-11T03:34:15.636Z (live) | stale on 2026-11-19
- url https://rumble.com
- free tier: No published total storage cap. 15 GB per file standard, 30 GB for Premium/monetised channels; up to 8 hours duration. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 15 GB per file | bytes: 15000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Rumble serves its own CDN, no egress billing. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 15 GB per file [1]
  - per-object-cap (binding): 15 GB/file [1]
- limits note: 15 GB/file is mid-tier. Upload is web-form only. This is the automation blocker, since yt-dlp solves retrieval but nothing solves programmatic upload.
- interface detail: rest
- tooling: yt-dlp `Rumble`, `RumbleChannel`, `RumbleEmbed` extractors (verified present). No public upload API; upload is web-only.
- composes with: Unlimited files x unlimited accounts at 15 GB each. No documented daily cap, which is unusual and useful.
- reliability: Direct FAQ documentation was unreachable during testing on 2026-10-21. The 15 GB maximum video upload figure is reported in third-party platform documentation.
- notes: unverified: https://rumble.support/help/how-to-upload-a-video answered HTTP 200 on 2026-11-11 through the environment proxy; its text carries a three-step upload heading, an image, a link reading https://rumble.com/upload and a licence note, and states no file-size or duration limit.
- evidence:
  - [2] 2026-05-22: 'Rumble max file size: 15 GB per upload' (third-party, claims last verified 2026-05-22)
  - [3] 2026-10-21: 'Max File Size 15 GB (standard) / 30 GB (Premium/monetised)'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors` -> Rumble, RumbleChannel, RumbleEmbed present
  - withheld 2026-10-21: unverified: rumble.com/faq and rumble.com/pricing returned 404/410/504 — blocked/unavailable, no first-party page read
  - [4] 2026-11-09: the linked upload article is a three-step guide and states no file-size or duration limit | capture: sha256:c84706deb4bfae5e473b39e91312af4f9e66437267624c33590c1502a48bcf37 | quote: How to upload a video in 3 steps
  - probe:https://rumble.support/help/how-to-upload-a-video 2026-11-11: the page answered HTTP 200 on 2026-11-11 and the 235507-byte body was read in full | capture: sha256:8a974d730ba08f4e2d9573da701dbd565b3b387a3239b27cefae084e25752423 | quote: "status": 200
  - [4] 2026-11-11: the upload article still carries its three-step heading | capture: sha256:024eda21a5811dc3ac082489d228b98906caf9fef834da4b626ecd8f8b093bde | quote: How to upload a video in 3 steps
- sources:
  - [1] https://rumble.support/help/
  - [2] https://kompozy.io/specs/rumble-file-size-limit
  - [3] https://allplatforms.io/rumble/
  - [4] https://rumble.support/help/how-to-upload-a-video
