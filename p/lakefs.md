# Tilde.run

> lakefs.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lakefs/ | JSON https://fshy.ajam.dev/api/v1/entity/lakefs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tilde.run (discontinued)

- `compute/tilde-run` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:13.655Z (live) | stale on 2026-11-22
- url https://lakefs.io/blog/we-recently-shut-down-tilde-run/
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the hosted service is shut down; the retrospective is the only thing at the URL [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: the hosted service was shut down; the operator published the retrospective
- notes: The record's URL is the shutdown notice itself, so the provider is already known to be closed.
- evidence note: the shutdown post was read on 2026-10-22 and states the service closed and why. That is a documented death rather than an absence, and the verdict stands
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - persistent_storage.price: not applicable: the service is closed
  - persistent_storage.durability: filesystem state was the product's whole subject
  - persistent_storage.max_retention: not applicable
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: a lakeFS blog post titled 'we recently shut down Tilde Run', carrying the retrospective 'The most important lesson was that the state (read: the filesystem!) matters far more than people expect' and 'Agents need more than object storage', quoted
- sources:
  - [1] https://lakefs.io/blog/we-recently-shut-down-tilde-run/

## lakefs

- `storage/lakefs` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.lakefs.io/
- free tier: None reachable: Self-hosted data-versioning over an existing object store. It versions data, it does not store any. Zero free bytes; it is a layer above whatever S3 you already pay for. Useful structurally. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Self-hosted data-versioning over an existing object store — it versions data, it does not store any. Zero free bytes; it is a layer above whatever S3 you already pay for. Useful…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Self-hosted data-versioning over an existing object store — it versions data, it does not store any. Zero free bytes; it is a layer above whatever S3 you already pay for. Useful…
- sources:
  - [1] https://docs.lakefs.io/
