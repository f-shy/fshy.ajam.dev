# tunnel64

> tunnel64.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnel64/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnel64.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnel64

- `egress/tunnel64` | qualifies-with-caveat | evidence documented | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:00.066Z (live) | stale on 2026-12-05
- url https://tunnel64.net/
- price USD 0
- free tier: Static routed /64 per tunnel, up to 5 tunnels per account, 100 Mbit/s per tunnel, dynamic IPv4 endpoint updates (dyndns2), self-service reverse DNS (PTR) - 0 kr / forever | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no traffic allowance is stated for the free tunnel; 'Unlimited traffic' is listed on the paid VPN plan, not on the free tunnel plan; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'Create an account at free.tunnel64.net and tell us the public IPv4 you connect from.' The paid VPN advertises 'Email-only signup - no name, no phone'; the free tunnel page states no field list. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 100 Mbit/s per tunnel [1]
- binding note: 100 Mbit/s is about thirty times the 3.24 Mbit/s that 1 TiB/month needs, and no byte quota is published, so nothing in the vocabulary fails at that volume. The real gate is protocol 41 reachability plus a public IPv4, and reachability is IPv6-only for the reader.
- interface detail: 'Copy the generated config - plain Linux, OpenWrt, or Windows. Standard 6in4, no client software'
- tooling: four ip commands on Linux or a pasted router config; ddclient for the dyndns2 endpoint
- composes with: needs a host with its own public IPv4, so it fits a free VM with an IPv4 address rather than one behind NAT.
- reliability: 'Outbound port 25 is blocked by default' on the VPN side; the free tunnel plan publishes no SLA.
- notes: Run on AS35100 from Sweden and the Philippines. A routed /48 tier is announced but not on sale. The free tier has no WireGuard, so a client that cannot receive protocol 41 gets nothing here; the paid VPN is the WireGuard path and it is priced, not free.
- evidence note: documented from the vendor page read. No WireGuard on the free tier is the fact most worth re-checking, because the provider sells a WireGuard VPN next door.
- extras:
  - wg_path: none
  - wg_detail: the free tier is 6in4 only: 'Standard 6in4, no client software'. WireGuard exists on the paid VPN product ('WireGuard, on the same AS35100 hardware'), not on the free tunnel.
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is stated for the free tunnel; 'Unlimited traffic' is listed on the paid VPN plan, not on the free tunnel plan
  - bytes_transit: yes
  - transit_note: AS35100 terminates the tunnel on hardware the operator says it runs itself.
- evidence:
  - [1] 2026-10-23: 'Static routed /64 per tunnel', 'Up to 5 tunnels per account', '100 Mbit/s per tunnel', '0 kr / forever'
  - [1] 2026-10-23: 'Standard 6in4, no client software, works on almost any router.'
  - [2] 2026-10-23: 'Sign up, tell us your public IPv4, and get a static point-to-point address plus a routed /64 for your whole LAN.'
  - [1] 2026-10-23: a /48 plan is 'coming soon' and the VPN is a separate paid product
  - [1] 2026-11-03: the free tunnel plan is shaped to 100 Mbit/s per tunnel | capture: sha256:e04c584d47122a975df5f60894a8c37fdd8ff334c8f3e7c00ac284eb5f8ec177 | quote: 100 Mbit/s per tunnel
  - [1] 2026-11-03: the paid VPN Standard plan lists unlimited traffic; the Free tunnel plan lists no traffic line | capture: sha256:e04c584d47122a975df5f60894a8c37fdd8ff334c8f3e7c00ac284eb5f8ec177 | quote: Unlimited traffic
  - [1] 2026-11-04: the free plan lists 100 Mbit/s per tunnel | capture: sha256:22be2d69cded1ac2ffcef84d8765a60cdcd870cf1c5c9e18ded677eab6d2a3cd | quote: 100 Mbit/s per tunnel
- sources:
  - [1] https://tunnel64.net/
  - [2] https://free.tunnel64.net/
