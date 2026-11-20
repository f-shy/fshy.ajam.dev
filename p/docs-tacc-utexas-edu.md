# TACC Corral

> docs.tacc.utexas.edu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs-tacc-utexas-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/docs-tacc-utexas-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TACC Corral (US) — 5 TB free per PI, $60/TB/year beyond

- `storage/tacc-corral-5-tb-free-per-pi-60-tb-year-beyond` | fails-quota | evidence documented | binding volume-quota | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T01:24:43.359Z (live) | stale on 2026-12-05
- url https://docs.tacc.utexas.edu/hpc/corral/
- free tier: 'The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost. For storage needs larger than 5TB, and for multiple project allocations, access to Corral is available at a cost of $60/TB/year.' 40 PB online + tape replica. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: Priced beyond 5 TB at $60/TB/year: a 10 TiB allocation costs $360 per year and a 20 TiB allocation $1020 per year after the free 5 TB, for a PI at a US based institution, if allocations are whole TB.
- per-object cap: No limitation on the size of files; by default 1 million files per 5TB allocated (200,000 files per allocated terabyte). | source: [1] | note: not stated
- retention: Files are never purged by automated processes; each allocation lasts one year and must be renewed. After expiry data is typically retained for 6 months, but may be deleted at any time at the discretion of the system administrators unless an allocation request is pending. | source: [1] | note: not stated
- egress: Not metered in the doc, but there is no public HTTP download path. Corral is a mounted/POSIX store, so serving is not its purpose. | metered: yes
- identity: institution | detail: PI status needs a faculty, staff or postdoctoral position at a US based institution; users from non-US institutions are not eligible for PI status but may be invited to a project by a US based PI
- interface: sftp, scp, rsync, s3-compatible
- limits:
  - volume-quota (binding): first 5TB for each PI on one project is free for UT System institutions; larger allocations cost $60/TB/year [1]
  - volume-quota (binding): limit of 200,000 files per allocated terabyte (1 million files per 5TB) [1]
- limits note: 5TB free for each PI on one project (UT System institutions), $60/TB/year beyond; a hard cap of 200,000 files per allocated terabyte. Allocations last one year. S3 access needs an allocation of at least 25TB.
- binding note: the free allocation is 5TB for each PI and every allocation carries a cap of 200,000 files per allocated terabyte; beyond 5TB the price is $60/TB/year
- interface detail: sftp
- tooling: scp and SFTP (Cyberduck documented) to data.tacc.utexas.edu; an S3 version 4 compatible endpoint is available only by request for allocations of at least 25TB, not for protected data; TACC allocation portal. rsync is not named on the page.
- composes with: 5 TB free × UT System PIs, then linear $60/TB/yr. The file-count rule is the real limiter: 'There is also a limit of 200,000 files per allocated terabyte'. At 5 TB that is 1 million files.
- reliability: The free 5 TB applies to UT System institutions only, and PI status needs a US based institution; storage beyond 5 TB costs $60/TB/year. Each allocation lasts one year and must be renewed, so this is a 5 TB niche tier, not a free archive.
- notes: the same as the free tier
- evidence note: re-read on 2026-11-03: the vendor pages https://docs.tacc.utexas.edu/hpc/corral/ (free 5TB, $60 per TB per year beyond, file count limit, one-year allocations, S3 by request, scp transfer) and https://tacc.utexas.edu/use-tacc/allocations/ (PI eligibility at US based institutions)
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost. For storage needs larger than 5TB, and for multiple project allocations, access to Corral is available at a cost of $60/TB/year.' 40 PB online + tape replica.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost ... $60/TB/year', 'limit of 200,000 files per allocated terabyte', '40PB of on-line storage' (last update August 4, 2026)
  - [2] 2026-10-21: 'Users from non-US institutions are not eligible for PI status'
  - [1] 2026-11-03: storage beyond 5TB costs $60/TB/year | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: For storage needs larger than 5TB, and for multiple project allocations, access to Corral is available at a cost of $60/TB/year.
  - [1] 2026-11-03: file size is not limited on Corral | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: There are no limitations on the size of files stored on Corral
  - [1] 2026-11-03: allocations last one year and files are never purged automatically | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Files on Corral are never "purged" using automated processes, however each allocation lasts for only one year and must be renewed at the end of that year.
  - [1] 2026-11-03: data is typically retained 6 months after an allocation expires | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Once an allocation has expired, data will typically be retained for 6 months after the expiration of the allocation, however data may be deleted at any time at the discretion of the system administrators unless there is an allocation request pending.
  - [1] 2026-11-03: an S3 version 4 compatible interface exists by request | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Corral can provide a cloud storage interface compatible with the S3 version 4 API, available only by request.
  - [1] 2026-11-03: a dedicated S3 service needs an allocation of at least 25TB | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Due to resource requirements, you must have an allocation size of at least 25TB to request a dedicated S3 service.
  - [1] 2026-11-03: data transfer uses the scp utility to a login node | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Data transfer from any Unix/Linux system can be accomplished using the `scp` utility to copy data to and from the login node.
  - [1] 2026-11-03: the first 5TB for each PI is free for UT System institutions | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost.
  - [1] 2026-11-03: the file count is limited to 200,000 files per allocated terabyte | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: There is also a limit of 200,000 files per allocated terabyte imposed on all Corral allocations
  - [1] 2026-11-03: the free allocation is 5TB for each PI | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost.
  - [1] 2026-11-03: the file count is limited per allocated terabyte | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: There is also a limit of 200,000 files per allocated terabyte imposed on all Corral allocations
  - [2] 2026-11-03: faculty, staff and postdoctoral researchers at US based institutions can request PI status | capture: sha256:19da6b80939814833658addc286cef797ff0aa651f13c853a36ef3c9838dc3f6 | quote: Faculty, staff, and postdoctoral researchers at US based institutions are eligible to request PI status.
  - [2] 2026-11-03: users from non-US institutions are not eligible for PI status | capture: sha256:19da6b80939814833658addc286cef797ff0aa651f13c853a36ef3c9838dc3f6 | quote: Users from non-US institutions are not eligible for PI status, but may be invited to work on a project by a US based PI.
  - [1] 2026-11-03: allocations last one year and must be renewed | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: Files on Corral are never "purged" using automated processes, however each allocation lasts for only one year and must be renewed at the end of that year.
  - [1] 2026-11-03: the first 5TB for each PI is still free for UT System institutions | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost.
  - [1] 2026-11-04: the first 5TB per PI is free for UT System institutions | capture: sha256:41a6b0852e64c54f1e0ee8e357e47228a5b8ee649f83db80c0c83a595b75cf48 | quote: The first 5TB of storage for each PI, on one project, is available to researchers at all UT System institutions at no cost.
- sources:
  - [1] https://docs.tacc.utexas.edu/hpc/corral/
  - [2] https://tacc.utexas.edu/use-tacc/allocations/
