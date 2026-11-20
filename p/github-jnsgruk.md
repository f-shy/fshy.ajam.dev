# wireguard-over-wss

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jnsgruk/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jnsgruk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wireguard-over-wss (jnsgruk)

- `egress/wireguard-over-wss` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/jnsgruk/wireguard-over-wss
- price USD 0
- free tier: no service and no account; it is a configuration recipe plus a shell script | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the recipe states no volume; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account; the server is a droplet the recipe assumes the reader already has | country: None
- interface: cli
- binding note: the constraint is the same host as wstunnel, since this project adds no code of its own; the recipe says 'droplet'
- interface detail: wstunnel plus /etc/wireguard/wss.wstunnel
- tooling: wstunnel binary, wg-quick, wstunnel.sh
- composes with: identical to wstunnel: needs a server host, then rides a websocket-capable forwarder.
- reliability: the client script edits /etc/hosts and reloads dnsmasq; a stale entry survives a failed tunnel start
- notes: Automated deployment script wrapping WireGuard over WebSocket using wstunnel. Configures systemd unit files and endpoint resolution scripts.
- evidence note: nothing to raise: it is a recipe whose only executable part is wstunnel, which is recorded on its own rung
- self hosted: yes
- extras:
  - wg_path: none
  - wg_detail: "Wireguard VPN connection to be tunnelled over a secure websockets connection"; the recipe runs wstunnel, not new software: 'wstunnel server wss://0.0.0.0:443 --restrict-to 127.0.0.1:51820'
  - ingress: tcp
  - volume_stated: not applicable; the recipe states no volume
  - bytes_transit: yes
  - transit_note: the same bytes as wstunnel, through a host the reader is assumed to rent
  - hosting_requirement: a server host with wstunnel and the WireGuard listener, described in the recipe as a droplet
  - last_release: none; last push 2024-07-01
  - stars: 220
- evidence:
  - [1] 2026-10-23: "No modifications need to be made to the Wireguard server configuration itself, but wstunnel needs to be installed", and the systemd unit with --restrict-to 127.0.0.1:51820
  - [1] 2026-10-23: 220 stars, no releases, last push 2024-07-01
- sources:
  - [1] https://github.com/jnsgruk/wireguard-over-wss
