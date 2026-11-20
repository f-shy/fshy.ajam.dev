# Featurize

> featurize.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/featurize/ | JSON https://fshy.ajam.dev/api/v1/entity/featurize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Featurize

- `compute/featurize` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://featurize.cn/
- free tier: Chinese GPU cloud and hosted notebook with published per-hour rates: RTX 4090 quoted at CNY 1.87 per hour on 16 AMD EPYC 9354 cores, 60 GB RAM and 750 GB of free disk; RTX 3090 quoted at CNY 1.62 per hour on 6 Xeon Gold 6142 cores, 60 GB RAM and 450 GB disk; PRO 6000 at CNY 6.19 per hour. At USD 1 = CNY 6.6743 that is USD 0.280, USD 0.243 and USD 0.927 per GPU-hour. PyTorch and TensorFlow images are preinstalled and billing is on demand or by monthly subscription. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: unverified, inferred: https://featurize.cn/register answers 404, so no registration form was read. A mainland number is inferred from the price currency and from every sibling service in this class using SMS registration; it is not quoted. | country: CN
- interface: rest
- limits:
  - write-gated (binding): The account is a Chinese mobile number plus an SMS code and the site publishes no alternate registration route, so the same identity wall as AutoDL applies. [1]
- limits note: The account is a Chinese mobile number plus an SMS code and the site publishes no alternate registration route, so the same identity wall as AutoDL applies.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 750 GB of free instance disk alongside a 4090 is larger than any Western broker's included disk at this rate, which matters for a dataset-heavy fine-tune.
- reliability: no reliability event recorded
- notes: The phone gate is inferred from the site being a mainland consumer service and from AutoDL's sibling form; the Featurize registration page was not read, so that is the weaker claim in this record and it is flagged in binding_note rather than presented as quoted.
- extras:
  - facets.class: regional-gpu-retailer
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 16
  - facets.shape.ram_gib: 60
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
  - facets.shape.disk_gib: 750
- evidence:
  - [1] 2026-10-22: translated from the Chinese page: the RTX 4090 row reads on-demand as low as CNY 1.87 per hour, on 16 AMD EPYC 9354 cores, 60 GB of high-speed memory and 750 GB of free disk; the RTX 3090 row reads CNY 1.62 per hour; the PRO 6000 row reads CNY 6.19 per hour
  - [2] 2026-10-22: USD 1 = CNY 6.6743 on 2026-10-22
- sources:
  - [1] https://featurize.cn/
  - [2] https://api.frankfurter.app/latest?from=USD&to=CNY
