# Nostr relays as blob transport

> nostr.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nostr-2/ | JSON https://fshy.ajam.dev/api/v1/entity/nostr-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nostr relays as blob transport (event path, not Blossom)

- `storage/nostr-relays-as-blob-transport` | fails-quota | evidence reported | binding per-object-cap | category signalling-only
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nips.nostr.com/94
- free tier: no storage quota, but a hard per-event size ceiling that is the real limit. Probed NIP-11 limitation.max_message_length: relay.damus.io 1,000,000 bytes; relay.primal.net 1,000,000 bytes; nos.lol 131,072 bytes. No payment_required, no auth_required on any of the three. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap ~1 MB | bytes: 1000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free and unmetered on all three. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - per-object-cap (binding): per-object-cap ~1 MB [1]
- limits note: per-object-cap ~1 MB on the most generous relays, 128 KB on nos.lol. 1 TiB would be ~1.4 million events.
- interface detail: WebSocket, NIP-01 REQ/EVENT; NIP-94 kind 1063 carries file metadata only.
- tooling: nak, nostr-tools, any relay client. Blobs are pinned by sha256+url in tags; the bytes live elsewhere (Blossom).
- composes with: Base64 encoding in tags expands payload size by 4/3, reducing a 1 MB message limit to approximately 750 KB of useful bytes. Storing binary objects in event streams introduces high metadata and encoding overhead.
- reliability: relays can be paid-gated (NIP-11 payment_required) and prune old events; several now require auth for writes. Correct use is metadata only, which is exactly what NIP-94 defines.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no storage quota, but a hard per-event size ceiling that is the real limit. Probed NIP-11 limitation.max_message_length: relay.damus.io 1,000,000 bytes; relay.primal.net 1,000,000 bytes; nos.lol 131,072 bytes. No payment_required, no auth_required on any of the three.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: with Accept: application/nostr+json — literal: max_message_length 1000000, max_subscriptions 200, payment_required None, auth_required None
  - [2] 2026-10-21: max_message_length 131072, max_subscriptions 100
  - [3] 2026-10-21: max_message_length 1000000, max_subscriptions 20
  - [4] 2026-10-21: NIP-94 defines kind 1063 file metadata with url/mime/sha256/size tags — metadata, not bytes
  - [5] 2026-10-21: 'the total size of the event can't be larger than 50 267 340 bytes (~50 MB)' as an upper protocol bound, far above what any public relay accepts
- sources:
  - [1] https://relay.damus.io/
  - [2] https://nos.lol/
  - [3] https://relay.primal.net/
  - [4] https://nips.nostr.com/94
  - [5] https://github.com/renostr/nrps/blob/master/nrp-1.md
