# Ritual

> ritualfoundation.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ritualfoundation/ | JSON https://fshy.ajam.dev/api/v1/entity/ritualfoundation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ritual

- `compute/ritual` | fails-quota | evidence reported | binding write-gated | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://docs.ritualfoundation.org/
- free tier: An AI-native chain where contracts call inference, HTTP and scheduling as precompiles and pay in RITUAL for enshrined compute. The only free lane is the public testnet (chain ID 1979), where 'Enter your access code to mint 5 RITUAL' from faucet.ritualfoundation.org, and the docs label the currency 'RITUAL (18 decimals, testnet)'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: testnet-faucet
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The faucet needs an access code and the token cannot be bridged; no mainnet token or mainnet credit programme has been announced, so real capacity is not purchasable by anyone yet. [1]
- limits note: The faucet needs an access code and the token cannot be bridged; no mainnet token or mainnet credit programme has been announced, so real capacity is not purchasable by anyone yet.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A testnet inference precompile lets an agent pipeline be written and debugged for free, which composes with any client that can sign a transaction; nothing produced runs on production hardware or has a resale value.
- reliability: no reliability event recorded
- notes: Two independent sources agree there is no mainnet token yet, which is the finding: the free lane exists and buys nothing durable. What would change it is a mainnet launch with a published fee schedule. The faucet's access code requirement was not tested; whether codes are issued on request was not established.
- extras:
  - facets.class: testnet-faucet
  - facets.free_tier_kind: testnet-faucet
- evidence:
  - [1] 2026-10-22: quick start lists chain ID 1979, currency 'RITUAL (18 decimals, testnet)', RPC and explorer, and a testnet faucet URL
  - [2] 2026-10-22: 'Check a balance or mint tokens. Access Code. Enter your access code to mint 5 RITUAL'
  - [3] 2026-10-22: public testnet announced 2026-06-23; 'Ritual has not published tokenomics, a token generation date, a points programme' and the testnet currency 'has no market value and cannot be bridged to a mainnet'
- sources:
  - [1] https://docs.ritualfoundation.org/
  - [2] https://faucet.ritualfoundation.org/
  - [3] https://cryptoincomehub.com/airdrops/ritual-testnet-2026-chain-ai-infrastructure-activity-guide/
