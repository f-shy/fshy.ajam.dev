# pinecast

> pinecast.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pinecast/ | JSON https://fshy.ajam.dev/api/v1/entity/pinecast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pinecast — free (demo) plan

- `storage/pinecast-free-plan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.981Z (live) | stale on 2026-12-04
- url https://help.pinecast.com/article/135-whats-included-with-the-free-plan
- free tier: none reachable: 48 MB per episode and only the ten most recent episodes per podcast stay available. Free forever with unlimited uploads, but the ten-episode visibility window makes it useless as storage.… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 48 MB per episode and only the ten most recent episodes per podcast stay available. Free forever with unlimited uploads, but the ten-episode visibility window makes it useless as storage.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 48 MB per episode and only the ten most recent episodes per podcast stay available. Free forever with unlimited uploads, but the ten-episode visibility window makes it useless as storage.…
  - [2] 2026-10-21: cited as the basis of the rejection: 48 MB per episode and only the ten most recent episodes per podcast stay available. Free forever with unlimited uploads, but the ten-episode visibility window makes it useless as storage. Pa
  - [1] 2026-11-19: free plan caps each episode at 48MB | capture: sha256:4ef8c6d9ac9ec2c1559604de2108aef973c3b58bb808932c906e6a6a14674efa | quote: Upload episodes up to 48MB.
  - [1] 2026-11-19: only the ten most recent episodes stay available, a visibility window | capture: sha256:4ef8c6d9ac9ec2c1559604de2108aef973c3b58bb808932c906e6a6a14674efa | quote: Free forever, with unlimited uploads. Only the ten most recent episodes per podcast are available.
- sources:
  - [1] https://help.pinecast.com/article/135-whats-included-with-the-free-plan
  - [2] https://help.pinecast.com/article/166-service-limits
