# registrish

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-jpetazzo/ | JSON https://fshy.ajam.dev/api/v1/entity/github-jpetazzo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## registrish (jpetazzo) and static-container-registry

- `storage/registrish-and-static-container-registry` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/jpetazzo/registrish
- free tier: None reachable: Not a provider. A trick for serving a read-only registry off static hosting. Interesting as an amplifier (point it at a free static host to get registry-shaped URLs), but it stores nothing. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not a provider — a trick for serving a read-only registry off static hosting. Interesting as an amplifier (point it at a free static host to get registry-shaped URLs), but it stores nothing
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Not a provider — a trick for serving a read-only registry off static hosting. Interesting as an amplifier (point it at a free static host to get registry-shaped URLs), but it stores nothing
- sources:
  - [1] https://github.com/jpetazzo/registrish
