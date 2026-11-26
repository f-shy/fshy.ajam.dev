# CockroachDB Cloud

> cockroachlabs.com | Databases and KV, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cockroachlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/cockroachlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CockroachDB Cloud Basic

- `databases-kv/cockroachdb-basic` | qualifies-with-caveat | evidence documented | binding retention-clamped | category distributed SQL
- needs card yes, phone no, ID no, institution no | verified 2026-11-09T14:11:26.569Z (live) | stale on 2026-12-10
- url https://www.cockroachlabs.com/docs/cockroachcloud/free-trial
- free tier: 'When you sign up for CockroachDB Cloud, your new organization's account starts with $400 in free credits, allowing you to try the product at no cost.' The page states no trial length. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: 10 GiB storage per organization on the recurring allowance; no per-object cap is published
- retention: trial credits last until used or expired; without a payment method, a 30-day grace period follows in which clusters are throttled and cannot be reconfigured, then all clusters in the organization are deleted and cannot be restored | days: 30 | source: [1] | note: the 30 days is the post-trial grace period before deletion, counted from the day the last credit is used or the credit expires, not from account creation; adding a payment method during the grace period fully restores the clusters
- egress: data transfer leaving the cluster is billed separately and the free-trial and Basic plan pages publish no included transfer allowance and no per-GB rate; recorded as a gap after checking both | metered: yes | source: [2]
- identity: email | detail: GitHub, Google, Microsoft or an email address and password; a name, company and email verification on the email path; a payment method only at the end of the trial
- interface: rest, cli
- limits:
  - volume-quota: USD 400 of credits, with no published expiry [1]
- limits note: the trial length is not published; the 30 days in retention.days is the post-trial grace period before deletion, not a trial length
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
  - [1] 2026-11-09: a 30 day grace period follows the trial when no payment method is added, in which clusters are throttled and cannot be reconfigured, and all clusters are then deleted and cannot be restored | capture: sha256:41204f7a65b0554a7a9e495f92ca821f14db475bb63f0be05cdedc33c7e2830e | quote: Monthly billing begins when the free trial ends: on the day that the last credit is used, or upon expiration of credit, if any remains. ... If the trial ends and a payment method has not been provided, a 30 day grace period begins where your organization’s clusters are throttled, and you are restricted from modifying their configuration, for example, to scale up or down, or update regions. ... If the end of the grace period is reached and no payment method has been added, all clusters in the organization are deleted. Deleted clusters can not be restored.
  - [1] 2026-11-09: billing and the grace period start when the last credit is used or the credit expires, and adding a payment method during the grace period fully restores the clusters | capture: sha256:41204f7a65b0554a7a9e495f92ca821f14db475bb63f0be05cdedc33c7e2830e | quote: Monthly billing begins when the free trial ends: on the day that the last credit is used, or upon expiration of credit, if any remains. ... If the trial ends and a payment method has not been provided, a 30 day grace period begins where your organization’s clusters are throttled, and you are restricted from modifying their configuration, for example, to scale up or down, or update regions. ... The cluster will be fully restored if a payment method is added.
  - [1] 2026-11-09: the page states a 30 day grace period and publishes no trial length | capture: sha256:41204f7a65b0554a7a9e495f92ca821f14db475bb63f0be05cdedc33c7e2830e | quote: If the trial ends and a payment method has not been provided, a 30 day grace period begins where your organization’s clusters are throttled, and you are restricted from modifying their configuration, for example, to scale up or down, or update regions.
- sources:
  - [1] https://www.cockroachlabs.com/docs/cockroachcloud/free-trial
  - [2] https://www.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [3] https://www.cockroachlabs.com/pricing/

## CockroachDB Cloud (Basic tier)

- `storage/cockroachdb-cloud` | fails-quota | evidence reported | binding volume-quota | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.914Z (live) | stale on 2026-12-04
- url https://www.cockroachlabs.com/
- free tier: $15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) free each month for pay-as-you-go organizations | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 10 GiB storage/month free allowance; 50M RUs/month; 30K RU/sec ceiling on Basic; the legacy 'Serverless free tier' (5 GiB + 50M RUs, no card) has been replaced. Current signup is $400 credit for 30 days then the $15/month Basic allowance. | days: 30 | source: [1] | note: not stated
- egress: Not separately charged (storage + RUs are the meters); but the free allowance is denominated in dollars, so ANY overage converts to a bill. Effectively metered. | metered: yes
- identity: card
- interface: rest, cli
- limits:
  - volume-quota (binding): Storage limit blocks writes once the monthly storage allowance is reached [1]
