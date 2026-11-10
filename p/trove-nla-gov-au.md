# Trove API

> trove.nla.gov.au | Data APIs, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trove-nla-gov-au/ | JSON https://fshy.ajam.dev/api/v1/entity/trove-nla-gov-au.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trove API (National Library of Australia)

- `data-apis/trove-api` | qualifies-with-caveat | evidence documented | binding write-gated | category library and newspaper metadata API | tier Free key (non-commercial, reviewed)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:50.592Z (live) | stale on 2026-12-03
- url https://trove.nla.gov.au/about/create-something/using-api
- free tier: A free API key after a reviewed application: 200 calls per minute (200m) at review Levels 1 to 4, up to 100 results per category per call, and a bulk download of search results to CSV (at most 1,000,000 records) in the Trove account. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Most applications are answered within a week; The quota can be raised on request, subject to approval.
- per-object cap: 100 results per category per call (n, default 20) | source: [2] | note: Paging uses a cursor (s and nextStart); bulkHarvest=true sorts by identifier so a harvest sees each record once.
- retention: bulk download files are deleted automatically seven days after they are created | days: 7 | source: [3] | note: A caller may hold retrieved metadata for at most 30 days, and only for offline use or where real-time calls would hurt performance; otherwise each display makes a live call.
- egress: not applicable: XML or JSON answers; bulk download files are CSV | metered: no | source: [3]
- identity: email | detail: A Trove account is needed first (its sign-up fields are unverified: the sign-up page renders by script); then an application form asking for the account username and contact details, the call rate needed, why and how the API will be used, and an agreement to the API terms. No card is mentioned.
- interface: rest
- limits:
  - request-rate: 200 API calls per minute (200m) as the standard quota [2]
  - per-object-cap: 100 results per category per call; bulk download results limited to 1,000,000 records and 10 downloads at a time [3]
  - write-gated (binding): a key is issued after a staff review of an application form; harvesting full text or AI use needs an approved exemption [1]
