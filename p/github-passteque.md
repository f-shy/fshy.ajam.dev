# gluetun

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-passteque/ | JSON https://fshy.ajam.dev/api/v1/entity/github-passteque.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gluetun

- `egress/gluetun` | self-hosted, last resort | verdict paid-only | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution yes | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/passteque/gluetun
- price USD 0
- free tier: no service and no account; a Docker container that connects to a VPN provider the operator has an account with | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the volume is the provider's, not the container's; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: institution | detail: a subscription with one of the listed VPN providers is what it exists to consume; the custom provider path needs no gluetun account but the endpoint still needs one | country: None
- interface: cli
- binding note: gluetun adds no limit and no path: it is a consumer of somebody else's tunnel, so the binding constraint lives in the provider record
- interface detail: Docker environment variables, plus built-in SOCKS5, Shadowsocks and HTTP proxies
- tooling: Docker image qmcgaw/gluetun; compose or docker run
- composes with: takes a .conf from any provider record in this topic and republishes it as SOCKS5 or Shadowsocks inside a Docker network.
- reliability: the built-in firewall kill switch blocks traffic when the tunnel drops, by design
- notes: VPN client container routing network traffic through OpenVPN and WireGuard connections, providing local SOCKS5 and Shadowsocks proxies. Operates as a routing container rather than an external transport encapsulation service.
- evidence note: nothing here is about gluetun's own numbers; the rung that matters belongs to the provider it dials
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: "For custom Wireguard configurations using the custom provider", so an ordinary .conf is its input
  - ingress: none
  - volume_stated: not applicable; the volume is the provider's, not the container's
  - bytes_transit: yes
  - transit_note: through whichever VPN provider is configured
  - hosting_requirement: a Docker host; the tunnel itself is the provider's
  - last_release: v3.41.3 2026-07-30
  - stars: 15857
- evidence:
  - [1] 2026-10-23: "For custom Wireguard configurations using the custom provider" and "Supports Wireguard both kernelspace and userspace"
  - [1] 2026-10-23: built-in Shadowsocks, SOCKS5 and HTTP proxies that tunnel through the VPN
  - [1] 2026-10-23: release v3.41.3 published 2026-07-30; last push 2026-10-21; 15857 stars; repo moved to passteque/gluetun
  - [1] 2026-10-23: "Choose the vpn network protocol, udp or tcp"
- sources:
  - [1] https://github.com/passteque/gluetun
