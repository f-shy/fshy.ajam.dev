# APIBay

> apibay.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apibay/ | JSON https://fshy.ajam.dev/api/v1/entity/apibay.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## APIBay (The Pirate Bay JSON API)

- `debrid/apibay` | qualifies | evidence documented | binding request-rate | category torrent index API (The Pirate Bay, JSON, no key) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://apibay.org/
- price USD 0
- free tier: No key and no account: GET /q.php?q=ubuntu&cat=0 returned 27,772 bytes of JSON with id, name, info_hash, seeders, leechers, size and category for every hit. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: index results | source: [2]
- retention: the index keeps the row after the swarm dies; seeders and leechers are the only liveness signal in the record | source: [2]
- egress: no byte allowance: JSON only; the transfer is between the user and the swarm | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No key, no account, no captcha. The site's own 'robot check' overlays are ad furniture, not an API gate.
- interface: rest
- limits:
  - request-rate (binding): none published; 10 status-checked requests plus 10 more over 55 s all returned 200, with no 429 and no Retry-After probe:apibay.org/q.php
- limits note: robots.txt on apibay.org carries only Cloudflare content signals and no crawl delay. The 7,200-second cache means repeated identical queries cost the origin nothing.
- binding note: No byte quota exists on an index; the only constraint is the rate at which titles are enumerated, and it tolerated about 0.2 req/s with no throttle.
- interface detail: GET /q.php?q=<query>&cat=<n> returns a JSON array; every row carries info_hash so a magnet is one string concatenation away. Responses are front-cached (Cache-Control max-age=7200).
- endpoint: https://apibay.org/q.php?q=ubuntu&cat=0
- tooling: One GET and a json parse; the whole site is a thin client over this API, so a scraper of the HTML is pointless.
- composes with: Search by title, build the magnet from info_hash, then ask a debrid service for a cache hit before pulling anything.
- reliability: The API is served through Cloudflare with a two-hour cache, so a query can answer from cache after the swarm has gone; single-file rows report num_files 1 and a size in bytes, which is enough to filter but not to confirm the file still exists.
- notes: The cleanest no-account JSON torrent feed found: a single GET, a fixed schema, and an info hash in every row. Its political fragility is the risk, not its quota: the domain is one seizure away from gone.
- evidence note: A live query was executed and its JSON read on 2026-10-23. A recorded probe over an hour would raise the rate row to measured.
- extras:
  - cache_max_age_s: 7200
  - fields: id,name,info_hash,leechers,seeders,size,num_files,username,added,status,category,imdb
- evidence:
  - [1] 2026-10-23: HTTP 200 application/json, 27,772 bytes, rows with info_hash, seeders, leechers, size in bytes and category id
  - [3] 2026-10-23: content-signal text only, with no crawl delay and no rate limit stated
- sources:
  - [1] https://apibay.org/q.php?q=ubuntu&cat=0
  - [2] https://apibay.org/
  - [3] https://apibay.org/robots.txt
