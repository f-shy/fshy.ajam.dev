# Proxmint GeoIP

> proxmint.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxmint/ | JSON https://fshy.ajam.dev/api/v1/entity/proxmint.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxmint GeoIP

- `data-apis/proxmint-geoip` | qualifies | evidence documented | binding request-rate | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.369Z (live) | stale on 2026-12-03
- url https://proxmint.com/tools/ip-lookup
- free tier: Keyless JSON lookup at proxmint.com/api/geoip: no API key, no sign-up, CORS open; no monthly or daily quota is stated, and the limit is 60 requests a minute per IP, then HTTP 429; MaxMind GeoLite2 data. | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: Measured on 2026-11-02: three bursts of 70 parallel lookups of distinct addresses all answered HTTP 200, and a fourth burst of 70 within 35 seconds answered 34 times HTTP 200 and 36 times HTTP 429.
- per-object cap: one address per request; the ip parameter takes a single public IPv4 or IPv6 address | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no key, no sign-up and no account for the lookup endpoint; an account exists only for the paid proxy service
- interface: rest
- limits:
  - request-rate (binding): 60 requests a minute per IP address, then HTTP 429 [1]
- binding note: No monthly or daily quota is stated, so the per-minute limit is the only published limit.
- interface detail: GET https://proxmint.com/api/geoip?ip=ADDRESS (IPv4 or IPv6; the caller's address when ip is omitted), JSON with ip, countryCode, countryName, city, region, lat, lon, tz, accuracyRadiusKm, asn and asnOrg; private and reserved addresses answer 400; OpenAPI 3.1 specification at /openapi.json
- endpoint: part of interface detail
- tooling: any HTTP client or a browser (CORS open)
- composes with: keyless country, city, ASN and time zone lookups from MaxMind GeoLite2 at a stated 60 a minute per address. Bulk path: none; the GeoLite2 data behind it is the route for large local jobs, last after every hosted route
- reliability: Answers carry cache-control public, s-maxage=86400, so a repeated lookup of one address can come from the CDN cache; the first HTTP 429 came only after about 210 lookups in 35 seconds, against a stated 60 a minute.
- notes: Free requests: no quota stated, keyless. Rate limit: 60 requests a minute per IP (HTTP 429); measured enforcement began later, after about 210 lookups in 35 seconds. The page carries the MaxMind GeoLite attribution notice. Bulk path: none.
- evidence note: The tool page and the OpenAPI specification were read on 2026-11-02, and a keyless lookup answered HTTP 200; the stated limit of 60 a minute is documented and the burst test shows it enforced later than stated, so the rung is documented rather than measured.
- extras:
  - bulk_path: none
  - free_requests: no stated quota; 60 a minute per IP
