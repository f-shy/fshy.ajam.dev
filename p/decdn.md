# deCDN

> decdn.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/decdn/ | JSON https://fshy.ajam.dev/api/v1/entity/decdn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## deCDN

- `storage/decdn` | fails-quota | evidence reported | binding write-gated | category Decentralized CDN — paid per MB in USDC, iroh transport
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://decdn.org/
- free tier: No free capacity. No storage tier at all: 'Not a blockchain or storage network — durability relies on cheap, reliable object storage (S3-class) owned by origin operators.' Target delivery price $0.01/GB (node default rate `payment.rate_per_mb = 10` = $0.00001/MB). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: $0.01/GB target, set per node and signed into every quote; client sets a ceiling. Testnet is sponsor-funded with a capped allowance. 'there is nothing to pay and no account to make'. But that is testnet money on Arbitrum Sepolia. | metered: yes
- identity: email | detail: email
- interface: cli
- limits:
  - per-ip-shaping: 1 Gbps [1]
  - write-gated (binding): approved, the rest of the network accepts your nodes as origins'), so publishing is writ [1]
  - write-gated (binding): approval-gated [1]
- limits note: Per-MB payment is mandatory for clients on mainnet. There is no free reader tier. Namespaces gate the origin role ('Once you get approved, the rest of the network accepts your nodes as origins'), so publishing is write-gated by a human. Node bond on testnet is 50,000 TOKEN for anything up to ~1 Gbps; unbonding takes 14 days. 0.4% verification overhead plus node-to-node pull costs.
- interface detail: Client SDK (Rust; macOS/Linux/Windows, phone/browser in testing) + `decdn` CLI: `decdn get 'decdn:<blake3hash>/?ns=1'`. One human-verification step in a browser on first install.
- tooling: Install via `curl -fsSL https://up.decdn.org/decdn.sh | sh -s -- get '<uri>'` (both scripts returned HTTP 200); PowerShell variant; node operator side is `decdn setup` / `decdn node bond`.
- composes with: Origin node in front of your own S3/R2/B2/NFS/local disk stays hidden; bonded nodes cache and re-serve over iroh QUIC with bao-encoded verified streaming. Multi-source fetch splits blobs >64 MiB across up to 4 nodes, one per operator. Publisher's own origin pulls are free. Cache misses cost the serving node, not the publisher.
- reliability: Public testnet only (Arbitrum Sepolia, launched 2026-10-13); governance hash blacklist forces nodes to stop serving a listed hash within 24 h, and the origin role is approval-gated.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free capacity. No storage tier at all: 'Not a blockchain or storage network — durability relies on cheap, reliable object storage (S3-class) owned by origin operators.' Target delivery price $0.01/GB (node default rate `payment.rate_per_mb = 10` = $0.00001/MB).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: content-addressed, paid per MB, origin-hidden, bonded/slashable, 'Not a blockchain or storage network'
  - [2] 2026-10-21: '$0.01/GB' target, split fetch over >64 MiB with ≥2 holders across up to 4 operators, origin 'Once you get approved'
  - [3] 2026-10-13: 2026-10-13 public testnet, sponsor-capped allowance, 'nothing to pay and no account to make', pilots by email
  - [4] 2026-10-21: bond curve 12.6 x Mbps^1.2, testnet minBond 50,000 TOKEN, 14-day unbond, operator share 60% testnet / 90% at mainnet launch
  - [5] 2026-10-21: UDP 4433 public, 5 TB/month egress recommended, cache 250 GB-1 TB
  - [6] 2026-10-21: 'no single vendor can reprice you'; the pitch is verified delivery, not free bytes
- sources:
  - [1] https://docs.decdn.org/overview/introduction
  - [2] https://decdn.org/
  - [3] https://decdn.org/blog/testnet-is-live/
  - [4] https://docs.decdn.org/run-a-node/bond-and-earnings
  - [5] https://docs.decdn.org/run-a-node/requirements
  - [6] https://decdn.org/blog/who-actually-needs-this/
