# Forgejo

> forgejo.org | CI runners, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/forgejo/ | JSON https://fshy.ajam.dev/api/v1/entity/forgejo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Forgejo and Gitea Actions (self-hosted)

- `ci-cd-runners/forgejo-gitea-actions` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category CI software
- needs card no, phone no, ID no, institution no | verified 2026-11-06T19:14:28.503Z (live) | stale on 2026-12-07
- url https://forgejo.org/docs/latest/user/actions/
- free tier: GPL v3+ for Forgejo v9.0 and later, MIT for Forgejo up to v8.0 | unit: unlimited | metered on: none | read on: 2026-11-06 | source: [1] | note: Gitea, the upstream project, is licensed under the MIT License.
- per-object cap: a job runs for at most the number of minutes its jobs.<job_id>.timeout-minutes key sets | source: [2] | note: the actual machine provided by the runner entirely depends on how the runner was registered
- retention: whatever the runner host retains | source: [2]
- egress: whatever the runner host charges | metered: no | source: [2]
- identity: anonymous | detail: the software needs no account
- interface: git, cli
- limits:
  - per-object-cap: a job runs for at most the number of minutes its jobs.<job_id>.timeout-minutes key sets [2]
- interface detail: a .forgejo/workflows or .gitea/workflows YAML; the act runner; a compatible subset of GitHub Actions
- tooling: the forgejo or act runner binary; docker or a host backend
- composes with: Actions syntax without GitHub, which lets a workflow move between a free hosted runner and your own machine without a rewrite
- reliability: compatibility with GitHub Actions is a documented subset, so a workflow that runs on GitHub may need edits
- notes: The compatibility is the value and the subset is the cost. A workflow that depends on a GitHub-only action does not run.
- evidence note: the Forgejo Actions user guide was read; Codeberg's hosted instance runs the same software.
- self hosted: yes
- evidence:
  - [2] 2026-10-22: Forgejo Actions is GitHub-Actions-compatible with documented differences; runners are user-provided
  - [3] 2026-10-22: Codeberg's hosted runners use ghcr.io/catthehacker/ubuntu:act-latest to provide a compatibility level with GitHub Actions, and Docker-in-Docker is not officially supported
  - [2] 2026-11-04: Forgejo Actions is not identical to GitHub Actions, so a workflow may need edits | capture: sha256:8c8a779c1a4e82b1679b0238872cb7c0a41dee2aa0046ff47932817138faf289 | quote: However, GitHub Actions and Forgejo Actions are not the same and things might not work right away.
  - [1] 2026-11-06: Forgejo v9.0 and later is GPL v3+ and Forgejo up to v8.0 is MIT | capture: sha256:09c8f6b9e7c660821c31c34a03ecd1c32b6731755ab183f685b753b9af7b5a8f | quote: Forgejo versions v9.0 and later are distributed under the terms of the GPL v3+. ... Forgejo versions up to v8.0 inclusive are distributed under the terms of the MIT license.
  - [4] 2026-11-06: Gitea is licensed under the MIT License | capture: sha256:f44bcff37456431faa23c5d19b75db142fc191e3e0ef0d70c60bd4ceee5aea3a | quote: This project is licensed under the MIT License.
  - [2] 2026-11-06: the jobs.<job_id>.timeout-minutes key caps how long a job runs | capture: sha256:8c8a779c1a4e82b1679b0238872cb7c0a41dee2aa0046ff47932817138faf289 | quote: Set the number of minutes this job can be performed before it is canceled.
  - [2] 2026-11-06: the machine a job gets depends on how the runner was registered | capture: sha256:8c8a779c1a4e82b1679b0238872cb7c0a41dee2aa0046ff47932817138faf289 | quote: The actual machine provided by the runner entirely depends on how the runner was registered
- sources:
  - [1] https://forgejo.org/faq/
  - [2] https://forgejo.org/docs/latest/user/actions/
  - [3] https://codeberg.org/actions/meta
  - [4] https://github.com/go-gitea/gitea

## Gitea / Forgejo self-hosted with any S3 LFS backend

- `storage/gitea-forgejo-self-hosted-with-any-s3-lfs-backend` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://forgejo.org/docs/latest/admin/advanced/quota/
- free tier: Unlimited by default: `quota.default.TOTAL = -1` means unlimited, and the soft-quota feature is 'currently not yet enabled by default'. You supply the disk/object store, so bytes = your infrastructure. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap unless you set one | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Yours to pay for. Unless the LFS backend is one of the free S3 endpoints (HF buckets, IA), in which case egress is the backend's and is free/CDN. | metered: no
- identity: email
- interface: s3-compatible, rest, git
- limits:
  - per-object-cap (binding): No per-file cap unless you set one [1]
- limits note: Soft-quota only: 'Forgejo checks the quota usage only before an action is executed, but it will allow a started action to complete'. So it can be overshot. No per-file cap unless you set one.
- interface detail: git
- tooling: Gitea/Forgejo binaries (single Go binary), `git-lfs` client, S3-compatible LFS storage config (`[lfs] STORAGE_TYPE=minio`). REST API + Swagger for full automation. Gitea Cloud offers a 30-day trial, not free.
- composes with: The pattern that makes 500 GB+ real: self-host the forge on a free-tier VM (or any always-on box) and set LFS storage to a free S3 endpoint. The forge holds ~metadata only; the bytes never touch your disk. Gitea's `LFS_MAX_FILE_SIZE`/`LFS_START_SERVER` are config, not policy.
- reliability: Quota feature is explicitly 'still in development' with 'little support for early prevention of operations in the UI'. Self-hosted means a dead VM = dead forge, but the LFS blobs survive in the object store.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'quota.default.TOTAL is -1 (unlimited) by default'; soft-quota semantics quoted
  - [2] 2026-10-21: storage backend configuration for LFS/attachments
- sources:
  - [1] https://forgejo.org/docs/latest/admin/advanced/quota/
  - [2] https://forgejo.org/docs/latest/admin/setup/storage/
