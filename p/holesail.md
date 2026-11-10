# Holesail

> holesail.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/holesail/ | JSON https://fshy.ajam.dev/api/v1/entity/holesail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Holesail

- `egress/holesail` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category p2p tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-04
- url https://holesail.io/
- price USD 0
- free tier: Holesail is the world's first truly peer-to-peer proxy for TCP and UDP ports. No port forwarding, servers or configuration required. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance exists: the bytes travel between the two peers, and the public DHT only coordinates the holepunch.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account, email or card: the connection string is a public key derived from a keypair generated locally. | country: None
- interface: cli
- limits:
  - per-ip-shaping: no quota: the vendor documentation lists 'Unlimited bandwidth' with 'No artificial limits or throttling'; throughput is whatever the two peers' paths allow [3]
- binding note: Nothing meters the bytes, so at 1 TiB/month the limit is the peer's uplink and NAT behaviour, not a vendor counter.
- interface detail: npm i holesail -g; holesail --live 3000 prints an hs:// connection string.
- tooling: npm i holesail -g; holesail --live <port> then holesail <connection-string>.
- composes with: Carries a WireGuard handshake between a free VM and a laptop without opening a port on either, at the cost of installing a client on both ends.
- reliability: Depends on public HyperDHT bootstrap nodes; symmetric NAT defeats the holepunch and falls back to TCP, which breaks UDP-only protocols. A harness verified the server side and public-DHT peer discovery on 2026-11-05; the end-to-end data path was not testable in that sandbox.
- notes: Not a hosted ingress: a third party cannot connect unless they run holesail with the connection string. It qualifies as free UDP capacity between two machines under one control, which covers a WireGuard endpoint only if the far side also runs it. A sandbox verified the server side and public-DHT peer discovery on 2026-11-05 but could not test the data path.
- evidence note: A measured transfer between two peers behind different NATs would show the real throughput and whether the DHT path holds; that is the missing rung.
- self hosted: yes
- extras:
  - wg_path: inside-udp
  - wg_detail: The transport after holepunching is UDX, a custom UDP protocol, with a TCP fallback. A WireGuard datagram can ride that path between two peers running holesail.
  - ingress: tcp+udp
  - volume_stated: No allowance exists: the bytes travel between the two peers, and the public DHT only coordinates the holepunch.
  - bytes_transit: overlay-only
  - transit_note: Bytes go peer to peer after holepunching; only coordination metadata crosses the public DHT.
- evidence:
  - [1] 2026-10-23: Peer-to-peer proxy for TCP and UDP; npm install; connection string replaces a public address.
  - [4] 2025-12-03: Launch post: no port forwarding, no VPNs, no servers in the middle, supports both UDP and TCP.
  - [5] 2026-10-23: Mechanism: peers announce to HyperDHT, DHT nodes coordinate a UDP holepunch, then UDX carries the data; TCP fallback exists.
  - [3] 2026-11-03: the vendor documentation lists unlimited bandwidth with no artificial limits or throttling | capture: sha256:10ec45d6e66d73e4c6a673e2696fa8f7dfa48a6cab0ffe58118c2ac38faf40e4 | quote: No artificial limits or throttling.
  - [3] 2026-11-04: the documentation lists unlimited bandwidth with no artificial limits or throttling | capture: sha256:10ec45d6e66d73e4c6a673e2696fa8f7dfa48a6cab0ffe58118c2ac38faf40e4 | quote: No artificial limits or throttling.
  - probe:holesail 2026-11-05: peer discovery on the public DHT worked from a capability-free sandbox | capture: sha256:33995b2eba9c39ca4f812c06c82d3d09bcdcd82d897be7778ea1c4a907ac1627 | quote: peer discovery on the public DHT works from this network
- sources:
  - [1] https://github.com/holesail/holesail
  - [2] https://holesail.io/
  - [3] https://docs.holesail.io/
  - [4] https://news.ycombinator.com/item?id=46131627
  - [5] https://news.ycombinator.com/item?id=46172495
