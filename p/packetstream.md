# PacketStream

> packetstream.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/packetstream/ | JSON https://fshy.ajam.dev/api/v1/entity/packetstream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PacketStream (buy side)

- `storage/packetstream` | fails-quota | evidence reported | binding per-ip-shaping | category contributed bandwidth - metered consumer-connection proxy
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://packetstream.io/pricing
- price $1024/TB (egress)
- free tier: $1.00/GB, $50 minimum purchase, balance never expires | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: metered at the gateway: 'you are metered at the gateway for exactly what you send'. No free allowance. | metered: yes
- identity: card | detail: card
- interface: s3, rclone
- limits:
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: 1 TiB/day = 30,720 GB/month x $1.00 = $30,720/month. Fails by roughly two orders of magnitude against any real storage budget. The $1/GB is the floor of the market, not an anomaly.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: HTTP/HTTPS/SOCKS5 proxy
- tooling: curl -x, requests, any S3/rclone HTTP proxy config
- composes with: the cheapest published per-GB consumer-connection rate found ($1.00/GB), and the only vendor that publishes both sides - pays contributors $0.10/GB and sells at $1.00/GB
- reliability: Consumer-connection exits, same automated-traffic-filter and churn issues as Proxyrack; payouts to contributors carry a 3% cashout fee.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: $1.00/GB, $50 minimum purchase, balance never expires
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $1024/TB (egress)
- evidence:
  - [1] 2026-10-21: '$1 per GB. No subscription.'; 'Buy $50 of bandwidth and use it over a year'; 'nothing expires, and you are metered at the gateway for exactly what you send'
  - [2] 2026-10-21: 'PacketStream is the only app that publishes both sides of the deal: it pays $0.10/GB and sells at $1.00/GB. That's a 10x markup'; median entry price across 10 consumer-connection proxy providers is $4.50/GB
- sources:
  - [1] https://packetstream.io/pricing
  - [2] https://proxypicker.com/what-your-wifi-is-worth/
