# Proxyrack Unlimited Residential

> proxyrack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxyrack/ | JSON https://fshy.ajam.dev/api/v1/entity/proxyrack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxyrack Unlimited Residential (per-thread, unmetered)

- `storage/proxyrack-unlimited-residential` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category contributed bandwidth - purchased egress, flat rate
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.proxyrack.com/pricing/
- price n/a (egress only): $150/mo flat = $5/TB at 1 TiB/day | parsed USD 150/mo
- free tier: unmetered bytes; the limit is concurrency. 100 threads = $150/mo ($1.50/thread); 500 = $750/mo; 1,000 = $1,250/mo ($1.25); 2,000 = $2,000/mo ($1.00); 5,000 = $4,500/mo ($0.90) | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unmetered - 'With this service you can use as much data as you would like, so you will not need to worry about any data limits' and 'Uncapped data - No GB limit' | metered: no
- identity: card | detail: card
- interface: rclone
- limits:
  - per-ip-shaping (binding): 12.7 MB/s [1]
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: Thread-bound, not byte-bound: 'the thread limit is equal to the number of threads you purchase'. 100 threads must aggregate 12.7 MB/s for 1 TiB/day, which requires ~1 Mbit/s sustained per thread - plausible on paper, unverified in practice and dependent on which consumer-connection IPs are live. Latency and availability are whatever the volunteer hosts happen to be. Cycling consumer-connection IPs will meet automated-traffic filters on many origins.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: HTTP/HTTPS/SOCKS5/UDP forward proxy; rotating or sticky ports (10/20/30 min); country/city/ISP targeting
- tooling: any HTTP client with proxy support - curl -x, requests, rclone --http-proxy, aria2
- composes with: this is the only flat-rate egress product found in the entire research: $150/month buys an unmetered HTTP egress path, so 1 TiB/day costs $5/TB of egress regardless of volume. It is a forward proxy, not a CDN - nothing is cached and every byte is re-fetched from origin through a stranger's home connection.
- reliability: Exit nodes are consumer connections that go offline without notice; origins frequently block or add a human-verification step to consumer-connection proxy ranges.
- notes: the same as the free tier
- extras:
  - price_verbatim: n/a (egress only): $150/mo flat = $5/TB at 1 TiB/day
- evidence:
  - [2] 2026-10-21: 'Pay per thread, unmetered bandwidth'; '500 Threads $750/mo $1.50 per thread'; '1,000 Threads $1,250/mo'; 'Unlimited Residential ... Uncapped data - No GB limit'
  - [1] 2026-10-21: 'you can use as much data as you would like, so you will not need to worry about any data limits'; 'the thread limit is equal to the number of threads you purchase'
  - [3] 2026-10-21: checkout shows 100 threads $150.00 ($1.50/thread), 250 threads $280.00, 500 threads $480.00, 1000 threads $880.00
  - [2] 2026-10-21: 'All plans support HTTP, HTTPS, SOCKS5, and UDP protocols'
- sources:
  - [1] https://help.proxyrack.com/en/articles/10961190-what-are-unlimited-residential-proxies
  - [2] https://www.proxyrack.com/pricing/
  - [3] https://app.proxyrack.com/dashboard/signup/proxy/usa?package=500
