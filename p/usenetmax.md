# UsenetMax

> usenetmax.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetmax/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetmax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetMax

- `debrid/usenetmax` | qualifies-with-caveat | evidence unverified | binding request-rate | category free usenet server (independent, demo indexer) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:12.551Z (live) | stale on 2026-11-19
- url https://www.usenetmax.com/
- price USD 0
- free tier: 'Free usenet server' with 'no credit card required, a password will be emailed to you'. Includes NNTP access for a newsreader or downloader, and a web-to-usenet gateway for browser access. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: Not stated anywhere read. The site carries only the groups its members request: 'We only carry the newsgroups that our members have requested. To add a newsgroup, please email support.' | source: [1]
- egress: Nothing published about speed, volume or retention; the only number on the site is the connection count | metered: no | source: [1]
- identity: email | detail: An email address: 'no credit card required, a password will be emailed to you'. The terms add that only one free account is permitted per individual, household or IP address.
- interface: nntp
- limits:
  - request-rate (binding): 3 connections free, up to 12 on a premium account [2]
- limits note: The terms permit one free account per individual, household or IP address. The bundled indexer is ikbin, an open-source binary indexer whose own FAQ says it is 'a demonstration and testing site' and that 'content may be cleared out rather unexpectedly if a beta goes south'. The premium account price is not published on the pages read; whether a datacenter address is accepted is not published.
- binding note: Three simultaneous connections is the ceiling and it is published; no volume or retention figure exists to bind instead. Three connections will not saturate a line, so throughput, not volume, is what a 50 GiB month runs into.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Would stack as a zero-cost secondary for recent, popular binaries if it is alive; it cannot be a primary, because three connections and a member-requested group list cannot cover a workload.
- reliability: A demo server attached to a demo indexer, with a group list that only covers what members ask for and a stated risk that content disappears when the beta misbehaves. On 2026-11-03 neither the website (an HTTP GET timed out) nor the NNTP port of news.usenetmax.com (a TCP connect timed out) answered, while DNS for both names resolves and a Wayback Machine copy of the home page dated 2026-06-27 shows the offer. Liveness is unconfirmed: the page text that reads today is an index copy.
- notes: Usenet provider advertising free trial access, though live registration availability remains unconfirmed.
- evidence note: The offer text was read from the live page body on 2026-10-23, but no HTTP status accompanied it and the direct fetch failed at network requests. Nothing was connected to, so neither the account flow nor the service's availability is established.
- extras:
  - host: news.usenetmax.com
  - port: 563
  - connections_free: 3
  - connections_premium: 12
  - liveness: unconfirmed: the HTTP GET and the NNTP TCP connect both timed out on 2026-11-03; the last archived copy of the home page is dated 2026-06-27
- evidence:
  - [1] 2026-10-23: 'Free usenet server'; 'NNTP access for newsreader or downloader'; 'Web to usenet gateway for browser access'; 'no credit card required a password will be emailed to you'
  - [2] 2026-10-23: Host news.usenetmax.com, port 563, 'Connections: 3 (up to 12 for a premium account)'
  - [3] 2026-10-23: the bundled indexer is ikbin, 'a demonstration and testing site'; 'Content may be cleared out rather unexpectedly if a beta goes south'
  - probe:https://www.usenetmax.com/ 2026-11-03: an HTTP GET to the site timed out with no response | capture: sha256:43164a7f5e832a98a37072686a067b1f33ecf3b893b3573bcbf71e81c2696fb4 | quote: "error": "timeout"
  - probe:news.usenetmax.com:563 2026-11-03: a TCP connection to news.usenetmax.com port 563 timed out | capture: sha256:d25e6f18540027f651926129ddc468d98691332b63fd738a5109b1888b89da4c | quote: "err": "TimeoutError('timed out')"
  - [4] 2026-11-03: an archived copy of the home page dated 2026-06-27 shows the free server offer | capture: sha256:4ac116bda4c6b5f844c1240c30dcfd6e01124432a3b3fc5d0c0a9e805925b38b | quote: Free usenet server
  - [5] 2026-11-03: one free account per individual, household or IP address | capture: sha256:b4f478e94fb02ed466840555e63e2c8970fa8cbe1c584e09033c838e16c09cd4 | quote: Only one free account is permitted per individual, household, or IP address.
  - [2] 2026-11-04: the connection limit of 3 free and up to 12 premium is stated | capture: sha256:2b5b9ad06a275791f1ad7dbb212c1f45b9c64efb31f36dd9c01aa7d4322c8581 | quote: Connections: 3 (up to 12 for a premium account, but more than 3 rarely improves anything)
  - [1] 2026-11-04: the home page text offers a free usenet server | capture: sha256:493b485d7dfa2b65c25df6e00518ec28bdf23a22842c898793c4ace191116d31 | quote: Free usenet server
  - probe:https://www.usenetmax.com/ 2026-11-04: a direct HTTP GET timed out with no response | capture: sha256:a4bb69063556437c4fc11c8dd19f10a2466173d1931a38132d359a3d2f04f377 | quote: "error": "timeout"
  - probe:news.usenetmax.com:563 2026-11-04: a TCP connect to port 563 timed out | capture: sha256:550cd84dcb716f13b645d5fce9bb27b9b7e99054ab719f595a7c250ae6e3dbd8 | quote: TimeoutError('timed out')
- sources:
  - [1] https://www.usenetmax.com/
  - [2] https://www.usenetmax.com/how-to/
  - [3] https://news.usenetmax.com/faq.php
  - [4] https://web.archive.org/web/20260627052500/https://www.usenetmax.com/?provider=wayback
  - [5] https://www.usenetmax.com/terms/
