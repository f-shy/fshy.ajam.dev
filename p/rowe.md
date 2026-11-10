# FreeMach

> rowe.sh | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rowe/ | JSON https://fshy.ajam.dev/api/v1/entity/rowe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FreeMach

- `compute/freemach-free` | fails-identity | evidence documented | binding write-gated | category VPS | tier community VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://freemach.rowe.sh/
- free tier: 'FreeMach™ is a community-powered project that provides free VPS hosting to qualifying applicants of the LowEndSpirit, HostedTalk, and LowEndTalk communities'. Current allocation: 'EU1 (AlphaVPS, Bulgaria): 10/10 VMs Allocated (0 slots free)' and 'US1 (VirMach, New York): 10/10 VMs Allocated (0 slots free)'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: '10/10 VMs Allocated (0 slots free)' on both hosts, so there is no free slot to allocate today
- retention: not published as a clock; the project states applicants are 'Expected to have a purpose in mind to use the service (no idlers)'
- egress: '1TB @ 1 Gbps' per VM, with '1 IPv4' | metered: yes | free allowance: 1 TB | source: [1]
- identity: institution | detail: no card, but a reputation gate: quoted 'Must be an active user of LowEndSpirit, HostedTalk, and/or LowEndTalk communities'; 'LES/HT/LET account must be at least 3 months old at time of application'; 'Must pass a FraudRecord check (Do not use a proxy to submit the application)'. The application is a Google Form.
- interface: ssh, rest
- limits:
  - volume-quota: 2 vCPU, 2 GB RAM, 25 GB SSD on EU1; 2 vCPU, 3 GB RAM, 120 GB HDD on US1 [1]
  - write-gated (binding): a forum account at least 3 months old, a FraudRecord check, and a human review of the application [1]
- binding note: Capacity is the first wall and reputation is the second: both hosts report 0 of 10 slots free, and the application requires a three-month-old forum account that passes a FraudRecord check.
- interface detail: a KVM virtual machine with root, one IPv4, on a host donated by AlphaVPS in Sofia or VirMach in New York
- tooling: any SSH client once allocated
- composes with: Nothing until a slot frees: both hosts are at 10 of 10.
- reliability: No reliability event observed. The project publishes a status link to a HetrixTools monitor.
- notes: A real project with real sponsors and a real specification, documented because it is the clearest illustration of why the free-VPS forum layer is not a route: every slot is full, and the door is a three-month-old forum account plus a fraud check. earlier readings already carries freevps.org and microlxc on the same reputation model. Nothing here is a defect in the project; it is simply not available to a person who is not already in that community.
- evidence note: The allocation count, the specification and the eligibility rules are quoted from the project's own page read. The page is small and the project is one person's, so this is documented about the offer and about the current full capacity.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 25
  - billing_model: free
  - term: not published
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge; the constraint is eligibility and capacity, not price
  - free_tier_kind: free-forever-with-quota
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 1 IPv4, 1 TB a month at 1 Gbps
  - network_out.static_ip: yes
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: no clock published; 'no idlers' is the stated policy
- evidence:
  - [1] 2026-10-24: quoted: 'EU1 (AlphaVPS, Bulgaria): 10/10 VMs Allocated (0 slots free)', 'US1 (VirMach, New York): 10/10 VMs Allocated (0 slots free)'; 'LES/HT/LET account must be at least 3 months old at time of application'; 'Must pass a FraudRecord check'; specs '2 vCPU', '2GB RAM', '25GB SSD', '1TB @ 1 Gbps', '1 IPv4'
- sources:
  - [1] https://freemach.rowe.sh/

## FreeMach — community free VPS (LES/HT/LET members, 3-month account age)

- `storage/freemach-community-free-vps` | fails-quota | evidence reported | binding none | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://freemach.rowe.sh/
- free tier: US1.KVM: 2 vCPU, 3 GB RAM, 120 GB HDD, 1 TB transfer. EU1.KVM: 2 vCPU, 2 GB, 25 GB SSD, 1 TB. Hosts are a VirMach Buffalo E3-1240v3 with 2x1TB HDD and an AlphaVPS Sofia dual-L5630. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 1 TB per VM at 1 Gbps. Metered and small. | metered: yes
- identity: email | detail: email
- interface: sftp, rsync, ssh
- limits note: 120 GB max disk per VM, 1 TB transfer. Currently 0 slots: 'EU1 (AlphaVPS, Bulgaria): 10/10 VMs Allocated (0 slots free) … US1 (VirMach, New York): 10/10 VMs Allocated (0 slots free)'.
- interface detail: sftp
- tooling: KVM root. SSH/SFTP/rsync.
- composes with: Hard-gated on community standing, not on payment: 'LES/HT/LET account must be at least 3 months old at time of application', 'Must pass a FraudRecord check (Do not use a proxy to submit the application)'. That check is a risk-scoring screen. A second account would need an aged forum identity and a clean risk-scoring record, which is the actual scarce resource.
- reliability: Sponsored capacity on other people's dedicated servers, 10 VMs per node. The risk-scoring screen means a closure follows the person across the low-end host ecosystem. That is the strongest usage-anomaly signal in the niche.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: US1.KVM: 2 vCPU, 3 GB RAM, 120 GB HDD, 1 TB transfer. EU1.KVM: 2 vCPU, 2 GB, 25 GB SSD, 1 TB. Hosts are a VirMach Buffalo E3-1240v3 with 2x1TB HDD and an AlphaVPS Sofia dual-L5630.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Must be an active user of LowEndSpirit, HostedTalk, and/or LowEndTalk … at least 3 months old'; 'Must pass a FraudRecord check (Do not use a proxy to submit the application)'; '10/10 VMs Allocated (0 slots free)' on both nodes. The check the page names is a risk-scoring screen.
- sources:
  - [1] https://freemach.rowe.sh/
