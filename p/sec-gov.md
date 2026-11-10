# SEC EDGAR Data APIs

> sec.gov | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sec-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/sec-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SEC EDGAR Data APIs

- `data-apis/sec-edgar-data` | qualifies | evidence documented | binding request-rate | category government filings API (filer submissions, XBRL company facts, bulk archives) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- free tier: Free data.sec.gov JSON APIs with no authentication or key; maximum request rate 10 requests per second; automated tools must declare a User-Agent; nightly bulk ZIP archives of all the JSON | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1] | note: The submissions API and XBRL data update through the day as filings are disseminated. The www.sec.gov documentation pages answered HTTP 403 to an automated page fetch with no declared agent. A keyless submissions call with a generic probe agent answered HTTP 200.
- per-object cap: not stated; one JSON per filer, and companyfacts.zip and submissions.zip hold every filer | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 10 requests per second rate bounds a client | metered: no | source: [2]
- identity: anonymous | detail: The APIs need no authentication or key; automated callers declare a User-Agent with a company name and contact address in the request header, which is not an account.
- interface: rest
- limits:
  - request-rate (binding): 10 requests per second maximum [2]
- limits note: Bulk path: companyfacts.zip and submissions.zip, rebuilt nightly at about 3:00 a.m. ET. Storage terms: no storage limit read; the page asks to download only what is needed.
- binding note: 10 requests per second is the only ceiling, and the bulk ZIPs avoid it.
- interface detail: GET https://data.sec.gov/submissions/CIK##########.json and https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json; bulk ZIPs under https://www.sec.gov/Archives/edgar/daily-index/
- endpoint: part of interface detail
- tooling: curl or any HTTP client that sends a declared User-Agent
- composes with: Company filings and XBRL facts for free; the nightly ZIPs replace thousands of calls and feed a database load.
- reliability: Requests above the rate, or from an undeclared automated tool, can be limited or refused; the www.sec.gov pages answered HTTP 403 to an automated fetch with no declared agent.
- notes: Keyless, 10 requests per second, nightly bulk ZIPs. Storage terms: no limit read.
- evidence note: Rate, auth and bulk terms are read from SEC pages; a keyless submissions call answered 200.
- extras:
  - bulk_path: companyfacts.zip and submissions.zip, rebuilt nightly about 3:00 a.m. ET
- evidence:
  - [1] 2026-11-03: the APIs need no authentication or keys | capture: sha256:7b38fa308d3d8f16f6d62377a36fac33cbe7ebcf43d4ea628920bd93270dbd39 | quote: These APIs do not require any authentication or API keys to access.
  - [1] 2026-11-03: the bulk ZIP is republished nightly | capture: sha256:7b38fa308d3d8f16f6d62377a36fac33cbe7ebcf43d4ea628920bd93270dbd39 | quote: This ZIP file is updated and republished nightly at approximately 3:00 a.m. ET.
  - [1] 2026-11-03: bulk archives are the efficient route | capture: sha256:7b38fa308d3d8f16f6d62377a36fac33cbe7ebcf43d4ea628920bd93270dbd39 | quote: The most efficient means to fetch large amounts of API data is the bulk archive ZIP files, which are recompiled nightly.
  - [2] 2026-11-03: maximum request rate is 10 per second | capture: sha256:a64b9647ce8b92d2619d808d10774b08fe138313adeb787523d54873f2b32f3b | quote: Current max request rate: 10 requests/second.
  - [2] 2026-11-03: automated callers declare a user agent | capture: sha256:a64b9647ce8b92d2619d808d10774b08fe138313adeb787523d54873f2b32f3b | quote: Please declare your user agent in request headers
  - probe:https://data.sec.gov/submissions/CIK0000320193.json 2026-11-03: a keyless submissions call answered HTTP 200 | capture: sha256:b318c312c7a84a4e07e5a3d1f8ccfc2370fbcd669e69a05a0511eee6f63008c5 | quote: "status": 200
- sources:
  - [1] https://www.sec.gov/search-filings/edgar-application-programming-interfaces
  - [2] https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data
