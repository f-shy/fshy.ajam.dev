# Supabase

> supabase.com | Compute, Databases and KV, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/supabase/ | JSON https://fshy.ajam.dev/api/v1/entity/supabase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Supabase (Compute)

- `compute/supabase` | qualifies-with-caveat | evidence reported | category managed database
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:24:38.000Z (live) | stale on 2026-11-06
- url https://supabase.com/pricing
- duplicate of `databases-kv/supabase`
- free tier: a free project with 500 MB RAM, a 500 MB database, 5 GB of egress, 1 GB of file storage and 50k monthly active users | unit: GiB | metered on: stored-bytes | read on: 2026-10-06 | source: [1] | note: projects are paused after a week of inactivity, limit 2 active projects
- per-object cap: not applicable
- retention: free projects are paused after 1 week of inactivity; data is retained while paused | days: 7 | source: [1]
- egress: 5 GB a month included, then metered | metered: yes | free allowance: 5 GB a month | source: [1]
- identity: email | detail: an account; no card on the free plan
- interface: ssh
- limits:
  - retention-clamped: a free project is paused after 1 week without activity [1]
  - request-rate: 2 active projects on the free plan [1]
  - per-ip-shaping: 5 GB of egress a month [1]
- limits note: a weekly API call or database query is enough to keep the project awake
- interface detail: a Postgres connection string plus a REST and GraphQL API; Edge Functions on Deno
- tooling: the supabase CLI, the client SDKs, Postgres clients, Deno for Edge Functions
- composes with: Edge Functions give an always-on process with a public URL on a free project, kept awake by a weekly query
- reliability: no reliability event recorded
- notes: Supabase provides PostgreSQL databases with Edge Functions supporting serverless compute execution under free monthly invocation limits.
- evidence note: re-read live on 2026-10-22 for the free-tier and limit figures
- extras:
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: paused after 1 week of inactivity
  - persistent_storage.included_gib: 1
  - persistent_storage.price_gib_month: 1 GB of file storage included
  - persistent_storage.durability: Postgres and file storage
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while the project exists
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: HTTPS through the API
  - network_out.per_session_bytes: 5 GB a month
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-06: 'Free projects are paused after 1 week of inactivity. Limit of 2 active projects.'
  - [1] 2026-10-22: read live: free projects pause after a week idle; 2 active project limit
- sources:
  - [1] https://supabase.com/pricing

## Supabase (Databases and KV)

- `databases-kv/supabase` | qualifies-with-caveat | evidence documented | binding retention-clamped | category managed Postgres with auth and storage
- needs card no, phone no, ID no, institution no | verified 2026-11-09T12:14:25.959Z (live) | stale on 2026-12-10
- url https://supabase.com/pricing
- price parsed USD 25/mo
- free tier: 500 MB database on Shared CPU with 500 MB RAM; 2 active projects; 5 GB egress and 5 GB cached egress; unlimited API requests | unit: mixed | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 500 MB per project database | source: [1]
- retention: a Free project is paused after 1 week of low activity, and is restorable for up to 1 year after the pause. A paid project is never paused | source: [2] | note: the pause trigger is activity, not age: a few user requests a day over the previous week keep it awake
- egress: 5 GB egress and 5 GB cached egress per month included. The Free plan publishes no overage price, so the fifth gigabyte is a wall and not a bill | metered: no | free allowance: 5 GB egress, 5 GB cached egress | source: [1]
- identity: email | detail: sign-up with an email address and password, or a GitHub, ChatGPT or SSO account
- interface: rest, cli
- limits:
  - retention-clamped (binding): paused after 1 week of low activity; restorable for up to 1 year [2]
  - per-object-cap: 500 MB per database [1]
  - request-rate: 2 active projects per account; paused projects do not count against the limit [3]
  - request-rate: 5 GB egress per month with no published overage path on Free [1]
  - request-rate: connections are set by the compute size and not published as a single number; the free plan runs Nano compute with up to 0.5 GB of RAM, and the pooler queues above the direct limit rather than raising it [4]
