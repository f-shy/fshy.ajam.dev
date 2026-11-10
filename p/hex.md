# Hex

> hex.tech | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hex/ | JSON https://fshy.ajam.dev/api/v1/entity/hex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hex (Community)

- `compute/hex-community` | qualifies-with-caveat | evidence documented | binding volume-quota | category notebook runtime | tier Community
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:51:16.012Z (live) | stale on 2026-12-04
- url https://hex.tech/pricing/
- free tier: Community is free and includes Small compute: 4 GB and 0.5 CPU, billed per minute of usage; scheduled runs and alerts are a Team feature at USD 75 per editor per month | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: The compute table marks Extra small, Small and Medium as Free per hour, but the plan tables grant Community 'Small compute' only.
- per-object cap: not applicable: the unit is a session, not an object
- retention: 7-day version history on Community | days: 7 | source: [1]
- egress: no egress allowance or price published | metered: no | source: [1]
- identity: email | detail: a free Community account; the trial needs no payment card, and the pricing page states no card for Community
- interface: rest, cli
- limits:
  - volume-quota (binding): Small compute only: 4 GB RAM, 0.5 CPU; no scheduled runs on Community [1]
  - retention-clamped: 7-day version history on Community, 30-day on Professional [1]
- binding note: half a CPU and 4 GB is the hard ceiling, and there is no scheduler to spend it unattended
- interface detail: a browser notebook with SQL and Python cells
- tooling: the web editor; scheduled runs need Team
- composes with: a collaborative analysis notebook; not a compute provider for a scheduled job
- reliability: no reliability event recorded
- notes: Half a CPU makes Hex the weakest compute among these notebook offers on raw capacity, and no hour cap is published. No free GPU: the A10G GPU profile is billed at USD 4.06 per hour and the L4 GPU profile at USD 2.93 per hour, as advanced compute add-ons of Team and Enterprise.
- evidence note: compute profiles and the scheduled-runs gating are quoted from the pricing page today. No monthly hour cap is published, which is the gap.
- extras:
  - shape.vcpu: 0.5
  - shape.ram_gib: 4
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 on Community
  - free_tier_kind: free-forever
  - unattended: no
  - unattended_mechanism: none on Community; scheduled runs are Team-tier
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: not published
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: '| Small | 4 | 0.5 | Free |' from the compute-profile table, and the footnote '*Billed per minute of usage. Free trials are limited to Medium compute.'
  - [1] 2026-10-24: quoted with an elision marked: 'Features include: Hex agent trial Connect any data source Build with all cell types ... Small compute'
  - [1] 2026-10-24: quoted: 'Scheduled runs and alerts' appears in the Team plan list only
  - [1] 2026-10-24: quoted: 'Anyone can try the Hex Team plan free for 14 days, no payment card required.'
  - [1] 2026-11-03: the Small compute profile is 4 GB and 0.5 CPU at no price per hour, and the Community plan lists Small compute | capture: sha256:b276af460e68e2cfaac55196d997ea50fa43779ec4c551dcd95c6cf79e871978 | quote: | Small | 4 | 0.5 | Free |
  - [1] 2026-11-03: version history is 7-day on Community, 30-day on Professional, unlimited on Team and Enterprise | capture: sha256:b276af460e68e2cfaac55196d997ea50fa43779ec4c551dcd95c6cf79e871978 | quote: Version history 7-day 30-day Unlimited Unlimited
  - [1] 2026-11-03: the A10G GPU compute profile is billed per hour; the L4 GPU row is USD 2.93 and Community lists only Small compute | capture: sha256:b276af460e68e2cfaac55196d997ea50fa43779ec4c551dcd95c6cf79e871978 | quote: | A10G GPU | 27 | 6 | $4.06 |
- sources:
  - [1] https://hex.tech/pricing/

## Hex (Storage)

- `storage/hex` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hex.tech
- free tier: Community (free): small compute only. 2 GB / 4 GB / 8 GB RAM profiles at $0/hr. No storage allocation published; there is no user-writable persistent disk, only data connections. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published meter; the model is 'bring your own warehouse', so bytes never live with Hex. | metered: no
- identity: card
- interface: graphql
- limits note: Free = 'Small compute' (8 GB max); 5 published apps on Professional; the free tier is a trial of the paid product in practice.
- interface detail: graphql
- tooling: Hex API + MCP server; data comes from connected warehouses (Snowflake, BigQuery, Postgres), not from Hex storage.
- composes with: None. Hex is a query layer. Whatever storage you use, you must already own.
- reliability: Not a storage provider in any sense. Recorded to close the branch.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Community (free): small compute only — 2 GB / 4 GB / 8 GB RAM profiles at $0/hr. No storage allocation published; there is no user-writable persistent disk, only data connections.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Community free 'Features include: ... Small compute'; compute table caps free profiles at 8 GB
  - [2] 2026-10-21: compute profiles are memory/CPU only, no disk
- sources:
  - [1] https://hex.tech/pricing/
  - [2] https://learn.hex.tech/docs/explore-data/projects/environment-configuration/environment-views
