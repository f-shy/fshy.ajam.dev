# Stoat

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-stoatchat/ | JSON https://fshy.ajam.dev/api/v1/entity/github-stoatchat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stoat / Revolt — self-hosted instance

- `storage/stoat-revolt-self-hosted-instance` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/stoatchat/self-hosted
- free tier: No platform cap at all: `body_limit_size` and `[files.limit]` live in Revolt.toml and are yours to set. Storage is whatever disk/MinIO you attach to Autumn. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Whatever your own host costs. Not free, so this is self-hosting rather than a free tier. Only interesting if a box with unmetered bandwidth is already available. | metered: no
- identity: email
- interface: s3, rest
- limits note: `body_limit_size = 20_000_000` is the shipped default (must exceed any per-file limit); `max_size = 20000000` in Autumn.toml is the per-file cap. Multiple users report editing Autumn.toml alone does not raise the limit. Body_limit_size in Revolt.toml must move too.
- interface detail: rest
- tooling: Docker Compose stack (stoatchat/self-hosted), Autumn file service with S3/MinIO backend, full Revolt/Stoat API so all existing clients and bots work unchanged.
- composes with: N/A. The multiplier is disk, not accounts. It is a reference architecture rather than a free provider.
- reliability: Self-hosted means the data is yours, but the project has had repeated breaking migrations (Autumn refactor 2024-09-30, breaking changes 2024-11-28) that require manual DB work.
- notes: the same as the free tier
- evidence note: Re-read 2026-10-22: the page answers and the claim holds; the rung is unchanged because the read establishes the page, not the enforcement.
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No platform cap at all: `body_limit_size` and `[files.limit]` live in Revolt.toml and are yours to set. Storage is whatever disk/MinIO you attach to Autumn.
  - dead_end.first_recorded: 2026-10-21
  - superseded_evidence[0].url: https://github.com/stoatchat/self-hosted
  - superseded_evidence[0].date: 2024-09-30
  - superseded_evidence[0].proved: README — notes on the 2024-09-30 Autumn refactor requiring manual migration
  - superseded_evidence_note: Rows that are older than the topic's 180-day evidence window. They are kept as the historically read statement and are not evidence for the current claim; the current claim rests on the 2026-10-22 re-read in evidence[]. Nothing was deleted.
- evidence:
  - [2] 2026-10-21: 'body_limit_size = 20_000_000 / Maximum permissible body size in bytes for uploads / (should be greater than any one file upload limit)'
  - [3] 2026-10-21: 'Editing line 10 [max_size = 20000000] in Autumn.toml ... does not change the file upload limits'
  - [1] 2026-10-22: re-read 2026-10-22 (HTTP 200, 14,637 B): the repository is live and still documents the Autumn refactor and its migration notice
- sources:
  - [1] https://github.com/stoatchat/self-hosted
  - [2] https://read.../github.com/stoatchat/stoatchat/blob/main/crates/core/config/Revolt.toml
  - [3] https://github.com/revoltchat/self-hosted/issues/53
