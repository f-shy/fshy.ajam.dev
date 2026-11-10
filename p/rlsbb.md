# RLSBB

> rlsbb.cc | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rlsbb/ | JSON https://fshy.ajam.dev/api/v1/entity/rlsbb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RLSBB (ReleaseBB)

- `debrid/rlsbb` | qualifies-with-caveat | evidence documented | binding request-rate | category DDL release index (TV, movies, scene releases with host links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://rlsbb.cc/
- price USD 0
- free tier: No account to read: /feed/ returned 50 items and the post page carried UPLOADY, NiTROFLARE and RAPiDGATOR links in clear text. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an index | source: [2]
- retention: Posts persist. The feed carries the 50 most recent items. | source: [1]
- egress: No byte allowance. The post links uploady.io, nitroflare.com and rapidgator.net for each release, plus a limetorrents search for the same release name. | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account to read the feed or a post. The site pushes registration only for the host accounts it advertises (rapidgator, uploady).
- interface: rest
- limits:
  - request-rate (binding): robots.txt sets Crawl-delay: 10 for the wildcard agent (0.1 req/s) and Disallow: / for it [3]
- binding note: Crawl-delay 10 is the only published request interval among debrid providers, and it is 0.1 req/s, far below what 1 TiB per month pull needs; it is the constraint met first here.
- interface detail: RSS 2.0 at /feed/ (text/xml, 50 items with title, link, dc:creator, pubDate and category). A search portal at search.rlsbb.ru has a 'light' mode that returns titles only.
- endpoint: https://rlsbb.cc/feed/
- tooling: RSS reader. Each post body is one line of host links, so extraction is a regex over the host URLs plus the protected.to nfo and subtitle links.
- composes with: Feed to post to a rapidgator, nitroflare or uploady link for the debrid service; the same post also links a limetorrents search, which gives the torrent path for the identical release.
- reliability: Domain rotation is the normal failure: the home page title reads 'UK users use .in domain or use VPN' and .cc, .in, .to and .ru all appear on the page. Host link sets change with the affiliate arrangement.
- notes: The only index in the sector that publishes a request interval. Documented as a technical constraint, not a judgement about use.
- evidence note: Feed, one post and robots.txt were fetched on 2026-10-23. A month of feed capture would raise it to measured and would also record how often the domain moves.
- extras:
  - feed_items: 50
  - feed_protocol: rss2
  - crawl_delay_s: 10
  - robots_disallow: /
- evidence:
  - [1] 2026-10-23: text/xml RSS with 50 item entries, channel title 'ReleaseBB', lastBuildDate Fri, 23 Oct 2026 12:10:21 +0000
  - [4] 2026-10-23: UPLOADY, NiTROFLARE and RAPiDGATOR links for three resolutions, plus a limetorrents search link, all rendered anonymously
  - [3] 2026-10-23: 
- sources:
  - [1] https://rlsbb.cc/feed/
  - [2] https://rlsbb.cc/
  - [3] https://rlsbb.cc/robots.txt
  - [4] https://rlsbb.cc/the-young-and-the-restless-s54e11-720p-web-h264-dirt/
