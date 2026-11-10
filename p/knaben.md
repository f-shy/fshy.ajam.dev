# Knaben

> knaben.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/knaben/ | JSON https://fshy.ajam.dev/api/v1/entity/knaben.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Knaben

- `debrid/knaben` | qualifies | evidence documented | binding request-rate | category meta indexer over public trackers (JSON API, no key) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://knaben.org/api/v2/
- price USD 0
- free tier: No key and no account: GET https://api.knaben.org/v2/search?q=... returned hits with hash, magnetUrl, tracker, seeders and bytes. The docs publish no quota. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: results are metadata and magnets | source: [1]
- retention: the database keeps documents after they go dead; the docs say 1.7 million documents were seen in the last week and the 'dead' flag is opt-in | source: [1]
- egress: no byte allowance: the API returns JSON records and magnets | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No key, no account, no captcha on the GET requests made today.
- interface: rest
- limits:
  - request-rate (binding): no number published; the v2 docs justify the rewrite with 'we've been struggling to serve the amount of bandwidth from the server to all the API clients' and close with 'if you alone are the main reason the server CPU sits at 100%, I will hunt you down'. Measured: 10 sequential GETs over about 24 s all 200, and 6 concurrent GETs all 200 [1]
- limits note: v2 moved from POST to GET so the edge can cache the responses, which is a bandwidth measure rather than a per-client quota. The 300-result ceiling is the only hard number, and six concurrent requests drew no 429.
- binding note: The operator names CPU and bandwidth as the failure mode and refuses to publish a number, so voluntary restraint is the only limit; no byte quota exists on this side.
- interface detail: GET /v2/search and GET /v2/browse with query parameters (q, sf, c, t, o, d, s, f, xxx, unsafe, dead, seen); size maximum 300. v1 still exists as POST /v1 with a JSON body. There is also an RSS page at knaben.org/rss/.
- endpoint: https://api.knaben.org/v2/search?q=ubuntu&s=2
- tooling: One GET. Sonarr/Radarr-style clients reach it through Torznab proxies; TorrentClaw lists Knaben as one of its sources, so the API is already the feed behind another index.
- composes with: Query by title, take the magnetUrl or hash, hand the hash to a debrid service's cache check, and only fetch the ones that come back cached.
- reliability: Bandwidth pressure is stated by the operator, and the API answers are edge-cached (Cache-Control public with s-maxage 300), so a stale page can show a torrent that has since gone dead.
- notes: The best machine-readable torrent feed in the sector that needs nothing: no key, documented parameters, 300 results per call, and a magnet in every hit that carries a hash. Its weakness is exactly the thing the sector asks about: the vendor publishes no rate, only a threat.
- evidence note: Both doc pages and a live v2 response were read on 2026-10-23. A sustained poll with recorded statuses would raise the rate row to measured.
- extras:
  - max_results: 300
  - protocol: rest-json
  - auth: none
  - cache_s_maxage: 300
- evidence:
  - [1] 2026-10-23: the full parameter table, the 300-result maximum, the bandwidth rationale and the 'server CPU sits at 100%' warning
  - [2] 2026-10-23: HTTP 200 JSON with hits containing hash, magnetUrl, tracker, seeders, bytes and virusDetection, with no key
  - [3] 2026-10-23: v1 is a POST/GET endpoint with the same fields and the same warning, and states the DB holds 1.7 million documents seen in the last week
- sources:
  - [1] https://knaben.org/api/v2/
  - [2] https://api.knaben.org/v2/search?q=ubuntu&s=2
  - [3] https://knaben.org/api/v1/
