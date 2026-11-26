# solcloud

> solcloud.fun | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/solcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/solcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## solcloud (solana p2p)

- `storage/solcloud` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.378Z (inherited) | stale on 2026-12-04
- url https://solcloud.fun/
- free tier: none reachable: Landing page only; storage is explicitly paid per-upload in SOL ('Pay small fees in SOL tokens to store your memories'). No free quota stated anywhere on the page. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Landing page only; storage is explicitly paid per-upload in SOL ('Pay small fees in SOL tokens to store your memories'). No free quota stated anywhere on the page.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Landing page only; storage is explicitly paid per-upload in SOL ('Pay small fees in SOL tokens to store your memories'). No free quota stated anywhere on the page.
  - probe:https://solcloud.fun/ 2026-11-19: the solcloud.fun host no longer serves the storage service | capture: sha256:2a3a28951d5ad48ee8c6bf8ae5bf9667f11e452837ed6c6de3c9d889d05622d7 | quote: Domain registration has expired.
  - probe:https://solcloud.fun/ 2026-11-19: the solcloud.fun host now serves a domain-parking page instead of the storage service | capture: sha256:2a3a28951d5ad48ee8c6bf8ae5bf9667f11e452837ed6c6de3c9d889d05622d7 | quote: Domain registration has expired.
- sources:
  - [1] https://solcloud.fun/
