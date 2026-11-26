# ScaleGrid

> scalegrid.io | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scalegrid/ | JSON https://fshy.ajam.dev/api/v1/entity/scalegrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ScaleGrid

- `databases-kv/scalegrid` | trial-only | evidence documented | binding retention-clamped | category hosted managed database service for MongoDB, Redis, MySQL and PostgreSQL
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.768Z (live) | stale on 2026-12-20
- url https://help.scalegrid.io/docs/trial-accounts-limitations
- free tier: No free plan. A 7-day free trial of the fully managed DBaaS platform is available with no credit card; signup asks for an email and a new password. Trial Dedicated Hosting is limited to one Micro-sized standalone instance per database type. If no payment method is entered by the end of the 7 days, the cluster is automatically deleted. | unit: none | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: The 7-day trial is time-limited and ends in deletion of the cluster unless a payment method is added. There is no recurring free allowance.
- per-object cap: No per-object cap is published on the pages read. The trial Dedicated Hosting limit is one Micro-sized standalone instance per database type. | source: [1]
- retention: If a payment method has not been entered by the end of the free 7-day trial period, the cluster is automatically deleted. Paid Dedicated Hosting includes up to 5 free backups per deployment, with additional backups for a fee. | days: 7 | source: [1]
- egress: Dedicated Hosting and Shared Hosting plans include all data transfer costs; Bring Your Own Cloud plans use the standard transfer rights of the connected cloud provider. | metered: no | source: [2]
- identity: email | detail: signup asks for an email and a new password with no credit card required; the Getting Started page specifies a business email. All accounts start as a trial and require a payment method only to continue after the 7 days. No phone number or identity document is shown.
- interface: rest, cli, browser
- limits:
  - retention-clamped (binding): cluster automatically deleted at the end of the 7-day trial if a payment method has not been entered [1]
  - volume-quota: one Micro-sized standalone instance per database type during the Dedicated Hosting trial; clone, Peek at Backup and Scaling are not supported in the trial [1]
- binding note: the 7-day trial clock deletes the cluster unless a payment method is added, so the retention limit fails before the one-instance-per-type quota or any paid price
- interface detail: a web management console and a documented API; clusters speak the native wire protocol of the selected database engine
- tooling: the native client for the chosen engine (mongosh, redis-cli, mysql, psql); the ScaleGrid Console and its API
- composes with: a managed cluster hosted on AWS, Azure, GCP, OCI, Linode or DigitalOcean on Dedicated Hosting, or in the reader's own cloud account on Bring Your Own Cloud
- reliability: the trial ends in automatic deletion of the cluster if no payment method is entered; Shared Hosting is no longer supported for new customer signups
- notes: ScaleGrid is a hosted managed database service, not software the reader runs. Its only no-cost path is a 7-day trial that deletes the cluster unless a payment method is added. The cheapest paid dedicated PostgreSQL plan is USD 13 per month. Shared Hosting, once a low-cost tier, is closed to new signups.
- evidence note: four first-party pages were captured and quoted on 2026-11-19: the trial limitations page, the Getting Started page, the pricing FAQ and the Dedicated Hosting plans page. The trial terms, signup fields and price come from those pages. No probe was run, so the rung stays documented.
- self hosted: no
- evidence:
  - [1] 2026-11-19: a 7-day free trial with no card; signup asks for an email and a new password | capture: sha256:3d5f9d376fc58bbe1013bad427e15349d8a20dd7e87d9100c1bc222633529ff6 | quote: At ScaleGrid, we provide a [free 7-day trial](https://console.scalegrid.io/users/register) so you can explore all the features in our fully managed DBaaS plans to decide whether our platform is right for you. No credit card required to sign up, simply enter your email and a new password to get access to your own personal database management and monitoring console.
  - [1] 2026-11-19: the Dedicated Hosting trial is limited to one Micro standalone instance per database type | capture: sha256:3d5f9d376fc58bbe1013bad427e15349d8a20dd7e87d9100c1bc222633529ff6 | quote: 1. During the trial period, you are limited to one Micro-sized standalone instance per database type.
  - [1] 2026-11-19: the cluster is deleted at the end of the 7-day trial without a payment method | capture: sha256:3d5f9d376fc58bbe1013bad427e15349d8a20dd7e87d9100c1bc222633529ff6 | quote: 1. If a payment method has not been entered by the end of your free 7-day trial period, your cluster will be automatically deleted.
  - [3] 2026-11-19: signup asks for a business email and a password with no card | capture: sha256:cdc6bdf685227058c6a1ae3dabfcbae3ed19c302599d65ee7257363c70bc9e53 | quote: Just enter a business email and a password, no credit card required.
  - [2] 2026-11-19: the 7-day free trial requires no credit card | capture: sha256:b341a708904ed6e8290545b93f7e6c35d67531c104d015baf76937869872d8d1 | quote: You bet! Try any of our plans free through our 7-day free trial, no credit card required.
  - [2] 2026-11-19: Shared Hosting is closed to new signups | capture: sha256:b341a708904ed6e8290545b93f7e6c35d67531c104d015baf76937869872d8d1 | quote: > 🚧 Shared Hosting is no longer supported for new customer signups.
  - [4] 2026-11-19: the cheapest dedicated PostgreSQL plan starts at USD 13 per month | capture: sha256:ce3c24dfaa8a45463259e14a32cc314ebd8e3aea2c5939b30d2535df2ec58e51 | quote: PostgreSQL:[Starts at $13/month](https://scalegrid.io/pricing/?plan=0\&replicaType=standalone\&databaseType=postgresql\&cloudType=digitalocean#section_pricing_byoc)
- sources:
  - [1] https://help.scalegrid.io/docs/trial-accounts-limitations
  - [2] https://help.scalegrid.io/docs/scalegrid-pricing-faq
  - [3] https://help.scalegrid.io/docs/getting-started
  - [4] https://help.scalegrid.io/docs/getting-started-dedicated-hosting-plans
