# Fast Grants

> fastgrants.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastgrants/ | JSON https://fshy.ajam.dev/api/v1/entity/fastgrants.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fast Grants

- `compute/fast-grants` | dead | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.fastgrants.org/
- free tier: The programme is offline. The domain now returns, quoted: 'This page doesn't exist - It may have been moved, removed, or never existed. 404 DEPLOYMENT_NOT_FOUND', which is a Vercel deployment error rather than a page. The archived version from 2021 states the scope, quoted: 'Funding for scientists at academic institutions working on COVID-19 related projects.' That sentence is also the reason the programme is out of lane: it funded COVID-19 bioscience at academic institutions, not compute. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): the door is shut and was always conditional on an academic institution: the site is a dead deployment, and the 2021 capture limits the grant to scientists at academic institutions working on COVID-19. [1]
- limits note: the door is shut and was always conditional on an academic institution: the site is a dead deployment, and the 2021 capture limits the grant to scientists at academic institutions working on COVID-19.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nil. Recording it stops the next reader from chasing a name that appears on lists of fast science funding and has never had a compute lane.
- reliability: no reliability event recorded
- notes: Any future program under the same name would represent a distinct offering.
- extras:
  - facets.class: grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'This page doesn't exist'; '404 DEPLOYMENT_NOT_FOUND'; 'bom1::9l4zl-1792682528794-85ed34daf84f'; page 404 at origin
  - [2] 2026-10-22: the 2021 capture's own description: 'Funding for scientists at academic institutions working on COVID-19 related projects.', and its body lists funded COVID-19 preprints and papers; capture 20210602095236 returned 200
  - [3] 2026-10-22: the archive lookup resolved exactly one capture at 121956 s from the requested 2021-06, which dates the page to June 2021 and shows no later capture in the queried window
  - [4] 2026-10-22: measured: the live host returns HTTP 404 with body 'DEPLOYMENT_NOT_FOUND' from Vercel, so the site no longer exists
  - [5] 2026-10-22: reported: 'Between the first and second rounds of funding, Fast Grants distributed over $40 million in grants before suspending the program'
  - [6] 2026-10-22: reported by a university research office: 'Due to receipt of a very large number of qualified submissions, Fast Grant applications are currently closed'
- sources:
  - [1] https://www.fastgrants.org/
  - [2] https://web.archive.org/web/20210602095236id_/https://fastgrants.org/
  - [3] https://web.archive.org/web/20210602095236/https://fastgrants.org/?provider=wayback
  - [4] https://fastgrants.org/
  - [5] https://www.influencewatch.org/non-profit/fast-grants/
  - [6] https://www.uoguelph.ca/research/alerts/content/fast-funding-covid-19-science
