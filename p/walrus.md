# Walrus Console

> walrus.xyz | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/walrus/ | JSON https://fshy.ajam.dev/api/v1/entity/walrus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Walrus

- `storage/walrus` | fails-quota | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://walrus.xyz
- free tier: No free tier on the network itself: $0.023/GB/month, billed on encoded size, which is 'about 4.5x the original blob plus a fixed 64 MB of per-blob metadata'. Lighthouse resells Walrus with a 100 MB free plan. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published free egress allowance; reads are served by Walrus storage nodes and aggregators. Cost is denominated in WAL + SUI gas per operation, so there is no 'free' path at all. | metered: yes
- identity: card
- interface: rest, cli
- limits note: 4.5x encoded-size billing + 64 MB per-blob overhead; SUI gas per blob registration; epoch-based storage duration (must be extended).
- interface detail: rest
- tooling: walrus CLI, TypeScript SDK, HTTP aggregator/publisher endpoints; Lighthouse wraps it as an IPFS-compatible layer.
- composes with: None. Paid per GB-month with a 4.5x encoding tax. 500 GB of real data costs like 2.3 TB of billing.
- reliability: The 64 MB per-blob metadata overhead is brutal for a data-science corpus of many small files: the docs' own worked example has 6 MB of 10 KiB files costing like 38.4 GB. Quilt batching mitigates but does not remove it.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier on the network itself: $0.023/GB/month, billed on encoded size, which is 'about 4.5x the original blob plus a fixed 64 MB of per-blob metadata'. Lighthouse resells Walrus with a 100 MB free plan.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'fixed, USD-denominated storage cost of $0.023/GB/month'; 'The encoded size is about 4.5x the original blob plus a fixed 64 MB of per-blob metadata'
  - [2] 2026-10-21: Walrus Free plan 'Total Storage: 100 MB'
- sources:
  - [1] https://docs.wal.app/docs/system-overview/storage-costs
  - [2] https://www.lighthouse.storage/pricing

## Walrus Console (Walrus Foundation, Oct 2026 launch)

- `storage/walrus-console` | fails-quota | evidence reported | binding none | category web3-storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://walrus.xyz/products/walrus-console/
- free tier: 5 GB free. Launched 2026-10-07 with 'Get started today with 5GB free'. No larger free tier is published. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: One week old at time of research. Storage is leased time, so 'free 5 GB' and 'kept forever' are not the same claim. | source: [1] | note: not stated
- egress: Reads via the Console API/MCP; the underlying Walrus network serves blobs from storage nodes. No egress meter published. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: Fails-quota at 5 GB by two orders of magnitude. Retention is epoch-based, so data expires unless renewed. A retention-clamped model at the protocol level.
- interface detail: rest
- tooling: Genuinely good for an agent workflow: API keys plus an MCP server that plugs into Claude Code, Codex and Cursor; 'Agent Storage Loop' SDK for batched small writes with durability confirmation. Encrypted by default, per-file on-chain fingerprint.
- composes with: The paid path is buying WAL and paying per epoch (storage is leased in time units, not bytes-forever). So cost scales with retention period × size, which is the opposite of an archive.
- reliability: One week old at time of research. Storage is leased time, so 'free 5 GB' and 'kept forever' are not the same claim.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free. Launched 2026-10-07 with 'Get started today with 5GB free'. No larger free tier is published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: opened: 'Get started today with 5GB free'; published 07 Oct 2026; 'Every file gets a cryptographic fingerprint recorded onchain'; MCP integration with Claude Code, Codex, Cursor; 'encryption and renewals in one place' (note: renewals).
- sources:
  - [1] https://walrus.xyz/blog/introducing-walrus-console/
