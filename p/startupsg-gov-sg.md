# Startup SG Tech

> startupsg.gov.sg | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/startupsg-gov-sg/ | JSON https://fshy.ajam.dev/api/v1/entity/startupsg-gov-sg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Startup SG Tech

- `compute/startup-sg-tech` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.startupsg.gov.sg/programmes/4897/startup-sg-tech/eligibility
- free tier: Competitive grant for deep-tech commercialisation with a POC cap of SGD 400,000 and a POV cap of SGD 800,000, both raised on 2 January 2025 from SGD 250,000 and SGD 500,000. The grant carries an equity component: Enterprise Singapore holds the right to subscribe to shares, and paid-up capital of 10 percent of the POC grant or 20 percent of the POV grant must be shown before award. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): The applicant must be 'Registered in Singapore within the past 10 years', must have 'at least 30% local equity held directly or indirectly by Singaporean(s) and/or Singapore PR(s)', and must carry out 'Core R&D activities ... in Singapore', so a foreign founder with no Singaporean shareholder fails the ownership test before the project is read. [1]
- limits note: The applicant must be 'Registered in Singapore within the past 10 years', must have 'at least 30% local equity held directly or indirectly by Singaporean(s) and/or Singapore PR(s)', and must carry out 'Core R&D activities ... in Singapore', so a foreign founder with no Singaporean shareholder fails the ownership test before the project is read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 30 percent local-ownership rule is what makes this hard to compose: a foreign founder must bring a Singaporean or PR shareholder holding a third of the company before the SGD 800,000 becomes visible, which is a different cost from the capital contribution the grant asks for.
- reliability: no reliability event recorded
- notes: Three gates were considered. (a) Singapore incorporation: confirmed, but it is the cheapest of the three and a foreigner can incorporate a Pte Ltd without a resident director only by appointing a nominee. (b) Local shareholding of 30 percent: confirmed, and this is the binding one, because it is an ownership test rather than a registration step. (c) A paid-up capital requirement: confirmed at 10 or 20 percent of the grant, which for the POV cap is SGD 160,000 that must exist before award, so the grant is really a matching instrument. The 'artificial intelligence (e.g. deep learning)' line under Information & Communications Technologies is the only sub-area that names AI directly, so a project must be framed inside one of the five listed areas to qualify at all.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'The grant cap for POC will remain at SGD400,000'; 'the grant cap for POC projects has been raised from the previous cap of SGD250,000 to SGD400,000', quoted
  - [1] 2026-10-22: 'The grant cap for POV will remain at SGD800,000'; raised 'from the previous cap of SGD500,000', quoted
  - [1] 2026-10-22: 'Company has at least 30% local equity held directly or indirectly by Singaporean(s) and/or Singapore PR(s), determined by the ultimate individual ownership', quoted
  - [1] 2026-10-22: 'Registered in Singapore within the past 10 years at time of grant application'; 'Core R&D activities to be carried out in Singapore'; 'Company is not a subsidiary of a corporate entity at point of incorporation', quoted
  - [1] 2026-10-22: 'startups will be required to demonstrate existing paid-up capital equivalent to at least 10% of the POC grant' and '20% of the POV grant', quoted
  - [2] 2026-10-22: 'the grant will also carry an equity component where Enterprise Singapore will have the rights to exercise a share subscription', quoted, page last updated 2025-09-18
- sources:
  - [1] https://www.startupsg.gov.sg/programmes/4897/startup-sg-tech/eligibility
  - [2] https://www.startupsg.gov.sg/programmes/4897/startup-sg-tech
