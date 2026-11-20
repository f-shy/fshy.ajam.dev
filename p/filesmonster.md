# FilesMonster

> filesmonster.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filesmonster/ | JSON https://fshy.ajam.dev/api/v1/entity/filesmonster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FilesMonster

- `debrid/filesmonster` | paid-only | evidence documented | binding volume-quota | category premium file host (one-click hoster), retrieval target and seller of time-boxed traffic | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:37:39.581Z (live) | stale on 2026-11-23
- url https://filesmonster.com/
- price USD 3.78 per TB per 30 days at the annual rate (USD 116 / 2.555 TB / 12 months) | parsed USD 3.78/TB-mo
- free tier: No free tier is published. The only offer reachable from the site is a Premium Membership, sold as 15 to 365 day passes, each carrying a fixed traffic bucket. Whether an anonymous unpaid download exists was not established: /free returns 404 and /info/ returns 404. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: A pay-per-download host with no advertised free path. The membership is the product and the traffic is the meter.
- per-object cap: Not stated per file. The premium page advertises 'One file, not multi-volume archives' as a benefit, which is the site saying the free path splits files into parts and the paid path does not. | source: [1]
- retention: Not stated on the pages read. | source: [2]
- egress: Premium traffic is the allowance: 'Premium account can be used to download any type of content ... within available amount of traffic (Premium traffic)'. Download speed is not limited and multi-threaded downloads and download managers are supported. | metered: yes | free allowance: none published | price per TB: USD 45.40 per TB at 365 days; USD 80.95 per TB at 30 days (computed from the quoted bucket and price) | source: [3]
- identity: card | detail: Buying premium needs an email address and a card: 'You will receive your login and password to this email ... You will be billed', with credit card and 'All Available Methods' listed, plus authorised resellers for local payment. No identity document is asked for on the page.
- interface: rest, unknown
- limits:
  - volume-quota (binding): 15 days = 105 GB, 30 days = 210 GB, 90 days = 630 GB, 180 days = 1260 GB, 365 days = 2555 GB of premium traffic [3]
  - per-ip-shaping: 250 downloads per 24 hours and 50 simultaneous downloads from a single IP address [3]
- limits note: The bucket is the design: 2555 GB for 365 days is 7 GB a day, and it does not roll over. A client pulling 1 TiB a month would exhaust a year's pass in about four months of use and then be buying a second one.
- binding note: At 1 TiB a month the traffic bucket is spent first: 1 TiB is 1024 GB, so the 30-day pass (210 GB) covers five days and the annual pass (2555 GB) covers about two and a half months. The per-IP download count is generous enough that it does not bind before the bucket does.
- interface detail: Download managers and multi-threaded clients are explicitly supported, which is the practical programme path: the host serves plain HTTP links to an authorised client. 'Download managers supported' and 'Multi-thread downloads are supported' appear in the premium rules.
- tooling: JDownloader class clients. No first-party API is advertised; the file host model is link-in, file-out.
- composes with: A file host that a debrid broker or a link site points at, not a service that chains outward. Here it is a price reference for the bucket model: 15 days buys 105 GB, which is the same shape as EX-LOAD's daily traffic but sold as a block.
- reliability: A shared pass is the fastest way to lose one.
- notes: The useful fact is the bucket arithmetic: this host prices traffic in blocks with an expiry, which is the cheapest per-TB shape among debrid providers and still an order of magnitude above a debrid subscription.
- evidence note: The traffic buckets, the per-IP limits and the prices were read on the vendor's own premium rules and pricing pages today. What is missing is whether a free anonymous download exists at all; /free 404'd and no download was attempted.
- extras:
  - bucket_math: 2555 GB per 365 days is 7.0 GB/day; 210 GB per 30 days is also 7.0 GB/day, so every tier is the same daily rate and only the commitment changes
- evidence:
  - [3] 2026-10-23: the traffic buckets ('15 days Premium Membership contains up to 105GB', '365 days ... up to 2555GB'), 'Download speed is not limited', '250 downloads per each 24 hours' and '50 simultaneous downloads' per IP
  - [1] 2026-10-23: the prices: 365 days USD 116 (0.32/day), 180 days USD 66, 90 days USD 37, 30 days USD 17, 15 days USD 12, credit card plus resellers
  - [2] 2026-10-23: the site is live and describes itself as 'Digital content distribution' with a content/link/file model
  - [4] 2026-10-23: there is no /free page (404 'Page not found'), so the free path is not documented on the site at the obvious address
- sources:
  - [1] https://filesmonster.com/premium
  - [2] https://filesmonster.com/
  - [3] https://filesmonster.com/info/premiumrules/
  - [4] https://filesmonster.com/free
