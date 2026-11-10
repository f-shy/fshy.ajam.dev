# Irys

> irys.xyz | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/irys/ | JSON https://fshy.ajam.dev/api/v1/entity/irys.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Irys (devnet bundler)

- `storage/irys` | fails-quota | evidence reported | binding retention-clamped | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- reliability: Irys is retiring its Arweave bundler endpoints (node1.irys.xyz, mainnet.arweave.irys.xyz) on 2026-11-01, so any wrapper built on the Arweave path breaks in ten days.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Devnet uploads are paid with free faucet tokens; 'Devnet ... data retention lasting approximately 60 days before deletion'. Mainnet has no free allowance — storage is metered per byte-second.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'a devnet bundler for testing with free faucet tokens'; 'data retention lasting approximately 60 days before deletion'
  - [2] 2026-10-21: 'Arweave bundlers retire on 1 November 2026'
  - [3] 2026-10-21: probe: GET -> 200 {"version":"0.2.0"...}
- sources:
  - [1] https://docs.irys.xyz/onchain-storage/mainnet-devnet
  - [2] https://docs.irys.xyz/onchain-storage/bundlers
  - [3] https://uploader.irys.xyz/info

## irys (ex-bundlr)

- `storage/irys-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://docs.irys.xyz/economics/economics-pricing
