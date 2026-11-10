# 1DUN dedicated scrubbing address

> 1dun.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/1dun/ | JSON https://fshy.ajam.dev/api/v1/entity/1dun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 1DUN dedicated scrubbing address

- `egress/1dun` | trial-only | evidence documented | binding none | category L4 reverse proxy (dedicated dedicated scrubbing address) | tier paid
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url http://www.1dun.com/en/product/ddos/
- price USD 149 per month | parsed USD 149/mo
- free tier: No credit card, Onboard in 5 min, Free trial | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Entry tier is USD 149/month for one dedicated dedicated scrubbing address with 200 Gbps of protection and 10 forwarding rules; no byte allowance is stated; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: Sales run through a Telegram bot rather than a self-serve form; the free trial is the only zero-cost path. | country: None
- interface: rest
- limits:
  - volume-quota: USD 149/month minimum [1]
  - request-rate: 10 forwarding rules on the entry tier [1]
- binding note: The constraint that ends this option is price, which is not a byte or rate limit: USD 149/month is the floor, so at 1 TiB/month the cost is the plan and not a quota.
- interface detail: Order through a Telegram bot; configuration in a portal.
- tooling: portal plus a chat channel for sales
- composes with: A dedicated IP in front of an origin with any port; priced far above the budget, so it is a reference point only.
- reliability: Sales and support through a Telegram bot; trial terms are not published.
- notes: Enterprise DDoS and L4 protection service. Pricing is custom and free trial duration is unpublished.
- evidence note: Prices and the trial statement are on the product page. The trial's length is not stated, and sales go through a chat channel, so nothing about it can be verified without contacting them.
- extras:
  - wg_path: inside-udp
  - wg_detail: A dedicated IP with full TCP/UDP forwarding would carry a WireGuard listener; there is no free tier.
  - ingress: tcp+udp
  - volume_stated: Entry tier is USD 149/month for one dedicated scrubbing address with 200 Gbps of protection and 10 forwarding rules; no byte allowance is stated
  - bytes_transit: yes
  - transit_note: 1DUN scrubbing PoP absorbs the flood and forwards clean traffic
- evidence:
  - [1] 2026-10-23: A dedicated dedicated scrubbing address forwards all TCP/UDP ports to an origin; 'No credit card, Onboard in 5 min, Free trial'
  - [1] 2026-10-23: Entry tier USD 149/month with 200 Gbps protection and 10 forwarding rules; every tier includes full TCP/UDP forwarding
- sources:
  - [1] http://www.1dun.com/en/product/ddos/
