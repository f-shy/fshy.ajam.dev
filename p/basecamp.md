# basecamp

> basecamp.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/basecamp/ | JSON https://fshy.ajam.dev/api/v1/entity/basecamp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## basecamp (free / paid)

- `storage/basecamp` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:56.870Z (live) | stale on 2026-12-04
- url https://basecamp.com/pricing
- free tier: none reachable: Free is 1 GB and 1 project, 3 users. Paid tops out at 1 TB for $199/mo. No free path to bulk and no API for arbitrary binaries. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the Basecamp pricing page states plan storage totals (1 GB free, up to 1 TB paid) but no per-file size cap. | source: [1] | note: not applicable
- retention: stated-absent: the Basecamp pricing page states storage quotas and account cancellation terms but no retention term for individual stored files. | source: [1]
- egress: stated-absent: the Basecamp pricing page states no egress, download or transfer-out price; it describes file storage quotas and AI connectors. | metered: no
- identity: email
- interface: browser
- interface detail: Basecamp stores assets through its Docs & Files web feature and offers AI-agent CLI and MCP connectors; no general file-storage API is stated. "Bring your own AI agents" and "CLI access and skills for AI agents you run on your computer" describe agent access, not a byte-store interface.
- tooling: not documented
- composes with: Basecamp offers "Official Basecamp support for ChatGPT, Claude, and AI agents with full MCP support." Files are stored in its Docs & Files feature; no general programmatic storage chaining is stated.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Free is 1 GB and 1 project, 3 users. Paid tops out at 1 TB for $199/mo. No free path to bulk and no API for arbitrary binaries.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free is 1 GB and 1 project, 3 users. Paid tops out at 1 TB for $199/mo. No free path to bulk and no API for arbitrary binaries.
  - [1] 2026-11-19: the free plan is still one project for up to 3 people, with no bulk-storage path | capture: sha256:69537cf8627e3f255ac97bdede18b3560e8e467d221d527b10e2d4eae5c38d49 | quote: One project, free forever. Invite up to 3 people. Limited, but plenty.
  - [1] 2026-11-19: Basecamp stores assets as Docs & Files in the web application | capture: sha256:69537cf8627e3f255ac97bdede18b3560e8e467d221d527b10e2d4eae5c38d49 | quote: Docs & Files for storing assets
  - [1] 2026-11-19: the page describes account cancellation but no per-file retention term | capture: sha256:69537cf8627e3f255ac97bdede18b3560e8e467d221d527b10e2d4eae5c38d49 | quote: Yes, you can cancel any time, no questions asked, no forms to fill out, no person to talk to.
  - [1] 2026-11-19: the free Basecamp plan includes 1 GB of file storage | capture: sha256:69537cf8627e3f255ac97bdede18b3560e8e467d221d527b10e2d4eae5c38d49 | quote: 1 GB storage space
  - [1] 2026-11-19: Basecamp chains with AI agents over MCP | capture: sha256:69537cf8627e3f255ac97bdede18b3560e8e467d221d527b10e2d4eae5c38d49 | quote: Official Basecamp support for ChatGPT, Claude, and AI agents with full MCP support.
- sources:
  - [1] https://basecamp.com/pricing
