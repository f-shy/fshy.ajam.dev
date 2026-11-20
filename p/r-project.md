# cran

> r-project.org | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/r-project/ | JSON https://fshy.ajam.dev/api/v1/entity/r-project.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cran

- `storage/cran-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:10.068Z (live) | stale on 2026-12-04
- url https://cran.r-project.org/web/packages/policies.html
- free tier: none reachable: 10 MB soft cap on source tarballs, 5 MB for data; policy explicitly rejects using packages to distribute bulk content. Human review. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: 10 MB soft cap on source tarballs, 5 MB for data; policy explicitly rejects using packages to distribute bulk content. Human review.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 10 MB soft cap on source tarballs, 5 MB for data; policy explicitly rejects using packages to distribute bulk content. Human review.
  - [1] 2026-11-19: CRAN policy caps data and documentation at 5 MB and rejects bulk distribution | capture: sha256:2085faa086794ece2378ac4eef0bf01359aff59545c717d5559afddca39b11fa | quote: As a general rule, neither data nor documentation should exceed 5MB (which covers several books). A CRAN package is not an appropriate way to distribute course notes, and authors will be asked to trim their documentation to a maximum of 5MB.
- sources:
  - [1] https://cran.r-project.org/web/packages/policies.html

## CRAN (Comprehensive R Archive Network)

- `storage/cran` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:10.068Z (live) | stale on 2026-12-04
- url https://cran.r-project.org
- free tier: Deliberately tiny, by policy. CRAN policy: 'As a general rule, neither data nor documentation should exceed 5MB ... Source package tarballs should if possible not exceed 10MB.' Larger tarballs need a individually-granted exception ('a modestly increased limit can be requested at submission'). | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 10 MB | bytes: 10000000 | source: [1] | note: not stated
- retention: per-object-cap: 10 MB source tarball (soft, 5 MB for data/doc). retention: indefinite per version, old versions archived | source: [1] | note: not stated
- egress: Free and globally mirrored (hundreds of CRAN mirrors). No metering. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - write-gated: reviewed [1]
  - write-gated: review make this unusable for bulk [1]
  - per-object-cap (binding): per-object-cap: 10 MB [1]
- limits note: per-object-cap: 10 MB source tarball (soft, 5 MB for data/doc). retention: indefinite per version, old versions archived. request-rate: submission is manual/email-reviewed.
- interface detail: rest
- tooling: `R CMD build` + `devtools::submit_cran`, `rhub`; mirrored tarballs at /src/contrib/. No rclone backend.
- composes with: unlimited packages x unlimited versions x 10 MB. CRAN is explicitly hostile to bulk data: 'A CRAN package is not an appropriate way to distribute course notes'. Human review on every submission.
- reliability: 10 MB per version and human review make this unusable for bulk; recorded so nobody re-checks it.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Deliberately tiny, by policy. CRAN policy: 'As a general rule, neither data nor documentation should exceed 5MB ... Source package tarballs should if possible not exceed 10MB.' Larger tarballs need a individually-granted exception ('a modestly increased limit can be requested at submission').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'As a general rule, neither data nor documentation should exceed 5MB ... Source package tarballs should if possible not exceed 10MB.'
  - [2] 2026-10-21: probe: GET -> 200, 2,527,103 bytes; ranged GET bytes 0-999 -> 206 (ranges honoured)
  - [1] 2026-11-19: CRAN policy caps data and documentation at 5 MB and rejects bulk course-note distribution | capture: sha256:2085faa086794ece2378ac4eef0bf01359aff59545c717d5559afddca39b11fa | quote: As a general rule, neither data nor documentation should exceed 5MB (which covers several books). A CRAN package is not an appropriate way to distribute course notes, and authors will be asked to trim their documentation to a maximum of 5MB.
  - [1] 2026-11-19: CRAN policy sets a 10 MB source tarball size limit | capture: sha256:2085faa086794ece2378ac4eef0bf01359aff59545c717d5559afddca39b11fa | quote: Source package tarballs should if possible not exceed 10MB.
- sources:
  - [1] https://cran.r-project.org/web/packages/policies.html
  - [2] https://cran.r-project.org/src/contrib/Matrix_1.7-6.tar.gz

## cran (r)

- `storage/cran-3` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:10.068Z (live) | stale on 2026-12-04
- url https://cran.r-project.org/web/packages/policies.html
- free tier: none reachable: Policy explicitly caps and actively polices size: 'neither data nor documentation should exceed 5MB ... authors will be asked to trim their documentation to a maximum of 5MB' and 'Source… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Policy explicitly caps and actively polices size: 'neither data nor documentation should exceed 5MB ... authors will be asked to trim their documentation to a maximum of 5MB' and 'Source…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Policy explicitly caps and actively polices size: 'neither data nor documentation should exceed 5MB ... authors will be asked to trim their documentation to a maximum of 5MB' and 'Source…
  - [1] 2026-11-19: CRAN trims documentation to a maximum of 5 MB and polices package size | capture: sha256:2085faa086794ece2378ac4eef0bf01359aff59545c717d5559afddca39b11fa | quote: As a general rule, neither data nor documentation should exceed 5MB (which covers several books). A CRAN package is not an appropriate way to distribute course notes, and authors will be asked to trim their documentation to a maximum of 5MB.
- sources:
  - [1] https://cran.r-project.org/web/packages/policies.html
