# Frankfurter

> frankfurter.dev | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frankfurter/ | JSON https://fshy.ajam.dev/api/v1/entity/frankfurter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Frankfurter

- `data-apis/frankfurter` | qualifies | evidence documented | binding request-rate | category exchange rate API (central bank reference rates, daily, history to 1948) | tier Public API
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://frankfurter.dev/
- free tier: Free public API at api.frankfurter.dev: no key, no quotas, no monthly or daily caps; requests are rate-limited only to prevent abuse; 228 currencies from 106 central banks and official sources, history back to 1948 | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: v2 is current and v1 is deprecated but stays available. Rates update once a day. Output is JSON, CSV or NDJSON. Keyless v1 and v2 rate calls answered HTTP 200; one earlier call answered a transient 522.
- per-object cap: not stated; narrow quotes and use NDJSON for large date ranges | source: [1]
- retention: not applicable | note: History goes back to 1948.
- egress: not metered; no quota is stated | metered: no | source: [1]
- identity: anonymous | detail: No key and no account: the vendor says no API key is needed and keyless calls answered HTTP 200.
- interface: rest
- limits:
  - request-rate (binding): rate-limited to prevent abuse, size not published; no monthly or daily caps [1]
- limits note: Bulk path: request a date range with from and to as NDJSON or CSV to stream the whole series. Storage terms: storing daily observations locally for caching or analytics is encouraged by the vendor.
- binding note: Only an unpublished abuse limit exists; there is no quota.
- interface detail: GET https://api.frankfurter.dev/v2/rates, /v2/rate/BASE/QUOTE and /v2/providers/ecb/rates; .csv suffix or Accept: application/x-ndjson for CSV and NDJSON; an MCP server at mcp.frankfurter.dev
- endpoint: part of interface detail
- tooling: curl or any HTTP client; the open-source project can also be installed and run by the user with Docker, which is the last resort after the hosted public API.
- composes with: Keyless daily reference rates to convert prices from the crypto and finance records; cache the daily rows locally.
- reliability: One call answered a transient HTTP 522 from the edge; later calls answered 200.
- notes: Keyless, no quotas. Bulk path: date ranges as NDJSON or CSV. Storage: local caching is encouraged.
- evidence note: Terms are read from the vendor page; keyless v1 and v2 calls answered 200; the abuse limit was not measured.
- extras:
  - bulk_path: from/to date ranges streamed as NDJSON or CSV
  - history_depth: back to 1948
- evidence:
  - [1] 2026-11-02: 228 currencies from 106 sources, daily, back to 1948 | capture: sha256:47f1f9327205dbbaf60b5393475c5bbcbb5efee37da64d546eb9c23aed6c3a51 | quote: Frankfurter is a free exchange rates API for 228 currencies from 106 central banks and official sources. Rates update daily and go back to 1948.
  - [1] 2026-11-02: no API key is needed | capture: sha256:47f1f9327205dbbaf60b5393475c5bbcbb5efee37da64d546eb9c23aed6c3a51 | quote: You don't need an API key.
  - [1] 2026-11-02: no quotas or monthly or daily caps | capture: sha256:47f1f9327205dbbaf60b5393475c5bbcbb5efee37da64d546eb9c23aed6c3a51 | quote: There are no quotas. Requests are rate-limited to prevent abuse, but there are no monthly or daily caps.
  - [1] 2026-11-02: storing daily observations locally is encouraged | capture: sha256:47f1f9327205dbbaf60b5393475c5bbcbb5efee37da64d546eb9c23aed6c3a51 | quote: Storing daily observations locally for caching or historical analytics is encouraged to keep API traffic light.
  - [1] 2026-11-02: NDJSON streams large time series | capture: sha256:47f1f9327205dbbaf60b5393475c5bbcbb5efee37da64d546eb9c23aed6c3a51 | quote: Each line is one independent JSON object, useful for streaming large time series without buffering the entire response.
  - probe:https://api.frankfurter.dev/v2/rates 2026-11-02: a keyless v2 rates call answered HTTP 200 | capture: sha256:63734813e4fd2be5551734cb15a9dc1c507f44494d48e54e48af0a9dc20743f7 | quote: "status": 200
- sources:
  - [1] https://frankfurter.dev/
