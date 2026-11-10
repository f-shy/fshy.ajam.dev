# CockroachDB Cloud

> cockroachlabs.com | Databases and KV, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cockroachlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/cockroachlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CockroachDB Cloud Basic

- `databases-kv/cockroachdb-basic` | qualifies-with-caveat | evidence documented | binding retention-clamped | category distributed SQL
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T11:10:48.000Z (live) | stale on 2026-11-23
- url https://www.cockroachlabs.com/docs/cockroachcloud/free-trial
- free tier: 'When you sign up for CockroachDB Cloud, your new organization's account starts with $400 in free credits, allowing you to try the product at no cost.' The page states no trial length. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: 10 GiB storage per organization on the recurring allowance; no per-object cap is published
- retention: no trial length is stated; billing starts on the day the last credit is used, or on credit expiry, and a 30-day grace period follows if no payment method is added | source: [1]
- egress: data transfer leaving the cluster is billed separately and the free-trial and Basic plan pages publish no included transfer allowance and no per-GB rate; recorded as a gap after checking both | metered: yes | source: [2]
- identity: email | detail: GitHub, Google, Microsoft or an email address and password; a name, company and email verification on the email path; a payment method only at the end of the trial
- interface: rest, cli
- limits:
  - volume-quota: USD 400 of credits, with no published expiry [1]
- limits note: the trial length is not published; the record's earlier 30 days is not supported by the page
- binding note: the request-unit counter throttles and the storage cap refuses writes, but both are recoverable. The 30-day deletion after the trial credits end is not: it removes every cluster in the organization and the page states they cannot be restored.
- interface detail: the Postgres wire protocol with CockroachDB extensions; a Cloud API and the cockroach CLI
- tooling: psql-compatible clients, the cockroach CLI, the Cloud API
- composes with: the only free tier above 10 GiB of card-free-capable relational storage, if the card question resolves in your favour
- reliability: no inactivity power-off; Request Unit consumption scales to zero when the cluster is idle. The trial path ends in an unrecoverable deletion 30 days after the credits run out without a payment method
- notes: The pricing page carries two different Standard rates and prices the product as 'Cockroach Continuum' from 2026-09-15. RAM is never stated. No arbitrary process can be hosted; the credit buys a managed database.
- evidence note: two first-party pages were read on 2026-10-23: the free-trial page for the credits, the grace period and the deletion sentence, and the Basic plan page for scale-to-zero and the storage-limit behaviour. The deletion after the grace period is unrecoverable, which the word 'interruption' would understate.
- extras:
  - hourly_usd.standard_vcpu: 0.092
  - hourly_usd.mission_critical_vcpu: 0.162
  - hourly_usd.standard_vcpu_footer: 0.057
  - rate_conflict: the Standard card reads USD 0.092 per vCPU-hour and the footer table reads 'Standard from $0.057 / vCPU-hr' on the same page
- evidence:
  - [1] 2026-10-23: quoted: 'your new organization's account starts with $400 in free credits' and 'If the trial ends and a payment method has not been provided, a 30 day grace period begins.'
  - [3] 2026-10-23: quoted: Standard '$0.092 per vCPU-hour', footer 'Standard from $0.057 / vCPU-hr' (the page contradicts itself), Mission Critical $0.162
- sources:
  - [1] https://www.cockroachlabs.com/docs/cockroachcloud/free-trial
  - [2] https://www.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [3] https://www.cockroachlabs.com/pricing/

## CockroachDB Cloud (Basic tier)

- `storage/cockroachdb-cloud` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.cockroachlabs.com/
- free tier: $15/month of free resource consumption per pay-as-you-go org, equivalent to 50 million Request Units AND 10 GiB of storage per month | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 10 GiB storage/month free allowance; 50M RUs/month; 30K RU/sec ceiling on Basic; the legacy 'Serverless free tier' (5 GiB + 50M RUs, no card) has been replaced. Current signup is $400 credit for 30 days then the $15/month Basic allowance. | days: 30 | source: [1] | note: not stated
- egress: Not separately charged (storage + RUs are the meters); but the free allowance is denominated in dollars, so ANY overage converts to a bill. Effectively metered. | metered: yes
- identity: card
- interface: rest, cli
- limits note: 10 GiB storage/month free allowance; 50M RUs/month; 30K RU/sec ceiling on Basic; the legacy 'Serverless free tier' (5 GiB + 50M RUs, no card) has been replaced. Current signup is $400 credit for 30 days then the $15/month Basic allowance.
- interface detail: rest
- tooling: psql / any Postgres wire client (CockroachDB is PG-wire compatible), `cockroach` CLI, Cloud API
- composes with: The $15 credit is per ORG, and the 10 GiB is a monthly allowance, not a permanent bucket. New orgs get a separate $400 30-day trial. There is no documented per-account cap on the number of orgs, so 50 orgs x 10 GiB = 500 GB in principle. But each org requires a distinct signup and a payment method to keep the $15 recurring benefit, which is a much higher friction per byte than Telegram or a drive.
- reliability: Very reliable, but the free tier is a dollar credit rather than a hard quota, so a runaway query or a large storage footprint silently converts to charges. Storage is billed on logical GiB with 3 replicas included.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $15/month of free resource consumption per pay-as-you-go org, equivalent to 50 million Request Units AND 10 GiB of storage per month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Each pay-as-you-go CockroachDB Cloud organization ... is given $15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) for free each month.'
  - [2] 2026-10-21: '$400 in free credits to start—no credit card required'; 'New users get $400 in free credits to use within the first 30 days.'
  - [3] 2026-10-21: '$400 in free-trial free trial credits ... you will need to [add a payment method] by the end of the trial'
- sources:
  - [1] https://docs.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [2] https://www.cockroachlabs.com/free-tier/1a/
  - [3] https://www.cockroachlabs.com/docs/cockroachcloud/quickstart

## CockroachDB Cloud (Basic) / Continuum

- `storage/cockroachdb-cloud-continuum` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.cockroachlabs.com
- free tier: $15/month of free resource consumption per pay-as-you-go org = 50M Request Units + 10 GiB storage/month | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No separate egress charge on Basic. Billing is storage GiB + Request Units. So egress is effectively free within the RU budget, and reads are the meter. | metered: no
- identity: card
- interface: rest, cli
- limits note: 10 GiB/month equivalent; hitting the storage limit blocks writes ('cluster will be unable to write to its storage'); hitting the RU limit disables the cluster until next cycle. Pricing changed for deployments created on/after 2026-09-15 ('Cockroach Continuum').
- interface detail: rest
- tooling: Postgres wire protocol (psql, any driver), `cockroach` CLI, Cloud API; no object storage. Bytes must live in tables/BYTEA.
- composes with: The $15 credit is per ORGANIZATION and explicitly spendable 'across all CockroachDB Basic clusters in an organization'. It is a monthly consumable, not a standing quota. 10 GiB is the storage-equivalent, and multi-region replication multiplies storage 3-5x against the same credit. New orgs get a $400 trial credit on top.
- reliability: Cluster is DISABLED when RU budget is exhausted. A hard stop mid-month, not throttling. Replication factor 3 eats the storage budget 3x.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $15/month of free resource consumption per pay-as-you-go org = 50M Request Units + 10 GiB storage/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '$15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) for free each month ... can be spent across all CockroachDB Basic clusters in an organization'
  - [2] 2026-10-21: 'This pricing applies to Cockroach Continuum for anyone getting started or adding new database deployments on or after September 15, 2026'
- sources:
  - [1] https://www.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [2] https://www.cockroachlabs.com/pricing/
