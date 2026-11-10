# Mozilla Builders

> mozilla.org | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mozilla/ | JSON https://fshy.ajam.dev/api/v1/entity/mozilla.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mozilla Open Source

- `compute/mozilla-open-source` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.mozilla.org/en-US/moss/
- free tier: 'Generally anyone who maintains an open source project can apply to MOSS, including individuals, NGOs, and for-profit companies' and 'the MOSS Committee has mostly chosen to award between $5,000 and $150,000 USD per project; the average project size is roughly $70,000 USD'. Applications 'are accepted on a rolling basis and are reviewed monthly'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: cash-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The project must already be important in its ecosystem with an active user and contributor community; the committee states it does not consider brand new projects, so the first award is not reachable tonight. [1]
- limits note: The project must already be important in its ecosystem with an active user and contributor community; the committee states it does not consider brand new projects, so the first award is not reachable tonight.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 70,000 average is the largest per-person award among evaluated providers after OTF, and it is paid as an award rather than a salary, so it can be spent entirely on rented accelerators during the stated work period.
- reliability: no reliability event recorded
- notes: Two real bars: maturity (no new projects) and, for Track I, a Mozilla insider willing to write an endorsement, which is a social gate no application can substitute for. Track II takes other projects without that letter. Mozilla pays as an award and states that recipients handle their own tax treatment; it reserves the right to use different payment mechanisms per award, so the payout route for an individual outside the US is not published.
- extras:
  - facets.class: grant-individual
  - facets.free_tier_kind: cash-grant
- evidence:
  - [1] 2026-10-22: quoted the award range and average, the rolling monthly review, the individual eligibility sentence, 'Individual applicants should not include indirect costs in their budget', the maturity bar, and the OSI or FSF licence requirement
  - [1] 2026-10-22: Track I (Foundational Technologies) applications 'should include an endorsement from a Mozilla Champion who can describe how your project is used by Mozilla and why it is an important dependency'
- sources:
  - [1] https://www.mozilla.org/en-US/moss/

## Mozilla Builders Accelerator

- `compute/mozilla-builders-accelerator` | dead | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://builders.mozilla.org/programs/
- free tier: The programme's own page still advertises, quoted: 'The Accelerator funds and supports work vital to the open-source AI ecosystem. It provides up to $100,000 in non-dilutive funding and a focused 12-week curriculum.' The only dates on it are from 2024, quoted: 'June 3, 2024 Accelerator Applications Open', 'August 1, 2024 Final Application Due', 'September 12, 2024 Accelerator Kickoff', 'December 5, 2024 Demo Day'. The page is headed 'Programs 2024' and lists an 'Accelerator 2024' cohort of 14 named builders. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): there is no open application window: the last published cycle closed its final application on August 1, 2024, and no 2025 or 2026 call appears on the programme page, so the constraint that fails first is the absence of a round rather than any term. [1]
- limits note: there is no open application window: the last published cycle closed its final application on August 1, 2024, and no 2025 or 2026 call appears on the programme page, so the constraint that fails first is the absence of a round rather than any term.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nil while closed. The composition that would matter is the one earlier readings already records for Mozilla Foundation: the separate Human-Scale AI Incubator is live with a November 20, 2026 deadline and USD 300,000 base awards, so a builder who wants Mozilla money today goes there, not here.
- reliability: no reliability event recorded
- notes: The program was integrated into the Foundation's Incubator.
- extras:
  - facets.class: grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'Accelerator funds and supports work vital to the open-source AI ecosystem. It provides up to $100,000 in non-dilutive funding and a focused 12-week curriculum'; 'Programs 2024'; key dates 'June 3, 2024', 'August 1, 2024', 'September 12, 2024', 'December 5, 2024'; 'Accelerator 2024' cohort listed; upstream status 403, body rendered through a provider, page content served
  - [2] 2026-10-22: 'Builders helps developers create transformative open-source AI projects through collaborations, programming, and community. Check out the projects we're supporting.', with no funding call and no application link on the landing page; origin status 403, body rendered through a provider
  - [3] 2026-10-22: third-party review dated 'Last checked Oct 2, 2026': 'Historical 2024 accelerator: up to $100,000', 'The listed 2024 application window has closed', 'the reviewed page does not announce an open 2026 funding cohort' (reported, not the vendor's own page)
- sources:
  - [1] https://builders.mozilla.org/programs/
  - [2] https://builders.mozilla.org/
  - [3] https://heap.page/software/mozilla-builders
