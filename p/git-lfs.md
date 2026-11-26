# Git LFS

> git-lfs.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/git-lfs/ | JSON https://fshy.ajam.dev/api/v1/entity/git-lfs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Git LFS

- `storage/git-lfs` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:39.838Z (live) | stale on 2026-12-04
- url https://git-lfs.com
- free tier: Free: 10 GiB storage AND 10 GiB bandwidth per month; per-file 2 GB on Free/Pro, 4 GB Team, 5 GB Enterprise. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 2 GB per file | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free tier includes 10 GiB per month bandwidth, with additional bandwidth metered at standard rates. | metered: yes | free allowance: 10 GiB per month
- identity: institution
- interface: rest, git
- limits:
  - per-object-cap (binding): 2 GB per file [1]
- limits note: 10 GiB storage, 10 GiB/month bandwidth, 2 GB per file on Free; 300 req/min unauthenticated LFS API, 3000 authenticated.
- interface detail: rest
- tooling: git-lfs client, batch API at /info/lfs/objects/batch (probed: 200).
- composes with: 10 GiB x unlimited accounts is the only path, and each account needs a payment method to go beyond. Without one, LFS is disabled until the next month.
- reliability: Exceeding free bandwidth without a payment method disables Git LFS entirely until the next month. A hard stop, not a throttle.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free: 10 GiB storage AND 10 GiB bandwidth per month; per-file 2 GB on Free/Pro, 4 GB Team, 5 GB Enterprise.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: table: 'GitHub Free | 10 GiB | 10 GiB' (Bandwidth | Storage); 'Git LFS support is disabled on your account until the next month'
  - [2] 2026-10-21: 'GitHub Free | 2 GB' max file size
  - withheld 2026-10-21: probe: POST github.com/git-lfs/git-lfs.git/info/lfs/objects/batch -> 200, per-object error 404 'Object does not exist on the server' (anonymous batch endpoint is live)
  - [1] 2026-11-19: the first-party billing page still lists 10 GiB bandwidth and 10 GiB storage for GitHub Free | capture: sha256:86871fb8f4b2a196b63e1c79129df9937783fd1c3052fef215a4e12ccf0b3d1a | quote: | GitHub Free | 10 GiB | 10 GiB | | GitHub Pro | 10 GiB | 10 GiB |
  - [1] 2026-11-19: the first-party page states LFS is disabled until the next month when the bandwidth quota is exceeded without a payment method | capture: sha256:86871fb8f4b2a196b63e1c79129df9937783fd1c3052fef215a4e12ccf0b3d1a | quote: If you use more than your included quota of bandwidth per month without a payment method on file, Git LFS support is disabled on your account until the next month.
  - [2] 2026-11-19: the first-party page still lists 2 GB as the maximum LFS file size on Free and Pro | capture: sha256:5895fb5506ab81747ea151d3e3a7cbea9c9620aab25ff130c0deda4d4145b371 | quote: | GitHub Free | 2 GB | | GitHub Pro | 2 GB | | GitHub Team | 4 GB | | GitHub Enterprise Cloud | 5 GB |
- sources:
  - [1] https://docs.github.com/en/billing/concepts/product-billing/git-lfs
  - [2] https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
