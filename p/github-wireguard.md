# wireguard-go

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-wireguard/ | JSON https://fshy.ajam.dev/api/v1/entity/github-wireguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wireguard-go

- `egress/wireguard-go` | self-hosted, last resort | verdict fails-egress | evidence documented | binding none | category tool (wireguard transport) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://github.com/WireGuard/wireguard-go
- price USD 0
- free tier: no service and no account; the reference userspace implementation | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable; the software states no volume; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account | country: None
- interface: cli
- binding note: it creates a TUN interface and speaks UDP; a UDP block stops it, so it adds no egress path
- interface detail: wireguard-go wg0, configured with wg(8)
- tooling: go build; wg and wg-quick for configuration
- composes with: the substrate for the WebSocket forks; on its own it composes only with a peer that accepts UDP.
- reliability: upstream mirror lags git.zx2c4.com; the Linux kernel module is the faster path where it exists
- notes: Userspace implementation of WireGuard in Go. Serves as a standard WireGuard network interface on platforms without native kernel support. Standard implementation uses UDP transport.
- evidence note: the verdict concerns egress only; this is the implementation every WebSocket fork starts from
- self hosted: yes
- extras:
  - wg_path: native-conf
  - wg_detail: "With wireguard-go, instead simply run: wireguard-go wg0 ... When an interface is running, you may use wg(8) to configure it", so the standard configuration applies unchanged
  - ingress: none
  - volume_stated: not applicable; the software states no volume
  - bytes_transit: yes
  - transit_note: carries the tunnel over UDP to the configured endpoint
  - hosting_requirement: none beyond the device; needs a reachable UDP peer
  - last_release: no GitHub release objects; last push 2026-10-06
  - stars: 4465
- evidence:
  - [1] 2026-10-23: "This is an implementation of WireGuard in Go" and the wireguard-go wg0 / wg(8) usage
  - [1] 2026-10-23: "Mirror only. Official repository is at https://git.zx2c4.com/wireguard-go"; 4465 stars; last push 2026-10-06; no GitHub releases
  - [1] 2026-10-23: on Linux the README says to use the kernel module instead, "which is faster and better integrated into the OS"
- sources:
  - [1] https://github.com/WireGuard/wireguard-go
