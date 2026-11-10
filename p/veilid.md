# Veilid

> veilid.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/veilid/ | JSON https://fshy.ajam.dev/api/v1/entity/veilid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Veilid

- `storage/veilid` | self-hosted, last resort | verdict fails-quota | evidence reported | binding write-gated | category p2p-relay-network
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://veilid.com/how-it-works/networking/
- free tier: No quota and no account. 'All Veilid applications running veilid-core are nodes, and they are all equal in the eyes of the network. No nodes are special. Nodes are only limited by the resources they bring.'. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Peer-to-peer, with inbound/outbound relays only for reachability. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - write-gated (binding): applications running veilid-core are nodes, and they are all equal in the eyes of the netwo [1]
- limits note: No congestion control implemented. Open issue #404 'congestion control could be implemented with NodeStatus'; relay throttling is a to-do, not a feature.
- interface detail: AppMessage / AppCall primitives over routes; the core never parses app bytes. DHT for storage of small records.
- tooling: veilid-core in Rust with bindings; veilid-server binary.
- composes with: Not a file transport. Designed mobile-first for 'intermittent network connections, volatile IP addresses, CGNAT, limited storage and bandwidth'. The opposite of a bulk path.
- reliability: sending bulk data through Veilid is unsupported in practice: without flow control a large transfer either starves or gets dropped. Eliminated on reliability, not on quota.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: no quota and no account — 'All Veilid applications running veilid-core are nodes, and they are all equal in the eyes of the network. No nodes are special. Nodes are only limited by the resources they bring.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'No nodes are special ... Nodes are only limited by the resources they bring and the configuration of the network they are on'
  - [2] 2026-10-21: 'congestion control could be implemented with NodeStatus'; 'max bytes a flow can consume in X minutes' proposed as an unimplemented idea
  - [3] 2026-10-21: 'Relay traffic could use bandwidth throttling or roundrobin assignments' listed as To do
  - [4] 2026-10-21: 'limited storage and bandwidth' as a design assumption (mobile-first)
- sources:
  - [1] https://veilid.com/how-it-works/networking/
  - [2] https://gitlab.com/veilid/veilid/-/issues/404
  - [3] https://gitlab.com/groups/veilid/-/work_items/3
  - [4] https://veilid.gitlab.io/developer-book/why-veilid/
