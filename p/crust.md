# Crust Network

> crust.network | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crust/ | JSON https://fshy.ajam.dev/api/v1/entity/crust.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Crust Network (free Web3Auth IPFS gateway + on-chain pinning)

- `storage/crust-network` | fails-egress | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wiki.crust.network/docs/en/build101
- free tier: Gateway writes are described as 'free' but need a signature; the storage quota itself comes from a Discord channel, not a published number: 'Get free storage quota: 1. Join Crust discord 2. Follow the pinned message on 📦free-storage channel'. Default storage order term is 6 months. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free gateways list is published (github.com/crustio/ipfsscan lib/constans.ts, e.g. https://ipfs-gw.decloud.foundation). No bandwidth meter documented. | metered: no | source: [2]
- identity: email
- interface: rest, rclone
- limits note: per-object-cap: not stated. retention: 'The default storage time for a single transaction(order) is 6 months'; extension requires prepaying into a pool. request-rate: unknown. Signature gate is the practical binding constraint.
- interface detail: rest
- tooling: IPFS HTTP API-compatible authenticated gateway; also a standard IPFS Pinning Service endpoint usable cross-chain. rclone can read IPFS via the gateway; writes need the W3Auth signature flow.
- composes with: Quota is granted per Discord/on-chain identity and the order is an on-chain transaction, so chaining means many funded Crust accounts. Closer to a staking scheme than a free tier.
- reliability: Write path is signature-gated; unauthenticated PUT returns 401 and reads of unknown CIDs return 403, so the gateway is not an open drop.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Gateway writes are described as 'free' but need a signature; the storage quota itself comes from a Discord channel, not a published number: 'Get free storage quota: 1. Join Crust discord 2. Follow the pinned message on 📦free-storage channel'. Default storage order term is 6 months.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Crust provides a web3-oriented gateway ... for free and 100% compatible with standard IPFS HTTP interfaces'; 'The default storage time for a single transaction(order) is 6 months'
  - [3] 2026-10-21: probe: POST -F file=@probe -> 401 {"error":{"reason":"UNAUTHORIZED","details":"Empty Signature"}}
  - [4] 2026-10-21: probe: GET cid> -> 403
- sources:
  - [1] https://wiki.crust.network/docs/en/build101
  - [2] https://ipfs-gw.decloud.foundation
  - [3] https://ipfs-gw.decloud.foundation/api/v0/add
  - [4] https://ipfs-gw.decloud.foundation/ipfs/<valid

## Crust Network DSM

- `storage/crust-network-dsm` | fails-quota | evidence inferred | binding none | category contributed storage - decentralised pinning market
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://wiki.crust.network/docs/en/DSM
- free tier: storage orders placed on-chain, each held for six months; the top four nodes submitting proofs share that file's reward | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: retrieval incentivised separately; no free allowance published | metered: yes
- identity: card | detail: card
- interface: cli
- limits note: Storage orders specify fixed 6-month durations. No free tier is provided, and public capacity metric endpoints on the homepage return unpopulated values.
- interface detail: IPFS CID-based orders; Crust apps
- tooling: crust CLI, IPFS, apps.crust.network
- composes with: IPFS-compatible, so any IPFS gateway can read it
- reliability: Reward goes only to the top four proof submitters per file, so payout is a race; unverified capacity reporting.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: storage orders placed on-chain, each held for six months; the top four nodes submitting proofs share that file's reward
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Currently, each storage order would be stored on the Crust Network for six months'; 'Any node that submits corresponding storage proof will be added to the payout queue ... the top four nodes in the queue will get the reward of this file's reward'
  - [2] 2026-10-21: capacity and node counters rendered as '0 TB' and '0'; no pricing table published
- sources:
  - [1] https://wiki.crust.network/docs/en/DSM
  - [2] https://crust.network/
