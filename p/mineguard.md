# MineGuard

> mineguard.pro | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mineguard/ | JSON https://fshy.ajam.dev/api/v1/entity/mineguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MineGuard

- `egress/mineguard` | paid-only | evidence documented | binding volume-quota | category game L4 reverse proxy (Minecraft) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://mineguard.pro/en/pricing
- price USD 0
- free tier: Free: Basic L3/L4 protection, 1 network, 1 TB traffic, Portless connection (Java), BungeeCord/Velocity support | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB traffic on Free, 3 TB on Basic, 5 TB on Starter, 30 TB on Optimal, 150 TB on Professional; ingress: tcp | metered: yes | free allowance: 1 TB traffic on Free, 3 TB on Basic, 5 TB on Starter, 30 TB on Optimal, 150 TB on Professional | source: [1]
- identity: email | detail: A panel account. The signup form was not opened and no page read names the required fields; payment on paid tiers runs through FreeKassa by card or SBP. | country: None
- interface: rest
- limits:
  - volume-quota (binding): 1 TB per month [1]
  - write-gated: the free plan is 'Portless connection (Java)'; Bedrock tunnels appear only on Optimal (1 tunnel) and Professional (5 tunnels) [1]
- binding note: The free plan's 1 TB is a real monthly byte counter and the vendor states the consequence: on exceeding the traffic limit the service is suspended within a few hours, after a warning that lets the customer buy more traffic or move up a plan.
- interface detail: Panel and, from the Starter tier, REST API access.
- tooling: DNS record in the panel, no client
- composes with: Sits in front of a public origin as a DNS proxy; it does not give a private origin a public address.
- reliability: Exceeding the traffic limit suspends service within a few hours; traffic can be topped up or the plan raised.
- notes: 1 TB is read as 10^12 bytes, which is 0.909 TiB; the page says TB throughout and never TiB. A genuine 1 TB/month free tier, the same headline number as TCPShield, but the free path is Java only and the Bedrock tunnel is a paid line item. Russian-facing product; the English pages are complete and were used so quotes stay ASCII.
- evidence note: Quota, Java-only free path and the suspension-on-overage sentence are all on the vendor's own English pricing page. The account fields would need a signup to establish.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard offering and no free UDP port.
  - ingress: tcp
  - volume_tib_month: 0.909
  - volume_stated: 1 TB traffic on Free, 3 TB on Basic, 5 TB on Starter, 30 TB on Optimal, 150 TB on Professional
  - bytes_transit: yes
  - transit_note: MineGuard's filtering nodes proxy the game traffic
- evidence:
  - [1] 2026-10-23: Free plan: 1 network, 3 domains, 1 TB traffic, Basic L3/L4, 'Portless connection (Java)'; Bedrock Edition support appears only from Optimal at RUB 2511/mo
  - [2] 2026-10-23: The Russian page carries the same table plus the overage rule: on exceeding the traffic limit the service is suspended within a few hours
  - [3] 2026-10-23: Front page states 1 TB of traffic free and describes Java and Bedrock protection as the product
- sources:
  - [1] https://mineguard.pro/en/pricing
  - [2] https://mineguard.pro/pricing
  - [3] https://mineguard.pro/
