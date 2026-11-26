# homebrew taps

> brew.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/brew/ | JSON https://fshy.ajam.dev/api/v1/entity/brew.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## homebrew taps

- `storage/homebrew-taps` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:04.248Z (live) | stale on 2026-12-04
- url https://docs.brew.sh/Taps
- free tier: none reachable: A tap is just a GitHub git repo of formulae; storage is GitHub's (2 GB push / repo recommended limits), and bottles live in GHCR or on the project's own host. Nothing Homebrew-specific adds | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: A tap is just a GitHub git repo of formulae; storage is GitHub's (2 GB push / repo recommended limits), and bottles live in GHCR or on the project's own host. Nothing Homebrew-specific adds
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A tap is just a GitHub git repo of formulae; storage is GitHub's (2 GB push / repo recommended limits), and bottles live in GHCR or on the project's own host. Nothing Homebrew-specific…
  - [2] 2026-10-21: cited as the basis of the rejection: A tap is just a GitHub git repo of formulae; storage is GitHub's (2 GB push / repo recommended limits), and bottles live in GHCR or on the project's own host. Nothing Homebrew-specific…
  - [1] 2026-11-19: a Homebrew tap is still just a git repository cloned from a GitHub URL; Homebrew itself adds no storage product | capture: sha256:4a9046dfc8643a88c19ab716fea0386107e1fbac3ecbd1683b5a460674725891 | quote: `brew tap <user>/<repository>` clones `https://github.com/<user>/homebrew-<repository>` into Homebrew
- sources:
  - [1] https://docs.brew.sh/Taps
  - [2] https://github.com/<user>/homebrew-<repository>`
