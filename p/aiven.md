# Aiven

> aiven.io | Databases and KV, Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aiven/ | JSON https://fshy.ajam.dev/api/v1/entity/aiven.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aiven

- `databases-kv/aiven-free` | qualifies-with-caveat | evidence documented | binding retention-clamped | category managed Postgres and friends with a free plan that powers off on inactivity
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://aiven.io/pricing/postgresql
- free tier: Free plan with 1 GB RAM and 1 GB total storage per service, on Postgres, MySQL, Valkey, Kafka and OpenSearch; free indefinitely with no time limit, but the service powers off after a period of inactivity | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 1 GB total storage per service | source: [1]
- retention: the service powers off after a period of inactivity, on three triggers: no initial usage in the first few hours, or no continuative activity later; a powered-off service is deleted after 180 days. The Free plan is the exception to 'data retention is only limited by storage' | days: 180 | source: [2]
- egress: no egress allowance, quota or per-GB rate is published on the free-plan pages or the PostgreSQL pricing table; recorded as a gap after checking both | metered: no | source: [1]
- identity: email | detail: email signup; no card on the Free plan
- interface: rest, cli
- limits:
  - per-object-cap: 1 GB total storage per service; 1 GB RAM [1]
  - retention-clamped (binding): the free service powers off after a period of inactivity; a service powered off for more than 180 days is automatically deleted [2]
  - request-rate: max_connections is set to 20 on a free PostgreSQL service, and there is no connection pooling [3]
- binding note: 1 GB of storage is small, but the inactivity power-off is what defeats the use a reader would pick this for: an unattended job that runs less often than the inactivity window. The 180-day deletion sets the outer limit.
- interface detail: the Postgres wire protocol; an API and the avn CLI
- tooling: psql and any Postgres client; the avn CLI
- composes with: no longer a candidate for a weekly or monthly job: the free service powers off on inactivity and is deleted 180 days after it powers off, so a keep-alive is required and the paid Developer tier is what removes the clock
- reliability: free services power off on inactivity and a service powered off for more than 180 days is automatically deleted; a powered-off service for a version past end of life is deleted within 7…
- notes: 1 GB is the smallest free Postgres storage in this class, and the free plan powers off on inactivity, so it does not answer the question the class was formed to ask. 5 GB is what the plan used to give and several comparison pages still print it. The paid Developer tier at USD 5 a month is the version of this that stays up: 'Developer tier services are not automatically powered off when inactive'.
- evidence note: three first-party Aiven pages were read on 2026-10-22. The pricing page gives 1 GB RAM and 1 GB storage. The free-PostgreSQL page gives the inactivity power-off. The service power-cycle page gives the 180-day deletion. The pricing page's 'with the exception of Free plan' clause is a carve-out and not boilerplate. The free tier is what it carves out.
- evidence:
  - [1] 2026-10-22: Free column: RAM per VM 1 GB, Total storage 1 GB; Developer USD 5 with 8 GB; Hobbyist from USD 12; 'Data retention is only limited by storage, with the exception of Free plan'
  - [4] 2026-10-22: 'Service powers off after a period of inactivity (you'll be notified by email and in-platform beforehand)'; 'It's free indefinitely with no time limit, but the service is automatically powered off after a period of inactivity'
  - [3] 2026-10-22: two power-off triggers: 'Power off free services with no initial usage within the first few hours after the service is running' and 'Power off free services with no continuative activity on the service'
  - [2] 2026-10-22: 'Services powered off for more than 180 days are automatically deleted'; the 180-day grace does not apply to an end-of-life version, which is deleted within 7 days
  - [5] 2026-10-22: 'Developer tier services are not automatically powered off when inactive'; the paid step is what removes the clock
  - [3] 2026-10-22: 'No connection pooling' and '`max_connections` limit set to `20`' on the free tier
- sources:
  - [1] https://aiven.io/pricing/postgresql
  - [2] https://aiven.io/docs/platform/concepts/service-power-cycle
  - [3] https://aiven.io/docs/products/postgresql/concepts/pg-free-tier
  - [4] https://aiven.io/free-postgresql-database
  - [5] https://aiven.io/docs/platform/concepts/free-plan

## Aiven (USD 300 trial)

- `compute/aiven` | trial-only | evidence documented | binding volume-quota | category managed data platform trial credit | tier free trial
- needs card no, phone no, ID no, institution no | verified 2026-10-23T10:57:29.000Z (live) | stale on 2026-11-23
- url https://aiven.io/pricing
- free tier: New accounts include $300 in free credits and no payment details are required to sign up. The documentation states 'Aiven offers a free trial for 30 days with credits you can use to explore the Aiven Platform. You don't need a credit card to sign up.' The amount and the duration are on two different pages. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the offer is a spending balance, not a stored object
- retention: the trial runs 30 days; the free service tier is separate and unlimited | days: 30 | source: [2]
- egress: not stated on the pages read | metered: no | source: [3]
- identity: email | detail: no payment details are required to sign up; Google, Microsoft, GitHub or email; the console is JavaScript-only so the form fields were not observed live
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 300 of credit over a 30-day trial [1]
- limits note: the amount is published on the developer-tier page and the 30 days on the service-pricing documentation; the /free-trial/ path returns 404
- binding note: USD 300 over 30 days is 41.7 cents an hour, and the balance is the only thing that ends the trial
- interface detail: the Aiven console, the Aiven CLI and per-service connection URIs; no general-purpose VM
- tooling: the Aiven CLI, the Terraform provider, and each service's native client
- composes with: the credit pays for managed PostgreSQL, Kafka, Valkey and the rest at list price; it does not buy a machine that runs arbitrary software
- reliability: the free service tier continues indefinitely and is separate from the trial credit, so a service can outlive the balance on the Free plan
- notes: The credit buys managed services only. The smallest paid plans are Developer at $5 a month (1 CPU, 1 GiB, 8 GB) and Hobbyist at $12 a month or $0.02 an hour (1 CPU, 1 GiB, 8 GB). A general-purpose process cannot be hosted here.
- evidence note: two first-party Aiven pages were read on 2026-10-23; the trial URL carried by the search index is dead, so the amount and the duration are each sourced from the page that still carries them
- extras:
  - credit_usd: 300
  - trial_days: 30
  - smallest_paid_plan_usd_month: 5
  - hobbyist_hourly_usd: 0.02
