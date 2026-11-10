# Ethereum blobs

> chainscorelabs.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chainscorelabs/ | JSON https://fshy.ajam.dev/api/v1/entity/chainscorelabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ethereum blobs (EIP-4844) as a storage layer

- `storage/ethereum-blobs-as-a-storage-layer` | fails-egress | evidence reported | binding per-object-cap | category blockchain
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://chainscorelabs.com/da
- free tier: No free tier. Live cost at time of check: $0.012 per MB as blobs (vs $11.01/MB as calldata). 128 KB per blob package, separate blob fee market. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 128 KB per blob | bytes: 128000 | source: [1] | note: not stated
- retention: ~18-day retention; per-block blob count cap; cost floats with the blob fee market. | days: 18 | source: [1] | note: not stated
- egress: Free to read while data exists, but data is pruned by consensus nodes after ~18 days. Retrieval after that depends on third-party archival indexers (Blobscan etc.), not on Ethereum. | metered: no
- identity: card
- interface: rest
- limits:
  - per-object-cap (binding): 128 KB per blob [1]
- limits note: ~18-day retention; per-block blob count cap; cost floats with the blob fee market.
- interface detail: rest
- tooling: blobkit.org (TypeScript SDK for blob transactions), Blobscan API, standard Ethereum JSON-RPC.
- composes with: Multiply cost, not capacity: 10 TiB/month = 10,485,760 MB x $0.012 = ~$125,800/month, and the data expires in 18 days regardless of payment.
- reliability: Data is intentionally ephemeral by protocol design. The network is built to forget it after the DA window.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier. Live cost at time of check: $0.012 per MB as blobs (vs $11.01/MB as calldata). 128 KB per blob package, separate blob fee market.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'At 14:49 UTC, posting 1 MB costs ... $0.012 on Ethereum blobs'; 'kept for about 18 days'; 'About 887 times cheaper ... than calldata'
  - [2] 2026-10-21: DA machinery description confirming blobs are sampled/expired, not archived
- sources:
  - [1] https://chainscorelabs.com/da
  - [2] https://ethereum.org/developers/docs/data-availability/

## ethstorage / evmfs / on-chain calldata file systems

- `storage/ethstorage-evmfs-on-chain-calldata-file-systems` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://chainscorelabs.com/da
- free tier: None reachable: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live. 10 TiB would be ~$115 million. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115…
  - [2] 2026-10-21: cited as the basis of the rejection: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115 million
  - [3] 2026-10-21: cited as the basis of the rejection: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115 million
- sources:
  - [1] https://chainscorelabs.com/da
  - [2] https://docs.ethstorage.io/dapp-developer-guide/tutorials/upload-your-file-folder-with-ethfs-cli
  - [3] https://evmfs.app/
