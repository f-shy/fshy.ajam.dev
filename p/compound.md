# Compound Reverie Grants

> compound.vc | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/compound/ | JSON https://fshy.ajam.dev/api/v1/entity/compound.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Compound Reverie Grants

- `compute/compound-reverie-grants` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://compound.vc/grants
- free tier: 'These are micro-grants to fund people exploring ideas that otherwise would not easily get funded through traditional means ... They range from as little as $500 to as much as $7,500 each, in fully non-dilutive, no-strings-attached capital.' Eligibility is described as people at the edges rather than by credential: 'You shouldn't be starting a company (though it could lead you to one) but instead you should be working on research, building a prototype, writing, open-sourcing something, or tinkering on a strange project that resists easy explanation.' A second stated category is 'thoughtful people who are simply in transition'. The application is a five-field form on the page: 'Name', 'Email', 'Location', 'What are you working on?', 'Why would a grant help you right now?' and 'Is there anything else you want from Compound besides the grant?' There is no deadline and no institutional field. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: name, email and a self-declared location. No company, affiliation or credential is requested anywhere in the form, and the operator states the funds are for people who are deliberately not starting a company.
- interface: rest
- limits:
  - write-gated (binding): a discretionary review by one venture firm's partners fails first, and the USD 7,500 ceiling buys weeks of compute rather than a training run, so the amount caps the value before the odds do. [1]
- limits note: a discretionary review by one venture firm's partners fails first, and the USD 7,500 ceiling buys weeks of compute rather than a training run, so the amount caps the value before the odds do.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A small unconditional cash grant, so it composes as a first purchase rather than as capacity: USD 7,500 at marketplace GPU rates covers a multi-week fine-tune or a few thousand inference-heavy agent runs, and it can be spent wherever the price is lowest. It does not compose into a training run for a large model.
- reliability: no reliability event recorded
- notes: Included because it is the same shape at a smaller scale and because its terms are unusually explicit about what it is not: non-dilutive, no company, and a stated appetite for people between projects. That last property matters more than the amount, because a person with no affiliation and no current publication fits the 'simply in transition' category the operator names. The failure mode is size: the ceiling is USD 7,500 and the modal award is likely nearer the USD 500 floor, which the page's own range implies without stating a distribution. One structural caution: the granting entity is a venture firm, so the review may weigh commercial potential even where the page says not to; nothing on the page promises otherwise. Reachability is easy: a form on the page and a named email address, grants@compound.vc.
- extras:
  - facets.class: independent-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'They range from as little as $500 to as much as $7,500 each, in fully non-dilutive, no-strings-attached capital.'; 'You shouldn't be starting a company'; 'working on research, building a prototype, writing, open-sourcing something, or tinkering on a strange project that resists easy explanation'; 'Our hope is that this first wave of grants are only the beginning'; the form fields 'Name / Email / Location / What are you working on? / Why would a grant help you right now?'; quoted; page 200
  - [2] 2026-10-22: a third-party tracker records the programme as 'Funding amount $500 - $7,500', 'Deadline Rolling', 'Location Global', reported and consistent with the vendor page
  - [3] 2026-10-22: 
- sources:
  - [1] https://compound.vc/grants
  - [2] https://sologrants.com/guide/compound-reverie-grants
  - [3] https://www.linkedin.com/posts/michaelhdempsey_compound-reverie-grants-activity-7416568373750419456-rpQN
