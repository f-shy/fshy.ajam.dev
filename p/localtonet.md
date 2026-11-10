# Localtonet

> localtonet.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localtonet/ | JSON https://fshy.ajam.dev/api/v1/entity/localtonet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Localtonet

- `egress/localtonet` | fails-quota | evidence documented | binding volume-quota | category udp port forward (hosted, multi-protocol) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://localtonet.com/
- price USD 0
- free tier: 1 HTTP/TCP/UDP Tunnel, 1 GB Bandwidth / month, 30 min Tunnel Timeout | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 GB bandwidth per month on the free plan; paid tunnels are sold as unlimited bandwidth; ingress: udp | metered: yes | free allowance: 1 GB bandwidth per month on the free plan; paid tunnels are sold as unlimited bandwidth | source: [1]
- identity: email | detail: an account and an AuthToken per client: 'Select the AuthToken you entered in the Localtonet App' https://localtonet.com/documents/udp | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 GB bandwidth per month [1]
  - retention-clamped: 30 min tunnel timeout on the free plan [1]
- binding note: 1 GB is 0.0009 TiB; the 30-minute timeout would kill a WireGuard endpoint anyway, so two limits fail before the month is out.
- interface detail: localtonet --headless --authtoken-file, plus a web dashboard that creates the tunnel
- tooling: localtonet client for Windows, macOS, Linux, Android, Docker
- composes with: not composable: a 30-minute UDP port is not an endpoint any peer can keep in a config
- reliability: free tunnels are dropped every 30 minutes and the public port can change on restart
- notes: UDP is a first-class free protocol, which is why it was worth reading. Both the quota and the port stability disqualify it.
- evidence note: The two failing numbers are on the vendor's own pricing block and in its own plan comparison; the community reply repeats the 30-minute figure.
- extras:
  - wg_path: none
  - wg_detail: the free plan's port is not fixed: the vendor's own comparison table gives the free plan 'Tunnel Server Port | May change on restart' and reserves a stable port for the paid plan
  - ingress: udp
  - volume_tib_month: 0.000909
  - volume_stated: 1 GB bandwidth per month on the free plan; paid tunnels are sold as unlimited bandwidth
  - bytes_transit: yes
  - transit_note: the Localtonet relay carries the datagrams
- evidence:
  - [1] 2026-10-23: free plan: 1 HTTP/TCP/UDP tunnel, 1 GB bandwidth per month, 30 min tunnel timeout; paid plan: unlimited bandwidth, no tunnel timeout, custom domains and ports
  - [2] 2026-10-23: 'UDP tunnels allows you to expose any local network services running over UDP protocol', with an IP and port chosen per tunnel
  - [3] 2026-10-23: vendor table: free plan 'Tunnel Server Port: May change on restart', paid 'Reserved'
- sources:
  - [1] https://localtonet.com/
  - [2] https://localtonet.com/documents/udp
  - [3] https://localtonet.com/blog/introducing-pay-as-you-go-pricing-for-localtonet
