# BestDebrid

> bestdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bestdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/bestdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BestDebrid

- `debrid/bestdebrid` | qualifies-with-caveat | evidence documented | binding pull-count | category multi-hoster (premium link generator and torrent seedbox) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:39:03.000Z (live) | stale on 2026-11-23
- url https://bestdebrid.com/en/downloader/
- price EUR 4.50/month subscription; EUR 3 per 15 days one-time (USD 5.05 and USD 3.37 at the 2026-10-23 ECB-derived rate of 0.8915 EUR per USD) | parsed USD 5.04/mo
- free tier: As a free user, you can debride one link at a time. The FAQ puts the free account at 'up to 1 link per day'. The guest downloader covers only hosts that are already free: 1fichier, facebook, redtube, twitter, xnxx, xvideos, youporn, youtube. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: Two different numbers appear. The FAQ says 1 link/day for a free account. The API reference says 70 unique files per 24 h per account (error 121), which is the paid-account ceiling. The conservative figure is used here. Guest 1fichier allowance is its own counter: 'Links : 0/1 Per Day'.
- per-object cap: not applicable: the service unlocks a file-host URL and does not store the object | source: [1] | note: The paid plan advertises 'Unlimited remote traffic', which is a transfer claim, not a per-object size.
- retention: not applicable: no storage product. Generated links are temporary and the downloader keeps a history of them for the account. | source: [2]
- egress: Download runs from BestDebrid's servers to the user. Premium advertises 'Unlimited bandwidth' and 'Unlimited remote traffic(1)', with the footnote 'Remote traffic (excluding Internet service providers)'. Free users are capped by links per day, not by bytes. | metered: no | free allowance: 1 link/day (free account); per-host counters shown live, e.g. 1fichier 0/1 per day | source: [3]
- identity: email | detail: Free account needs a username, an email address and a password. Google and Facebook sign-in also offered. No card and no phone on the free path. Paid plans are bought as a key or by subscription.
- interface: rest, webdav
- limits:
  - pull-count (binding): 1 link per day on a free account; 70 unique files per 24 h on a paid account (web and API combined) https://bestdebrid.com/en/faq/ ; https://bestdebrid.com/fr/restapi.php
  - request-rate: 1 concurrent link as a free user; error 122 'Too many unrestricts in progress - retry in ~1 min' https://bestdebrid.com/en/downloader/ ; https://bestdebrid.com/fr/restapi.php
  - per-ip-shaping: error 632 'VPN/proxy detected' and error 56 'Invalid IP address, waiting time not elapsed' block datacentre and VPN egress [4]
- limits note: Hosts go offline individually; the downloader page showed 51 of 52 hosts online and filejoker listed as offline on the read date.
- binding note: At 1 TiB/month the free tier fails on link count long before bytes: 1 link/day is 30 unlocks a month, so 1 TiB of monthly transfer would need a 34 GiB average file. On the paid tier the same counter binds first at 70 files per 24 h.
- interface detail: REST API documented at /fr/restapi.php with API keys, per-host limits endpoint and error codes; the support form lists 'JDownloader, Kodi, Stremio, WebDAV, API' as client categories.
- endpoint: https://bestdebrid.com/api/v1/hostslimits
- tooling: JDownloader/IDM via the API, a documented REST API, and a browser downloader. No rclone backend.
- composes with: A sub-USD-5 one-time 15-day pass (EUR 3) at unlimited remote traffic is the cheapest per-TB route among debrid providers for a user who needs many file hosts rather than torrent cache; it pairs with JDownloader for a resumable queue.
- reliability: Free tier covers only hosts that are already free; filejoker was offline on the read date; VPN and proxy egress is refused with error 632; the paid plan allows VPN.
- notes: The free tier is not a free multi-hoster: its host list is the set of hosts that need no debrid. The sub-USD-5 band is the paid side. USD conversions use the exchangerate-api USD base read on 2026-10-23 (EUR 0.891529 per USD). Cheapest per-month shape is the 365-day one-time pass at EUR 45, or EUR 3 per 15 days for a short burst. The '2147483647 GB' bandwith figure is 2^31-1, an integer sentinel, not a measured allowance.
- evidence note: Free and paid limits are quoted from the vendor's FAQ, plans page and API reference. A generated link pulled end to end would raise it to measured.
- extras:
  - hosts_listed: 52
  - hosts_online_on_read: 51
  - offline_host_on_read: filejoker
  - free_hosts: 1fichier, facebook, redtube, twitter, xnxx, xvideos, youporn, youtube
  - api: documented REST API with per-host limits endpoint
- evidence:
  - [2] 2026-10-23: 'As a free user, you can debride one link at a time', the free-host list (1fichier facebook redtube twitter xnxx xvideos youporn youtube), 'Files per day: 0/100', 'Bandwidth per day: 2147483647 GB', and the 1fichier counter 'Links : 0/1 Per Day'
  - [1] 2026-10-23: The free account 'includes several limitations: fewer supported file hosts; up to 1 link per day; limited access to certain features'
  - [3] 2026-10-23: One-time prices EUR 3 / 15 days, EUR 5 / 31 days, EUR 25 / 180 days, EUR 45 / 365 days, and a EUR 4.50/month auto-renewing subscription, each with 'Unlimited remote traffic' and seedbox
  - [4] 2026-10-23: 'Quota journalier : chaque compte est limité à 70 fichiers uniques par 24 h, web et API confondus (erreur 121)', error 56 (free daily quota), error 122 (concurrency), error 632 (VPN/proxy), and a per-host limits endpoint returning 'linksperday' and 'bandwidth' such as '150 GB'
- sources:
  - [1] https://bestdebrid.com/en/faq/
  - [2] https://bestdebrid.com/en/downloader/
  - [3] https://bestdebrid.com/en/plans/
  - [4] https://bestdebrid.com/fr/restapi.php
