# NovaNode IP Tunnel

> novanode.eu | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/novanode/ | JSON https://fshy.ajam.dev/api/v1/entity/novanode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NovaNode IP Tunnel

- `egress/novanode-ip-tunnel` | paid-only | evidence documented | binding volume-quota | category routed public IPv4 and IPv6 over WireGuard | tier ip-tunnel
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://novanode.eu/tunnel
- price quote only; the volume reference level is 1 TB per full euro of monthly price with a 3 TB minimum
- free tier: No free tier; the product is quote-only: "Request a quote" and "We review every tunnel order individually." | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: "Ordinary traffic is unlimited and not metered per GB. Each tunnel has a monthly reference level: 1 TB for every full euro of the monthly price excluding VAT, rounded up, at least 3 TB." Above that: "Going above the level is not a breach and costs nothing by itself" and the vendor says it will not cut a tunnel for volume alone.; ingress: tcp+udp | metered: yes | free allowance: "Ordinary traffic is unlimited and not metered per GB. Each tunnel has a monthly reference level: 1 TB for every full euro of the monthly price excluding VAT, rounded up, at least 3 TB." Above that: "Going above the level is not a breach and costs nothing by itself" and the vendor says it will not cut a tunnel for volume alone. | source: [1]
- identity: email | detail: A quote request through the support system followed by payment; activation is human: "Activation normally takes one to five business days from the later of payment and receipt of your key." The account form was not read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 TB per full euro of monthly price, minimum 3 TB [1]
  - request-rate: one active WireGuard peer per tunnel; single endpoint, no SLA [1]
- binding note: The reference level is the only counter, and it is generous by construction: at a 3 EUR monthly price the level is 3 TB, which is 2.728 TiB, so 1 TiB/month sits at a third of the allowance. The binding constraint is really the quote and the one-peer shape.
- interface detail: Quote and ticket flow, then a client-configured tunnel; no API named.
- tooling: wg-quick on MikroTik, OPNsense, pfSense, Linux or a VM
- composes with: The routed prefix plus a free-tier VM gives a whole subnet rather than one forwarded port range.
- reliability: Single endpoint, best effort, no SLA by default; a second endpoint is a paid add-on. Outbound 25 is closed until reviewed.
- notes: The only provider that states a volume policy in a formula a reader can apply, and the only one that says outright it will not cut a tunnel for volume. WireGuard only: "WireGuard only. Other protocols are not offered." No price is published, so this row establishes shape and volume policy rather than cost.
- evidence note: The routing shape, the protocol, the fair-use formula and the process are all first-party. The price itself is quote-only, so cost per TiB stays unverified.
- extras:
  - wg_path: extractable
  - wg_detail: The vendor publishes the exact wg-quick shape it expects, with keys exchanged by ticket: "You send us your WireGuard public key in a ticket. We reply with our endpoint, our public key, your addresses and the gateway addresses." The published block is a standard [Interface]/[Peer] pair with AllowedIPs 0.0.0.0/0.
  - ingress: tcp+udp
  - volume_tib_month: 2.728
  - volume_stated: "Ordinary traffic is unlimited and not metered per GB. Each tunnel has a monthly reference level: 1 TB for every full euro of the monthly price excluding VAT, rounded up, at least 3 TB." Above that: "Going above the level is not a breach and costs nothing by itself" and the vendor says it will not cut a tunnel for volume alone.
  - bytes_transit: yes
  - transit_note: NovaNode PA space registered in Luxembourg and routed statically to the tunnel.
- evidence:
  - [1] 2026-10-23: WireGuard over UDP, a /32 or larger IPv4 block routed for a user, an IPv6 prefix, all ports forwarded, monthly reference level of 1 TB per euro with a 3 TB floor, one peer per tunnel, no BGP needed
  - [1] 2026-10-23: a complete wg-quick configuration example with the client-supplied private key and the vendor's endpoint
  - [1] 2026-10-23: outbound TCP 25 closed by default and opened after review; addresses are the vendor's PA space
- sources:
  - [1] https://novanode.eu/tunnel
