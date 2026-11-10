# Start-Up Chile

> startupchile.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/startupchile/ | JSON https://fshy.ajam.dev/api/v1/entity/startupchile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Start-Up Chile

- `compute/start-up-chile` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://startupchile.org/content/uploads/brochure-big-13-eng-2026-1.pdf
- free tier: Equity-free co-financing for a 4-month programme, published for generation BIG 13 as BUILD CLP 15M (about USD 16K), IGNITE CLP 30M (about USD 33K) and GROWTH CLP 75M (about USD 83K). The brochure states 'WE ARE AGNOSTIC TO NATIONALITIES' and CORFO's eligibility line reads 'Personas naturales chilenas o extranjeras, mayores de 18 anos'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The money is a co-financing reimbursement against a project executed in Chile, capped at 90 percent of cost, and IGNITE and GROWTH require a Chilean legal entity with tax activity started at the SII, so the first disbursement needs either a Chilean entity or a relocation. [1]
- limits note: The money is a co-financing reimbursement against a project executed in Chile, capped at 90 percent of cost, and IGNITE and GROWTH require a Chilean legal entity with tax activity started at the SII, so the first disbursement needs either a Chilean entity or a relocation.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- reliability: no reliability event recorded
- notes: Two published documents disagree on the IGNITE ceiling: the BIG 13 brochure states CLP 30M (about USD 33K) while the CORFO Ignite 12 call page states a cap of CLP 50.000.000 for line 2. The next opening is expected around November 2026 because two generations run per year.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'WE ARE AGNOSTIC TO NATIONALITIES'; BUILD 'Equity-free funding, CLP $15M (~16K USD)'; IGNITE 'CLP $30M (~33K USD)'; GROWTH 'CLP $75M (~83K USD)', quoted
  - [2] 2026-10-22: 'Personas naturales chilenas o extranjeras, mayores de 18 anos' may apply; subsidy 'Hasta $15.000.000 para la linea 1. Hasta $50.000.000 para la linea 2. Hasta $75.000.000 para la linea 3', quoted
  - [3] 2026-10-22: eligibility names 'Personas juridicas con fines de lucro, constituidas en Chile con iniciacion de actividades ante el Servicio de Impuestos Internos' as the entity route, quoted
  - [2] 2026-10-22: the generation table shows Build 12, Ignite 12 and Growth 12 all opened 04/05/2026 and closed 25/05/2026 with results 10/07/2026, read from the published schedule
- sources:
  - [1] https://startupchile.org/content/uploads/brochure-big-13-eng-2026-1.pdf
  - [2] https://www.corfo.gob.cl/sites/cpp/programa/startup-chile/
  - [3] https://www.corfo.gob.cl/sites/cpp/convocatoria/start-up-chile-growth-12-2026/
