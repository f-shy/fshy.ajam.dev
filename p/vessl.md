# VESSL Cloud

> vessl.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vessl/ | JSON https://fshy.ajam.dev/api/v1/entity/vessl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VESSL Cloud

- `compute/vessl-cloud` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.cloud.vessl.ai/ko/pricing/gpu-instances
- free tier: Korean GPU cloud with an on-demand rate table in Korean, last updated 2026-09-26: H100 SXM 80GB at USD 2.98 per hour, A100 SXM 80GB at USD 1.48 per hour, L40S 48GB at USD 1.80 per hour. H200 SXM 141GB, B200 192GB, B300 288GB and GB300 288GB are reserved-only and priced by sales quote. The page states the prices are for reference and the billed amount may differ slightly. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: No free tier appears in the pricing documentation; the signup route was not read, so the identity kind is unconfirmed.
- interface: unknown
- limits note: Nothing published binds above the scale; a reserved tier exists but priced by quote, so the on-demand rows are the only comparable lane.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- reliability: no reliability event recorded
- notes: Recorded from the Korean documentation because the English pricing page was not the source of these numbers; the vendor also states the figures are indicative, which is a caveat on the price rather than on the capacity. Whether a Korean entity or phone is required to open an account was not established, and that is what would move this from paid-only to fails-identity.
- extras:
  - facets.class: regional-gpu-retailer
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: A100 SXM
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 80
- evidence:
  - [1] 2026-10-22: quoted table: H100 SXM 80 GB US 2.98 per hour, A100 SXM 80 GB US 1.48 per hour, L40S 48 GB US 1.80 per hour; H200, B200, B300 and GB300 shown as unavailable on demand and quoted through sales
  - [1] 2026-10-22: quoted notes: prices are for reference and the actual billed amount may differ slightly; last updated 2026-09-26
- sources:
  - [1] https://docs.cloud.vessl.ai/ko/pricing/gpu-instances
