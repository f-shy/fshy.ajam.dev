# IP2Location LITE

> ip2location.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip2location/ | JSON https://fshy.ajam.dev/api/v1/entity/ip2location.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP2Location LITE

- `data-apis/ip2location-lite` | qualifies | evidence documented | binding pull-count | category IP geolocation database download | tier LITE
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.114Z (live) | stale on 2026-12-04
- url https://www.ip2location.com/database/lite
- free tier: one free account unlocks the IP2Location LITE (up to DB11: country, region, city, latitude, longitude, ZIP code, time zone), IP2Proxy LITE and ASN LITE databases, updated monthly, in BIN, CSV and MMDB | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1] | note: local lookups are not metered; the download itself is expected once a month
- per-object cap: DB11 LITE IPv4: BIN 92.26 MB, CSV 328.53 MB (2,965,251 rows), MMDB 85.25 MB; IPv6: BIN 220.36 MB, CSV 855.89 MB; current version 01 November 2026 | source: [2] | note: unverified: behind a sign-up: the byte size of each file served by a token download
- retention: source: [3]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an IP2Location account: name, email address, a password of 8 or more characters with a confirmation field and a required agreement checkbox, or Google or GitHub sign-up
- interface: rest
- limits:
  - pull-count (binding): download once a month, on a random day in the first week; accounts with massive downloads or shared accounts are disabled [3]
- binding note: lookups are local and unmetered, so the only constraint is the monthly download rhythm and the account-disable rule on massive downloads
- interface detail: HTTPS file download with the account's download token, through the IP2Location download client (download.pl -package DB11LITE -token TOKEN) or wget and curl
- tooling: the IP2Location download client, wget or curl, IP2Location BIN libraries, any MMDB reader
- composes with: a monthly download of DB11 LITE gives city-level lookups locally with no request meter, and the same account adds IP2Proxy LITE and ASN LITE; the hosted API is the separate IP2Location.io record. Bulk path: the monthly LITE downloads
- reliability: a LITE account is disabled when account sharing or massive download is detected; LITE accuracy is stated as 98 percent at country and 60 percent at city level
- notes: Free requests: unmetered local lookups against the monthly LITE files. Rate limit: none; one download a month is expected. Bulk path: the monthly DB1 to DB11 LITE, IP2Proxy LITE and ASN LITE downloads (BIN, CSV, MMDB).
- evidence note: the LITE landing pages, the DB11 page, the LITE FAQ and the registration form were quoted on 2026-10-30. No account was opened, so no file was downloaded; a token download would move it to measured.
- extras:
  - bulk_path: monthly IP2Location LITE, IP2Proxy LITE and ASN LITE downloads with an account token
  - free_requests: unmetered local lookups
