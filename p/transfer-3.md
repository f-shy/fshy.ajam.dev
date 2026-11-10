# Transfer.zip

> transfer.zip | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transfer-3/ | JSON https://fshy.ajam.dev/api/v1/entity/transfer-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Transfer.zip

- `storage/transfer-zip` | fails-quota | evidence reported | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://transfer.zip
- free tier: Quick Transfers are free and have NO file-size limit, but they are ephemeral P2P: 'deleted automatically when either party closes the transfer window'. Persistent storage starts at Starter $6/mo (200 GB storage, 200 GB/file, 14 days). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 200 GB/file | bytes: 200000000000 | source: [1] | note: not stated
- retention: until the instance is recycled; not persistent | source: [1] | note: not stated
- egress: free for Quick Transfer (browser-to-browser, so their egress is minimal). | metered: no
- identity: card
- interface: unknown
- limits:
  - per-object-cap (binding): 200 GB/file [1]
- limits note: per-object-cap: none on Quick Transfer, 200 GB on Starter. Retention: zero on Quick Transfer (session-bound); 14 days on Starter paid. 'Unlimited free file size' on the marketing page refers to the P2P mode.
- interface detail: wrapper-only
- tooling: Open source (github.com/robinkarlberg/transfer.zip-web, 1,514 stars) and self-hostable. Which means you can run the whole service on your own box, but that is your storage, not theirs.
- composes with: The free path is a WebRTC pipe, so it multiplies to nothing durable. Self-hosting it is a legitimate option only if you already have the disk.
- reliability: Its own terms are unambiguous that Quick Transfers are ephemeral and that paid plans are a pool of SIMULTANEOUS storage, not cumulative. Reading 'unlimited free file size' as a storage quota would be a mistake.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Quick Transfers are free and have NO file-size limit, but they are ephemeral P2P: 'deleted automatically when either party closes the transfer window'. Persistent storage starts at Starter $6/mo (200 GB storage, 200 GB/file, 14 days).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Quick Transfers are ephemeral and are deleted automatically when either party closes the transfer window'
  - [2] 2026-10-21: Starter $6/mo: Max file size 200 GB, expiry 14 days, storage 200 GB
- sources:
  - [1] https://transfer.zip/legal/terms-and-conditions
  - [2] https://transfer.zip/pricing
