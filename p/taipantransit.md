# Taipan Transit

> taipantransit.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/taipantransit/ | JSON https://fshy.ajam.dev/api/v1/entity/taipantransit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Taipan Transit

- `egress/taipan-transit` | paid-only | evidence documented | binding volume-quota | category routed public IP over WireGuard | tier wireguard
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:43:48.837Z (live) | stale on 2026-12-26
- url https://taipantransit.com/pricing
- price EUR 2 per month for a WireGuard tunnel, EUR 0.70 per additional IPv4, EUR 0.35 per TB above the first TB | parsed USD 2.25/mo
- free tier: No free tier. Regular Performance WireGuard: EUR 2 per tunnel, EUR 0.70 per IPv4, first 1 TB of transit included. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "Included transit 1 TB free", then "Additional transit 0.35 [EUR]/TB" at the campaign rate (list 0.50). Capacity is "up to 1 Gbit/s".; ingress: tcp+udp | metered: yes | free allowance: "Included transit 1 TB free", then "Additional transit 0.35 [EUR]/TB" at the campaign rate (list 0.50). Capacity is "up to 1 Gbit/s". | source: [1]
- identity: card | detail: Registration is an email plus a 6-digit mail code, but the service is gated on payment and on a verified account: "Once your account is verified, getting your tunnel online is sssssimple." The privacy page names what is collected: "Identite et contact : prenom, nom, email, telephone", and Stripe is the payment processor. | country: None
- interface: cli
- limits:
  - volume-quota (binding): Regular Performance: 1 TB included, then EUR 0.35 per TB; Cost-Optimized: EUR 0.35 per TB billed from the first TB [1]
  - write-gated: account verification before the tunnel comes online [2]
- binding note: Regular Performance includes 1 TB of transit; additional transit is EUR 0.35 per TB (EUR 0.50 per TB on IPsec), billed on consumption.
- interface detail: Order and manage in the panel; no API named on the pages read.
- tooling: wg-quick; the vendor's operator panel
- composes with: A tunnel plus one routed IPv4 on a free-tier VM is the whole stack; the same tunnel can carry a /29 if more addresses are bought at 0.70 each.
- reliability: Mitigated attack traffic is not counted against the allowance, which matters if the address is ever a target.
- notes: Cheapest per TiB with a real included terabyte: EUR 0.35 per extra TB is about USD 0.40 per TiB at the campaign rate, and mitigated DDoS traffic is excluded from the count. The price is a campaign price with a struck-through list price, so it can end. Registration collects a phone number even though the form marks optional fields as optional.
- evidence note: Price, allowance, overage rate, IP price and tunnel types are all first-party. What a verified account requires beyond email and card is unread.
- extras:
  - wg_path: extractable
  - wg_detail: The tunnel is ordered in the panel and configured at the customer end: "Each endpoint has a public and private key", and the product page describes routed delivery: "It keeps configuration readable, establishes sessions quickly, and carries routed IPv4 or IPv6 traffic". IPv4 is a separate line item at "0.70 [EUR]/IP".
  - ingress: tcp+udp
  - volume_tib_month: 0.909
  - volume_stated: "Included transit 1 TB free", then "Additional transit 0.35 [EUR]/TB" at the campaign rate (list 0.50). Capacity is "up to 1 Gbit/s".
  - bytes_transit: yes
  - transit_note: The vendor routes the prefix to the tunnel from its own network and reports 1 to 7 ms routes.
- evidence:
  - [1] 2026-10-23: WireGuard tunnel 2 EUR/month (list 5), 1 TB transit included, additional transit 0.35 EUR/TB, additional IPv4 0.70 EUR/IP, term discounts up to 15 percent
  - [2] 2026-10-23: the tunnel carries routed IPv4 or IPv6 and survives a changing client address without dynamic DNS
  - [3] 2026-10-23: "IPv4 addresses from 0.70 [EUR]/IP"; DDoS mitigation included up to 7 Tb/s and mitigated traffic is not counted
  - [4] 2026-10-23: name, email and phone are collected at signup; Stripe is the payment processor
  - [1] 2026-11-25: the pricing page now lists Regular Performance at EUR 2 per tunnel and EUR 0.70 per IPv4 with the first TB included, and no campaign or list price | capture: sha256:f17b6d48742bada45227b18aeac1440bfe8854b3ed99c0a0494247629a9a8b29 | quote: Regular Performance coûte 0,70 € par IPv4 et 2 € par tunnel, avec le premier To inclus; le trafic supplémentaire coûte 0,35 €/To en GRE et WireGuard, ou 0,50 €/To en IPsec.
  - [1] 2026-11-25: Cost-Optimized bills transit from the first TB; Regular Performance includes 1 TB | capture: sha256:f17b6d48742bada45227b18aeac1440bfe8854b3ed99c0a0494247629a9a8b29 | quote: | Volume ou capacité | Facturé dès le premier To | 1 TB offert | Débit engagé |
  - [1] 2026-11-25: additional transit is EUR 0.35 per TB on WireGuard and EUR 0.50 per TB on IPsec | capture: sha256:f17b6d48742bada45227b18aeac1440bfe8854b3ed99c0a0494247629a9a8b29 | quote: Regular Performance coûte 0,70 € par IPv4 et 2 € par tunnel, avec le premier To inclus; le trafic supplémentaire coûte 0,35 €/To en GRE et WireGuard, ou 0,50 €/To en IPsec.
  - [1] 2026-11-25: paid transit with 1 TB included then EUR 0.35 per TB, so volume-quota still binds and the verdict stays paid-only | capture: sha256:f17b6d48742bada45227b18aeac1440bfe8854b3ed99c0a0494247629a9a8b29 | quote: Regular Performance coûte 0,70 € par IPv4 et 2 € par tunnel, avec le premier To inclus; le trafic supplémentaire coûte 0,35 €/To en GRE et WireGuard, ou 0,50 €/To en IPsec.
- sources:
  - [1] https://taipantransit.com/pricing
  - [2] https://taipantransit.com/wireguard-tunnels
  - [3] https://taipantransit.com/
  - [4] https://taipantransit.com/privacy
