# Databricks

> databricks.com | Compute, Inference, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/databricks/ | JSON https://fshy.ajam.dev/api/v1/entity/databricks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Databricks (Compute)

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

## Databricks (Inference)

- `inference/databricks` | trial-only | evidence documented | binding volume-quota | category managed inference on a data platform
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis
- free tier: No standing free inference allowance: Foundation Model APIs are pay-per-token. A free Databricks trial grants time-limited credits determined after account creation, and ends when credits are exhausted. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Databricks workspace/account and API token; trial credit eligibility determined after account creation
- interface: rest
- limits:
  - volume-quota (binding): trial credits, amount and expiry determined by Databricks after account creation; trial ends when credits are exhausted [2]
- endpoint: https://${DATABRICKS_HOST}/ai-gateway/mlflow/v1
- tooling: OpenAI-compatible client or the MLflow Deployments SDK with a Databricks API token
- composes with: trial credits expire and are the scarce link; calls are otherwise pay-per-token
- reliability: if configured in the user's own cloud account, the cloud provider bills for compute during the trial
- notes: doc URL redirected to /foundation-model-apis; trial credits are not a standing free inference tier.
- evidence:
  - [1] 2026-11-18: most Foundation Model APIs are OpenAI-compatible | capture: sha256:6b46af6aa4cfc60bccf6a76b24679816e1dfffc9f3e359bab935054f1b7db80c | quote: Most Foundation Model APIs are compatible with OpenAI
  - [2] 2026-11-18: Databricks is pay-as-you-go and its trial credits are time-limited and end when exhausted | capture: sha256:668555a9bc0e7a2fe588c138ef54ea0ca0b3420c8767f692505257ebf45da871 | quote: Databricks offers you a pay-as-you-go approach with no up-front costs
- sources:
  - [1] https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis
  - [2] https://www.databricks.com/product/pricing

## Databricks Free Edition (default storage / Unity Catalog volumes)

- `storage/databricks-free-edition` | trial-only | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:29.380Z (live) | stale on 2026-12-04
- url https://docs.databricks.com/aws/en/getting-started/free-edition
- disagrees on verdict: `storage/databricks-free-edition` says trial-only, `storage/databricks-free-edition-2` says fails-quota
- free tier: No published byte quota. Free Edition ships 'serverless compute and default storage, so you can immediately start exploring and building'. Default storage is 'a fully managed object storage platform' and in serverless workspaces you can 'create additional catalogs in either default storage or in your own cloud object storage'. Quotas are documented for compute, jobs, pipelines, model serving and apps. Never for bytes. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not addressed in the Free Edition docs. Outbound internet is 'restricted to a limited set of trusted domains', which throttles external egress to non-approved hosts. | metered: no
- identity: email
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
  - [1] 2026-11-19: the first-party limitations page states the compute quota behaviour and data retention | capture: sha256:19ecf3409d4dfec641c26889e3aade6305d0df8a123648dd94c173066efd5b96 | quote: If you exceed your quota, your workspace's compute resources will be shut down and unavailable for the rest of the day (and in extreme cases, the rest of the month). While your compute will be unavailable, your data and settings will not be deleted.
  - [3] 2026-11-19: the first-party default-storage page states the serverless compute requirement | capture: sha256:4c6ec79d2bf97824ba6fcce08f91ea13176dcd3ac737d5dcf600728cf51ae078 | quote: Workspace compute that interacts with default storage must be serverless and Unity Catalog-enabled.
  - [1] 2026-11-19: the first-party limitations page states authentication is email OTP or consumer sign-in, not an institution gate | capture: sha256:19ecf3409d4dfec641c26889e3aade6305d0df8a123648dd94c173066efd5b96 | quote: Authentication is limited to email OTP, Sign in with Google, and Sign in with Microsoft. No SSO or SCIM support.
- sources:
  - [1] https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
  - [2] https://docs.databricks.com/aws/en/getting-started/free-edition
  - [3] https://docs.databricks.com/aws/en/storage/default-storage

## databricks free edition (default storage as an archive)

- `storage/databricks-free-edition-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.921Z (live) | stale on 2026-12-04
- url https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
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
  - [1] 2026-11-19: the first-party page says data is not deleted when quota is exceeded | capture: sha256:19ecf3409d4dfec641c26889e3aade6305d0df8a123648dd94c173066efd5b96 | quote: If you exceed your quota, your workspace's compute resources will be shut down and unavailable for the rest of the day (and in extreme cases, the rest of the month). While your compute will be unavailable, your data and settings will not be deleted.
  - [1] 2026-11-19: the first-party page says only serverless compute is available | capture: sha256:19ecf3409d4dfec641c26889e3aade6305d0df8a123648dd94c173066efd5b96 | quote: Free Edition users only have access to serverless compute resources. Custom compute configurations are not supported.
- sources:
  - [1] https://docs.databricks.com/aws/en/getting-started/free-edition-limitations