- limits note: the shared pooler is IPv4-only on every plan; a direct connection is IPv6-only without the paid IPv4 add-on, so an IPv4-only host must use the pooler
- interface detail: Postgres wire protocol; a PostgREST data API; a Management API and the Supabase CLI
- tooling: psql and any Postgres client; the supabase CLI; PostgREST over HTTP
- composes with: a free Postgres plus free auth plus free object storage in one project, which is the whole reason to pick it over a bare Postgres
- reliability: two warning emails precede an automatic pause, one about a week ahead and one on the pause; restore is a dashboard action, not an API call on the free plan
- notes: Projects on paid plans are not paused for inactivity, so the smallest paid step removes the Free plan's 1-week inactivity pause. That step is Pro, from USD 25 a month: a single database-only project on Micro compute costs USD 25 a month before usage beyond the included quotas, and additional projects add their full compute cost. Pro includes an 8 GB disk per project (then USD 0.125 per GB), 250 GB egress (then USD 0.09 per GB), 250 GB cached egress (then USD 0.03 per GB), 100 GB file storage (then USD 0.0213 per GB) and 100,000 monthly active users (then USD 0.00325 per MAU), plus daily backups stored for 7 days, 7-day log retention and email support. A USD 10 a month compute credit covers one Micro instance, and spend caps are on by default.
- evidence note: the pricing page and the pausing guide were read; nothing was provisioned. The 90-day restore window stated in the 2024-06-24 changelog has since been widened to 1 year.
- extras:
  - monthly_usd: 25
- evidence:
  - [1] 2026-10-22: 500 MB database, 2 active projects, 5 GB egress, 5 GB cached egress, 'Free projects are paused after 1 week of inactivity', and the plan table row Pausing: After 1 week of inactivity
  - [2] 2026-10-22: 'Supabase pauses Free Plan projects that show low activity over a 7-day period'; restore is available 'for up to 1 year after it was paused'; a few user requests a day over a week prevent…
  - [3] 2026-10-22: two free projects across all organizations where you are Owner or Administrator; paused projects do not count toward the free project limit
  - [5] 2026-10-22: the 2024-06-24 change set the restore window at 90 days, which the current doc has since widened to 1 year
  - [6] 2026-10-22: the shared Supavisor pooler is multi-tenant and IPv4-only; the dedicated PgBouncer pooler needs a paid plan
  - [4] 2026-10-22: Nano compute is the free plan at USD 0 with up to 0.5 GB of RAM and a recommended 500 MB database; 'Database max connections are recommended values and can be customized via max_connections', so the compute size sets the count
  - [1] 2026-11-09: Pro costs USD 25 a month and includes the listed quotas, compute credit and spend caps | capture: sha256:1fe5ef1f0e24f26e3d6ac2bf82b29b1bd758e708755830e9d059dd5b3eb964b5 | quote: Pro: from $25/month, including 8 GB disk size per project and $10/month in compute credits that cover one project on Micro compute.
  - [7] 2026-11-09: the sign-up form offers an email address and password, GitHub, ChatGPT and SSO | capture: sha256:6806be3ce5703a020fa537448e5b496fc56164b8e8d7f00855dd0f96ab1c4427 | quote: Create a new account ... Continue with GitHub ... Continue with ChatGPT ... Continue with SSO ... Email ... Password ... Sign up
  - [8] 2026-11-09: a paid plan requires a credit card on file | capture: sha256:d08aa1479af2e7a9a44da5e9e7f5e1d2d52c33a4b3178679a79785193d964ecb | quote: Paid plans require a credit card to be on file.
  - [1] 2026-11-09: the Free plan includes unlimited API requests, a 500 MB database on Shared CPU with 500 MB RAM, 5 GB egress, 5 GB cached egress and 2 active projects | capture: sha256:1fe5ef1f0e24f26e3d6ac2bf82b29b1bd758e708755830e9d059dd5b3eb964b5 | quote: Unlimited API requests ... 500 MB database size (Shared CPU • 500 MB RAM) ... 5 GB egress ... 5 GB cached egress ... Limit of 2 active projects.
  - [2] 2026-11-09: the 7-day window is the low-activity trigger, restoration is possible for up to 1 year after a pause, and paid projects are never paused; the page states no fixed days-to-loss | capture: sha256:2794bb73d71217ba17c5d3fb4ed01ba2feb5bfab23192bb2686f5283ca133d31 | quote: Supabase pauses Free Plan projects that show low activity over a 7-day period ... You can restore a paused project for up to 1 year after it was paused ... Projects under a paid plan cannot be paused and are not subject to automatic pausing for inactivity.
- sources:
  - [1] https://supabase.com/pricing
  - [2] https://supabase.com/docs/guides/platform/free-project-pausing
  - [3] https://supabase.com/docs/guides/platform/billing-on-supabase
  - [4] https://supabase.com/docs/guides/platform/compute-and-disk
  - [5] https://supabase.com/changelog/27497-paused-free-plan-projects-are-restorable-for-90-days
  - [6] https://supabase.com/docs/guides/database/connecting-to-postgres/pooling-and-limits
  - [7] https://supabase.com/dashboard/sign-up
  - [8] https://supabase.com/docs/guides/platform/get-set-up-for-billing

