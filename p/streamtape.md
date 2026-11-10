# Streamtape

> streamtape.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamtape/ | JSON https://fshy.ajam.dev/api/v1/entity/streamtape.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Streamtape

- `storage/streamtape` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://streamtape.com
- free tier: 'Unlimited Storage — Upload as many Videos as you wish. Active files will be saved'. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No stated bandwidth cap; 'unlimited upload/download speed' claimed. Ad-monetised, so egress is the product. | metered: no
- identity: email
- interface: rest
- limits note: Video formats only; files are encoded/re-encoded on ingest (lossy for anything not already a video). 'Active files' only are kept. Inactive files are purged. Downloads require a generated ticket.
- interface detail: rest
- tooling: Documented API at https://streamtape.com/api with account info, download ticket, get download link, file info and upload endpoints. Widely integrated into upload bots.
- composes with: Free accounts x unlimited storage x unlimited files. Video-only in practice (it is a streaming host); the useful play is media/checkpoint shards, not raw datasets.
- reliability: Re-encoding destroys byte fidelity, so it cannot store arbitrary binaries. Ticket-gated downloads and ad-injected players make unattended fetch fragile. Activity requirement is unquantified on the pages read.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Unlimited Storage ... Active files will be saved on a system of safe and secured servers'
  - [2] 2026-10-21: API sections: Account Infos, generate Download Ticket, get Download Link, check File Info, Upload
  - [1] 2026-10-21: probe: GET -> 200
- sources:
  - [1] https://streamtape.com/
  - [2] https://streamtape.com/api
