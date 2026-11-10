# Neo4j AuraDB

> neo4j.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neo4j/ | JSON https://fshy.ajam.dev/api/v1/entity/neo4j.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neo4j AuraDB

- `compute/neo4j-auradb` | qualifies-with-caveat | evidence documented | binding per-object-cap | category managed database
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://neo4j.com/pricing/
- free tier: AuraDB Free, quoted from the quotas page: 'AuraDB Free: A perpetual free tier for learning, prototyping, and small projects' with Nodes '200,000', Relationships '400,000' and Storage '1GB'. Vendor support adds: 'after a period of 72 hours of inactivity, we will automatically pause it ... If the database remains paused for 30 days, it will be deleted by the system.' | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 400,000 relationships caps a graph before the node count does for any connected dataset, because the average degree in a real graph is above 2; the 1 GB storage ceiling is the third constraint and usually arrives at the same time. [1]
- limits note: 400,000 relationships caps a graph before the node count does for any connected dataset, because the average degree in a real graph is above 2; the 1 GB storage ceiling is the third constraint and usually arrives at the same time.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 200,000 nodes and 400,000 relationships is a complete citation graph or a mid-sized knowledge graph, and Aura's Cypher is the same query language as the open-source server, so a graph built here moves to a rented container unchanged.
- reliability: no reliability event recorded
- notes: Free instances run on GCP us-central1 only, cannot be paused by the user, and have on-demand backups only. A read-only query does not reset the 72-hour timer, because inactivity is defined as no updates or write queries, so a monitoring ping that only reads will not keep the graph awake. The graphacademy course page states the same limits.
- extras:
  - facets.class: graph-free-tier
  - facets.free_tier_kind: perpetual-free
  - facets.shape.disk_gib: 1
- evidence:
  - [2] 2026-10-22: 'AuraDB Free: A perpetual free tier for learning, prototyping, and small projects' with Nodes 200,000, Relationships 400,000, Storage 1GB, quoted
  - [1] 2026-10-22: AuraDB Free is 'Starting at $0'; the plan table lists 'Auto-pause/resume' as included, backups 'Not Included' to 'On-demand', and 'Available Zone' as single-zone
  - [3] 2026-10-22: 'after a period of 72 hours of inactivity, we will automatically pause it ... If the database remains paused for 30 days, it will be deleted by the system', quoted
- sources:
  - [1] https://neo4j.com/pricing/
  - [2] https://neo4j.com/docs/aura/quotas-and-limits/
  - [3] https://support.neo4j.com/s/article/4406830696083-Why-is-my-AuraDB-Free-Instance-Paused
