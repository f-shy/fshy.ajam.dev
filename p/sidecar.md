# Sidecar Network

> sidecar.network | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sidecar/ | JSON https://fshy.ajam.dev/api/v1/entity/sidecar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sidecar Network

- `egress/sidecar-network` | fails-quota | evidence documented | binding per-ip-shaping | category public IPv4 and IPv6 per container over WireGuard | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://sidecar.network/pricing
- price USD 0 for the free tier (3 peers, IPv6 only, 2 Mbps); paid from USD 0.99 per month, IPv4 tiers priced only by their USD 29 setup and USD 3 provisioning fees on the page read | parsed USD 0.99/mo
- free tier: "Free $0 / forever 3 peers - 4 IPv6 - 2 Mbps", and "Personal tiers: unlimited data transfer - IPv6 reachable - cancel anytime". | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "Every tier ships with unlimited data transfer. You pay for a public IP and speed - not for gigabytes." and "We never charge you for data - ever. Our tiers are speed-limited, not data-capped." The free tier's speed is the cap: 2 Mbps.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: Free peers are provisioned through an RFC 8628 device code with no email: "without a browser, email, or human-in-the-loop steps". Payment, where required, is PayPal or Bitcoin via Lightning. | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): 2 Mbps per peer on the free tier [1]
- binding note: The free tier's 2 Mbps is below the 3.24 Mbit/s that 1 TiB/month needs, so a single peer tops out near 0.65 TB in 30 days (2e6 bits per second times 2,592,000 seconds over 8). Paid tiers are speed-tiered up to 100 Mbps on Launch and unlimited on bytes.
- interface detail: REST API with an OpenAPI spec, plus an installer and a Docker network plugin.
- tooling: one-line agent install for Docker; REST API; systemd or Docker Desktop
- composes with: An agent running on a virtual machine obtains a public IP address without configuration files, with scriptable API provisioning.
- reliability: Outbound port 25 is blocked at the relay on all tiers; free peers share a relay with other customers, and isolation starts at Pulse.
- notes: The surprising row: genuinely unlimited bytes at USD 0, with no email, and the free tier still cannot carry 1 TiB/month because of the 2 Mbps ceiling. The 2 Mbps is a per-peer rate, not a per-account cap: the pricing page attaches the rate to each peer ("each peer gets its own rate limit at the plan's throughput tier"), so a single service on one address gets 2 Mbps. Unlimited data is real and only speed is sold: two independent sentences on the same page say so, and a published customer claim reports 14 TB in a month. The free tier is IPv6-only: the FAQ names Free among the IPv6-only plans. Monthly prices for the IPv4 tiers (Pulse and up) are not in the page HTML, so the paid IPv4 path is priced only by its setup fees here.
- evidence note: The free plan card, the unlimited-data claim, the IPv6-only rule and the API path are first-party. A measured throughput test at 2 Mbps would confirm the ceiling; the monthly figure here is arithmetic from the stated rate, not a measurement.
- extras:
  - wg_path: registration-api
  - wg_detail: There is no file to import: the agent injects the tunnel into the container's network namespace. "WireGuard kernel netns injection - the container IS the IP. No NAT, no proxy; every protocol including raw UDP and ICMP." Peers are created through the REST API: "POST https://sidecar.network/v1/device/authorize ... tier: free". The device-flow page states the onboarding: "AI agents can install Sidecar without a browser, email, or human-in-the-loop steps using RFC 8628 device-code flow."
  - ingress: tcp+udp
  - volume_stated: "Every tier ships with unlimited data transfer. You pay for a public IP and speed - not for gigabytes." and "We never charge you for data - ever. Our tiers are speed-limited, not data-capped." The free tier's speed is the cap: 2 Mbps.
  - bytes_transit: yes
  - transit_note: Six regions on the vendor's relays; the container holds the address itself rather than sitting behind NAT.
- evidence:
  - [1] 2026-10-23: Free 3 peers / 4 IPv6 / 2 Mbps / USD 0 forever; Micro USD 0.99 at 100 kbps; Spark USD 4.99 at 25 Mbps; Launch USD 9.99 at 100 Mbps; unlimited data on every tier
  - [1] 2026-10-23: "IPv4 depends on plan: Pulse+IPv4, Relay, Surge, Fleet, and Command include dedicated IPv4(s); Micro / Free / Spark / Launch / Pulse are IPv6-only."
  - [1] 2026-10-23: IPv4 tiers carry a USD 29 setup fee plus USD 3 provisioning fee
  - [2] 2026-10-23: device-code onboarding without email or a browser; REST API for peers; verify call returns externally_reachable and the assigned addresses
- sources:
  - [1] https://sidecar.network/pricing
  - [2] https://sidecar.network/llms.txt
