# Filecoin Plus DataCap

> allocator.tech | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/allocator/ | JSON https://fshy.ajam.dev/api/v1/entity/allocator.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filecoin Plus DataCap (faucet + allocators)

- `storage/filecoin-plus-datacap` | fails-egress | evidence reported | binding per-ip-shaping | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://faucet.allocator.tech/
- free tier: 1 TiB of free DataCap per verified client, instantly, via Gitcoin Passport (score >= 20) on Optimism. Fil+ allocators can grant more. DataCap is a one-time, non-transferable credit. 'If a client needs more DataCap, they must request additional allocations.'. | unit: TiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not free, and this is what kills it. DataCap buys storage deal quality, not bandwidth. On Filecoin Onchain Cloud the retrieval layer is Filecoin Beam: 'Up to $14/TiB (≈ $0.014/GiB) egress'. FCSS: 'Retrieval is billed per TiB retrieved, with one free full-dataset retrieval a year'; unsealed HTTP retrieval returns 402 Payment Required per paid piece. | metered: yes
- identity: email
- interface: rest
- limits:
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: 64 GiB+ via GLIF (GitHub age dependent), 1 TiB via the faucet; deal duration fixed at signing; retrieval metered; FCSS minimum 6-month term.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Lotus/Boost deal-making, Singularity (github.com/data-preservation-programs/singularity), Spade for renewals, synapse-sdk for FOC, retrieval-client for FCSS.
- composes with: DataCap is per verified client and explicitly non-transferable; GLIF Verify caps re-verification at once per 30 days and grants from 64 GiB by GitHub account age. Multiple Gitcoin Passports are an identity-farming exercise, not a technical multiplier. And even a successful farm buys storage, not egress.
- reliability: DataCap grants verified storage deals up to 1 TiB of storage capacity. Data retrieval and egress are metered separately by storage providers.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TiB of free DataCap per verified client, instantly, via Gitcoin Passport (score >= 20) on Optimism. Fil+ allocators can grant more. DataCap is a one-time, non-transferable credit — 'If a client needs more DataCap, they must request additional allocations.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'provides 1 TiB of free DataCap to users looking to store verified data on the Filecoin network'; requires Gitcoin Passport score >= 20
  - [2] 2026-10-21: 'DataCap is a one-time credit and cannot be transferred between addresses. If a client needs more DataCap, they must request additional allocations.'
  - [3] 2026-10-21: 'Add-on Retrieval (Filecoin Beam) | Up to $14/TiB (≈ $0.014/GiB) egress'; 'Storage | $2.50/TiB/month/copy (minimum 2 copies)'
  - [4] 2026-10-21: 'Retrieval is billed per TiB retrieved, with one free full-dataset retrieval a year'; 'A paid piece returns 402 Payment Required'
- sources:
  - [1] https://faucet.allocator.tech/
  - [2] https://fil.org/filecoin-plus
  - [3] https://docs.filecoin.cloud/introduction/about/
  - [4] https://docs.filecoin.io/build-on-filecoin/filecoin-onchain-cloud/fcss
