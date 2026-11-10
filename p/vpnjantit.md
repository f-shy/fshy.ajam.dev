# VPN Jantit Free SSH Singapore

> vpnjantit.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpnjantit/ | JSON https://fshy.ajam.dev/api/v1/entity/vpnjantit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPN Jantit Free SSH Singapore

- `egress/vpnjantit-ssh-singapore` | trial-only | evidence documented | binding retention-clamped | category ssh tunnel account (hosted, Singapore) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.vpnjantit.com/free-ssh-singapore
- price USD 0
- free tier: 'Free SSH Tunnel Singapore Servers. Support for Windows, Android, Linux, Iphone etc. Active up to 7 days with unlimited bandwidth.' | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'unlimited bandwidth' per the page description; the accounts themselves are 'Active 1 Days' on the Singapore 1 and 5 servers, against 'up to 7 days' in the overview.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The page offers 'Create Username SSH Tunnel' and the site description says 'create username and password whatever you want'; no email confirmation is described on the page read. | country: None
- interface: ssh
- limits:
  - retention-clamped (binding): 'Active 1 Days' on the Singapore 1 and 5 servers; 'up to 7 days' in the overview [1]
- binding note: Bandwidth is stated unlimited, so volume does not bind. The one-day account life binds first, and the ingress test is not passed at all: the account is an outbound proxy, and SSH remote forwarding would need GatewayPorts enabled on the provider's host, which the page does not state.
- interface detail: 'Port 22(OpenSSH)', '81,444-SSL(Dropbear)', 'Support UDP CUSTOM port 1-65535', 'Support SlowDNS', 'WebSocket CDN (Port 80)', '446,7200 BADVPN UDPGW'.
- tooling: any SSH client; Dropbear on 81 and 444, SlowDNS, WebSocket on 80, BADVPN UDPGW on 7200 and 446
- composes with: A one-day Singapore SSH account is a cheap way to test whether SSH remote forwarding is permitted, which would make it an ingress path that needs no card and no VM.
- reliability: Accounts reset daily at 21:00 GMT+7 and some servers are full; torrent is refused; the offering is ad-funded with affiliate links to DigitalOcean and Vultr.
- notes: The second Singapore data point and the cheaper shape of the same idea: a free SSH login on a DigitalOcean or Vultr host in Singapore, no email, one day. It is an outbound proxy. The interesting untested question is whether the host permits SSH remote forwarding, which would turn a free account into a TCP ingress without local hardware; that is a probe, not a read. Country of endpoint: Singapore. Operator: the same Indonesian account-generator network class as OpenTunnel. Several Singapore servers showed 'Server Full' at read time.
- evidence note: Hosts, ports, account life and the unlimited-bandwidth sentence are on the page read on 2026-10-23.
- extras:
  - wg_path: none
  - wg_detail: An SSH login on a public Singapore address, not a WireGuard peer: no .conf is issued and the host is not controlled, so no WireGuard interface can be created on the far side.
  - ingress: none
  - volume_stated: 'unlimited bandwidth' per the page description; the accounts themselves are 'Active 1 Days' on the Singapore 1 and 5 servers, against 'up to 7 days' in the overview.
  - bytes_transit: yes
  - transit_note: A rented Singapore host (the page names DigitalOcean and Vultr) carries the bytes.
- evidence:
  - [1] 2026-10-23: 'Free SSH Tunnel Singapore Servers', 'Active up to 7 days with unlimited bandwidth', 'Free SSH Tunnel will reset at 21:00 GMT+7'.
  - [1] 2026-10-23: Server Singapore 1: 'sg1.vpnjantit.com', 'Port 22(OpenSSH)', 'Support UDP CUSTOM port 1-65535', 'BADVPN UDPGW', 'Active 1 Days', 'Provider DIGITALOCEAN'.
- sources:
  - [1] https://www.vpnjantit.com/free-ssh-singapore
