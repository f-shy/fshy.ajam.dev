# CodeFloe

> codefloe.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codefloe/ | JSON https://fshy.ajam.dev/api/v1/entity/codefloe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CodeFloe (Forgejo, Hetzner Germany)

- `storage/codefloe` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://codefloe.com
- free tier: 5 GB Git + 20 GB packages + 10 GB Git LFS + 10 GB attachments per account/organization; unlimited public and private repositories | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Single small operator on one Hetzner box; nightly off-site backups with 90-day retention described as disaster recovery, not per-account restore | days: 90 | source: [1] | note: not stated
- egress: Download traffic for packages, container images and LFS is counted per account per month but 'There is no limit today'. Unlimited, and the endpoint is Cloudflare-fronted. Git clones, release assets and attachments are explicitly not counted. | metered: no
- identity: anonymous
- interface: rest, webdav, oci, rclone
- limits note: Per-account quotas only (5 GB git / 20 GB packages / 10 GB LFS / 10 GB attachments). Download counter booked hourly at the edge proxy; a limit will be set later (currently 429 only after an as-yet-unset threshold). Uploads and Git ops never blocked by traffic limits. 2500 CI minutes/month.
- interface detail: rest
- tooling: Full Forgejo API v1 (packages, generic, OCI registry, releases, LFS) + rclone's Gitea/Forgejo-compatible WebDAV-free REST via any HTTP client; OCI via ORAS/skopeo; package registry speaks Generic/Docker/npm/PyPI etc.
- composes with: Unlimited free accounts -> 5+20+10+10 = 45 GB of separately-metered pools per identity. Because packages (20 GB) and LFS (10 GB) are separate pools from Git (5 GB), one account yields ~45 GB across four subjects, and each further account carries the same 45 GB. Registry blobs are anonymous-pullable, so shard across repos like any OCI store.
- reliability: Single small operator on one Hetzner box; nightly off-site backups with 90-day retention described as disaster recovery, not per-account restore. Explicit published policy of monitoring several accounts used to exceed its quota and deleting/suspending. The chaining path is actively watched, unlike GitLab's.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Git repo size 5 GB | "Packages" size 20 GB | Git LFS 10 GB | Attachments 10 GB'; 'There is no limit today' on download traffic
  - [2] 2026-10-21: 'Unlimited public and private repositories', '5 GB Git storage per account'
  - [3] 2026-10-21: probe: GET -> {"version":"16.0.6"} (live Forgejo 16, not a brochure)
  - [4] 2026-10-21: probe: GET -> 401 WWW-Authenticate Bearer realm=https://codefloe.com/v2/token (registry live)
  - withheld 2026-10-21: probe: anonymous token for CodeFloe/forgejo-codefloe:pull -> 200, then GET /v2/CodeFloe/forgejo-codefloe/manifests/latest with that token -> 200 application/vnd.oci.image.index.v1+json, docker-content-digest sha256:d75b4b8f... (anonymous OCI pull works)
  - [5] 2026-10-21: probe: GET -> 200 (open registration)
  - [6] 2026-10-21: probe: GET -> 200, lists container packages incl. sha256-digest tags (anonymous package enumeration)
- sources:
  - [1] https://docs.codefloe.com/usage-quotas/
  - [2] https://codefloe.com/pricing
  - [3] https://codefloe.com/api/v1/version
  - [4] https://codefloe.com/v2/
  - [5] https://codefloe.com/user/sign_up
  - [6] https://codefloe.com/api/v1/packages/CodeFloe?limit=5
