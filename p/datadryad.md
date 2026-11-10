# dryad

> datadryad.org | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datadryad/ | JSON https://fshy.ajam.dev/api/v1/entity/datadryad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dryad

- `storage/dryad` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datadryad.org
- disagrees on identity_kind: `storage/dryad` says institution, `storage/dryad-2` says email
- disagrees on identity_kind: `storage/dryad` says institution, `storage/dryad-the-2025-26-pricing-model` says email
- free tier: Pay-to-publish (Data Publishing Charge). Up to 5 GB = $150; 1 TB = $6,077; 2 TB = $12,162. Not a free tier in any sense. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads once published; no egress metering. | metered: no
- identity: institution
- interface: rest
- limits note: 10 GB per individual file; 300 GB per publication through the web UI; above that it is a negotiated large-data order. Partner institutions sponsor only the first 10 GB, with a Large Data Fee above.
- interface detail: rest
- tooling: REST API + OAI-PMH; DOI minting; integration with manuscript submission systems.
- composes with: None. The fee scales linearly per dataset, so there is no multiplication play. Cost per TB is roughly $6,000 and does not fall with volume ($6.08/GB flat from 500 GB to 2 TB).
- reliability: Highly reliable, curated, POSI-signatory, but gated behind a credit-card payment at submission. Useless as free bulk storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Pay-to-publish (Data Publishing Charge). Up to 5 GB = $150; 1 TB = $6,077; 2 TB = $12,162. Not a free tier in any sense.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: fee table effective May 6 2025: 'Up to 5 GB $150', 'Up to 1 TB $6,077', 'Up to 2 TB $12,162'
  - [1] 2026-10-21: 'Authors not affiliated with a Dryad partner organization are asked to pay a DPC by credit card at the time of submission'
- sources:
  - [1] https://datadryad.org/help/requirements/costs

## dryad (data publishing with fee waiver)

- `storage/dryad-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datadryad.org/help/requirements/costs
- disagrees on identity_kind: `storage/dryad` says institution, `storage/dryad-2` says email
- free tier: none reachable: A publishing charge, not a grant: $150 for a 0-5 GB dataset, rising by size band, and sponsorship exists only through a partner institution or journal. There is no individual waiver and the | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: A publishing charge, not a grant: $150 for a 0-5 GB dataset, rising by size band, and sponsorship exists only through a partner institution or journal. There is no individual waiver and the
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A publishing charge, not a grant: $150 for a 0-5 GB dataset, rising by size band, and sponsorship exists only through a partner institution or journal. There is no individual waiver and the
- sources:
  - [1] https://datadryad.org/help/requirements/costs

## dryad — the 2025-26 pricing model

- `storage/dryad-the-2025-26-pricing-model` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datadryad.org/publishers
- disagrees on identity_kind: `storage/dryad` says institution, `storage/dryad-the-2025-26-pricing-model` says email
- free tier: none reachable: Pay-to-publish, and the price scales with size, so it is anti-correlated with the requirement. Large-data fees: $259 for >10–50 GB, $464 to 100 GB, $1,123 to 250 GB, $2,153 to 500 GB, $4,3 | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Pay-to-publish, and the price scales with size, so it is anti-correlated with the requirement. Large-data fees: $259 for >10–50 GB, $464 to 100 GB, $1,123 to 250 GB, $2,153 to 500 GB, $4,3
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Pay-to-publish, and the price scales with size, so it is anti-correlated with the requirement. Large-data fees: $259 for >10–50 GB, $464 to 100 GB, $1,123 to 250 GB, $2,153 to 500 GB, $4,3
  - [2] 2026-10-21: cited as the basis of the rejection: Pay-to-publish, and the price scales with size, so it is anti-correlated with the requirement. Large-data fees: $259 for >10–50 GB, $464 to 100 GB, $1,123 to 250 GB, $2,153 to 500 GB, $4,3
- sources:
  - [1] https://datadryad.org/publishers
  - [2] https://libraries.ou.edu/get-help/help-research/research-lifecycle/dryad
