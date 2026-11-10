# wireguard-proxy

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-moparisthebest/ | JSON https://fshy.ajam.dev/api/v1/entity/github-moparisthebest.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wireguard-proxy (moparisthebest)

- `egress/wireguard-proxy` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/moparisthebest/wireguard-proxy
- price USD 0
- free tier: no service and no account; source and static builds | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; a server-side daemon and a client-side daemon on hosts the operator controls | country: None
- interface: cli
- binding note: the constraint is a server-side host, plus an unmaintained codebase, neither of which the vocabulary covers
- interface detail: wireguard-proxy -tt / -th daemons
- tooling: cargo, static builds in releases, AUR package
- composes with: plain TCP or TLS, so it can ride a TCP forwarder that hands over a raw stream; it cannot ride an HTTP-only CDN because it never speaks an HTTP upgrade.
- reliability: unmaintained; --tls without --pinnedpubkey authenticates nothing
- notes: Functionally the cleanest of the plain TCP wrappers and the only one whose TLS warning is honest about doing nothing by default. Five years without a commit makes it a reference implementation, not a recommendation. TLS mode needs a certificate at the server end.
- evidence note: nothing would raise the maintenance rung; the last code change was 2020 and the last release tag is 'beta' from 2021
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "Proxy wireguard UDP packets over TCP/TLS"; client mode listens on 127.0.0.1:51820 by default and the WireGuard peer points at it
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: server daemon pipes to the local WireGuard UDP port
  - hosting_requirement: a publicly reachable host running the server daemon, plus the client daemon on the device
  - last_release: beta 2021-05-22
  - stars: 96
- evidence:
  - [1] 2026-10-23: the two modes and the -uh default of 127.0.0.1:51820 in client mode
  - [1] 2026-10-23: release tag 'beta' published 2021-05-22; last push 2020-11-27; 96 stars
  - [1] 2026-10-23: "--tls WARNING: authenticates/verifies nothing without --pinnedpubkey below!!"
- sources:
  - [1] https://github.com/moparisthebest/wireguard-proxy
