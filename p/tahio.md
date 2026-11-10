# tahio TunnelBroker

> tahio.eu | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tahio/ | JSON https://fshy.ajam.dev/api/v1/entity/tahio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tahio TunnelBroker

- `egress/tahio-tunnelbroker` | qualifies-with-caveat | evidence documented | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:00.066Z (live) | stale on 2026-12-05
- url https://tb.tahio.eu/
- price USD 0
- free tier: SIT, GRE and WireGuard tunnels with BGP-routed /48s. Free, dual-stack, dyndns2-ready. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no monthly byte allowance is published; the fair-use section caps speed instead: '50 Mbit/s up + down, kernel-shaped'; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: https://tb.tahio.eu/sign-up asks for Email, Password and Full Name, with Nickname optional; no card and no phone field. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 50 Mbit/s up and down, kernel-shaped, per tunnel [1]
  - per-ip-shaping: SYN-flood and ICMP rate limits applied per tunnel automatically [1]
- binding note: At 1 TiB/month the requirement is 3.24 Mbit/s sustained; the 50 Mbit/s cap is about fifteen times that, so the speed limit does not bind at this volume and no byte quota exists. What actually constrains a workload here is the blocked-port list, which the seven kinds do not name: 'SMTP - 25 - 465 - 587 - 2525' and 'POP3/IMAP - 110 - 143 - 993 - 995' are closed, so a mail service on this prefix cannot work. Reachability is IPv6-only.
- interface detail: the site hands out SIT, GRE and WireGuard configuration; a dyndns2 endpoint updater is offered per tunnel for dynamic IPv4
- tooling: wg-quick or wireguard-tools; a plain SIT/GRE interface for the other two transports
- composes with: a native WireGuard profile with no dashboard step makes it the cheapest way to put a free compute instance on a public IPv6 address with every port open.
- reliability: no SLA: 'No SLA, no uptime guarantee.' Abuse, spam or scanning gives 'instant termination, no warning.'
- notes: The page contradicts itself on prefix size: the headline says 'BGP-routed /48s' while the network section says 'Each tunnel gets two /64s from the primary pools plus a /64 from a tertiary.' The /64 arithmetic is the concrete statement and the /48 is unexplained, so the record carries three /64s and flags the /48 as unestablished. AS198889, single PoP in Oslo, peered with Gigahost.
- evidence note: documented from the vendor page read, including a full WireGuard profile. A measured rung needs a tunnel brought up and a UDP service reached through it, which needs an account.
- extras:
  - wg_path: native-conf
  - wg_detail: the page publishes a complete WireGuard profile with 'Endpoint = tb.tahio.eu:51820', AllowedIPs ::/0 and PersistentKeepalive 25, and says 'The endpoint learns your IP from the handshake, so dynamic IPv4 routers work out of the box.'
  - ingress: tcp+udp
  - volume_stated: no monthly byte allowance is published; the fair-use section caps speed instead: '50 Mbit/s up + down, kernel-shaped'
  - bytes_transit: yes
  - transit_note: AS198889 carries the traffic; upstream is AS56655 (Gigahost), importing a default route.
- evidence:
  - [1] 2026-10-23: 'SIT, GRE and WireGuard tunnels with BGP-routed /48s. Free, dual-stack, dyndns2-ready.'
  - [1] 2026-10-23: a WireGuard profile with Endpoint = tb.tahio.eu:51820 and Address 2a05:1083:bef0::1/64
  - [1] 2026-10-23: '50 Mbit/s up + down, kernel-shaped' and '2 tunnels per account' under 'Free isn't unlimited'
  - [1] 2026-10-23: blocked ports: 'SMTP - 25 - 465 - 587 - 2525', 'POP3/IMAP - 110 - 143 - 993 - 995'
  - [2] 2026-10-23: Email, Password and Full Name are the only account fields
  - [1] 2026-10-23: 'Each tunnel gets two /64s from the primary pools plus a /64 from a tertiary.'
  - [1] 2026-11-04: the fair-use section caps each tunnel at 50 Mbit/s and lists no byte cap | capture: sha256:f963d08a3af3271768727540ccf7414193ada051dcb66a14756176ec730d28c2 | quote: 50 Mbit/s up + down, kernel-shaped
- sources:
  - [1] https://tb.tahio.eu/
  - [2] https://tb.tahio.eu/sign-up
