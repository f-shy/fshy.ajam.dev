# Tableland

> tableland.xyz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tableland/ | JSON https://fshy.ajam.dev/api/v1/entity/tableland.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tableland

- `storage/tableland` | fails-quota | evidence documented | binding per-object-cap | category web3-database
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:24:43.358Z (live) | stale on 2026-12-05
- url https://tableland.xyz
- free tier: 500,000 rows and 24 columns per table. That is the entire quota. It is a SQL-over-SQLite network, not an object store. Byte capacity is implied by row content and is not published as a number, but 500k rows × 24 columns cannot reach 500 GB under any encoding. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: each table cell is limited to 1kb | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Reads go through the Tableland gateway and are free; there is no egress meter because the payloads are rows. | metered: no
- identity: email | detail: email
- interface: rest, cli
- limits:
  - per-object-cap (binding): each table cell is limited to 1kb; 500000 rows and 24 columns per table [2]
- limits note: fails-quota categorically. Still described as open beta with 'temporary limits while the production mainnet is further researched', so even the row cap is provisional.
- binding note: each cell holds at most 1kb and each table at most 500000 rows by 24 columns; the docs state it is not a file storage solution
- interface detail: rest
- tooling: Studio web app + Studio CLI + JS SDK, and a documented SQL API. Clean for structured data; irrelevant for blobs. Their own docs recommend pushing large media to IPFS and storing only the CID in a table. Which is an admission that the network is a pointer store.
- composes with: Tables are creatable per project and per team, so the multiplier is tables × 500k rows. Even at 10,000 tables this is a metadata tier, not a byte tier.
- reliability: As read on 2026-11-03, tableland.xyz and docs.tableland.xyz answer HTTP 302 to textile.io and then HTTP 302 to the 2026-10-30 post announcing the wind-down of Recall Labs. Beta-network limits were explicitly flagged as temporary. Do not build a chunk index on a limit that a mainnet launch can change.
- notes: the same as the free tier
- evidence note: re-read on 2026-11-03: the vendor docs limits page https://raw.githubusercontent.com/tablelandnetwork/docs/main/docs/fundamentals/limits.md (row, column and cell limits, not a file storage solution) and the Recall Labs wind-down post on x.com (RecallLabs_) that tableland.xyz and docs.tableland.xyz redirect to; identity, tooling and retention were not read
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 500,000 rows and 24 columns per table. That is the entire quota — it is a SQL-over-SQLite network, not an object store. Byte capacity is implied by row content and is not published as a number, but 500k rows × 24 columns cannot reach 500 GB under any encoding.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: fetched raw: 'Table limits … Rows 500000 … Columns 24'; 'Since Tableland is still in open beta, each table is limited to the following constraints … These are temporary limits'.
  - [3] 2026-10-21: opened: 'The decentralized cloud database … built on SQLite. Read and write tamperproof data from apps, data pipelines' — a database positioning, no storage claim.
  - [4] 2026-10-21: surfaced: 'Tableland naturally imposes limits on the size of data you can store in a table. If you need to store larger pieces media, you can use IPFS to store the data and then reference unique Content Identifiers in a table.' Their own recommended alternative route concedes the point.
  - [2] 2026-11-03: each table cell is capped at 1kb | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Each cell limit is 1kb.
  - [2] 2026-11-03: the docs say the network is not file storage | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Tableland is _not a file storage_ solution.
  - [5] 2026-11-03: the company that built the network announced its wind-down on 2026-10-30 | capture: sha256:56d5fded2755e82d1ab2cb5f223ed6877abb4e539960ade67b329079375a68cc | quote: We’ve made the decision to wind down Recall Labs.
  - [2] 2026-11-03: the per-table row limit is 500000 | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: | Rows | 500000 |
  - probe:tableland.xyz 2026-11-03: tableland.xyz redirects (HTTP 302 twice, via textile.io) to the Recall Labs post | capture: sha256:bbe5d9c808f06daa52ca656a8b9b27faeeee81dd3fc88fb1cd1f113f062ef76b | quote: "final_url": "https://x.com/RecallLabs_/status/2116235386582426069"
  - probe:docs.tableland.xyz 2026-11-03: docs.tableland.xyz redirects (HTTP 302 twice, via textile.io) to the same post | capture: sha256:e63caeec7e844fd0362ad7951e0173f771e3dae43705b4de36697204d61051f7 | quote: "final_url": "https://x.com/RecallLabs_/status/2116235386582426069"
  - [2] 2026-11-04: each table cell is capped at 1kb | capture: sha256:3de2af041bd64971a7ea2ca2ee46166f26434ed7885bce85336a1c5eb2606bc8 | quote: Each cell limit is 1kb.
- sources:
  - [1] https://docs.tableland.xyz/fundamentals/limits
  - [2] https://raw.githubusercontent.com/tablelandnetwork/docs/main/docs/fundamentals/limits.md
  - [3] https://tableland.xyz/
  - [4] https://docs.tableland.xyz/playbooks/integrations/ipfs
  - [5] https://x.com/RecallLabs_/status/2116235386582426069
