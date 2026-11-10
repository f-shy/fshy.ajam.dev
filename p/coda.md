# Coda

> coda.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coda/ | JSON https://fshy.ajam.dev/api/v1/entity/coda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Coda / Superhuman Docs (free plan) - attachments

- `storage/coda-superhuman-docs-attachments` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://coda.io
- free tier: 1 GB of attachments per doc on Free, 10 MB per individual attachment, with no cap on the number of personal docs or their objects | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; attachments served from Coda's CDN with signed URLs | metered: no
- identity: institution
- interface: rest
- limits note: 1 GB per doc total attachments; 10 MB per single attachment; docs over 125 MB lose the API and break cross-doc sync; shared docs on Free limited to 50 objects and 1,000 rows (so the docs must stay unshared to stay unlimited); 35 time-based automations/month
- interface detail: rest
- tooling: Coda REST API (docs/tables/rows) can create rows with attachment values by URL; API is size-gated at 125 MB doc size
- composes with: Per-record unlimited: 1 GB x unlimited personal docs x unlimited free workspaces. Personal (unshared) docs on Free have 'no object or row limits', so the 1 GB/doc is the only ceiling - 1,000 docs = 1 TB in one free account.
- reliability: Sharing a doc flips it into the 50-object / 1,000-row regime and can lock it read-only after a 14-day grace period - the unlimited mode is strictly the unshared mode, which also kills public download links.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Per-doc file limits (the amount of total attachments in a doc): Free plan: 1 GB per doc'; 'Individual file size limit: Free plan: 10 MB per attachment'
  - [2] 2026-10-21: 'Personal docs, or docs that aren't shared with anyone, have no object or row limits'; 'Shared docs... up to 50 objects... and up to 1000 table rows per doc'
- sources:
  - [1] https://help.coda.io/hc/en-us/articles/39555760015757-Overview-Doc-limits
  - [2] https://help.coda.io/hc/en-us/articles/39555798022797-Doc-limits-on-Free-plan
