# onlySSH UDP Tunnel

> onlyssh.my.id | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onlyssh/ | JSON https://fshy.ajam.dev/api/v1/entity/onlyssh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## onlySSH UDP Tunnel

- `egress/onlyssh` | fails-egress | evidence documented | binding none | category proxy account (not a port forward) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://onlyssh.my.id/udp-tunnel
- price USD 0
- free tier: Free UDP Tunnel: select a server country and get a UDP tunnel account | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no allowance is published on the selection page; the service hands out per-country proxy accounts; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: an account is issued per server country through the site | country: None
- interface: cli
- binding note: Nothing binds because the offer is not ingress: there is no public address and port that reaches a service run locally.
- interface detail: per-country proxy account with VLESS ws and VMess ws paths
- tooling: a VLESS or VMess client
- composes with: an outbound proxy composes with a crawler or an egress lane, not with an ingress lane
- reliability: single small site; accounts are handed out without stated capacity
- notes: Provides outbound SSH and UDP proxy tunnels for client internet access. Does not provide inbound public port forwarding or reverse tunneling.
- extras:
  - wg_path: none
  - wg_detail: the product is a QUIC-based proxy account (VLESS and VMess endpoints), which is a client-side outbound proxy, not a public port forwarded to a service run locally
  - ingress: none
  - volume_stated: no allowance is published on the selection page; the service hands out per-country proxy accounts
  - bytes_transit: yes
  - transit_note: the operator relays outbound proxy traffic
- evidence:
  - [1] 2026-10-23: 'UDP Tunnel is a feature-packed proxy & relay tool' with per-country accounts, and VLESS/VMess path options
- sources:
  - [1] https://onlyssh.my.id/udp-tunnel
