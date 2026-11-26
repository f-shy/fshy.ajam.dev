# Gensyn

> gensyn.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gensyn/ | JSON https://fshy.ajam.dev/api/v1/entity/gensyn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gensyn

- `compute/gensyn` | self-hosted, last resort | verdict fails-quota | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.gensyn.ai/testnet/rl-swarm/getting-started
- free tier: No consumer-facing capacity. Quoted: 'RL Swarm is a peer-to-peer reinforcement-learning swarm you can run on a laptop or a GPU server', with system requirements 'A 64-bit arm64 or x86 CPU with at least 32 GB RAM, or an officially supported NVIDIA GPU (3090, 4090, 5090, A100, H100)'. The dashboard states: 'There are no official swarms running right now.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a Hugging Face write token: the getting-started page is quoted as requiring 'a Hugging Face write token', which in turn implies a Hugging Face account that issues it. No card, hold, phone or ID is stated, and the email kind rests on that Hugging Face account rather than on a quoted signup form. Debit and prepaid do not arise because no payment method is mentioned. The 32 GB RAM or listed NVIDIA GPU requirement is a capacity gate, not an identity one.
- interface: unknown
- limits:
  - write-gated (binding): The direction is inverted: Gensyn pays suppliers who bring hardware, so it consumes hardware rather than supplying it. Even as a supplier lane it fails first on the 32 GB RAM or supported-GPU floor, then on 'no official swarms running right now'. [1]
- limits note: The direction is inverted: Gensyn pays suppliers who bring hardware, so it consumes hardware rather than supplying it. Even as a supplier lane it fails first on the 32 GB RAM or supported-GPU floor, then on 'no official swarms running right now'.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. Gensyn is a market for selling compute, not buying it, and it has no live swarm. A chain that includes Gensyn would need a GPU already in place.
- reliability: no reliability event recorded
- notes: REFUTATION OF A COMMON MISREADING. Gensyn appears in free-GPU roundups because RL Swarm is free to join, but joining means contributing hardware, not receiving capacity. Three independent facts kill it as a source of capacity: it needs 32 GB RAM or a listed NVIDIA card, its dashboard says no official swarms are running, and its reward unit is a token allocation out of a 2 percent testnet pool with no published per-node formula. A third-party guide also records that renting a GPU to run a Gensyn node costs USD 65 to USD 300 per month.
- self hosted: yes
- extras:
  - facets.class: decentralized-training-network
  - facets.shape.ram_gib: 32
- evidence:
  - [1] 2026-10-22: quoted: requires a 64-bit arm64/x86 CPU with at least 32 GB RAM or a supported NVIDIA GPU (3090, 4090, 5090, A100, H100); a Hugging Face write token is required
  - [2] 2026-10-22: quoted: 'There are no official swarms running right now. Please check back later'; the network reports 427,530 on-chain users
  - [3] 2026-10-22: public testnet launched March 2025; the network tracks participation and makes payments, it does not rent capacity to consumers
  - [4] 2026-10-22: third-party operator guide states 'No compute-provider earnings have been published for Gensyn mainnet' and that testnet rewards were 'relative and pool-based'
- sources:
  - [1] https://docs.gensyn.ai/testnet/rl-swarm/getting-started
  - [2] https://dashboard.gensyn.ai/
  - [3] https://docs.gensyn.ai/testnet
  - [4] https://depinrun.com/guides/gensyn-node-operator-guide
