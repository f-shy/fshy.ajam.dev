# transferrocket

> transferrocket.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transferrocket/ | JSON https://fshy.ajam.dev/api/v1/entity/transferrocket.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## transferrocket

- `storage/transferrocket` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.962Z (live) | stale on 2026-11-19
- url https://www.transferrocket.io/
- free tier: transfers up to 5 GB and up to 7 days of storage are free, no account required; larger or longer transfers are priced per transfer | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: No download allowance or per-download price is stated on the pages read: pricing is per transfer by file size and storage duration. Transfers up to 5 GB are free with no daily aggregate cap and no account required; larger transfers cost a one-time fee calculated before the transfer. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free: transfers up to 5 GB, stored up to 7 days, no account, no daily aggregate cap. Larger or longer transfers are priced per transfer by file size and duration. No download cap or per-download price is stated on the pages read.
- notes: the same as reliability
- evidence note: read 2026-11-03: https://www.transferrocket.io/pricing (up to 5 GB free, up to 7 days free), https://www.transferrocket.io/transferxl-alternative (no daily aggregate cap) and https://www.transferrocket.io/ (no account required); the paid-transfer prices behind fails-quota carry the 2026-10-21 evidence rows only.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free is 5 GB transfer AND 7 days storage, both as hard pay-per-use boundaries ('Transfers up to 5 GB are free', 'Transfers up to 7 days are free') — the product is metered from the first…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free is 5 GB transfer AND 7 days storage, both as hard pay-per-use boundaries ('Transfers up to 5 GB are free', 'Transfers up to 7 days are free') — the product is metered from the first…
  - [2] 2026-11-03: free transfers up to 5 GB have no daily aggregate cap | capture: sha256:b795e6c598af62c05895900c545c76819d2d7542d435cc3acd952127c0bb7633 | quote: Transfers up to 5 GB are free, with no daily aggregate cap.
  - [3] 2026-11-03: transfers up to 5 GB are free | capture: sha256:bc7f04dd4420b1104889e04c75e2c082310e6210115a9c62352e8fb097ce7781 | quote: Dynamic pricing based on file size* - Up to 5 GB Free
  - [3] 2026-11-03: storage up to 7 days is free | capture: sha256:bc7f04dd4420b1104889e04c75e2c082310e6210115a9c62352e8fb097ce7781 | quote: Dynamic pricing based on duration* - Up to 7 days Free
  - [1] 2026-11-03: no account is required | capture: sha256:5e387ecae2cc500bdb171aff7a5826628bfab46e10d73ea76bedef1edd790ce3 | quote: No account required
  - [1] 2026-11-03: transfers up to 5 GB are free | capture: sha256:5e387ecae2cc500bdb171aff7a5826628bfab46e10d73ea76bedef1edd790ce3 | quote: Transfers up to 5 GB are free!
  - [3] 2026-11-04: transfers up to 5 GB are free | capture: sha256:bc7f04dd4420b1104889e04c75e2c082310e6210115a9c62352e8fb097ce7781 | quote: Dynamic pricing based on file size* - Up to 5 GB Free
- sources:
  - [1] https://www.transferrocket.io/
  - [2] https://www.transferrocket.io/transferxl-alternative
  - [3] https://www.transferrocket.io/pricing
