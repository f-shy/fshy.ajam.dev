# bioconductor

> bioconductor.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bioconductor/ | JSON https://fshy.ajam.dev/api/v1/entity/bioconductor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bioconductor

- `storage/bioconductor` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.621Z (live) | stale on 2026-12-04
- url https://contributions.bioconductor.org/general.html
- free tier: none reachable: Hard 5 MB per individual file even after acceptance, and 10 MB per source package. 'individual files must be <= 5MB. This restriction exists even after the package is accepted.' | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: individual files must be <= 5MB | source: [1] | note: 5MB per-file ceiling; source package under 10 MB
- retention: not stated on the Bioconductor package development page | source: [1] | note: not stated on the Bioconductor package development page
- egress: not stated on the Bioconductor package development page | metered: no
- identity: email
- interface: git, cli
- interface detail: source packages submitted through git and built with R CMD build
- tooling: R CMD build and BiocCheck for package submission
- composes with: packages are reviewed and added to the Bioconductor repository
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Hard 5 MB per individual file even after acceptance, and 10 MB per source package. 'individual files must be <= 5MB. This restriction exists even after the package is accepted.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard 5 MB per individual file even after acceptance, and 10 MB per source package. 'individual files must be <= 5MB. This restriction exists even after the package is accepted.'
  - [1] 2026-11-19: individual package files are capped at 5 MB even after acceptance | capture: sha256:4a575873d1231de0c4e765b916e0166566894b2262231c08b7c4bdd3afda09d6 | quote: For software packages, individual files must be <= 5MB. This restriction exists even after the package is accepted and added to the
  - [1] 2026-11-19: source packages are capped at 10 MB | capture: sha256:4a575873d1231de0c4e765b916e0166566894b2262231c08b7c4bdd3afda09d6 | quote: The source package resulting from running `R CMD build` should occupy less than 10 MB on disk.
  - [1] 2026-11-19: packages are submitted through git and built with R CMD build | capture: sha256:4a575873d1231de0c4e765b916e0166566894b2262231c08b7c4bdd3afda09d6 | quote: should not be committed to git
  - [1] 2026-11-19: BiocCheck and R CMD build are the submission tools | capture: sha256:4a575873d1231de0c4e765b916e0166566894b2262231c08b7c4bdd3afda09d6 | quote: Packages must also pass `BiocCheck::BiocCheckGitClone()` and `BiocCheck::BiocCheck('new-package'=TRUE)` with no errors and no warnings.
- sources:
  - [1] https://contributions.bioconductor.org/general.html
