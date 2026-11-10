# Snowflake

> snowflake.com | Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/snowflake/ | JSON https://fshy.ajam.dev/api/v1/entity/snowflake.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Snowflake

- `compute/snowflake` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:43:11.429Z (live) | stale on 2026-12-05
- url https://signup.snowflake.com/
- free tier: Start your 30-day Snowflake trial with USD 400 in free credits. The documentation states: 'To sign up for a trial account, all you need is a valid email address; no payment information or other qualifying information is required.' AI features are disabled on a self-service trial account until a credit card is added. | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Per-byte egress fee for transfers into a different region or cloud platform, with transfers inside the same region free and no ingress fee; the per-byte rate depends on the hosting region and is on the separate pricing guide, not read. | metered: no | source: [1]
- identity: email | detail: a valid email address only, with no payment information required at signup; AI features, external network access, hybrid tables and Openflow stay capped until a credit card is added
- interface: cli
- limits:
  - volume-quota (binding): USD 400 of usage over 30 days [2]
- limits note: at USD 2 a credit on AWS US East Standard and 1 credit an hour for an X-Small Gen1 warehouse, the USD 400 buys 200 warehouse-hours, which is 8.3 days of continuous running
- binding note: the 30-day clock ends the USD 400 before any usage ceiling is reached
- interface detail: Snowflake CLI, an open-source command line client for SQL execution and for Snowpark, Streamlit and Native App objects, over a configured connection; SnowSQL is the legacy command line client; documented at docs.snowflake.com
- tooling: Snowflake CLI (open source, the preferred client) and SnowSQL (legacy client)
- composes with: USD 400 of Snowflake credit is a genuine warehouse for a month and is the standard route to loading a large public dataset once; nothing about it composes, because both the credit and the access end on the same day.
- reliability: no reliability event recorded
- notes: The balance is a warehouse budget, not a host. A 30-day trial cannot run even an X-Small warehouse continuously: 720 hours at 1 credit an hour is 720 credits, and USD 400 buys 200. Auto-suspend is the only sane setting.
- extras:
  - facets.class: analytics-trial-credit
  - facets.free_tier_kind: trial-credit
  - credit_price_usd.aws_us_east_standard: 2.0
  - credit_price_usd.aws_us_east_enterprise: 3.0
  - xs_credits_per_hour_gen1: 1
- evidence:
  - [1] 2026-10-23: quoted: 'Start your 30-day trial with $400 in free credits'
  - [3] 2026-10-23: quoted X-Small row: '1 | 0.0003' credits per second, and 'The numbers in the preceding table refer to the first generation (Gen1)'
  - [4] 2026-10-23: the price table is client-side; the linked consumption table gives AWS US East Standard $2.00, Enterprise $3.00 per credit, effective 2026-10-15
  - [5] 2026-11-03: egress is charged per byte across regions | capture: sha256:a7dce1db3e40b779e545d404989e4b738c6bb37681705bb076d7f41992f455bc | quote: Snowflake charges a per-byte fee for data egress when users transfer data from a Snowflake account into a different region on the same
  - [6] 2026-11-03: a CLI exists | capture: sha256:0f7de69086407ace6e1cfbd078732b40f8f12a12baa03d2f9be0b6719c339728 | quote: is the preferred command-line client for new installs and new work.
  - [6] 2026-11-04: Snowflake CLI is the preferred command line client | capture: sha256:0f7de69086407ace6e1cfbd078732b40f8f12a12baa03d2f9be0b6719c339728 | quote: is the preferred command-line client for new installs and new work.
  - [6] 2026-11-04: the page names Snowflake CLI and SnowSQL | capture: sha256:0f7de69086407ace6e1cfbd078732b40f8f12a12baa03d2f9be0b6719c339728 | quote: SnowSQL is a legacy command-line client.
- sources:
  - [1] https://signup.snowflake.com/
  - [2] https://docs.snowflake.com/en/user-guide/admin-trial-account
  - [3] https://docs.snowflake.com/en/user-guide/warehouses-overview
  - [4] https://www.snowflake.com/en/pricing-options/
  - [5] https://docs.snowflake.com/en/user-guide/cost-understanding-data-transfer
  - [6] https://docs.snowflake.com/en/developer-guide/snowflake-cli/index

## Snowflake 30-day trial ($400 credits)

- `storage/snowflake-30-day-trial` | trial-only | evidence reported | binding retention-clamped | category iaas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.snowflake.com/en/snowflake-trial/
- free tier: $400 in free credits on a 30-day trial ('Start your 30-day Snowflake trial today. Get $400 in credits'). No byte quota. Storage is billed from the credit balance. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: retention: 'Snowflake trial account credits may be used within 30 days'; 'If you don't upgrade before the trial period ends, the account is suspended and any unused free usage balance expires' and 'you may lose access to your data'. | days: 30 | source: [1] | note: not stated
- egress: Data leaves via query results, not object GETs; no egress-free download path. | metered: no
- identity: card
- interface: rest, rclone
- limits:
  - retention-clamped (binding): retention: 'Snowflake trial account credits may be used within 30 days [1]
