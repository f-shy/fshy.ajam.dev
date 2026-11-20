# Odysee

> odysee.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/odysee/ | JSON https://fshy.ajam.dev/api/v1/entity/odysee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Odysee / LBRY

- `storage/odysee-lbry` | qualifies | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:27.600Z (live) | stale on 2026-11-25
- url https://odysee.com
- free tier: Odysee uploads are restricted to 16 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Odysee uploads are restricted to 16 GB. | bytes: 16000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Files are content-addressed blobs served by the LBRY DHT/reflectors and by Odysee's CDN; retrieval by hash is not metered. | metered: no
- identity: email | detail: Email and password
- interface: rest
- limits:
  - per-object-cap (binding): 16 GB per file [1]
- limits note: 16 GB per file is the real ceiling; no per-day upload cap documented. Every publish needs an LBC deposit, so a large library costs a real (small) crypto balance up front and must be re-staked to keep claims alive.
- interface detail: rest
- tooling: yt-dlp `lbry` extractor (verified present). Odysee JSON-RPC at api.na-backend.odysee.com (`resolve`, `claim_search`). LBRY Desktop hosts blobs locally under lbrynet/blob.
- composes with: Unlimited claims per channel x unlimited channels x unlimited accounts. Because the object is a plain blob, there is no video-duration ceiling to fight. The only cap is 16 GB/file, so capacity = unlimited files x 16 GB.
- reliability: This is the only candidate here that stores the original bytes, but the platform is visibly decaying in 2026. Community 'collapse watch' posts and a Sept 2026 outage report; LBRY Inc. wound down. Treat as a live archive with a short expected half-life.
- notes: the same as the free tier
- evidence note: the file-selection page states the 16 GB upload limit
- evidence:
  - [1] 2026-10-21: 'Odysee uploads are restricted to 16 GB'
  - [2] 2026-10-21: 'you can also publish files up to 4 GB from the web at Odysee.com'; 'a minimum of 0.0001 LBC deposit'
  - withheld 2026-10-21: probe: POST api.na-backend.odysee.com claim_search -> value.source = {hash, sd_hash, size: 205035588, media_type: video/mp4} — the claim points at one content-addressed blob, not a set of renditions
  - [3] 2026-10-21: 'the file isn't actually being uploaded to Odysee. It's being uploaded to the LBRY network'
  - [1] 2026-11-09: an Odysee upload is capped at 16 GB | capture: sha256:1bf307f4226e04a131a30a5b88ae67bdd3f44c5575a8822c5259270004fba405 | quote: Odysee uploads are restricted to 16 GB.
  - [4] 2026-11-09: the sign-up form asks for an email address and a password | capture: sha256:fe42fe4d1c2126caa8a822be8c05fe44d96793fda595a6a700f78bd98d0c3fab | quote: Email Password
- sources:
  - [1] https://help.odysee.tv/category-uploading/category-fileuploads/fileselection/
  - [2] https://lbry.com/faq/how-to-publish
  - [3] https://help.odysee.tv/category-blockchain/overview/
  - [4] https://odysee.com/$/signup
