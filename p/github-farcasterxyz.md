# Farcaster hubs

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-farcasterxyz/ | JSON https://fshy.ajam.dev/api/v1/entity/github-farcasterxyz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Farcaster hubs / Snapchain — storage RENT, actively metered

- `storage/farcaster-hubs-snapchain-storage-rent-actively-metered` | fails-quota | evidence reported | binding none | category farcaster
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/farcasterxyz/protocol/blob/main/docs/SPECIFICATION.md
- free tier: Storage is allocated in integer units per fid and must be BOUGHT from the Storage Registry contract on Optimism (0x00000000fcCe7f938e7aE6D3c335bD6a1a7c593D). Each CRDT specifies messages-per-unit, so the unit is a message count, not bytes. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/a. Hubs replicate messages, media is a URL in the cast body pointing at an external host (often Cloudflare Images / imgur). | metered: no
- identity: email
- interface: unknown
- limits note: per-object-cap not applicable; the binding limit is storage units paid for on Optimism plus per-CRDT message-count accounting. Free tier = whatever 1 storage unit covers (a few hundred casts).
- interface detail: grpc
- tooling: gRPC hub API (submitMessage); `@farcaster/hub-nodejs`. Storage must be purchased on-chain before a message is accepted.
- composes with: None. Media is never stored by the protocol. A cast embed is a plain URL. Farcaster is a message log with paid rent, not a file store.
- reliability: Snapchain (2025 rewrite) preserves the rent model.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Storage is allocated in integer units per fid and must be BOUGHT from the Storage Registry contract on Optimism (0x00000000fcCe7f938e7aE6D3c335bD6a1a7c593D). Each CRDT specifies messages-per-unit, so the unit is a message count, not bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The Storage registry contract keeps track of the storage allocated to each fid. The storage for an fid is denominated in integer units. Each CRDT specifies the number of messages it can store per unit.'; 'For a message to be accepted, the fid must be registered in the Id registry, and signed with a valid signer present in the Key registry, and the fid must have enough storage allocated in the Storage registry.'
  - [2] 2026-10-21: probe: GET -> 404 (moved); docs.farcaster.xyz is a Next.js shell with no server-rendered quota table
- sources:
  - [1] https://raw.githubusercontent.com/farcasterxyz/protocol/main/docs/SPECIFICATION.md
  - [2] https://docs.farcaster.xyz/learn/architecture/storage
