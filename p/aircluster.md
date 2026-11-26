# Air Cluster

> aircluster.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aircluster/ | JSON https://fshy.ajam.dev/api/v1/entity/aircluster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Air Cluster — commercial product that advertises combining several accounts (incl. accounts from the same provider)

- `storage/air-cluster-commercial-product-that-advertises-multi-acc` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category provider-advertising-stacking
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.aircluster.org/en/clouds/
- free tier: 'Air Cluster allows you to add several accounts from the same server (e.g., three different OneDrive accounts) and combine their capacity into one single cluster.' | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Client-side; files are read from each provider directly. Optional client-side encryption. | metered: no
- identity: email
- interface: rclone
- limits note: Windows graphical interface only without public programmatic API access. Documentation does not specify whether large files are striped across accounts or distributed at the whole-file level.
- interface detail: wrapper-only
- tooling: Windows desktop app (AirCluster-Installer.exe). No API, no Linux, no rclone backend.
- composes with: N accounts, including N accounts of the same provider, presented as one large-capacity 'cluster'. This is the clearest commercial statement of the hypothesis: 'Unlike standard file managers, Air Cluster allows you to create a "Cluster", which combines the storage space of all your cloud accounts. This lets you manage the total space as if it were a single, large-capacity hard drive.'
- reliability: Closed-source commercial; cannot audit placement or repair behaviour.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Air Cluster allows you to add several accounts from the same server (e.g., three different OneDrive accounts) and combine their capacity into one single cluster.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Can I use multiple accounts from the same provider? Yes... combine their capacity into one single cluster'; 'manage the total space as if it were a single, large-capacity hard drive' — the vendor's own copy, quoted verbatim; it describes several accounts combined into one pool
- sources:
  - [1] https://www.aircluster.org/en/clouds/
