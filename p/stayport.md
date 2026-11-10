# Stayport

> stayport.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stayport/ | JSON https://fshy.ajam.dev/api/v1/entity/stayport.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stayport

- `egress/stayport` | paid-only | evidence documented | binding volume-quota | category hosted public IP over WireGuard | tier ipv4
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://stayport.io/
- price INR 599 per month billed annually for IPv4 (INR 7188 per year); INR 149 per month for the IPv6-only plan | parsed USD 1.57/mo
- free tier: No free tier; the vendor says so itself: "It's paid. If a free tool already covers your use case, use the free tool." | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "There's a fair-use allowance generous enough for game servers, web apps and personal use. Stayport isn't built for bulk transfer or proxying - if you plan to push very large volumes, talk to us first." No figure is given.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: "Tell us what you want to host and we'll onboard you within 24 hours", and "Every signup is verified, and each address is attributable to exactly one customer." Onboarding is manual, so a person reads the stated use. | country: None
- interface: cli
- limits:
  - volume-quota (binding): fair-use allowance, no figure published [1]
  - write-gated: manual onboarding within 24 hours on an annually billed plan [1]
- binding note: The fair-use clause is the only cap and it has no number, so 1 TiB/month is the exact case the vendor says to discuss first. Before that, the annual prepayment and the manual onboarding gate the account.
- interface detail: A config file plus email onboarding; no API named.
- tooling: official WireGuard client on Windows, Linux, macOS, NAS
- composes with: One address serves a game server and a web app on standard ports, so it replaces both a tunnel and a port-remap step.
- reliability: Abuse handling is graduated from warning to immediate cut-off; outbound 25 is off until requested.
- notes: Provides dedicated IPv4 addresses priced in Indian Rupees (INR) with manual onboarding, routed through a Bangalore datacenter edge.
- evidence note: Price, ports, protocol and the config file are first-party. The fair-use figure needs a support question, which is the vendor's own instruction for large volume.
- extras:
  - wg_path: native-conf
  - wg_detail: "We send you a ready-made config file. Import it into the official WireGuard app on Windows, Linux, macOS or your NAS. One click to connect." The IPv4 plan adds "Dedicated IPv6 address included free".
  - ingress: tcp+udp
  - volume_stated: "There's a fair-use allowance generous enough for game servers, web apps and personal use. Stayport isn't built for bulk transfer or proxying - if you plan to push very large volumes, talk to us first." No figure is given.
  - bytes_transit: yes
  - transit_note: Traffic enters at the vendor's Bangalore edge and is routed down the tunnel; only inbound traffic touches them ("Your browsing, streaming and downloads never touch us.").
- evidence:
  - [1] 2026-10-23: IPv4 plan INR 599/mo billed yearly (INR 7188/yr), IPv6 plan INR 149/mo (INR 1788/yr); every port open; TCP and UDP; ready-made WireGuard config; fair-use bandwidth with no figure
  - [1] 2026-10-23: outbound port 25 blocked by default and unblocked on request; reception works out of the box
- sources:
  - [1] https://stayport.io/
