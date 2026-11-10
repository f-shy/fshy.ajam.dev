# ITIDA StartIT

> itida.gov.eg | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/itida-gov-eg/ | JSON https://fshy.ajam.dev/api/v1/entity/itida-gov-eg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ITIDA StartIT /

- `compute/itida-startit` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:14.342Z (live) | stale on 2026-12-05
- url https://itida.gov.eg/English/Pages/Incubation.aspx
- free tier: USD 10,000 of AWS credit within a one-year incubation: "AWS Services with $10,000 credit on AWS" (the Cloud Services row of the host package) and "The lifespan of TIEC incubation is a year." | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: incubation-with-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: no egress allowance or overage price on https://itida.gov.eg/English/Pages/Incubation.aspx, read 2026-11-04 | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): Selection needs a working ICT prototype or proof of concept rather than an idea, applicants pitch to a judging panel, and delivery is in person at a TIEC office in Egypt, so the binding cost is presence plus a built artefact, not a company document. [1]
- limits note: Selection needs a working ICT prototype or proof of concept rather than an idea, applicants pitch to a judging panel, and delivery is in person at a TIEC office in Egypt, so the binding cost is presence plus a built artefact, not a company document.
- binding note: the same as limits note
- interface detail: not published: the page names an online application form (login required) and no REST API, CLI, SSH or SDK; the credit is held in an AWS account
- tooling: not stated
- composes with: This is the best composition found in the Africa and MENA slice: USD 10,000 of AWS credits arrives with no equity and no cash cost, so it stacks cleanly on top of AWS's own always-free tier and any AWS Activate credit, and the twelve-month incubation is long enough for a credit balance to be spent rather than expire against it.
- reliability: no reliability event recorded
- notes: Whether a company is required is unresolved: no page read names an incorporation document, and the published exclusion is only that undergraduates cannot apply. The round is open for an October 2026 intake according to a third-party tracker at a 31 October 2026 deadline, while ITIDA's own incubation page states no deadline, and two other pages carry different dates, one closing 1 August 2026 and one describing a 2027 cohort beginning 1 January 2027. The date discrepancy is the finding to carry forward: the rounds are frequent enough that a reader should check ITIDA's own press releases rather than any aggregator.
- extras:
  - facets.class: government-incubator
  - facets.free_tier_kind: incubation-with-credit
  - facets.shape.gpu_class: provider-dependent (AWS)
- evidence:
  - [1] 2026-10-22: 'Funding: EGP 480,000 Fund'; 'Cloud Services: AWS Services with $10,000 credit on AWS'; 'The lifespan of TIEC incubation is a year', quoted
  - [2] 2026-10-22: 'support from Amazon Web Services (AWS) has been raised to $10,000 in cloud credits per startup, doubling the previous amount', quoted, ITIDA press release
  - [3] 2026-10-22: 
  - [4] 2026-10-22: 'Deadline: 31 October 2026, 11:59 PM'; 'Nationality rules are not stated'; 'You need a working prototype or proof of concept; undergraduates are also excluded', reported by a third-party opportunity tracker
  - [5] 2026-10-22: 'The incubation period will run for 12 months, starting on January 1, 2027', reported
  - [1] 2026-10-30: the incubation package's Cloud Services row is USD 10,000 of AWS credit | capture: sha256:84d89d38594dad6ece70b5c6789f1e454ba8b68890428b50f235cc5e1f7e3da9 | quote: AWS Services with $10,000 credit on AWS
  - [1] 2026-10-30: the incubation that carries the credit lasts one year | capture: sha256:84d89d38594dad6ece70b5c6789f1e454ba8b68890428b50f235cc5e1f7e3da9 | quote: The lifespan of TIEC incubation is a year.
  - [1] 2026-11-04: the page offers this and its text carries no traffic-out term, allowance or price | capture: sha256:84d89d38594dad6ece70b5c6789f1e454ba8b68890428b50f235cc5e1f7e3da9 | quote: | Cloud Services | AWS Services with $10,000 credit on AWS |
- sources:
  - [1] https://itida.gov.eg/English/Pages/Incubation.aspx
  - [2] https://itida.gov.eg/English/PressReleases/Pages/start-it-47-cohort-digital-perks-2025.aspx
  - [3] https://egyptinnovate.com/en/challenge-center/startit-incubation-program-2
  - [4] https://startuphub.today/en/opportunity-radar/50/egp-480-000-of-equity-free-support-for-ict-startups-startit-october-2026
  - [5] https://menastartupdigest.com/itida-opens-applications-for-2027-startit-startup-incubator-in-egypt/
