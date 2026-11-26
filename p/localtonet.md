# Localtonet

> localtonet.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localtonet/ | JSON https://fshy.ajam.dev/api/v1/entity/localtonet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Localtonet

- `egress/localtonet` | fails-quota | evidence documented | binding volume-quota | category udp port forward (hosted, multi-protocol) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T17:26:44.696Z (live) | stale on 2026-12-26
- url https://localtonet.com/
- price USD 0
- free tier: 1 tunnel of any type; 1 GB of bandwidth per 30 days; TCP, UDP, TLS and proxy tunnels stop after 30 minutes per start, while HTTP, File Server and MCP Gateway tunnels have no time limit. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: 1 GB of bandwidth per 30 days on the free plan; paid tunnels have unlimited bandwidth that is never billed. | metered: yes | free allowance: 1 GB of bandwidth per 30 days on the free plan. | source: [1]
- identity: email | detail: an account and an AuthToken per client: 'Select the AuthToken you entered in the Localtonet App' https://localtonet.com/documents/udp | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB per 30 days [1]
  - retention-clamped: 30 minutes per start for TCP, UDP, TLS and proxy tunnels; HTTP, File Server and MCP Gateway tunnels have no time limit [1]
- binding note: The free grant is 1 GB per 30 days; TCP, UDP, TLS and proxy tunnels also stop after 30 minutes per start, which a restart clears, so the quota is the limit a restart does not clear.
- interface detail: localtonet --headless --authtoken-file, plus a web dashboard that creates the tunnel
- tooling: localtonet client for Windows, macOS, Linux, Android, Docker
- composes with: not composable: a 30-minute UDP port is not an endpoint any peer can keep in a config
- reliability: TCP, UDP, TLS and proxy tunnels stop after 30 minutes per start; the server port is not reserved on the Free plan, so it can change when the tunnel starts again.
- notes: UDP is a first-class free protocol, which is why it was worth reading. Both the quota and the port stability disqualify it.
- evidence note: The two failing numbers are on the vendor's own pricing block and in its own plan comparison; the community reply repeats the 30-minute figure.
- extras:
  - wg_path: none
  - wg_detail: the free plan's port is not fixed: the vendor's own comparison table gives the free plan 'Tunnel Server Port | May change on restart' and reserves a stable port for the paid plan
  - ingress: udp
  - volume_tib_month: 0.000909
  - volume_stated: 1 GB bandwidth per 30 days on the free plan; paid tunnels have unlimited bandwidth that is never billed
  - bytes_transit: yes
  - transit_note: the Localtonet relay carries the datagrams
- evidence:
  - [2] 2026-10-23: free plan: 1 HTTP/TCP/UDP tunnel, 1 GB bandwidth per month, 30 min tunnel timeout; paid plan: unlimited bandwidth, no tunnel timeout, custom domains and ports
  - [3] 2026-10-23: 'UDP tunnels allows you to expose any local network services running over UDP protocol', with an IP and port chosen per tunnel
  - [4] 2026-10-23: vendor table: free plan 'Tunnel Server Port: May change on restart', paid 'Reserved'
  - [1] 2026-11-25: the free plan's tunnel count, allowance, timeout and the tunnelled types without one | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free plan's own description on the pricing page | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free allowance period and the paid plan's unbilled bandwidth | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free plan's allowance and the paid plan's unbilled bandwidth | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free allowance period | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the timeout applies only to some tunnel types | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [3] 2026-11-25: an unreserved free port changes when the tunnel starts again | capture: sha256:87bec25d457c94c6654cb56855786335a0e08457bd10909c86b7af103e7944d6 | quote: The server port is not reserved on the Free plan, so it can change when the tunnel starts again.
  - [1] 2026-11-25: the free allowance and the timeout | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free plan's tunnel count, allowance and timeout | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [1] 2026-11-25: the free allowance period and the limited tunnel types | capture: sha256:64193fb662ceb7f2b26ea51505b9295d652eb192f54ee7343188c91e30744653 | quote: The free plan allows one tunnel and 1 GB of bandwidth per 30 days. TCP, UDP, TLS and proxy tunnels stop after 30 minutes and can be started again. HTTP, File Server and MCP Gateway tunnels have no time limit.
  - [3] 2026-11-25: the free port changes when the tunnel starts again | capture: sha256:87bec25d457c94c6654cb56855786335a0e08457bd10909c86b7af103e7944d6 | quote: The server port is not reserved on the Free plan, so it can change when the tunnel starts again.
  - [3] 2026-11-25: the free plan carries UDP tunnels | capture: sha256:87bec25d457c94c6654cb56855786335a0e08457bd10909c86b7af103e7944d6 | quote: UDP tunnels count as TCP/UDP tunnels for the Free session limit: they stop after 30 minutes.
- sources:
  - [1] https://localtonet.com/pricing
  - [2] https://localtonet.com/
  - [3] https://localtonet.com/documents/udp
  - [4] https://localtonet.com/blog/introducing-pay-as-you-go-pricing-for-localtonet
