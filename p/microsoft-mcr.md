# microsoft mcr

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/microsoft-mcr/ | JSON https://fshy.ajam.dev/api/v1/entity/microsoft-mcr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## microsoft mcr / registry.k8s.io / icr.io / docker.elastic.co / registry.ope

- `storage/microsoft-mcr-registry-k8s-io-icr-io-docker-elastic-co-r` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- page https://fshy.ajam.dev/p/microsoft-mcr.md
- free tier: none reachable: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 (length… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not recorded | note: not applicable
- retention: not recorded
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
  - dead_end.why: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 (length…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All are read-only or reject auth-less writes. Probed anonymously: mcr.microsoft.com and registry.opensuse.org answer /v2/ with 200 but an anonymous POST blobs/uploads returns 411 length…
