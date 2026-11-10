# Radicle Garden

> radicle.garden | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/radicle/ | JSON https://fshy.ajam.dev/api/v1/entity/radicle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Radicle Garden (hosted seed) + permissionless public seeds

- `storage/radicle-garden-permissionless-public-seeds` | fails-quota | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://radicle.garden
- free tier: 5 GB of storage to start with on a Garden subscription ('talk to us if you need more'); public permissionless seed nodes self-configure their own limit, e.g. 10 GB observed on a community node | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Served over HTTP from designated node subdomains (`node-name.radicle.garden`) without published egress metering. Peer-to-peer replication allows multiple network nodes to mirror repositories without centralized bandwidth charges. | metered: no
- identity: email
- interface: git, cli
- limits note: 5 GB on Garden (paid add-on beyond), per-account. Public permissive seeds are free but each sets its own cap. Fetching needs at least one node online holding the data.
- interface detail: git
- tooling: `rad` CLI (Radicle heartwood), git remote `rad://`. Real client, actively developed.
- composes with: Replication is the chaining primitive: each additional seed that follows your repo (rad id allow-list) is another free full copy and another serving endpoint. Content is addressed by git OID so it is verifiable. But it is a replication multiplier, not a capacity multiplier. Total bytes are still bounded by the largest seed.
- reliability: Availability is the weak point, not durability: if no seed holds the repo, it is unreachable until a peer comes back. Garden states it is 'walkaway-safe'. Losing the host does not lose your local repo.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB of storage to start with on a Garden subscription ('talk to us if you need more'); public permissionless seed nodes self-configure their own limit, e.g. 10 GB observed on a community node
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '5 GB of storage to start with (talk to us if you need more)'; 'Web hosting of those repositories under your own node-name.radicle.garden subdomain'
  - [2] 2026-10-21: commit 'Change storage limit to 10gb' in a seed's src/lib/server/config.json (per-seed caps are operator-chosen, not protocol-fixed)
  - [3] 2026-10-21: 'Add disclaimer for permissive seeds' (free public seeds exist and are documented as such)
- sources:
  - [1] https://radicle.garden/blog/introducing-radicle-garden
  - [2] https://radicle.network/nodes/rosa.radicle.network/rad%3Az2v4XbSTEqnYrxToCAA3vf9yCD5Er/commits/12ba071829d126aeffea30c616d54751c2ff63bc
  - [3] https://radicle.network/nodes/seed.radicle.dev/rad%3Az371PVmDHdjJucejRoRYJcDEvD5pp/commits/a82b388aec68a3c7289c99a9e27c0aae679ff5be

## radicle garden subscription

- `storage/radicle-garden-subscription` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://radicle.garden/blog/introducing-radicle-garden
- free tier: none reachable: Storage allowance is 5 GB on a paid subscription with no free tier. Higher capacity requires custom pricing. Uncapped usage is available via permissionless seed nodes. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: 5 GB and it is a paid subscription, not a free tier; beyond that is 'talk to us'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB and it is a paid subscription, not a free tier; beyond that is 'talk to us'.
- sources:
  - [1] https://radicle.garden/blog/introducing-radicle-garden
