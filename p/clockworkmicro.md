# Clockwork Micro

> clockworkmicro.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clockworkmicro/ | JSON https://fshy.ajam.dev/api/v1/entity/clockworkmicro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clockwork Micro

- `data-apis/clockwork-micro` | qualifies-with-caveat | evidence reported | binding volume-quota | category map tiles and US elevation API | tier Personal
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-11-17
- url https://www.clockworkmicro.com/pricing
- free tier: Personal plan, free: 50,000 API requests for the Elevation API and 50,000 tile requests for each of Basemap, Map Maker, Terrain Tiles and USGS Topo Maps, with 8¢ charged per additional 1,000 requests; the pricing page states no period for the Personal column (the paid columns are per month), and a third-party listing reads the quotas as monthly | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: the Standard plan is $25.00 a month for 100,000 API requests; whether the Personal plan can be billed for the overage, and so whether a card is asked, is unverified; the service is tiles and elevation, not a geocoder
- per-object cap: the Elevation API takes a single latitude and longitude pair or an array of up to 100 pairs in one query, for locations in the United States | source: [2]
- retention: unverified: no storage or caching rule for results or tiles was found | source: [3]
- egress: not applicable: requests, not bytes, are the metered unit | metered: no | source: [1]
- identity: email | detail: an account at clockworkmicro.com/register with a full name, email, password, company and country, plus the services of interest, the intended use case and the industry; the form has no card field
- interface: rest
- limits:
  - volume-quota (binding): 50,000 API requests (Elevation) and 50,000 tile requests for each tile service on the Personal plan, 8¢ per additional 1,000; the period is not stated on the pricing page [1]
  - per-object-cap: up to 100 latitude and longitude pairs in one elevation query [2]
  - request-rate: unverified: no rate limit was found on the pricing page, the service pages or the docs [3]
- binding note: the 50,000-request allowance is the only published limit
- interface detail: HTTPS microservices authorised with an x-api-key header or an OAuth 2 client-credentials access token exchanged from API credentials; tile endpoints addressed by z, x and y for basemap, terrain and USGS topo layers, and an Elevation API; the docs are at docs.clockworkmicro.com
- tooling: any HTTP client; a no-code Map Maker tool on the site
- composes with: 50,000 elevation lookups or tile requests per service on a free personal account whose form has no card field, with overage priced at 8¢ per 1,000: a US elevation API and a basemap for web maps, not a geocoder; the vendor does not state the free period
- reliability: unverified: no rate limit, uptime statement or terms page was found, and the free period is stated only by third-party listings
- notes: Free requests: 50,000 API requests and 50,000 tile requests per service on Personal, period not stated by the vendor. Rate limit: unverified. Bulk path: an elevation query of up to 100 pairs.
- evidence note: the pricing page, the register form, the service pages and the docs were quoted on 2026-11-02; the pricing page states no period for the Personal column, and the monthly reading comes from a third-party listing. The terms page and the account dashboard were not reachable, so the rate limit and the storage rule are unverified.
- extras:
  - free_requests: 50,000 API requests (Elevation) and 50,000 tile requests per tile service; period not stated by the vendor
  - rate_limit: unverified: none found
  - bulk_path: an elevation query of up to 100 latitude and longitude pairs; tiles by z, x and y
- evidence:
  - [1] 2026-11-02: the free Personal plan lists 50,000 API requests with 8¢ per additional 1,000 and no period | capture: sha256:9f2f5cd9d20eb601db94f59cdb808486156ce5cef43ed5699b1262becb0bf1d0 | quote: ## Personal Free 50,000 API requests 8¢ / additional 1,000 API requests
  - [1] 2026-11-02: the Personal plan lists 50,000 tile requests for each tile service | capture: sha256:9f2f5cd9d20eb601db94f59cdb808486156ce5cef43ed5699b1262becb0bf1d0 | quote: 50,000 tile requests
  - [1] 2026-11-02: the Standard plan is $25.00 a month for 100,000 API requests | capture: sha256:9f2f5cd9d20eb601db94f59cdb808486156ce5cef43ed5699b1262becb0bf1d0 | quote: ## Standard $25.00 / month 100,000 API requests
  - [4] 2026-11-02: a third-party listing reads the free quotas as monthly | capture: sha256:3924b30cbd446cc68da50174880751aba83b231109e0f3f3bb5d6437d8d73b52 | quote: This free tier includes meaningful monthly quotas across five services
  - [5] 2026-11-02: the register form asks for a full name, email, password, company and country | capture: sha256:6d1248db43aa2d7b69189b45c9884ec5626a22182d1ba9b91a367c718966d00f | quote: Full Name\* Email\* Password\* Company\* Country\*
  - [5] 2026-11-02: the register form asks for the intended use case | capture: sha256:6d1248db43aa2d7b69189b45c9884ec5626a22182d1ba9b91a367c718966d00f | quote: ### What is your intended use case?
  - [6] 2026-11-02: registering is free | capture: sha256:809a873a707191bd6db8bfce7098b3a3d09ac11e6748a4e043646129addad7aa | quote: [Register](https://www.clockworkmicro.com/register) for free to start using Map Maker and other services.
  - [2] 2026-11-02: an elevation query takes one pair or up to 100 pairs | capture: sha256:31d4f9c1f5b88a3551d827800007ca719624e07fc18dbed40ab044fafad18a98 | quote: A query may be either a single latitude and longitude pair or an array of up to 100 latitude and longitude pairs.
  - [2] 2026-11-02: the Elevation API covers locations in the United States | capture: sha256:31d4f9c1f5b88a3551d827800007ca719624e07fc18dbed40ab044fafad18a98 | quote: Clockwork Micro provides a simple, highly accurate US elevation API that allows users to query locations in the United States.
  - [7] 2026-11-02: the basemap is served as individual raster or vector tiles | capture: sha256:898d05a8bd79426698641688b29efcea7c2e6b90b85dc837b55d59fcd591c24d | quote: Alternatively, a software customer may request the individual tiles in either raster or vector format and incorporate them into another map.
  - [3] 2026-11-02: the tile API accepts an OAuth 2 client-credentials token or an x-api-key | capture: sha256:c96d435273d3b50b6b226a915027b6c07efaf34ecf049d19e5212dbbf4c98c06 | quote: oAuth2ClientCredentialsx-api-key
  - [3] 2026-11-02: tiles are addressed by z, x and y | capture: sha256:c96d435273d3b50b6b226a915027b6c07efaf34ecf049d19e5212dbbf4c98c06 | quote: | z required | integer Example: 14z coordinate of the tile |
  - [3] 2026-11-02:  | capture: sha256:c96d435273d3b50b6b226a915027b6c07efaf34ecf049d19e5212dbbf4c98c06
  - [8] 2026-11-02: API credentials are exchanged for an access token | capture: sha256:8f1e7300db97cac12b3da010dc87fa2655fe50805716de8df61f4dc7f526e29c | quote: Exchange your API credentials for an access token.
- sources:
  - [1] https://www.clockworkmicro.com/pricing
  - [2] https://www.clockworkmicro.com/services/elevation-api
  - [3] https://docs.clockworkmicro.com/v1.html
  - [4] https://freetier.co/directory/products/clockwork-micro
  - [5] https://www.clockworkmicro.com/register
  - [6] https://clockworkmicro.com/
  - [7] https://www.clockworkmicro.com/services/basemap
  - [8] https://www.clockworkmicro.com/help
