# ix.io

> ix.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ix-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ix-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ix.io

- `storage/ix-io` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:13.424Z (inherited) | stale on 2026-12-04
- url https://ix.io/
- free tier: None reachable: the root now serves a static maintenance page; the classic pastebin POST endpoint is gone. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Root returns 404 and POST returns 404. The classic ix.io pastebin endpoint is dead.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Root returns 404 and POST returns 404 — the classic ix.io pastebin endpoint is dead.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Root returns 404 and POST returns 404 — the classic ix.io pastebin endpoint is dead.
  - [2] 2026-10-21: cited as the basis of the rejection: Root returns 404 and POST returns 404 — the classic ix.io pastebin endpoint is dead.
  - probe:https://ix.io/ 2026-11-19: the root is a static maintenance page, so the classic pastebin endpoint is gone | capture: sha256:17a6c046ce28cc8885556d37d00ad47ed0e1db76fa91e91dfaad2fb96bf32330 | quote: ix.io is taking a break
  - probe:https://ix.io/ 2026-11-19: the endpoint no longer serves the pastebin, now a maintenance page | capture: sha256:17a6c046ce28cc8885556d37d00ad47ed0e1db76fa91e91dfaad2fb96bf32330 | quote: ix.io is taking a break
- sources:
  - [1] https://ix.io/
  - [2] https://ix.io
