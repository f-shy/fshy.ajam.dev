# Wormhole

> wormhole.app | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wormhole/ | JSON https://fshy.ajam.dev/api/v1/entity/wormhole.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wormhole

- `storage/wormhole` | fails-quota | evidence reported | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wormhole.app
- free tier: Up to 10 GB per send. Only the first 5 GB is actually stored server-side; anything above 5 GB is PEER-TO-PEER and requires the sender's tab to stay open. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 5 GB | bytes: 5000000000 | source: [1] | note: not stated
- retention: Retention: 24 hours hard ('Files are permanently deleted from the server after 24 hours') | days: 1 | source: [1] | note: not stated
- egress: free while it exists; P2P above 5 GB routes around their egress entirely. | metered: no
- identity: anonymous
- interface: unknown
- limits:
  - retention-clamped: Retention: 24 hours [1]
  - retention-clamped: deleted from the server after 24 hours [1]
  - per-object-cap (binding): per-object-cap: 5 GB [1]
- limits note: per-object-cap: 5 GB stored / 10 GB total via P2P. Retention: 24 hours hard ('Files are permanently deleted from the server after 24 hours'). Client-side AES-128-GCM.
- interface detail: none
- tooling: No public API. Only the crypto layer is open source (github.com/webtorrent/wormhole-crypto).
- composes with: 5 GB stored x 24 hours. Nothing compounds. Files are permanently deleted after 24 hours and the service has no account model.
- reliability: The 24-hour hard delete plus P2P-above-5GB means the service has no durable component at all.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Up to 10 GB per send. Only the first 5 GB is actually stored server-side; anything above 5 GB is PEER-TO-PEER and requires the sender's tab to stay open.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'For files up to 5 GB, Wormhole stores your files on our servers for 24 hours. For files larger than 5 GB, Wormhole uses peer-to-peer transfer'
  - [1] 2026-10-21: 'Files are permanently deleted from the server after 24 hours'
- sources:
  - [1] https://wormhole.app/faq
