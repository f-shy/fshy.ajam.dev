# Baseten

> baseten.co | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/baseten/ | JSON https://fshy.ajam.dev/api/v1/entity/baseten.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Baseten (published tiers, no free plan)

- `compute/baseten` | paid-only | evidence documented | binding none | category GPU cloud | tier published tiers, no free plan
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T18:39:12.192Z (live) | stale on 2026-12-07
- url https://www.baseten.co/pricing/
- free tier: No free tier, no credit and no trial on the pricing page: every GPU row is billed by the minute and by the hour, from the T4 at USD 0.6312 an hour to the B200 at USD 9.98, and the word 'free' does not appear on the page. Per GPU-hour: L4 USD 0.8484, A100 80 GB USD 4.00, H100 MIG 40 GB USD 3.75 and H100 80 GB USD 6.50. L40S: not listed; RTX 4090: not listed. | unit: none | metered on: none | read on: 2026-11-06 | source: [1] | note: The word 'free' does not appear on the page.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not applicable: no free allowance | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a paid account: the pricing page describes only pay-for-use billing and states no free plan
- interface: unknown
- limits:
  - volume-quota: no free tier: every GPU row is billed from the first minute, and the cheapest card listed is the T4 at USD 0.6312 an hour [1]
- binding note: there is no free allowance to exhaust
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Per-card rates on the pricing page: T4 USD 0.6312, L4 USD 0.8484, A10G USD 1.2072, A100 80 GB USD 4.00, H100 MIG 40 GB USD 3.75, H100 80 GB USD 6.50 and B200 180 GB USD 9.98 an hour, priced per minute and repeated for Training Compute. H100 MIG is a partition of an H100 rather than a whole card. L40S and RTX 4090: not listed. The page states no free tier and no credit.
- evidence note: the absence of a free tier is read from the full pricing page. earlier readings carried a free tier at reported confidence with no amount; that is not supported by the page.
- extras:
  - keep_rate: 1.0
  - billing_model: usage
  - session_cap.restart_required: no
  - session_cap.note: not applicable
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - term: monthly
  - price_arithmetic: not published in a comparable hourly unit
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: the resources documentation was read on 2026-10-22 and describes instance selection, vCPU/RAM/GPU sizing and multi-node inference; it publishes no free tier and no rate
  - [1] 2026-10-24: quoted: 'Only pay for the time your model is actively deploying, scaling up or down, or making predictions.'
  - [1] 2026-10-24: the page contains no free-tier row and no occurrence of 'free'
  - [1] 2026-11-06: the T4 row is a billed GPU at USD 0.6312 an hour, the cheapest of the seven GPU rows | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: GPUT4 Memory16 GiB VM Per Minute$0.01052 Approx / hour$0.6312
  - [1] 2026-11-06: the T4 is the cheapest GPU row on the page at USD 0.6312 an hour | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: Approx / hour$0.6312
  - [1] 2026-11-06: the H100 80 GB row is USD 6.50 an hour on the page read | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: Approx / hour$6.50
  - [1] 2026-11-06: the A100 row carries 80 GiB of VRAM and is USD 4.00 an hour | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: GPUA100 Memory80 GiB VRAM Per Minute$0.06667 Approx / hour$4.00
  - [1] 2026-11-06: the GPU rate card is unchanged in shape: every row is billed, and the T4 is the cheapest | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: Approx / hour$0.6312
  - [1] 2026-11-06: the L4 row is USD 0.8484 an hour, USD 0.01414 a minute, on a 24 GiB card | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: GPUL4 Memory24 GiB VRAM Per Minute$0.01414 Approx / hour$0.8484
  - [1] 2026-11-06: the H100 MIG row is USD 3.75 an hour on a 40 GiB partition | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: GPUH100 MIG Memory40 GiB VRAM Per Minute$0.0625 Approx / hour$3.75
  - [1] 2026-11-06: the H100 80 GiB row is USD 6.50 an hour | capture: sha256:7b9d0233a63c43df7ecdd918433f7e3dfce933b9e1a8cc7f0760b6b2641490f7 | quote: Approx / hour$6.50
- sources:
  - [1] https://www.baseten.co/pricing/
  - [2] https://docs.baseten.co/deployment/resources

## baseten (Storage)

- `storage/baseten` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.baseten.co/pricing/
- free tier: none reachable: Inference-only PaaS. The pricing page is a model-API price list ($/token) plus per-second deployment billing; there is no storage product, no artifact store, and no free tier bytes to claim. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Inference-only PaaS. The pricing page is a model-API price list ($/token) plus per-second deployment billing; there is no storage product, no artifact store, and no free tier bytes to claim.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Inference-only PaaS. The pricing page is a model-API price list ($/token) plus per-second deployment billing; there is no storage product, no artifact store, and no free tier bytes to claim.
- sources:
  - [1] https://www.baseten.co/pricing/

## Baseten Delivery Network (BDN) model weight mirrors

- `storage/baseten-delivery-network-model-weight-mirrors` | fails-egress | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://baseten.co
- free tier: No published per-account storage number. BDN 'mirrors model weights to Baseten and caches them near your replicas'; there is no documented quota and no free tier stated. Sized for 'a few GB or less' (weights that can be bundled directly with a Truss) up to multi-GB weight sources. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not applicable. BDN is a read-only cache mounted into your own replicas ('mounted read-only'), not a public download surface. No anonymous URL. | metered: no
- identity: anonymous
- interface: rest
- limits note: per-object-cap: not published; the system expects weights in the GB range, not the 100 GB+ range. Retention: cached by config hash, evicted by the platform ('Caching and deduplication happen behind the scenes'). No free allowance stated.
- interface detail: rest
- tooling: `baseten model push` (Truss), management API POST /v1/prepare_model_upload ('Validates a model push payload and issues upload credentials'), config.yaml `weights:` / `bdn:` keys.
- composes with: Private artifact cache within an inference platform. Anonymous bulk read access is not supported.
- reliability: Requires an organisation account and a paid inference deployment to exist before weights are cached; withdrawing the deployment removes the mount.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published per-account storage number. BDN 'mirrors model weights to Baseten and caches them near your replicas'; there is no documented quota and no free tier stated. Sized for 'a few GB or less' (weights that can be bundled directly with a Truss) up to multi-GB weight sources.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Mirror and cache model weights ... mounted read-only'; 'If your model is small (a few GB or less) you can also bundle weights directly with your Truss'
  - [2] 2026-10-21: POST /v1/prepare_model_upload 'Validates a model push payload and issues upload credentials'
- sources:
  - [1] https://docs.baseten.co/development/model/bdn
  - [2] https://docs.baseten.co/reference/management-api/models/prepare-model-upload
