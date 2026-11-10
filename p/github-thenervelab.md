# Hippius Arion

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-thenervelab/ | JSON https://fshy.ajam.dev/api/v1/entity/github-thenervelab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hippius Arion (Bittensor subnet on iroh)

- `storage/hippius-arion` | fails-quota | evidence inferred | binding none | category Decentralized storage subnet — erasure-coded, iroh transport
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://github.com/thenervelab/arion
- free tier: Paid storage product (Hippius sells S3-compatible storage, Drive, Hub). No free tier published on the pages opened. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Competitive pricing, no surprises—just pay for what you use'. Metered, no free allowance stated. | metered: yes
- identity: email | detail: email
- interface: s3-compatible
- limits note: Repo marked 'Active Development ... subject to change without notice', with a disclaimer beside that marker. Miner registration is on-chain.
- interface detail: HTTP gateway (:3000) for upload/download; S3-compatible product separately; miner/validator P2P via iroh `FetchBlob`.
- tooling: Reed-Solomon k=10/m=20 over 2 MiB stripes, CRUSH placement, PoSt audits via Plonky3, on-chain miner registration.
- composes with: Interesting architecture reference rather than a usable free store: it is the only system seen that combines erasure coding with iroh, i.e. 20 TiB of user data would occupy 60 TiB of miner disk at 3x parity.
- reliability: Testnet-stage code; the validator is a metadata authority and a single point of coordination for placement and recovery.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Paid storage product (Hippius sells S3-compatible storage, Drive, Hub). No free tier published on the pages opened.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: README: architecture, RS(10,20), CRUSH, iroh FetchBlob, active development warning
  - [1] 2026-10-21: commercial decentralized storage: Arion, S3-compatible, Drive, Hub; 'pay for what you use, recorded on-chain'
- sources:
  - [1] https://hippius.com/
  - [2] https://github.com/thenervelab/arion
