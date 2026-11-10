# mempool.space API

> mempool.space | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mempool/ | JSON https://fshy.ajam.dev/api/v1/entity/mempool.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mempool.space API

- `data-apis/mempool-space` | qualifies | evidence documented | binding request-rate | category Bitcoin explorer REST API (blocks, transactions, fees, mempool) | tier Public API
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://mempool.space/docs/api/rest
- free tier: Public REST API with no key; rate limits are enforced but their size is not published; HTTP 429 on excess and a possible ban on repeated excess | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: Bulk block queries return up to 10 blocks per call; more needs an enterprise sponsorship. A keyless tip-height call answered HTTP 200. Enterprise starts at USD 1499 a month with higher limits by API key or IP allow-list.
- per-object cap: 10 blocks per blocks-bulk call | source: [1]
- retention: not applicable
- egress: not metered in bytes; request limits of unpublished size apply | metered: no | source: [1]
- identity: anonymous | detail: The public API needs no account or key; a keyless call answered HTTP 200. Enterprise limits go through an API key or IP allow-list after signing up.
- interface: rest
- limits:
  - request-rate (binding): rate limits enforced, size not published; HTTP 429 on excess [1]
  - per-object-cap: up to 10 blocks per blocks-bulk call [1]
- limits note: Bulk path: none beyond 10 blocks a call without Enterprise. Storage terms: unverified, no page read states one.
- binding note: The unpublished request limit, with a ban after repeated 429s, is the ceiling a keyless client meets.
- interface detail: GET https://mempool.space/api/... with no key, plus a WebSocket at wss://mempool.space/api/v1/ws; testnet, testnet4 and signet have their own paths
- endpoint: part of interface detail
- tooling: curl or any HTTP client; mempool.js is the JavaScript client. The open-source stack can also be installed and run by the user on a rented or free machine, which is the last resort after the hosted public API and Enterprise.
- composes with: Keyless Bitcoin chain data and fee estimates; Enterprise raises the limits when the public API throttles.
- reliability: Past the limits the API answers HTTP 429 and repeated excess can ban the caller.
- notes: Keyless with unpublished limits. Bulk path: 10 blocks a call. Storage terms: unverified.
- evidence note: Limits and bulk cap are read from the vendor docs; a keyless call answered 200; the rate size is unpublished.
- extras:
  - bulk_path: blocks-bulk, 10 blocks a call; more is Enterprise
- evidence:
  - [1] 2026-11-02: limits are enforced, 429 on excess, possible ban | capture: sha256:696c7d3725ad918ad77a4d98c036dfe13736a02b61315c5da6582fbaf6d1b788 | quote: Note that we enforce rate limits. If you exceed these limits, you will get an HTTP 429 error. If you repeatedly exceed the limits, you may be banned from accessing the service altogether.
  - [1] 2026-11-02: bulk block queries are capped at 10 blocks | capture: sha256:696c7d3725ad918ad77a4d98c036dfe13736a02b61315c5da6582fbaf6d1b788 | quote: To return data for more than 10 blocks, consider becoming an enterprise sponsor.
  - [2] 2026-11-02: Enterprise starts at USD 1499 a month | capture: sha256:0d023a11cbb9a24b9e029e02177248da5046cc3ead61bc5cf268191b35d30059 | quote: Silver$1499 per month
  - [2] 2026-11-02: higher limits come through API keys or IP whitelisting | capture: sha256:0d023a11cbb9a24b9e029e02177248da5046cc3ead61bc5cf268191b35d30059 | quote: Higher rate limits available through API keys or IP whitelisting.
  - probe:https://mempool.space/api/blocks/tip/height 2026-11-02: a keyless tip-height call answered HTTP 200 | capture: sha256:4d5c1d27ef83910476e89ed679728310d7e3c39a2fbeddc948a0a6522101cc8a | quote: "status": 200
- sources:
  - [1] https://mempool.space/docs/api/rest
  - [2] https://mempool.space/enterprise
