# Bpifrance

> bpifrance.fr | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bpifrance/ | JSON https://fshy.ajam.dev/api/v1/entity/bpifrance.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bpifrance

- `compute/bpifrance` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:49.065Z (live) | stale on 2026-12-04
- url https://www.bpifrance.fr/catalogue-offres/bourse-french-tech
- free tier: A grant of 'un montant maximum de 30 000 EUR sous condition', covering up to 50 percent of eligible expenses and up to 70 percent for some company categories, over a programme of at most 24 months, for a PME under the European SME definition. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The beneficiary must be an entity registered in France and less than one year old, or a physical person in pre-creation accompanied by a labelled incubator, so the door needs either French incorporation or a French support structure willing to sponsor the file. [1]
- limits note: The beneficiary must be an entity registered in France and less than one year old, or a physical person in pre-creation accompanied by a labelled incubator, so the door needs either French incorporation or a French support structure willing to sponsor the file.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The rule that no expense incurred before the application date is eligible makes this a forward-looking budget rather than a rebate, so it cannot pay for compute already burned while testing; it composes with a vendor trial only if the trial is structured as an expense after filing.
- reliability: no reliability event recorded
- notes: This finding contains a refutation. The aggregator figure is wrong or describes a different scheme, and the smaller number is recorded. The physical-person route is the only clause that admits somebody without a company, and it is conditioned on an incubator that has its own selection committee, which converts a formality into a discretionary review.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'Aide sous forme de subvention d'un montant maximum de 30 000 EUR sous condition'; 'Cette aide peut couvrir jusqu'a 50 % des depenses eligibles et selon la categorie de l'entreprise, jusqu'a 70 %'; 'Programme d'une duree maximum de 24 mois', quoted
  - [1] 2026-10-22: 'Aucune depense engagee anterieurement a la date de depot de la demande d'aide ne peut etre retenue', quoted
  - [2] 2026-10-22: 'Entrepreneurs personnes physiques, y compris s'ils sont constitues en entreprise individuelle, sous reserve d'etre accompagnes par des structures ... dediees a l'accompagnement de projets innovants', and 'Montant maximum : 30 000 EUR', quoted, regional French Tech network
  - [3] 2026-10-22: '50 000 euros : c'est le plafond de la Bourse French Tech', stated by a grant aggregator, which the Bpifrance page contradicts
  - [1] 2026-11-03: the grant is at most EUR 30,000; the page lists no GPU or hourly price | capture: sha256:1096ad3f8e7e2d9ef199231f8c1c189eae6b38c437728dd9c0f7914ab4043cca | quote: Aide sous forme de subvention d'un montant maximum de 30 000 € sous condition.
- sources:
  - [1] https://www.bpifrance.fr/catalogue-offres/bourse-french-tech
  - [2] https://lafrenchtech-aixmarseille.fr/dispositif_financeme/bourse-french-tech/
  - [3] https://subventions.fr/insights/bourse-french-tech-guide/
