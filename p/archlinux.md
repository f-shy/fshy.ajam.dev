# AUR

> archlinux.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archlinux/ | JSON https://fshy.ajam.dev/api/v1/entity/archlinux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## aur

- `storage/aur-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://bugs.archlinux.org/task/68997
- free tier: none reachable: 250 KiB hard blob cap enforced by a server-side git hook. Off by three orders of magnitude. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 250 KiB hard blob cap enforced by a server-side git hook. Off by three orders of magnitude.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 250 KiB hard blob cap enforced by a server-side git hook. Off by three orders of magnitude.
- sources:
  - [1] https://bugs.archlinux.org/task/68997

## AUR (Arch User Repository)

- `storage/aur` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://aur.archlinux.org
- free tier: Not a storage candidate at all: the AUR enforces a hard maximum blob size of 250 KiB per git object. The git hook rejects the push: 'remote: error: maximum blob size (250.00KiB) exceeded / remote: error: hook declined to update refs/heads/master'. Config files around 250.8 KiB already trip it. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 250 KiB | bytes: 256000 | source: [1] | note: not stated
- retention: per-object-cap: 250 KiB (hard, server-side git hook). retention: indefinite for packages | source: [1] | note: not stated
- egress: Free (plain git over SSH/HTTPS), but irrelevant given the cap. | metered: no
- identity: email
- interface: ssh, git, rclone
- limits:
  - per-object-cap (binding): per-object-cap: 250 KiB [1]
- limits note: per-object-cap: 250 KiB (hard, server-side git hook). retention: indefinite for packages. request-rate: git push over ssh, per-key.
- interface detail: part of the free tier
- tooling: git over ssh://aur.archlinux.org/<pkg>.git; AUR RPC v5 at /rpc/. No rclone backend (git is the interface).
- composes with: unlimited AUR packages x 250 KiB = useless for bulk. Content must be PKGBUILD + patches; large sources are fetched at build time by URL, never stored.
- reliability: Any 'AUR as storage' idea dies here.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: quota
  - dead_end.why: Not a storage candidate at all: the AUR enforces a hard maximum blob size of 250 KiB per git object. The git hook rejects the push: 'remote: error: maximum blob size (250.00KiB) exceeded / remote: error: hook declined to update refs/heads/master'. Config files around 250.8 KiB already trip it.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'remote: error: maximum blob size (250.00KiB) exceeded' on a 250.8 KiB config file; maintainer confirms the limit is intentional
  - [2] 2026-10-21: '[aur-general] max blob size exceeded'
  - [3] 2026-10-21: probe: GET -> 200, 679 bytes (RPC v5 live; metadata only, no blob path)
- sources:
  - [1] https://bugs.archlinux.org/task/68997
  - [2] https://lists.archlinux.org/pipermail/aur-general/2015-August/031470.html
  - [3] https://aur.archlinux.org/rpc/?v=5&type=info&arg=google-chrome
