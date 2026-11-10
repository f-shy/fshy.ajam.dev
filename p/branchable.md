# git-annex

> branchable.com | Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/branchable/ | JSON https://fshy.ajam.dev/api/v1/entity/branchable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## git-annex rclone special remote (built into annex since 2023)

- `storage/git-annex-rclone-special-remote` | self-hosted, last resort | verdict qualifies | evidence reported | binding per-ip-shaping | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://git-annex.branchable.com/special_remotes/rclone/
- free tier: N/A. Front-end to rclone storage backends, inheriting free tiers of supported providers. Documentation lists Drive, OneDrive, Dropbox, Mega, pCloud, Box, Yandex, Jottacloud, WebDAV, FTP, SFTP, Swift, B2, and S3. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Determined by the selected rclone backend. Rclone handles throttling and retries across remote endpoints. | metered: no
- identity: institution
- interface: rest, git, rclone
- limits:
  - per-ip-shaping (binding): 750 GB/day [1]
- limits note: Per-backend: file size caps, per-day upload quotas, API rate limits all apply unchanged. rclone's Drive backend has its own 750 GB/day upload cap; OneDrive throttles. Encrypted annex remotes lose rclone's server-side dedupe.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Two paths: (a) `git annex initremote type=rclone ..`. Native, no extra install, documented via `rclone gitannex -h`; (b) the older `git-annex-remote-rclone` bash script (DanielDent, ~300 lines). rclone itself is a single static binary.
- composes with: Combines git-annex versioning, checksum verification, and partial checkouts with rclone remote storage backends. A single repository can configure multiple rclone remotes across diverse storage providers using git annex copy commands.
- reliability: Solid; the native remote removed the bash-script dependency. The failure mode is per-backend token expiry and drive-level rate limiting, which rclone surfaces as retries rather than data loss.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'With a recent version of rclone and git-annex, it is not necessary to install anything else, just use `git-annex initremote type=rclone ...`'
  - [2] 2026-10-21: the gitannex bridge command exists in rclone proper
  - [3] 2026-10-21: backend feature matrix (Internet Archive, Drive, OneDrive, Box, Mega, WebDAV, SFTP, S3 all Tier 1-3 with R/W)
- sources:
  - [1] https://git-annex.branchable.com/special_remotes/rclone/
  - [2] https://rclone.org/commands/rclone_gitannex/
  - [3] https://rclone.org/overview/

## git-annex S3 special remote (backend-agnostic)

