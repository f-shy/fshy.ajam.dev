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
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://about.gitgud.io/
- free tier: none reachable: GitLab-based host publishes no storage or LFS quota. Support repository returned HTTP 504 and /help returned HTTP 409. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
  - [2] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
  - [3] 2026-10-21: Their support repo 504'd and /help returned 409. Unverifiable, and a GitLab i
- sources:
  - [1] https://about.gitgud.io/
  - [2] https://gitgud.io/help
  - [3] https://gitgud.io/gitgud/gitgud-support
