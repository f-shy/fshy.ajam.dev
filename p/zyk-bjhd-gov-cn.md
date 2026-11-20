# Haidian District Elastic

> zyk.bjhd.gov.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zyk-bjhd-gov-cn/ | JSON https://fshy.ajam.dev/api/v1/entity/zyk-bjhd-gov-cn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Haidian District Elastic

- `compute/haidian-district-elastic` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://zyk.bjhd.gov.cn/zwdt/zcjd/202501/t20250121_4755086.shtml
- free tier: District government guideline, verbatim: 'The laboratory construction period is no more than 3 years; first-year support is no more than CNY 27,000,000, spent on compute rental, related configuration and operations. The laboratory compute serves no fewer than 30 quality projects or talent teams each year and must convert at least 8 into companies.' Eligibility, verbatim: 'The project founder or individual must meet at least one of: 1. a QS top-200 university background; 2. work experience at a leading domestic or overseas big-tech firm; 3. work experience at a star startup valued above CNY 1 billion or an AI unicorn; 4. fine-tuning experience on 8 or more GPUs; 5. an existing product demo plus open-source contribution, such as a GitHub or Hugging Face project with at least 100 stars; 6. backing from multiple investors.' | unit: none | metered on: wall-clock | read on: 2025-01-21 | source: [1] | note: government-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: national-id
- interface: unknown
- limits:
  - write-gated (binding): The money is municipal and the bar is a credential screen, not a signup: CNY 27,000,000 a year over at least 30 projects caps the average award near CNY 900,000, and the six criteria require an elite affiliation or a pre-existing track record. [1]
- limits note: The money is municipal and the bar is a credential screen, not a signup: CNY 27,000,000 a year over at least 30 projects caps the average award near CNY 900,000, and the six criteria require an elite affiliation or a pre-existing track record.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the upstream reason the MiraclePlus ceiling exists. The credits a researcher receives are municipal money administered by an operator, so the award size is bounded by a district budget line rather than by a commercial free tier. It composes with nothing, because it is the funding behind the resource and not a resource itself.
- reliability: no reliability event recorded
- notes: THE NUMBER THAT DECIDES THE SHAPE: CNY 27,000,000 divided by at least 30 projects gives an average ceiling near CNY 900,000 per project, consistent with and slightly below the published CNY 1,000,000 maximum. That is arithmetic proof that the million is a per-project cap inside a fixed municipal budget, not a standard award. TWO LAYERS, and the distinction carries the verdict: the laboratory guideline is a credential screen written for the operating entity and its intake; MiraclePlus runs its own intake in front of it and publishes no such list, naming instead research capability, technical fit and project potential. An unaffiliated individual therefore faces no formal document barrier but a de facto one, because the intake behind the panel selects for exactly those credentials. The fails-identity verdict is recorded against this record because the public funding terms are the ones that bind; the sibling MiraclePlus record carries the softer verdict so a reader sees both. UNCERTAIN: whether MiraclePlus applies the six criteria literally to every compute applicant or uses them only as a preference. Nothing published says, and the two documents are silent about each other. Re-verified 2026-10-22 by raw fetch rather than by the text extractor. The notice is still served.
- extras:
  - facets.class: municipal-grant
  - facets.free_tier_kind: government-grant
  - facets.shape.gpu_class: H800
  - facets.shape.gpu_count: 8
- evidence:
  - [2] 2026-10-22: quoted, translated from the application guide published with the same notice: 'the laboratory construction period is no more than 3 years; first-year support funding is no more than CNY 27,000,000' and 'the laboratory compute is used for no fewer than 30 quality projects or outstanding talent teams each year', plus the six eligibility criteria verbatim (QS top-200 university background; work experience at a leading domestic or overseas big-tech firm; work experience at a star startup valued above CNY 1 billion or an AI unicorn; fine-tuning experience on 8 or more GPUs; an existing product demo plus an open-source project with at least 100 stars; backing from multiple investors). Supports every figure and the credential screen the stored claim rests on. Caveat: the page's own heading is prefixed with the Chinese word for lapsed, read from the raw HTML, so the 2025 application round is closed while the terms stay published
  - [1] 2026-10-22: re-read 2026-10-22 by raw fetch: the page returns 14,598 bytes of HTML and the served text still contains the scheme terms, including the word for laboratory (实验室), the figure 2700 and the declaration term (申报); the text extractor returns nothing for this host
- sources:
  - [1] https://zyk.bjhd.gov.cn/zwdt/zcjd/202501/t20250121_4755086.shtml
  - [2] https://zyk.bjhd.gov.cn/zwdt/zcwj/202501/t20250121_4755081.shtml
