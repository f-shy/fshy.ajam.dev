# CloudLab

> cloudlab.us | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudlab/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudLab

- `compute/cloudlab` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:03:39.492Z (live) | stale on 2026-12-26
- url https://docs.cloudlab.us/users.html
- free tier: Registering doesn’t cost anything, it’s simply for accountability. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: unmetered-bare-metal
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Creating a project requires being "faculty, senior research staff, or in some other senior position" and passes a staff review that takes a few days; joining one requires the leader's approval, so an unaffiliated person cannot obtain nodes on their own. [1]
- limits note: Creating a project requires being "faculty, senior research staff, or in some other senior position" and passes a staff review that takes a few days; joining one requires the leader's approval, so an unaffiliated person cannot obtain nodes on their own.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The absence of a quota is the unusual part and it is what makes CloudLab usable for a long-running measurement rather than a benchmark: a project can hold nodes for days provided the profile reserves them, which is the shape a network or storage experiment needs and which no credit-based programme provides.
- reliability: no reliability event recorded
- notes: Disk and RAM per node are not published on documentation pages and remain null.
- extras:
  - facets.class: open-science-grid
  - facets.free_tier_kind: unmetered-bare-metal
  - facets.shape.vcpu: 32
- evidence:
  - [1] 2026-10-22: "Registering doesn't cost anything, it's simply for accountability", quoted
  - [1] 2026-10-22: "We therefore require that project leaders be faculty, senior research staff, or others who are relatively senior positions"; "You should only start a new project if you are a faculty member, senior research staff, or in some other senior position", quoted
  - [1] 2026-10-22: a new project application "will be reviewed by our staff" and "The review process may take a few days", quoted
  - [2] 2026-10-22: Utah cluster is 9,336 cores; d6515 is 28 nodes of 32-core AMD 7452 with 100Gb Ethernet; c6525-100g is 36 nodes of 24-core AMD 7402P with 25/100Gb, quoted
  - [2] 2026-10-22: the four GPU-capable d750 nodes are "not available for general use. CloudLab staff will grant access to your project on request", quoted
  - [1] 2026-11-25: the page states that registering a CloudLab account costs nothing and is for accountability | capture: sha256:4b75dc46da8f15bff785bd88790fcf67311b0d61c7cd055d90e2754117ce49d0 | quote: Registering doesn’t cost anything, it’s simply for accountability.
  - [1] 2026-11-25: the page states registration is free for accountability and that heavier use must be explained to staff | capture: sha256:4b75dc46da8f15bff785bd88790fcf67311b0d61c7cd055d90e2754117ce49d0 | quote: Registering doesn’t cost anything, it’s simply for accountability. We just ask that if you’re going to use CloudLab for anything other than light use, you tell us a bit more about who you are and what you want to use CloudLab for.
- sources:
  - [1] https://docs.cloudlab.us/users.html
  - [2] https://docs.cloudlab.us/hardware.html

## CloudLab c240g1 / per-node local blockstore (40 TB)

- `storage/cloudlab-c240g1-per-node-local-blockstore` | fails-identity | evidence reported | binding none | category research testbed - free bare metal with local HDDs
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:00.041Z (live) | stale on 2026-12-04
- url https://docs.cloudlab.us/advanced-storage.html
- free tier: c240g1 node type = 12 x 3 TB HDDs (36 TB raw) on 5 nodes at Wisconsin; the storage table prices a 'per-node local blockstore' at 90GB-40TB, so a multi-TB blockstore is requestable by size in the profile and the system picks a node type | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Default experiment lifetime is 'a few hours'; extensions need a written justification reviewed by staff, indefinite needs the steering committee | source: [1] | note: not stated
- egress: free - nodes are on 10-25 Gb experiment fabric plus a 1-25 Gb control link to the internet; no byte meter of any kind | metered: no
- identity: institution | detail: institution
- interface: s3, webdav, scp, rsync, ssh
- limits:
  - write-gated: reviewed by staff, indefinite needs the steering committee [1]
