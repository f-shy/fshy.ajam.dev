# Keep2Share

> keep2share.cc | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keep2share/ | JSON https://fshy.ajam.dev/api/v1/entity/keep2share.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Keep2Share / TezFiles (same operator)

- `storage/keep2share-tezfiles` | fails-egress | evidence reported | binding per-ip-shaping | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://keep2share.cc
- free tier: Free plan: 10 GB/day of download traffic, no storage quota published. Paid Premium Max: 100 GB/day. Both are download-traffic products, not storage products. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free = slow speed plus 10 GB/day cap; premium = 100 GB/day on Max. Egress is the thing being sold, so free egress is structurally absent. | metered: no
- identity: card
- interface: unknown
- limits:
  - per-ip-shaping (binding): 10 GB/day [1]
  - per-ip-shaping (binding): 100 GB/day [1]
- limits note: Free 10 GB/day; Premium Max 100 GB/day; no simultaneous downloads on free. TezFiles pricing shown as $35.87/$27.98 per month, 100 GB/day on Max.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: wrapper-only
- tooling: JDownloader/Mipony support; no documented API.
- composes with: None. With egress sold per day, multiplying accounts multiplies a metered cost structure.
- reliability: TezFiles serves an interstitial 'Check your browser settings. Make sure JavaScript is enabled' to plain fetchers, so only the firecrawl-pinned read gets the plan table.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Free plan: 10 GB/day of download traffic, no storage quota published. Paid Premium Max: 100 GB/day. Both are download-traffic products, not storage products.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Daily traffic 10 GB/day [Free] ... 100 GB/day [Premium Max]'
  - [1] 2026-10-21: 
  - [3] 2026-10-21: returns the JS interstitial, not content
- sources:
  - [1] https://tezfiles.com/premium
  - [2] https://keep2share.cc/premium
  - [3] https://tezfiles.com/faq
