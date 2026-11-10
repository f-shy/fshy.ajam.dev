# Emergent Ventures

> mercatus.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mercatus/ | JSON https://fshy.ajam.dev/api/v1/entity/mercatus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Emergent Ventures

- `compute/emergent-ventures` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.mercatus.org/emergent-ventures
- free tier: A rolling grant and fellowship programme running since 2018 with no published range. published words, quoted: 'We encourage you to think big, but we also will consider very small grants if they might change the trajectory of your life. We encourage applications from all ages and all parts of the world.' On the amount: 'There is NO typical grant range or average award amount - funding is project specific.' On credentials: 'We probably don't care much about your formal education, credentials, or awards, unless they're particularly germane to who you are or your idea.' The only stated eligibility bar is age: 'To be eligible for an EV grant, all applicants must be 13 years of age or older.' The route is a 1,500-word proposal through a form, with dedicated lanes for India, Africa and the Caribbean, and Ukraine. One condition applies to how the text is produced: 'Emergent Ventures no longer accepts AI-written applications. We will test all submissions and reject those using AI for anything other than proofreading.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an individual aged 13 or over, anywhere. No affiliation, company or degree is requested, and the form explicitly says credentials will not impress. The atlas of grantees records recipients in 116 countries, which includes the likely target jurisdictions.
- interface: unknown
- limits:
  - write-gated (binding): a competitive written proposal read by the programme's director fails first, and because the programme publishes no typical amount the expected value of an award cannot be computed before applying. [1]
- limits note: a competitive written proposal read by the programme's director fails first, and because the programme publishes no typical amount the expected value of an award cannot be computed before applying.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cash with no vendor lock, so it composes with everything: even a very small award, which the operator says it will consider, buys marketplace GPU hours outright. The dedicated India, Africa and Caribbean and Ukraine lanes are the reason this record matters more than its unpublished size, because they show a non-US applicant is a first-class case rather than a tolerated one.
- reliability: no reliability event recorded
- notes: First, the form's own words confirming the two conditions it cited, read at first party. Second, a throughput figure grounded in a published index rather than in a tracker: 1,082 grantees across 53 main cohorts, 15 India cohorts, 116 countries, 2018 to 2026, from an independent atlas that states it compiled every published cohort announcement, with the announcement channel being the director's own blog. Third, the failure mode, which the existing record notes but does not name as the first thing that breaks. What remains unestablished: the amount distribution (the existing record's 'USD 1k to USD 50k typical' is attributed to third-party trackers and is not on any operator page read), the acceptance rate (no applicant count is published), and the payout rail for a non-US individual. Routes tried for those: the operator page, the application form, the atlas and two searches; no page states an applicant count.
- extras:
  - facets.class: independent-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [2] 2026-10-22: the application form itself: 'we also will consider very small grants if they might change the trajectory of your life. We encourage applications from all ages and all parts of the world.'; 'There is NO typical grant range or average award amount - funding is project specific.'; 'We probably don't care much about your formal education, credentials, or awards'; 'To be eligible for an EV grant, all applicants must be 13 years of age or older.'; 'The proposal should be no longer than 1500 words'; 'we will test all submissions and reject those using AI for anything other than proofreading'; quoted; page 200
  - [1] 2026-10-22: 'Launched in 2018, Emergent Ventures is a low-overhead fellowship and grant program'; 'Grants are awarded to thinkers and doers around the world, with dedicated support available for projects with a focus on India, Africa and the Caribbean, or Ukraine'; 'all applicants must be 13 years of age or older'; quoted; page served through a rendering provider because the origin answered 403
  - [3] 2026-10-22: an independent atlas that compiled every published cohort: 'Grantees indexed 1,082', 'Main cohorts 53', 'India cohorts 15 + 1 Africa', 'Countries 116', '2018-2026', 'Latest main cohort Cohort 53'; labelled 'An unofficial atlas', so this is reported rather than documented; page 200
  - [4] 2026-10-22: 
- sources:
  - [1] https://www.mercatus.org/emergent-ventures
  - [2] https://mercatus.tfaforms.net/5099527
  - [3] https://emergentventures.vercel.app/
  - [4] https://marginalrevolution.com/marginalrevolution/2018/11/emergent-ventures-grant-recipients.html

## Emergent Ventures (Mercatus Center) - 13+, worldwide, no institution

- `storage/emergent-ventures-13-worldwide-no-institution-fastest-in` | qualifies-with-caveat | evidence reported | binding write-gated | category grant
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mercatus.org/emergent-ventures
- free tier: Open-budget microgrant: no fixed cap. Third-party trackers report a $1k-$50k typical range and up to $100k over two years, but the programme itself publishes no range - budgets are evaluated case by case. Rolling applications, one 1,500-word proposal, occasional 10-15 minute interview. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: n/a - cash. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated (binding): applications, one 1,500-word proposal, occasional 10-15 minute interview [1]
  - write-gated (binding): application per applicant per project [1]
- limits note: Applicants must be at least 13 years old; one application per applicant per project. AI-written applications are now rejected outright ('We will test all submissions and reject those using AI for anything other than proofreading') - relevant given how this research was produced.
- interface detail: n/a
- tooling: the same as interface detail
- composes with: Dedicated tranches (Africa/Caribbean, India, UK Dynamism, Ukraine, Archaeology, Travel for Career Development, US Science Policy) each have their own budget, so a project can be aimed at the tranche where it fits best.
- reliability: One-time or slightly staggered payments; no reporting burden. The realistic ceiling for a storage project is a few thousand dollars, i.e. tens of TB-months - enough to self-fund a year of Hetzner, not a decade.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Applicants must be at least 13 years old'; 'Emergent Ventures no longer accepts AI-written applications'; tranche list
  - [1] 2026-10-21: the live application form
  - [3] 2026-10-21: 'a 1500 word proposal'
- sources:
  - [1] https://mercatus.tfaforms.net/5099527
  - [2] https://www.mercatus.org/emergent-ventures
  - [3] https://www.lesswrong.com/posts/7gd6HehTBa8my6wEj/apply-for-emergent-ventures
