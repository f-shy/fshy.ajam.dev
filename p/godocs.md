# ipfs

> godocs.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/godocs/ | JSON https://fshy.ajam.dev/api/v1/entity/godocs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipfs / libp2p circuit relay v2 as a data path

- `storage/ipfs-libp2p-circuit-relay-v2-as-a-data-path` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://godocs.io/github.com/libp2p/go-libp2p/p2p/protocol/circuitv2/relay
- free tier: none reachable: Protocol defaults are 2 min and 128 KB per direction, deliberately sized for hole-punching (DCUtR), not transfer. Kubo ships these defaults and the docs say v2 relays exist 'to enable NAT… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Protocol defaults are 2 min and 128 KB per direction, deliberately sized for hole-punching (DCUtR), not transfer. Kubo ships these defaults and the docs say v2 relays exist 'to enable NAT…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Protocol defaults are 2 min and 128 KB per direction, deliberately sized for hole-punching (DCUtR), not transfer. Kubo ships these defaults and the docs say v2 relays exist 'to enable NAT…
  - [2] 2026-10-21: cited as the basis of the rejection: Protocol defaults are 2 min and 128 KB per direction, deliberately sized for hole-punching (DCUtR), not transfer. Kubo ships these defaults and the docs say v2 relays exist 'to enable NAT ho
- sources:
  - [1] https://godocs.io/github.com/libp2p/go-libp2p/p2p/protocol/circuitv2/relay
  - [2] https://discuss.ipfs.tech/t/roadmap-for-circuit-relay-v2-file-transfer/14713
