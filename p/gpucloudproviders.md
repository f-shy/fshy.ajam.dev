# Akash Network GPU

> gpucloudproviders.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpucloudproviders/ | JSON https://fshy.ajam.dev/api/v1/entity/gpucloudproviders.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Akash Network GPU

- `compute/akash-network-gpu` | trial-only | evidence reported | binding retention-clamped | category GPU cloud
- needs card unknown, phone no, ID no, institution no | verified 2026-11-06T19:39:36.653Z (live) | stale on 2026-11-21
- url https://gpucloudproviders.com/gpu/h100
- free tier: A second live tracker reports H100 capacity on the Akash marketplace confirmed in stock at USD 2.730 per GPU-hour, timestamped 2026-10-21 19:31 UTC, from 60 offers across 14 providers, with the lowest listed price of USD 2.500 on Hyperstack marked as not reporting live stock. The existing corpus record for Akash holds a USD 1 trial credit whose own terms exclude the RTX 4090, RTX 5090, A100 and H100, so H100 supply exists on the network for a paying account while the trial cannot reach it. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: The existing record's facts still hold and are what bind: deployments run up to 24 hours each, and the trial credit is USD 1 for 30 days, so the H100 supply is unreachable inside the free lane. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: Unchanged from the existing record: the trial is a credit on a normal account, and the card question for a paid deployment was not tested.
- interface: unknown
- limits:
  - retention-clamped (binding): The existing record's facts still hold and are what bind: deployments run up to 24 hours each, and the trial credit is USD 1 for 30 days, so the H100 supply is unreachable inside the free lane. [1]
- limits note: The existing record's facts still hold and are what bind: deployments run up to 24 hours each, and the trial credit is USD 1 for 30 days, so the H100 supply is unreachable inside the free lane.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Akash is the only one of these providers where a marketplace price is set by independent providers rather than by the platform, so the USD 2.73 is a bid floor that moves; it composes with earlier existing note that the network's cheaper cards start at USD 0.150 for an RTX 3090.
- reliability: no reliability event recorded
- notes: The trial excludes H100 and above, and H100 capacity is nonetheless on the network at a published floor. The distinction that matters is trial versus paid, and collapsing the two would mislead the next reader in either direction. The verdict is trial-only: the trial credit cannot reach H100.
- extras:
  - facets.class: gpu-marketplace
  - facets.free_tier_kind: trial-credit
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 80
- evidence:
  - [1] 2026-10-22: quoted: 'As of 21 Oct 2026, 19:31 UTC, the cheapest H100 confirmed in stock is $2.730 per GPU-hour on Akash Network', compared across 60 offers from 14 providers
  - [1] 2026-10-22: quoted: 'The lowest listed price is $2.500 on Hyperstack, which does not report live stock', which separates a listed rate from a bookable one
  - [2] 2026-10-22: 
  - [3] 2026-11-06: Akash's own H100 page prices on-demand H100 capacity at USD 2.73 per GPU-hour | capture: sha256:6b274db249122fe24b799c8e0a23258e303fd9c48af86499142333ae1e8d025e | quote: As of October 22, 2026, on-demand H100s on Akash start at $2.73 per GPU-hour.
- sources:
  - [1] https://gpucloudproviders.com/gpu/h100
  - [2] https://gpurentalprices.com/
  - [3] https://akash.network/pricing/gpus/h100/
