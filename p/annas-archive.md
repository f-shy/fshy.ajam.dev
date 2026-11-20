# anna's archive

> annas-archive.gd | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/annas-archive/ | JSON https://fshy.ajam.dev/api/v1/entity/annas-archive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## anna's archive

- `storage/anna-s-archive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:54.755Z (live) | stale on 2026-12-04
- url https://annas-archive.gd/faq
- free tier: None reachable: No upload endpoint of its own. It is an index. Its FAQ routes uploads to Z-Library / Libgen.li and only takes >10,000-file dumps by email contact; its own 'datasets' are torrents of metadat. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Anna's Archive FAQ page | source: [1] | note: not applicable
- retention: not stated on the Anna's Archive FAQ page | source: [1]
- egress: not stated on the Anna's Archive FAQ page | metered: no
- identity: email
- interface: browser, nntp
- interface detail: A search/index website; uploads are redirected to Z-Library and Libgen.li and data is distributed through torrents.
- tooling: not documented
- composes with: Chains to Z-Library and Libgen.li for uploads and distributes its own data through torrents; it holds no upload endpoint of its own.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No upload endpoint of its own — it is an index. Its FAQ routes uploads to Z-Library / Libgen.li and only takes >10,000-file dumps by email contact; its own 'datasets' are torrents of…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No upload endpoint of its own — it is an index. Its FAQ routes uploads to Z-Library / Libgen.li and only takes >10,000-file dumps by email contact; its own 'datasets' are torrents of…
  - [2] 2026-10-21: cited as the basis of the rejection: No upload endpoint of its own — it is an index. Its FAQ routes uploads to Z-Library / Libgen.li and only takes >10,000-file dumps by email contact; its own 'datasets' are torrents of metadat
  - [1] 2026-11-19: the first-party FAQ still routes small uploads to Z-Library and Libgen.li rather than hosting them | capture: sha256:72e68cdc2046929e816661802a5e8b6dc3d091c6b1fc5689ebb8dd4883180154 | quote: For small uploads (up to 10,000 files) please upload them to both Z-Library and Libgen.li.
  - [1] 2026-11-19: large uploads go by email contact, not a self-service endpoint, so the quota rejection stands | capture: sha256:72e68cdc2046929e816661802a5e8b6dc3d091c6b1fc5689ebb8dd4883180154 | quote: For large uploads (over 10,000 files) that don’t get accepted by Libgen or Z-Library, please contact us at Contact email.
  - [1] 2026-11-19: the FAQ describes a search/index service and states no per-object cap, egress price or retention period for uploads | capture: sha256:72e68cdc2046929e816661802a5e8b6dc3d091c6b1fc5689ebb8dd4883180154 | quote: With this search engine, we build on the shoulders of giants.
  - [1] 2026-11-19: large uploads are handled by email contact, not a self-service upload endpoint | capture: sha256:72e68cdc2046929e816661802a5e8b6dc3d091c6b1fc5689ebb8dd4883180154 | quote: For large uploads (over 10,000 files) that don't get accepted by Libgen or Z-Library, please contact us at Contact email.
- sources:
  - [1] https://annas-archive.gd/faq
  - [2] https://annas-archive.is/uploads
