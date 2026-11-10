# DB-IP

> db-ip.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/db-ip/ | JSON https://fshy.ajam.dev/api/v1/entity/db-ip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DB-IP

- `data-apis/db-ip` | qualifies | evidence documented | binding volume-quota | category IP geolocation API and database download | tier Free API and Lite databases
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://db-ip.com/db/download/ip-to-city-lite
- free tier: Free API: IP to country, state and city, limited to 500 requests a day with no key; IP to City Lite, IP to Country Lite and IP to ASN Lite databases as monthly CSV and MMDB downloads with no account | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the Lite downloads are not metered; the City Lite release of October 2026 has 7,786,864 records against 40,982,099 in the paid IP to Location database
- per-object cap: the October 2026 City Lite CSV is listed at 660.7 MB and is served as an 85,827,400-byte gzip; the MMDB is listed at 121.1 MB | bytes: 85827400 | source: [2]
- retention: source: [2]
- egress: not applicable | metered: no | source: [2]
- identity: anonymous | detail: no account and no key for the free API or the Lite downloads; the download page asks only to accept the licensing terms
- interface: rest
- limits:
  - volume-quota (binding): 500 free API requests a day [1]
- binding note: the API meter of 500 a day is the only limit; the Lite files are unmetered but monthly and less accurate than the paid data
- interface detail: free API: GET api.db-ip.com/v2/free/{ip} with no key, JSON; Lite files at download.db-ip.com/free/dbip-{city,country,asn}-lite-YYYY-MM.{csv,mmdb}.gz, served with no account and honouring HTTP range requests
- endpoint: https://api.db-ip.com/v2/free/
- tooling: any HTTP client; any MMDB reader for the MMDB files
- composes with: anonymous on both paths: the monthly City Lite file serves unmetered local lookups and the free API covers 500 remote lookups a day; DB-IP Lite is also redistributed by the ip-location-db project on GitHub. Bulk path: the monthly Lite downloads
- reliability: Lite data is updated monthly and has reduced coverage and accuracy (accuracy index 77 against 96 for the paid database)
- notes: Free requests: 500 API requests a day, no key; Lite downloads unmetered. Rate limit: none published beyond the daily count. Bulk path: monthly IP to City Lite, IP to Country Lite and IP to ASN Lite downloads (CSV, MMDB), no account.
- evidence note: the free API page and the Lite download pages were quoted on 2026-10-30; a keyless API lookup answered HTTP 200 with city data and a ranged read of the City Lite CSV answered HTTP 206 with no account. The 500-a-day API meter was not exhausted to observe it.
- extras:
  - bulk_path: monthly City, Country and ASN Lite downloads (CSV, MMDB) from download.db-ip.com, no account
  - free_requests: 500 API requests a day
- evidence:
  - [1] 2026-10-30: the free API maps IP to country, state and city and is limited to 500 requests a day | capture: sha256:28e08eab2dd1822453d3ac3aacb858ad12f06890de1969a79aed5ffe8aa51332 | quote: The Free API is a fast and easy way to implement IP geolocation in a prototype or small website. It provides a simple IP to country, state and city mapping and is limited to 500 daily requests.
  - [1] 2026-10-30: the free API endpoint | capture: sha256:28e08eab2dd1822453d3ac3aacb858ad12f06890de1969a79aed5ffe8aa51332 | quote: ~# curl http://api.db-ip.com/v2/free/8.8.8.8
  - [2] 2026-10-30: City Lite is monthly, CSV and MMDB | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: Our IP to City Lite database is updated monthly and available in CSV and MMDB formats.
  - [2] 2026-10-30:  | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a
  - [2] 2026-10-30: a web application links back to DB-IP.com | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: In the case of a web application, you must include a link back to DB-IP.com on pages that display or use results from the database.
  - [2] 2026-10-30: the City Lite CSV is listed at 660.7 MB | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: 660.7 MB
  - [2] 2026-10-30: the City Lite MMDB is listed at 121.1 MB | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: 121.1 MB
  - [2] 2026-10-30: the City Lite download URL | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: [Download IP to City Lite CSV](https://download.db-ip.com/free/dbip-city-lite-2026-10.csv.gz)
  - [2] 2026-10-30: the paid database has 40,982,099 records and accuracy index 96 | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: | IP to Location | 40,982,099 | 96 | October 30th 2026 |
  - [2] 2026-10-30: City Lite has 7,786,864 records and accuracy index 77 | capture: sha256:236a0d0f0addc7ec08e8777c51eae7f72a4afec38e80de95188065829039a65a | quote: | IP to City Lite | 7,786,864 | 77 | October 1st 2026 |
  - [3] 2026-10-30: all Lite downloads are monthly | capture: sha256:5277f0289579df96b37557158c96ce61215eb6e602ce2f24b7274324fee9b99e | quote: Lite downloads are updated monthly and distributed.
  - [3] 2026-10-30: an ASN Lite database is offered too | capture: sha256:5277f0289579df96b37557158c96ce61215eb6e602ce2f24b7274324fee9b99e | quote: | [IP to ASN Lite](https://db-ip.com/db/download/ip-to-asn-lite) | CSV, MMDB | October 2026 |
  - probe:https://api.db-ip.com/v2/free/8.8.8.8 2026-10-30: the free API answered a keyless request with city data | capture: sha256:85f8c759003fff40e957144d2f83439ba8cd0bc86047c4a2999551cc2d03cddb | quote: "city": "Mountain View"
  - probe:https://download.db-ip.com/free/dbip-city-lite-2026-10.csv.gz 2026-10-31: the City Lite CSV gzip is 85,827,400 bytes and downloads with no account | capture: sha256:c7ef3b3742bd6bc55483ac4318175d9b2d9c15ca56a10c0a6b9b7236ec58d054 | quote: "content-range": "bytes 0-1023/85827400"
- sources:
  - [1] https://db-ip.com/api/free
  - [2] https://db-ip.com/db/download/ip-to-city-lite
  - [3] https://db-ip.com/db/lite.php
