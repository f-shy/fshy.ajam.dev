# Spreaker

> spreaker.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spreaker/ | JSON https://fshy.ajam.dev/api/v1/entity/spreaker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spreaker — Free plan

- `storage/spreaker-free-plan` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.spreaker.com
- free tier: One podcast, unlimited episodes: 'The free plan allows users to have one podcast with an unlimited number of episodes.' No total-storage or per-file figure is published on the plans page or in the free-plan announcement. The plans page renders unlimited episodes but no storage number. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered in the sense that no bandwidth cap or per-GB price is published for Free; the constraint is episode count and the house format. | metered: no
- identity: email
- interface: unknown
- limits note: Everything is transcoded into 'Spreaker Storage Format'. 'All audio that we stream must be in the same format: for this reason, sometimes it is necessary to transcode the audio files that are uploaded'. Upload lossless and it will not be double-transcoded, but it is still re-encoded once into the house format.
- interface detail: wrapper-only
- tooling: No public upload API; dashboard and mobile app.
- composes with: 1 podcast x unlimited episodes x N accounts. Storage ceiling is implicit (whatever the house transcode produces) rather than stated.
- reliability: Definitively re-encodes. Spreaker's own help tells you to upload WAV/FLAC 'so they will not be transcoded' twice, which confirms the platform stores a single normalised format, not your master. No storage number published anywhere means the real ceiling is discoverable only by hitting it.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'The free plan allows users to have one podcast with an unlimited number of episodes.'
  - [2] 2026-10-21: 'All audio that we stream must be in the same format: for this reason, sometimes it is necessary to transcode the audio files that are uploaded'
  - [3] 2026-10-21: 'Craft unlimited episodes across a single podcast'
- sources:
  - [1] https://help.spreaker.com/en/articles/7035244-how-many-podcasts-can-i-have-on-my-plan
  - [2] https://help.spreaker.com/en/articles/3810635-how-do-i-keep-my-audio-file-s-quality-when-uploading-it-to-spreaker
  - [3] https://news.spreaker.com/27153-the-free-plan
