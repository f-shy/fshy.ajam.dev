# udp-over-tcp

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-mullvad/ | JSON https://fshy.ajam.dev/api/v1/entity/github-mullvad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## udp-over-tcp (mullvad)

- `egress/mullvad-udp-over-tcp` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/mullvad/udp-over-tcp
- price USD 0
- free tier: no service and no account; a Rust library with two binaries, udp2tcp and tcp2udp | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: the constraint is the server half, which is why Mullvad itself can offer the feature and a client cannot get it for free
- interface detail: udp2tcp and tcp2udp binaries, or the Rust crate
- tooling: cargo; two binaries, embeddable as a library
- composes with: composes with a server host; the Mullvad deployment of it is a paid provider feature recorded elsewhere.
- reliability: one udp2tcp instance handles one peer only; the server spawns a UDP socket per TCP connection
- notes: Included because it is the production-grade reference for the technique and the ancestor proxyguard names. Its existence also explains why the wrapper question is a hosting question: Mullvad can offer WireGuard over TCP because it owns the server half. A library alone cannot give the same thing without a server to run it. The 16-bit length prefix caps a datagram at 65535 bytes, which is not a real constraint for WireGuard's MTU.
- evidence note: its behaviour inside the Mullvad app is not testable without a subscription; the library's own protocol is documented
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: tcp2udp runs on the server and forwards to 127.0.0.1:51820; udp2tcp runs on a user beside the WireGuard interface
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: through the tcp2udp server, which owns the UDP socket to WireGuard
  - hosting_requirement: a server host running tcp2udp; the client binary goes beside the WireGuard interface
  - last_release: no GitHub releases; last push 2026-08-17
  - stars: 588
- evidence:
  - [1] 2026-10-23: "A library (and binaries) for tunneling UDP datagrams over a TCP stream"; tcp2udp example forwarding 10.0.0.0:5001/TCP to 127.0.0.1:51820/UDP
  - [1] 2026-10-23: the wire format: "Each datagram is preceded with a 16 bit unsigned integer in big endian byte order"
  - [1] 2026-10-23: 588 stars, no GitHub releases, last push 2026-08-17
  - [2] 2026-10-23: Mullvad deploys WireGuard over TCP on its own servers and switches to it with 'mullvad relay set tunnel wireguard --protocol tcp'
- sources:
  - [1] https://github.com/mullvad/udp-over-tcp
  - [2] https://mullvad.net/en/blog/introducing-wireguard-over-tcp-and-ipv6
