# Waymorphic Map

> waymorphic.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/waymorphic/ | JSON https://fshy.ajam.dev/api/v1/entity/waymorphic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Waymorphic Map

- `data-apis/waymorphic` | qualifies-with-caveat | evidence documented | binding request-rate | category map tiles, place search and reverse geocoding API with no key | tier Free, no key
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://waymorphic.com/
- free tier: no plan and no quota to keep under: OpenStreetMap vector tiles for the whole planet (zoom 0 to 14), five MapLibre styles, place search and reverse geocoding endpoints, with no API key, sign-up, token, domain allow-list or card; fair use applies, and bulk downloads and scraping the whole planet will be blocked | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: free means best effort: there is no contract or uptime guarantee; the OpenStreetMap attribution that the styles carry must stay in place
- per-object cap: one query a request for search and reverse; an empty tile is an HTTP 204; no batch endpoint is listed, and bulk downloads and scraping the whole planet will be blocked | source: [1]
- retention: unverified: no rule for storing search or reverse results is stated on the page | source: [1]
- egress: no usage tiers and no invoice; tiles are cached at the edge by a CDN and no byte metering is stated | metered: no | source: [1]
- identity: anonymous | detail: no sign-up, no key, no token, no domain allow-list and no card; keyless search and reverse calls answered HTTP 200
- interface: rest
- limits:
  - request-rate (binding): unverified: no numeric rate limit or quota is published; fair use applies and bulk downloads and whole-planet scraping will be blocked [1]
- binding note: no quota exists, so the blocking of bulk use under fair use is the only stated ceiling
- interface detail: HTTPS GET with CORS (Access-Control-Allow-Origin *): MapLibre style JSON at tiles.waymorphic.com/styles/{positron,bright,liberty,dark,fiord}, TileJSON at /planet, vector tiles at /planet/{version}/{z}/{x}/{y}.pbf, place search at /search?q=, address lookup at /reverse?lat=&lon=, and one place at /lookup/{id}; keyless search and reverse calls answered HTTP 200 with GeoJSON
- endpoint: https://tiles.waymorphic.com/search
- tooling: any HTTP client; MapLibre, Leaflet and QGIS read the tiles; an OpenAPI description of the tile endpoints is published
- composes with: keyless vector tiles, place search and reverse geocoding with no account, for prototypes and production maps; best effort with no contract or uptime guarantee, and no stated rule for storing results
- reliability: best effort on a small server and a global CDN with no contract or uptime guarantee; bulk downloads and whole-planet scraping will be blocked
- notes: Free requests: no quota; fair use applies. Rate limit: none published. The OpenStreetMap attribution must stay. Bulk path: none; bulk downloads and whole-planet scraping will be blocked.
- evidence note: the home page, which also serves as the API reference, was quoted on 2026-11-02, and keyless search and reverse calls answered HTTP 200 with GeoJSON. The request volume at which fair use blocks was not tested, and no storage rule for results is stated.
- extras:
  - free_requests: no quota and no plan; fair use
  - rate_limit: unverified: no numeric limit is published
  - bulk_path: none: bulk downloads and scraping the whole planet are blocked
- evidence:
  - [1] 2026-11-02: planet-wide OpenStreetMap vector tiles with no API key, usage tiers or invoice | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: OpenStreetMap vector tiles for the whole planet, in five ready-made MapLibre styles, from a global CDN. No API key, no usage tiers, no invoice.
  - [1] 2026-11-02: no sign-up, token, domain allow-list or card | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: No sign-up, no token, no domain allow-list, no card on file. Copy a URL and it works, in a prototype or in production.
  - [1] 2026-11-02: the tiles cover the whole planet from zoom 0 to 14 | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: No sign-up. No card. Whole planet, zoom 0 to 14.
  - [1] 2026-11-02: there is no plan and no quota | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: There is no plan to choose and no quota to keep under.
  - [1] 2026-11-02: bulk downloads and scraping the whole planet will be blocked | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: Bulk downloads and scraping the whole planet are not what it is for, and they will be blocked.
  - [1] 2026-11-02: the service is best effort with no contract or uptime guarantee | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: It is fast and stable, but there is no contract or uptime guarantee behind it.
  - [1] 2026-11-02: the attribution carried by the styles must stay | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: Keep the attribution. The styles carry the credits that OpenStreetMap's licence requires, plus a link back here.
  - [1] 2026-11-02: the search endpoint returns places, streets, addresses, postcodes and points of interest as GeoJSON | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: Search: places, streets, addresses, postcodes and points of interest, as GeoJSON, best match first.
  - [1] 2026-11-02: the reverse endpoint returns the nearest address at a coordinate | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: Address lookup: the nearest address at a coordinate, with its postcode, city, state and country;
  - [1] 2026-11-02: vector tiles are served at a versioned planet path | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: https://tiles.waymorphic.com/planet/{version}/{z}/{x}/{y}.pbf
  - [1] 2026-11-02: an empty tile answers HTTP 204 | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: An empty tile (sea, outside the extract) is a 204.
  - [1] 2026-11-02: every endpoint sends a CORS header | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: Every endpoint answers with `Access-Control-Allow-Origin: *`.
  - [1] 2026-11-02: an OpenAPI description of the tile endpoints is published | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: The OpenAPI description is at https://waymorphic.com/openapi/tiles.json.
  - [1] 2026-11-02: no accounts, cookies or analytics on the tiles, with short-lived access logs | capture: sha256:e8993b683d547d3cbb1771018f98655e30727b8b4df1bd1c4a199dca91caf437 | quote: No tracking. No accounts, no cookies, no analytics on the tiles. The tile server keeps ordinary access logs for a short while to run the service, and nothing else.
  - probe:https://tiles.waymorphic.com/search?q=Zurich 2026-11-02: a keyless place search answers HTTP 200 | capture: sha256:36966c0eb5998a99a1847a64459f2d133600672940ca57794136ca53b9689d7f | quote: "status": 200
  - probe:https://tiles.waymorphic.com/search?q=Zurich#body 2026-11-02: the keyless search returns a GeoJSON place for Zurich | capture: sha256:7319cb4dad79a19995b7e3db53f2521253ac5585a26076cd9c21d479ea16b6c3 | quote: "label":"Zürich, Switzerland"
  - probe:https://tiles.waymorphic.com/reverse?lat=47.3769&lon=8.5417 2026-11-02: a keyless reverse lookup answers HTTP 200 | capture: sha256:8b7b4d9e0896251d18dfcb823e8f878afc39a3d0752c6e51986f91999a31752b | quote: "status": 200
  - probe:https://tiles.waymorphic.com/reverse?lat=47.3769&lon=8.5417#body 2026-11-02: the keyless reverse lookup returns the nearest street for the coordinate | capture: sha256:bedf55609bd8bea1230c5349d8e357979811e22c9b9476baca431628aad983f2 | quote: "name":"Bahnhofquai"
- sources:
  - [1] https://waymorphic.com/
