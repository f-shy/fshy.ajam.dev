# CDTI Neotec 2026

> cdti.es | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cdti/ | JSON https://fshy.ajam.dev/api/v1/entity/cdti.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CDTI Neotec 2026

- `compute/cdti-neotec-2026` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:49.065Z (live) | stale on 2026-12-04
- url https://www.cdti.es/ayudas/ayudas-neotec-2026
- free tier: Subsidies of up to 70 percent of the eligible budget, capped at EUR 250,000 per beneficiary, raised to 85 percent and EUR 325,000 where at least one doctorate holder is hired, on a total call budget of EUR 20,383,300 with a minimum reserve of EUR 5,000,000 for projects led by women. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): Beneficiaries must be 'constituidas como maximo en los tres anos anteriores a la fecha de cierre' and registered in the Spanish mercantile registry, with a minimum eligible budget of EUR 175,000 that the applicant must be able to fund alongside the subsidy. [1]
- limits note: Beneficiaries must be 'constituidas como maximo en los tres anos anteriores a la fecha de cierre' and registered in the Spanish mercantile registry, with a minimum eligible budget of EUR 175,000 that the applicant must be able to fund alongside the subsidy.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The EUR 175,000 minimum eligible budget is the clause that decides usability: at a 70 percent rate the smallest viable award is EUR 122,500 of subsidy against at least EUR 52,500 of the applicant's own money, so this is a grant for a company already spending, not seed capacity for a person testing an idea.
- reliability: no reliability event recorded
- notes: The 85 percent and EUR 325,000 tier is the number most summaries omit, and it is reachable only by hiring a doctorate holder, which is a real cost rather than a formality. The EUR 250,000 cap is per company across the call, not per project: the resolution says 'por entidad beneficiaria'. A foreign founder can plausibly hold a Spanish S.L. and apply, because the eligibility test is registration and age, not nationality, and the resolution names no nationality condition in the articles read. So the identity gate is the company rather than the person, and it is one of the cheapest company gates, alongside Malaysia's RM 1,000 paid-up capital.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'Subvenciones hasta el 70% del presupuesto elegible de la actuacion, con un importe maximo de subvencion de 250.000 euros por beneficiario'; 'Reserva presupuestaria minima de 5.000.000 euros destinados a proyectos liderados por mujeres'; '20.383.300 euros', quoted
  - [2] 2026-10-22: 'con un importe maximo de subvencion de 250.000 euros por entidad beneficiaria'; with a doctorate hire 'hasta el 85% ... con un importe maximo de subvencion de 325.000 euros por entidad beneficiaria', quoted from Articulo 6
  - [2] 2026-10-22: 'Estar constituidas como maximo en los tres anos anteriores a la fecha de cierre del plazo de presentacion de solicitudes'; 'El presupuesto minimo financiable de la actuacion debera ser de 175.000 euros'; 'El presupuesto maximo financiable ... debera ser de 750.000 euros', quoted
  - [2] 2026-10-22: actuaciones 'deberan iniciarse el 1 de enero de 2027', quoted from Articulo 6
  - [1] 2026-11-03: the subsidy is up to 70 percent of the eligible budget and at most EUR 250,000 per beneficiary; the page lists no GPU or hourly price | capture: sha256:87154af1ef697eb616186c5227fb775c752ecda4514cbc434ea593b96a7e308d | quote: Subvenciones hasta el 70% del presupuesto elegible de la actuación, con un importe máximo de subvención de 250.000 euros por beneficiario.
- sources:
  - [1] https://www.cdti.es/ayudas/ayudas-neotec-2026
  - [2] https://www.cdti.es/sites/default/files/2026-04/convocatoria_neotec_2026.pdf
