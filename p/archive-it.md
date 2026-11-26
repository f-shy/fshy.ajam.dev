# archive-it

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive-it/ | JSON https://fshy.ajam.dev/api/v1/entity/archive-it.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## archive-it

- `storage/archive-it` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.371Z (live) | stale on 2026-12-04
- url https://help.archive.org/help/save-pages-in-the-wayback-machine/
- free tier: none reachable: Paid subscription crawler, not free storage; only appeared because it shares the Wayback infrastructure. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the help page states no per-object size cap | source: [1] | note: not applicable
- retention: Saved pages continue to exist even after the original page changes or is removed from the web; no numeric retention period is stated. | source: [1]
- egress: stated-absent: the help page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the help page describes a subscription crawling service run for the subscriber and states no client interface or API
- tooling: not documented
- composes with: stated-absent: the help page states no way to chain the crawling service into a general byte store; it deposits crawled results in the Wayback Machine
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Paid subscription crawler, not free storage; only appeared because it shares the Wayback infrastructure.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Paid subscription crawler, not free storage; only appeared because it shares the Wayback infrastructure.
  - [1] 2026-11-19: Archive-It is a paid subscription, not free storage | capture: sha256:5ddd318dd103ed8d27537dd433e54013168a95bcd9999a5131c8199d845c02af | quote: Archive-It is a paid subscription service with technical and web archivist support.
  - [1] 2026-11-19: the first-party help page states that saved pages persist, without a numeric retention period | capture: sha256:5ddd318dd103ed8d27537dd433e54013168a95bcd9999a5131c8199d845c02af | quote: These saved pages can be cited, shared, linked to
  - [1] 2026-11-19: the service is a managed crawler depositing into the Wayback Machine, with no byte-store chaining stated | capture: sha256:5ddd318dd103ed8d27537dd433e54013168a95bcd9999a5131c8199d845c02af | quote: Tell us what to crawl and how often to crawl it, and we execute the crawl and put the results in the Wayback Machine.
  - [1] 2026-11-19: the page describes single-page saves and states no egress allowance | capture: sha256:5ddd318dd103ed8d27537dd433e54013168a95bcd9999a5131c8199d845c02af | quote: it only saves one page at a time
- sources:
  - [1] https://help.archive.org/help/save-pages-in-the-wayback-machine/
