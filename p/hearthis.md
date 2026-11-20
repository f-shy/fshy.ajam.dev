# hearthis.at

> hearthis.at | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hearthis/ | JSON https://fshy.ajam.dev/api/v1/entity/hearthis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hearthis.at — free tier

- `storage/hearthis-at-free-tier` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:18.130Z (live) | stale on 2026-11-25
- url https://hearthis.at
- free tier: Free accounts can upload up to 400 MB per week. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Free accounts upload MP3, M4A, OGG and WMA files of up to 90 minutes. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free streaming; no per-GB egress charge. 'Podcast and RSS Feed for your Profile and Sets of music' is included on the free side, which is unusual. | metered: no
- identity: email | detail: Your name Your email address Your password Create Account
- interface: unknown
- limits note: Free accounts have a total storage limit of 5.000 MB (5 GB).
- interface detail: wrapper-only
- tooling: Uploading and changing your own content through the API needs a Premium account.
- composes with: the same as limits note
- reliability: RE-ENCODES to 192 kbps CBR joint stereo for everyone on Free ('This ensures compatibility across all devices. Premium members can set their own bitrate preferences'). The 'original (mp3 only)' option in the feature list is a Premium/paid capability, so on the free tier what comes out is the 192k transcode, not your file.
- notes: the same as limits note
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Upload up to 400 MB of music each week for free'; 'Podcast and RSS Feed for your Profile and Sets of music'; format list 'MP3, WAV, AIF, M4A, AAC, OGG, FLAC, WMA'
  - [2] 2026-10-21: 'When is the upload limit reset? (400 MB) Free accounts — Your weekly upload quota of 400 MB is automatically reset every Sunday at 7:00 pm (CET)'
  - [2] 2026-10-21: 'Why do you transcode uploaded music? We convert all uploaded tracks to a unified streaming format: 192 kbit/s, constant bitrate (CBR), joint stereo'
  - [2] 2026-11-09: The FAQ states the allowance this record relies on. | capture: sha256:454877cb8056f06c7a2cb845ce395cecfd592bec4b19ae31152073281eeea2d8 | quote: Free accounts can upload up to 400 MB per week.
  - [2] 2026-11-09: The FAQ states a total storage limit, so the old uncapped-accumulation claim is wrong. | capture: sha256:454877cb8056f06c7a2cb845ce395cecfd592bec4b19ae31152073281eeea2d8 | quote: Free accounts have a total storage limit of 5.000 MB (5 GB).
  - [2] 2026-11-09: The FAQ states that API uploads need a Premium account. | capture: sha256:454877cb8056f06c7a2cb845ce395cecfd592bec4b19ae31152073281eeea2d8 | quote: Uploading and changing your own content through the API needs a Premium account.
  - [2] 2026-11-09: The signup form states the required fields. | capture: sha256:454877cb8056f06c7a2cb845ce395cecfd592bec4b19ae31152073281eeea2d8 | quote: Your name Your email address Your password Create Account
  - [2] 2026-11-09: The FAQ states the per-file duration limit. | capture: sha256:454877cb8056f06c7a2cb845ce395cecfd592bec4b19ae31152073281eeea2d8 | quote: Free accounts upload MP3, M4A, OGG and WMA files of up to 90 minutes.
- sources:
  - [1] https://hearthis.at/
  - [2] https://hearthis.at/faq/