- evidence:
  - [1] 2026-11-02: the lookup endpoint needs no key and no sign-up and allows browser calls | capture: sha256:f4ce9206448877522921c7cebaee741108a68575b67a933d285d3b06f27a8507 | quote: The lookup above is a public JSON endpoint. No API key, no signup, and CORS is open, so it works from a browser as well as a server.
  - [1] 2026-11-02: the limit is 60 requests a minute per IP, then HTTP 429; private addresses answer 400 | capture: sha256:f4ce9206448877522921c7cebaee741108a68575b67a933d285d3b06f27a8507 | quote: Leave out `ip` to look up the address the request comes from. Private and reserved addresses get a 400. The limit is 60 requests a minute per IP, then 429.
  - [1] 2026-11-02:  | capture: sha256:f4ce9206448877522921c7cebaee741108a68575b67a933d285d3b06f27a8507 | quote: This product includes GeoLite Data created by MaxMind, available from [maxmind.com](https://www.maxmind.com/).
  - [2] 2026-11-02: lookups are resolved against a local GeoLite2 database | capture: sha256:da39f774ee8c372666df2daebe332abac24149eb768493793863a80285cc3f19 | quote: Resolved against a local MaxMind GeoLite2 database
  - [2] 2026-11-02: the geolocation endpoint is open, key-free and rate limited per IP | capture: sha256:da39f774ee8c372666df2daebe332abac24149eb768493793863a80285cc3f19 | quote: The free proxy list and IP geolocation are open and key-free: rate limited per IP
  - [2] 2026-11-02: the ip parameter takes one public IPv4 or IPv6 address | capture: sha256:da39f774ee8c372666df2daebe332abac24149eb768493793863a80285cc3f19 | quote: Any public IPv4 or IPv6 address. Omit to look up the caller
  - [3] 2026-11-02: the free tools, the IP lookup among them, need no signup | capture: sha256:cb0aadb1c43293f5a12cd951080eebb3a92cbdf28252166a12096d774a7d87c0 | quote: Free proxy utilities — check your IP address and generate ready-to-paste proxy commands for curl, Python and Node. No signup required.
  - [4] 2026-11-02: an account is for the paid proxy service, billed by the gigabyte | capture: sha256:5da2b42e841329bc72660a2ae3a56404c4b176773b2082cabffeed10f84121b4 | quote: Free to join — you pay only for the GB you buy.
  - probe:https://proxmint.com/api/geoip?ip=8.8.8.8 2026-11-02: a keyless lookup of 8.8.8.8 answered HTTP 200 | capture: sha256:1b0e167145b76c95d2cbddbb1b675630aedd0cba5543dcc91c16da0721a44718 | quote: "status": 200
  - probe:https://proxmint.com/api/geoip?ip=8.8.8.8 2026-11-02: answers are cacheable at the CDN for 86400 seconds | capture: sha256:1b0e167145b76c95d2cbddbb1b675630aedd0cba5543dcc91c16da0721a44718 | quote: "cache-control": "public, s-maxage=86400, stale-while-revalidate=604800"
  - probe:https://proxmint.com/api/geoip?ip=8.8.8.8 2026-11-02: answers allow any browser origin | capture: sha256:1b0e167145b76c95d2cbddbb1b675630aedd0cba5543dcc91c16da0721a44718 | quote: "access-control-allow-origin": "*"
  - probe:https://proxmint.com/api/geoip?ip=8.8.8.8 2026-11-02: the keyless answer for 8.8.8.8 is country-level with a 1000 km accuracy radius and the ASN | capture: sha256:2e1381f9fd1cb632e0452d9ebbed832286fee50ec19af700e2fffe655fc0e3d7 | quote: {"ip":"8.8.8.8","countryCode":"us","countryName":"United States","city":null,"region":null,"lat":37.751,"lon":-97.822,"tz":"America/Chicago","accuracyRadiusKm":1000,"asn":15169,"asnOrg":"Google LLC"}
  - probe:https://proxmint.com/api/geoip?ip=4.4.4.1 2026-11-02: a first burst of 70 parallel lookups of distinct addresses all answered HTTP 200 | capture: sha256:ece247b312bcf549e8d81682fc1620956abab8e77814811dcdd9233e1dc80269 | quote: "status": 200
  - probe:https://proxmint.com/api/geoip?ip=4.4.5.1 2026-11-02: a second burst of 70 parallel lookups, about 29 seconds later, all answered HTTP 200 | capture: sha256:c6c0e4d8b2c483e319c1cdfdde724d5dd0c66c8715f4de8e7949953ff6869ab9 | quote: "status": 200
  - probe:https://proxmint.com/api/geoip?ip=4.4.5.1 2026-11-02: a third burst of 70 parallel lookups, about 3 seconds later, all answered HTTP 200 | capture: sha256:fce89a61cc15754573f1f7cc64cebda6d5fe132f1dd4b9555d587bcc11712c65 | quote: "status": 200
  - probe:https://proxmint.com/api/geoip?ip=4.4.5.1 2026-11-02: a fourth burst of 70 parallel lookups, about 2 seconds later, answered HTTP 429 for 36 of them and HTTP 200 for 34 | capture: sha256:998c795969a75c6e2139bcf3cbfef8ae435375f02ac1e9677c760ca0fc9cf5c6 | quote: "error": "http-429"
- sources:
  - [1] https://proxmint.com/tools/ip-lookup
  - [2] https://proxmint.com/openapi.json
  - [3] https://proxmint.com/tools
  - [4] https://proxmint.com/signup
