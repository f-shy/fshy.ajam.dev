# FloodGuard

> floodguard.xyz | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/floodguard/ | JSON https://fshy.ajam.dev/api/v1/entity/floodguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FloodGuard

- `egress/floodguard` | paid-only | evidence documented | binding none | category game L4/L7 reverse proxy (Minecraft) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://floodguard.xyz/
- price USD 0
- free tier: Protect a small server, at no cost: 1 server, 30 players online, 1 backend, 5 domains, Anti-bot, bans and whitelist, Basic support | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No bandwidth caps and no overage charges on any plan; player counts follow your plan; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Sign in with Discord: 'Open the dashboard and sign in with Discord. There is no separate password.' | country: None
- interface: rest
- limits:
  - per-ip-shaping: free plan allows 30 players online on 1 server and 1 backend [1]
  - write-gated: Bedrock and voice chat appear as add-ons on the Pro card and are absent from the Free card; the docs describe a Bedrock add-on without naming which plans may buy it [1]
- binding note: Bandwidth is declared uncapped on every plan, so a 1 TiB/month figure never meets a counter. The constraint that stops a caller first is the plan class itself: the Free card lists no Bedrock add-on while the Pro card does, so on the pages read there is no UDP port to consume the allowance.
- interface detail: Dashboard at floodguard.xyz/dashboard, Discord login, no separate password.
- tooling: DNS record in the dashboard, PROXY protocol enabled on the origin
- composes with: DNS in front of a public origin; needs the origin reachable from the internet, so it does not give a private VM a public address.
- reliability: Uncapped bandwidth plus a 30-player cap; no published enforcement policy.
- notes: DDoS protection for Minecraft Java servers. Free plan includes unmetered bandwidth for up to 30 concurrent players; UDP and Bedrock proxying require paid plans.
- evidence note: Free plan fields, the uncapped-bandwidth sentence and the Discord-only signin are all on first-party pages read. An actual transfer test would be needed to see whether the uncapped claim survives 1 TiB/month.
- extras:
  - wg_path: none
  - wg_detail: No WireGuard offering, and no free UDP port.
  - ingress: tcp
  - volume_stated: No bandwidth caps and no overage charges on any plan; player counts follow your plan
  - bytes_transit: yes
  - transit_note: FloodGuard's four locations proxy the traffic
- evidence:
  - [1] 2026-10-23: Free plan: GBP 0, 1 server, 30 players online, 1 backend, 5 domains, anti-bot, bans and whitelist; Pro lists 'Bedrock and voice chat add-ons'
  - [1] 2026-10-23: Unlimited bandwidth, no caps and no overage charges on any plan; player counts follow the plan
  - [2] 2026-10-23: Sign-in is Discord only, and Bedrock appears as an add-on section that only exists once Bedrock is set up
- sources:
  - [1] https://floodguard.xyz/
  - [2] https://floodguard.xyz/docs