- evidence:
  - [1] 2026-10-30: one signup opens all three LITE databases | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: One signup unlocks access to all three comprehensive LITE databases.
  - [1] 2026-10-30: LITE is free for personal or commercial projects | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: Use LITE freely for personal or commercial projects.
  - [1] 2026-10-30: LITE releases are monthly | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: Stay current with monthly data releases.
  - [1] 2026-10-30: LITE country accuracy is stated as 98 percent | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: 98% country accuracy
  - [1] 2026-10-30: LITE city accuracy is stated as 60 percent | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: 60% city accuracy
  - [4] 2026-10-30:  | capture: sha256:e4ab32ddaf0411418ae78c96fba35160d953adf3c049b3b4584281bb673631d9
  - [2] 2026-10-30: DB11 LITE IPv4 file sizes | capture: sha256:0961968022713a1cb6f9e5a2352e33fe166eb951ad458dc67368155b953c1af4 | quote: | IPv4 Database Size | BIN: 93.03 MB CSV: 331.25 MB (2,990,649 Rows) CIDR: 388.6 MB (3,774,146 Rows) MMDB: 84.64 MB |
  - [2] 2026-10-30: DB11 LITE IPv6 file sizes | capture: sha256:0961968022713a1cb6f9e5a2352e33fe166eb951ad458dc67368155b953c1af4 | quote: | IPv6 Database Size | BIN: 221.11 MB CSV: 858.83 MB (6,026,149 Rows) CIDR: 1.2 GB (11,176,080 Rows) |
  - [3] 2026-10-30: the databases update on the first day of the month | capture: sha256:a897d92e8b2822e8cd8659021b6b971370a07028c108b74fd4e686d8e3a65bd9 | quote: We update IP2Location databases on the first day of the calendar month.
  - [3] 2026-10-30: one download a month in the first week is expected | capture: sha256:a897d92e8b2822e8cd8659021b6b971370a07028c108b74fd4e686d8e3a65bd9 | quote: Please download the database once a month during a random day from the first week of calendar month to avoid network congestion.
  - [3] 2026-10-30: massive downloads disable the account | capture: sha256:a897d92e8b2822e8cd8659021b6b971370a07028c108b74fd4e686d8e3a65bd9 | quote: We will disable any LITE account if account sharing or massive download is detected.
  - [3] 2026-10-30: the download client takes a per-account token | capture: sha256:a897d92e8b2822e8cd8659021b6b971370a07028c108b74fd4e686d8e3a65bd9 | quote: ./download.pl -package DB11LITE -token DOWNLOAD_TOKEN
  - [3] 2026-10-30:  | capture: sha256:a897d92e8b2822e8cd8659021b6b971370a07028c108b74fd4e686d8e3a65bd9
  - [5] 2026-10-30: the registration form asks a name | capture: sha256:48824a9243548df3d67aca92b9e1cc4d74e10907774d32bac2a384f77a991bdb | quote: <label for="name" class="form-label">Name</label>
  - [5] 2026-10-30: the registration form asks an email address | capture: sha256:48824a9243548df3d67aca92b9e1cc4d74e10907774d32bac2a384f77a991bdb | quote: <label for="emailAddress" class="form-label">Email Address</label>
  - [5] 2026-10-30: the registration form asks a password | capture: sha256:48824a9243548df3d67aca92b9e1cc4d74e10907774d32bac2a384f77a991bdb | quote: Password must be at least 8 characters in length, include at least one upper case letter, one number, and one special character.
  - [5] 2026-10-30: GitHub sign-in is offered | capture: sha256:48824a9243548df3d67aca92b9e1cc4d74e10907774d32bac2a384f77a991bdb | quote: vendor%3Dgithub
  - [5] 2026-10-30: Google sign-in is offered | capture: sha256:48824a9243548df3d67aca92b9e1cc4d74e10907774d32bac2a384f77a991bdb | quote: vendor%3Dgoogle
  - [2] 2026-11-02: the DB11 LITE page, current version 01 November 2026, lists the IPv4 and IPv6 file sizes | capture: sha256:a5f39ad500fa0a8c0c6ca9dc4c8ec8d7f824cf31876d8d4dfc613fe904b2561e | quote: | IPv4 Database Size | BIN: 92.26 MB CSV: 328.53 MB (2,965,251 Rows) CIDR: 385.97 MB (3,747,194 Rows) MMDB: 85.25 MB |
  - probe:https://www.ip2location.com/download?file=DB11LITE 2026-11-02: a download request with no token was redirected with HTTP 302 to the log-in page, so a token download needs an account | capture: sha256:73e625204fa3efa5d69cda4f3d0edb3020894713087910632d624fc14e8015f4 | quote: "status": 302
  - [5] 2026-11-02: the LITE registration form asks name, email address, a password of at least 8 characters with a confirmation field and an agreement checkbox, and offers Google and GitHub sign-up | capture: sha256:8306684329afc8ccb7510ec36e7024956635e76c8acd5da26d33b193cdb9390c | quote: Password must be at least 8 characters in length, include at least one upper case letter, one number, and one special character.
  - [2] 2026-11-02: the DB11 LITE page lists current version 01 November 2026 and next update 15 November 2026 | capture: sha256:a5f39ad500fa0a8c0c6ca9dc4c8ec8d7f824cf31876d8d4dfc613fe904b2561e | quote: | Next Update | 15 November, 2026 |
  - [1] 2026-11-02: the LITE page states a semi-monthly update frequency for the LITE edition, beside its text about monthly releases | capture: sha256:2bf38d2c9bd89a3ba2f69f5b42c659e29daff49c78b72b7b82047ef831558d1c | quote: | Update Frequency | Semi-monthly | Daily / Weekly / Semi-monthly |
  - [6] 2026-11-02: the token download URL is www.ip2location.com/download with the parameters token and file, and downloads redirect to presigned R2 URLs | capture: sha256:bea3f2dbc019444d7784cf95cc7d10f228259e67221e26cde800d1f992118a39 | quote: wget "https://www.ip2location.com/download?token={DOWNLOAD_TOKEN}&file={DATABASE_CODE}" -O {LOCAL_ZIP_FILE_NAME}
  - probe:https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP 2026-11-02: a HEAD request for IP2LOCATION-LITE-DB1.CSV.ZIP at download.ip2location.com/lite/ with no account or token answered HTTP 200 with content-length 2610652 and last-modified 01 Nov 2026 | capture: sha256:fed58b575ddf2cd8d73314ac21f87dc906fb9aab9dd24c39fa19764fe4216373 | quote: "status": 200
  - [7] 2026-11-02: the open directory download.ip2location.com/lite/ lists only DB1 LITE files, with their sizes and the date 01-Nov-2026 | capture: sha256:2cefd9bd64f3c49258c6ae641209e52f435a359958121b98fac150674a561949 | quote: IP2LOCATION-LITE-DB1.CSV.ZIP 01-Nov-2026 00:00 2610652
  - probe:https://download.ip2location.com/lite/IP2LOCATION-LITE-DB11.CSV.ZIP 2026-11-02: the open directory has no DB11 LITE file: a HEAD request for IP2LOCATION-LITE-DB11.CSV.ZIP answered HTTP 404 | capture: sha256:3b1f150938a385236f94a51a5c35876dcfa2522b6715790fc7efe595ce36ffb4 | quote: "status": 404
  - [5] 2026-11-02: the LITE registration form asks name, email address and password, with no card or phone field | capture: sha256:8306684329afc8ccb7510ec36e7024956635e76c8acd5da26d33b193cdb9390c | quote: <label for="emailAddress" class="form-label">Email Address</label>
- sources:
  - [1] https://www.ip2location.com/database/lite
  - [2] https://lite.ip2location.com/database/db11-ip-country-region-city-latitude-longitude-zipcode-timezone
  - [3] https://lite.ip2location.com/faqs
  - [4] https://lite.ip2location.com/
  - [5] https://www.ip2location.com/register?id=lite
  - [6] https://www.ip2location.com/free/downloader
  - [7] https://download.ip2location.com/lite/
