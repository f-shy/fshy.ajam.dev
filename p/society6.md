# society6

> society6.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/society6/ | JSON https://fshy.ajam.dev/api/v1/entity/society6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## society6

- `storage/society6` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.376Z (live) | stale on 2026-12-04
- url https://help.society6.com/en-US/pixel-dimension-requirements-and-templates-for-all-society6-products-6266803
- free tier: none reachable: 150 MB limit, JPG/PNG only, print-resolution pipeline. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: the cited help article URL returned HTTP 404 on 2026-11-19; an archived copy of that page states the file size limit and the JPG or PNG file format.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 150 MB limit, JPG/PNG only, print-resolution pipeline.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 150 MB limit, JPG/PNG only, print-resolution pipeline.
  - [2] 2026-11-19: the pixel-dimension page states a 150mb file size limit for artwork | capture: sha256:e26b1115aea0b39563e56f3c216b629846e61aa9309c3df318c3df9074b4527a | quote: * File Size Limit: 150mb
  - probe:https://help.society6.com/en-US/pixel-dimension-requirements-and-templates-for-all-society6-products-6266803 2026-11-19: the cited help article URL returned HTTP 404 | capture: sha256:39c127cab398c1cbf5631ac0cad4c48e62d7a5c11377f2ac1264994c6f5062d0 | quote: "status": 404
- sources:
  - [1] https://help.society6.com/en-US/pixel-dimension-requirements-and-templates-for-all-society6-products-6266803
  - [2] https://web.archive.org/web/20260710234850/https://help.society6.com/en-US/pixel-dimension-requirements-and-templates-for-all-society6-products-6266803?provider=wayback
