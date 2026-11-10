# figshare

> figshare.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/figshare/ | JSON https://fshy.ajam.dev/api/v1/entity/figshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## figshare (figshare.com free accounts)

- `storage/figshare` | fails-quota | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://figshare.com
- free tier: 20 GB storage quota per account. The current limit is 20 GB per individual file. Items 500, files per item 500, collections 100, projects 100. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file | bytes: 5000000000 | source: [1] | note: not stated
- retention: Stable commercial service (Digital Science); the binding constraint is the 20 GB pool, and published items are permanent/citable, so it behaves more like a publication endpoint than a bucket. | source: [1] | note: not stated
- egress: Free and CDN-friendly. Download path: ndownloader.figshare.com -> 302 -> S3 object (Server: AmazonS3), with Accept-Ranges/Content-Range exposed. No egress metering on free accounts. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 5 GB per file [1]
- limits note: 20 GB total storage and 20 GB max single file; 500 items, 500 files per item, 50 versions; virus scan only up to 10 MB. Exceeding 20 GB requires figshare+ (paid) or an institutional subscription.
- interface detail: rest
- tooling: figshare REST API v2 (live: GET api.figshare.com/v2/articles -> 200 JSON; per-file download_url at ndownloader.figshare.com). OAI-PMH available. figshare Python client (official, github.com/figshare/figshare-python). No rclone backend.
- composes with: 20 GB x unlimited free accounts. Weak multiplication within an account: the 20 GB is a single pool and the 500-item cap binds long before the bytes do at 20 GB/item.
- reliability: Stable commercial service (Digital Science); the binding constraint is the 20 GB pool, and published items are permanent/citable, so it behaves more like a publication endpoint than a bucket.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB storage quota per account. Items 500, files per item 500, collections 100, projects 100.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'storage quota: 20GB', 'max individual file size: 20GB', 'max number of items: 500'
  - [2] 2026-10-21: 'All figshare.com accounts are provided with 20GB of private storage and are able to upload individual files up to 20GB'
  - [3] 2026-10-21: probe: GET -L -> 302 then 200, 1512608 bytes, Server: AmazonS3
- sources:
  - [1] https://info.figshare.com/user-guide/account-limits/
  - [2] https://info.figshare.com/user-guide/file-size-limits-and-storage/
  - [3] https://ndownloader.figshare.com/files/69259858

## figshare for institutions

- `storage/figshare-for-institutions` | fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-12-05
- url https://info.figshare.com/user-guide/account-limits/
- free tier: Free figshare.com accounts: 20GB private storage and 20GB per file. Institutional repositories set their own private space and allow files up to 5TB; an individual has no self-serve route to that tier. Figshare+ is a paid, one-time-cost route for outputs above 20GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20GB per file on figshare.com accounts; up to 5TB per file in institutional repositories. | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Institutional private space is set by each institution and is not published on the limits page; files up to 5TB are offered both in institutional repositories and through Figshare+ (a paid, one-time-cost route).
- notes: Raises file size to 5 TB and private space per institution, but only for users with an institutional figshare repository. No self-serve route for an individual. Institutional quotas are set.
- evidence note: Documented from the vendor page https://info.figshare.com/user-guide/account-limits/ re-read on 2026-11-04: 20GB free private storage and file limit, 5TB files for institutions, institution-set private space, Figshare+ one-time cost.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Raises file size to 5 TB and private space per institution, but only for users with an institutional figshare repository — no self-serve route for an individual. Institutional quotas are…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Raises file size to 5 TB and private space per institution, but only for users with an institutional figshare repository — no self-serve route for an individual. Institutional quotas are…
  - [1] 2026-11-03: a free figshare.com account has 20GB private storage and a 20GB file limit | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: All figshare.com accounts are provided with 20GB of private storage and are able to upload individual files up to 20GB.
  - [1] 2026-11-03: the free allowance is stated in GB | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: storage quota: 20GB
  - [1] 2026-11-03: the quota is a storage quota | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: storage quota: 20GB
  - [1] 2026-11-03: institutional repositories allow files up to 5TB; figshare.com accounts 20GB | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: Figshare for institutions also offers larger file size uploads up to 5TB.
  - [1] 2026-11-03: private space above the free quota is set by the institution | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: For institutional users, your private space limit is dependent on your institution, please contact your institutional admins if you require more space.
  - [1] 2026-11-03: institutional space is institution-dependent | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: For institutional users, your private space limit is dependent on your institution, please contact your institutional admins if you require more space.
  - [1] 2026-11-03: Figshare+ is a paid one-time-cost route for outputs above 20GB; the price is not on this page | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: There is a one-time cost associated with Figshare+ to cover the cost of storing the data persistently ad infinitum.
  - [1] 2026-11-03: the free quota is 20GB, below the need | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: storage quota: 20GB
  - [1] 2026-11-03: institutional private space is set by each institution | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: For institutional users, your private space limit is dependent on your institution, please contact your institutional admins if you require more space.
  - [1] 2026-11-03: files up to 5TB are also offered through Figshare+, which is not an institutional repository | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: If you would like to publish outputs larger than 20GB (up to many TBs) or files larger than 20GB (up to 5TB), please consider
  - [1] 2026-11-03: institutional repositories also offer files up to 5TB | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: Figshare for institutions also offers larger file size uploads up to 5TB.
  - [1] 2026-11-04: a free figshare.com account has 20GB private storage and a 20GB file limit | capture: sha256:9fc92b71bdfabff77d4d6f7259d9bfebf01a7da2d0ab2590a2b2c1ab017d0e18 | quote: All figshare.com accounts are provided with 20GB of private storage and are able to upload individual files up to 20GB.
- sources:
  - [1] https://info.figshare.com/user-guide/account-limits/

## figshare+ (large-data tier)

- `storage/figshare-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://info.figshare.com/figshare-plus/
- free tier: none reachable: Paid, one-time data publishing charge ($875 per 250 GB per a third-party guide); requires a single publication/project, max 10 item DOIs, and all items submitted within 12 months.… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Paid, one-time data publishing charge ($875 per 250 GB per a third-party guide); requires a single publication/project, max 10 item DOIs, and all items submitted within 12 months.…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Paid, one-time data publishing charge ($875 per 250 GB per a third-party guide); requires a single publication/project, max 10 item DOIs, and all items submitted within 12 months.…
- sources:
  - [1] https://info.figshare.com/figshare-plus/
