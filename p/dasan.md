# DASAN

> dasan.co | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dasan/ | JSON https://fshy.ajam.dev/api/v1/entity/dasan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DASAN

- `debrid/dasan` | fails-quota | evidence documented | binding per-object-cap | category debrid / cloud download service (premium links, torrent, usenet) | tier free trial
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://dasan.co/
- price from USD 2.99 entry, metered per GB; per-GB rate not published
- free tier: 'Try a Magnet, Torrent or NZB free. One free job per 24 hours, up to 500 MB. No account required.' Paid service 'Start from $2.99 and pay only for the GBs you use. No monthly subscription.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The free job is scoped to magnet, torrent or NZB. A file-host link is the paid product; the page does not offer a free file-host unlock.
- per-object cap: 500 MB per free job ('up to 500 MB'). | bytes: 524288000 | source: [1] | note: Paid per-GB jobs have no stated per-file cap on the landing page.
- retention: unverified: files are kept in the account's cloud and can be streamed or re-downloaded; no retention period is stated on the landing page. | source: [1]
- egress: Pay per GB of traffic on paid plans; the free job includes its 500 MB. No per-TB price is listed on the landing page, only the $2.99 entry point. | metered: yes | free allowance: 500 MB per 24 hours | price per TB: start from USD 2.99, pay per GB (rate not stated on the landing page) | source: [1]
- identity: anonymous | detail: 'No account required' for the one free job per 24 hours; an account is required to buy or hold a balance.
- interface: unknown, rest
- limits:
  - request-rate: 1 free job per 24 hours [1]
  - per-object-cap (binding): 500 MB per free job [1]
  - per-object-cap (binding): 500 MB per job on the free path [1]
  - request-rate: 1 job per 24 hours on the free path [1]
- limits note: The free path is a trial for torrents and usenet, not for host links. The paid path is metered per GB with a $2.99 minimum, which is the debrid model debrid other rows price.
- binding note: At 1 TiB/month the 500 MB per-job ceiling is the harder wall than the 1 job/day: 500 MB times 30 days is 15 GB a month, and a single 4 GB file cannot be fetched at all on the free path.
- interface detail: Web app (Chrome/Firefox/mobile) plus a documented JDownloader integration page; file management, zip/unzip, split/join, streaming. No public API documentation was found on the pages read.
- tooling: Browser; JDownloader integration is documented by the vendor at dasan.co/jdownloader.
- composes with: It is the debrid layer itself: it accepts a host link, torrent, magnet or NZB and returns a direct link, so it replaces the whole downloader chain rather than slotting into it.
- reliability: Cloudflare fronts the site and challenged a plain client probe (challenge detected on a 200 response), so unattended automation needs a browser session. Free jobs are capped so low that queue failures are cheap to retry.
- notes: The most precisely stated free tier in the premium-link class after LeechPremium, but it is a torrent/usenet trial rather than a host-link unlock. Documented as trial-only because the free path cannot fetch a host link at any size. Included because the pay-per-GB model is the only pricing shape in the sector that could beat a subscription for one 20 GiB pull, but the vendor publishes neither the rate nor the retention, so the comparison cannot be completed from its pages.
- evidence note: The free-trial terms and the $2.99 entry price are quoted from the live landing page; the per-GB rate, retention and file-host free path are not published, so the paid economics stay unverified.
- extras:
  - free_job_scope: magnet, torrent, NZB
  - paid_model: prepaid balance, per GB, $2.99 minimum
  - jdownloader_integration: https://dasan.co/jdownloader
  - usenet: yes, NZB accepted
- evidence:
  - [1] 2026-10-23: 'One free job per 24 hours, up to 500 MB. No account required.'; 'Start from $2.99 and pay only for the GBs you use'; host list including Rapidgator, KatFile, Keep2Share, 1Fichier, Turbobit, Mega
  - probe:https://dasan.co/ 2026-10-23: HTTP 200, 42673 bytes, sha256 7ca8a7590ab1264f..., challenge detected (Cloudflare) for a non-browser client
  - [1] 2026-10-23: torrent, magnet and NZB support; 'One free job per 24 hours, up to 500 MB. No account required.'; 'Start from $2.99 and pay only for the GBs you use'
- sources:
  - [1] https://dasan.co/
