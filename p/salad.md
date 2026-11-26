# Salad

> salad.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/salad/ | JSON https://fshy.ajam.dev/api/v1/entity/salad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Salad

- `compute/salad` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T18:47:21.392Z (live) | stale on 2026-12-25
- url https://salad.com/pricing/
- free tier: No free trial; pay-as-you-go with no minimum commitment. Billing is per second while an instance runs. Prices are per GPU-hour by priority tier, with vCPU and RAM included: RTX 4090 24 GB USD 0.440 High, 0.347 Medium, 0.253 Low, 0.160 Lowest. Classes below the table start at USD 0.015 per GPU-hour at Lowest priority; CPU-only groups are USD 0.005 per vCPU-hour and USD 0.001 per GB-RAM-hour. Medium and Low can be preempted after roughly 30 minutes. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: Account creation uses only an email: "Create your Salad account and sign in to the app with an email code or your Google account." "Salad has no passwords. You sign in with a one-time code sent to your email, or with your Google account." Then "Your SaladCloud organization must have a billing method associated with it in order to deploy a container or use any of the inference endpoints." The portal signup form itself could not be read on 2026-11-24.
- interface: rest
- limits:
  - volume-quota (binding): A billing method must be attached before any container can be deployed, and there is no free trial. [1]
- limits note: A billing method is required before a container deploys; CPU-only groups start at USD 0.005 per vCPU-hour and USD 0.001 per GB-RAM-hour and GPU classes at USD 0.015 per GPU-hour at Lowest priority.
- binding note: A billing method is required before the first deployment; once attached, the per-hour rate is USD 0.005 per vCPU-hour for CPU-only groups and USD 0.015 per GPU-hour at Lowest priority.
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
  - [1] 2026-11-24: CPU-only container groups have their own per-hour rates | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: Billed at $0.005 per vCPU-hour and $0.001 per GB of RAM per hour.
  - [4] 2026-11-24: a billing method must be attached before any deployment | capture: sha256:a6786903d8f80d8069ab8a7ba953e0381accec894f5c7efb977d7e225d7dcf85 | quote: Your SaladCloud organization must have a billing method associated with it in order to deploy a container or use any of the inference endpoints.
  - [1] 2026-11-24: the headline USD 0.015 per GPU-hour at Lowest priority | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: Additional classes (RTX 3060, RTX 3070, RTX 3070 Ti, and others) are available in the portal from $0.015 per GPU-hour at Lowest priority.
  - [1] 2026-11-24: no free trial; pay-as-you-go with no minimum commitment | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: No. SaladCloud and the Transcription API are pay-as-you-go with no minimum commitment, so you can start with a small, low-cost test before scaling.
  - [1] 2026-11-24: per-second billing while an instance runs | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: Billing is per second while an instance is in the running state.
  - [1] 2026-11-24: the RTX 4090 four-tier hourly rates | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: RTX 4090 24 GB $0.440 $0.347 $0.253 $0.160 $116.80
  - [1] 2026-11-24: Medium and Low tiers may be preempted after roughly 30 minutes | capture: sha256:ea2b10bcebad63d457e40dc42b3e2ae671d570120cea29a613b75fe7414098a0 | quote: May be preempted by higher-priority groups. Minimum run before reallocation is roughly 30 minutes.
  - [4] 2026-11-24: a billing method is required before any compute can deploy, which is the card gate | capture: sha256:a6786903d8f80d8069ab8a7ba953e0381accec894f5c7efb977d7e225d7dcf85 | quote: Your SaladCloud organization must have a billing method associated with it in order to deploy a container or use any of the inference endpoints.
  - [5] 2026-11-24: the first-party signup guide shows an email code or Google account and no other identity document | capture: sha256:bfb67b85618ee9af5fe5112ce50357fb1a26cd19b051066122573a1e68da3e56 | quote: Create your Salad account and sign in to the app with an email code or your Google account.
  - [4] 2026-11-24: the billing method is required before deployment | capture: sha256:a6786903d8f80d8069ab8a7ba953e0381accec894f5c7efb977d7e225d7dcf85 | quote: Your SaladCloud organization must have a billing method associated with it in order to deploy a container or use any of the inference endpoints.
- sources:
  - [1] https://salad.com/pricing/
  - [2] https://buildaicurrent.com/credits/salad-free-credits/
  - [3] https://blog.salad.com/salad-gpu-cloud-ssap/
  - [4] https://docs.salad.com/general/tutorials/account-setup
  - [5] https://support.salad.com/guides/getting-started/how-to-register-and-log-into-salad/
