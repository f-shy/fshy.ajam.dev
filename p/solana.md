# Solana account rent as raw storage

> solana.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/solana/ | JSON https://fshy.ajam.dev/api/v1/entity/solana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Solana account rent as raw storage

- `storage/solana-account-rent-as-raw-storage` | fails-quota | evidence reported | binding none | category blockchain
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.377Z (live) | stale on 2026-12-04
- url https://solana.com/docs/core/accounts
- free tier: No free tier. Storage is a refundable rent-exempt deposit: 10 MiB account costs 53,268,311,040 lamports (~53.27 SOL) to create, reclaimed only on close. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Max account data size: 10 MiB (10,485,760 bytes); max data growth per transaction 20 MiB (20,971,520 bytes). | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free reads via RPC while the account exists; all RPC providers rate-limit or block bulk account-data reads. | metered: no
- identity: email
- interface: rest
- limits note: Rent-exempt deposit per byte; per-transaction size cap means large accounts are written in many transactions; account data is public and account creation is rate-limited/expensive.
- interface detail: rest
- tooling: Solana JSON-RPC (getMinimumBalanceForRentExemption, getAccountInfo), solana-sdk, Anchor. Wrapper examples exist but nothing production-grade for bulk file storage.
- composes with: Cost scales linearly with bytes at ~5 SOL/MiB; 1 TiB would need ~5.3 million SOL of locked capital. Sharding across wallets does not reduce the deposit.
- reliability: The full storage balance can be recovered when the account is closed, so it is a refundable deposit rather than a fee.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: paid
  - dead_end.why: No free tier — storage is a refundable rent-exempt deposit: 10 MiB account costs 53,268,311,040 lamports (~53.27 SOL) to create, reclaimed only on close.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: probe: POST solana-rpc.publicnode.com getMinimumBalanceForRentExemption([10485760]) -> result 53268311040 lamports for a 10 MiB account
  - [1] 2026-10-21: 'Accounts must hold a minimum lamport balance proportional to their data size to stay onchain'
  - [2] 2026-10-21: rent is reclaimable in full when the account is closed
  - [3] 2026-11-19: an account holds at most 10 MiB of data | capture: sha256:2e594e185c1b306eed7771faf66f7d50d845c196dde9ce6fe94712ac16e072a5 | quote: Max account data size | 10 MiB (10,485,760 bytes)
  - [1] 2026-11-19: the storage balance is a refundable deposit proportional to data size | capture: sha256:35b5dfaf4914cf11d061568e6bc945250385e28385cc1614101c1c22429e9ee4 | quote: This refundable storage balance is proportional to the account's data size.
  - [1] 2026-11-19: the storage deposit is refundable on account close | capture: sha256:35b5dfaf4914cf11d061568e6bc945250385e28385cc1614101c1c22429e9ee4 | quote: the full balance can be recovered when the account is closed
- sources:
  - [1] https://solana.com/docs/core/accounts/account-structure
  - [2] https://solana.com/developers/cookbook/accounts/calculate-rent
  - [3] https://solana.com/docs/core/accounts
