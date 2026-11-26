# Proxyrack Unlimited Residential

> proxyrack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxyrack/ | JSON https://fshy.ajam.dev/api/v1/entity/proxyrack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxyrack Unlimited Residential (per-thread, unmetered)

- `storage/proxyrack-unlimited-residential` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category contributed bandwidth - purchased egress, flat rate
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T19:55:16.879Z (live) | stale on 2026-12-10
- url https://www.proxyrack.com/pricing/
- price n/a (egress only): $150/mo flat = $5/TB at 1 TiB/day | parsed USD 150/mo
- free tier: unmetered bytes; the limit is concurrency. 100 threads = $150/mo ($1.50/thread); 500 = $750/mo; 1,000 = $1,250/mo ($1.25); 2,000 = $2,000/mo ($1.00); 5,000 = $4,500/mo ($0.90) | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The published limit is a thread count equal to the number of threads purchased.
- retention: source: [1] | note: Proxies use random or sticky ports: they rotate on each request or remain static for a set time and then rotate.
- egress: Unmetered bandwidth & data transfer. | metered: no
- identity: card | detail: card
- interface: rclone
- limits:
  - per-ip-shaping (binding): 12.7 MB/s [1]
  - per-ip-shaping (binding): 1 TiB/day [1]
- limits note: Thread-bound, not byte-bound: 'the thread limit is equal to the number of threads you purchase'. 100 threads must aggregate 12.7 MB/s for 1 TiB/day, which requires ~1 Mbit/s sustained per thread - plausible on paper, unverified in practice and dependent on which consumer-connection IPs are live. Latency and availability are whatever the volunteer hosts happen to be. Cycling consumer-connection IPs will meet automated-traffic filters on many origins.
- binding note: part of limits note
- interface detail: All plans support HTTP, HTTPS, SOCKS5, and UDP protocols, and each comes with its own proxy pool.
- tooling: any HTTP client with proxy support - curl -x, requests, rclone --http-proxy, aria2
- composes with: Pay per thread, unmetered bandwidth.
- reliability: Exit nodes are consumer connections that go offline without notice; origins frequently block or add a human-verification step to consumer-connection proxy ranges.
- notes: the same as the free tier
- evidence note: unverified: no page read on 2026-11-11 states why this record carries the reported rung
- extras:
  - price_verbatim: n/a (egress only): $150/mo flat = $5/TB at 1 TiB/day
- evidence:
  - [2] 2026-10-21: 'Pay per thread, unmetered bandwidth'; '500 Threads $750/mo $1.50 per thread'; '1,000 Threads $1,250/mo'; 'Unlimited Residential ... Uncapped data - No GB limit'
  - [1] 2026-10-21: 'you can use as much data as you would like, so you will not need to worry about any data limits'; 'the thread limit is equal to the number of threads you purchase'
  - [3] 2026-10-21: checkout shows 100 threads $150.00 ($1.50/thread), 250 threads $280.00, 500 threads $480.00, 1000 threads $880.00
  - [2] 2026-10-21: 'All plans support HTTP, HTTPS, SOCKS5, and UDP protocols'
  - [2] 2026-11-11: the pricing page still sells the plan per thread with unmetered bandwidth | capture: sha256:5f070ae9676c3013f412dfc1c71744479777bbffe69f2e8b7bd7ce56eff81a4c | quote: Pay per thread, unmetered bandwidth
  - [1] 2026-11-11: the help article states the thread limit equals the purchased thread count | capture: sha256:c37f278977d49351aa7b035d49fbc7ad589b1ca2de05d6efa3e7fee3f10480d1 | quote: the thread limit is equal to the number of threads you purchase
  - [1] 2026-11-25: the help article states the thread limit equals purchased threads | capture: sha256:dead9f8d1f8951650731af325df98fb97d2e764b0eb194286d2a070d558907e9 | quote: Yes, the thread limit is equal to the number of threads you purchase.
  - [1] 2026-11-25: the help article describes random and sticky port rotation | capture: sha256:dead9f8d1f8951650731af325df98fb97d2e764b0eb194286d2a070d558907e9 | quote: Unlimited Residential proxies provide access to both random and sticky ports. This means that you can either have your proxies rotate on each request or remain static for a set amount of time and then rotate.
  - [2] 2026-11-25: the pricing page lists unmetered bandwidth and data transfer on every plan | capture: sha256:fca2b52ad71b39b5169c2e1f7715a810fe4f7b65a0ab4e6f5b8d8a09e189af46 | quote: - Unmetered bandwidth & data transfer
  - [2] 2026-11-25: the pricing page states the supported protocols | capture: sha256:fca2b52ad71b39b5169c2e1f7715a810fe4f7b65a0ab4e6f5b8d8a09e189af46 | quote: All plans support HTTP, HTTPS, SOCKS5, and UDP protocols, and each comes with its own proxy pool.
  - [2] 2026-11-25: the pricing page states the thread-based billing and unmetered bandwidth | capture: sha256:fca2b52ad71b39b5169c2e1f7715a810fe4f7b65a0ab4e6f5b8d8a09e189af46 | quote: Pay per thread, unmetered bandwidth
- sources:
  - [1] https://help.proxyrack.com/en/articles/10961190-what-are-unlimited-residential-proxies
  - [2] https://www.proxyrack.com/pricing/
  - [3] https://app.proxyrack.com/dashboard/signup/proxy/usa?package=500
