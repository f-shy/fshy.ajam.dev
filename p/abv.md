# abv.bg free

> abv.bg | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abv/ | JSON https://fshy.ajam.dev/api/v1/entity/abv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## abv.bg free

- `storage/abv-bg-free` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.936Z (live) | stale on 2026-12-04
- url https://blog.abv.bg/
- free tier: none reachable: the first-party blog front page was read on 2026-11-19 through pinned providers and no longer carries the former mailbox-plus-netdisk quota sentence; that quota is unverified: no longer stated on the page reached. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the first-party page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the first-party page states no retention period for stored bytes | source: [1]
- egress: stated-absent: the first-party page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party blog is about e-mail account security and states no storage client interface
- tooling: not documented
- composes with: stated-absent: the first-party page states no way to chain byte storage with other services
- reliability: Blog states the quota evolution 6 GB -> 10 GB (7 GB mailbox + 3 GB drive), and the live IMAP port did not complete a CAPABILITY handshake. Under threshold regardless.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Blog states the quota evolution 6 GB -> 10 GB (7 GB mailbox + 3 GB drive), and the live IMAP port did not complete a CAPABILITY handshake. Under threshold regardless.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Blog states the quota evolution 6 GB -> 10 GB (7 GB mailbox + 3 GB drive), and the live IMAP port did not complete a CAPABILITY handshake. Under threshold regardless.
  - [1] 2026-11-19: the first-party blog front page is reachable through a pinned provider but no longer carries the quota sentence | capture: sha256:d33d800b10cf85f11e504573da8d9dfd01151ad162e48d128432399093999128 | quote: Грижата за сигурността на електронната поща не се изчерпва със силната парола.
- sources:
  - [1] https://blog.abv.bg/
