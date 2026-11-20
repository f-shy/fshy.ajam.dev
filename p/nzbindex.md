# NZBIndex

> nzbindex.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbindex/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbindex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBIndex

- `debrid/nzbindex` | qualifies | evidence measured | binding none | category Usenet search engine (undocumented JSON search API, anonymous NZB download) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.nzbindex.com/
- free tier: No account and no key. GET /api/search?q=linux returned 7,318 bytes of JSON: 25 items, totalElements 4,348 over 174 pages. GET /download/<item-id>.nzb returned a 4,264-byte NZB. The route is what the site's own single-page app calls; no API documentation was found on any page reached. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No quota is published, and no account exists to attach one to. 6 rapid requests and 1 download in one session produced no 429.
- per-object cap: not applicable: the answer is an NZB pointer file (4,264 bytes), never the payload | source: [1]
- retention: not stated on the pages read. A third-party indexer comparison claims 'approximately 1,900 days retention, 900+ newsgroups indexed' (nzbhydra.com, 2026-10-23). | source: [2] | note: reported
- egress: No metering. The JSON is a result list and the download is an XML pointer file measured at 4,264 bytes. | metered: no | source: [1]
- identity: anonymous | detail: Nothing is collected: both the JSON search and the NZB download answered without a cookie, header or key.
- interface: rest
- limits:
  - request-rate: none observed: 6 consecutive JSON searches in one session, all 200 probe:https://www.nzbindex.com/api/search?q=test1..test6
- limits note: Page size is fixed at 25 in the JSON the app consumes (data.page.size = 25); there is no limit parameter to raise it.
- binding note: No byte counter, no daily cap, no account. At 1 TiB/month the indexer is not the constraint; the news provider's retention is, and a missing post costs a failed grab rather than a quota.
- interface detail: The search page is a client-rendered Next.js app: /search?q=linux returns 8,702 bytes of HTML shell with zero results and an empty query state. The real interface is GET /api/search?q=<query>, which returns JSON with data.content[] and data.page{size,number,totalElements,totalPages}. NZB download is GET /download/<item-id>.nzb.
- endpoint: https://www.nzbindex.com/api/search?q=<query> ; https://www.nzbindex.com/download/<id>.nzb
- tooling: No Newznab endpoint, so Prowlarr, NZBHydra2, Sonarr and Radarr cannot add it directly. A wrapper is small: one GET for JSON, one GET per download, both unauthenticated. The JSON route is undocumented and can change with any front-end deploy, which is the maintenance cost.
- composes with: A second unnamed fallback beside Binsearch, and the only one of the three open engines with a JSON answer, so it is the easiest to wrap and the one to poll when a name has to be resolved without an account.
- reliability: Advertiser-supported; the JSON route is an internal app call, so a front-end deploy can move or rename it without notice, and a scrape that depended on it fails silently as an empty result list.
- notes: Adding ?x=1 made the path valid and the download worked.
- evidence note: Search and download were run today with status, byte count and digest recorded. The undocumented route is the fragility, not the confidence rung: it worked when measured and may not tomorrow.
- extras:
  - price: USD 0
  - measurements[0].url: https://www.nzbindex.com/api/search?q=linux
  - measurements[0].status: 200
  - measurements[0].bytes: 7318
  - measurements[0].sha256: 2333a15273d5eb24afc8e4aff8f09d7fe7976967dd323248f378c221f4ac91b5
  - measurements[1].url: https://www.nzbindex.com/download/288b97bf-89a3-359e-8ac8-d1b8623caa9c.nzb?x=1
  - measurements[1].status: 200
  - measurements[1].bytes: 4264
  - measurements[1].sha256: 12eb97154cf848ba0dd79400d412d3714595b9961c7e9c0cda9fdccf14d5b0c7
  - measurements[2].url: https://www.nzbindex.com/search?q=linux
  - measurements[2].status: 200
  - measurements[2].bytes: 8702
  - measurements[2].sha256: 01ff0f47761e25a17ea5b8d4681f766ee9daa6643acf6ba13b01ea6ea761d6cf
  - nzb_is_newznab: no
  - burst: 6 sequential JSON searches, all 200
- evidence:
  - probe:https://www.nzbindex.com/api/search?q=linux 2026-10-23: anonymous JSON search returned 200 and 7,318 bytes: 25 items, totalElements 4,348, 174 pages
  - probe:https://www.nzbindex.com/download/288b97bf-89a3-359e-8ac8-d1b8623caa9c.nzb?x=1 2026-10-23: anonymous NZB download returned 200, application/x-nzb, 4,264 bytes (sha256 12eb9715...)
  - probe:https://www.nzbindex.com/search?q=linux 2026-10-23: the HTML page carries no results: 8,702 bytes of app shell with "q":"" in the serialised state, which is why a scraper must use /api/search
- sources:
  - [1] https://www.nzbindex.com/
  - [2] https://nzbhydra.com/indexers/
