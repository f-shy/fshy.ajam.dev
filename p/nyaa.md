# Nyaa

> nyaa.si | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nyaa/ | JSON https://fshy.ajam.dev/api/v1/entity/nyaa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nyaa

- `debrid/nyaa` | qualifies | evidence documented | binding request-rate | category torrent index, anime and East Asian media (RSS, no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://nyaa.si/
- price USD 0
- free tier: No account: the search feed at /?page=rss&q=... returned RSS 2.0 with a nyaa namespace and per-item torrent links. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: the tracker caps a single torrent file and the site caps uploads, neither of which is a client-side limit on the index | source: [2] | note: the caps were not read on the pages fetched
- retention: releases persist; the feed returns only the query's matches, so age is not implied by the feed | source: [1]
- egress: no byte allowance: the feed serves XML and .torrent links; the transfer is client-to-swarm | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account for search or RSS; uploading and commenting need one, which is not needed here.
- interface: rest
- limits:
  - request-rate (binding): none published on the pages fetched; the feed answered immediately with no 429 [1]
- limits note: The feed is the whole interface: no key, no token, no pagination wall on the routes tried.
- binding note: No byte accounting exists on an index; polling a saved search is a handful of requests a day, far below anything that would throttle.
- interface detail: RSS at /?page=rss with the usual query parameters (q, c, f); each item's <link> is a .torrent download and <guid> is the view page.
- endpoint: https://nyaa.si/?page=rss&q=ubuntu&c=0_0&f=0
- tooling: Any RSS reader; the item link is already the .torrent, so no page fetch is needed.
- composes with: A saved search as an RSS feed is the cheapest possible subscription: one URL per interest is polled and returns .torrent links, which a debrid service then turns into cached playback.
- reliability: A query with no match returns a valid feed with zero items rather than an error, so a client must check item count rather than status. The one match for 'ubuntu' was dated 2009, so the index holds very old items and a fresh-looking feed says nothing about freshness.
- notes: The narrowest and most reliable feed in the sector: a saved search is a URL, and the URL returns.torrent files. Useless outside anime and East Asian media, which is why it is a second feed rather than the primary one.
- evidence note: The feed was fetched on 2026-10-23 and parsed: one item for 'ubuntu', with a .torrent link. A month of polling would raise it to measured.
- extras:
  - feed_protocol: rss2
  - namespace: nyaa
  - saved_search: yes
- evidence:
  - [1] 2026-10-23: RSS 2.0 with the nyaa namespace, channel title 'Nyaa - ubuntu - Torrent File RSS', items whose link is https://nyaa.si/download/<id>.torrent and pubDate 2009 for the one match
- sources:
  - [1] https://nyaa.si/?page=rss&q=ubuntu&c=0_0&f=0
  - [2] https://nyaa.si/
