# ip-location-db

> github.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-sapics/ | JSON https://fshy.ajam.dev/api/v1/entity/github-sapics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ip-location-db (sapics, GitHub)

- `data-apis/ip-location-db` | qualifies | evidence documented | binding none | category IP geolocation database download | tier GitHub releases
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://github.com/sapics/ip-location-db
- free tier: IP to country, city and ASN databases in CSV and MMDB from GitHub Releases with no account: its own user-country, server-country and origin-asn files, updated daily, plus redistributed DB-IP Lite (monthly), GeoLite2 (twice weekly) and IPtoASN data | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: user-country-ipv4.csv is 9,146,819 bytes | bytes: 9146819 | source: [1]
- retention: source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no account; public GitHub release downloads
- interface: rest
- binding note: static files with no published download limit
- interface detail: HTTPS downloads from github.com/sapics/ip-location-db/releases/download/latest/{file}, redirected to GitHub release-asset storage, with SHA-256 checksum files in a checksum release
- endpoint: https://github.com/sapics/ip-location-db/releases/download/latest/
- tooling: curl or wget, any CSV tool, any MMDB reader
- composes with: the one free route to city-level and country-level IP data with no account at all, pulled from GitHub on a schedule; Bulk path: GitHub release downloads
- reliability: the release URLs changed on 2026-06-18; the city data is redistributed DB-IP Lite and GeoLite2, as accurate as those sources
- notes: Free requests: unmetered (static files). Rate limit: none published. Bulk path: GitHub release downloads (CSV, MMDB).
- evidence note: the repository README was quoted on 2026-10-30 and a ranged read of user-country-ipv4.csv from the latest release answered HTTP 206 with no account on 2026-10-31.
- extras:
  - bulk_path: GitHub release downloads of country, city and ASN files
  - free_requests: unmetered
- evidence:
  - [1] 2026-10-30: country, city and ASN databases in CSV and MMDB | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb | quote: This project provides IP to location databases in CSV and MMDB formats since 2019.
  - [1] 2026-10-30:  | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb
  - [1] 2026-10-30: the original databases update daily | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb | quote: Original Databases [Update: Daily]
  - [1] 2026-10-30: city data comes from DB-IP Lite | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb
  - [1] 2026-10-30: release assets have SHA-256 checksum files | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb | quote: SHA-256 checksum files for all release assets are available in the
  - [1] 2026-10-30: the release URLs changed on 2026-06-18 | capture: sha256:5c73b90d697e2b96508510199fcfffefe96d9ba8bbb211c73d3ada9ddb4b42bb | quote: As of June 18, 2026, we have revised our distribution method for
  - probe:https://github.com/sapics/ip-location-db/releases/download/latest/user-country-ipv4.csv 2026-10-31: user-country-ipv4.csv is 9,146,819 bytes and downloads with no account | capture: sha256:00aa62b8ed5caf110e5de7fd0f733b91f58fba4a31c63544fb60a0eb5917a2b0 | quote: "content-range": "bytes 0-1023/9146819"
- sources:
  - [1] https://github.com/sapics/ip-location-db
