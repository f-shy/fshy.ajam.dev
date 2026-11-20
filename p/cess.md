# cess deoss

> cess.cloud | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cess/ | JSON https://fshy.ajam.dev/api/v1/entity/cess.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cess deoss

- `storage/cess-deoss` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.547Z (inherited) | stale on 2026-12-04
- url https://deoss-sg.cess.cloud/health
- free tier: none reachable: Could not be probed alive: the documented endpoint does not resolve and the Cloudflare-fronted host returns 530. No quota page could be opened, so nothing to report. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Could not be probed alive: the documented endpoint does not resolve and the Cloudflare-fronted host returns 530. No quota page could be opened, so nothing to report.
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Could not be probed alive: the documented endpoint does not resolve and the Cloudflare-fronted host returns 530. No quota page could be opened, so nothing to report.
  - probe:https://deoss-sg.cess.cloud/health 2026-11-19: the documented DEOSS health endpoint does not resolve (name did not resolve) | capture: sha256:d98e6ea83fec7c20f1b6f5cff47e356ea59bfaa30dd36b830b0789d875cb5d0d | quote: "error": "transport"
- sources:
  - [1] https://deoss-sg.cess.cloud/health