## Supabase (Storage)

- `storage/supabase` | fails-egress | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:25.205Z (live) | stale on 2026-12-04
- url https://supabase.com
- free tier: 1 GB file storage. PER ORGANIZATION, not per project; 5 GB egress + 5 GB cached egress per org; 2 free projects per user (across all orgs). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 50 MB max file size on Free (global limit, cannot raise); 1 GB storage/org; projects paused after 7 days inactivity and must be manually restored; storage metered in GB-Hours so deleting late in the month barely helps; 5 GB egress hard-capped (overage not purchasable on Free). | days: 7 | source: [1] | note: not stated
- egress: 5 GB uncached + 5 GB cached egress per org per month, unified across Database/Auth/Storage. Storage has its own Smart CDN so cache hits consume the cached bucket. THIS IS THE WALL: 1 GB stored can be served only 5x/month before the org is restricted. | metered: no
- identity: email
- interface: s3-compatible, rest, rclone, cli
- limits note: 50 MB max file size on Free (global limit, cannot raise); 1 GB storage/org; projects paused after 7 days inactivity and must be manually restored; storage metered in GB-Hours so deleting late in the month barely helps; 5 GB egress hard-capped (overage not purchasable on Free).
- interface detail: s3
- tooling: Storage is S3-compatible (supabase storage S3 endpoint, aws CLI / boto3 / rclone `s3` remote with endpoint override), plus supabase-js and the REST storage API
- composes with: The premise '100 projects per free org' is WRONG on two counts: (a) quota is per ORGANIZATION not per project. 'The quota is applied to your entire organization, independent of how many projects you launch'; (b) the free project limit is TWO, and it is account-wide: 'You are granted two free projects. The project limit applies across all organizations where you are an Owner or Administrator.. two Free Plan organizations with one project each, or one Free Plan organization with two projects.' So the ceiling is 2 projects x but only 1 GB + 5 GB egress TOTAL. Paused projects do not count toward the limit, so pause/unpause rotation is the only lever, and it is manual.
- reliability: Free projects pause after 1 week of inactivity. Data persists but the project is offline until manually restored from the dashboard. Egress overage leads to a grace period then restriction until the next billing cycle.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 1 GB file storage — PER ORGANIZATION, not per project; 5 GB egress + 5 GB cached egress per org; 2 free projects per user (across all orgs)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: '1 GB file storage', '5 GB egress', '5 GB cached egress', 'Limit of 2 active projects'
  - [3] 2026-10-21: 'You are granted two free projects. The project limit applies across all organizations where you are an Owner or Administrator... The quota is applied to your entire organization, independent of how many projects you launch within that organization.'
  - [4] 2026-10-21: 'Free | 5 GB / 5 GB | -' (no overage on Free)
  - [5] 2026-10-21: 'For Free projects, the limit can't exceed 50 MB'
  - [2] 2026-11-19: the Free plan includes 1 GB file storage and 5 GB uncached plus 5 GB cached egress | capture: sha256:e75657ca80bf147de32048d373d97c922984757ab9ad192df22a8e812183c64a | quote: - 5 GB egress - 5 GB cached egress - 1 GB file storage
  - [3] 2026-11-19: two free projects, counted account-wide across organizations | capture: sha256:1527ee76b68fce390f0cda82f04ae1de033c33916c59b5bb5057fa7e1446c0ba | quote: You are granted two free projects. The project limit applies across all organizations where you are an Owner or Administrator.
  - [5] 2026-11-19: the maximum file size on Free is 50 MB | capture: sha256:5baf5a029df68b617f2ffeecfbe039c7ee43e89f0199f3298e16351d5bfb3537 | quote: For Free projects, the limit can't exceed 50 MB.
  - [1] 2026-11-19: the Free storage quota is 1 GB, metered as 744 GB-Hrs | capture: sha256:48d3725e72a37311985f52ae7e79c3283e227ed4ad8871c9e80726eb482128e4 | quote: | Free | 1 | - | 744 | - |
  - [4] 2026-11-19: the Free egress quota is 5 GB uncached plus 5 GB cached with no overage | capture: sha256:c389c5ab82692c93deb9d00001cd54a56f8819729c6499eb3bbcdbc1e35168cd | quote: | Free | 5 GB / 5 GB | - |
- sources:
  - [1] https://supabase.com/docs/guides/platform/manage-your-usage/storage-size
  - [2] https://supabase.com/pricing
  - [3] https://supabase.com/docs/guides/platform/billing-on-supabase
  - [4] https://supabase.com/docs/guides/platform/manage-your-usage/egress
  - [5] https://supabase.com/docs/guides/storage/uploads/file-limits
