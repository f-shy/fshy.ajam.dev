# Odysee

> odysee.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/odysee/ | JSON https://fshy.ajam.dev/api/v1/entity/odysee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Odysee / LBRY

- `storage/odysee-lbry` | qualifies | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://odysee.com
- free tier: No storage quota at all. 16 GB per file via the Odysee uploader (4 GB from the plain lbry.com web form). Unlimited claims. Storage cost is a one-time LBC claim deposit, minimum 0.0001 LBC. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 16 GB per file | bytes: 16000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Files are content-addressed blobs served by the LBRY DHT/reflectors and by Odysee's CDN; retrieval by hash is not metered. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 16 GB per file [1]
- limits note: 16 GB per file is the real ceiling; no per-day upload cap documented. Every publish needs an LBC deposit, so a large library costs a real (small) crypto balance up front and must be re-staked to keep claims alive.
- interface detail: rest
- tooling: yt-dlp `lbry` extractor (verified present). Odysee JSON-RPC at api.na-backend.odysee.com (`resolve`, `claim_search`). LBRY Desktop hosts blobs locally under lbrynet/blob.
- composes with: Unlimited claims per channel x unlimited channels x unlimited accounts. Because the object is a plain blob, there is no video-duration ceiling to fight. The only cap is 16 GB/file, so capacity = unlimited files x 16 GB.
- reliability: This is the only candidate here that stores the original bytes, but the platform is visibly decaying in 2026. Community 'collapse watch' posts and a Sept 2026 outage report; LBRY Inc. wound down. Treat as a live archive with a short expected half-life.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Odysee uploads are restricted to 16 GB'
  - [2] 2026-10-21: 'you can also publish files up to 4 GB from the web at Odysee.com'; 'a minimum of 0.0001 LBC deposit'
  - withheld 2026-10-21: probe: POST api.na-backend.odysee.com claim_search -> value.source = {hash, sd_hash, size: 205035588, media_type: video/mp4} — the claim points at one content-addressed blob, not a set of renditions
  - [3] 2026-10-21: 'the file isn't actually being uploaded to Odysee. It's being uploaded to the LBRY network'
- sources:
  - [1] https://help.odysee.tv/category-uploading/category-fileuploads/fileselection/
  - [2] https://lbry.com/faq/how-to-publish
  - [3] https://help.odysee.tv/category-blockchain/overview/
