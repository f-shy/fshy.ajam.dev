# RES

> res.es | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/res/ | JSON https://fshy.ajam.dev/api/v1/entity/res.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RES

- `compute/res` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.res.es/en/faq
- free tier: RES resources are free of charge through open competitive calls and open to all scientists working in open research within the European Union and associated states, with the principal investigator allowed to be from an institution in any of those countries; typical requests run between 50,000 and 2,000,000 hours, and fast access activities are evaluated weekly with no priority guarantee. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed national allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The PI must still be affiliated with an institution in an EU Member State or associated state, so the nationality test is the loosest found but the affiliation test is unchanged, and a Spanish team member is strongly recommended rather than required. [1]
- limits note: The PI must still be affiliated with an institution in an EU Member State or associated state, so the nationality test is the loosest found but the affiliation test is unchanged, and a Spanish team member is strongly recommended rather than required.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Fast access gives a weekly-reviewed foothold on the same machines that the six-month ordinary activity then uses, and the continuation activity after a completed ordinary activity is simplified, so the three form an internal ladder.
- reliability: no reliability event recorded
- notes: This is the most nationality-open allocation programme found in the whole assignment, and it is the one row a reconciler should prioritise: the PI may be from any EU or associated-state institution, not a Spanish one, and there is no minimum request size. It is still fails-identity because no European institutional affiliation is in place, and the distinction matters: RES fails on affiliation, not on nationality or on the science case. The hours are site-hours, not GPU-hours or core-hours, so no conversion is offered. Deadlines per the FAQ were HPC/AI/Quantum 15 September 2026, with fast access weekly.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-reviewed national allocation
  - facets.shape.gpu_class: partition-dependent (MareNostrum 5 H100/Acc, CSUC, CESGA)
- evidence:
  - [1] 2026-10-22: 'the RES resources are open to all scientists and technologists working in open research within the European Union and associated states. Therefore, the principal investigator of the team submitting the proposal can be from an institution in any of these countries', quoted
  - [2] 2026-10-22: 'It is strongly recommended that at least one member of the research team work in a Spanish research center'; 'The RES provides free access to supercomputing resources for open R&D through open competitive calls', quoted
  - [2] 2026-10-22: 'There is not a strict minimum or maximum limit of requested time. However, those activities requesting more than 10 million hours should provide a justification'; 'Typically, RES applicants request between 50.000 and 2.000.000 hours', quoted
  - [3] 2026-10-22: 'Fast access activities: These are activities designed for projects with low computational requirements that allow quick access to shared RES machine resources ... The evaluation of this type of proposal is carried out weekly', quoted
- sources:
  - [1] https://www.res.es/en/faq
  - [2] https://www.res.es/en
  - [3] https://www.res.es/en/services/access-and-calls
