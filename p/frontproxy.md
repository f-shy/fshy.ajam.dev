# Frontproxy

> frontproxy.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frontproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/frontproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Frontproxy (unlimited residential, speed-tiered)

- `storage/frontproxy` | trial-only | evidence reported | binding per-ip-shaping | category contributed bandwidth - unmetered, speed-capped
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://frontproxy.com/pricing/
- price $0.058/GB = $59/TB (egress)
- free tier: $10 for a 3-day 25 Mbps unlimited trial; Pro from $375/day at 400 Mbps unlimited, stated max transfer 4.3 TB/day at sustained full speed, 'effective cost $0.058 per GB'; scales to 2 Gbps | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered - 'No per-GB fees, ever'; 'No data caps' | metered: no
- identity: card | detail: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 25 Mbps [1]
  - per-ip-shaping (binding): 400 Mbps [1]
- limits note: Priced per day, which is hostile to a steady 1 TiB/day: $375/day at 400 Mbps is $11,250/month, and even the $0.058/GB effective rate is worse than Proxyrack's $5/TB equivalent at the same volume. The $10/3-day 25 Mbps entry is a trial, not a product tier (no auto-renew, 3 days only). Speed caps make this predictable but expensive.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: HTTP(S) proxy, rotating and sticky sessions, 195+ countries
- tooling: curl -x, any HTTP client
- composes with: Transfer volume is governed by port speed caps: 25 Mbps yields up to 270 GB per day, while 400 Mbps supports up to 4.3 TB per day.
- reliability: Day-rate billing with no volume discount path; guaranteed throughput is per-session, not aggregate across threads.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $10 for a 3-day 25 Mbps unlimited trial; Pro from $375/day at 400 Mbps unlimited, stated max transfer 4.3 TB/day at sustained full speed, 'effective cost $0.058 per GB'; scales to 2 Gbps
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $0.058/GB = $59/TB (egress)
- evidence:
  - [1] 2026-10-21: '3-day trial for $10 · Scale up to 2 Gbps'; 'No data caps, no per-GB fees'; trial: '$10 / 3 days ... 25 Mbps Guaranteed throughput ... Unlimited bandwidth'; Pro: '$375 / day ... 400 Mbps · Unlimited bandwidth, Max transfer 4.3 TB at sustained full speed, Effective cost $0.058 per GB transferred'
- sources:
  - [1] https://frontproxy.com/pricing/
