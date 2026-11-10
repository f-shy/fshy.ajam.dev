# Framagit

> framagit.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/framagit/ | JSON https://fshy.ajam.dev/api/v1/entity/framagit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Framagit (framagit.org) - Framasoft's GitLab

- `storage/framagit-framasoft-s-gitlab` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://framagit.org
- free tier: No published total quota. Per-object table is published and slightly tighter than Salsa: max attachment 12 MiB, import 300 MiB, job artifact 250 MiB, page 250 MiB, snippet 50 MiB, import remote file 10 GiB, download file 5 GiB. Registry: Conan 3 GiB, Maven 3 GiB, PyPI 3 GiB, Terraform 1 GiB, npm/NuGet 500 MiB, Helm 5 MiB. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 250 MiB | bytes: 262144000 | source: [1] | note: not stated
- retention: per-object-cap: 250 MiB CI artifacts (vs Salsa's 750 MiB), 5 GiB download file. retention: indefinite for published projects | source: [1] | note: not stated
- egress: Free; Framasoft-funded, no billing, downloads served from the instance. | metered: no
- identity: institution
- interface: ssh, git, rclone
- limits:
  - per-object-cap (binding): per-object-cap: 250 MiB [1]
- limits note: per-object-cap: 250 MiB CI artifacts (vs Salsa's 750 MiB), 5 GiB download file. retention: indefinite for published projects. request-rate: not published on the page read.
- interface detail: git
- tooling: Standard GitLab: git over SSH/HTTPS, Generic Package API, CI. No rclone backend.
- composes with: unlimited projects x 5 GiB/download file (and 3 GiB per registry artifact) x unlimited versions. Same shape as Salsa with a lower artifact ceiling.
- reliability: Registration sits behind an Anubis proof-of-work wall ('Making sure you're not a bot!', Anubis v1.28.2, modified by Framasoft) - so signup is not scriptable at all, which is a stronger anti-farming gate than Salsa's human queue. The instance-configuration page itself was readable, so limits are auditable; only signup is walled.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '## Size Limits ... Maximum attachment size | 12 MiB ... Maximum job artifact size | 250 MiB'; 'Generic | 5 GiB' style registry table
  - [2] 2026-10-21: Anubis challenge: 'Making sure you're not a bot! ... Protected by Anubis'
  - [3] 2026-10-21: probe: GET -> 401 (API present, auth required)
- sources:
  - [1] https://framagit.org/help/instance_configuration
  - [2] https://framagit.org/users/sign_up
  - [3] https://framagit.org/api/v4/version
