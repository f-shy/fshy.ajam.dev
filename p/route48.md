# route48.org

> route48.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/route48/ | JSON https://fshy.ajam.dev/api/v1/entity/route48.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## route48.org

- `egress/route48-org` | dead | evidence documented | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://route48.org/
- price USD 0
- free tier: the read of https://route48.org/ on 2026-10-23 returned final_url https://bgptunnel.com/ with the title 'Home' and the description 'BGPTunnel.com offers free IPv4 and IPv6 Transit via GRE Tunnels in various locations for non-commercial and personal networks via AS209533' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not applicable: the host now serves another provider's page; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: not established: no route48 signup page is reachable, the host redirects to bgptunnel.com | country: None
- interface: unknown
- binding note: The provider as an independent broker no longer answers; nothing binds at any volume. What is left at the domain is BGPTunnel.com, which requires an ASN and its own prefix, and that is recorded separately.
- interface detail: not established
- tooling: not applicable
- composes with: the same as tooling
- reliability: domain now serves a different provider; any published route48 configuration is stale.
- notes: The 2022 r/ipv6 thread that named it is the reason it is checked at all. Both names in that thread now point at the same successor network: route64.org is live and independent, route48.org is not.
- evidence note: documented from today's read: the domain resolves to another provider's page. Whether route48 moved, merged or was absorbed is not stated anywhere read; only that its own service is no longer served.
- extras:
  - wg_path: unknown
  - wg_detail: not established for route48 itself; the handwiki list credited it with GRE, BIRD, WireGuard and ZeroTier
  - ingress: none
  - volume_stated: not applicable: the host now serves another provider's page
  - bytes_transit: no
  - transit_note: not applicable
- evidence:
  - [1] 2026-10-23: read returned final_url https://bgptunnel.com/ with the BGPTunnel description, not route48 content
  - [2] 2026-10-23: listed as active in 2024 with '/48 Automated, /44 Free Ripe Assignement' and GRE, BIRD, WireGuard, ZeroTier
  - [3] 2026-10-23: recommended in 2022 as an alternative to Hurricane Electric alongside route64.org
- sources:
  - [1] https://route48.org/
  - [2] https://handwiki.org/wiki/List_of_IPv6_tunnel_brokers
  - [3] https://www.reddit.com/r/ipv6/comments/y896f2/
