# TurtleGuard

> turtleguard.cloud | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turtleguard/ | JSON https://fshy.ajam.dev/api/v1/entity/turtleguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TurtleGuard

- `egress/turtleguard` | paid-only | evidence documented | binding none | category game L4 reverse proxy (Minecraft and generic TCP/UDP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://turtleguard.cloud/en/tcp-udp
- price USD 0 for one Java server; USD 5-7 per month for Bedrock or other UDP | parsed USD 5/mo
- free tier: The first Minecraft Java server on the default worldwide region is free: up to 20 players at once. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance is stated for the free server or for the paid lines; prices are per month by protocol, from USD 5 for Minecraft Bedrock and from USD 7 for other UDP; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: An account with a balance; support runs through Telegram. The signup form was not opened. | country: None
- interface: rest
- limits:
  - write-gated: free covers 'One Minecraft Java server in the default worldwide region on the Start plan'; Bedrock and other UDP are separate paid lines [1]
  - per-ip-shaping: free server is capped at 20 players at once [1]
- binding note: The free entitlement is one Java server with no stated byte counter, and UDP is a paid line item, so nothing free reaches a 1 TiB/month quota. The paid 'Other UDP' line is explicitly 'Not for VPNs or proxies', which is the relevant limit for a WireGuard use.
- interface detail: Wizard that shows the total before you connect, billed from an account balance.
- tooling: DNS record, per-protocol setup
- composes with: Fronts a public origin per protocol; the free server is a Minecraft Java endpoint only.
- reliability: Free server is one Java server at 20 players; generic UDP is sold with an explicit exclusion of VPN and proxy traffic.
- notes: DDoS protection proxy for Minecraft servers. Free tier provides TCP protection for up to 20 players; UDP port forwarding requires paid tiers.
- evidence note: Free entitlement, price list and the per-protocol caveat are on one first-party page. Whether the free server has an unpublished fair-use cap would need an account.
- extras:
  - wg_path: none
  - wg_detail: Generic UDP is sold from USD 7/month as its own line item; the free entitlement is one Minecraft Java server.
  - ingress: tcp
  - volume_stated: No byte allowance is stated for the free server or for the paid lines; prices are per month by protocol, from USD 5 for Minecraft Bedrock and from USD 7 for other UDP
  - bytes_transit: yes
  - transit_note: TurtleGuard nodes terminate the connection and forward to the origin
- evidence:
  - [1] 2026-10-23: Free: one Minecraft Java server in the default worldwide region on the Start plan, up to 20 players at once, no charges
  - [1] 2026-10-23: Any TCP or UDP and Bedrock are sold from USD 5-7 per month; 'Other UDP' is 'Packet and flow limits per address. Not for VPNs or proxies.'
- sources:
  - [1] https://turtleguard.cloud/en/tcp-udp