- binding note: No call works without a key, and the key comes from a reviewed application; 200 calls a minute is met only after that.
- interface detail: REST over HTTPS at api.trove.nla.gov.au/v3 (result search, work, newspaper, gazette, magazine titles, list, people) with an OpenAPI file; the key goes in the key parameter or a header; XML by default, JSON with encoding=json
- endpoint: https://api.trove.nla.gov.au/v3/result
- tooling: any HTTP client
- composes with: Metadata for books, images, maps, music, journals and digitised newspaper and gazette articles from Australian libraries; article full text is included with include=articletext for approved uses.
- reliability: A keyless call answered HTTP 401 No API key found in request; the Trove website pages, not the API host, sit behind an Anubis proof-of-work challenge that a plain page fetch stores as a challenge page; keys can be withdrawn at the Library's discretion.
- notes: Storage: retrieved metadata may be cached for up to 30 days for offline use or performance; otherwise each display makes a live call; bulk download CSV files last 7 days. Bulk path: Download results in a Trove account (CSV of metadata and an abstract, up to 1,000,000 records, one category at a time, 10 downloads at a time) or bulkHarvest=true through the API. This is the read API; the deposit question has its own record in storage.
- evidence note: Key process, review levels, quota, caps, bulk download and caching limit are read from first-party pages; a keyless call answered HTTP 401, and the key application is behind a sign-up, so whether an individual key is granted is unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-02: ongoing use needs an active API key | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9 | quote: On-going use of the Trove API will require an active API key.
  - [1] 2026-11-02: a Trove account is needed to receive a key | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9 | quote: You will need a Trove account to receive a Trove API key.
  - [1] 2026-11-02: the application form asks for the call rate needed | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9 | quote: - the rate of calls you require
  - [1] 2026-11-02: most applications are answered within a week | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9 | quote: Most requests will be answered within a week, however complex enquiries or those that need higher review may take longer.
  - [1] 2026-11-02:  | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9
  - [1] 2026-11-02: harvesting full-text records and AI modelling are Level 3 and need an exemption | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9
  - [1] 2026-11-02: training generative AI is Level 4 and needs an exemption | capture: sha256:fd94cdc3f07e535ec3432a1a46f8aa461bbdad5bdc4bfcaed6d27e079daed7b9 | quote: | Level 4 | 200m | | | Training generative AI | Y |
  - [2] 2026-11-02: the standard quota is 200 calls per minute | capture: sha256:8de2bd3e80ae5aaf767d9f9972ffa285ec94d75082dd51d0e5cb39f8211a44d7 | quote: The standard API quota is 200m (API calls per minute).
  - [2] 2026-11-02: a call returns at most 100 results per category | capture: sha256:179863c35b9c5ddbbaa6fd6cd9de6e5c57e44174289772028ae02155bdcda447 | quote: The number of results to return per category. Maximum is 100.
  - [2] 2026-11-02: a bulkHarvest parameter orders results by identifier for a harvest | capture: sha256:179863c35b9c5ddbbaa6fd6cd9de6e5c57e44174289772028ae02155bdcda447 | quote: Include this parameter if you intend to harvest a set of records for further processing in your own system.
  - [3] 2026-11-02: bulk download files are deleted seven days after creation | capture: sha256:c0deb1043efca6af79ae205e10ad074da260c51a1bb734f77ee2f7a7d2f35553 | quote: Bulk downloaded files will be automatically deleted seven days after they are created, so make sure to save it of you need it longer than this period.
  - [3] 2026-11-02: a bulk download is limited to 1,000,000 records | capture: sha256:c0deb1043efca6af79ae205e10ad074da260c51a1bb734f77ee2f7a7d2f35553 | quote: Search result downloads are limited to 1,000,000 records.
  - [3] 2026-11-02: at most 10 bulk downloads can exist at a time | capture: sha256:c0deb1043efca6af79ae205e10ad074da260c51a1bb734f77ee2f7a7d2f35553 | quote: Note that you may only have a maximum of 10 downloads at a time.
  - [4] 2026-11-02: retrieved metadata may be cached for at most 30 days, and only for offline use or performance | capture: sha256:118122ce7e8192eecdc141ce3bf1d1dfba9c161d16bdca78fd3c4a03f9e9a42e | quote: in which case you may cache Trove metadata retrieved via the Trove API for up to 30 days.
  - [4] 2026-11-02: the Library may refuse any key at its discretion | capture: sha256:118122ce7e8192eecdc141ce3bf1d1dfba9c161d16bdca78fd3c4a03f9e9a42e | quote: (a) not to grant an API key to any person or organisation at its complete discretion;
  - probe:https://api.trove.nla.gov.au/v3/result?category=newspaper&q=test&encoding=json 2026-11-02: a keyless call answers HTTP 401 No API key found in request | capture: sha256:c3e937d7627f54190215d3baba37a69a5b85e3632345d72f84f40cefe869e221 | quote: "message":"No API key found in request"
- sources:
  - [1] https://trove.nla.gov.au/about/create-something/using-api
  - [2] https://trove.nla.gov.au/about/create-something/using-api/v3/api-technical-guide
  - [3] https://trove.nla.gov.au/about/create-something/bulk-download
  - [4] https://trove.nla.gov.au/about/create-something/using-api/trove-api-terms-use

## trove (national library of australia)

- `storage/trove` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://trove.nla.gov.au/about/contribute
- free tier: None reachable: Anubis proof-of-work wall on /about/contribute, and structurally Trove is a discovery layer over member-collection metadata plus newspaper OCR. Not an upload target for third-party bulk dat. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Anubis proof-of-work wall on /about/contribute, and structurally Trove is a discovery layer over member-collection metadata plus newspaper OCR — not an upload target for third-party bulk…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Anubis proof-of-work wall on /about/contribute, and structurally Trove is a discovery layer over member-collection metadata plus newspaper OCR — not an upload target for third-party bulk…
- sources:
  - [1] https://trove.nla.gov.au/about/contribute
