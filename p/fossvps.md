# FOSSVPS

> fossvps.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fossvps/ | JSON https://fshy.ajam.dev/api/v1/entity/fossvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FOSSVPS / ST-Hosting — free VPS for open-source developers (Frankfurt, Buffalo, LA, Chisinau)

- `storage/fossvps-st-hosting-free-vps-for-open-source-developers` | fails-quota | evidence reported | binding none | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:38.677Z (live) | stale on 2026-12-04
- url https://fossvps.org/
- free tier: Free VPSs on donated hardware. The first-party site now lists per-VM specs of 2 vCPU, 4GiB RAM and 64GiB HDD, with donated nodes in Frankfurt (to 1 Feb 2028), Chisinau (to 30 Jan 2027), Bucharest (to 17 Oct 2026), Buffalo (to 22 Nov 2026 or 30 Jan 2027) and Los Angeles (to 21 Dec 2026). Per-VM disk is small; the infrastructure has published end dates. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Node-level 1 Gbps; per-VM transfer not published. Unverified. | metered: no
- identity: email | detail: email
- interface: sftp, rsync, ssh
- limits note: Per-VM disk is far below 500 GB. Node end-dates are published (Moldova to 2027-01-31, Buffalo to 2026-11-22, LA to 2026-12-21). The infrastructure has an expiry date.
- interface detail: sftp
- tooling: Root VPS. SSH/SFTP/rsync.
- reliability: Donated capacity with published sunset dates and a public status page. Structurally temporary even when the VM is free.
- notes: Free VPSs on donated hardware; the Frankfurt node is an AMD EPYC 7402P, 128 GiB RAM, 1 TB SSD donated by ST-Hosting for at least two years. Per-VM disk is small (the node is large, the slices are not).
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free VPSs on donated hardware; the Frankfurt node is an AMD EPYC 7402P, 128 GiB RAM, 1 TB SSD donated by ST-Hosting for at least two years. Per-VM disk is small (the node is large, the slices are not).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'an AMD EPYC 7402P 24-Core Processor with 128GiB RAM and 1TB SSD'; 'Free and open source software developers only … No excessive high cpu, disk or bandwidth'; node end dates to 2026/2027
  - [2] 2026-10-21: probe: GET -> HTTP 200
  - [2] 2026-11-19: the first-party site now publishes explicit per-VM specs of 2 vCPU, 4GiB RAM, 64GiB HDD | capture: sha256:0c5472e537615141f2ad1dfed2f45d884df491adbe7dfa1ef94523b2fed6cec2 | quote: VPS: 2VCPU, 4GiB Ram and 64GiB HDD
  - [2] 2026-11-19: the first-party site states per-VM capacities in GiB | capture: sha256:0c5472e537615141f2ad1dfed2f45d884df491adbe7dfa1ef94523b2fed6cec2 | quote: VPS: 2VCPU, 4GiB Ram and 64GiB HDD
  - [2] 2026-11-19: Frankfurt node's donated capacity end date is restated on the live first-party site | capture: sha256:0c5472e537615141f2ad1dfed2f45d884df491adbe7dfa1ef94523b2fed6cec2 | quote: DE Frankfurt (de11) courtesy of ST-Hosting till 1st Feb 2028
  - [2] 2026-11-19: the Chisinau node's published end date is unchanged | capture: sha256:0c5472e537615141f2ad1dfed2f45d884df491adbe7dfa1ef94523b2fed6cec2 | quote: Moldova Chisinau (mol1) courtesy of Alexhost till 30th January 2027
- sources:
  - [1] https://lowendspirit.com/discussion/10506/st-hosting-free-vps
  - [2] https://fossvps.org/
