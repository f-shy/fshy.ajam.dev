# Europe PMC

> europepmc.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/europepmc/ | JSON https://fshy.ajam.dev/api/v1/entity/europepmc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Europe PMC

- `debrid/europe-pmc` | qualifies-with-caveat | evidence documented | binding request-rate | category biomedical literature index with an open-access full-text subset | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://europepmc.org/RestfulWebService
- price USD 0
- free tier: REST access to 'over 33 million publications', including '10.2 million full text articles and 6.5 million open access articles', with JSON or XML responses and pageSize up to 1000. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: pageSize=1000 returned 786,907 bytes of JSON in one response here; pageSize=100 returned 88,669 bytes.
- per-object cap: not applicable: one JSON/XML response per request, paged. The largest single response measured was 786,907 bytes at pageSize=1000. | source: [2]
- retention: the index is continuously updated; the bulk FTP tree carries dated snapshots (weekly for metadata, per-release for the OA subset) | source: [3]
- egress: Free and unmetered from the EBI endpoint. No key, no account, no registration mentioned anywhere on the web-service page. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No key and no account: an anonymous GET returned 200 and 1,408 bytes. Nothing on the web-service page asks for registration.
- interface: rest, ftp, cli
- limits:
  - request-rate (binding): no numeric rate limit is published; paging is by pageSize/cursorMark and the largest single page is pageSize=1000 [1]
- limits note: The bulk path is FTP and it did not answer from this network: https://europepmc.org/ftp/oa/ returned 403 and ftp://europepmc.org/oa/ timed out after 20 s. That is a reachability fact about this network, not a statement that the mirror is gone.
- binding note: With the FTP mirror unreachable here, the API is the only path, and it is one page per call with no published ceiling: at 787 KB per pageSize=1000 call, a TiB would take about 1.4 million calls, so the call rate decides the day's bytes, not any byte quota.
- interface detail: GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&pageSize=1000&cursorMark=...; eight bulk content types are listed at /downloads and served over FTP.
- endpoint: part of interface detail
- tooling: curl/python-requests for the API; lftp or curl for the FTP tree. No SDK needed.
- composes with: Use Europe PMC as the index (PMIDs, PMCIDs, licence flags, full-text availability) and pmc-oa-opendata as the byte store; the API's pageSize=1000 gives about 787 KB of metadata per call without an account.
- reliability: No throttling signal was seen at the low rate used here; the FTP tree is the fragile part - one 403 on HTTPS and a timeout on port 21 make the bulk mirror look absent when it may only be filtered.
- notes: Caveat is the bulk mirror, not the API. Metadata is effectively unlimited through pageSize=1000; full text at TiB scale depends on the FTP tree, which this network could not open.
- evidence note: The API was exercised at two page sizes with byte counts, and the bulk-path failures were observed. The 33M/10.2M/6.5M counts are the vendor's own page, not independently measured.
- extras:
  - page_1000_bytes: 786907
  - page_100_bytes: 88669
  - publications: 33000000
  - oa_fulltext: 6500000
  - ftp_https_status: 403
- evidence:
  - [1] 2026-10-23: 'over 33 million publications', '10.2 million full text articles and 6.5 million open access articles', JSON/XML output
  - [3] 2026-10-23: eight bulk content types (OA subset, author manuscripts, preprints, metadata, ID mappings, text-mined terms) served over FTP
  - probe:https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=OPEN_ACCESS:Y&format=json&pageSize=1000 2026-10-23: 200, 786,907 bytes in one anonymous response - pageSize=1000 is accepted and returns real records
  - probe:https://europepmc.org/ftp/oa/ 2026-10-23: 403 over HTTPS - the FTP tree has no HTTPS mirror at that path
- sources:
  - [1] https://europepmc.org/RestfulWebService
  - [2] https://www.ebi.ac.uk/europepmc/webservices/rest/search
  - [3] https://europepmc.org/downloads
