# MixDebrid

> mixdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/mixdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MixDebrid

- `debrid/mixdebrid` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-hoster (premium link generator, torrent conversion) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:00:09.301Z (live) | stale on 2026-12-26
- url https://mixdebrid.com/statistics
- price USD 0 on the free tier; no paid tier found on the site
- free tier: Free, no account, no payment. 'Downloading files requires passing through 3 short advertisement pages.' No byte or link allowance is published anywhere on the site. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The 'unlimited' unit records the site's own claim, not a measured absence of a cap. No limits, terms or FAQ page resolved: /terms and /faq both returned 404.
- per-object cap: none published. The public recent-downloads table showed a 40.46 GB 1fichier file completed. | source: [1]
- retention: not applicable: links only. The site says generated premium links are removed after the download finishes. | source: [1]
- egress: The service fetches the file to its own server and hands back a direct link; no byte cap is stated. 'Sec... resume supported ... no waiting time'. | metered: no | free allowance: unpublished | source: [1]
- identity: anonymous | detail: No account, no email and no card on the free path. The site says 'No account, no payment, no software install'.
- interface: rest
- limits:
  - request-rate (binding): no concurrency number published; the ad gate is three pages per download [1]
  - volume-quota: none published [1]
- limits note: The failed-unlock rate is the real ceiling: 338 of 338 attempts in the last 7 days were errors. A failed attempt costs the ad pages and the wait, which the site reports as up to 20 minutes on a slow host.
- binding note: No byte quota is published, so the constraint that actually stops 1 TiB of monthly transfer is throughput of successful unlocks: at the vendor-reported 0.0% seven-day success rate, no unlock has succeeded in the last seven days and ad-gate traversals dominate over any bandwidth figure.
- interface detail: Web form taking links, magnets or a .torrent; returns a /download/<hash> URL that any HTTP client can pull.
- tooling: Any HTTP client on the returned link; no plugin and no API documented.
- composes with: The only zero-cost service among debrid providers whose own statistics show multi-gigabyte files completing, so it is the first thing to try before paying; it cannot be relied on for 1 TiB of monthly transfer because three out of four unlock attempts fail.
- reliability: Self-reported success rate is 0.0% over the last 7 days (0 successes against 338 errors) and 24.8% for the month (319 successes against 943 errors); three advertisement pages are mandatory per download.
- notes: Reached both as mixdebrid.com and through leech.web.id/debrid, which redirects here. The size column in the statistics table reads 0 B for the 7-day row and 4.09 TB for the month row, so only the success/error counts are used. No pricing page was found: the site appears to be funded by the ad gate alone.
- evidence note: The free model and the statistics are quoted from the vendor's own pages, including its own failure counts. The statistics are self-reported, so the success rate is at the reported rung even though the page is the vendor's.
- extras:
  - aliases: leech.web.id/debrid redirects to mixdebrid.com
  - success_rate_7d: 0.0%
  - success_rate_month: 24.8%
  - largest_recent_file: 40.46 GB (1fichier)
  - ad_pages: 3
- evidence:
  - [2] 2026-10-23: 'Last 7 Days 369 links generated ... Success 78 Errors 287 Success Rate 21.1% Size 1.08 TB'; 'This Month 969 ... Success 78 Errors 887 Success Rate 8.0%'; 'All Time 23,483 ... 9,205 successes 13,289 errors 39.2%'
  - [1] 2026-10-23: 'Please Note: Downloading files requires passing through 3 short advertisement pages', the recent-downloads table with 10.33 GB, 19.16 GB and 63.6 GB entries, and completion times from 1 s to 21 minutes
  - [1] 2026-11-25: the three-page advertisement gate is still stated on the home page | capture: sha256:c59b94310fd456bc6d31c9faf2ebd08cbb6b9ffe4308f134281f0d3fcc0558c3 | quote: Please Note: Downloading files requires passing through 3 short advertisement pages.
  - [1] 2026-11-25: the largest completed file in the recent-downloads table on 2026-11-25 is 40.46 GB | capture: sha256:c59b94310fd456bc6d31c9faf2ebd08cbb6b9ffe4308f134281f0d3fcc0558c3 | quote: | 1fichier.com CUSA02320_UNCHARTED_THE_NATHAN_DRAK... | 40.46 GB | 1fichier.com | Completed | 1 week ago 17 Nov 19:28 • took 11s |
  - [2] 2026-11-25: the all-time statistics now show 25,222 links generated and 14,567 errors | capture: sha256:8f2a356633458a783b31b4103dffe43e217fe28d45f47fba90d8d84b37201a47 | quote: | All Time | 25,222 | 13,654 | 11,568 | 9,636 | 14,567 | 38.2% | 262.26 TB |
  - [2] 2026-11-25: the vendor-reported seven-day success rate is 0.0%: 0 successes against 338 errors | capture: sha256:df6e1b73d0308d386eae9c1898fd2c0bce0afd98338f236379c2cc46d0b749ca | quote: | Last 7 Days | 338 | 261 | 77 | 0 | 338 | 0.0% | 0 B |
  - [2] 2026-11-25: the vendor-reported monthly success rate is 24.8%: 319 successes against 943 errors | capture: sha256:df6e1b73d0308d386eae9c1898fd2c0bce0afd98338f236379c2cc46d0b749ca | quote: | This Month | 1,288 | 1,032 | 256 | 319 | 943 | 24.8% | 4.09 TB |
  - [2] 2026-11-25: the statistics page says its numbers are updated in real time | capture: sha256:df6e1b73d0308d386eae9c1898fd2c0bce0afd98338f236379c2cc46d0b749ca | quote: Statistics are updated in real-time.
  - [1] 2026-11-25: the home page states that three advertisement pages are mandatory per download | capture: sha256:c59b94310fd456bc6d31c9faf2ebd08cbb6b9ffe4308f134281f0d3fcc0558c3 | quote: Please Note: Downloading files requires passing through 3 short advertisement pages.
- sources:
  - [1] https://mixdebrid.com/
  - [2] https://mixdebrid.com/statistics
