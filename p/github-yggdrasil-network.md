# Yggdrasil public peers

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-yggdrasil-network/ | JSON https://fshy.ajam.dev/api/v1/entity/github-yggdrasil-network.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Yggdrasil public peers

- `egress/yggdrasil-public-peers` | fails-egress | evidence documented | binding none | category relay network (volunteer)
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://github.com/yggdrasil-network/public-peers
- free tier: peering with a volunteer node at the rate it advertises, with no byte meter in the protocol; the overlay carries traffic only to other Yggdrasil nodes | unit: unlimited | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a routed overlay rather than an object store
- retention: not applicable | source: [1]
- egress: no byte quota exists anywhere in the protocol, and no peer carries traffic to the public internet: the project states it has no exit nodes. The 2.16 TB per day a 200 Mbit/s peer implies is overlay capacity between two Yggdrasil nodes | metered: no | source: [1]
- identity: anonymous | detail: the network is keyed by a self-generated keypair, not an account
- interface: unknown
- limits:
  - per-ip-shaping: whatever the peer grants; the directory lists 100 Mbit/s to 1 Gbit/s per node, which bounds overlay traffic between Yggdrasil nodes [1]
- limits note: the absence of an exit node is the whole finding and it is not a limit of any of the six kinds: it is a capability the network does not have. Yggdrasil routes inside 0200::/7 only, and the project states that reaching the public internet 'can be achieved using proxies or other tunnelling solutions on top of Yggdrasil but this is not something we explicitly aim to provide'
- binding note: nothing in Yggdrasil binds, because nothing in Yggdrasil carries the traffic. The peer's advertised rate bounds overlay volume and is irrelevant to a public serving path
- interface detail: quic://, tls://, tcp:// or ws:// entries in the Peers[] list of yggdrasil.conf
- tooling: part of interface detail
- composes with: a private mesh between a user's own machines: a node reaches another node's 0200::/7 address with no port forward and no public address. It is not a route to a reader, so it has no place in a serving chain
- reliability: an alpha-level research project by its own description; the directory is a snapshot of who is currently willing to peer
- notes: Two corrections. And 200 Mbit/s is 2.16 TB, not 2.16 TiB.
- evidence note: the exit-node absence is a first-party statement on the project's own about page, so the field the verdict rests on is documented. Peer rates come from the public directory. No throughput was measured, and none would change the verdict
- extras:
  - stale_after_days: 180
  - bytes_transit: no
  - transit_note: Yggdrasil routes only inside its own 0200::/7 overlay and the project states it has no exit nodes, so no peer carries traffic to the public internet
- evidence:
  - [2] 2026-10-22: quoted verbatim: 'Yggdrasil has no native exit nodes, nor does it have any concept of exit nodes, for providing access to the public Internet or to other networks. This can be achieved using proxies or other tunnelling solutions on top of Yggdrasil but this is not something we explicitly aim to provide.'
  - [3] 2026-10-22: quoted: 'Yggdrasil uses the 0200::/7 range, which is a range deprecated by the IETF', and 'While Yggdrasil does transport only IPv6 traffic internally, you do not need an IPv6 internet connection to peer'
  - probe:tcp://ygg.mkg20001.io:443 2026-10-22: 3 of 4 sampled peers accepted a TCP connection from this host: mkg20001, mk16.de and yggdrasil.su open; the Oracle Ashburn address timed out
- sources:
  - [1] https://github.com/yggdrasil-network/public-peers
  - [2] https://yggdrasil-network.github.io/about.html
  - [3] https://yggdrasil-network.github.io/faq.html
