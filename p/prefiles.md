# PreFiles

> prefiles.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prefiles/ | JSON https://fshy.ajam.dev/api/v1/entity/prefiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PreFiles

- `debrid/prefiles` | qualifies | evidence documented | binding volume-quota | category file host (three paid tiers, one-time billing) | tier Pro
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://prefiles.com/pricing/
- price USD 17.99 per month for 1 TB stored and 50 GB/day | parsed USD 17.99/TB-mo
- free tier: Free: 50 GB storage, 512 Mb max upload, 10 upload slots, files deleted 30 days after the last download, download volume '5 GB in 1 days', 256 KB/s, 'Download restriction 1 file / 30 min'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Free 512 Mb; Pro 10240 Mb (10 GB); Max 10240 Mb (10 GB) | bytes: 10737418240 | source: [1] | note: The 10 GB cap is stated in Mb as '10240 Mb' on the vendor's own compare table.
- retention: Free: 30 days. Pro and Max: 'Never'. | days: 30 | source: [1] | note: The FAQ qualifies it: 'Files on a paid account are kept for as long as the account stays active'.
- egress: Free 5 GB/day at 256 KB/s with one file per 30 minutes; Pro 50 GB/day at 10 MB/s with no download restriction; Max 'Download volume: Unlimited' at 'Unlimited' speed. Traffic can also be bought separately at 10 GB / $4.99, 30 GB / $9.99, 100 GB / $19.99 with a balance that 'never expires' and 'works without a premium plan'. | metered: yes | free allowance: 5 GB/day | price per TB: USD 199.90 per TB bought as 10x100 GB top-ups, or USD 24.99 per month unlimited on Max | source: [1]
- identity: card | detail: Checkout through Paddle as merchant of record, which also carries the refund terms. The pricing page's checkout step asks only 'Enter your email'.
- interface: unknown
- limits:
  - volume-quota (binding): 5 GB/day free, 50 GB/day Pro, unlimited Max [1]
  - per-ip-shaping: free tier 256 KB/s and '1 file / 30 min' [1]
  - per-object-cap: 512 Mb free, 10240 Mb paid [1]
- limits note: The 10 MB/s figure on Pro is a speed cap, not a byte cap, and it is the number that decides whether a 50 GB day is reachable in a day: 50 GB at 10 MB/s takes 1.4 hours.
- binding note: Pro's 50 GB/day is 1.46 TB a month, above the 1 TiB monthly volume, so Pro clears this scale. Free's 5 GB/day is 150 GB a month, which fails by a factor of seven.
- interface detail: Web upload with remote URL upload and FTP upload on both paid tiers. No API is published on the pricing page.
- tooling: FTP upload on paid tiers is the only non-browser write path stated. The host is on the Leechall generator list for pull.
- composes with: The traffic top-up is what makes this host composable: 100 GB for $19.99 that never expires is a way to buy a single large pull without a subscription, and the balance survives after a plan ends.
- reliability: A premium expiry drops the account to free limits without deleting files, so an archive survives a lapsed month but its download speed does not.
- notes: Max at $24.99 for 10 TB and unlimited volume is the cheapest unlimited-volume offer found in tested services, but the 10 GB per-file cap is unchanged from Pro, so a 40 GB remux still has to be split. The 365-day Max at $149.99 is $12.33 a month.
- evidence note: Full three-tier comparison and every price read from the vendor's own table. A download at Pro speed would raise egress to measured.
- extras:
  - plans: Pro 30d $17.99 / 90d $35.99 / 365d $109.99; Max 30d $24.99 / 90d $49.99 / 365d $149.99
  - traffic_addons: 10 GB $4.99; 30 GB $9.99; 100 GB $19.99
  - max_annual_effective_monthly: USD 12.33
  - merchant_of_record: Paddle
- evidence:
  - [1] 2026-10-23: Pro $17.99/30d, $35.99/90d, $109.99/365d with 1024 GB and 50 GB/day; Max $24.99/30d, $49.99/90d, $149.99/365d with 10240 GB and unlimited volume; traffic 10 GB $4.99 / 30 GB $9.99 / 100 GB $19.99; free row 50 GB, 512 Mb, 5 GB/day, 256 KB/s, 1 file / 30 min
- sources:
  - [1] https://prefiles.com/pricing/
