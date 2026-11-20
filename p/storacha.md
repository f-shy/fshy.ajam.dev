# Storacha

> storacha.network | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storacha/ | JSON https://fshy.ajam.dev/api/v1/entity/storacha.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Storacha (successor to web3.storage)

- `storage/storacha` | dead | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:22.713Z (live) | stale on 2026-12-04
- url https://storacha.network
- free tier: No longer offered. The developer upload and IPFS service was shut down. Was 5 GB free at launch (2025-05); the old web3.storage 1 TB free plan did not survive into Storacha. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A. Service closed. w3s.link, the Storacha/web3.storage gateway, now 301-redirects to dweb.link, which returns 429 with Retry-After: 900. | metered: no
- identity: email
- interface: rest, cli
- limits note: Service wound down; users told to migrate 'by the end of May' (2026).
- interface detail: rest
- tooling: Previously @storacha/client, UCAN-based; CLI 'w3'. Repos remain but the hosted service is gone.
- composes with: None. Dead.
- reliability: Data-loss event, not a throttle: the team joined Filecoin Foundation and the upload service shut down. The successor for the same shape is Fil One (S3, 1 TB free for 30 days = trial) and Filecoin Onchain Cloud / Filecoin Pin (paid per TiB).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: No longer offered — the developer upload and IPFS service was shut down. Was 5 GB free at launch (2025-05); the old web3.storage 1 TB free plan did not survive into Storacha.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: (2026-04-03) — 'The Storacha developer upload and IPFS service, however, will be shutting down.' 'you will have to move it — by the end of May at the very latest.'
  - [2] 2026-10-21: (2025-05-27) — 'You can get started with 5GB for free!'
  - [3] 2026-10-21: probe: GET -> 301 Location: https://dweb.link/... -> 429 Retry-After 900
  - [1] 2026-11-19: the first-party notice still states that the developer upload and IPFS service is shutting down | capture: sha256:4edb946f2b3f1a6a98e3d7280fdde68e0c6bb478415540765f7a191570f9ddf1 | quote: The Storacha developer upload and IPFS service, however, will be shutting down.
  - [1] 2026-11-19: first-party notice sets a final gateway cutoff of 2026-05-31, already past | capture: sha256:4edb946f2b3f1a6a98e3d7280fdde68e0c6bb478415540765f7a191570f9ddf1 | quote: May 31, 2026: The Storacha gateways (w3s.link) will stop serving content. Uploaded data will no longer be accessible through Storacha.
- sources:
  - [1] https://medium.com/@storacha/an-update-on-storacha-and-important-news-for-you-and-your-data-15a5d10b7da0
  - [2] https://medium.com/@storacha/you-can-get-started-with-5gb-for-free-e7d456c73729
  - [3] https://w3s.link/ipfs/bafybei...5u4
