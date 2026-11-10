# LeechPremium

> leechpremium.link | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leechpremium/ | JSON https://fshy.ajam.dev/api/v1/entity/leechpremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LeechPremium

- `debrid/leechpremium-link` | qualifies-with-caveat | evidence documented | binding request-rate | category premium link generator (free leech of host links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://leechpremium.link/
- free tier: 'Free users can generate up to 5 links per day with a maximum file size of 1GB.' Free speed 'Up to 50 MB/s'; premium 'Up to 100+ MB/s'. 'No registration' required. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The FAQ claims 50+ hosters including Rapidgator, Uploaded and Nitroflare. Premium removes both caps (unlimited downloads, no file size limit).
- per-object cap: 1 GB per file on the free tier ('with a maximum file size of 1GB'); no limit on premium. | bytes: 1073741824 | source: [1]
- retention: unverified: the FAQ does not say how long a generated link, or the copy on their server, survives. | source: [1]
- egress: Free users download from the leech server at 'Up to 50 MB/s'; no byte allowance is stated for the download itself. | metered: no | free allowance: unstated; the caps are 5 links/day and 1 GB/file | source: [1]
- identity: anonymous | detail: 'No registration' is stated in the FAQ and on the front page; no account field appears in the generate flow.
- interface: unknown
- limits:
  - request-rate (binding): 5 generated links per day on the free tier [1]
  - per-object-cap: 1 GB per file on the free tier [1]
- limits note: The FAQ also names the failure mode that limits the service itself: an error occurs when 'the filehost's premium account has reached daily bandwidth limit'. The leech site is itself a free user of the host.
- binding note: Five links a day binds before the 1 GB cap does: at 5 links/day the monthly ceiling is 150 GB even with maximum-size files, and 1 TiB/month would need 34 files a day.
- interface detail: A single web form: paste the host link, click Generate, receive a premium link. No API documentation was found; a wrapper would drive the form or the resulting page with a browser session.
- tooling: Nothing published. The FAQ recommends IDM, FDM, JDownloader, wget or curl for the generated link, which is a plain resumable HTTP URL.
- composes with: Its output is an ordinary HTTP link, so it feeds any downloader or storage relay. 5 links/day at 1 GB is 5 GB/day of ceiling, which is 150 GB/month at best.
- reliability: The leech depends on the vendor's own premium accounts, so it fails when those hit the host's daily bandwidth cap. Ads fund it, and the generated link is a third-party copy, so availability is the vendor's uptime, not the host's.
- notes: This is the clearest published free cap in the sector: 5 links/day, 1 GB/file, no account. It is not a debrid service and it does not touch usenet or torrents; it only converts host links that the vendor's accounts can still fetch.
- evidence note: The caps are quoted verbatim from the site's own FAQ. What is not tested is whether a generation succeeds on 2026-10-23: leechpremium.link did not resolve from this host (DNS failure) and the page was read through network requests.
- extras:
  - free_links_per_day: 5
  - free_max_file_gb: 1
  - premium_speed_mbps: 100+
- evidence:
  - [1] 2026-10-23: 'Free users can generate up to 5 links per day with a maximum file size of 1GB'; 50 MB/s free vs 100+ MB/s premium; 'No registration'
  - [2] 2026-10-23: front page offers a paste box and 'No registration required for free users'; names 50+ hosts including Rapidgator, Uploaded, Nitroflare
  - probe:https://leechpremium.link/ 2026-10-23: reachability is network-dependent
- sources:
  - [1] https://leechpremium.link/faq.php
  - [2] https://leechpremium.link/
