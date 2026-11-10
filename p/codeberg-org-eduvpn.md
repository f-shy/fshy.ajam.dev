# proxyguard

> codeberg.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codeberg-org-eduvpn/ | JSON https://fshy.ajam.dev/api/v1/entity/codeberg-org-eduvpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## proxyguard

- `egress/proxyguard` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://codeberg.org/eduVPN/proxyguard
- price USD 0
- free tier: no service and no account; MIT-licensed client and server, packaged in the eduVPN server repository | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account for the tool; the eduVPN ecosystem around it issues accounts separately | country: None
- interface: cli
- binding note: the constraint is a server host, mitigated by the fact that it is designed to sit behind a reverse proxy on an existing HTTPS port
- interface detail: proxyguard-client --to http://host ; proxyguard-server --listen --to
- tooling: make install adds systemd units; DEB and RPM packages in the eduVPN repo
- composes with: rides any HTTPS reverse proxy, so it composes with a host that already serves a website and with a CDN that passes an Upgrade header.
- reliability: client requires TLS 1.3 or newer; on Linux --fwmark may be needed to avoid a routing loop, and that flag needs root or CAP_NET_ADMIN
- notes: Reverse proxy software wrapping WireGuard over TCP, maintained for eduVPN deployments. Shares port 443 with HTTPS web servers via HTTP Upgrade headers.
- evidence note: a measured run through an nginx or HAProxy front would raise it; eduVPN publishes deployment docs but no throughput figure
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: client listens on 127.0.0.1:51821 and the WireGuard config sets Endpoint = 127.0.0.1:51821; server runs 'proxyguard-server --listen 0.0.0.0:51821 --to 127.0.0.1:51820'
  - ingress: tcp
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: through the server half, which forwards to the local WireGuard port
  - hosting_requirement: a server host with an HTTP listener, preferably behind a reverse proxy on 443; a user half runs on the device
  - last_release: 2.1.1 2026-08-26
- evidence:
  - [2] 2026-10-23: "proxy UDP connections over HTTP(s). The main use case is to proxy WireGuard packets" and "This proxy thus needs to run for every client and for a server"
  - [2] 2026-10-23: "This project started with a UDP to TCP approach, but later moved to HTTP for use behind a reverse proxy"
  - [3] 2026-10-23: release 2.1.1 published 2026-08-26
  - [2] 2026-10-23: "The goal of this project is NOT to work around intentional state/organizational network blocks/censorship"
- sources:
  - [1] https://codeberg.org/eduVPN/proxyguard
  - [2] https://codeberg.org/eduVPN/proxyguard/raw/branch/main/README.md
  - [3] https://codeberg.org/eduVPN/proxyguard/releases
