# Irys

> irys.xyz | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/irys/ | JSON https://fshy.ajam.dev/api/v1/entity/irys.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Irys (devnet bundler)

- `storage/irys` | fails-quota | evidence reported | binding retention-clamped | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.854Z (live) | stale on 2026-12-04
- url https://docs.irys.xyz/onchain-storage/mainnet-devnet
- disagrees on identity_kind: `storage/irys` says institution, `storage/irys-2` says email
- free tier: Devnet uploads are paid with free faucet tokens; 'Devnet .. data retention lasting approximately 60 days before deletion'. Mainnet has no free allowance. Storage is metered per byte-second. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: data retention lasting approximately 60 days before deletion' | days: 60 | source: [1] | note: not stated
- egress: not metered separately; data is served from the destination network (Irys L1). Not quantified on the pages read. | metered: yes
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, cli
- limits:
  - retention-clamped (binding): retention lasting approximately 60 days [1]
  - retention-clamped (binding): retention: ~60 days [1]
- limits note: per-object-cap: not stated. retention: ~60 days on devnet, hard deletion. request-rate: none documented. Binding constraint is faucet economics plus the 60-day retention.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: @irys/upload SDK (TypeScript), plus a storage CLI. Endpoint uploader.irys.xyz (probe GET /info -> 200, version 0.2.0).
- composes with: Faucet-funded devnet wallets are cheap to mint, and 60-day retention means rolling re-upload. Volume is bounded by faucet drip, not by a published quota.
- reliability: The Arweave bundler endpoints node1.irys.xyz and mainnet.arweave.irys.xyz retired on 1 November 2026; new uploads use uploader.irys.xyz to Irys L1.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Devnet uploads are paid with free faucet tokens; 'Devnet ... data retention lasting approximately 60 days before deletion'. Mainnet has no free allowance — storage is metered per byte-second.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'a devnet bundler for testing with free faucet tokens'; 'data retention lasting approximately 60 days before deletion'
  - [2] 2026-10-21: 'Arweave bundlers retire on 1 November 2026'
  - [3] 2026-10-21: probe: GET -> 200 {"version":"0.2.0"...}
  - [1] 2026-11-19: devnet uploads use free faucet tokens and are retained approximately 60 days before deletion | capture: sha256:ae2c49dccb763c3c5372cd0e1a6168e2e1d34dc4c00d50d6db17cba0a3d872bc | quote: The devnet testing network uses free faucet tokens for uploads, with data retention lasting approximately 60 days before deletion.
  - [2] 2026-11-19: the Arweave bundler retirement date passed on 1 November 2026 | capture: sha256:851cec6ab6034886aeb9e7b911200bcfe78714bbf1ce48565f7a325d4d477d1f | quote: Arweave bundlers retire on 1 November 2026
- sources:
  - [1] https://docs.irys.xyz/onchain-storage/mainnet-devnet
  - [2] https://docs.irys.xyz/onchain-storage/bundlers
  - [3] https://uploader.irys.xyz/info

## irys (ex-bundlr)

- `storage/irys-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.854Z (live) | stale on 2026-12-04
- url https://docs.irys.xyz/economics/economics-pricing
- disagrees on identity_kind: `storage/irys` says institution, `storage/irys-2` says email
- free tier: none reachable: Permanent on-chain storage priced by the protocol in IRYS tokens; docs describe a fee market and price-stabilisation mechanism, not a free tier. Uploads require a funded wallet. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Permanent on-chain storage priced by the protocol in IRYS tokens; docs describe a fee market and price-stabilisation mechanism, not a free tier. Uploads require a funded wallet.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Permanent on-chain storage priced by the protocol in IRYS tokens; docs describe a fee market and price-stabilisation mechanism, not a free tier. Uploads require a funded wallet.
  - [1] 2026-11-19: Irys prices storage by amount and duration, with no free tier described | capture: sha256:cfbd01014c497161bb7a2fad03bb4c1150f02aaeeb95286943f2e30a91c8aab6 | quote: Storage fees are determined by the amount of data stored and the duration it is expected to persist.
- sources:
  - [1] https://docs.irys.xyz/economics/economics-pricing
