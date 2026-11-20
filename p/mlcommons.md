# MLPerf

> mlcommons.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mlcommons/ | JSON https://fshy.ajam.dev/api/v1/entity/mlcommons.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MLPerf

- `compute/mlperf` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://mlcommons.org/benchmarks/
- free tier: MLPerf awards no compute at all. The programme is a measurement, and the submitter supplies the system, quoted: 'The working group defines the AI model to run, the data set against which it gets run, sets rules on what changes to the model are allowed, and measures how fast a given hardware runs the model.' The gate is membership, quoted: 'Membership is required for most benchmark working groups (e.g., Training, Inference, Mobile). There are some public benchmark working groups that have no access requirements where non-members may submit to the benchmark by first signing a Non-member Test Agreement.' The submission requirements list, quoted: 'Join an appropriate MLCommons Working Group', 'A signed Contributor License Agreement', 'Membership in MLCommons OR a signed Non-member Test Agreement', 'A signed trademark license agreement'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): two gates stack: the Training and Inference working groups require organisational membership, and even a non-member submission needs a signed test agreement and a trademark licence before a result can be published, so the constraint that fails first is the membership, not the hardware. [1]
- limits note: two gates stack: the Training and Inference working groups require organisational membership, and even a non-member submission needs a signed test agreement and a trademark licence before a result can be published, so the constraint that fails first is the membership, not the hardware.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nil. The useful product of the record is the exclusion: a reader who sees MLPerf results quoted as free capacity should be told that the numbers are vendor submissions, and that no MLCommons programme pays for the machine under test.
- reliability: no reliability event recorded
- notes: MLPerf is not a compute-awarding programme. The membership sentence could mean that an individual can join, that a company pays dues, or that non-members are fine through the test agreement. The page's own 'Membership and Affiliate' FAQ and the phrase 'if you do not think your organization would be a good fit as a Member' in the GitHub route point at the company-dues reading, and the test-agreement reading is true but ends in a signed agreement that a solo entrant can sign. So the honest verdict is fails-identity for the main suites and a narrow non-member path for the public groups; the hardware cost stands either way.
- extras:
  - facets.class: benchmark-programme
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'Membership is required for most benchmark working groups (e.g., Training, Inference, Mobile)'; 'There are some public benchmark working groups that have no access requirements where non-members may submit to the benchmark by first signing a Non-member Test Agreement'; 'Membership in MLCommons OR a signed Non-member Test Agreement'; 'A signed trademark license agreement'; page 200
  - [2] 2026-10-22: the suite page describes measurement only ('measures how fast systems can process inputs and produce results') and names no grant, credit, allowance or hardware pool; page 200
  - [3] 2026-10-22: the policies page offers three agreements, 'Membership Agreement', 'Membership and Affiliate FAQ', 'Non-member Test Agreement', which is the only route for an unaffiliated submitter; page 200
- sources:
  - [1] https://mlcommons.org/benchmarks/
  - [2] https://mlcommons.org/benchmarks/inference-datacenter/
  - [3] https://mlcommons.org/about-us/policies/
