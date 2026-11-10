# Thiel Fellowship

> thielfellowship.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thielfellowship/ | JSON https://fshy.ajam.dev/api/v1/entity/thielfellowship.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Thiel Fellowship

- `compute/thiel-fellowship` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://thielfellowship.org/
- free tier: 'The Thiel Fellowship gives $250,000 to young people who want to build new things instead of sitting in a classroom.' The shape, quoted: 'Two years. $250,000. Some ideas can't wait.' and 'Thiel Fellows skip or stop out of college to receive a $250,000 grant and support from the Thiel Foundation's network of founders, investors, and scientists.' No entity is required: the award is to a person, and the page's own terms of trade are quoted as 'How you spend your two years in the Fellowship is up to you'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): an age and enrolment condition decides it before any project does: the fellowship is for people young enough to 'skip or stop out of college', which excludes anyone past that stage regardless of what they can build. [1]
- limits note: an age and enrolment condition decides it before any project does: the fellowship is for people young enough to 'skip or stop out of college', which excludes anyone past that stage regardless of what they can build.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cash with no stated spending restriction, so at Lambda's documented on-demand rate of USD 3.99 per H100 GPU-hour (compute/lambda) USD 250,000 is about 62,500 H100-hours across two years. It composes with every compute record in documented records for the same reason the Eigenprize does, and it is the only award in this category denominated in years rather than weeks.
- reliability: no reliability event recorded
- notes: The age and enrolment condition is inferred from the page's own framing ('young people', 'skip or stop out of college') rather than from a quoted rule, because the site publishes no eligibility section on the landing page read. That is the gap in this record: the number is documented and the gate is inferred, so a reader should treat the age limit as likely rather than established. The programme is a grant, not compute, and is recorded because names it.
- extras:
  - facets.class: grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'The Thiel Fellowship gives $250,000 to young people who want to build new things instead of sitting in a classroom'; 'Two years. $250,000.'; 'Thiel Fellows skip or stop out of college to receive a $250,000 grant and support from the Thiel Foundation's network of founders, investors, and scientists'; 'How you spend your two years in the Fellowship is up to you'; page 200
- sources:
  - [1] https://thielfellowship.org/
