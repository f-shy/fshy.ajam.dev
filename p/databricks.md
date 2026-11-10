# Databricks

> databricks.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/databricks/ | JSON https://fshy.ajam.dev/api/v1/entity/databricks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Databricks

- `compute/databricks` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:18.802Z (live) | stale on 2026-12-05
- url https://www.databricks.com/product/startups
- free tier: 'Up to $400 in credits' on the free-trial table, with 'Full Databricks platform access for two (2) weeks used for business evaluation'. The page adds: 'A customer's eligibility for credits under this offer, the amount of credits (if any), and when any credits expire are solely determined by Databricks following account creation.' | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: platform access for 14 days; the credit's expiry is determined by Databricks after signup, and the trial ends when the credits are exhausted | days: 14 | source: [1]
- egress: not stated | metered: no | source: [2]
- identity: email | detail: no credit card is required to start the trial; a work email is recommended for full trial benefits, and the Free Edition accepts a personal address
- interface: cli, rest
- limits:
  - volume-quota (binding): up to USD 400 of credits, 14 days of platform access, amount at Databricks' discretion [1]
- limits note: this is a ceiling, not a grant: the page states eligibility, amount and expiry are decided after account creation
- binding note: the credit is a discretionary ceiling with a 14-day access window, so the balance and the window end it together
- interface detail: Databricks CLI, REST API, SDKs (Python, JavaScript, Java, Go), SSH tunnel and the workspace web console
- tooling: Databricks CLI (databricks/cli), Databricks SDKs for Python, JavaScript, Java, Go and R, Databricks Connect, the Terraform provider and SQL drivers
- composes with: USD 200,000 on Databricks compute is the largest credit in the data-platform group and it also funds Neon Postgres, so one approval covers both a warehouse and an app database. The chain breaks at the funding round.
- reliability: no reliability event recorded
- notes: The 14 days is the access window, not a stated credit expiry. No all-purpose-cluster DBU rate could be read, so the credit cannot be sized as a machine. Working against the user's own cloud account bills that cloud provider directly, outside the credit.
- evidence note: the trial page was read on 2026-10-23 and carries the amount, the two-week access window and the discretion clause; the pricing page serves its SKU tables client-side, so no DBU rate is recorded
- extras:
  - facets.class: startup-credit
  - facets.free_tier_kind: one-shot-credit
  - credit_usd_ceiling: 400
  - access_days: 14
