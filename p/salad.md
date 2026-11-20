# Salad

> salad.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/salad/ | JSON https://fshy.ajam.dev/api/v1/entity/salad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Salad

- `compute/salad` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:33.434Z (live) | stale on 2026-12-04
- url https://salad.com/pricing/
- free tier: No free trial; pay-as-you-go with no minimum commitment. Billing is per second while an instance is running. Prices are per GPU-hour by priority tier (High, Medium, Low, Lowest), with vCPU and RAM included: RTX 4090 24 GB USD 0.440 High, 0.347 Medium, 0.253 Low, 0.160 Lowest. Classes below the table start at USD 0.015 per GPU-hour at Lowest priority. Medium and Low tiers can be preempted, with a minimum run before reallocation of roughly 30 minutes. The page lists no H100, A100, L40S or L4. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): There is no free lane at all, so the binding constraint is the first dollar: a prepaid balance must be funded before any container runs. [1]
- limits note: There is no free lane at all, so the binding constraint is the first dollar: a prepaid balance must be funded before any container runs.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None without a first payment. USD 0.015/h is the cheapest per-hour GPU figure found in this class, so it is the right target once any budget exists.
- reliability: no reliability event recorded
- notes: Salad's USD 0.015/h is the lowest headline GPU rate in the whole class and it is a genuine consumer-GPU network, but the free door is closed. The SSAP grant (USD 5k-10k) is recorded here as a fails-identity door inside a paid-only record: it needs a company, not a person.
- extras:
  - facets.class: consumer-gpu-marketplace
  - facets.shape.gpu_class: consumer cards from USD 0.015/hour
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: quoted: 'Is there a free trial? No.' and GPUs from USD 0.015 per hour billed per second
  - [2] 2026-10-22: independent check dated 2026-09-18 reaches the same conclusion against the official pricing and get-started pages, and notes the withdrawn 5-audio-hour transcription trial
  - [3] 2026-10-22: the only free credit Salad advertises is USD 5k-10k for 'qualifying companies' through its Solutions Architect Program, a sales-gated door not available to an individual
  - [1] 2026-11-03: the RTX 4090 24 GB is priced at USD 0.440, 0.347, 0.253 and 0.160 per GPU-hour on the High, Medium, Low and Lowest tiers | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: | RTX 4090 | 24 GB | $0.440 | $0.347 | $0.253 | $0.160 | $116.80 |
  - [1] 2026-11-03: billing is per second while an instance runs | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: Billing is per second while an instance is in the running state.
  - [1] 2026-11-03: the USD 0.015 per GPU-hour headline applies to classes outside the table at Lowest priority | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: Additional classes (RTX 3060, RTX 3070, RTX 3070 Ti, and others) are available in the portal from $0.015 per GPU-hour at Lowest priority.
  - [1] 2026-11-03: there is no free trial and no minimum commitment | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: No. SaladCloud and the Transcription API are pay-as-you-go with no minimum commitment, so you can start with a small, low-cost test before scaling.
- sources:
  - [1] https://salad.com/pricing/
  - [2] https://buildaicurrent.com/credits/salad-free-credits/
  - [3] https://blog.salad.com/salad-gpu-cloud-ssap/
