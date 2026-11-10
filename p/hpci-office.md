# Fugaku Trial

> hpci-office.jp | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hpci-office/ | JSON https://fshy.ajam.dev/api/v1/entity/hpci-office.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HPCI Shared Storage (Japan, RIKEN R-CCS + Univ. of Tokyo, Gfarm)

- `storage/hpci-shared-storage` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.hpci-office.jp/en/using_hpci/hardware_software_resource/2026/hpci_2026_st-1
- free tier: 500 TB initial allocation for new applicants; expandable to 1.5 PB. Total logical capacity 90.0 PB, replicated east/west hub. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free - it is a shared filesystem (Gfarm), not a metered object store. Transfer via scp/rsync/GridFTP-style tools. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rsync, rclone
- limits:
  - write-gated (binding): approval at submission [1]
- limits note: Requires an organisational representative's online approval at submission; project must specify a plan to remove data by project end. Annual/periodic calls; resource granted per project period, not perpetually.
- interface detail: posix
- tooling: Gfarm 2.8 filesystem; mounted space, standard POSIX tools (rsync/rclone local backend).
- composes with: A storage-only proposal: the 'Sharing Use' call exists precisely for projects that need shared space rather than compute time. Request 500 TB, then request gradual expansion to 1.5 PB based on usage.
- reliability: Enterprise DDN + Gfarm, cross-hub replication. Stable. The binding constraint is the organisational sign-off and the end-of-project deletion requirement.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Total Logical Size :90.0 PB'; 'HPCI Shared Storage (Sharing Use) Projects : 500 TB'; expansion '1.5 PB'
  - [2] 2026-10-21: 'For regular calls, the max limit is 1.5 PB of file space. For new application, the initial allocation is up to 500 TB.'
  - [3] 2026-10-21: 'The Project Representative must belong to a corporation (i.e., university, research institution, company), regardless of whether it is in or outside of Japan.'
  - [4] 2026-10-21: call doc v2.0 updated 2026-10-01
- sources:
  - [1] https://www.hpci-office.jp/en/using_hpci/hardware_software_resource/2026/hpci_2026_st-1
  - [2] https://www.hpci-office.jp/application/files/7717/8839/3664/r08_boshu_hpci_resource_e.pdf
  - [3] https://www.hpci-office.jp/en/using_hpci/beginner/beginner_eligibility
  - [4] https://www.hpci-office.jp/en/using_hpci/proposal_submission_current/shared_storage

## Fugaku Trial Access

- `compute/fugaku-trial-access` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.hpci-office.jp/en/using_hpci/proposal_submission_current/fugaku_trial
- free tier: Trial Access Projects on Fugaku award up to 100,000 node-hours per project, free of charge, with the call open throughout the year, a project period of up to half a year, and screening results notified within one to two weeks; a First-touch option fixes 1,000 node-hours per project for a simplified application. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / trial allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The project representative must obtain approval from the head of their organisation and must belong to a legal entity, so an individual with no organisation cannot lead the project even though the call is free and open all year. [1]
- limits note: The project representative must obtain approval from the head of their organisation and must belong to a legal entity, so an individual with no organisation cannot lead the project even though the call is free and open all year.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 1,000 NH first-touch tier needs only an online form and eligibility check, so it is the cheapest way to obtain a Fugaku scaling number that a later full proposal can cite.
- reliability: no reliability event recorded
- notes: The strongest single number in evaluated benchmarks: 100,000 Fugaku node-hours free, open all year, no competitive expert review at the trial tier. Fugaku nodes carry one A64FX CPU with 48 compute cores plus 4 assistant cores, so 100,000 node-hours is roughly 4.8 million core-hours; that conversion is arithmetic from the published node design, not a quoted figure. The binding door is the organisational signature, not money and not the science case. Foreign non-resident participants are explicitly allowed but require separate R-CCS approval under the Foreign Exchange and Foreign Trade Act.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / trial allocation
- evidence:
  - [1] 2026-10-22: Available Resources per project 'Up to 100,000 Node-Hours'; First-touch option '1,000 Node-Hours per project (fixed)'; usage fee 'None'; project period up to half a year; call opens throughout the year, quoted
  - [1] 2026-10-22: 'Awarding result will be notified as soon as the screening process is completed. (Estimated to be within one or two weeks after a proposal is received.)', quoted
  - [2] 2026-10-22: Trial Access screening method is 'Online application content confirmation and eligibility screening' for first-touch and 'Review of the application form and eligibility screening' for the 100,000 NH tier, against 'Expert screening' for General Access, quoted
  - [3] 2026-10-22: Proposal instructions section 2: the general-category project representative is 'a person belonging to a legal entity (university, research institute, incorporated association, company, etc.) regardless of whether inside or outside Japan', except that company employees must belong to a company registered in Japan, quoted in Japanese
  - [4] 2026-10-22: FAQ: use by non-residents of Japan and by non-Japanese nationals 'is possible'; a non-resident may be project representative; for Fugaku, projects with non-resident participants need separate R-CCS approval, quoted in Japanese
- sources:
  - [1] https://www.hpci-office.jp/en/using_hpci/proposal_submission_current/fugaku_trial
  - [2] https://www.hpci-office.jp/en/using_hpci/beginner/beginner_calls
  - [3] https://www.riken.jp/medialibrary/riken/collab/programs/fugaku_trial_boshu_youryo_j.pdf
  - [4] https://www.hpci-office.jp/faq_list
