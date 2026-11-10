# Socrata

> socrata.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/socrata/ | JSON https://fshy.ajam.dev/api/v1/entity/socrata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Socrata / Tyler Data & Insights — 'Community Content' on US city portals

- `storage/socrata-tyler-data-insights-community-content-on-us-city` | fails-quota | evidence reported | binding none | category municipal-portal-community-tier
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.socrata.com/hc/en-us/articles/10552522485015-Community-Created-Content
- free tier: No file storage at all. Community Users may create filtered views and visualisations of EXISTING public datasets; there is no upload of new bytes. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: n/a. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Write-gated and restricted in capacity. Terms state: 'A community user is limited to creating two assets per day per site', and allowed asset types are filtered views and visualizations (charts, graphs, maps). Does not support raw bulk binary storage.
- interface detail: Data & Insights web/SDK (SODA). Views only.
- tooling: n/a for storage.
- composes with: None. A community asset is a query/saved view, not an object.
- reliability: None needed. It cannot store files, so it cannot fail on retention or egress.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No file storage at all. Community Users may create filtered views and visualisations of EXISTING public datasets; there is no upload of new bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Community content can be created by any user who has a Data & Insights account... not a member of the organization'; 'A community user is limited to creating two assets per day per site'; 'Community Users can create filtered views and visualizations (charts, graphs, maps, etc) using any public dataset'
- sources:
  - [1] https://support.socrata.com/hc/en-us/articles/10552522485015-Community-Created-Content
