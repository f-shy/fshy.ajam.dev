# Fedora COPR

> copr.fedorainfracloud.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/copr/ | JSON https://fshy.ajam.dev/api/v1/entity/copr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fedora COPR (copr.fedorainfracloud.org)

- `storage/fedora-copr` | qualifies-with-caveat | evidence reported | binding retention-clamped | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:14.807Z (live) | stale on 2026-11-25
- url https://copr.fedorainfracloud.org
- free tier: We keep one build for each package in one project indefinitely. All other builds (old packages, failed builds) are deleted after 14 days. | unit: unlimited | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: source: [2] | note: not stated
- retention: We keep one build for each package in one project indefinitely. All other builds (old packages, failed builds) are deleted after 14 days. | days: 14 | source: [1] | note: not stated
- egress: Free. Results are served from copr-be.cloud.fedoraproject.org and the Fedora CDN; there is no billing or bandwidth meter anywhere in COPR. | metered: no
- identity: email
- interface: rest, rclone, cli
- limits:
  - retention-clamped (binding): deleted after 14 days [2]
  - retention-clamped (binding): retention: 14 days [2]
- limits note: retention: 14 days for all but the newest build of each package (Pulp backend exception: count-based - keeps the 5 most recent successful builds per package, and 'the 14-day preservation period is not guaranteed'). per-object-cap: src.rpm upload is the write path; no published byte limit found. request-rate: not documented. Build timeout default 5 h, max 50 h. Projects that opted into manual repository creation are exempt from the old package removal.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: `copr-cli` (create/build/upload), `copr` Python API v3 with Swagger at /api_3/docs/, and plain HTTPS dnf repo access. `copr-cli buildscm`, `copr-cli add-package-*`. No rclone backend.
- composes with: unlimited COPR projects x unlimited packages per project x (one retained build each, indefinitely). Because retention is per RPM Name within a repository, the documented route is: 'Create a separate Copr project for each version' - and the pruner explicitly only groups by RPM Name, so distinct Name: values (golang1.24 / golang1.25 / golang1.26 are named as the alternative route) each keep their own build forever. That is an unlimited-cardinality, indefinite-retention store, and each further Fedora account carries the same allowance again.
- reliability: The 14-day pruner is the whole story: anything but the newest build of a package evaporates, and on the Pulp backend it is even stricter (keeps only 5, time-based guarantee dropped). Copr is a build service - content must arrive as a buildable src.rpm, so arbitrary files require wrapping in a spec with %install/%files. The retention mechanics above are the new detail.
- notes: the same as the free tier
- evidence note: the cited page was read on 2026-11-09
- evidence:
  - [3] 2026-10-21: lines 1026-1027 - 'We keep one build for each package in one project indefinitely. All other builds (old packages, failed builds) are deleted after 14 days.'
  - withheld 2026-10-21: same file lines 1067-1069 - Pulp backend: 'retention is count-based: Copr keeps the 5 most recent successful builds ... the 14-day preservation period is not guaranteed'
  - withheld 2026-10-21: same file lines 1057-1063 - 'Create a separate Copr project for each version' (the multiplication path)
  - [4] 2026-10-21: probe: GET -> 301 (CDN redirect, repo live)
  - [1] 2026-11-09: one build per package in a project is kept indefinitely and all other builds are deleted after 14 days | capture: sha256:93dbaca2f42a1c722d9c128221c6e2177c0673b75fced69996b1efd946379047 | quote: We keep one build for each package in one project indefinitely. All other builds (old packages, failed builds) are deleted after 14 days.
- sources:
  - [1] https://docs.copr.fedorainfracloud.org/user_documentation.html
  - [2] https://docs.copr.fedorainfracloud.org/user_documentation/
  - [3] https://raw.githubusercontent.com/fedora-copr/copr/main/doc/user_documentation.rst
  - [4] https://copr-be.cloud.fedoraproject.org/results/@copr/PyPI/fedora-40-x86_64/repodata/repomd.xml