- limits note: 10 GiB storage/month free allowance; 50M RUs/month; 30K RU/sec ceiling on Basic; the legacy 'Serverless free tier' (5 GiB + 50M RUs, no card) has been replaced. Current signup is $400 credit for 30 days then the $15/month Basic allowance.
- binding note: the storage limit is a hard volume quota that blocks writes when the allowance is reached
- interface detail: rest
- tooling: psql / any Postgres wire client (CockroachDB is PG-wire compatible), `cockroach` CLI, Cloud API
- composes with: The $15 credit is per ORG, and the 10 GiB is a monthly allowance, not a permanent bucket. New orgs get a separate $400 30-day trial. There is no documented per-account cap on the number of orgs, so 50 orgs x 10 GiB = 500 GB in principle. But each org requires a distinct signup and a payment method to keep the $15 recurring benefit, which is a much higher friction per byte than Telegram or a drive.
- reliability: Very reliable, but the free tier is a dollar credit rather than a hard quota, so a runaway query or a large storage footprint silently converts to charges. Storage is billed on logical GiB with 3 replicas included.
- notes: $15/month of free resource consumption per pay-as-you-go org, equivalent to 50 million Request Units AND 10 GiB of storage per month
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $15/month of free resource consumption per pay-as-you-go org, equivalent to 50 million Request Units AND 10 GiB of storage per month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Each pay-as-you-go CockroachDB Cloud organization ... is given $15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) for free each month.'
  - [2] 2026-10-21: '$400 in free credits to start—no credit card required'; 'New users get $400 in free credits to use within the first 30 days.'
  - [3] 2026-10-21: '$400 in free-trial free trial credits ... you will need to [add a payment method] by the end of the trial'
  - [1] 2026-11-19: Each pay-as-you-go Basic org gets $15/month = 50M Request Units + 10 GiB storage free | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: given \$15 of resource consumption (equivalent to 50 million [Request Units](#request-units) and 10 GiB of storage) for free each month.
  - [1] 2026-11-19: Storage limit is a hard volume quota that blocks writes | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: If you reach your storage limit, your cluster will be unable to write to its storage unless you delete data or increase your storage limit.
  - [1] 2026-11-19: Storage limit is a hard quota that stops writes | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: If you reach your storage limit, your cluster will be unable to write to its storage unless you delete data or increase your storage limit.
  - [1] 2026-11-19: Storage metered in GiB per billing period; no per-object cap; no object-store interface | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: cluster storage is measured in GiB and is based on the total amount of storage your cluster used over a billing period
- sources:
  - [1] https://docs.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [2] https://www.cockroachlabs.com/free-tier/1a/
  - [3] https://www.cockroachlabs.com/docs/cockroachcloud/quickstart

## CockroachDB Cloud (Basic) / Continuum

- `storage/cockroachdb-cloud-continuum` | fails-quota | evidence reported | binding volume-quota | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.914Z (live) | stale on 2026-12-04
- url https://www.cockroachlabs.com
- free tier: $15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) free each month, spendable across all Basic clusters in an organization | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Data transfer is not included in the Continuum estimate and is billed separately on data leaving the cluster. | metered: no
- identity: card
- interface: rest, cli
- limits:
  - volume-quota (binding): Storage limit blocks writes once the monthly storage allowance is reached [2]
- limits note: 10 GiB/month equivalent; hitting the storage limit blocks writes ('cluster will be unable to write to its storage'); hitting the RU limit disables the cluster until next cycle. Pricing changed for deployments created on/after 2026-09-15 ('Cockroach Continuum').
- binding note: the storage limit is a hard volume quota that blocks writes when the allowance is reached
- interface detail: rest
- tooling: Postgres wire protocol (psql, any driver), `cockroach` CLI, Cloud API; no object storage. Bytes must live in tables/BYTEA.
- composes with: The $15 credit is per ORGANIZATION and explicitly spendable 'across all CockroachDB Basic clusters in an organization'. It is a monthly consumable, not a standing quota. 10 GiB is the storage-equivalent, and multi-region replication multiplies storage 3-5x against the same credit. New orgs get a $400 trial credit on top.
- reliability: Cluster is DISABLED when RU budget is exhausted. A hard stop mid-month, not throttling. Replication factor 3 eats the storage budget 3x.
- notes: $15/month of free resource consumption per pay-as-you-go org = 50M Request Units + 10 GiB storage/month
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $15/month of free resource consumption per pay-as-you-go org = 50M Request Units + 10 GiB storage/month
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '$15 of resource consumption (equivalent to 50 million Request Units and 10 GiB of storage) for free each month ... can be spent across all CockroachDB Basic clusters in an organization'
  - [3] 2026-10-21: 'This pricing applies to Cockroach Continuum for anyone getting started or adding new database deployments on or after September 15, 2026'
  - [2] 2026-11-19: The $15/50M RU/10 GiB monthly benefit is per organization and shared across its Basic clusters | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: for free each month. Every monthly billing cycle, this free monthly resource benefit can be spent across all CockroachDB Basic clusters in an organization.
  - [3] 2026-11-19: Continuum bills egress separately from the estimate | capture: sha256:2145bf89bc755cde161102e66e734130594a95983e497d40f7ce769b2e4ab881 | quote: Data transfer is not included in the estimate and is billed separately on data leaving the cluster.
  - [2] 2026-11-19: Storage limit is a hard volume quota that blocks writes | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: If you reach your storage limit, your cluster will be unable to write to its storage unless you delete data or increase your storage limit.
  - [2] 2026-11-19: Storage limit is a hard quota that stops writes | capture: sha256:02dcf34faf8aaa9e4b036056e041282d794bf1536d5b12558d1f162e8ca9be6f | quote: If you reach your storage limit, your cluster will be unable to write to its storage unless you delete data or increase your storage limit.
  - [3] 2026-11-19: Continuum organization signup needs no credit card | capture: sha256:2145bf89bc755cde161102e66e734130594a95983e497d40f7ce769b2e4ab881 | quote: Create a free Continuum Cloud organization and run your first workload in minutes. No credit card required.
  - [3] 2026-11-19: Continuum pricing applies to deployments created on or after 2026-09-15 | capture: sha256:2145bf89bc755cde161102e66e734130594a95983e497d40f7ce769b2e4ab881 | quote: This pricing applies to Cockroach Continuum for anyone getting started or adding new database deployments on or after September 15, 2026.
- sources:
  - [1] https://www.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [2] https://docs.cockroachlabs.com/docs/cockroachcloud/plan-your-cluster-basic
  - [3] https://www.cockroachlabs.com/pricing/