- limits note: per-object-cap: internal stage file size limits apply. request-rate: warehouse credits burn while running. retention: 'Snowflake trial account credits may be used within 30 days'; 'If you don't upgrade before the trial period ends, the account is suspended and any unused free usage balance expires' and 'you may lose access to your data'.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Snowflake SQL API / Snowpark; internal stages + `GET`/`PUT` for file transfer. No rclone backend; files sit inside stages or named internal stages, not a general object store.
- composes with: New email = new trial, explicitly ('you can sign up .. all you need is a valid email address; no payment information'). So $400 x N throwaway trials. But each dies at 30 days.
- reliability: Hard 30-day cliff with documented data loss on non-conversion. Not storage. A compute trial that happens to include stage space.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $400 in free credits on a 30-day trial ('Start your 30-day Snowflake trial today. Get $400 in credits'). No byte quota — storage is billed from the credit balance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '$400 in free credits ... built for a 30-day experience'; 'credits may be used within 30 days'
  - [2] 2026-10-21: 'the account is suspended and any unused free usage balance expires'
  - withheld 2026-10-21: probe: GET docs.snowflake.com/en/user-guide/admin-trial-account -> 200; GET www.snowflake.com/en/snowflake-trial/ -> 200
- sources:
  - [1] https://www.snowflake.com/en/snowflake-trial/
  - [2] https://docs.snowflake.com/en/user-guide/admin-trial-account

## Snowflake trial account (internal stage)

- `storage/snowflake-trial-account` | trial-only | evidence reported | binding none | category data-warehouse
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.snowflake.com/en/snowflake-trial/
- price $40/TB/month storage after the trial (Standard). | parsed USD 40/TB-mo
- disagrees on verdict: `storage/snowflake-trial` says fails-quota, `storage/snowflake-trial-account` says trial-only
- free tier: No byte quota. A $400 credit balance and a 30-day clock, whichever ends first. 'The trial continues for 30 days (from the sign-up date) or until you've depleted your free usage balance.' Storage accrues cost against that balance at standard rates (~$40/TB/month per the documented Standard rate). So the nominal free storage is whatever the credit buys after compute: at $40/TB/mo, $400 buys 10 TB-months, i.e. 10 TB for one month or 1 TB for ten. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not free. Snowflake bills egress/transfer separately and the trial credit is consumed by it. | metered: no
- identity: email | detail: email
- interface: s3, rest
- limits note: retention-clamped and hard-capped by design. Data is NOT deleted on suspension but is also not retrievable, which is worse than deletion for the purpose of treating it as storage. Identity is email only, which is the one thing in its favour.
- interface detail: rest + s3
- tooling: Excellent: PUT to an internal stage, full SQL, Snowflake SDKs, and external stages pointing at your own S3/Azure/GCS. Programmatically the best of the warehouse entrants.
- composes with: One trial per email; trials cannot be chained legitimately because the account is suspended at day 30. 'At the end of the trial, the account is suspended. You can still log into a suspended account, but you cannot use any features, such as … loading data.'.
- reliability: Suspension at day 30 makes this a 30-day buffer, not storage. Any chunked-object scheme built on it would need a full re-upload cycle monthly.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: No byte quota — a $400 credit balance and a 30-day clock, whichever ends first. 'The trial continues for 30 days (from the sign-up date) or until you've depleted your free usage balance.' Storage accrues cost against that balance at standard rates (~$40/TB/month per the documented Standard rate). So the nominal free storage is whatever the credit buys after compute: at $40/TB/mo, $400 buys 10 TB-months, i.e. 10 TB for one month or 1 TB for ten.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $40/TB/month storage after the trial (Standard).
- evidence:
  - [1] 2026-10-21: opened: 'The trial continues for 30 days (from the sign-up date) or until you've depleted your free usage balance, whichever occurs first'; 'At the end of the trial, the account is suspended … you cannot use any features, such as running a virtual warehouse, loading data, or performing queries'; 'To reactivate a suspended trial account, add a credit card.'
  - [2] 2026-10-21: surfaced: '200 free credits, a $400 value' — the credit figure, confirming the balance framing.
  - [3] 2026-10-21: surfaced: '$40/TB/month in storage' on standard plan, which is the rate the credit is spent against.
- sources:
  - [1] https://docs.snowflake.com/en/user-guide/admin-trial-account
  - [2] https://www.snowflake.com/wp-content/uploads/2020/06/Test-Driving-Snowflake.pdf
  - [3] https://news.ycombinator.com/item?id=25978000

## snowflake trial ($400 / 30 days)

- `storage/snowflake-trial` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.snowflake.com/en/user-guide/admin-trial-account
- disagrees on verdict: `storage/snowflake-trial` says fails-quota, `storage/snowflake-trial-account` says trial-only
- free tier: none reachable: Thirty days then suspension. Storage is billed from the credit balance, so $400 buys a few TB-months at most and then the account is suspended rather than downgraded. Trial, not free tier. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Thirty days then suspension. Storage is billed from the credit balance, so $400 buys a few TB-months at most and then the account is suspended rather than downgraded. Trial, not free tier.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Thirty days then suspension. Storage is billed from the credit balance, so $400 buys a few TB-months at most and then the account is suspended rather than downgraded. Trial, not free tier.
- sources:
  - [1] https://docs.snowflake.com/en/user-guide/admin-trial-account
