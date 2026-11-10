# MyIPRightNow

> myiprightnow.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/myiprightnow/ | JSON https://fshy.ajam.dev/api/v1/entity/myiprightnow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MyIPRightNow

- `data-apis/myiprightnow` | qualifies-with-caveat | evidence measured | binding none | category caller IP address and location echo API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://myiprightnow.com/
- free tier: keyless GET /api/ip returns the caller's own public IP address with network, location and timezone as JSON with permissive CORS; the page documents no parameter for another address | unit: requests | metered on: unstated | read on: 2026-11-02 | source: [1] | note: unverified: no request quota or rate limit is stated on the page.
- per-object cap: one record for the calling connection per request | source: [1]
- retention: not applicable: answers are marked no-store | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: a request with no key or credentials answered HTTP 200
- interface: rest
- limits:
  - request-rate: unverified: no rate limit or quota is stated [1]
- binding note: no limit is published, so none could be named.
- interface detail: GET https://myiprightnow.com/api/ip answers JSON with Access-Control-Allow-Origin *; curl and jq examples are shown on the page
- endpoint: part of interface detail
- tooling: any HTTP client; curl piped to jq as shown on the page
- composes with: Keyless read of the address, network and location a connection presents, useful for a script that needs its own egress address. It is a caller-only echo: unverified whether any lookup of another IP exists. Bulk path: none.
- reliability: no rate limit, quota or uptime statement is published; answers are marked no-store, so nothing is cached between the caller and the edge
- notes: Free requests: no quota stated. Rate limit: not stated. Bulk path: none; a caller-only lookup.
- evidence note: The page was quoted and a keyless HEAD of /api/ip was probed on 2026-11-02 (HTTP 200, application/json, no-store); a GET body was not saved because it describes the calling connection.
- extras:
  - bulk_path: none
  - free_requests: no quota stated
- evidence:
  - [1] 2026-11-02: the API is JSON at /api/ip with permissive CORS | capture: sha256:14e454ac103cc4fcc1bc7262d8088cd172563705743d4162b1d0f2cfbd2c7bda | quote: The same data is available as JSON at `/api/ip`, with permissive CORS, so you can call it from a script or a terminal:
  - [1] 2026-11-02: the data describes the caller's own address and network | capture: sha256:14e454ac103cc4fcc1bc7262d8088cd172563705743d4162b1d0f2cfbd2c7bda | quote: Your public address, and the network details that come with it.
  - [1] 2026-11-02: answers are marked no-store | capture: sha256:14e454ac103cc4fcc1bc7262d8088cd172563705743d4162b1d0f2cfbd2c7bda | quote: The response is marked `no-store`, so nothing between you and the edge keeps a copy of it.
  - [1] 2026-11-02: the address is not stored beyond the ordinary request log | capture: sha256:14e454ac103cc4fcc1bc7262d8088cd172563705743d4162b1d0f2cfbd2c7bda | quote: No. The address is read from the request and sent straight back to you, with no database and no logging beyond the ordinary request log our host keeps for security.
  - probe:https://myiprightnow.com/api/ip 2026-11-02: a keyless HEAD of /api/ip answered HTTP 200 | capture: sha256:4216c7596d63eed9ac1fa7a6bbc7d8f2b9fa403c41358601803392e8274c0981 | quote: "status": 200
  - probe:https://myiprightnow.com/api/ip 2026-11-02: the answer is marked no-store | capture: sha256:4216c7596d63eed9ac1fa7a6bbc7d8f2b9fa403c41358601803392e8274c0981 | quote: "cache-control": "no-store, private"
  - probe:https://myiprightnow.com/api/ip 2026-11-02: the answer allows cross-origin reads | capture: sha256:4216c7596d63eed9ac1fa7a6bbc7d8f2b9fa403c41358601803392e8274c0981 | quote: "access-control-allow-origin": "*"
- sources:
  - [1] https://myiprightnow.com/
