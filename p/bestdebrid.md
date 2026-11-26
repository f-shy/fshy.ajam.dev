# BestDebrid

> bestdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bestdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/bestdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BestDebrid

- `debrid/bestdebrid` | qualifies-with-caveat | evidence documented | binding pull-count | category multi-hoster (premium link generator and torrent seedbox) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:53.123Z (live) | stale on 2026-12-26
- url https://bestdebrid.com/en/downloader/
- price EUR 4.50/month subscription; EUR 3 per 15 days one-time (USD 5.05 and USD 3.37 at the 2026-10-23 ECB-derived rate of 0.8915 EUR per USD) | parsed USD 5.07/mo
- free tier: As a free user, you can debride one link at a time. The FAQ puts the free account at 'up to 1 link per day'. The guest downloader covers only hosts that are already free: 1fichier, facebook, redtube, twitter, xnxx, xvideos, youporn, youtube. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: Two different numbers appear. The FAQ says 1 link/day for a free account. The API reference says 70 unique files per 24 h per account (error 121), which is the paid-account ceiling. The conservative figure is used here. Guest 1fichier allowance is its own counter: 'Links : 0/1 Per Day'.
- per-object cap: not applicable: the service unlocks a file-host URL and does not store the object | source: [1] | note: The paid plan advertises 'Unlimited remote traffic', which is a transfer claim, not a per-object size.
- retention: Not applicable: no storage product. A generated link is valid from a few minutes to approximately 24 hours depending on the file host. | source: [2]
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
- reliability: Free tier covers only hosts already free. On the read date 49 of 52 hosts were online, with hulkshare, silkfiles and world-files marked offline; 8 hosts are marked free. VPN and proxy use is refused on free accounts and allowed on Premium.
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
  - [1] 2026-11-25: generated link validity spans minutes to about 24 hours | capture: sha256:0a2d36c12d8beee0dc712cc54913f36fe6dc37ea69d32b9d901360138d171575 | quote: The validity period of a generated link depends on the file host and may range from a few minutes to approximately 24 hours.
  - [1] 2026-11-25: the free account allows one link per day | capture: sha256:0a2d36c12d8beee0dc712cc54913f36fe6dc37ea69d32b9d901360138d171575 | quote: - up to 1 link per day;
  - [4] 2026-11-25: all accounts are capped at 70 unique files per 24 hours across web and API | capture: sha256:f82dcaca9e59129b123d19b8f2db17c99548bc9b89e8a32af3062776cbb3978b | quote: Quota journalier : chaque compte est limité à 70 fichiers uniques par 24 h, web et API confondus (erreur 121).
  - [2] 2026-11-25: 49 of 52 hosts were online on the read date | capture: sha256:332613fe79b40a8a5ac94ed921e486efe10e72ec0c2696d50939e5ef3a3ecd2a | quote: 49 / 52 hosts online
  - [3] 2026-11-25: the 15-day one-time plan costs EUR 3 | capture: sha256:621d6a9791683922584608405e21e2b016aa69dcb114253a202e941d8e29f612 | quote: € 3
  - [1] 2026-11-25: the service is browser-only with no software to install | capture: sha256:0a2d36c12d8beee0dc712cc54913f36fe6dc37ea69d32b9d901360138d171575 | quote: BestDebrid works entirely online through your web browser.
  - [5] 2026-11-25: 49 of 52 hosts online and 8 free hosts on the read date | capture: sha256:058d3a4b63c0b52feb884db762d2e4306995945c35422d3752fcae3512bb9a2f | quote: 49 / 52 online 8 free Automatic checks
  - [1] 2026-11-25: the FAQ describes the Premium payment gates on its accepted-methods list | capture: sha256:0a2d36c12d8beee0dc712cc54913f36fe6dc37ea69d32b9d901360138d171575 | quote: We accept:
- sources:
  - [1] https://bestdebrid.com/en/faq/
  - [2] https://bestdebrid.com/en/downloader/
  - [3] https://bestdebrid.com/en/plans/
  - [4] https://bestdebrid.com/fr/restapi.php
  - [5] https://bestdebrid.com/en/hosters/
