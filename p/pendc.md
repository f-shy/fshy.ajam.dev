# PenDC

> pendc.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pendc/ | JSON https://fshy.ajam.dev/api/v1/entity/pendc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PenDC

- `compute/pendc` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:55.982Z (live) | stale on 2026-12-05
- url https://www.pendc.com/
- free tier: Two months of free server hosting, stated on the homepage as a campaign: '2 AY UCRETSIZ BARINDIRMA' (2 months free hosting), requested by contact rather than by self-serve order. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The home page lists 'Sınırsız trafik imkanı' (unlimited traffic) under Cloud Sunucu; no overage price is published. | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The campaign is claimed through a contact form or phone call and not through a self-serve checkout, so the allocation depends on a human agreeing to it. [1]
- limits note: The campaign is claimed through a contact form or phone call and not through a self-serve checkout, so the allocation depends on a human agreeing to it.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Two months of a Turkish-hosted server is a latency test for the Turkish market rather than a compute allowance, because no configuration is stated.
- reliability: no reliability event recorded
- notes: The Turkish market's free lane is almost entirely this shape: a campaign with no published configuration, claimed by talking to sales. PenDC is recorded because it is the one the Turkish forums name, and the discrepancy between the site's two months and the forum's three months is itself the finding: neither figure is a published quota. No spec, no traffic term and no price are stated on the homepage, so all of those are null rather than guessed.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: '2 AY UCRETSIZ SUNUCU BARINDIRMA ICIN HEMEN TIKLA' linking to the contact page, and '2 AY UCRETSIZ BARINDIRMA' under the campaign heading, quoted
  - [2] 2026-10-22: a Turkish forum thread states 'Turkiye'de de PenDC 3 ay ucretsiz veriyor' (PenDC gives 3 months free in Turkey), which contradicts the site's own 2 months, reported
  - [1] 2026-11-03: the cloud server card states unlimited traffic | capture: sha256:f9bdef1fb80e052f34624240a44485c3ff50a426e5a59ab882846574c59ac858 | quote: - Sınırsız trafik imkanı
- sources:
  - [1] https://www.pendc.com/
  - [2] https://www.technopat.net/sosyal/konu/bedava-veya-ucuz-vds-var-mi.3713191/
