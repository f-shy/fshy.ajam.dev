# Bandcamp

> bandcamp.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bandcamp/ | JSON https://fshy.ajam.dev/api/v1/entity/bandcamp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bandcamp — free artist account

- `storage/bandcamp-free-artist-account` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bandcamp.com
- free tier: 291 MB per track to start ('It starts out at 291MB per track .. Once you've made a few sales through Bandcamp (totaling $20 USD or more), we increase the max per-track upload size to 600 megs'), and crucially 'There is no limit on the size of albums'. So total capacity is unbounded at 291 MB x unlimited tracks. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free streaming and free downloads to fans; Bandcamp takes 15% of sales (10% after $5k) but there is no storage or egress bill, and a $0-priced release generates none of that. | metered: no
- identity: card
- interface: unknown
- limits note: Audio must be 'at least 16-bit, 44.1 kHz lossless files (WAV, AIFF, or FLAC), in stereo (no mono- or multi-channel audio)'. So no MP3 uploads at all. Pro ($10/mo, not free) raises the per-track cap to 2 GB and adds video (500 MB). Free accounts can't upload video.
- interface detail: wrapper-only
- tooling: No public API, no bulk uploader. Web album editor only ('Click + add in the top toolbar'). This is the weakest tooling story in the slot.
- composes with: Unlimited albums per artist account x unlimited tracks per album x 291 MB per track. The 291 MB cap is per track, and an album has no cap, so a 20-track album is ~5.8 GB before you need anything else.
- reliability: Lossless masters are kept and fans who buy get the original format; streams are transcoded mp3. The lossless-only requirement is actually a positive for this use case (nothing is lossy-transcoded on the way in), but the 'no multi-channel / no mono' rule rejects perfectly good files, and a release is public the moment it's published. There is no private/unlisted storage mode.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'It starts out at 291MB per track'; 'we increase the max per-track upload size to 600 megs'; 'There is no limit on the size of albums'; 'up to 2 GB by subscribing to Bandcamp Pro'
  - [2] 2026-10-21: 'Your audio files must be at least 16-bit, 44.1 kHz lossless files (WAV, AIFF, or FLAC), in stereo (no mono- or multi-channel audio)'
  - [3] 2026-10-21: 'The max upload size for videos is 500MB' (paid tier)
- sources:
  - [1] https://get.bandcamp.help/en/articles/15263336-what-s-the-maximum-upload-size
  - [2] https://get.bandcamp.help/en/articles/15263088-how-do-i-upload-music
  - [3] https://get.bandcamp.help/en/articles/15263341-what-is-the-maximum-video-upload-size
