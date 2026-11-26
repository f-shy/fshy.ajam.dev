# osf registrations

> osf.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osf/ | JSON https://fshy.ajam.dev/api/v1/entity/osf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OSF (Open Science Framework) — per-component quotas

- `storage/osf-per-component-quotas` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:16.851Z (live) | stale on 2026-12-10
- url https://osf.io
- free tier: OSF limited the capacity of private projects and components utilizing OSF Storage to 5 GB and public projects and components to 50 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB per file | bytes: 5000000000 | source: [1] | note: Individual files must be 5GB or less to be uploaded to OSF Storage.
- retention: source: [1] | note: No retention statement documented on the cited OSF Storage FAQ page.
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
- notes: Currently, there is no applied overall cap on the amount of OSF Storage per user.
- evidence:
  - [1] 2026-10-21: read live: 'Currently, there is no applied overall cap on the amount of OSF Storage per user' and 'Individual files must be 5GB or less'
  - [2] 2026-10-21: read live: 'Private Projects: 5 GB ... Public Projects: 50 GB ... Max File Size: 5 GB per individual file ... Each Component on a project has its own 5GB/50GB storage limit'
  - [2] 2026-10-21: read live: storage add-ons 'do not count against these storage limits', i.e. add-ons are a second un-metered path
  - [1] 2026-11-11: OSF caps private projects and components at 5 GB and public projects and components at 50 GB | capture: sha256:238d582842bcd0b0da89c01c14bbe31f3ee829fdd2db0b38f25e68b5bf3e0b48 | quote: OSF limited the capacity of private projects and components utilizing OSF Storage to 5 GB and public projects and components to 50 GB.
  - [1] 2026-11-11: OSF applies no overall cap on OSF Storage per user | capture: sha256:238d582842bcd0b0da89c01c14bbe31f3ee829fdd2db0b38f25e68b5bf3e0b48 | quote: Currently, there is no applied overall cap on the amount of OSF Storage per user.
  - [1] 2026-11-19: the private 5 GB and public 50 GB quotas are unchanged | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: OSF limited the capacity of private projects and components utilizing OSF Storage to 5 GB and public projects and components to 50 GB.
  - [1] 2026-11-19: OSF still applies no overall per-user cap | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Currently, there is no applied overall cap on the amount of OSF Storage per user.
  - [1] 2026-11-19: the 5 GB per-file limit is unchanged | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Individual files must be 5GB or less to be uploaded to OSF Storage.
  - [1] 2026-11-25: the OSF FAQ states a 5 GB per-file limit for OSF Storage | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Individual files must be 5GB or less to be uploaded to OSF Storage. Larger files can be stored in an add-on. [Learn more about storage add-ons](https://help.osf.io/article/395-storage-add-ons)
  - [1] 2026-11-25: the cited FAQ page contains no retention period statement; it states deleted files or projects cannot be recovered | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Unfortunately, no. When a user deletes a file or project from OSF, access to this content is removed for all users.
  - [1] 2026-11-25: the OSF FAQ states the 5 GB per-file cap for OSF Storage | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Individual files must be 5GB or less to be uploaded to OSF Storage. Larger files can be stored in an add-on. [Learn more about storage add-ons](https://help.osf.io/article/395-storage-add-ons)
  - [1] 2026-11-25: the cited OSF FAQ page does not state a retention period; it states deleted content cannot be recovered | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Unfortunately, no. When a user deletes a file or project from OSF, access to this content is removed for all users.
- sources:
  - [1] https://help.osf.io/article/555-add-ons-storage-api-integration-faq-s
  - [2] https://help.osf.io/article/353-welcome-to-projects

## osf registrations

- `storage/osf-registrations` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.864Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the first-party FAQ confirms registrations are capped at 5 GB across all registered storage | capture: sha256:4690800e909bc8df0c0560a0d694fe7fbffbd7dfe54ca5c43f3b9380bde9cef2 | quote: Registrations must be 5GB or less across all storage being registered.
- sources:
  - [1] https://help.osf.io/article/555-add-ons-storage-api-integration-faq-s
