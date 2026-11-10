# NAIRR Pilot

> nairrpilot.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nairrpilot/ | JSON https://fshy.ajam.dev/api/v1/entity/nairrpilot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NAIRR Pilot

- `compute/nairr-pilot` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://nairrpilot.org/opportunities/allocations
- free tier: Compute, model and platform allocations from federal agencies and contributing partners, 'awarded for twelve (12) months duration', spread across a resource catalogue that includes national-lab and commercial partner capacity. The eligibility sentence and the email rule are the whole finding: 'This call is open to meritorious proposals by US-based researchers and educators from US-based institutions including academic institutions ..., non-profits, federal agencies or federally funded R&D centers, state, local, or tribal agencies, startups and small businesses with federal grants.' and 'Note that the email address you provide must be your institutional email. Requests providing personal email addresses such as .gmail.com addresses will not be considered.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a US institutional email address: the call states 'the email address you provide must be your institutional email. Requests providing personal email addresses such as.gmail.com addresses will not be considered', and the applicant must be at a US-based institution. A university briefing deck adds that U.S. citizenship is not required unless a resource says so, reported. No card or hold is stated; the proposal also needs a three-page PDF and survives a peer review
- interface: unknown
- limits:
  - write-gated (binding): a US institutional email is checked before the proposal is read, and the proposal itself needs a three-page PDF plus a peer review, so an unaffiliated applicant is excluded twice. [1]
- limits note: a US institutional email is checked before the proposal is read, and the proposal itself needs a three-page PDF plus a peer review, so an unaffiliated applicant is excluded twice.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. The allocation is bound to a US institution and to a named PI whose affiliation is published, so it cannot be held by an individual.
- reliability: no reliability event recorded
- notes: Worth recording because NAIRR is the program a reader is most likely to be told to try, and the exclusion is unusually explicit: not only an institution, but an institutional email address, with the.gmail case named. The one softening clause is real and should not be overstated - 'Proposals for research activities without merit-reviewed support will be accepted' removes the federal-grant precondition inside the eligible institution class, but does not create an unaffiliated lane. The pilot's own end date is unbounded ('until the end of the NAIRR Pilot program or until all resources have been committed'), which is a second reason not to treat it as durable capacity.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: 'Projects will be awarded for twelve (12) months duration'; 'This call is open to meritorious proposals by US-based researchers and educators from US-based institutions'; 'the email address you provide must be your institutional email. Requests providing personal email addresses such as .gmail.com addresses will not be considered'; 'Proposals for research activities without merit-reviewed support will be accepted, but will be subject to additional review', quoted; page 200
  - [1] 2026-10-22: 'Proposals require completing a form and uploading a three-page PDF proposal'; 'All supported projects will have the name of the principal investigator (PI), their affiliation, the project title, and project abstract posted on the NAIRR Pilot website'; a 1-month and 6-month update plus a three-page final report are required
  - [2] 2026-10-22: a contributing partner's restatement agrees: 'applicants must be US-based researchers and educators from US-based institutions including academic institutions, non-profits, federal agencies or federally funded R&D centers, state, local, or tribal agencies, or startups and small businesses with federal grants'
  - [1] 2026-10-22: 'This call is open to meritorious proposals by US-based researchers and educators from US-based institutions'; 'Requests providing personal email addresses such as .gmail.com addresses will not be considered', quoted
  - [3] 2026-10-22: 'Principal Investigator / Lead Instructor and all other users must perform work via an eligible organization physically based in the U.S.'; 'U.S. citizenship is not required, unless noted in resource-specific requirements', reported from a university briefing deck
  - [4] 2026-10-22: NSF established a NAIRR Operations Center on 1 September 2026 led by the San Diego Supercomputer Center, so the programme is transitioning rather than closing
- sources:
  - [1] https://nairrpilot.org/opportunities/allocations
  - [2] https://www.microsoft.com/en-us/research/project/national-ai-research-resource-nairr-pilot/who-can-apply/
  - [3] https://www.depts.ttu.edu/hpcc/downloads/2025-09-29_Requesting-Resources-via-the-NAIRR-Pilot.pdf
  - [4] https://nairrpilot.org/

## nairr pilot (us) as a storage route

- `storage/nairr-pilot-as-a-storage-route` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nairrpilot.org/opportunities/allocations
- free tier: none reachable: Twelve-month compute/model awards for AI research; eligibility is 'US-based researchers and educators from US-based institutions' with an institutional email, and the resource list is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: Twelve-month compute/model awards for AI research; eligibility is 'US-based researchers and educators from US-based institutions' with an institutional email, and the resource list is…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Twelve-month compute/model awards for AI research; eligibility is 'US-based researchers and educators from US-based institutions' with an institutional email, and the resource list is…
- sources:
  - [1] https://nairrpilot.org/opportunities/allocations