- evidence:
  - [1] 2026-10-23: quoted: 'Up to $400 in credits' and 'Full Databricks platform access for two (2) weeks used for business evaluation'
  - [1] 2026-10-23: quoted: 'No credit card is required to start your Databricks free trial.' and the discretion clause on eligibility, amount and expiry
  - [3] 2026-10-23: 200 with 413 words; every instance-type path returned 404 or an empty extraction, so no DBU rate was established
  - [4] 2026-11-03: the CLI and REST API exist | capture: sha256:97898700c3011dcb9c29df6de963310bd3f3706e86a929230e34ce2da839d2d1 | quote: Direct interaction with Databricks from the command line Shell scripting Experimentation Invoke the REST API directly
  - [5] 2026-11-04: the docs name the Databricks CLI as a user | capture: sha256:7a5ec231182c9a2207c9a30f5720273a5dd93a875632c2f49ee40d31504617ee | quote: The [Databricks CLI](https://github.com/databricks/cli) (command-line interface) allows you to interact with the Databricks platform from your local terminal or automation scripts.
- sources:
  - [1] https://www.databricks.com/try-databricks
  - [2] https://www.databricks.com/product/startups
  - [3] https://www.databricks.com/product/pricing
  - [4] https://docs.databricks.com/en/dev-tools/index.html
  - [5] https://docs.databricks.com/aws/en/dev-tools/cli/

## Databricks Free Edition (default storage / Unity Catalog volumes)

- `storage/databricks-free-edition` | trial-only | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.databricks.com/aws/en/getting-started/free-edition
- disagrees on identity_kind: `storage/databricks-free-edition` says institution, `storage/databricks-free-edition-2` says email
- disagrees on verdict: `storage/databricks-free-edition` says trial-only, `storage/databricks-free-edition-2` says fails-quota
- free tier: No published byte quota. Free Edition ships 'serverless compute and default storage, so you can immediately start exploring and building'. Default storage is 'a fully managed object storage platform' and in serverless workspaces you can 'create additional catalogs in either default storage or in your own cloud object storage'. Quotas are documented for compute, jobs, pipelines, model serving and apps. Never for bytes. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not addressed in the Free Edition docs. Outbound internet is 'restricted to a limited set of trusted domains', which throttles external egress to non-approved hosts. | metered: no
- identity: institution
- interface: rest, rclone, cli
- limits note: Per-object-cap: not documented for default storage. Unverified. request-rate: per-account serverless quotas ('Max of 5 concurrent job tasks per account', one SQL warehouse capped at 2X-Small). This is the binding constraint and it is compute, not storage. retention: 'While your compute will be unavailable, your data and settings will not be deleted'; deleting a managed table/volume keeps files 'to allow for a 7-day recovery window' then purges within 48 hours.
- interface detail: rest
- tooling: Unity Catalog volumes via SQL (`CREATE CATALOG ..`) or the Databricks CLI / REST API; no rclone backend. File access requires serverless, Unity-Catalog-enabled compute. 'All interactions with default storage require serverless, Unity Catalog-enabled compute'.
- composes with: One workspace per signup; the docs do not cap workspaces. Storage is uncapped in the docs but only reachable through compute, so the real multiplier is compute quota resets ('your workspace's compute resources will be shut down and unavailable for the rest of the day' on quota exhaustion; data is retained).
- reliability: Storage without a documented quota but also without a storage-native API. You cannot `PUT` arbitrary bytes without spinning compute, and compute is throttled to 'the rest of the day'. Custom workspace storage locations are unsupported. Realistically a place to park tabular artefacts, not a 20 TiB blob archive.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: No published byte quota. Free Edition ships 'serverless compute and default storage, so you can immediately start exploring and building' — default storage is 'a fully managed object storage platform' and in serverless workspaces you can 'create additional catalogs in either default storage or in your own cloud object storage'. Quotas are documented for compute, jobs, pipelines, model serving and apps — never for bytes.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Your new workspace includes serverless compute and default storage'
  - [3] 2026-10-21: 'Default storage is a fully managed object storage platform'; 'All interactions with default storage require serverless, Unity Catalog-enabled compute'
  - [1] 2026-10-21: (last updated 2026-10-18) — quota table covers compute/jobs/pipelines/serving only; 'Custom workspace storage locations' unsupported
  - withheld 2026-10-21: probe: GET docs.databricks.com/aws/en/getting-started/free-edition-limitations -> 200 (read live 2026-10-21)
- sources:
  - [1] https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
  - [2] https://docs.databricks.com/aws/en/getting-started/free-edition
  - [3] https://docs.databricks.com/aws/en/storage/default-storage

## databricks free edition (default storage as an archive)

- `storage/databricks-free-edition-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
- disagrees on identity_kind: `storage/databricks-free-edition` says institution, `storage/databricks-free-edition-2` says email
- disagrees on verdict: `storage/databricks-free-edition` says trial-only, `storage/databricks-free-edition-2` says fails-quota
- free tier: none reachable: Free Edition is perpetual in the sense that it does not expire, and hitting quota does not delete data ('your data and settings will not be deleted'). But it is serverless-only with… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: Free Edition is perpetual in the sense that it does not expire, and hitting quota does not delete data ('your data and settings will not be deleted'). But it is serverless-only with…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free Edition is perpetual in the sense that it does not expire, and hitting quota does not delete data ('your data and settings will not be deleted'). But it is serverless-only with…
- sources:
  - [1] https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
