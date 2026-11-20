# Ethereum blobs

> chainscorelabs.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chainscorelabs/ | JSON https://fshy.ajam.dev/api/v1/entity/chainscorelabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ethereum blobs (EIP-4844) as a storage layer

- `storage/ethereum-blobs-as-a-storage-layer` | fails-egress | evidence reported | binding per-object-cap | category blockchain
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:31.792Z (live) | stale on 2026-12-04
- url https://chainscorelabs.com/da
- free tier: No free tier. Live cost at time of check: $0.012 per MB as blobs (vs $8.74/MB as calldata). 128 KB per blob package, separate blob fee market. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
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
- notes: No free tier. Live cost at time of check: $0.012 per MB as blobs (vs $11.01/MB as calldata). 128 KB per blob package, separate blob fee market.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier. Live cost at time of check: $0.012 per MB as blobs (vs $11.01/MB as calldata). 128 KB per blob package, separate blob fee market.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'At 14:49 UTC, posting 1 MB costs ... $0.012 on Ethereum blobs'; 'kept for about 18 days'; 'About 887 times cheaper ... than calldata'
  - [2] 2026-10-21: DA machinery description confirming blobs are sampled/expired, not archived
  - [1] 2026-11-19: current live cost is $0.012 per MB as blobs and $8.74 per MB as calldata | capture: sha256:beb266e0223d25fb5b033b2b3d5bfcef4b108e4d790b2ea4d103b3e7b1c15f06 | quote: About 751 times cheaper right now: 1 MB costs $0.012 as blobs and $8.74 as calldata. Blobs have their own fee market and are pruned after about 18 days, while calldata is kept forever and priced as execution gas.
  - [1] 2026-11-19: current live blob cost is $0.012 per MB | capture: sha256:beb266e0223d25fb5b033b2b3d5bfcef4b108e4d790b2ea4d103b3e7b1c15f06 | quote: At 11:27 UTC, posting 1 MB costs $0.00015 on Avail, $0.0016 on NEAR DA, $0.012 on Ethereum blobs, $0.013 on Celestia.
  - [1] 2026-11-19: a blob is a 128 KB package of data | capture: sha256:beb266e0223d25fb5b033b2b3d5bfcef4b108e4d790b2ea4d103b3e7b1c15f06 | quote: A blob is a 128 KB package of data that a rollup attaches to an Ethereum transaction, added by EIP-4844 in March 2024.
  - [1] 2026-11-19: blobs are pruned after about 18 days | capture: sha256:beb266e0223d25fb5b033b2b3d5bfcef4b108e4d790b2ea4d103b3e7b1c15f06 | quote: Blobs have their own fee market and are pruned after about 18 days, while calldata is kept forever and priced as execution gas.
- sources:
  - [1] https://chainscorelabs.com/da
  - [2] https://ethereum.org/developers/docs/data-availability/

## ethstorage / evmfs / on-chain calldata file systems

- `storage/ethstorage-evmfs-on-chain-calldata-file-systems` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:35.941Z (live) | stale on 2026-12-04
- url https://chainscorelabs.com/da
- free tier: None. Files are stored on-chain in FlatDirectory contracts, billed per transaction with calldata or blob upload types; the DA comparison page prices calldata at 9.98 USD per MB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live. 10 TiB would be ~$115 million.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115…
  - [2] 2026-10-21: cited as the basis of the rejection: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115 million
  - [3] 2026-10-21: cited as the basis of the rejection: Real systems (EthStorage mainnet chain 333, FlatDirectory contracts; EVMFS 20 KB chunks per call) but pricing is per-calldata-byte. Calldata is $11.01/MB live — 10 TiB would be ~$115 million
  - [1] 2026-11-19: calldata is priced per MB as execution gas and retained indefinitely | capture: sha256:8348a13205388c3a0c4163054346a85395fc3e743d8c6c6dcb5dadf0c2cdd342 | quote: About 818 times cheaper right now: 1 MB costs $0.012 as blobs and $9.98 as calldata. Blobs have their own fee market and are pruned after about 18 days, while calldata is kept forever and priced as execution gas.
  - [2] 2026-11-19: uploads are billed on-chain via calldata or blob transaction types, not a free tier | capture: sha256:f4b6719cbed854cb8ba08ccf895870cb619708b16534b30831f1ddc475f2c83c | quote: Notice that you have 2 options to specify the file upload type: `calldata`, `blob`. The default type is `blob` which requires network support for EIP-4844.
- sources:
  - [1] https://chainscorelabs.com/da
  - [2] https://docs.ethstorage.io/dapp-developer-guide/tutorials/upload-your-file-folder-with-ethfs-cli
  - [3] https://evmfs.app/
