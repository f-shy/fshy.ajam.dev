# MixDebrid

> mixdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/mixdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MixDebrid

- `debrid/mixdebrid` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-hoster (premium link generator, torrent conversion) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:39:03.000Z (live) | stale on 2026-11-23
- url https://mixdebrid.com/statistics
- price USD 0 on the free tier; no paid tier found on the site
- free tier: Free, no account, no payment. 'Downloading files requires passing through 3 short advertisement pages.' No byte or link allowance is published anywhere on the site. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The 'unlimited' unit records the site's own claim, not a measured absence of a cap. No limits, terms or FAQ page resolved: /terms and /faq both returned 404.
- per-object cap: none published. The public recent-downloads table showed a 63.6 GB torrent and a 19.16 GB 1fichier file completed on the read date. | source: [1]
- retention: not applicable: links only. The site says generated premium links are removed after the download finishes. | source: [1]
- egress: The service fetches the file to its own server and hands back a direct link; no byte cap is stated. 'Sec... resume supported ... no waiting time'. | metered: no | free allowance: unpublished | source: [1]
- identity: anonymous | detail: No account, no email and no card on the free path. The site says 'No account, no payment, no software install'.
- interface: rest
- limits:
  - request-rate (binding): no concurrency number published; the ad gate is three pages per download [1]
  - volume-quota: none published [1]
- limits note: The failed-unlock rate is the real ceiling: 287 of 369 attempts in the last 7 days were errors. A failed attempt costs the ad pages and the wait, which the site reports as up to 20 minutes on a slow host.
- binding note: No byte quota is published, so the constraint that actually stops 1 TiB of monthly transfer is throughput of successful unlocks: at the self-reported 21.1% seven-day success rate, a user needs roughly five attempts and five ad-gate traversals per file, and the queue waits dominate over any bandwidth figure.
- interface detail: Web form taking links, magnets or a .torrent; returns a /download/<hash> URL that any HTTP client can pull.
- tooling: Any HTTP client on the returned link; no plugin and no API documented.
- composes with: The only zero-cost service among debrid providers whose own statistics show multi-gigabyte files completing, so it is the first thing to try before paying; it cannot be relied on for 1 TiB of monthly transfer because four out of five unlock attempts fail.
- reliability: Self-reported success rate was 21.1% over the last 7 days and 8.0% for the month (78 successes against 887 errors); advertisement pages are mandatory per download; generated links are deleted after download.
- notes: Reached both as mixdebrid.com and through leech.web.id/debrid, which redirects here. The size column in the statistics table reads 1.08 TB for both the 7-day and the month row, which cannot both be right, so only the success/error counts are used. No pricing page was found: the site appears to be funded by the ad gate alone.
- evidence note: The free model and the statistics are quoted from the vendor's own pages, including its own failure counts. The statistics are self-reported, so the success rate is at the reported rung even though the page is the vendor's.
- extras:
  - aliases: leech.web.id/debrid redirects to mixdebrid.com
  - success_rate_7d: 21.1%
  - success_rate_month: 8.0%
  - largest_recent_file: 63.6 GB (torrent)
  - ad_pages: 3
- evidence:
  - [2] 2026-10-23: 'Last 7 Days 369 links generated ... Success 78 Errors 287 Success Rate 21.1% Size 1.08 TB'; 'This Month 969 ... Success 78 Errors 887 Success Rate 8.0%'; 'All Time 23,483 ... 9,205 successes 13,289 errors 39.2%'
  - [1] 2026-10-23: 'Please Note: Downloading files requires passing through 3 short advertisement pages', the recent-downloads table with 10.33 GB, 19.16 GB and 63.6 GB entries, and completion times from 1 s to 21 minutes
- sources:
  - [1] https://mixdebrid.com/
  - [2] https://mixdebrid.com/statistics
