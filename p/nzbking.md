# NZBKing

> nzbking.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbking/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbking.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBKing

- `debrid/nzbking` | qualifies | evidence measured | binding none | category Usenet binary search engine (HTML search, anonymous NZB download) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.nzbking.com/
- free tier: No account and no key. GET /search/?q=linux returned 54,006 bytes with a rendered result list, and GET /nzb:<details-id>/ returned a 7,231-byte NZB with 19 files. No daily counter is published on the site. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No quota page exists; the claim rests on a 5-request burst rather than a vendor sentence.
- per-object cap: not applicable: the answer is an NZB pointer file (7,231 bytes, 19 files), never the payload | source: [1]
- retention: not stated on the pages read. A third-party indexer comparison claims '4,000+ days retention, 200 million+ Usenet posts indexed, 3,570 newsgroups' (nzbhydra.com, 2026-10-23). | source: [2] | note: reported
- egress: No metering. The result page and the NZB are both kilobytes; the payload comes from the news provider. | metered: no | source: [1]
- identity: anonymous | detail: No account and no key: search and NZB download both answered an anonymous request.
- interface: rest
- limits:
  - request-rate: none observed: 5 consecutive anonymous searches in one session, all 200 probe:https://www.nzbking.com/search/?q=t1..t5
- limits note: No request counter, byte counter or per-IP shaping was observed.
- binding note: Nothing in the vocabulary fails at 1 TiB/month. The practical ceiling is index coverage per newsgroup, which is not a limit kind.
- interface detail: HTML search over HTTP GET against /search/?q=<query>. Each result carries a /details:<id>/ link and an NZB link served as /nzb:<id>/. Both are plain GETs.
- endpoint: https://www.nzbking.com/search/?q=<query> ; https://www.nzbking.com/nzb:<id>/
- tooling: No Newznab API found, so Prowlarr and NZBHydra2 cannot add it. A wrapper parses /search and GETs /nzb:<id>/, and the site also offers a per-query RSS feed (the page advertises 'Get query as RSS feed'), which is the cheaper automation route.
- composes with: A third unnamed fallback that also exposes an RSS feed per query, so a cron job can watch a name without a scraper.
- reliability: The result page loads a cookie-consent script and an analytics tag before results; the results themselves are server-rendered, so a plain GET still sees them.
- evidence note: Search and download were run today with status, bytes and digest. A per-query RSS feed is advertised in the page text but was not fetched, so the feed route is documented-by-advertisement only.
- extras:
  - price: USD 0
  - measurements[0].url: https://www.nzbking.com/search/?q=linux
  - measurements[0].status: 200
  - measurements[0].bytes: 54006
  - measurements[0].sha256: d7f3e267c6a168fc7214a81e819162f9d0ac653427b9ca672eed44c9762916b8
  - measurements[1].url: https://www.nzbking.com/nzb:6ab08229f21b66ba553317a8/?x=1
  - measurements[1].status: 200
  - measurements[1].bytes: 7231
  - measurements[1].sha256: a7308d721125bd857186e390fecf88ab4c20977e4679317419cea408f0898fb4
  - nzb_is_newznab: no
  - rss: advertised per query; not fetched
  - burst: 5 sequential searches, all 200
- evidence:
  - probe:https://www.nzbking.com/search/?q=linux 2026-10-23: anonymous search returned 200 and 54,006 bytes with a rendered result table and per-result /details:<id>/ links
  - probe:https://www.nzbking.com/nzb:6ab08229f21b66ba553317a8/?x=1 2026-10-23: anonymous NZB download returned 200, application/x-nzb, 7,231 bytes, 19 <file> elements (sha256 a7308d72...)
  - probe:https://www.nzbking.com/api/nzb?id=<id> 2026-10-23: no Newznab-style API path: 404, so a client cannot add it as an indexer
- sources:
  - [1] https://www.nzbking.com/
  - [2] https://nzbhydra.com/indexers/
