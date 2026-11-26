# earnapp

> proxypicker.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxypicker/ | JSON https://fshy.ajam.dev/api/v1/entity/proxypicker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxyware earn-app tier as a purchasable egress path (Honeygain, EarnApp, Pawns.app, Traffmonetizer, Repocket, Grass)

- `storage/proxyware-earn-app-tier-as-a-purchasable-egress-path` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category contributed bandwidth - the supply side of the market
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://proxypicker.com/what-your-wifi-is-worth/
- free tier: these pay you; they do not sell to you. Honeygain 10 GB = $1 ($0.10/GB); PacketStream $0.10/GB; EarnApp moved to hourly pay on 20 Aug 2025, ceiling $10/IP/month in the US and $5 elsewhere; Pawns.app, Repocket and Traffmonetizer publish no rate; Grass pays in points with no dollar rate | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A - no HTTP egress endpoint is sold to consumers by any of them | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Residential bandwidth sharing applications do not expose HTTP proxy egress endpoints directly. Software clients sell device bandwidth wholesale to residential proxy aggregators (such as Bright Data, IPRoyal, and PacketStream). Contributors receive fixed cash payouts per gigabyte rather than reciprocal routing credits.
- interface detail: none exposed to a buyer at consumer tier
- tooling: part of interface detail
- composes with: none - but this tier is the source of the bytes that PacketStream/Proxyrack resell, which is why their retail floor is $1/GB
- reliability: Per-IP caps and per-IP demand make earnings non-scalable; Honeygain's own example needs three separate networks to reach $5-6.67/month; Emerging Threats now ships 'ADWARE_PUP: Bandwidth Sharing Tool' rules for 5 of these 8 domains, so IDS-equipped networks flag them.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: these pay you; they do not sell to you. Honeygain 10 GB = $1 ($0.10/GB); PacketStream $0.10/GB; EarnApp moved to hourly pay on 20 Aug 2025, ceiling $10/IP/month in the US and $5 elsewhere; Pawns.app, Repocket and Traffmonetizer publish no rate; Grass pays in points with no dollar rate
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Only 2 of the 8 apps publish what they pay per gigabyte, and both pay $0.10'; 'A gigabyte that earns you $0.10 sells for a median $4.50, a 45x markup'; 'EarnApp ... pays at most $10 a month per US IP address ... Outside the US the ceiling is $5'; 'Pawns.app, Repocket and Traffmonetizer don't publish a rate, and Grass pays in points'
  - [2] 2026-10-21: 'Network-contribution programs like Grass reward uptime consistency instead: no per-GB meter, no per-minute tally'; per-unit apps 'typically between 20 cents and $1 per gigabyte'
  - [3] 2026-10-21: '$2 starting gift'; rates not restated on the homepage
  - [1] 2026-10-21: Emerging Threats rules table: PacketStream, EarnApp, Pawns.app, Traffmonetizer, Repocket, Grass each get 2 rules in category ADWARE_PUP added 11 Feb 2026
- sources:
  - [1] https://proxypicker.com/what-your-wifi-is-worth/
  - [2] https://www.grass.io/learn/how-can-you-get-rewarded-for-the-internet-you-don-t-use/
  - [3] https://honeygain.com/

## earnapp (bright data)

- `storage/earnapp` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://proxypicker.com/what-your-wifi-is-worth/
- free tier: none reachable: Dropped per-GB pay on 20 Aug 2025 and now pays per hour of active use, capped at $10/month per US IP and $5 elsewhere - a hard ceiling that makes it useless as a scale path in either… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Dropped per-GB pay on 20 Aug 2025 and now pays per hour of active use, capped at $10/month per US IP and $5 elsewhere - a hard ceiling that makes it useless as a scale path in either…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Dropped per-GB pay on 20 Aug 2025 and now pays per hour of active use, capped at $10/month per US IP and $5 elsewhere - a hard ceiling that makes it useless as a scale path in either…
- sources:
  - [1] https://proxypicker.com/what-your-wifi-is-worth/

## peer2profit

- `storage/peer2profit` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://proxypicker.com/what-your-wifi-is-worth/
- free tier: none reachable: Official site unreachable (connection closed, twice, on 2 Oct 2026). Third-party research places it at $0.28/GB residential feeding AstroProxy at $7.60/GB, but nothing about it can be… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Official site unreachable (connection closed, twice, on 2 Oct 2026). Third-party research places it at $0.28/GB residential feeding AstroProxy at $7.60/GB, but nothing about it can be…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Official site unreachable (connection closed, twice, on 2 Oct 2026). Third-party research places it at $0.28/GB residential feeding AstroProxy at $7.60/GB, but nothing about it can be…
- sources:
  - [1] https://proxypicker.com/what-your-wifi-is-worth/
