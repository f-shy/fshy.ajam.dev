# osf registrations

> osf.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osf/ | JSON https://fshy.ajam.dev/api/v1/entity/osf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OSF (Open Science Framework) — per-component quotas

- `storage/osf-per-component-quotas` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://osf.io
- free tier: 50 GB per public project, 5 GB per private project, 5 GB per file. But 'Each Component on a project has its own 5GB/50GB storage limit' and, crucially, 'Currently, there is no applied overall cap on the amount of OSF Storage per user.' Component trees are unbounded, so this is per-unit quota, not per-account. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; downloads served from OSF Storage (US/Canada/Germany/Australia regions) | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB per file [1]
- limits note: 5 GB per file is the hard limit. Worse than Zenodo's 50 GB and worse than Harvard's 2.5 GB only in being middling. 5 GB applies to private projects, so working storage is the expensive tier here; 50 GB requires making the project public.
- interface detail: rest
- tooling: OSF open API v2 (api.osf.io/v2, JSON:API: nodes, files, waterbutler); official osfclient Python package; OSF is the canonical 'component = free bucket' multiplier
- composes with: 50 GB x unlimited components x (optionally) unlimited projects. A project can nest components, each with its own 50 GB, and there is no overall per-user cap. So the structure is the same per-record multiplier as Zenodo but with a smaller unit (50 GB) and a much lower per-file ceiling (5 GB).
- reliability: OSF is mid-'Project Transition' per its own help banner, which is a structural-change risk for a long-lived archive. Storage is regional and selectable only at project creation and cannot be moved afterwards.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: 'Currently, there is no applied overall cap on the amount of OSF Storage per user' and 'Individual files must be 5GB or less'
  - [2] 2026-10-21: read live: 'Private Projects: 5 GB ... Public Projects: 50 GB ... Max File Size: 5 GB per individual file ... Each Component on a project has its own 5GB/50GB storage limit'
  - [2] 2026-10-21: read live: storage add-ons 'do not count against these storage limits', i.e. add-ons are a second un-metered path
- sources:
  - [1] https://help.osf.io/article/555-add-ons-storage-api-integration-faq-s
  - [2] https://help.osf.io/article/353-welcome-to-projects

## osf registrations

- `storage/osf-registrations` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.osf.io/article/555-add-ons-storage-api-integration-faq-s
- free tier: none reachable: Registrations archive OSF Storage plus add-ons but are capped at 5 GB across all storage being registered, and you can no longer create Registrations from Projects after the transition. Not | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Registrations archive OSF Storage plus add-ons but are capped at 5 GB across all storage being registered, and you can no longer create Registrations from Projects after the transition. Not
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Registrations archive OSF Storage plus add-ons but are capped at 5 GB across all storage being registered, and you can no longer create Registrations from Projects after the transition. Not
- sources:
  - [1] https://help.osf.io/article/555-add-ons-storage-api-integration-faq-s
