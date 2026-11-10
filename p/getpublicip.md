# GetPublicIP

> getpublicip.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getpublicip/ | JSON https://fshy.ajam.dev/api/v1/entity/getpublicip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetPublicIP

- `egress/getpublicip` | paid-only | evidence documented | binding volume-quota | category hosted public IP over WireGuard | tier per-ip
- identity a placeholder: card and phone unknown | verified 2026-10-30T17:51:45.684Z (live) | stale on 2026-11-30
- url https://getpublicip.com/
- price USD 8.99 per month per IP | parsed USD 8.99/mo
- free tier: No free tier and no trial on the pages read: "Only $8.99 USD / Month per IP" and "No contracts - Cancel anytime - Rapid activation". | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: "Your payment method will be charged without further action from you until you cancel" (refund policy). The sign-up form was not read, so card-versus-other is inferred from a paid monthly subscription rather than observed. | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): no published figure [2]
- binding note: Nothing is documented, so the first wall at 1 TiB/month is an unpublished the provider judgement rather than a counter that can be watched. That is worse than a number: capacity cannot be planned against a clause.
- interface detail: Configuration file plus a dashboard; the docs have a page titled "Create API Key", but the API itself was not read.
- tooling: wg-quick on Linux, the vendor's Windows client, a Docker image
- composes with: Put it on a free-tier VM and the VM gains a stable ingress address without an elastic IP; reverse DNS is included, so a mail listener is possible on port 25.
- reliability: The vendor recommends its own watchdog script because an ISP address change can hang the handshake; the address itself is static across ISP changes.
- notes: Port mapping is done in the dashboard as single ports or ranges ("Map single ports or ranges in the dashboard, with optional source-IP rules"), and the page does not state a maximum count, so treat the port count as unverified. A third-party table by competitor GetAStatic lists "Any port you open" at $8.99, which agrees on price and ports but adds nothing on volume.
- evidence note: Price, ports, protocol and the configuration file are read from first-party pages.
- extras:
  - wg_path: native-conf
  - wg_detail: "Download the Linux configuration from your IP address. Copy the pi0.conf to /etc/wireguard/" then "systemctl start wg-quick@pi0". The address is a whole IPv4 plus a public IPv6: "Every IP includes both a public IPv4 and a public IPv6 address, routed through the same tunnel."
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: The vendor carries the traffic through its own edge and, it says, does not inspect it: "We never inspect or modify your packets".
- evidence:
  - [1] 2026-10-23: USD 8.99 per IP per month; dedicated IPv4 and IPv6; no bandwidth figure on the page
  - [3] 2026-10-23: the vendor issues pi0.conf, imported with wg-quick, then ports are opened on the server's own firewall
  - [4] 2026-10-23: "All ports and protocols, with port ranges"; "All: TCP, UDP, ICMP"; 32 locations; port mapping is done in the dashboard
  - [2] 2026-10-23: 
  - [2] 2026-10-30: section 4 of the page, read on 2026-10-30, lists sustained traffic patterns that materially exceed the documented or published limits of the subscription tier; the page states no transfer figure in GB or TB | capture: sha256:221a9294e422f8ac57342294fa27d588ff3c633fb668213e77022cdb410f5295 | quote: sustained traffic patterns that materially exceed the documented or published limits of your subscription tier
  - [2] 2026-10-30: the page read on 2026-10-30 is dated 'Last updated September 29, 2026', and its full HTML carries no transfer figure in GB or TB | capture: sha256:418f7def52fd5dfa978c173e1c4f16c372e357ffa1947cfbfde664b560860984 | quote: Last updated September 29, 2026
- sources:
  - [1] https://getpublicip.com/
  - [2] https://getpublicip.com/legal/acceptable-use-policy
  - [3] https://getpublicip.com/docs/linux
  - [4] https://getpublicip.com/cgnat-public-ip
