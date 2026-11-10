# Drop Download

> drop.download | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drop/ | JSON https://fshy.ajam.dev/api/v1/entity/drop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Drop Download

- `debrid/drop-download` | qualifies | evidence documented | binding volume-quota | category file host (premium one-time, XFileSharing script) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://drop.download/premium
- price USD 15 per month for 60 GB/day | parsed USD 15/mo
- free tier: Free tier: max upload 5120 Mb, download volume '20 GB in 1 days', files deleted '15 days after last download'. The 'Registered' column gives 10240 Mb, 10240 GB storage, 30 GB/day and 30 days. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Registration doubles the per-file cap and adds storage; the anonymous tier has no storage column at all.
- per-object cap: Premium 102400 Mb (100 GB); Registered 10240 Mb (10 GB); Free 5120 Mb (5 GB) | bytes: 107374182400 | source: [1]
- retention: Free 15 days after last download; Registered 30 days; Premium 60 days | days: 60 | source: [1]
- egress: Download volume per day: Free '20 GB in 1 days', Registered 30 GB, Premium 60 GB. Premium also lists 'Remote URL upload', accelerator support and resume. | metered: yes | free allowance: 20 GB/day free, 30 GB/day registered | source: [1]
- identity: card | detail: Premium at $15 for 30 days; the page shows no payment-method list beyond checkout. Signup is a form with an email.
- interface: unknown
- limits:
  - volume-quota (binding): 60 GB per day of download volume on premium [1]
  - per-object-cap: 100 GB per file premium, 10 GB registered, 5 GB free [1]
  - retention-clamped: free files deleted 15 days after the last download [1]
- limits note: The storage row reads 'Unlimited' for premium and '10240 GB' for registered; only the free column is blank.
- binding note: 60 GB/day is 1.76 TB a month, above the 1 TiB monthly volume, so at this scale nothing in the vocabulary breaks. Volume-quota is named because it is the only counter the vendor states and the first one a larger workload would meet.
- interface detail: Web upload with remote URL upload on premium. No API or FTP published on the page read.
- tooling: Browser only as read. Not on the Leechall list; it is reachable through a paid debrid or a direct subscription.
- composes with: 60 GB/day on premium is more than the 34.1 GB/day that 1 TiB a month needs, and 100 GB per file means a single Blu-ray remux fits. For bulk transfer it is the most usable shape of the cheap hosts compared.
- reliability: The 15-day free retention is the shortest in tested services, so a free-tier link shared on 2026-10-23 can be dead in two weeks.
- notes: The $90 year is $7.50 a month. The 7-day plan at $10 is the only short trial in tested services and is the cheapest way to test whether a specific host's speed holds.
- evidence note: Prices and the three-column feature table read on the vendor premium page. The free tier's actual speed is unread.
- extras:
  - plans: 7 days $10; 30 days $15; 90 days $30; 180 days $50; 365 days $90
  - annual_effective_monthly: USD 7.50
  - corpus_stats: 26.9 M files, 2 PB used
- evidence:
  - [1] 2026-10-23: the five prices (7 days $10, 30 days $15, 90 days $30, 180 days $50, 365 days $90) and the three-column table: 5/10/100 GB upload cap, 20/30/60 GB per day, 15/30/60 day retention
  - [2] 2026-10-23: 26.9 M+ files shared, 2000 Tb+ total disk used, 129 K+ active members
- sources:
  - [1] https://drop.download/premium
  - [2] https://drop.download/
