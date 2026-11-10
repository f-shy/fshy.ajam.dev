# Lighthouse

> lighthouse.storage | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lighthouse/ | JSON https://fshy.ajam.dev/api/v1/entity/lighthouse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lighthouse (Filecoin/IPFS pinning)

- `storage/lighthouse` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lighthouse.storage/pricing
- free tier: Filecoin plans, Free: 'Total Storage: 5 GB' (IPFS + Filecoin). Walrus plans, Free: 'Total Storage: 100 MB'. Next tier is $12/month for 500 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: not stated on the pricing page; gateway is ipfs-gw-style and historically unmetered, but there is no published allowance to quote. | metered: no
- identity: institution
- interface: rest, rclone
- limits note: per-object-cap: not stated. quota-cap: 5 GB hard. retention: Filecoin deals are duration-based; free-plan renewal path not documented.
- interface detail: rest
- tooling: IPFS pinning API + Filecoin deals; SDKs exist. No rclone backend.
- composes with: 5 GB x unlimited free accounts, each requiring an API key; the jump from 5 GB free to 500 GB at $12 means the free tier is deliberately a demo, not a base to multiply.
- reliability: Free plan omits encryption, IPNS and migration support that paid plans have, and the Walrus sub-product free tier is only 100 MB.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Filecoin plans, Free: 'Total Storage: 5 GB' (IPFS + Filecoin). Walrus plans, Free: 'Total Storage: 100 MB'. Next tier is $12/month for 500 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free ... Total Storage: 5 GB, IPFS: Yes, Filecoin: Yes'; 'Walrus ... Free ... Total Storage: 100 MB'
- sources:
  - [1] https://lighthouse.storage/pricing
