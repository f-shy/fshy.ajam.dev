# Nominatim

> osmfoundation.org | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osmfoundation/ | JSON https://fshy.ajam.dev/api/v1/entity/osmfoundation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nominatim (OpenStreetMap Foundation public instance)

- `data-apis/nominatim` | qualifies-with-caveat | evidence documented | binding request-rate | category geocoding API | tier public instance at nominatim.openstreetmap.org
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:48:53.808Z (live) | stale on 2026-12-01
- url https://operations.osmfoundation.org/policies/nominatim/
- free tier: no request count and no key: an absolute maximum of 1 request per second per application, summed over all its users; a script running longer than a day or at regular intervals is held to 4 requests per minute, from a single thread on one machine | unit: requests | metered on: none | read on: 2026-10-30 | source: [1] | note: a rate ceiling, not a metered quota; the service runs on donated servers with a very limited capacity, and the policy may change without notice
- per-object cap: one query per request, returning at most 40 results | source: [2]
- retention: source: [1] | note: the answer carries the licence line "Data © OpenStreetMap contributors"
- egress: not applicable: a query API, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no account and no key; each request carries a valid HTTP Referer or a User-Agent that identifies the application, since stock library User-Agents are refused by the policy
- interface: rest
- limits:
  - request-rate (binding): 1 request per second at most, summed over every user of an application [1]
  - request-rate (binding): 4 requests per minute for a script that runs longer than a day or at regular intervals; one thread on one machine [1]
  - per-object-cap: at most 40 results for one search [2]
- limits note: auto-complete search, systematic queries (reverse queries in a grid, complete lists of postcodes or towns, all POIs in an area) and scraping of the details page are banned outright
- binding note: there is no counted quota, so the 1 request per second ceiling, and 4 per minute for a long-running script, is the whole capacity
- interface detail: HTTPS GET to nominatim.openstreetmap.org/search (and /reverse, /lookup) with format=json, jsonv2, geojson, geocodejson or xml; no key; a valid HTTP Referer or an application User-Agent is required; without a format parameter the public instance answers with the web page
- endpoint: https://nominatim.openstreetmap.org/search
- tooling: any HTTP client that sets an identifying User-Agent or Referer; the policy asks apps to go through a caching proxy
- composes with: a keyless geocoder for low-volume, user-triggered lookups at 1 request a second; a stored data set of more than a few thousand addresses goes to a keyed provider with storable results (data-apis/geoapify, data-apis/opencage, data-apis/maptiler). Bulk path: no bulk geocoding (systematic queries are banned); the raw data is the weekly OSM planet file (89 GB PBF) or a regional extract. The last resort is self-hosted: the Nominatim software, which the user installs and runs on a rented machine with an imported planet or extract
- reliability: a requester that sends the same query repeatedly may be classed as faulty and blocked, a banned use (auto-complete, systematic queries, scraping of the details page) leads to a ban, and access can be withdrawn when the definition of heavy use changes
- notes: The hosted public instance of the Nominatim software. Bulk path: no bulk geocoding on the public instance; the raw data is the weekly OSM planet file or an extract.
- evidence note: the rate ceiling is documented and was not exercised.
- self hosted: no
- extras:
  - bulk_path: no bulk geocoding; raw OSM data from the weekly planet file (89 GB PBF) or regional extracts
- evidence:
  - [1] 2026-10-30: the public instance allows at most 1 request per second | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - No heavy uses (an absolute maximum of 1 request per second).
  - [1] 2026-10-30: a valid Referer or an identifying User-Agent is required | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agents as set by http libraries will not do).
  - [1] 2026-10-30: the limit applies per application, summed over its users | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: Note that the usage limits above apply per website/application: the sum of traffic by all your users should not exceed the limits.
  - [1] 2026-10-30: long-running or periodic scripts are held to 4 requests per minute | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - Scripts running longer than a day and scripts that are run at regular intervals are restricted to 4 requests per minute.
  - [1] 2026-10-30: bulk requests are limited to a single thread | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - limit your requests to a single thread
  - [1] 2026-10-30: bulk results must be cached, and repeated identical queries can be blocked | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - Results must be cached on your side. Clients sending repeatedly the same query may be classified as faulty and blocked.
  - [1] 2026-10-30: systematic queries are banned and complete data sets come from the planet file | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: If you need complete sets of data, get it from the [OSM planet](https://planet.openstreetmap.org/) or an extract.
  - [1] 2026-10-30: auto-complete search on the public instance is banned | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: - Auto-complete search This is not yet supported by Nominatim and you must not implement such a service on the client side using the API.
  - [1] 2026-10-30: access can be withdrawn when the definition of heavy use changes | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: In particular, the definition of heavy use may need to be modified in the future and you might have your access withdrawn.
  - [1] 2026-10-30: the service runs on donated servers with very limited capacity | capture: sha256:8ae65e6264a9e78441e9be396259b6ab3083ce4fddbb7432a19b9e34d8693b67 | quote: However, be aware that the service runs on donated servers and has a very limited capacity.
  - [2] 2026-10-30: one search returns at most 40 results | capture: sha256:214dd5c72684d07754f3c545dbc600fbee2dc29e97e97a840905e8eb9b53f0a5 | quote: Limit the maximum number of returned results. Cannot be more than 40.
  - [2] 2026-10-30: the output formats offered | capture: sha256:214dd5c72684d07754f3c545dbc600fbee2dc29e97e97a840905e8eb9b53f0a5 | quote: | format | one of: `xml`, `json`, `jsonv2`, `geojson`, `geocodejson` | `jsonv2` |
  - [3] 2026-10-30:  | capture: sha256:8bbe1273acdc20549fd92172881e75be80bd197cf6a5cc63b4c1f3b008da0b18 | quote: You are free to copy, distribute, transmit and adapt our data, as long as you credit OpenStreetMap and its contributors.
  - [4] 2026-10-30: the weekly planet PBF file is 89 GB | capture: sha256:6e07677e9bbfe0e773a21b54f53d19b17433ae56ccd0a84a3d0c0627299e3e58 | quote: 89 GB, created 21 hours ago.
  - [4] 2026-10-30: a complete copy of OSM data is published every week | capture: sha256:6e07677e9bbfe0e773a21b54f53d19b17433ae56ccd0a84a3d0c0627299e3e58 | quote: Each week, a new and complete copy of all data in OpenStreetMap is made available as both a compressed XML file and a custom PBF format file.
  - [5] 2026-10-30: the Nominatim software can be installed by the user; a full planet import takes days | capture: sha256:28ae966d339f7d0f1f4e30110c4362cf95a72640c13088f14f5b131a134f809d | quote: Even on a well configured machine the import of a full planet takes around 2.5 days.
  - probe:https://nominatim.openstreetmap.org/search?q=Zurich 2026-10-30: an anonymous search with no key answered HTTP 200 | capture: sha256:20f292556dd2cb145d0ae96602656d9cd60f7eab3a2c749f21d7d724990710cb | quote: "status": 200
  - probe:https://nominatim.openstreetmap.org/search 2026-10-30: the anonymous answer is a real geocode with coordinates | capture: sha256:39b28164fb94d386cdc64f6af470d1d1c9c99570fdcee67df1bf7200d4a57d2c | quote: "lat":"47.3744489","lon":"8.5410422"
- sources:
  - [1] https://operations.osmfoundation.org/policies/nominatim/
  - [2] https://nominatim.org/release-docs/latest/api/Search/
  - [3] https://www.openstreetmap.org/copyright
  - [4] https://planet.openstreetmap.org/
  - [5] https://nominatim.org/release-docs/latest/admin/Installation/
