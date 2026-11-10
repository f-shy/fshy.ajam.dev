# Flathub

> flathub.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flathub/ | JSON https://fshy.ajam.dev/api/v1/entity/flathub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flathub (dl.flathub.org OSTree repo)

- `storage/flathub` | fails-quota | evidence reported | binding write-gated | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://flathub.org
- free tier: No published storage quota for published applications. This is a deduplicating OSTree/OCI repo: apps are stored as content-addressed ostree commits, so identical files across apps are stored once. Review is human: submissions arrive as a pull request to github.com/flathub/flathub and 'will be reviewed' - there is no self-service arbitrary-blob publish. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none published; the practical constraint is the build (GitHub-hosted runners with limited CPU/memory/time). retention: indefinite for published apps (OSTree history is retained; `flatpak repair`/`prune` is user-side) | source: [1] | note: not stated
- egress: Free, CDN-backed static repo at dl.flathub.org. No billing. | metered: no
- identity: email
- interface: rest, oci, rclone
- limits:
  - write-gated (binding): applications [1]
  - write-gated (binding): Review is human: submissions arrive as a pull request to github [1]
- limits note: per-object-cap: none published; the practical constraint is the build (GitHub-hosted runners with limited CPU/memory/time). retention: indefinite for published apps (OSTree history is retained; `flatpak repair`/`prune` is user-side). request-rate: dl.flathub.org supports ranges (verified 206). Builds that exceed CI limits 'fail to build'. Human review gates publication.
- interface detail: rest
- tooling: `flatpak` (client), `flatpak-builder` + `org.flatpak.Builder`, `ostree` tooling, and the repo is readable as a plain static OSTree (summary / summary.idx / objects). No rclone backend and no OCI registry (registry.flathub.org does not resolve publicly - DNS NXDOMAIN from this vantage).
- composes with: one repo, unlimited apps x unlimited architectures (x86_64, aarch64) x unlimited builds. Per-app dedup means 20 TiB of distinct content is not achievable here; dedup only helps legitimately-overlapping app payloads. Multiplication is by flatpak app, not by account, and every app is human-reviewed.
- reliability: Read path is excellent and range-capable. Write path is not programmatic: a pull request + human review + a CI build. Content must be a valid Flatpak app manifest that builds from source, so arbitrary blobs cannot be published without wrapping them in an app (and reviewers will see them). dl.flathub.org works; registry.flathub.org does not resolve.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: No published storage quota for published applications. This is a deduplicating OSTree/OCI repo: apps are stored as content-addressed ostree commits, so identical files across apps are stored once. Review is human: submissions arrive as a pull request to github.com/flathub/flathub and 'will be reviewed' - there is no self-service arbitrary-blob publish.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 12,702,673 bytes (real binary OSTree summary, contains app/ai.jan.Jan/x86_64/stable etc.)
  - [3] 2026-10-21: probe: ranged GET bytes 0-1048575 on -> 206, 1,048,576 bytes
  - [3] 2026-10-21: probe: GET -> 200, 10,738,037 bytes
  - [1] 2026-10-21: submission is a PR to github.com/flathub/flathub, built with org.flatpak.Builder and reviewed
  - withheld 2026-10-21: probe: DNS registry.flathub.org -> NXDOMAIN (the OCI registry endpoint is not publicly resolvable)
- sources:
  - [1] https://docs.flathub.org/docs/for-app-authors/submission
  - [2] https://dl.flathub.org/repo/summary
  - [3] https://dl.flathub.org/repo/appstream/x86_64/appstream.xml.gz

## flathub as bulk storage

- `storage/flathub-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.flathub.org/docs/for-app-authors/submission
- free tier: none reachable: Human-reviewed flatpak app submissions; content-addressed/deduplicated OSTree means distinct bytes are not additive; registry.flathub.org does not resolve publicly. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: Human-reviewed flatpak app submissions; content-addressed/deduplicated OSTree means distinct bytes are not additive; registry.flathub.org does not resolve publicly.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Human-reviewed flatpak app submissions; content-addressed/deduplicated OSTree means distinct bytes are not additive; registry.flathub.org does not resolve publicly.
- sources:
  - [1] https://docs.flathub.org/docs/for-app-authors/submission