- `storage/git-annex-s3-special-remote` | self-hosted, last resort | verdict qualifies | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://git-annex.branchable.com/special_remotes/S3/
- free tier: N/A by itself. Inherits whatever S3-compatible store you point it at. This is the multiplier: any free S3 endpoint (Internet Archive s3.us.archive.org, HF s3.hf.co, Oracle/Cloudflare-adjacent object tiers, MinIO on a free VM) becomes a versioned large-file store with git-annex's own manifest. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Determined by the backing S3 store. Parameter publicurl enables downloads via direct HTTP GET, and parameter signature=anonymous allows unauthenticated read-only access. | metered: no
- identity: email
- interface: s3, git
- limits note: Depends on backend. Practical: `partsize=1GiB` needed for multipart; parts under 100 MiB are rejected by S3; `versioning=yes` means git-annex cannot drop content. No delete-resume; interrupted uploads restart. For IA specifically, uploads to the test collection vanish after 30 days and public visibility lags.
- interface detail: part of the free tier
- tooling: git-annex (Haskell, standalone Linux/macOS builds, ~1.5k stars on the mirror). Config via `git annex initremote type=S3 host=... bucket=... requeststyle=path`. Internet Archive has a documented special mode (`host=s3.us.archive.org`) where git-annex writes x-archive-meta-* headers and records the public URL, so every annexed file is also fetchable from archive.org with no login.
- composes with: One special remote per bucket; `fileprefix=` lets many remotes share one bucket. The allowance is per account, so each free S3 account adds one bucket. Because git-annex keys content by hash, the S3 side is a dumb blob store. A client can shard the same dataset across several free stores, and git-annex tracks which copy is where (`git annex whereis`). Chunking (`chunk=1MiB`) avoids per-object size caps on the backing store.
- reliability: Mature and boring — the special remote has existed for over a decade. Failure mode is backend-side (IA's S3 endpoint was unreachable: connect timeout on s3.us.archive.org:443, and archive.org/help/abouts3.txt returned 522 through the proxy), not annex-side.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: full parameter list including `host`, `requeststyle=path`, `publicurl`, `signature=anonymous`, `chunk`, `fileprefix`
  - [2] 2026-10-21: 'git annex initremote archive type=S3 protocol=https host=s3.us.archive.org bucket=...' with x-archive-meta headers
  - [3] 2026-10-21: built-in list: S3, rclone, webdav, rsync, directory, bup, ddar, git-lfs, httpalso, gcrypt
  - withheld 2026-10-21: probe: TCP connect to s3.us.archive.org:443 -> timeout after 21s (backend flaky, tooling fine)
- sources:
  - [1] https://git-annex.branchable.com/special_remotes/S3/
  - [2] https://git-annex.branchable.com/tips/Internet_Archive_via_S3/
  - [3] https://git-annex.branchable.com/special_remotes/

## git-annex git-lfs special remote (annex over any LFS host)

- `storage/git-annex-git-lfs-special-remote` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://git-annex.branchable.com/special_remotes/git-lfs/
- free tier: N/A. A protocol adapter. Turns ANY git-lfs server (GitHub, GitLab, Bitbucket, a self-hosted Gitea) into an annex special remote, so the LFS host's quota applies but annex adds hash-verified partial clone and `whereis` across mirrors. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Cannot delete = every mistake is permanent on the LFS side, and the host's month-storage accounting (GitHub) means you keep paying for it in quota | source: [1] | note: not stated
- egress: Determined by the underlying Git LFS host. | metered: no
- identity: email
- interface: git
- limits note: Hard, documented limitations: 'The git-lfs protocol does not support deleting content, so git-annex cannot delete anything from a git-lfs special remote'; no upload resume; 'git-annex doesn't do batching. This may cause it to fall afoul of rate limiting of git-lfs servers' — which directly collides with GitLab's 1000 req/min LFS limit. Requires SHA256 backend for efficiency.
- interface detail: part of the free tier
- tooling: `git annex initremote lfstest type=git-lfs url=... encryption=shared`. Supports gcrypt:: URL prefix for encrypting the git side too.
- composes with: Because annex can hold the same content on several LFS remotes, you can stack the 10 GiB/project GitLab allowance and the 10 GiB GitHub allowance as tiers of one logical dataset, with annex tracking which objects live where. Sharding a 1 TiB corpus across 100 GitLab projects becomes a `git annex copy --to` loop.
- reliability: Cannot delete = every mistake is permanent on the LFS side, and the host's month-storage accounting (GitHub) means you keep paying for it in quota. No batching + per-object request = the exact workload LFS rate limits are designed to stop.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: limitations section quoted above
  - [1] 2026-10-21: example: 'git annex initremote lfstest type=git-lfs url=gcrypt::[address removed]:username/somerepo.git encryption=shared'
- sources:
  - [1] https://git-annex.branchable.com/special_remotes/git-lfs/

## git-annex bup / ddar special remotes

- `storage/git-annex-bup-ddar-special-remotes` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://git-annex.branchable.com/special_remotes/bup/
- free tier: none reachable: Both dedupe into a repository you must host yourself and both need full shell access (bup: 'git-annex-shell does not support bup ... you need full shell access to the server'). No hosted… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both dedupe into a repository you must host yourself and both need full shell access (bup: 'git-annex-shell does not support bup ... you need full shell access to the server'). No hosted…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both dedupe into a repository you must host yourself and both need full shell access (bup: 'git-annex-shell does not support bup ... you need full shell access to the server'). No hosted…
  - [2] 2026-10-21: cited as the basis of the rejection: Both dedupe into a repository you must host yourself and both need full shell access (bup: 'git-annex-shell does not support bup ... you need full shell access to the server'). No hosted fre
- sources:
  - [1] https://git-annex.branchable.com/special_remotes/bup/
  - [2] https://git-annex.branchable.com/special_remotes/ddar/
