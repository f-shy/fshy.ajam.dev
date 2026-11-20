# CodeFloe

> codefloe.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codefloe/ | JSON https://fshy.ajam.dev/api/v1/entity/codefloe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CodeFloe (Forgejo, Hetzner Germany)

- `storage/codefloe` | qualifies-with-caveat | evidence reported | binding none | category registry
- needs card no, phone no, ID no, institution no | verified 2026-11-11T02:51:00.984Z (live) | stale on 2026-11-26
- url https://codefloe.com
- free tier: 5 GB Git + 20 GB packages + 10 GB Git LFS + 10 GB attachments | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB per release asset or issue/comment attachment | source: [1] | note: not stated
- retention: Single small operator on one Hetzner box; nightly off-site backups with 90-day retention described as disaster recovery, not per-account restore | days: 90 | source: [1] | note: not stated
- egress: There is no limit today. | metered: no
- identity: email | detail: Registration asks for a username, an email address and a password.
- interface: rest, webdav, oci, rclone
- limits note: Per-account quotas only (5 GB git / 20 GB packages / 10 GB LFS / 10 GB attachments). Download counter booked hourly at the edge proxy; a limit will be set later (currently 429 only after an as-yet-unset threshold). Uploads and Git ops never blocked by traffic limits. 2500 CI minutes/month.
- interface detail: rest
- tooling: Full Forgejo API v1 (packages, generic, OCI registry, releases, LFS) + rclone's Gitea/Forgejo-compatible WebDAV-free REST via any HTTP client; OCI via ORAS/skopeo; package registry speaks Generic/Docker/npm/PyPI etc.
- composes with: Unlimited free accounts -> 5+20+10+10 = 45 GB of separately-metered pools per identity. Because packages (20 GB) and LFS (10 GB) are separate pools from Git (5 GB), one account yields ~45 GB across four subjects, and each further account carries the same 45 GB. Registry blobs are anonymous-pullable, so shard across repos like any OCI store.
- reliability: Single small operator on one Hetzner box; nightly off-site backups with 90-day retention described as disaster recovery, not per-account restore. Explicit published policy of monitoring several accounts used to exceed its quota and deleting/suspending. The chaining path is actively watched, unlike GitLab's.
- notes: 5 GB Git + 20 GB packages + 10 GB Git LFS + 10 GB attachments per account/organization; unlimited public and private repositories
- evidence note: the usage-quotas page states a 500 MB cap on a release asset or issue/comment attachment
- evidence:
  - [1] 2026-10-21: 'Git repo size 5 GB | "Packages" size 20 GB | Git LFS 10 GB | Attachments 10 GB'; 'There is no limit today' on download traffic
  - [2] 2026-10-21: 'Unlimited public and private repositories', '5 GB Git storage per account'
  - [3] 2026-10-21: probe: GET -> {"version":"16.0.6"} (live Forgejo 16, not a brochure)
  - [4] 2026-10-21: probe: GET -> 401 WWW-Authenticate Bearer realm=https://codefloe.com/v2/token (registry live)
  - withheld 2026-10-21: probe: anonymous token for CodeFloe/forgejo-codefloe:pull -> 200, then GET /v2/CodeFloe/forgejo-codefloe/manifests/latest with that token -> 200 application/vnd.oci.image.index.v1+json, docker-content-digest sha256:d75b4b8f... (anonymous OCI pull works)
  - [5] 2026-10-21: probe: GET -> 200 (open registration)
  - [6] 2026-10-21: probe: GET -> 200, lists container packages incl. sha256-digest tags (anonymous package enumeration)
  - [1] 2026-11-09: the account quotas are 5 GB Git, 20 GB packages, 10 GB Git LFS and 10 GB attachments | capture: sha256:09d4ddc82c3e8d6b5513bdd3c2c6d179a1e5bde8a7cd9ac61a7c5b2f13d6f683 | quote: | Git repo size | “Packages” size | Git LFS size | Attachments size | Actions Artifacts size | | --- | --- | --- | --- | --- | | 5 GB | 20 GB | 10 GB | 10 GB | 2 GB |
  - [1] 2026-11-09: a release asset or issue/comment attachment is capped at 500 MB | capture: sha256:09d4ddc82c3e8d6b5513bdd3c2c6d179a1e5bde8a7cd9ac61a7c5b2f13d6f683 | quote: | Release assets and issue/comment attachments | 500 MB |
  - [1] 2026-11-09: downloads are counted but no limit applies today | capture: sha256:09d4ddc82c3e8d6b5513bdd3c2c6d179a1e5bde8a7cd9ac61a7c5b2f13d6f683 | quote: There is no limit today.
  - [5] 2026-11-09: registration asks for a username, an email address and a password | capture: sha256:b8a22611096c30f59367a551d23065d3abb60abdeeb535d2b96c3c47db138927 | quote: #### Register Username Email address Password Confirm password
  - [2] 2026-11-09: all functionality is free | capture: sha256:6fcae8bfd32bb876a8289532f0eab05d8b4c73fbb5066a3edfafbc26fee0467a | quote: All functionality is free.
  - [1] 2026-11-11: the quota table states 5 GB Git, 20 GB packages, 10 GB Git LFS and 10 GB attachments | capture: sha256:575354bec2c72d99aa3d8fe0cf7d5aa5583e34fe6fce210c7aec8a10469e1483 | quote: | Git repo size | “Packages” size | Git LFS size | Attachments size | Actions Artifacts size | | 5 GB | 20 GB | 10 GB | 10 GB | 2 GB |
- sources:
  - [1] https://docs.codefloe.com/usage-quotas/
  - [2] https://codefloe.com/pricing
  - [3] https://codefloe.com/api/v1/version
  - [4] https://codefloe.com/v2/
  - [5] https://codefloe.com/user/sign_up
  - [6] https://codefloe.com/api/v1/packages/CodeFloe?limit=5
