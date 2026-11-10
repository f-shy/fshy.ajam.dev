# OpenTunnel Free WireGuard Singapore

> opentunnel.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opentunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/opentunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenTunnel Free WireGuard Singapore

- `egress/opentunnel-wireguard-singapore` | trial-only | evidence documented | binding retention-clamped | category wireguard endpoint (hosted, Singapore) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://opentunnel.net/wireguard-server-102/
- price USD 0
- free tier: 'Free WireGuard Singapore SGC 1', 'This WireGuard server location in Singapore with daily account limit 50. You can surf with unlimited data and high-speed connections on these servers.' | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Unlimited data' per the page. The account itself is 'Active: 7 Days'.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'daily account limit 50' per server. The page issues a username and a configuration from a form; no email, card or phone step is described. | country: None
- interface: cli
- limits:
  - retention-clamped (binding): 'Active: 7 Days' [1]
  - request-rate: 'daily account limit 50' [1]
- binding note: Unlimited data is stated, so volume does not bind. The 7-day account life binds first, and before that the outbound-only topology does: the peer gets a private address inside the provider's network, not a public port.
- interface detail: A web form issues the peer configuration; the page lists host, UDP port and account life for a standard WireGuard client.
- tooling: any WireGuard client; the .conf is issued by the page
- composes with: Gives a Singapore exit address to a client that has none; it does not give a Singapore ingress, so it cannot front a service.
- reliability: Accounts expire after 7 days and 50 are issued per server per day; torrent, DDoS and spam are refused on the page; the site is ad-funded and carries a live traffic counter.
- notes: Generates free WireGuard client configurations with Singapore exit endpoints. Operates as an outbound VPN client endpoint behind provider NAT; inbound connections from external networks are not supported.
- evidence note: Host, port, account life and the unlimited-data sentence are on the page read on 2026-10-23.
- extras:
  - wg_path: registration-api
  - wg_detail: 'Host: wg-sg-2.optnl.com', 'UDP Port: 51820', 'Active: 7 Days'. The page issues the peer configuration on submission; there is no account to log into afterwards.
  - ingress: none
  - volume_stated: 'Unlimited data' per the page. The account itself is 'Active: 7 Days'.
  - bytes_transit: yes
  - transit_note: The provider's Singapore host relays the peer's traffic out.
- evidence:
  - [1] 2026-10-23: 'Free WireGuard Singapore SGC 1', 'daily account limit 50', 'You can surf with unlimited data and high-speed connections on these servers.'
  - [1] 2026-10-23: 'Host: wg-sg-2.optnl.com', 'UDP Port: 51820', 'Active: 7 Days', and a counter showing 21,210 accounts created on that server.
- sources:
  - [1] https://opentunnel.net/wireguard-server-102/
