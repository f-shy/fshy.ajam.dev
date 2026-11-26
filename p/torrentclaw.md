# TorrentClaw

> torrentclaw.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torrentclaw/ | JSON https://fshy.ajam.dev/api/v1/entity/torrentclaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TorrentClaw

- `debrid/torrentclaw` | qualifies-with-caveat | evidence documented | binding request-rate | category torrent aggregator (JSON API, Torznab, RSS, Stremio addon) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:47:05.722Z (live) | stale on 2026-12-26
- url https://torrentclaw.com/
- price USD 0
- free tier: Anonymous reads work and are metered: x-ratelimit-limit: 10 and x-ratelimit-tier: anonymous on the search response, which returned total 8 for q=ubuntu. Magnet links, info hashes and torrent downloads require a free API key. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: index rows | source: [2]
- retention: not applicable to the caller: results are computed per request; the tracker's own stats are published at /api/v1/tracker-stats | source: [3]
- egress: no byte allowance on the API;.torrent files are proxied through cache services, and the swarm transfer is the user's | metered: no | free allowance: none published | source: [2]
- identity: email | detail: A free key is required before magnets, info hashes or .torrent downloads are returned: the response itself carries '_notice: Magnet links, info hashes, and torrent downloads require a free API key. Register at https://torrentclaw.com/register'.
- interface: rest
- limits:
  - request-rate (binding): 10 per window for the anonymous tier, returned in-band as x-ratelimit-limit: 10 with a reset stamp 42 to 60 s ahead of the request probe:torrentclaw.com/api/v1/search
- limits note: The llms.txt says limits are per endpoint and IP-based for anonymous traffic, key-based for authenticated traffic, and that a 429 carries Retry-After. The free key raises the quota and is what unlocks magnets.
- binding note: Ten requests per window is the hardest published number among debrid providers; at one search per title 1 TiB per month pull exhausts it on every batch, so the key is not optional in practice.
- interface detail: /api/v1/search, /api/v1/torrent/{infoHash}, /api/rss/{popular,recent,search}, /api/v1/torznab (Newznab/Torznab) and /api/stremio/manifest.json. An OpenAPI 3.1 spec sits at /api/openapi.json.
- endpoint: https://torrentclaw.com/api/v1/search?q=ubuntu&limit=3
- tooling: curl or any HTTP client; Sonarr/Radarr take the Torznab URL with a key; an MCP server is published as an npm package.
- composes with: Search for a title, take the hash with a key, ask the debrid provider for a cache hit, and let the Torznab endpoint serve the automation stack.
- reliability: The anonymous payload is metadata only, so a client that ignores the notice will spend its quota collecting rows it cannot act on; the aggregator also depends on the upstreams it names (YTS, EZTV, Knaben, Prowlarr, Bitmagnet, Torrentio, Torrents.csv and others).
- notes: The only index among debrid providers that publishes its anonymous quota in the response headers, which makes it the honest answer to 'what is the rate limit': 10 per window, and the object itself needs a free key. The caveat is precisely that split.
- evidence note: Three live searches were executed on 2026-10-23 and the rate headers read on each; the docs were read from llms.txt and llms-full.txt. Registering for a key confirms the free tier's real quota.
- extras:
  - ratelimit_limit: 10
  - ratelimit_tier: anonymous
  - openapi: https://torrentclaw.com/api/openapi.json
  - torznab: https://torrentclaw.com/api/v1/torznab
- evidence:
  - [1] 2026-10-23: HTTP 200 JSON with total 7 and a _notice that magnets and info hashes need a free API key
  - [3] 2026-10-23: the endpoint list, the anonymous/free/pro tiers, and that PRO unlocks Torznab, debrid integration and custom RSS
  - [4] 2026-10-23: limits are per endpoint and IP-based for anonymous traffic, 429 carries Retry-After, and the free key is enough for some endpoints while anonymous is rejected on others
  - [1] 2026-11-25: the anonymous search payload withholds magnets and info hashes until a free key is supplied | capture: sha256:63fdb99708ffb4af32cae9270d877d041751e0c2249bc8e4af7ee7c666a654a0 | quote: Magnet links, info hashes, and torrent downloads require a free API key. Register at https://torrentclaw.com/register
  - [1] 2026-11-25: magnets and info hashes are still withheld from anonymous searches | capture: sha256:63fdb99708ffb4af32cae9270d877d041751e0c2249bc8e4af7ee7c666a654a0 | quote: Magnet links, info hashes, and torrent downloads require a free API key. Register at https://torrentclaw.com/register
  - [1] 2026-11-25: the anonymous search response still reports a limit of 10 | capture: sha256:63fdb99708ffb4af32cae9270d877d041751e0c2249bc8e4af7ee7c666a654a0 | quote: x-ratelimit-limit: 10
  - [4] 2026-11-25: the rate-limit model in the documentation is unchanged | capture: sha256:fa2f091b237463799f723fac147c2fc7bdbb959af7e374b3ad4d8008ccbeacab | quote: - Rate limits: per-endpoint, IP-based for anonymous traffic, key-based for authenticated traffic.
  - [4] 2026-11-25: the documented API still returns 429 with Retry-After on rate limits | capture: sha256:fa2f091b237463799f723fac147c2fc7bdbb959af7e374b3ad4d8008ccbeacab | quote: Rate-limit responses use HTTP 429 with `Retry-After`. Authentication failures use HTTP 401 with `{ "error": "..." }`.
  - [5] 2026-11-25: the free key registration form asks for a name and an email address and no card | capture: sha256:d4df2fbf8cf9361364256e9f1408387ab3cd8dc4a13b1bcc94510bd3ec5ee057 | quote: Name Email Prefer not to share your real email? Use an alias from [SimpleLogin](https://simplelogin.io/), [addy.io](https://addy.io/), [DuckDuckGo](https://duckduckgo.com/email/).
- sources:
  - [1] https://torrentclaw.com/api/v1/search?q=ubuntu&limit=3
  - [2] https://torrentclaw.com/
  - [3] https://torrentclaw.com/llms.txt
  - [4] https://torrentclaw.com/llms-full.txt
  - [5] https://torrentclaw.com/register
