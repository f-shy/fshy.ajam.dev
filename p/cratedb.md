# CrateDB Cloud

> cratedb.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cratedb/ | JSON https://fshy.ajam.dev/api/v1/entity/cratedb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CrateDB Cloud

- `compute/cratedb-cloud` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:18.802Z (live) | stale on 2026-12-05
- url https://cratedb.com/pricing
- free tier: Free plan, quoted: 'Free Plan Available', 'Shared environment', 'Single node', 'Free plan with 2 vCPUs, 2 GB RAM, and 8 GB storage (no credit card required)', 'Backups (once per day)'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card: the pricing page states 'Free plan with 2 vCPUs, 2 GB RAM, and 8 GB storage (no credit card required)'. No hold exists because no payment method is taken on the free plan. The signup fields are not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 8 GB of storage fails first; 2 vCPU and 2 GB RAM are enough for a small ingest and query loop but not for a parallel scan over the full 8 GB. [1]
- limits note: 8 GB of storage fails first; 2 vCPU and 2 GB RAM are enough for a small ingest and query loop but not for a parallel scan over the full 8 GB.
- binding note: the same as limits note
- interface detail: REST API, the croud command-line client, a SQL console in the cloud console, and standard database drivers
- tooling: croud, the CrateDB Cloud command-line client; the Cloud REST API; standard database client libraries and drivers; SQL console in the cloud console
- composes with: CrateDB is distributed SQL with a Postgres wire protocol, so it accepts ordinary Postgres clients; 8 GB with a daily backup is the only free tier among evaluated providers that states a backup schedule at all.
- reliability: no reliability event recorded
- notes: The page lists the free plan inside the Shared card whose headline capacity is 'Up to 8 shared vCPUs and 12 GB RAM' and 'Up to 1 TB storage', which is the paid shared ceiling, not the free one; the parenthetical sentence is the free plan. Whether the free cluster suspends after inactivity is not stated. No probe was run.
- extras:
  - facets.class: sql-free-tier
  - facets.free_tier_kind: perpetual-free
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 8
- evidence:
  - [1] 2026-10-22: 'Free plan with 2 vCPUs, 2 GB RAM, and 8 GB storage (no credit card required)' and 'Backups (once per day)', quoted
  - [2] 2026-11-03: a command-line client, croud, exists | capture: sha256:cf62ef71004e06133c5ebfe870565b239f03765c690a5559f75701ccbf7982fb | quote: Use services from the command-line.
  - [2] 2026-11-03: an API exists | capture: sha256:cf62ef71004e06133c5ebfe870565b239f03765c690a5559f75701ccbf7982fb | quote: Programmatic access to services.
  - [2] 2026-11-04: the Cloud docs index names croud as the API command-line client | capture: sha256:cf62ef71004e06133c5ebfe870565b239f03765c690a5559f75701ccbf7982fb | quote: API CLI (croud)
- sources:
  - [1] https://cratedb.com/pricing
  - [2] https://cratedb.com/docs/cloud/en/latest/
