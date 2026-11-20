# EZTV

> eztv.re | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eztv/ | JSON https://fshy.ajam.dev/api/v1/entity/eztv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EZTV

- `debrid/eztv` | qualifies | evidence documented | binding request-rate | category torrent index, TV only (JSON API with magnets) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://eztv.re/
- price USD 0
- free tier: No key and no account: /api/get-torrents?limit=3 returned JSON reporting torrents_count 1,095,199 with magnet_url and filename per row. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: index rows | source: [2]
- retention: the API returns the catalogue history, so old episodes stay listed after the swarm empties | source: [1]
- egress: no byte allowance: JSON and magnets only | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No key and no account on the API call made today.
- interface: rest
- limits:
  - request-rate (binding): none published; the call answered immediately with Cache-Control no-store, so nothing suggests an edge cache is absorbing repeats [1]
- limits note: No rate headers were returned on the call made. The API is undocumented beyond community use, so the schema is the risk rather than the quota.
- binding note: An index has no byte quota; the request rate is the only lever, and the page parameter lets a client pace a backfill deliberately.
- interface detail: GET /api/get-torrents with limit and page parameters returns JSON. Also /api/get-torrent?limit=... per-page variants and an HTML front end.
- endpoint: https://eztv.re/api/get-torrents?limit=3
- tooling: One GET; the magnet_url field means no torrent file fetch is needed.
- composes with: Pull the recent page once a day, filter by show, and hand the magnet to a debrid service; the API's page parameter is the cursor for a backfill.
- reliability: The magnet dn strings carry a different domain ('[EZTVx.to]') from the host that answered (eztv.re), so a client that whitelists one will meet the other. Cache-Control is no-store, so repeats reach the origin.
- notes: The largest no-account magnet feed measured here by row count (1.09 million), and the narrowest by subject. It pairs with the DDL feeds badly (TV only) and with Torrentio well, because Torrentio already indexes it.
- evidence note: The API was called on 2026-10-23 and the JSON read. A recorded backfill would raise it to measured and would show whether page depth is capped.
- extras:
  - torrents_count: 1095199
  - protocol: rest-json
  - subject: tv
- evidence:
  - [1] 2026-10-23: HTTP 200 JSON with torrents_count 1,095,199, limit 3, page 1, and rows carrying magnet_url with dn and multiple udp trackers
  - [1] 2026-10-23: response header Cache-Control: no-store, so repeats reach the origin rather than an edge cache
- sources:
  - [1] https://eztv.re/api/get-torrents?limit=3
  - [2] https://eztv.re/
