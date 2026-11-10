# NOMAD

> nomad-lab.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nomad-lab/ | JSON https://fshy.ajam.dev/api/v1/entity/nomad-lab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NOMAD (NOMAD Central / nomad-lab.eu)

- `storage/nomad` | fails-quota | evidence reported | binding none | category research-data-repository
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nomad-lab.eu
- free tier: 32 GiB maximum per project, and at most 10 unpublished projects per user. Both are config knobs (process.max_upload_size, services.upload_limit) rather than business limits, and they differ per deployment. Publishing requires at least one successfully parsed entry, and publishing is what frees the 10-project slot. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and anonymous for published entries via the NOMAD API and GUI. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: fails-quota at 32 GiB, and write-gated by the parser: 'A project must contain at least one successfully processed entry before it can be published.' Content must be materials-science-shaped (DFT codes, ELN exports) to be parseable at all. Both limits together make it useless as bulk storage despite the clean API.
- interface detail: rest
- tooling: Documented REST API requires HTTP authentication tokens for uploads via API endpoints. File parsers are plugin-based and format validation depends on target deployment configuration.
- composes with: 10 unpublished projects × 32 GiB = 320 GiB of live scratch on a free account, and publishing an entry releases a slot. So the steady-state ceiling is bounded by how fast a human can publish, not by bytes.
- reliability: Well-run EU (FAIRmat) infrastructure with a real API. The constraint is semantic, not technical.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 32 GiB maximum per project, and at most 10 unpublished projects per user. Both are config knobs (process.max_upload_size, services.upload_limit) rather than business limits, and they differ per deployment. Publishing requires at least one successfully parsed entry, and publishing is what frees the 10-project slot.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: opened: 'a maximum project size of 32 GiB, controlled by process.max_upload_size'; 'at most 10 unpublished projects per user, controlled by services.upload_limit'; 'A project must contain at least one successfully processed entry before it can be published.'
  - [2] 2026-10-21: PROBED: curl -> HTTP 200, 271,764 bytes (public endpoint). curl https://nomad-lab.eu/prod/v1/api/v1/uploads?page_size=1 -> HTTP 401, 37 bytes, {"detail":"Authentication required."} — an honest auth gate.
  - [3] 2026-10-21: (older v1 doc, reached via search) — same 32 GB / 10 upload figures, confirming the numbers are stable across doc generations.
- sources:
  - [1] https://docs.nomad-lab.eu/howto/manage/gui/upload.html
  - [2] https://nomad-lab.eu/prod/v1/api/v1/info
  - [3] https://nomad-lab.eu/prod/v1/docs/howto/manage/gui/upload.html
