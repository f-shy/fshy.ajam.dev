# anaconda.org free plan

> continuumio-docs.readthedocs-hosted.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/continuumio-docs/ | JSON https://fshy.ajam.dev/api/v1/entity/continuumio-docs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## anaconda.org free plan

- `storage/anaconda-org-free-plan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:54.754Z (live) | stale on 2026-12-04
- url https://continuumio-docs.readthedocs-hosted.com/anacondaorg/faq/
- free tier: none reachable: 3 GB total per account; would need ~6,800 accounts for 20 TiB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Anaconda.org FAQ page | source: [1] | note: not applicable
- retention: not stated on the Anaconda.org FAQ page | source: [1]
- egress: not stated on the Anaconda.org FAQ page | metered: no
- identity: email
- interface: browser
- interface detail: Packages are uploaded to Anaconda.org as tar.bz2 or .conda files.
- tooling: not documented
- composes with: Hosts public conda/Python packages for download by others; not stated on the FAQ as chaining to other storage services.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 3 GB total per account; would need ~6,800 accounts for 20 TiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 3 GB total per account; would need ~6,800 accounts for 20 TiB.
  - [1] 2026-11-19: the anaconda.org free plan still provides 3 GB for public packages only | capture: sha256:d569f7f99a5fe9bc7acf74feb1b1acbd7b31db15ad244a945b4b0b9e2d4556b3 | quote: The free plan allows you to search for, create and host public packages, and provides up to 3 GB storage space.
  - [1] 2026-11-19: packages are uploaded to Anaconda.org as tar.bz2 or .conda files | capture: sha256:d569f7f99a5fe9bc7acf74feb1b1acbd7b31db15ad244a945b4b0b9e2d4556b3 | quote: Both `tar.bz2` and `.conda` compression files can be uploaded to Anaconda.org.
- sources:
  - [1] https://continuumio-docs.readthedocs-hosted.com/anacondaorg/faq/