- limits note: local datasets are ALWAYS ephemeral - node disks are re-imaged after every experiment use, and the manual is explicit that infrastructure is 'not a storage provider' and node disks are 'not configure[d] in any redundant way'. Default experiment lifetime is 'a few hours'; extensions need a written justification reviewed by staff, indefinite needs the steering committee. Usage is metered in node-hours, not bytes. The Emulab parent facility has BYTE-IDENTICAL terms and shares the account: 'Emulab is a public facility, available without charge to most researchers worldwide', but project leaders must still be 'faculty, senior research staff, or others who are relatively senior positions', and an Emulab login is accepted directly as a CloudLab login - so it is a second door onto the same hardware with the same institutional lock.
- interface detail: ssh (key-only) + root/sudo on real hardware; anything you install - S3, WebDAV, rsync, nginx
- tooling: geni-lib RSpec profiles, portal API token, terraform-provider-cloudlab, ssh/scp
- composes with: run rclone/S3/WebDAV server directly on the node; put Cloudflare in front of it and the fabric becomes the origin. This is the only path in the whole research where the origin has no provider and no byte bill.
- reliability: No redundancy on node disks by design; a single drive failure loses the blockstore, and the whole volume is destroyed at experiment termination.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: c240g1 node type = 12 x 3 TB HDDs (36 TB raw) on 5 nodes at Wisconsin; the storage table prices a 'per-node local blockstore' at 90GB-40TB, so a multi-TB blockstore is requestable by size in the profile and the system picks a node type
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: c240g1 = 5 nodes, Haswell 16 core, 128GB RAM, two 480GB SATA SSD + 'Twelve 3 TB HDDs donated by Seagate'; c240g2 = 3 nodes with four 3TB HDDs
  - [2] 2026-10-21: storage table: 'Per-node local blockstore | No [persistent] | 90GB to 40TB | 100-1000MB/sec | When up to 40TB is needed; specified by size in profile, system picks the node type'
  - [3] 2026-10-21: 'All experiments have an expiration time. By default, the expiration time is short (a few hours)' and longer extensions 'require the intervention of CloudLab staff'
  - [4] 2026-10-21: litmus test is intent to publish in scholarly venues
  - [5] 2026-10-21: the parent facility shares the account: 'Emulab is a public facility, available without charge to most researchers worldwide'
  - [6] 2026-10-21: 'We therefore require that project leaders be faculty, senior research staff, or others who are relatively senior positions'
  - [1] 2026-11-19: the c240g1 storage configuration is unchanged at twelve 3 TB HDDs | capture: sha256:e4818c8b8988125ee6d85583fd35c0196ed5207d755f99fd761fedb6b1068798 | quote: Twelve 3 TB HDDs donated by Seagate
  - [2] 2026-11-19: the per-node local blockstore still ranges up to 40TB and is non-persistent | capture: sha256:db2b384396fab7ae669a6223a97dbc36a3eb6a905d21c81105f2bd3f4a33db32 | quote: Per-node local blockstore | | No | | No | | 90GB to 40TB | | 100-1000MB/sec | | When up to 40TB is needed
  - [3] 2026-11-19: the default experiment lifetime remains a few hours | capture: sha256:e2d3d10fedf0785e6534b766741f872e2b050d2e9cd60f83c3d6505bbccbe7be | quote: All experiments have an expiration time. By default, the expiration time is short (a few hours)
- sources:
  - [1] https://docs.cloudlab.us/hardware.html
  - [2] https://docs.cloudlab.us/advanced-storage.html
  - [3] https://docs.cloudlab.us/basic-concepts.html
  - [4] https://www.cloudlab.us/aup.php
  - [5] https://docs.emulab.net/
  - [6] https://docs.emulab.net/users.html

## CloudLab persistent remote dataset (10 TB, iSCSI)

- `storage/cloudlab-persistent-remote-dataset` | fails-identity | evidence reported | binding none | category research testbed - persistent block storage
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:00.041Z (live) | stale on 2026-12-04
- url https://docs.cloudlab.us/advanced-storage.html
- free tier: up to 10 TB per persistent remote dataset; pool is 500 TB at Utah, 160 TB at Wisconsin, 40 TB at Clemson. Anything over 1 TB 'likely to require administrative approval'; long-term datasets are 'subject to per-project quotas for total size and might require interaction with CloudLab staff' | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 TB hard ceiling per | bytes: 10000000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free; mounted as /dev/sdb via iSCSI on the experiment network, 50-200 MB/s | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits:
  - write-gated: approval' [1]
  - per-object-cap: 10 TB hard ceiling per [1]
- limits note: 10 TB hard ceiling per dataset, so 20 TiB needs two datasets and two projects' worth of quota. >1 TB needs a human to approve. Simultaneous read-write sharing across nodes 'will almost certainly wind up with a corrupted dataset'. No off-site backup; RAID/ZFS on the storage server only.
- interface detail: block device -> any filesystem -> any server you run on the node
- tooling: portal 'Create Dataset' UI, RemoteBlockstore in RSpec, rwclone/readonly mapping for multi-node
- composes with: persistent dataset + one node running S3/WebDAV + Cloudflare in front = 10 TB of genuinely durable-by-dint-of-not-being-wiped storage at $0
- reliability: Storage servers have RAID/ZFS but 'most clusters do not have off-site backup of user data'; a project expiry deletes the allocation.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: up to 10 TB per persistent remote dataset; pool is 500 TB at Utah, 160 TB at Wisconsin, 40 TB at Clemson. Anything over 1 TB 'likely to require administrative approval'; long-term datasets are 'subject to per-project quotas for total size and might require interaction with CloudLab staff'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'Persistent remote datasets ... Capacity: up to 10TB'; 'sizes in excess of 1TB are likely to require administrative approval'; 'long-term datasets ... subject to per-project quotas for total size and might require interaction with CloudLab staff'
  - [1] 2026-10-21: 'The Utah Cloudlab cluster includes a storage server for remote datasets. The server currently has 500TB available for allocation'; Wisconsin 160TB; Clemson 40TB
  - [2] 2026-11-19: the persistent remote dataset ceiling is still up to 10TB | capture: sha256:db2b384396fab7ae669a6223a97dbc36a3eb6a905d21c81105f2bd3f4a33db32 | quote: Persistent remote datasets | | Yes | | Yes, all nodes can read-write share | | up to 10TB | | 50-200MB/sec
  - [2] 2026-11-19: sizes above 1TB still require administrative approval | capture: sha256:db2b384396fab7ae669a6223a97dbc36a3eb6a905d21c81105f2bd3f4a33db32 | quote: Pick a Size, keeping in mind that sizes in excess of 1TB are likely to require administrative approval.
  - [1] 2026-11-19: the Utah remote-dataset pool is still 500TB | capture: sha256:e4818c8b8988125ee6d85583fd35c0196ed5207d755f99fd761fedb6b1068798 | quote: The Utah Cloudlab cluster includes a storage server for remote datasets. The server currently has 500TB available for allocation.
- sources:
  - [1] https://docs.cloudlab.us/hardware.html
  - [2] https://docs.cloudlab.us/advanced-storage.html
