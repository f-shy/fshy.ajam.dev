# SteadIP Anchor

> steadip.com | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/steadip/ | JSON https://fshy.ajam.dev/api/v1/entity/steadip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SteadIP Anchor

- `egress/steadip-anchor` | paid-only | evidence documented | binding volume-quota | category dedicated IPv4 over WireGuard | tier anchor
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://blog.steadip.com/2026/08/14/introducing-steadip-anchor-your-own-dedicated-ipv4-for-29-99-year/
- price USD 29.99 per year per dedicated IPv4 (about USD 2.50 per month) | parsed USD 2.5/mo
- free tier: The free SteadIP tier supports HTTP and HTTPS only: "Free users get a random subdomain" and "SteadIP focuses on HTTP and HTTPS first". Dedicated IPv4 is paid: "$29.99 USD per dedicated IPv4 address, billed annually." | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No transfer allowance and no fair-use figure are published in the announcement, the product explainer or the homepage. The plan is priced per address per year only.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: A SteadIP account plus a paid annual add-on; the site sells a separate "Verified" tier at USD 19.99 per year, which suggests verification is a paid product rather than an identity check. The signup form was not read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): unpublished [2]
- binding note: Nothing published fails at 1 TiB/month except an unknown volume policy, so the honest answer is that the wall is undocumented. At USD 29.99 per year for a whole IPv4 the price is not the wall.
- interface detail: Config file plus a customer panel for ports and an optional hostname.
- tooling: wg-quick; an optional hostname under steadip.com
- composes with: Pairs with the vendor's own free HTTP tunnel: one address for raw TCP and UDP, one hostname for the website.
- reliability: Nothing published on throttling, bans or drop behaviour; the free HTTP tier and the paid Anchor product share a vendor whose main product is an frp-based tunnel.
- notes: Cheapest whole IPv4 found at USD 29.99 per year, and the only one whose free tier is honestly HTTP-only rather than an IPv6 substitute. Which inbound mode the Anchor add-on gets is not stated, and that decides whether every port is open or a few are forwarded.
- evidence note: Price, the config file and both inbound modes are first-party. Two gaps: which mode the Anchor add-on includes, and any volume figure. A support question would close both.
- extras:
  - wg_path: native-conf
  - wg_detail: "We provide a WireGuard config. You import it on a router, server, VM, or even a desktop." Inbound is either selected ports or all of them: "Port forwarding: forward only the ports you want" or "Forward all ports (1:1 NAT): true full inbound reachability (all ports)".
  - ingress: tcp+udp
  - volume_stated: No transfer allowance and no fair-use figure are published in the announcement, the product explainer or the homepage. The plan is priced per address per year only.
  - bytes_transit: yes
  - transit_note: The vendor's gateway carries the address and terminates the tunnel; the local ISP only sees outbound.
- evidence:
  - [2] 2026-10-23: USD 29.99 per year per dedicated IPv4, about USD 2.50 per month; the address is assigned to the account rather than shared
  - [3] 2026-10-23: WireGuard config supplied by the vendor; Starter forwards selected ports, Pro and Business offer 1:1 NAT for all ports
  - [1] 2026-10-23: the free tier is HTTP and HTTPS with a random subdomain; the paid tunnel tier is USD 19.99 per year
- sources:
  - [1] https://steadip.com/
  - [2] https://blog.steadip.com/2026/08/14/introducing-steadip-anchor-your-own-dedicated-ipv4-for-29-99-year/
  - [3] https://blog.steadip.com/2026/02/16/steadip-dedicated-public-ipv4-over-wireguard-port-forwarding-or-true-11-nat/

## SteadIP

- `egress/steadip` | fails-egress | evidence documented | binding write-gated | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://steadip.com/
- price USD 0
- free tier: Free HTTP/HTTPS tunnels. Verified features for $19.99 USD/year. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is published for either tier. The free tier is described as random subdomains over HTTP/HTTPS.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The client command is steadip login against a free account; the TCP/UDP page says the managed layer is available to verified users, and the site prices verified features at USD 19.99 per year. | country: None
- interface: cli
- limits:
  - write-gated (binding): TCP and UDP tunnels require the verified tier at USD 19.99/year [2]
  - volume-quota: no byte allowance published [1]
- binding note: A verification step and a payment stand between an account and a UDP port, so nothing about volume matters until that gate is passed.
- interface detail: steadip login then steadip up, configured through the dashboard.
- tooling: curl -fsSL https://steadip.com/install-linux.sh | sh; steadip login; steadip up.
- composes with: Free tier fronts a web app on a free VM; UDP needs the paid verified tier, at which point a cheap VPS with frp is comparable in cost.
- reliability: Managed FRP instance shared across customers.
- notes: SteadIP requires paid subscription verification before activating TCP and UDP port forwarding.
- evidence note: Reading the pricing page failed twice (504, then a page with no numbers); a checkout walk would establish the verified tier's actual byte allowance.
- extras:
  - wg_path: inside-udp
  - wg_detail: The managed gateway is FRP-based and the page says frp supports TCP and UDP proxy types, with TCP and UDP options selectable, but only for verified users. On the free tier there is no UDP listener.
  - ingress: http-only
  - volume_stated: No byte allowance is published for either tier. The free tier is described as random subdomains over HTTP/HTTPS.
  - bytes_transit: yes
  - transit_note: A SteadIP-managed FRP gateway receives public traffic and forwards it down the outbound tunnel.
- evidence:
  - [1] 2026-10-23: Free HTTP/HTTPS tunnels; verified features for $19.99 USD/year; free users get a random subdomain.
  - [2] 2026-10-23: Managed FRP gateway with TCP and UDP options, available to verified users; examples include SSH, game and voice services and UDP telemetry.
- sources:
  - [1] https://steadip.com/
  - [2] https://steadip.com/tcp-udp-tunnel
