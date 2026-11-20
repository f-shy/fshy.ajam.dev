# Rocket Internet Public IPv4

> rocketinternet.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rocketinternet/ | JSON https://fshy.ajam.dev/api/v1/entity/rocketinternet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rocket Internet Public IPv4

- `egress/rocket-internet-ipv4` | trial-only | evidence documented | binding none | category dedicated IPv4 over WireGuard | tier trial
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:10:55.763Z (live) | stale on 2026-12-20
- url https://rocketinternet.com/ipv4-solutions/
- price USD 25 per month after a 30-day free trial with no card
- free tier: "START YOUR 30-DAY FREE TRIAL" then "$25/month after trial - No credit card required - No long-term contract". | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published. The only bandwidth statement answers a speed question: "Will this tunnel limit my download speed? No. Your native internet connection determines your bandwidth."; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: The trial takes no card: "No credit card required", and the paid plan bills monthly. The order form itself was not read. | country: None
- interface: cli
- limits:
  - volume-quota: unverified: no published byte allowance or rate cap; the FAQ states the tunnel does not limit download speed [1]
- binding note: The first-party FAQ states the tunnel does not limit download speed ('Your native internet connection determines your bandwidth'), so no egress rate or byte quota is published to bind a transfer; the trial window ends the offer by wall clock, which the constraint vocabulary does not name.
- interface detail: Order through the vendor's cart with a promo code for the trial.
- tooling: vendor gateway or client-side WireGuard; no config file named on the page
- composes with: 30-day trial allows evaluating architecture requirements before committing to paid address allocations.
- reliability: The gateway is described as hardware for satellite installs; the FAQ asks for the terminal in bypass mode, which is a setup constraint rather than a usage cap.
- notes: Offers a 30-day free trial on dedicated public IPv4 transit without requiring a credit card. Targets satellite and remote ISP connectivity.
- evidence note: Price, the trial terms without a card, the port range and the tunnel type are first-party. Volume is unstated and needs a support answer.
- extras:
  - wg_path: extractable
  - wg_detail: The tunnel is described but no file is named: "Rocket routes a dedicated public IPv4 address through an encrypted WireGuard tunnel directly to your network." Inbound is the product: "INBOUND TCP + UDP" and "65,535 ports! Your firewall determines what's allowed."
  - ingress: tcp+udp
  - volume_stated: No allowance is published. The only bandwidth statement answers a speed question: "Will this tunnel limit my download speed? No. Your native internet connection determines your bandwidth."
  - bytes_transit: yes
  - transit_note: A US ISP announcing its own addresses, which the vendor argues gives better reputation than a shared VPN block.
- evidence:
  - [1] 2026-10-23: 30-day free trial with no credit card, USD 25/month after; dedicated IPv4 with inbound TCP and UDP on 65,535 ports; WireGuard; works behind CGNAT
  - [1] 2026-10-23: no bandwidth allowance is stated anywhere on the page; the FAQ addresses speed only
  - [1] 2026-11-19: the vendor states the tunnel does not limit download speed, so no egress rate cap is published | capture: sha256:6ce64e40445904f89ba8c8d2177904e7849b70fb3d75dd290a8725b5cb83f642 | quote: No. Your native internet connection determines your bandwidth.
  - [1] 2026-11-19: no numeric allowance or rate is published for the tunnel | capture: sha256:6ce64e40445904f89ba8c8d2177904e7849b70fb3d75dd290a8725b5cb83f642 | quote: No. Your native internet connection determines your bandwidth.
  - [1] 2026-11-19: no egress rate or byte quota is published, supporting binding none | capture: sha256:6ce64e40445904f89ba8c8d2177904e7849b70fb3d75dd290a8725b5cb83f642 | quote: No. Your native internet connection determines your bandwidth.
  - [1] 2026-11-19: the binding is none because the vendor publishes no egress rate or byte cap | capture: sha256:6ce64e40445904f89ba8c8d2177904e7849b70fb3d75dd290a8725b5cb83f642 | quote: No. Your native internet connection determines your bandwidth.
- sources:
  - [1] https://rocketinternet.com/ipv4-solutions/
