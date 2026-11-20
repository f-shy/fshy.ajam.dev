# Freehold

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-maceip/ | JSON https://fshy.ajam.dev/api/v1/entity/github-maceip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freehold

- `egress/freehold` | fails-egress | evidence inferred | binding none | category public anycast relay (QUIC/H3) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/maceip/freehold
- price USD 0
- free tier: Your service is now reachable at freehold.lit.app:8080. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published for the public relay: 'Test the public relay without installing anything.'; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No account: the client registers itself with the relay over UDP and completes an HMAC challenge. | country: None
- interface: cli
- limits:
  - volume-quota: no byte allowance published for the public relay [1]
- binding note: The relay is a public anycast endpoint with no published quota; what stops the UDP test first is the data path, which is described as QUIC/H3 rather than a raw datagram forward.
- interface detail: 'freehold --relay freehold.lit.app:9999 --port 8080 --backend 127.0.0.1:3000'
- tooling: The freehold Rust client; the relay itself needs a Linux host with eBPF and root, which is the relay operator's problem, not a client-side one
- composes with: Nothing to chain until the datagram question is settled.
- reliability: NAT traversal is best-effort: the port spray 'opens Bob's NAT' only if the carrier allocates ports sequentially, and traffic falls back to the relay otherwise.
- notes: A free public anycast relay that a client can register with anonymously is the only such relay found. What it exposes is an HTTP/3 service on a shared anycast name: the README diagram shows a QUIC request being rewritten, not a raw datagram being forwarded, and the client software is a Rust binary, not a tunnel daemon. If that reading is wrong, this becomes the strongest lead of its kind, which is why the reading is labelled inferred and not treated as settled.
- evidence note: Reverse proxy architecture and transport specifications are documented in product reference guides.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard; the relay terminates QUIC and rewrites addresses with XDP.
  - ingress: http-only
  - volume_stated: No byte allowance is published for the public relay: 'Test the public relay without installing anything.'
  - bytes_transit: yes
  - transit_note: The relay's XDP program forwards to the registered client, or a user and peer go direct after a successful punch.
- evidence:
  - [1] 2026-10-23: 'Give any device a real public IP address. Host services that browsers trust - not tunnel URLs.'
  - [1] 2026-10-23: 'This relay announces the 142.248.222.0/24 anycast prefix.' and 'A public relay is available at freehold.lit.app:9999'
  - [1] 2026-10-23: The data path is 'Browser (Alice) ... QUIC/H3 request ... XDP SNAT+DNAT', and the feature list names 'Optional HTTP/3 reverse proxy with automatic TLS'
- sources:
  - [1] https://github.com/maceip/freehold
