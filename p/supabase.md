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
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://supabase.com/pricing
- free tier: 500 MB database on Shared CPU with 500 MB RAM; 2 active projects; 5 GB egress and 5 GB cached egress; unlimited API requests | unit: mixed | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 500 MB per project database | source: [1]
- retention: a Free project is paused after 1 week of low activity, and is restorable for up to 1 year after the pause. A paid project is never paused | days: 7 | source: [2] | note: the pause trigger is activity, not age: a few user requests a day over the previous week keep it awake
- egress: 5 GB egress and 5 GB cached egress per month included. The Free plan publishes no overage price, so the fifth gigabyte is a wall and not a bill | metered: no | free allowance: 5 GB egress, 5 GB cached egress | source: [1]
- identity: email | detail: email signup; no card on Free
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
- notes: The pause is the finding, and it is a 7-day activity clock rather than a 30-day deletion. A weekly cron that touches the database keeps it alive; a monthly one loses a week of availability every cycle. The restore window is 1 year, so the data is not at risk the way a deletion would put it at risk.
- evidence note: the pricing page and the pausing guide were read; nothing was provisioned. The 90-day restore window stated in the 2024-06-24 changelog has since been widened to 1 year.
- evidence:
  - [1] 2026-10-22: 500 MB database, 2 active projects, 5 GB egress, 5 GB cached egress, 'Free projects are paused after 1 week of inactivity', and the plan table row Pausing: After 1 week of inactivity
  - [2] 2026-10-22: 'Supabase pauses Free Plan projects that show low activity over a 7-day period'; restore is available 'for up to 1 year after it was paused'; a few user requests a day over a week prevent…
  - [3] 2026-10-22: two free projects across all organizations where you are Owner or Administrator; paused projects do not count toward the free project limit
  - [5] 2026-10-22: the 2024-06-24 change set the restore window at 90 days, which the current doc has since widened to 1 year
  - [6] 2026-10-22: the shared Supavisor pooler is multi-tenant and IPv4-only; the dedicated PgBouncer pooler needs a paid plan
  - [4] 2026-10-22: Nano compute is the free plan at USD 0 with up to 0.5 GB of RAM and a recommended 500 MB database; 'Database max connections are recommended values and can be customized via max_connections', so the compute size sets the count
- sources:
  - [1] https://supabase.com/pricing
  - [2] https://supabase.com/docs/guides/platform/free-project-pausing
  - [3] https://supabase.com/docs/guides/platform/billing-on-supabase
  - [4] https://supabase.com/docs/guides/platform/compute-and-disk
  - [5] https://supabase.com/changelog/27497-paused-free-plan-projects-are-restorable-for-90-days
  - [6] https://supabase.com/docs/guides/database/connecting-to-postgres/pooling-and-limits

## Supabase (Storage)

- `storage/supabase` | fails-egress | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://supabase.com/docs/guides/platform/manage-your-usage/storage-size
  - [2] https://supabase.com/pricing
  - [3] https://supabase.com/docs/guides/platform/billing-on-supabase
  - [4] https://supabase.com/docs/guides/platform/manage-your-usage/egress
  - [5] https://supabase.com/docs/guides/storage/uploads/file-limits
