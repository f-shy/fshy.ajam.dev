# Perplexity Projects

> perplexity.ai | Crawling, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/perplexity/ | JSON https://fshy.ajam.dev/api/v1/entity/perplexity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Perplexity

- `crawler-scraper/perplexity` | paid-only | evidence documented | binding request-rate | category search API
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.perplexity.ai/getting-started/pricing
- free tier: none: the Search API is billed per successful request from the first one | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable: nothing is stored | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: billing is required before the first call
- interface: rest
- limits:
  - request-rate (binding): USD 5.00 per 1,000 search requests; Fast Search USD 1.00 per 1,000 [1]
- interface detail: REST Search API, one billing unit per successful POST /search whatever the query count
- tooling: not established
- composes with: Ranks near the top of external search benchmark evaluations. Unusable programmatically without a prepaid account balance.
- reliability: no reliability event recorded
- notes: The platform's status.json shows a spent credit for this provider and no limit, consistent with a prepaid balance rather than a free tier.
- evidence:
  - [1] 2026-10-22: Search API USD 5.00 and Fast Search USD 1.00, charged per successful POST /search; a request with up to five queries is one billing unit
- sources:
  - [1] https://docs.perplexity.ai/getting-started/pricing

## Perplexity Projects (formerly Spaces) — persistent file repository

- `storage/perplexity-projects-persistent-file-repository` | fails-egress | evidence reported | binding per-object-cap | category AI answer engine / project files
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.perplexity.ai/help-center/en/articles/12009761-enterprise-file-limits
- free tier: 5 GB per Project, 10,000 files per Project, 100 MB per file. Identical on every plan, including free. Projects themselves: 'There's no limit on how many Projects you can create.'. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: Session uploads (not Projects) are 40-50 MB/file and are deleted after 7 days. Do not confuse the two. | days: 7 | source: [1] | note: not stated
- egress: No egress concept. Files are read by the model or viewed in-app, not served over a shareable URL. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): 100 MB per file [1]
  - per-object-cap (binding): 50 MB/file [1]
  - retention-clamped: deleted after 7 days [1]
- limits note: Per-object-cap 100 MB. Session uploads (not Projects) are 40-50 MB/file and are deleted after 7 days. Do not confuse the two. Projects created before Aug 2026 may exceed 5 GB and then refuse new uploads.
- interface detail: Web UI only for consumer. No public Files API. Enterprise has File Connectors and an organization repository (being retired 2026-10-01).
- tooling: None for storage. Unofficial browser automation only.
- composes with: Unlimited Projects x 5 GB each. Projects are the multiplicative axis and the help centre states the cap is absent. Unlike NotebookLM, adding a Project costs nothing and there is no account-wide byte wall documented.
- reliability: Projects retain uploaded files until deleted. No public API is provided and programmatic interaction requires browser automation. Access is restricted to internal search readers, and unsupported binary formats cannot be exported or queried via documented endpoints.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB per Project, 10,000 files per Project, 100 MB per file — identical on every plan, including free. Projects themselves: 'There's no limit on how many Projects you can create.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Every Project supports up to 10,000 files, 5 GB of total storage, and 100 MB per file. These limits are the same for all subscribers, regardless of plan'; table 'Total storage per Project | 5 GB'
  - [1] 2026-10-21: 'There's no limit on how many Projects you can create.'
  - [2] 2026-10-21: 'Files uploaded to sessions are retained for 7 days, then deleted'; organization file repository 'retired on October 1, 2026'
- sources:
  - [1] https://www.perplexity.ai/help-center/en/articles/10352961-what-are-projects
  - [2] https://www.perplexity.ai/help-center/en/articles/12009761-enterprise-file-limits
