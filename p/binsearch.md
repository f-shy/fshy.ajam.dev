# Binsearch

> binsearch.info | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/binsearch/ | JSON https://fshy.ajam.dev/api/v1/entity/binsearch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Binsearch

- `debrid/binsearch` | qualifies | evidence measured | binding none | category Usenet binary search engine (HTML search, anonymous NZB build) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.binsearch.info/
- free tier: No account and no key. GET /search?q=linux returned 98,890 bytes of results, paginated to 174 pages. GET /nzb?q=linux&<base64 collection id>=on returned a 4,229-byte NZB carrying 9 files. The site publishes no daily counter anywhere a reader can reach. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: 'unlimited' is a statement about the absence of a published quota, supported by a 6-request burst, not by a vendor sentence.
- per-object cap: not applicable: the answer is an NZB pointer file (4,229 bytes, 9 files), never the payload | source: [1]
- retention: not stated on the pages read. A third-party indexer comparison claims 'up to 1,100 days of binary retention, searches 400+ popular newsgroups by default' (nzbhydra.com, 2026-10-23). | source: [2] | note: reported, not documented: Binsearch publishes no retention figure on its search or results page.
- egress: No metering. Every answer is a small XML pointer file; the bytes themselves come from whichever news provider the account is with. | metered: no | source: [1]
- identity: anonymous | detail: No account, no key, no cookie. Search and NZB creation both answered an anonymous request with no credential of any kind.
- interface: rest
- limits:
  - request-rate: none observed: 6 consecutive anonymous searches in one session all returned 200 probe:https://www.binsearch.info/search?q=test1..test6
- limits note: Page depth is the only ceiling the service shows: the query 'linux' exposed 174 pages. No per-IP shaping was observed and no quota page exists to read.
- binding note: Nothing in the seven-kind vocabulary fails at a client pulling 1 TiB a month: there is no counter to hit. The real cost is two GETs per NZB plus a scraper that survives a front-end rewrite, which is a tooling cost and not a limit.
- interface detail: HTML search over HTTP GET against /search (Next.js front end, results server-rendered). NZB is built by a GET to /nzb?q=<query>&<name>=on where <name> is the base64 collection id carried by each result's checkbox. There is no Newznab endpoint: /api returns 404.
- endpoint: https://www.binsearch.info/search?q=<query> ; https://www.binsearch.info/nzb?q=<query>&<collection-id>=on
- tooling: No Newznab API, so Sonarr, Radarr, Prowlarr and NZBHydra2 cannot add it as an indexer. A wrapper must GET /search, parse the collection ids out of the checkbox names, and re-issue GET /nzb. Two GETs per download.
- composes with: A fallback name search when every Newznab indexer is down or refuses registration; the NZB it returns goes into the same SABnzbd or NZBGet queue as any other.
- reliability: Advertiser-supported binary search engine; results are raw article headers, so completion depends entirely on the retention of the news provider paid for, and dead posts stay listed until the indexer notices.
- notes: The result page is a Next.js front end but the results are server-rendered, so the HTML carries them; that is why a plain GET works where NZBIndex's does not. A query string is mandatory on /nzb or the proxy's parameter append corrupts the path, which is a tooling detail documented here so the subsequent audit does not read a 404 as a dead endpoint.
- evidence note: Search and NZB creation were both run today and both produced payload bytes with a recorded digest. Nothing here is quoted from a third party. What would raise nothing: the rung is already the top one; what is missing is a long-run rate test, which a 6-request burst does not provide.
- extras:
  - price: USD 0
  - measurements[0].url: https://www.binsearch.info/search?q=linux&o=1
  - measurements[0].status: 200
  - measurements[0].bytes: 98890
  - measurements[0].sha256: c7624df04530992f588d89403f858d43888f39b640d376a279f0cf500b4df236
  - measurements[1].url: https://www.binsearch.info/nzb?q=linux&Mjg4Yjk3YmYtODlhMy0zNTllLThhYzgtZDFiODYyM2NhYTlj=on
  - measurements[1].status: 200
  - measurements[1].bytes: 4229
  - measurements[1].sha256: 7070590ff44a8fa02a9da80d3c706348b5a8a0b5ca8710a9d8a6c18f7444a089
  - nzb_is_newznab: no
  - burst: 6 sequential searches, all 200
- evidence:
  - probe:https://www.binsearch.info/search?q=linux&o=1 2026-10-23: anonymous HTML search returned 200 and 98,890 bytes with 174 result pages and per-result collection ids
  - probe:https://www.binsearch.info/nzb?q=linux&Mjg4Yjk3YmYtODlhMy0zNTllLThhYzgtZDFiODYyM2NhYTlj=on 2026-10-23: anonymous GET returned 200, a 4,229-byte NZB with 9 <file> elements (sha256 7070590f...)
  - probe:https://www.binsearch.info/api 2026-10-23: the API path does not exist: 404, so there is no Newznab surface to add to a client
  - [2] 2026-10-23: third-party claim of 1,100 days retention and 400+ groups; used only for the retention field, which Binsearch does not publish
- sources:
  - [1] https://www.binsearch.info/
  - [2] https://nzbhydra.com/indexers/
