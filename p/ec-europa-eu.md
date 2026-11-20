# Eurostat web services

> ec.europa.eu | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ec-europa-eu/ | JSON https://fshy.ajam.dev/api/v1/entity/ec-europa-eu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Eurostat web services (SDMX 2.1 and Statistics API)

- `debrid/eurostat-api` | qualifies-with-caveat | evidence documented | binding request-rate | category official statistics API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://ec.europa.eu/eurostat/web/main/data/web-services
- price USD 0
- free tier: The whole Eurostat database is reachable through 'SDMX 2.1 web services' and the 'Eurostat statistics web services'; datasets are updated twice a day at 11:00 and 23:00 CET. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No key, account or allowance is mentioned on the web-services page.
- per-object cap: not applicable: JSON-stat, SDMX-ML or TSV per query. A single-series query measured 2,949 bytes; a whole dataset is a larger query, not a larger object. | source: [2]
- retention: 'The Eurostat database always contains the latest version of the datasets, meaning that there is no versioning or documentation of past versions of the data.' A revision overwrites. | source: [1]
- egress: Free and unmetered; no authentication at the transport level. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No key and no account: both queries returned 200 to an anonymous client.
- interface: rest, cli
- limits:
  - request-rate (binding): none published; two anonymous queries returned 200 here with no throttling headers probe:https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp
- limits note: The legacy bulk download listing is gone: https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/nama_10_gdp.tsv.gz returned 404 on 2026-10-23, so the only verified path is the per-query API.
- binding note: Each query returns kilobytes, so 1 TiB is millions of calls; with no published limit and no bulk file verified, the call rate decides the day's bytes.
- interface detail: GET https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/<dataset>?format=JSON&lang=EN&<dimension>=<value>, and the SDMX 2.1 endpoint /api/dissemination/sdmx/2.1/data/<dataset>.
- endpoint: part of interface detail
- tooling: curl/python-requests; eurostat and pandasdmx python packages; the query builder on the site generates the URL.
- composes with: The EU-level counterpart to World Bank indicators; the two overlap on national accounts and trade, so a reconciliation step needs both rather than either.
- reliability: No versioning: a revision replaces the number in place, so a client that re-runs a query a month later can silently get different data for the same period.
- notes: Caveat is bulk: the service is unlimited and free but ships data in small JSON-stat responses, and the old bulk file endpoint is dead. A full Eurostat mirror is millions of queries, which is slow rather than blocked.
- evidence note: Two API responses were measured with byte counts and the web-services page was read. The bulk path is documented as unavailable here, not as a measured success.
- extras:
  - single_series_bytes: 2971
  - bulk_listing_status: 404
  - update_times_cet: 11:00; 23:00
- evidence:
  - [1] 2026-10-23: SDMX 2.1 and Statistics web services; 'no versioning or documentation of past versions'; twice-daily update at 11:00 and 23:00 CET
  - probe:https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?format=JSON&lang=EN&geo=DE&na_item=B1GQ&unit=CP_MEUR&time=2023 2026-10-23: 200, 2,971 bytes of application/json, anonymous
  - probe:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/nama_10_gdp.tsv.gz 2026-10-23: 404 - the legacy bulk TSV listing did not answer
- sources:
  - [1] https://ec.europa.eu/eurostat/web/main/data/web-services
  - [2] https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp
