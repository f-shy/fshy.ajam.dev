# GitGud

> gitgud.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitgud/ | JSON https://fshy.ajam.dev/api/v1/entity/gitgud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GitGud (gitgud.io) - GitLab instance

- `storage/gitgud-gitlab-instance` | fails-quota | evidence inferred | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://gitgud.io
- free tier: unverified: blocked by challenge. The origin returned HTTP 403 through the fetch proxy (x-web-origin-status: 403) on every attempt, and the reader returned empty content. No instance-configuration page could be read, so no size table exists. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unknown; presumed free like other GitLab instances, but not verified. | metered: no
- identity: email
- interface: ssh, git
- limits note: unverified: blocked by challenge. What is known: the site is a long-running GitLab instance popular with modding/NSFW-adjacent projects, and it has historically been open-registration.
- interface detail: git
- tooling: Standard GitLab (git over SSH/HTTPS, GitLab API).
- composes with: Unknown - cannot state a multiplication rule without a verified per-object cap.
- reliability: Site actively refuses automated clients (403 at the origin, not a human-verification step to solve). Also its archive captures are thin - the closest 2025-06 capture is a 302 with a 445-byte body, so even the archived copy carries no content. Two attempts spent per the challenge protocol, then abandoned.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: unverified: blocked by challenge. The origin returned HTTP 403 through the fetch proxy (x-web-origin-status: 403) on every attempt, and the reader returned empty content. No instance-configuration page could be read, so no size table exists.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> 403 direct
  - [3] 2026-10-21: capture 20250601203907 is status 302, 445 bytes (no content)
  - withheld 2026-10-21: unverified: blocked by challenge - instance_configuration never read
- sources:
  - [1] https://gitgud.io/help/instance_configuration
  - [2] https://gitgud.io/
  - [3] https://web.archive.org/web/202506/gitgud.io

## gitgud.io

- `storage/gitgud-io` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:39.840Z (live) | stale on 2026-12-04
- url https://about.gitgud.io/
- free tier: No repo size or quantity limits, including groups; large or binary data should use Git LFS on a separate storage array. Content must be development-related; the host states it is not free storage or a CDN. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The about page states no repo size or quantity limits, including groups, with large or binary data directed to Git LFS on a separate array; content must be development-related and the host states it is not free storage or a CDN.
- notes: GitLab-based host; the first-party about page states no repo size or quantity limits, Git LFS on a separate array, and development-only content (not free storage or a CDN).
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
  - [2] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
  - [3] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
  - [1] 2026-11-19: the first-party about page states no repo size or quantity limits and directs large data to Git LFS | capture: sha256:e1d5a96dc6698148559a60feff1961e6dbbe59b91898a215f5c00ba5cfa12d28 | quote: ## WHAT ARE THE REPOSITORY LIMITS No repo size or quantity limits, including groups. However we ask that large/binary data utilize Git LFS, which uses a different storage array from normal Git data. All data on GitGud should be development-related content only. We are not free storage or cdn.
  - [1] 2026-11-19: the first-party about page states the host is free with no set repo size limit | capture: sha256:e1d5a96dc6698148559a60feff1961e6dbbe59b91898a215f5c00ba5cfa12d28 | quote: ### Free Totally free for any user or group. No set size limit for repo sizes.
  - [1] 2026-11-19: the first-party about page states the repository-size and LFS policy | capture: sha256:e1d5a96dc6698148559a60feff1961e6dbbe59b91898a215f5c00ba5cfa12d28 | quote: ## WHAT ARE THE REPOSITORY LIMITS No repo size or quantity limits, including groups. However we ask that large/binary data utilize Git LFS, which uses a different storage array from normal Git data. All data on GitGud should be development-related content only. We are not free storage or cdn.
  - [1] 2026-11-19: the first-party about page states the current repository-size and LFS policy | capture: sha256:e1d5a96dc6698148559a60feff1961e6dbbe59b91898a215f5c00ba5cfa12d28 | quote: ## WHAT ARE THE REPOSITORY LIMITS No repo size or quantity limits, including groups. However we ask that large/binary data utilize Git LFS, which uses a different storage array from normal Git data. All data on GitGud should be development-related content only. We are not free storage or cdn.
- sources:
  - [1] https://about.gitgud.io/
  - [2] https://gitgud.io/help
  - [3] https://gitgud.io/gitgud/gitgud-support
