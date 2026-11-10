# Chameleon Cloud

> chameleoncloud.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chameleoncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/chameleoncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chameleon Cloud

- `compute/chameleon-cloud` | fails-identity | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://chameleoncloud.org/learn/frequently-asked-questions/
- free tier: "Chameleon operates on a 'soft allocation model' where each project, if approved, receives a startup allocation of 20,000 SUs for six months. This allocation can be both recharged (more SUs added) and renewed (duration extended)"; "Users can expect a project decision within one business day". | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits note: no binding constraint identified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: no open question recorded
- evidence:
  - [1] 2026-10-22: startup allocation of 20,000 SUs for six months, rechargeable and renewable, decision within one business day, quoted
  - [2] 2026-10-22: "PI status is limited to faculty and research staff at US-based academic institutions", quoted
  - [2] 2026-10-22: Daypass "lets anyone request temporary access to system resources for the purpose of reproducing an experiment published on Trovi ... No allocation, no project membership, no approval from a PI required", quoted
  - [3] 2026-10-22: Daypass is for reproducing a published artefact, the request is reviewed by the artefact's project PI, and the suggested default reservation length is 6 hours, quoted
- sources:
  - [1] https://chameleoncloud.org/learn/frequently-asked-questions/
  - [2] https://blog.chameleoncloud.org/posts/tips-and-tricks-getting-access-to-chameleon-as-a-student/
  - [3] https://blog.chameleoncloud.org/posts/interactive-science-made-easy-with-chameleon-daypass/

## Chameleon Cloud (TACC / UChicago)

- `storage/chameleon-cloud` | fails-identity | evidence reported | binding none | category research testbed - free bare metal and storage nodes
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://chameleoncloud.org/
- free tier: 534 nodes across KVM@TACC, CHI@UC, CHI@TACC, CHI@NRP; 62 nodes with >1TB total storage, dedicated 'storage' (20) and 'storage_nvme' (10) node classes, plus 297 nodes at 400GB-1TB | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Accounts deactivate after 120 days' inactivity | days: 120 | source: [1] | note: not stated
- egress: free within allocation; no published byte meter | metered: no
- identity: institution | detail: institution
- interface: ssh, cli
- limits note: PI status is the binding constraint and is 'limited to faculty and research staff at US-based academic institutions'. International PIs are supported only as 'a limited number ... with ongoing, active collaborations with scientists in the US'. Students explicitly excluded except NSF GRFP holders. Accounts deactivate after 120 days' inactivity. FPGA resources additionally refuse residents or citizens of Iran, Iraq, North Korea, Sudan, Syria.
- interface detail: OpenStack API (Nova/Cinder/Blazar), CLI, Jupyter; ssh to instances
- tooling: python-chi, openstackclient, blazar reservations, Trovi artifacts, Daypass for artifact reproduction
- composes with: bare-metal reservation -> local NVMe -> object store you run yourself
- reliability: Project expiry immediately revokes all access and the allocation; storage is not offered as a durable service.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 534 nodes across KVM@TACC, CHI@UC, CHI@TACC, CHI@NRP; 62 nodes with >1TB total storage, dedicated 'storage' (20) and 'storage_nvme' (10) node classes, plus 297 nodes at 400GB-1TB
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'PI status is limited to faculty and research staff at US-based academic institutions'
  - [3] 2026-10-21: eligibility list: academic institutions (research staff/faculty in supervisory positions), federal agencies, 'a limited number of international PIs with ongoing, active collaborations with scientists in the US', NSF Graduate Student Fellows, US museums/libraries/labs, K-12 educators; 'We do occasionally provide case-by-case exceptions ... in well-justified cases'
  - [4] 2026-10-21: Deactivation after 120 days inactivity
  - [1] 2026-10-21: 534 nodes; 20 storage, 10 storage_nvme, 62 nodes >1TB; per-node inventory with r740xd/r630 chassis listed
- sources:
  - [1] https://chameleoncloud.org/hardware/
  - [2] https://blog.chameleoncloud.org/posts/tips-and-tricks-getting-access-to-chameleon-as-a-student/
  - [3] https://chameleoncloud.readthedocs.io/en/stable/user/pi_eligibility.html
  - [4] https://www.chameleoncloud.org/terms/
