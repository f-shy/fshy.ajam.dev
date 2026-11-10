# PreDB.me

> predb.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/predb/ | JSON https://fshy.ajam.dev/api/v1/entity/predb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PreDB.me

- `debrid/predb-me` | qualifies | evidence documented | binding none | category scene pre-release database (public, no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://predb.me/
- price USD 0
- free tier: A public, unauthenticated feed of scene release names with relative timestamps ('5 mins', '6 mins'), newest first. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No account, query cap or price appears on the page served.
- per-object cap: not applicable: names and timestamps, not bytes | source: [1]
- retention: not stated; the front page lists only the most recent releases | source: [1]
- egress: Nothing is downloadable: the site publishes release names and times, not files. | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: No account on the page served.
- interface: unknown
- limits:
  - request-rate: unstated; the origin answered a plain read with HTTP 403 and the content still rendered [1]
- binding note: A name index transfers nothing, so no byte constraint binds.
- interface detail: A web listing. /about and /api both return nginx 404 on the origin, so no documented API exists at those paths.
- tooling: Browser only as read. A crawler can parse the front page; there is no documented API to call.
- composes with: The 'does this exist yet' layer: it answers whether a named release is real and how old it is, before a client spends a debrid pull on a search. Pairs with a torrent indexer (which release to fetch) or a DDL index (which post to look for).
- reliability: The origin returned HTTP 403 to the reader while still serving the listing through it, so a client that trusts status codes alone will record this site as blocked when it is not.
- notes: Release database (PreDB) tracking scene metadata and timestamps. The service does not host or transfer downloadable payloads.
- evidence note: The listing was read with releases minutes old. The 403-with-content behaviour is the same observation, and it is why the confidence note says 'served' rather than 'reachable'.
- extras:
  - api_paths_tried: /about and /api, both 404
  - upstream_status_on_success: 403
- evidence:
  - [1] 2026-10-23: the live release feed with '5 mins' / '6 mins' timestamps, and the upstream 403 that still returned content
  - [2] 2026-10-23: no documented API at /api: the origin returns '404 Not Found' from nginx
- sources:
  - [1] https://predb.me/
  - [2] https://predb.me/api
