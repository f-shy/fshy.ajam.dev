# Rumble

> rumble.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rumble/ | JSON https://fshy.ajam.dev/api/v1/entity/rumble.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rumble

- `storage/rumble` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-19
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
- notes: the same as the free tier
- evidence:
  - [2] 2026-05-22: 'Rumble max file size: 15 GB per upload' (third-party, claims last verified 2026-05-22)
  - [3] 2026-10-21: 'Max File Size 15 GB (standard) / 30 GB (Premium/monetised)'
  - withheld 2026-10-21: probe: `yt-dlp --list-extractors` -> Rumble, RumbleChannel, RumbleEmbed present
  - withheld 2026-10-21: unverified: rumble.com/faq and rumble.com/pricing returned 404/410/504 — blocked/unavailable, no first-party page read
- sources:
  - [1] https://rumble.support/help/
  - [2] https://kompozy.io/specs/rumble-file-size-limit
  - [3] https://allplatforms.io/rumble/
