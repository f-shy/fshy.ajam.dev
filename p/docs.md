# walrus

> docs.wal.app | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs/ | JSON https://fshy.ajam.dev/api/v1/entity/docs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Walrus Testnet public publishers (Mysten Labs + community)

- `storage/walrus-testnet-public-publishers` | qualifies-with-caveat | evidence reported | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.wal.app/docs/system-overview/public-aggregators-and-publishers
- free tier: No account, no key, no quota. Docs quote only a per-request limit: 'Most aggregators and publishers limit requests to 10 MiB by default'. In practice the reference publisher accepted 300 MiB and 1 GiB. Max storage duration is 53 epochs; on Testnet 1 epoch = 1 day. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 1 GiB | bytes: 1073741824 | source: [1] | note: not stated
- retention: retention: 53 epochs max, 1 day per epoch on Testnet = 53 days, and 'Walrus wipes the data periodically without warning' | days: 1 | source: [1] | note: not stated
- egress: unmetered. Reads are served by ~55 independent community aggregators plus the Mysten reference aggregator; all returned CORS-open bytes with no metering observed and no auth header. | metered: no
- identity: anonymous
- interface: rest, cli
- limits:
  - retention-clamped: retention: 53 epochs max, 1 day [1]
  - per-object-cap (binding): per-object-cap: 1 GiB [1]
- limits note: per-object-cap: 1 GiB verified write; read path has a per-object-cap of 500 MiB on the Mysten reference aggregator (403 SIZE_EXCEEDED, 'the blob size exceeds the maximum allowed size: 524288000') while community aggregators served the same 1 GiB blob fine. retention: 53 epochs max, 1 day per epoch on Testnet = 53 days, and 'Walrus wipes the data periodically without warning'. request-rate: 10 x 1 MiB PUTs back-to-back all returned 200, no shaping seen; no rate limit documented on Testnet.
- interface detail: rest
- tooling: Plain HTTP: PUT $PUBLISHER/v1/blobs?epochs=N --upload-file; GET $AGGREGATOR/v1/blobs/<blobId>. OpenAPI at /v1/api. Machine-readable operator list at https://docs.wal.app/operators.json (updated weekly). Walrus CLI + TypeScript SDK also exist (github.com/MystenLabs/walrus).
- composes with: 16 public Testnet publishers in operators.json (3 live-tested: walrus.space, tududes, banansen) x unlimited keyless PUTs x unlimited blobs. Any number of blobs per publisher; distinct content hashes so no account dimension is needed at all. Store 10 TiB as 20,000 x 500 MiB blobs, or 10,000 x 1 GiB against community aggregators. Also: 53-epoch max means re-upload on a rolling schedule, so 'capacity' = (publishers x disk) not a per-identity tier.
- reliability: Testnet is periodically wiped without warning and publishers are volunteer-run (2 of 5 tested endpoints were down: h2o-nodes 502, atalma connection refused); treat as ephemeral, not archive.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [2] 2026-10-21: 'You do not need to run your own daemon... community operators expose public aggregator and publisher services'; 'Most aggregators and publishers limit requests to 10 MiB by default'
  - [1] 2026-10-21: epoch duration Testnet 1 day, Mainnet 2 weeks; 'Maximum number of epochs for which storage can be bought 53'; 'Data persistence ... Walrus wipes the data periodically without warning'
  - [3] 2026-10-21: probe: PUT --upload-file <1 GiB random> -> 200 in 165 s, blobId AzBDr3weHh3aHfjIdql5DT8z357Y1FGK3nDIJC5KEeI, storageSize 4888852000
  - [4] 2026-10-21: probe: GET GiB id> -> 403 SIZE_EXCEEDED 524288000; GET https://walrus-testnet-aggregator.stakely.io/v1/blobs/<same id> -> 200, 1073741824 bytes, sha256 matches original byte-for-byte
  - withheld 2026-10-21: probe: 16 parallel 3 MiB ranged GETs of a 50 MiB blob -> 200/206, 50,331,648 bytes in 1.98 s (25.4 MB/s) vs 3.97 MB/s single-stream (13.2 s) — 6.4x from concurrency
- sources:
  - [1] https://docs.wal.app/docs/network-reference
  - [2] https://docs.wal.app/docs/system-overview/public-aggregators-and-publishers
  - [3] https://publisher.walrus-testnet.walrus.space/v1/blobs?epochs=53
  - [4] https://aggregator.walrus-testnet.walrus.space/v1/blobs/<1

## walrus (sui)

- `storage/walrus-2` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.wal.app/docs/system-overview/storage-costs
- free tier: none reachable: $0.023/GB/month with no free tier, billed on encoded size which is ~4.5x the file plus 64 MB per-blob overhead. A 50 GB file for a year is ~$62; 20 TiB would be ~$25,000/yr and rising with… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: $0.023/GB/month with no free tier, billed on encoded size which is ~4.5x the file plus 64 MB per-blob overhead. A 50 GB file for a year is ~$62; 20 TiB would be ~$25,000/yr and rising with…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: $0.023/GB/month with no free tier, billed on encoded size which is ~4.5x the file plus 64 MB per-blob overhead. A 50 GB file for a year is ~$62; 20 TiB would be ~$25,000/yr and rising with…
  - [2] 2026-10-21: cited as the basis of the rejection: $0.023/GB/month with no free tier, billed on encoded size which is ~4.5x the file plus 64 MB per-blob overhead. A 50 GB file for a year is ~$62; 20 TiB would be ~$25,000/yr and rising with e
- sources:
  - [1] https://docs.wal.app/docs/system-overview/storage-costs
  - [2] https://docs.wal.app/docs/sponsored-uploads

## walrus mainnet (public upload)

- `storage/walrus-mainnet` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.wal.app/docs/http-api/storing-blobs
- free tier: none reachable: No keyless publisher exists and none is planned: 'Walrus has no public unauthenticated publisher on Mainnet. There are no plans to create one.' Every store spends WAL + SUI, and 'There is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: No keyless publisher exists and none is planned: 'Walrus has no public unauthenticated publisher on Mainnet. There are no plans to create one.' Every store spends WAL + SUI, and 'There is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No keyless publisher exists and none is planned: 'Walrus has no public unauthenticated publisher on Mainnet. There are no plans to create one.' Every store spends WAL + SUI, and 'There is…
  - [2] 2026-10-21: cited as the basis of the rejection: No keyless publisher exists and none is planned: 'Walrus has no public unauthenticated publisher on Mainnet. There are no plans to create one.' Every store spends WAL + SUI, and 'There is no
  - [3] 2026-10-21: cited as the basis of the rejection: No keyless publisher exists and none is planned: 'Walrus has no public unauthenticated publisher on Mainnet. There are no plans to create one.' Every store spends WAL + SUI, and 'There is no
- sources:
  - [1] https://docs.wal.app/docs/http-api/storing-blobs
  - [2] https://docs.wal.app/docs/sponsored-uploads
  - [3] https://docs.wal.app/operators.json
