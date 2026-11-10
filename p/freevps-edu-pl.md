# freevps.edu.pl

> freevps.edu.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freevps-edu-pl/ | JSON https://fshy.ajam.dev/api/v1/entity/freevps-edu-pl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freevps.edu.pl

- `compute/freevps-edu-pl` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://freevps.edu.pl/
- free tier: 'Free Windows VPS Hosting For Students & Developers', 'No Credit Card Instant Activation Student Verified', 'No credit card required - simply verify your student status to get started'. The earlier description added '4 dedicated Ryzen cores', '4GB DDR5 RAM' and 'no trial periods'; the read on 2026-10-22 did not reproduce those figures. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: no expiration is stated on the page | source: [1] | note: a machine record: what is lost is the running process
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: student status is verified before activation; the page states 'simply verify your student status' and does not describe the check
- interface: ssh
- limits:
  - write-gated (binding): student verification fails first: without a verifiable enrolment there is no activation, and the page does not describe which document it accepts [1]
- limits note: student verification fails first: without a verifiable enrolment there is no activation, and the page does not describe which document it accepts
- binding note: the same as limits note
- interface detail: full root access to a Linux VM; the access route is not otherwise stated
- tooling: a Linux VM with root access; no client is named on the page
- composes with: a Windows host composes with the free Linux lane for anything that needs a Windows-only tool, if the student gate can be met
- reliability: no reliability event recorded
- notes: Documented from live retrieval on 2026-10-22.
- extras:
  - facets.class: perpetual-vps
- evidence:
  - [1] 2026-10-22: 'Free Windows VPS Hosting For Students & Developers', 'No Credit Card Instant Activation Student Verified' and 'No credit card required - simply verify your student status to get started', quoted from the page read on 2026-10-22
- sources:
  - [1] https://freevps.edu.pl/
