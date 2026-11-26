# Knaben

> knaben.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/knaben/ | JSON https://fshy.ajam.dev/api/v1/entity/knaben.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Knaben

- `debrid/knaben` | qualifies | evidence documented | binding request-rate | category meta indexer over public trackers (JSON API, no key) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:50.792Z (live) | stale on 2026-12-26
- url https://knaben.org/api/v2/
- price USD 0
- free tier: No key and no account: GET https://api.knaben.org/v2/search?q=... returned hits with hash, magnetUrl, tracker, seeders and bytes. The docs publish no quota. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: results are metadata and magnets | source: [1]
- retention: the database keeps documents after they go dead; the docs say 1.7 million documents were seen in the last week and the 'dead' flag is opt-in | source: [1]
- egress: no byte allowance: the API returns JSON records and magnets | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: No key, no account, no captcha on the GET requests made today.
- interface: rest
- limits:
  - request-rate (binding): the operator published a temporary rate of 1 request per 2 seconds on 2026-08-12, after a record of 25 million requests in a single day; the v2 docs state 'Size of the response, maximum is 300'. The status page of 2026-09-29 reads 'Now set up new network routing. Let's see how this goes...' [1]
- limits note: v2 moved from POST to GET so the edge can cache the responses, which is a bandwidth measure. The operator published a temporary 1 request per 2 seconds limit on 2026-08-12 and later reported bandwidth maxed out; the 300-result ceiling remains in the v2 docs.
- binding note: The operator published a temporary 1 request per 2 seconds limit on 2026-08-12 and names bandwidth as the failure mode; no byte quota exists on this side.
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
  - [4] 2026-11-25: a published temporary limit of 1 request per 2 seconds and a 25 million request day | capture: sha256:1a9abab0871697375b32776e04414f85494a312440aace5c89031bb7b9c36e65 | quote: We have seen an intense increase of API traffic the last day, a new record of 25 million requests in a single day. Because of this, there is a temporary 1 request per 2 seconds limit.
  - [4] 2026-11-25: a published rate limit replaces the earlier undeclared rate | capture: sha256:1a9abab0871697375b32776e04414f85494a312440aace5c89031bb7b9c36e65 | quote: We have seen an intense increase of API traffic the last day, a new record of 25 million requests in a single day. Because of this, there is a temporary 1 request per 2 seconds limit.
  - [4] 2026-11-25: a published rate limit at this provider | capture: sha256:1a9abab0871697375b32776e04414f85494a312440aace5c89031bb7b9c36e65 | quote: We have seen an intense increase of API traffic the last day, a new record of 25 million requests in a single day. Because of this, there is a temporary 1 request per 2 seconds limit.
  - [4] 2026-11-25: the operator's published rate limit is unchanged | capture: sha256:1a9abab0871697375b32776e04414f85494a312440aace5c89031bb7b9c36e65 | quote: We have seen an intense increase of API traffic the last day, a new record of 25 million requests in a single day. Because of this, there is a temporary 1 request per 2 seconds limit.
  - [1] 2026-11-25: the GET endpoints and their parameters are unchanged | capture: sha256:131b083a151d2c8e950bbb83d2d6dda98433b69f8db714143a3cfa3a88a3a257 | quote: Use GET /v2/search or GET /v2/browse with these query parameters.
  - [2] 2026-11-25: the anonymous GET still returns hits with no key | capture: sha256:c61dcd355f0c800486992db79233065bafcb49b2c00012accc8192d5d77d797b | quote: "total":{"relation":"eq","value":61}
- sources:
  - [1] https://knaben.org/api/v2/
  - [2] https://api.knaben.org/v2/search?q=ubuntu&s=2
  - [3] https://knaben.org/api/v1/
  - [4] https://knaben.org/status/
