# Heyzine

> heyzine.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heyzine/ | JSON https://fshy.ajam.dev/api/v1/entity/heyzine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Heyzine

- `storage/heyzine` | fails-quota | evidence reported | binding none | category document-hosting
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://heyzine.com
- free tier: Free Basic: 5 flipbooks, unlimited pages, 1 GB storage, 1 user, no watermark, API access included. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unlimited visits, no ads, no watermark on free; offline download of the flipbook HTML is offered ("download the html to host it yourself"). | metered: no
- identity: institution
- interface: rest
- limits note: 1 GB total disk per account; 5 flipbooks on free; PDF is converted to page assets rather than stored byte-for-byte; over-quota accounts get 'old flipbooks auto removal'.
- interface detail: rest
- tooling: Real documented API + MCP server: create/list/delete flipbooks, access lists, embed codes, webhooks; API key via 'Authorization: Bearer'. Third-party python libs exist but nothing first-party for bulk sync.
- composes with: 1 GB/account x unlimited free accounts; the API means it is automatable, but 1 GB units mean 1 TiB == 1,024 accounts and 10 TiB == 10,240. Only interesting as a serving front, not as bulk storage.
- reliability: Over-quota accounts are subject to automatic deletion of old flipbooks, and free accounts hold only 5 publications.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free Basic: 5 flipbooks, unlimited pages, 1 GB storage, 1 user, no watermark, API access included.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Basic Free - 5 free flipbooks - Unlimited pages - Unlimited visits - No ads - API access - 1GB storage'
  - [2] 2026-10-21: 'the total disk space of your flipbooks and assets can't exceed your user's disk space'; auto-removal of old flipbooks when over quota
  - [3] 2026-10-21: API: create/list/delete flipbooks, 'Authorization: Bearer API_KEY'
- sources:
  - [1] https://heyzine.com/
  - [2] https://heyzine.com/faq
  - [3] https://heyzine.com/developers
