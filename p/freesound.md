# Freesound

> freesound.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freesound/ | JSON https://fshy.ajam.dev/api/v1/entity/freesound.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freesound — Creative Commons sound library (byte-exact originals)

- `storage/freesound-creative-commons-sound-library` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://freesound.org
- free tier: 1 GB per upload batch ('there is a file size upper limit of 1GB ... when uploading multiple files at once, the size limit is applied to the sum of all file sizes'), no published total-account cap. Volume comes from the number of sounds, not their size. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1 GB per upload | bytes: 1000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads, no metering, CDN-served. The site is explicitly built for bulk download (a Freesound Data Packs Portal exists for model-training dumps). | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per upload [1]
  - write-gated: review, the download is the master [1]
- limits note: 1 GB per upload (summed across a batch); every sound must be given one of exactly three licences and pass human moderation; sounds must be sounds, not songs. 'don't be offended if your sound gets rejected by a moderator'. That moderation queue is the throughput ceiling.
- interface detail: rest
- tooling: Public Freesound APIv2 (freesound.org/docs/api/) with OAuth2 for upload; documented endpoints for search, download, and upload. Bulk metadata via CSV/XLS upload ('Bulk description of files', unlocked after 40 sounds).
- composes with: Unlimited sounds per account x 1 GB batches. The API makes it fully scriptable, unlike every podcast host here. 40 uploads unlocks bulk describe, which removes the per-sound metadata tax that otherwise makes this unusable at volume.
- reliability: Serves the original, byte-for-byte, and says so explicitly: 'When you download the sound you get the exact same original file that was uploaded, no transcoding nor any kind of editing at all, without the artefacts'. The in-site player is a low-bitrate mp3/ogg preview, the download is the master. Data does not vanish, but a moderator can reject an upload before it is ever stored.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'there is a file size upper limit of 1GB. Note that when uploading multiple files at once, the size limit is applied to the sum of all file sizes'
  - [1] 2026-10-21: 'When you download the sound you get the exact same original file that was uploaded, no transcoding nor any kind of editing at all'
  - [1] 2026-10-21: moderation can reject; bulk describe at 40+ sounds
- sources:
  - [1] https://freesound.org/help/faq/
