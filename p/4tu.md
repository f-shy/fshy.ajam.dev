# 4TU.ResearchData

> 4tu.nl | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/4tu/ | JSON https://fshy.ajam.dev/api/v1/entity/4tu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 4TU.ResearchData

- `storage/4tu-researchdata` | fails-quota | evidence reported | binding none | category Dutch multi-university Dataverse/Invenio
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.4tu.nl
- free tier: 5 GB per researcher per year free, then a one-off €4.50/GB (~$4,900/TB). Some sources cite 10 GB for non-4TU institutions. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free | metered: no
- identity: email | detail: Email. Explicitly open: 'Anyone from science, engineering and design can use 4TU.ResearchData to upload and publish their research data and software' and 'I am not affiliated with one of the 4TU's, can I deposit my data? Anyone .. can upload'. The identity gate is genuinely zero; the quota gate is what kills it.
- interface: rest
- limits note: Strict quota enforced with paid per-gigabyte pricing.
- interface detail: REST, OAI-PMH
- tooling: part of interface detail
- composes with: none at the scale
- reliability: Pricing is per-GB one-off, so cost scales linearly with volume. No bulk escape.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB per researcher per year free, then a one-off €4.50/GB (~$4,900/TB). Some sources cite 10 GB for non-4TU institutions.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: (Wayback 20251018113714) — 'I am not affiliated with one of the 4TU's, can I deposit my data? Anyone from science, engineering and design can use 4TU.ResearchData to upload and publish their research data and software'
  - [1] 2026-10-21: (search snippet) — 'Every researcher can upload up to 5 GB of data per year ... free of charge'; larger uploads charged a one-off fee
  - [3] 2026-10-21: (search snippet) — 'we charge a one-off €4.50 per GB'
- sources:
  - [1] https://data.4tu.nl/info/en/use/publish-cite/upload-your-data-in-our-data-repository
  - [2] https://data.4tu.nl/info/about-4turesearchdata/frequently-asked-questions
  - [3] https://community.data.4tu.nl/frequently-asked-questions/
