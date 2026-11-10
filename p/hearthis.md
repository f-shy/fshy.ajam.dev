# hearthis.at

> hearthis.at | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hearthis/ | JSON https://fshy.ajam.dev/api/v1/entity/hearthis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hearthis.at — free tier

- `storage/hearthis-at-free-tier` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hearthis.at
- free tier: 400 MB per week, reset Sunday 19:00 CET: 'Upload up to 400 MB of music each week for free' and 'Your weekly upload quota of 400 MB is automatically reset every Sunday at 7:00 pm (CET)'. ~1.7 GB/month recurring, uncapped total accumulation. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free streaming; no per-GB egress charge. 'Podcast and RSS Feed for your Profile and Sets of music' is included on the free side, which is unusual. | metered: no
- identity: email
- interface: unknown
- limits note: 400 MB/week on Free; transcode to a single house format. 'We convert all uploaded tracks to a unified streaming format: 192 kbit/s, constant bitrate (CBR), joint stereo'; Premium can pick bitrate and gets 'original (mp3 only)' play quality.
- interface detail: wrapper-only
- tooling: No API. Web upload plus a 'Sounds import from sharehosters' feature (pull from a sharehoster URL rather than uploading through the browser). That is the automation-adjacent path.
- composes with: 400 MB/week x N accounts, accumulating indefinitely (the quota resets, storage does not expire). ~1.7 GB/month/account at zero cost, so 10 accounts is ~17 GB/month and 100 accounts ~170 GB/month. Throughput, not quota, is the constraint.
- reliability: RE-ENCODES to 192 kbps CBR joint stereo for everyone on Free ('This ensures compatibility across all devices. Premium members can set their own bitrate preferences'). The 'original (mp3 only)' option in the feature list is a Premium/paid capability, so on the free tier what comes out is the 192k transcode, not your file.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Upload up to 400 MB of music each week for free'; 'Podcast and RSS Feed for your Profile and Sets of music'; format list 'MP3, WAV, AIF, M4A, AAC, OGG, FLAC, WMA'
  - [2] 2026-10-21: 'When is the upload limit reset? (400 MB) Free accounts — Your weekly upload quota of 400 MB is automatically reset every Sunday at 7:00 pm (CET)'
  - [2] 2026-10-21: 'Why do you transcode uploaded music? We convert all uploaded tracks to a unified streaming format: 192 kbit/s, constant bitrate (CBR), joint stereo'
- sources:
  - [1] https://hearthis.at/
  - [2] https://hearthis.at/faq/
