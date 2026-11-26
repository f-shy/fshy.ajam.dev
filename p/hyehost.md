# HYEHOST IPv4 tunnels

> hyehost.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyehost/ | JSON https://fshy.ajam.dev/api/v1/entity/hyehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HYEHOST IPv4 tunnels

- `egress/hyehost-ipv4-tunnels` | paid-only | evidence documented | binding none | category routed IPv4 prefix over WireGuard | tier 32
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:23:43.032Z (live) | stale on 2026-12-26
- url https://hyehost.org/ipv4-tunnels
- price USD 2.00 per IPv4 address per month; USD 0.20 per Mbps per month above the included 100 Mbps in UK and US
- free tier: No free tier: the IPv4 component costs $2.00 per address per month in every location. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Not a byte quota but a rate, measured at the 95th percentile: "Included - 95th percentile 100 Mbps" in the UK and US, "Tunnel port 2 Gbps", and "Extra bandwidth: $0.20/Mbps". New Zealand includes 10 Mbps.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Ordering is self-serve in the panel: "Pay in the panel, configure the generated tunnel details, then assign the IPv4 addresses." The payment and verification steps were not read, so a card requirement is inferred from a paid panel order rather than observed. | country: None
- interface: cli
- limits:
  - per-ip-shaping: 100 Mbps at the 95th percentile in UK and US; 10 Mbps in New Zealand; above the allowance the tunnel is limited to the purchased allowance [1]
  - volume-quota: no byte quota; bandwidth is bought per Mbps at USD 0.20 (USD 0.60 in NZ) [1]
- binding note: Nothing fails at 1 TiB/month: the included 100 Mbps at the 95th percentile is far above the sustained rate that volume needs. The rate is the only cap: above it the tunnel is limited to the purchased allowance and more bandwidth costs USD 0.20 per Mbps per month, so no constraint binds at this volume.
- interface detail: Generated tunnel details in the panel; no API named on the pages read.
- tooling: wg-quick, or the router's own WireGuard, GRE, GRETAP, SIT or VXLAN
- composes with: A /29 on a free-tier VM gives each container a real public address, which removes the port-remap step from every service behind it.
- reliability: No DDoS protection on tunneled addresses and null-routing when attacked; the vendor says so plainly.
- notes: Cheapest per address of the providers compared: USD 1.50 per month is USD 18 per year for a /32, and the same price buys a /25. The price conflict is real and unresolved: the homepage tile says "From $1.25 / mo" and the product page says "$1.50 per IPv4 address per month" in three separate places. Every per-prefix figure on the product page is exactly 1.50 times the address count, so the homepage tile may be stale after a rise. $1.25 is not the 12-month term price, because 15 percent off 1.50 is 1.275, not 1.25. $1.25 may be a leftover campaign rate, like the page's other struck-through campaign prices, but that is unproven. The record keeps the product-page figure.
- evidence note: Prefix sizes, per-address price, tunnel protocols and 95th-percentile terms are all first-party. A probe past the included rate would show what the limit-down looks like.
- extras:
  - wg_path: extractable
  - wg_detail: The prefix is routed to the customer's endpoint: "Your selected public IPv4 space is delivered to your endpoint over WireGuard, GRE, GRETAP, SIT, or VXLAN" and "Choose WireGuard, GRE, GRETAP, SIT or VXLAN when configuring the service." It is a routed prefix, not a single NAT address: "The prefix is delivered to your tunnel endpoint for use on your router, server, firewall or customer-edge network."
  - ingress: tcp+udp
  - volume_stated: Not a byte quota but a rate, measured at the 95th percentile: "Included - 95th percentile 100 Mbps" in the UK and US, "Tunnel port 2 Gbps", and "Extra bandwidth: $0.20/Mbps". New Zealand includes 10 Mbps.
  - bytes_transit: yes
  - transit_note: Prefixes are announced from the vendor's own AS47272 network.
- evidence:
  - [1] 2026-10-23: /32 through /25 at USD 1.50 per address per month; WireGuard among five tunnel types; 100 Mbps included at the 95th percentile in UK and US; 2 Gbps tunnel port
  - [1] 2026-10-23: "We do not provide or claim DDoS protection for tunneled IP addresses"; tunneled addresses are null-routed when attacked
  - [2] 2026-10-23: the product tile says "From $1.25 / mo", which disagrees with the product page's $1.50 per address (see notes)
  - [1] 2026-11-25: the address price is now USD 2.00 per month | capture: sha256:b43d3faa58b11ab534b39b9e1bc3d989137c8c6ebae5878d787a17e2c2eef32e | quote: The IPv4 component costs $2.00 per address per month in every location.
  - [1] 2026-11-25: the address price is USD 2.00 per month | capture: sha256:b43d3faa58b11ab534b39b9e1bc3d989137c8c6ebae5878d787a17e2c2eef32e | quote: The IPv4 component costs $2.00 per address per month in every location.
  - [1] 2026-11-25: excess usage is limited to the purchased allowance, not only billed | capture: sha256:b43d3faa58b11ab534b39b9e1bc3d989137c8c6ebae5878d787a17e2c2eef32e | quote: If usage exceeds it, the tunnel is limited to your purchased allowance.
  - [1] 2026-11-25: extra bandwidth is sold per Mbps | capture: sha256:b43d3faa58b11ab534b39b9e1bc3d989137c8c6ebae5878d787a17e2c2eef32e | quote: Additional bandwidth above the included 100 Mbps costs $0.20 per Mbps per month, plus the IP charge.
  - [1] 2026-11-25: no byte quota; bandwidth is bought per Mbps | capture: sha256:b43d3faa58b11ab534b39b9e1bc3d989137c8c6ebae5878d787a17e2c2eef32e | quote: New Zealand: 10 Mbps is included at the 95th percentile. Bandwidth above this allowance costs $0.60 per Mbps per month, plus the IP charge; the shared port is 1 Gbps.
- sources:
  - [1] https://hyehost.org/ipv4-tunnels
  - [2] https://hyehost.org/
