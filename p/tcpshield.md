# TCPShield

> tcpshield.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tcpshield/ | JSON https://fshy.ajam.dev/api/v1/entity/tcpshield.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TCPShield (Sentry Tunnel)

- `egress/tcpshield` | qualifies-with-caveat | evidence inferred | binding volume-quota | category game L4 reverse proxy (VXLAN, any TCP/UDP) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tcpshield.com/plans
- price USD 0
- free tier: Free $0/mo, Base TCPShield plan, ideal for small 20-30 player servers: 1.0 TB monthly bandwidth, 1 network, 3 domains | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1.0 TB monthly bandwidth on Free; 5.0 TB on Pro at USD 25/mo; Unlimited bandwidth on Premium at USD 100/mo; ingress: udp | metered: yes | free allowance: 1.0 TB monthly bandwidth on Free; 5.0 TB on Pro at USD 25/mo; Unlimited bandwidth on Premium at USD 100/mo | source: [1]
- identity: email | detail: A self-serve panel account at panel.tcpshield.com. The register form was not opened, so the fields it requires are unread. No card is named for the Free plan. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1.0 TB per month on Free; at 90% the vendor emails every few hours, at 100% it overwrites the server MOTD, at 200% or five days after 100% the domains are disabled [2]
  - write-gated: creating the VXLAN interface needs root or full sudo on a Linux origin [3]
- binding note: At 1 TiB/month the 1.0 TB monthly allowance is met first, and the consequence is now documented rather than unstated: an email at 90%, a MOTD overwrite at 100%, and the domains disabled at 200% or five days after 100%, whichever comes first. Bandwidth is counted as ingress from the server and the players.
- interface detail: Self-serve panel: create a tunnel, copy the generated setup script, run it as root.
- tooling: the panel generates a shell script that creates a vxlan interface (ip link add ... type vxlan, dstport, nolearning)
- composes with: A free Linux VM becomes the origin; the tunnel gives it a public IP with UDP on any port and no domain, so it replaces the CNAME-plus-plugin step that the Minecraft path needs.
- reliability: The overage rule is now known: email at 90%, MOTD overwritten at 100%, domains disabled at 200% or five days after 100%. Bandwidth is counted from inception, so a spike is charged against the month. One backend IPv4 per tunnel.
- notes: 1.0 TB is read as 10^12 bytes, which is 0.909 TiB; the page says TB and never TiB, so if the vendor means TiB the allowance is 1.0 TiB. The strongest candidate. Two paths exist and only one carries UDP: the Minecraft CNAME path (Bedrock is Premium-only, per the FAQ) and the Sentry Tunnel path (protocol-agnostic, dedicated public IP, no domain needed). The free-plan gate on Tunnels is the open question; candidates and tests are in lane.md. A tunnel needs one backend IPv4 and root, so it pairs with a free Linux VM rather than a managed game panel. The billing doc does, in one paragraph, and the enforcement is a three-stage escalation ending in the domain being disabled at 200% of the allowance. The record called the consequence unstated. Replaces 'no overage rule is published', which the billing page contradicts.
- evidence note: The allowance, the enforcement ladder and the metering direction are all on vendor pages read on 2026-10-23, so the volume fields are documented. The record stays at inferred only because the identity field was read from the panel's name and not from the register form, which was never opened.
- extras:
  - wg_path: inside-udp
  - wg_detail: No .conf and no registration API. The tunnel forwards any TCP or UDP port to one backend IPv4, so a WireGuard listener on the origin is reachable on the tunnel's public IP; wg-quick runs on the origin, not at the edge.
  - ingress: udp
  - volume_tib_month: 0.909
  - volume_stated: 1.0 TB monthly bandwidth on Free; 5.0 TB on Pro at USD 25/mo; Unlimited bandwidth on Premium at USD 100/mo
  - bytes_transit: yes
  - transit_note: TCPShield's anycast edge carries the encapsulated traffic to the origin over VXLAN/UDP
- evidence:
  - [1] 2026-10-23: Free tier carries 1.0 TB monthly bandwidth, 1 network and 3 domains; Pro USD 25/mo carries 5.0 TB; Premium USD 100/mo carries Unlimited bandwidth
  - [4] 2026-10-23: Sentry Tunnel forwards any TCP or UDP traffic, is VXLAN over UDP, and is port-agnostic across a whole backend IP
  - [3] 2026-10-23: Root access or full sudo on a Linux server is required; the overview shows a Public IP the users connect to and an assigned VXLAN port in 32768-60999
  - [5] 2026-10-23: A UDP game port keeps its own number behind the tunnel: 19132 stays 19132 on the tunnel public IP
  - [6] 2026-10-23: The vendor says it supports ALL APPLICATIONS AND GAMES via Sentry Tunnel, and in the same paragraph gates only Bedrock on the Premium plan, naming no gate for Sentry Tunnel
  - [2] 2026-10-23: Payment methods and activation only; no overage rule for the monthly bandwidth allowance
- sources:
  - [1] https://tcpshield.com/plans
  - [2] https://docs.tcpshield.com/billing
  - [3] https://docs.tcpshield.com/vxlan/sentry-tunnel-general-setup
  - [4] https://docs.tcpshield.com/vxlan/sentry-tunnel-features
  - [5] https://docs.tcpshield.com/vxlan/sentry-tunnel-for-bedrock-geyser-pocketmine-voicechat
  - [6] https://docs.tcpshield.com/faq
