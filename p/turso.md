# Turso

> turso.tech | Databases and KV, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turso/ | JSON https://fshy.ajam.dev/api/v1/entity/turso.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Turso (Databases and KV)

- `databases-kv/turso` | qualifies | evidence documented | binding retention-clamped | category SQLite at the edge
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://turso.tech/pricing
- price USD 0.75/GB beyond 9 GB on Developer
- free tier: 100 databases; 5 GB storage; 500 million rows read per month; 10 million rows written per month; 3 GB sync | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 5 GB across all databases on Free; the plan table gives no per-database cap
- retention: a database is archived after 10 days of inactivity on a free plan, and an archived database must be unarchived before it can be used; a deleted database has no point-in-time restore on Free and the Free column shows 1-day audit logs | days: 10 | source: [2] | note: the archive clock is documented on the CLI and API reference pages, not on the pricing page
- egress: no egress charge and no transfer allowance is published; the metered quantities are rows read and rows written, so a byte of egress is not what is counted | metered: no | source: [1]
- identity: email | detail: email signup; GitHub OAuth also offered
- interface: rest, cli
- limits:
  - request-rate: 500 million rows read and 10 million rows written per month [1]
  - per-object-cap: 5 GB total across all databases; 100 databases [1]
  - retention-clamped (binding): an inactive database is archived after 10 days on a free plan [2]
  - request-rate: no connection limit is published on the pricing page or the feature pages; recorded as a gap [1]
- binding note: 10 days of inactivity archives the database on the free plan, so a job that runs less often than that finds the database unavailable. The 5 GB total and the 10-million-row monthly write budget are larger than that clock allows a quarterly job to reach.
- interface detail: libSQL over HTTP and WebSockets; the Turso CLI; a platform API
- tooling: the turso CLI; libSQL client libraries; sqld for a local replica
- composes with: a free SQLite replica per tenant suits multi-tenant read-heavy work that a single free Postgres cannot hold, provided something touches each database at least every 10 days, because the free plan archives an inactive one
- reliability: an inactive database on a free plan is archived after 10 days and must be unarchived before use; the archive is not a deletion and the data survives it
- notes: The 500-database and 9-GB figures in circulation are the Developer plan, not Free. The 5 GB is a total, so 100 databases average 50 MB each. The binding constraint is not either number: it is the 10-day archive, which a quarterly job meets first and which nothing on the pricing page states.
- evidence note: the pricing table was read on 2026-10-22 and its own meta description states 100 databases and 5 GB. The 10-day archive clock is from Turso's CLI reference, read the same day; the pricing page does not carry it, so a reader who checks only the pricing page will not find the constraint that binds first.
- evidence:
  - [1] 2026-10-22: Free column: 100 databases, 5GB storage, 500 Million rows read, 10 Million rows written, 3GB sync, 1 day audit logs; Developer USD 4.99 gives unlimited databases and 9GB
  - [2] 2026-10-22: 'Databases get archived after 10 days of inactivity for users on a free plan'; the unarchive command restores one
  - [3] 2026-10-22: the platform API exposes a group unarchive endpoint, so the archive state is reachable programmatically and not only through the CLI
  - probe:https://api.turso.tech/v1/organizations 2026-10-22: an unauthenticated GET returns 401 with 'token contains an invalid number of segments', proving the platform API exists and is token-authenticated
- sources:
  - [1] https://turso.tech/pricing
  - [2] https://docs.turso.tech/cli/group/unarchive
  - [3] https://docs.turso.tech/api-reference/groups/unarchive

## Turso (Storage)

- `storage/turso` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://turso.tech
- free tier: 5 GB total storage, 100 databases on Free | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not separately metered on Free; the binding meters are 500M rows read / 10M rows written per month, plus 3 GB embedded syncs. Serving files out of SQLite blobs burns rows-read, not bytes. | metered: yes
- identity: email
- interface: rest, cli
- limits note: 5 GB is a hard total across all 100 DBs. This is the key trap: the big number is database COUNT, not storage. Exceeding rows-read returns `BLOCKED`. 3 GB sync cap for embedded replicas.
- interface detail: rest
- tooling: Turso CLI + HTTP API (`/v2/pipeline`), libSQL clients (JS/Python/Rust/Go), `turso db shell`, embedded replicas
- composes with: 100 databases is a unit multiplier for ORGANIZATION, but the 5 GB storage is an ACCOUNT-level pot, not per database. 100 DBs x 50 MB each rather than 100 x 5 GB. Second axis: each org/account. Multiply accounts (GitHub OAuth is one click). N accounts x 5 GB.
- reliability: Exceeding quota returns BLOCKED errors on queries rather than data loss; DBs stay warm (no cold starts since Mar 2025).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB total storage, 100 databases on Free
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free $0/month | 100 | 5GB | 500 Million | 10 Million | 3GB'
  - [2] 2026-10-21: '500 million rows read per month, 10 million rows written per month, and 5GB of storage'; Developer plan allows 1,000 databases
- sources:
  - [1] https://turso.tech/pricing
  - [2] https://turso.tech/blog/turso-cloud-debuts-the-new-developer-plan
