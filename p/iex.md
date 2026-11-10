# iExec

> iex.ec | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iex/ | JSON https://fshy.ajam.dev/api/v1/entity/iex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iExec

- `compute/iexec` | fails-quota | evidence documented | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.iex.ec/get-started/tooling-and-explorers/faucet
- free tier: TEE compute on workerpools paid per execution in RLC, split between the app provider, the data provider, the workerpool and gas. The free lane is testnet only: 'Get 5 RLC tokens per claim on Arbitrum Sepolia testnet', with GitHub authentication, a 24-hour cooldown and 'Balance verification (max 1 RLC)'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: testnet-faucet
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a GitHub account is the gate on the free lane: the faucet documentation states "Get 5 RLC tokens per claim on Arbitrum Sepolia testnet" with GitHub authentication, a 24-hour cooldown and a balance check capped at 1 RLC, and the tokens buy testnet executions only. Mainnet capacity needs RLC bought on an exchange, and the record does not state whether that purchase or the mainnet account requires KYC, a phone or an identity document; no card, hold, debit or prepaid statement appears
- interface: unknown
- limits:
  - write-gated (binding): The faucet pays 5 RLC per claim with a 24-hour cooldown and a wallet balance check capped at 1 RLC, and the tokens buy only Arbitrum Sepolia executions, so no production job can run on the free lane. [1]
- limits note: The faucet pays 5 RLC per claim with a 24-hour cooldown and a wallet balance check capped at 1 RLC, and the tokens buy only Arbitrum Sepolia executions, so no production job can run on the free lane.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A workerpool order with all price fields at 0 accepts only free resources, so a testnet run can be assembled at zero token cost; the same setting on mainnet finds no worker, because no provider serves for nothing.
- reliability: no reliability event recorded
- notes: iExec is the cheapest TEE execution lane found here only if a provider publishes a 0-price order; none was found. Mainnet capacity needs RLC bought on an exchange. Whether the Sepolia workerpool has live workers was not tested; that needs a funded testnet wallet and an order match.
- extras:
  - facets.class: testnet-faucet
  - facets.free_tier_kind: testnet-faucet
- evidence:
  - [1] 2026-10-22: read directly: 'Get 5 RLC tokens per claim on Arbitrum Sepolia testnet', GitHub authentication, 24-hour cooldown, balance verification with a max of 1 RLC, testnet only
  - [2] 2026-10-22: four cost components per execution: app fee, data fee, workerpool fee and gas, all in nRLC; default max prices are 0, which accepts only free resources
  - [3] 2026-10-22: RLC USD 0.657628, so a 5 RLC claim is about USD 3.29 of testnet token with no market value
- sources:
  - [1] https://docs.iex.ec/get-started/tooling-and-explorers/faucet
  - [2] https://docs.iex.ec/guides/use-iapp/how-to-pay-executions
  - [3] https://api.coingecko.com/api/v3/simple/price?ids=iexec-rlc&vs_currencies=usd
