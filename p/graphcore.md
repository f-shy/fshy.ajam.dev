# Graphcore IPU Cloud

> graphcore.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/graphcore/ | JSON https://fshy.ajam.dev/api/v1/entity/graphcore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Graphcore IPU Cloud

- `compute/graphcore-ipu-cloud` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.graphcore.ai/projects/graphcloud-getting-started/en/latest/system.html
- free tier: The free tier is gone and what remains is a sales contract. Graphcore's Paperspace guide now opens with 'Running code on IPUs in Paperspace is no longer supported', and the page that advertised IPU cloud access 'with free trials and a range of pricing options' returns 404 today. The surviving lane is Graphcloud, whose systems are 'available on Graphcloud that you can purchase access to' with 'Full pricing details for accessing these systems... available from Cirrascale or from Graphcore sales'. The smallest listed system is a Bow Pod16: four Bow-2000s and a host server. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): no published price and no self-serve checkout: the entry step is a quote from Graphcore sales or Cirrascale for a four-card minimum. [1]
- limits note: no published price and no self-serve checkout: the entry step is a quote from Graphcore sales or Cirrascale for a four-card minimum.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It chains with nothing: a four-card minimum and a quote step rule out an individual buyer, and the free IPU-POD4 notebook route that did fit has now been withdrawn on two independent platforms.
- reliability: no reliability event recorded
- notes: Reopening criteria: published trial SKU on the Cirrascale marketplace.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: Graphcore Bow-2000 IPU
  - facets.shape.gpu_count: 4
- evidence:
  - [2] 2026-10-22: 'Running code on IPUs in Paperspace is no longer supported', quoted at the top of the guide
  - [3] 2026-10-22: the page that carried the free-trial claim returns 404 today
  - [1] 2026-10-22: 'Full pricing details for accessing these systems are available from Cirrascale or from Graphcore sales', quoted, with Bow Pod16 as the smallest example
  - [4] 2026-10-22: release note dated 26 February 2024: 'Graphcore IPU machines are now discontinued in Notebooks'
- sources:
  - [1] https://docs.graphcore.ai/projects/graphcloud-getting-started/en/latest/system.html
  - [2] https://docs.graphcore.ai/projects/paperspace-getting-started/en/latest/overview.html
  - [3] https://www.graphcore.ai/ipus-in-the-cloud
  - [4] https://docs.digitalocean.com/release-notes/machines/
