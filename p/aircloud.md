# Aircloud

> aircloud.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aircloud/ | JSON https://fshy.ajam.dev/api/v1/entity/aircloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aircloud (aircloud.dev)

- `compute/aircloud-dev` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-06T18:39:12.190Z (live) | stale on 2026-12-07
- url https://aircloud.dev/pricing
- free tier: no free credit or trial is stated on the pages read: every product bills against a prepaid balance, and signup needs only an email address, 'no card required until you add credit'. | unit: none | metered on: wall-clock | read on: 2026-11-06 | source: [1]
- per-object cap: not applicable | source: [2] | note: a machine record
- retention: not applicable | source: [2] | note: volumes bill per GB-hour while they exist; an unused volume bills until deleted
- egress: Outbound network transfer off a container, job, or endpoint isn’t billed separately from compute. | metered: no | free allowance: unmetered | source: [2]
- identity: card | detail: Signup needs an email address ('no card required until you add credit'); adding credit needs a card, since a top-up with no payment method on file is refused with 'add a card first' and the payment methods are Stripe cards. Reserved clusters are quoted through a form that asks for name, work email and company. Whether signup asks for a phone number is unverified: behind a sign-up.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): the prepaid balance is the quota: usage is denied once the balance reaches zero, and a dedicated endpoint, container or job bills every second it is up whether or not it is working [3]
- limits note: no free allowance; the published starting rates cover A100 80GB, H100 SXM, H200 SXM, B200, B300 and GB200 only
- binding note: the same as limits note
- interface detail: the air CLI, the REST API and the dashboard drive the same control plane; containers are reached over SSH. Not probed.
- tooling: the `air` CLI (for example `air price --gpu h100:2`, `air gpu list`, `air job submit`), a REST API at api.aircloud.dev, a dashboard at app.aircloud.dev, and SSH into a GPU container
- composes with: Reserved clusters are the purchasable route on the marketing pricing page: 60 months, single tenant, one exit at month 36, from USD 3.00 per GPU-hour for an HGX B200 and USD 3.50 for an HGX B300, with H200, H100 and A100 nodes quoted per cluster. On-demand containers, jobs and dedicated endpoints, which the docs price per GPU-hour with egress unmetered, are listed as 'opening soon' behind a waitlist.
- reliability: unverified: no status page or incident history was read
- notes: Per-card rates, USD per GPU-hour. The marketing pricing page prices reserved clusters only, on a 60-month term, single tenant: HGX B300 from USD 3.50, HGX B200 from USD 3.00, GB200 NVL72 from USD 4.00, GB300 NVL72 from USD 5.00 and VR200 NVL72 from USD 6.50, with one exit at month 36. On that page H100 SXM and A100 are quoted per cluster with no rate, L40S, RTX 4090 and L4 are not listed, and on-demand and small jobs are 'opening soon' behind a waitlist. The docs pricing page still publishes on-demand from-rates for its six accelerator classes and states that those rates are published at aircloud.dev/pricing, which does not publish them; the docs rows in this record's evidence carry the figures. No free tier is stated on either page.
- evidence:
  - [2] 2026-11-03: the published on-demand starting rate for an A100 80GB is USD 1.39 per GPU-hour (the table header reads 'From (on-demand, per GPU-hour)') | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: | A100 80GB | $1.39 |
  - [2] 2026-11-03: the published on-demand starting rate for an H100 SXM is USD 2.49 per GPU-hour | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: | H100 SXM | $2.49 |
  - [4] 2026-11-03: reserved cluster starting rates per GPU-hour on a 60-month term | capture: sha256:fa322092a28782b54b9c5ec7ff49b0dde2ab2f20fd17bcf61e78312fb2928ea8 | quote: On a 60-month term: HGX B300 from US$3.50, HGX B200 from US$3.00, GB200 NVL72 from US$4.00, GB300 NVL72 from US$5.00, Vera Rubin NVL72 (VR200) from US$6.50.
  - [4] 2026-11-03: on the reserved-cluster page the H200, H100 and A100 nodes are quoted per build, with 48 or 60 month terms | capture: sha256:fa322092a28782b54b9c5ec7ff49b0dde2ab2f20fd17bcf61e78312fb2928ea8 | quote: H200, H100 and A100 nodes and every 48-month term are quoted per build.
  - [2] 2026-11-03: egress off a container, job or endpoint is not a separate charge | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: Outbound network transfer off a container, job, or endpoint isn’t billed separately from compute.
  - [1] 2026-11-03: signup needs an email address and no card until credit is added | capture: sha256:378387dcf02440b684ccd692513167b9fe661a796279315ecabf17fa99fabfc0 | quote: An email address to sign up with (no card required until you add credit).
  - [3] 2026-11-03: adding credit needs a card on file; the payment methods are Stripe cards | capture: sha256:731cc8c35c39707298d5b31416e637b4187517129940a6484dfdc6bbf467ffb9 | quote: If you have none on file yet, the top-up returns `422` naming the problem — add a card first (above).
  - [3] 2026-11-03: payment methods are Stripe cards | capture: sha256:731cc8c35c39707298d5b31416e637b4187517129940a6484dfdc6bbf467ffb9 | quote: Payment methods are Stripe cards attached to your organization.
  - [2] 2026-11-03: the launchable GPU classes are a live catalog; L40S, RTX 4090 and L4 are not in the published starting-rate table | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: Which accelerators you can actually launch (and at what rate) is a live catalog, not a fixed list — capacity changes.
  - [5] 2026-11-03: containers are reached over SSH; the air CLI, REST API and dashboard drive one control plane | capture: sha256:20ee72d1ef61664f57704ce23ac13d16a5a5dcb5a66a055cedd048475ebfb274 | quote: SSH into a GPU container running the image you picked. Full root, forwarded ports, your workflow.
  - [3] 2026-11-03: the prepaid balance is enforced: usage is denied once the balance reaches zero | capture: sha256:731cc8c35c39707298d5b31416e637b4187517129940a6484dfdc6bbf467ffb9 | quote: There’s no grace period on the API side once balance hits zero
  - [6] 2026-11-03: a third-party index lists only the reserved-cluster rates for this provider, not the on-demand containers | capture: sha256:8f6e047f7f889857612dd49b61661d571d8c23e5e7525806e178570b121c57bc | quote: Aircloud offers dedicated GPU clusters and private nodes tailored for specific customer needs.
  - [4] 2026-11-06: the marketing pricing page quotes the H100 SXM per cluster instead of publishing a rate | capture: sha256:9ee6b22df9cbe161f2287f2d7017cee8e13d31616a78dc6500a5979058184d31 | quote: | H100 SXM | Nodes of 8 GPUs | Quoted |
  - [4] 2026-11-06: on-demand is not purchasable: the marketing page puts it behind a waitlist | capture: sha256:9ee6b22df9cbe161f2287f2d7017cee8e13d31616a78dc6500a5979058184d31 | quote: On-demand and small jobs run on the Aircloud Platform, opening soon.
  - [2] 2026-11-06: the docs pricing table still prices an H100 SXM at USD 2.49 per GPU-hour on demand | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: | H100 SXM | $2.49 |
  - [4] 2026-11-06: the marketing page quotes H200, H100 and A100 nodes per cluster with no published rate | capture: sha256:9ee6b22df9cbe161f2287f2d7017cee8e13d31616a78dc6500a5979058184d31 | quote: H200, H100 and A100 nodes are quoted per cluster.
  - [4] 2026-11-06: on-demand and small jobs are announced as opening soon, behind a waitlist | capture: sha256:9ee6b22df9cbe161f2287f2d7017cee8e13d31616a78dc6500a5979058184d31 | quote: On-demand and small jobs run on the Aircloud Platform, opening soon.
  - [2] 2026-11-06: the docs on-demand table ends at GB200, so it lists six classes and no L40S, RTX 4090 or L4 | capture: sha256:b485e6d61161a120a48e3f8ad1dfe2200487d1e7440eb9cac965e317a9026f60 | quote: | GB200 | $6.60 |
  - [4] 2026-11-06: the reserved term is 60 months only, with no one-year or pilot term | capture: sha256:9ee6b22df9cbe161f2287f2d7017cee8e13d31616a78dc6500a5979058184d31 | quote: No. Every cluster is reserved for 60 months, with one exit at the end of month 36. There are no one-year or pilot terms.
- sources:
  - [1] https://docs.aircloud.dev/quickstart
  - [2] https://docs.aircloud.dev/pricing
  - [3] https://docs.aircloud.dev/account/billing
  - [4] https://aircloud.dev/pricing
  - [5] https://docs.aircloud.dev/
  - [6] https://computeprices.com/providers/aircloud