- evidence:
  - [1] 2026-10-23: quoted: 'New accounts include $300 in free credits and no payment details are required to sign up.'
  - [2] 2026-10-23: quoted: 'Aiven offers a free trial for 30 days with credits you can use to explore the Aiven Platform. You don't need a credit card to sign up.'
  - [4] 2026-10-23: 404 on 2026-10-23; no Wayback capture for 2026-10, so the indexed trial URL proves nothing
- sources:
  - [1] https://aiven.io/developer-tier
  - [2] https://aiven.io/docs/platform/concepts/service-pricing
  - [3] https://aiven.io/pricing
  - [4] https://aiven.io/free-trial

## Aiven free tier (PostgreSQL / MySQL / Valkey / OpenSearch / Kafka)

- `storage/aiven-free-tier` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://aiven.io/
- free tier: 1 GB disk each for PostgreSQL, MySQL and Valkey (Valkey maxmemory = 50% of 1 GB RAM = 512 MB usable); 20 GB storage for OpenSearch; Kafka free tier is throughput-capped at 250 KiB/s. 'Only one service of each service type in your organization.' No time limit, no credit card. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. 'Network traffic is not charged separately' (Aiven service pricing doc). This is the best egress term of any structured store here, which makes the tiny byte quotas the only blocker. | metered: no
- identity: card
- interface: rest, cli
- limits note: 1 GB disk (PG/MySQL), 1 GB RAM (Valkey, 50% maxmemory), 20 GB + 4 GB RAM + 2 shards (OpenSearch free), Kafka 250 KiB/s ingress/egress with 5 topics x 2 partitions and fixed retention; single node; no VPC; no static IPs; no forking; `max_connections` 20 on free PG
- interface detail: rest
- tooling: psql / mysql / redis-cli / OpenSearch REST API / any Kafka client; Aiven Terraform provider and `avn` CLI for provisioning; PG-wire and RESP protocols unchanged
- composes with: One service of each type per ORG (verified in the Valkey free-tier doc: 'Only one service of each service type in your organization'). So one org yields ~1 + 1 + 0.5 + 20 GB = ~22.5 GB across four services, plus Kafka. 23 orgs would reach 500 GB. The best per-org yield of any structured store found, and the only one where egress is genuinely free.
- reliability: Aiven 'reserves the right to power off free services with no initial usage in the first few hours' and to power off services with no continuing activity. For a cold archive that means keep-alive traffic is mandatory or the service sleeps. No data loss reported, just power-off.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB disk each for PostgreSQL, MySQL and Valkey (Valkey maxmemory = 50% of 1 GB RAM = 512 MB usable); 20 GB storage for OpenSearch; Kafka free tier is throughput-capped at 250 KiB/s. 'Only one service of each service type in your organization.' No time limit, no credit card.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The Free tier is available for the following service types: Apache Kafka, MySQL, OpenSearch, PostgreSQL, Valkey'; 'You don't need a credit card ... use them indefinitely free of charge'; 'Aiven reserves the right to power off free services with no initial usage ... Power off free services with no continuative activity'
  - [2] 2026-10-21: '1 GB RAM', '1 GB disk storage'
  - [3] 2026-10-21: '1 GB disk storage'; https://aiven.io/docs/products/valkey/concepts/valkey-free-tier — '1 GB RAM', 'maxmemory set to 50%', 'Only one service of each service type in your organization'
  - [4] 2026-10-21: '4 GB RAM, 20 GB storage', '2 shards', 'Max 20 shards per node', '50 concurrent connections'
  - [5] 2026-10-21: 'Streaming throughput up to 250 KiB/s ingress and 250 KiB/s egress', 'Up to 5 topics, each with two partitions'
  - [6] 2026-10-21: 'Network traffic is not charged separately'
- sources:
  - [1] https://aiven.io/docs/platform/concepts/free-plan
  - [2] https://aiven.io/docs/products/postgresql/concepts/pg-free-tier
  - [3] https://aiven.io/docs/products/mysql/concepts/mysql-free-tier
  - [4] https://aiven.io/docs/products/opensearch/concepts/opensearch-free-tier
  - [5] https://aiven.io/docs/products/kafka/free-tier/kafka-free-tier
  - [6] https://aiven.io/docs/platform/concepts/service-pricing
