# Perplexity

> perplexity.ai | Crawling, Inference, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/perplexity/ | JSON https://fshy.ajam.dev/api/v1/entity/perplexity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Perplexity (Crawling)

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

## Perplexity (Inference)

- `inference/perplexity` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.perplexity.ai/docs/getting-started/pricing
- free tier: No free text allowance; the Orchestrator and Agent APIs bill per token, and the Search API bills $5.00 per 1,000 successful requests. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key from the console; no card gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): per-token model rates and USD 5.00 per 1K Search API requests [1]
- endpoint: https://api.perplexity.ai
- tooling: OpenAI-compatible clients and the Perplexity SDK
- composes with: no standing free text tier; requests rejected with 429 are not billed
- reliability: tool fees and per-request charges are separate from token billing
- notes: -
- evidence:
  - [1] 2026-11-18: the API platform bills per token and per request with no free tier | capture: sha256:28f932182c8412af1043de83f0ba57505e83b6b29320b9c6c1c6168f45ba6e7f | quote: Each Perplexity API bills differently.
- sources:
  - [1] https://docs.perplexity.ai/docs/getting-started/pricing

## Perplexity Agent

- `inference/perplexity-agent` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.perplexity.ai/docs/agent-api/models
- free tier: No free text allowance; Agent API models bill per token (e.g. anthropic/claude-haiku-5-5 at $0.10 input / $0.50 output per 1M for prompts at or under 100k) plus per-call tool fees. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and shared API key from the console; no card gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): per-token model rates plus per-call tool fees [1]
- endpoint: https://api.perplexity.ai/v1
- tooling: OpenAI-compatible and Anthropic-compatible clients
- composes with: no free tier; tool fees accumulate on top of token cost
- reliability: service tiers flex (0.5x) and priority (2x) change token rates only for models that list them
- notes: -
- evidence:
  - [1] 2026-11-18: Agent API models are billed per token with published rates | capture: sha256:a55208fcf265199474716e27578a1bacedf6ddf404233543a875f47174fb0ddc | quote: Pricing rates are published per model and may differ from provider list prices.
- sources:
  - [1] https://docs.perplexity.ai/docs/agent-api/models

## Perplexity Projects (formerly Spaces) — persistent file repository

- `storage/perplexity-projects-persistent-file-repository` | fails-egress | evidence reported | binding per-object-cap | category AI answer engine / project files
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:39.876Z (live) | stale on 2026-12-04
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
  - [2] 2026-11-19: Project limits are 10,000 files, 5 GB, 100 MB per file on every plan | capture: sha256:fe19711f6d09da5ccd7170fdce7928aef3ceace3d2200ce6b809b70d1e45c01f | quote: Every Project supports up to 10,000 files, 5 GB of total storage, and 100 MB per file. These limits are the same for all subscribers, regardless of plan, and there is no restriction on file type.
  - [2] 2026-11-19: session uploads are deleted after 7 days, unchanged | capture: sha256:fe19711f6d09da5ccd7170fdce7928aef3ceace3d2200ce6b809b70d1e45c01f | quote: Files uploaded to sessions are retained for 7 days, then deleted.
  - [1] 2026-11-19: no cap on the number of Projects, so the chaining axis is unbounded | capture: sha256:d684a04629f65b599480dbe85278a3334211700aa99bb52b8974879b549e9ebf | quote: There’s no limit on how many Projects you can create.
- sources:
  - [1] https://www.perplexity.ai/help-center/en/articles/10352961-what-are-projects
  - [2] https://www.perplexity.ai/help-center/en/articles/12009761-enterprise-file-limits
