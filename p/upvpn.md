# UpVPN

> upvpn.app | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upvpn/ | JSON https://fshy.ajam.dev/api/v1/entity/upvpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UpVPN

- `egress/upvpn` | paid-only | evidence documented | binding none | category wireguard vpn provisioning (paid) | tier paid
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://upvpn.app/pricing
- price USD 39.99/year
- free tier: Pay as you go: $4.99/one-time ... Yearly: $39.99/year, Unlimited Data | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited Data on the yearly plan; the pay-as-you-go plan meters 4 cents per GB plus 2 cents per hour.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: prepaid credits or a yearly subscription; 'Cryptocurrency payments accepted'. | country: None
- interface: cli
- binding note: No free tier, so the first failure is the invoice, not a datum. The metered plan prices 1 TiB at roughly USD 41 in data charges alone.
- interface detail: Vendor apps and a web checkout.
- tooling: vendor apps; the aggregator says provisioning is API-driven.
- composes with: Could carry client egress only; gives nothing inbound.
- reliability: Session-based accounting: a dropped session is a new charge.
- notes: Consumer VPN service providing outbound WireGuard connections for internet access. Does not provide inbound port forwarding or reverse tunneling.
- evidence note: A free session allowance would change this; the pricing page lists only the two paid plans.
- extras:
  - wg_path: unknown
  - wg_detail: The aggregator says the apps 'use APIs to create on-demand WireGuard servers'. No .conf export, registration endpoint or peer config is described on the pricing page read.
  - ingress: tcp+udp
  - volume_stated: Unlimited Data on the yearly plan; the pay-as-you-go plan meters 4 cents per GB plus 2 cents per hour.
  - bytes_transit: overlay-only
  - transit_note: Vendor VPN servers.
- evidence:
  - [1] 2026-10-23: USD 4.99 pay-as-you-go with 5 cents base, 4 cents/GB, 2 cents/hr; USD 39.99/year unlimited
- sources:
  - [1] https://upvpn.app/pricing
