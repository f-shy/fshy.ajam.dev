# Infinity-Filter

> infinity-filter.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infinity-filter/ | JSON https://fshy.ajam.dev/api/v1/entity/infinity-filter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Infinity-Filter

- `egress/infinity-filter` | paid-only | evidence documented | binding none | category game L4/L7 reverse proxy (Minecraft) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.infinity-filter.com/pricing/
- price USD 0
- free tier: Free tier ships with real DDoS protection, no credit card, no time limit. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Bandwidth is listed as Unlimited on all six plans including Free; the free plan caps players at 20, domains at 1 and backends at 1; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: No credit card is required for the free tier, per the pricing page. The register form was not opened, so the fields it requires are unread. | country: None
- interface: rest
- limits:
  - write-gated: Geyser and Bedrock are a paid module: the free column shows 0 module backends and the module row carries a price on every other plan [1]
  - per-ip-shaping: the free plan is sized at 20 players online [1]
- binding note: Bandwidth is unlimited on the free plan, so no byte counter is reached at 1 TiB/month. What fails first is the plan class: the free tier cannot carry UDP at all, because the Geyser module is a paid add-on and the free column has zero module backends.
- interface detail: Panel at panel.infinity-filter.com; API access is a paid feature.
- tooling: DNS record in the panel, no client
- composes with: DNS in front of a public origin; the paid dedicated IP is the only version that could front a private origin with UDP.
- reliability: Free tier is limited to 20 players online and one backend; the vendor sells nothing else on that column.
- notes: DDoS mitigation for Minecraft Java over TCP. Free plan provides unmetered bandwidth for up to 20 concurrent players. UDP port forwarding requires dedicated IP assignments and paid plans.
- evidence note: The vendor states the exclusion in plain words and publishes the free column of the plan table. Whether the free plan has any hidden fair-use enforcement would need an account and traffic.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard offering, and no free UDP port to put one behind.
  - ingress: tcp
  - volume_stated: Bandwidth is listed as Unlimited on all six plans including Free; the free plan caps players at 20, domains at 1 and backends at 1
  - bytes_transit: yes
  - transit_note: Infinity-Filter's filtering nodes proxy the game traffic
- evidence:
  - [1] 2026-10-23: Free is EUR 0.00 with Unlimited bandwidth, Max Networks 1, Max Players 20, Max Domains 1, Max Backends 1, Max Module Backends 0; Backend Module Access (Geyser, Votifier) is priced at EUR 4.99/mo on the five paid columns only
  - [2] 2026-10-23: Geyser is not part of the Free plan; Geyser support starts at the Starter plan and totals about EUR 7.98/month with the required dedicated IP
  - [2] 2026-10-23: The reason UDP costs money: Bedrock's UDP packets carry no server address, so there is nothing to route by and each Bedrock setup needs its own IP
- sources:
  - [1] https://www.infinity-filter.com/pricing/
  - [2] https://www.infinity-filter.com/minecraft-geyser-ddos-protection/
