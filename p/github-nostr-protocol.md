# Nostr relays + NIP-94/NIP-96 file metadata

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-nostr-protocol/ | JSON https://fshy.ajam.dev/api/v1/entity/github-nostr-protocol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nostr relays + NIP-94/NIP-96 file metadata — index only, not bytes

- `storage/nostr-relays-nip-94-nip-96-file-metadata-index-only-not` | fails-quota | evidence reported | binding per-object-cap | category nostr-relay
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/nostr-protocol/nips/blob/master/94.md
- free tier: Zero bytes. NIP-94 is a metadata event: `url`, `m` (mime), `size`, `dim`, `i` (torrent infohash), `thumb`. The relay stores the JSON pointer, the file lives elsewhere. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap = relay event size limit (~64 KB | bytes: 64000 | source: [1] | note: not stated
- retention: until the instance is recycled; not persistent | source: [1] | note: not stated
- egress: N/a. Relay never serves the file. | metered: no
- identity: email
- interface: cli
- limits:
  - per-object-cap (binding): per-object-cap = relay event size limit (~64 KB [1]
- limits note: per-object-cap: Bounded by relay event size limits (~64 KB typical). Base64 encoding overhead leaves approximately 48 KB of payload data per event.
- interface detail: websocket
- tooling: nostr websocket protocol (EVENT/REQ), `nak` CLI. Relays are free and accept arbitrary events, but the event size limit (typ. 64 KB) caps any inline-base64 trick at ~48 KB.
- composes with: Chains with Blossom: NIP-94/NIP-96 events make Blossom blobs discoverable and re-mirrorable. On its own this is not storage.
- reliability: Relays are ephemeral and freely delete events; free relays exist in the thousands but none is a byte store.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Zero bytes. NIP-94 is a metadata event: `url`, `m` (mime), `size`, `dim`, `i` (torrent infohash), `thumb`. The relay stores the JSON pointer, the file lives elsewhere.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: tags are `url`, `m`, `size`, `dim`, `i` (torrent infohash), `thumb`; 'A relay for indexing shared files. For example, to promote torrents.' — confirms metadata-only semantics
- sources:
  - [1] https://raw.githubusercontent.com/nostr-protocol/nips/master/94.md
