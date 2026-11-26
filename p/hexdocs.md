# hex.pm

> hexdocs.pm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hexdocs/ | JSON https://fshy.ajam.dev/api/v1/entity/hexdocs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hex.pm (elixir/erlang)

- `storage/hex-pm` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:03.730Z (live) | stale on 2026-12-04
- url https://hexdocs.pm/hex/Mix.Tasks.Hex.Publish.html
- free tier: none reachable: 8 MB compressed / 64 MB uncompressed for packages and docs combined. Also requires a curated package name and does review. Far too small to shard meaningfully. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 8 MB compressed / 64 MB uncompressed for packages and docs combined. Also requires a curated package name and does review. Far too small to shard meaningfully.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 8 MB compressed / 64 MB uncompressed for packages and docs combined. Also requires a curated package name and does review. Far too small to shard meaningfully.
  - [1] 2026-11-19: published packages and docs are capped at 8 MB compressed and 64 MB uncompressed | capture: sha256:ec528a557714b9214b5c693c56da6464669bbf928cdc1017e4883d3fa427f5f8 | quote: Packages and documentation sizes are limited to 8mb compressed, and 64mb uncompressed.
- sources:
  - [1] https://hexdocs.pm/hex/Mix.Tasks.Hex.Publish.html
