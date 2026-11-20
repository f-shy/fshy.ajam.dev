# atomgit

> atomgit.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/atomgit/ | JSON https://fshy.ajam.dev/api/v1/entity/atomgit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## atomgit (atomgit.com / docs.atomgit.com)

- `storage/atomgit` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:56.063Z (inherited) | stale on 2026-12-04
- url https://docs.atomgit.com/en/repo/capacity
- free tier: none reachable: 5 GB of LFS per repo. The capacity doc states it plainly: 'By default, a repository has 2GB Git storage space and 5GB LFS storage space', confirmed by a 2024 user write-up ('默认单个代码库具备 2GB… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: https://docs.atomgit.com/en/repo/capacity answered HTTP 404 on 2026-11-19 | source: [1] | note: not applicable
- retention: unverified: https://docs.atomgit.com/en/repo/capacity answered HTTP 404 on 2026-11-19 | source: [1]
- egress: unverified: https://docs.atomgit.com/en/repo/capacity answered HTTP 404 on 2026-11-19 | metered: no
- identity: email
- interface: unknown
- interface detail: unverified: https://docs.atomgit.com/en/repo/capacity answered HTTP 404 on 2026-11-19
- tooling: not documented
- composes with: the same as interface detail
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB of LFS per repo. The capacity doc states it plainly: 'By default, a repository has 2GB Git storage space and 5GB LFS storage space', confirmed by a 2024 user write-up ('默认单个代码库具备 2GB…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB of LFS per repo. The capacity doc states it plainly: 'By default, a repository has 2GB Git storage space and 5GB LFS storage space', confirmed by a 2024 user write-up '默认单个代码库具备 2GB Gi
  - [2] 2026-10-21: cited as the basis of the rejection: 5 GB of LFS per repo. The capacity doc states it plainly: 'By default, a repository has 2GB Git storage space and 5GB LFS storage space', confirmed by a 2024 user write-up '默认单个代码库具备 2GB Gi
  - probe:https://docs.atomgit.com/en/repo/capacity 2026-11-19: the first-party capacity page answered HTTP 404 on 2026-11-19 | capture: sha256:7f1ceed93a5dd05480d7eba57efe31e12490abe6523d94b2172290ff0d7e9494 | quote: "status": 404
  - probe:https://docs.atomgit.com/en/repo/capacity 2026-11-19: the first-party capacity page again answered HTTP 404 on 2026-11-19 | capture: sha256:7f1ceed93a5dd05480d7eba57efe31e12490abe6523d94b2172290ff0d7e9494 | quote: "status": 404
- sources:
  - [1] https://docs.atomgit.com/en/repo/capacity
  - [2] https://ost.51cto.com/posts/28716
