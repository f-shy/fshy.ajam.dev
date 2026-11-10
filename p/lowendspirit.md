# kts24

> lowendspirit.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lowendspirit/ | JSON https://fshy.ajam.dev/api/v1/entity/lowendspirit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FOSSVPS

- `compute/fossvps` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://lowendspirit.com/discussion/10909/welcome-to-fossvps-and-goodbye-to-nodeseek
- free tier: FOSSVPS is a free 2 vCPU / 4 GiB / 64 GiB VPS gated on a human review of the applicant's open-source work. The provider's own forum posts show a second gate: forum reputation on named boards, with entire communities excluded. 'Nodeseek is no longer an accepted forum for potential new clients. Clients with good non spammy reputations are only accepted from LET or LES. Registration via a VPN is blocked. Throw away email addresses are blocked. Registering from Russia, China or North Korea is blocked.' And on the abuse that caused it: '29th of May VPS's belonging to NodeSeek clients will be terminated with no records kept.' | unit: GiB | metered on: wall-clock | read on: 2026-05-27 | source: [1] | note: sponsored-per-node
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The gate is a reputation held on one of two named forums plus a country the operator will accept, so an applicant with no LET or LES history and a blocked country cannot enter at all, whatever their open-source work. [1]
- limits note: The gate is a reputation held on one of two named forums plus a country the operator will accept, so an applicant with no LET or LES history and a blocked country cannot enter at all, whatever their open-source work.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The per-node sponsor dates are the composition rule: a box on buc2 expired 2026-10-17 and a rebuild to another node destroys the data, so this is a place to run a workload and not a place to keep state.
- reliability: no reliability event recorded
- notes: FOSSVPS provides donated VPS resources to eligible open-source projects.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: sponsored-per-node
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 64
- evidence:
  - [1] 2026-05-27: quoted exclusions: NodeSeek clients terminated with no records kept; only LET or LES reputations accepted; VPN registration blocked; throwaway emails blocked; registration from Russia, China or North Korea blocked
  - [2] 2026-10-22: quoted in full: 2 vCPU, 4 GiB RAM, 64 GiB HDD, dual-stack NAT plus IPv6 /128 or /96, IPv4 very limited, and six locations with named sponsors and end dates ranging from 17th October 2026 to 1st February 2028
  - [2] 2026-10-22: 'VPS: 2VCPU, 4GiB Ram and 64GiB HDD', 'Dual stack NAT + IPv6 /128 or /96 Location dependent', 'IPv4 very limited', 'OS: Debian, Ubuntu and Alpine', quoted, with six locations and end dates from 2026-12-21 to 2028-02-01
  - [3] 2026-10-22: 'Absolutely FREE, no catches, no credits, no price bumps'; 'Free and open source software developers only'; 'Good reputation on this forum (no history, no server - sorry)'; 'Multiple registrations will get you banned'; 'Acceptance will give you 2 VCPU, 4GiB Ram, 64GiB disk with NAT + IPv6 /96', quoted
  - [4] 2026-10-22: quoted: 'node buc1 will terminate on 17th of April 2026 ... all data WILL BE DESTROYED'
  - [5] 2026-10-22: 
  - [6] 2026-10-22: 
  - [7] 2026-10-22: 
- sources:
  - [1] https://lowendspirit.com/discussion/10909/welcome-to-fossvps-and-goodbye-to-nodeseek
  - [2] https://fossvps.org/
  - [3] https://lowendtalk.com/discussion/215848/fossvps-updates-free-server-for-open-source-developers-from-alexhost-hosteroid-and-st-hosting
  - [4] https://lowendspirit.com/discussion/10570/important-buc1-hosteroid-server-termination
  - [5] https://lowendtalk.com/discussion/217109/fossvps-mol1-server-currently-correctly-suspended-by-alexhost
  - [6] https://lowendtalk.com/discussion/212694/free-vps-for-open-source-developers
  - [7] https://lowendtalk.com/discussion/214669/important-buc1-hosteroid-server-termination

## scaleway perpetual 75 gb free object storage

- `storage/scaleway-perpetual-75-gb-free-object-storage` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:23.416Z (live) | stale on 2026-11-18
- url https://lowendspirit.com/discussion/6958/scaleway-the-end-of-the-free-75gb-free-tier
- free tier: none reachable: Removed December 2023; only the 75 GB/month free egress survived. The replacement is a one-shot 750 GB / 90-day trial. A free-for-dev PR was merged removing Scaleway for exactly this reason. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: 75GB of egress free every month, then EUR 0.01/GB; ingress and requests included. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: The 2026-11-03 evidence row reads https://www.scaleway.com/en/pricing/storage/ for Object Storage egress (75GB free every month, then EUR 0.01/GB). The removal of the free storage tier is cited only to a forum thread, not a vendor capture, so the rung stays reported.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Removed December 2023; only the 75 GB/month free egress survived. The replacement is a one-shot 750 GB / 90-day trial. A free-for-dev PR was merged removing Scaleway for exactly this reason.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Removed December 2023; only the 75 GB/month free egress survived. The replacement is a one-shot 750 GB / 90-day trial. A free-for-dev PR was merged removing Scaleway for exactly this reason.
  - [2] 2026-11-03: Object Storage egress: 75GB free each month, then EUR 0.01/GB | capture: sha256:d3c55b4fc433a1cba9321d67b04ac0adfc1f943bd05919de38e33a8cf751a5a0 | quote: | Egress * | | 75GB free every month then €0.01/GB /MONTH |
- sources:
  - [1] https://lowendspirit.com/discussion/6958/scaleway-the-end-of-the-free-75gb-free-tier
  - [2] https://www.scaleway.com/en/pricing/storage/

## kts24 — 1 tb storage vps free for 3 months (ceph beta)

- `storage/kts24-1-tb-storage-vps-free-for-3-months` | dead | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T01:28:34.900Z (inherited) | stale on 2026-11-18
- url https://lowendspirit.com/discussion/3945/kts24-com-free-storage-vps-for-at-least-3-month
- free tier: 1000 GB storage on an unmanaged VPS with 1 vCore, 2 GB memory and 2 TB traffic per month, free of charge for at least 3 months; EUR 8.99 per month after the 3 months. A test offer posted in March 2022 in a discussion that is now closed | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: a March 2022 test offer in a LowEndSpirit thread that is now closed; trial servers expire at the end of the trial unless extended
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: the March 2022 test needed an account at the provider's panel and a request e-mail sent from the registered address; no card was asked for in the offer text. The offer is closed
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Promotional offer of 1 TB storage VPS free for 3 months with no card required dates to March 2022. The series was not launched publicly.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-03
  - death.cause: free-tier-removed
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: the provider's March 2022 post offers its ceph storage VPS free of charge for at least 3 months | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: currently we are testing our new ceph based storage vps series, but until know there are only a hand full active customers, I have therefore decided to give you the opportunity to test the service free of charge for at least 3 months.
  - [1] 2026-10-30: the free test VPS carries 1000 GB of storage | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: 1000 GB storage
  - [1] 2026-10-30: the provider's account states that trial servers expire after the trial unless extended | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: After the trial period ends, the servers will automatically expire if you do not wish to extend it.
  - [1] 2026-10-30: the offer thread is closed | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: This discussion has been closed.
  - [1] 2026-10-30: the VPS costs EUR 8.99 per month after the 3 free months | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: The price after the 3 months is 8,99 € / month.
  - [2] 2026-11-03: the provider discontinued the storage VPS project that carried the 1000 GB free test offer | capture: sha256:a94ef4af596f7c0af362e3fc9f712072d9589427f0010a6561a0bebedfff79d8 | quote: Unfortunately, this increases the costs so much that we would no longer be competitive in storage and will therefore discontinue the Storage VPS 2022 project.
  - [2] 2026-11-03: every server created for the beta was blocked by the provider | capture: sha256:a94ef4af596f7c0af362e3fc9f712072d9589427f0010a6561a0bebedfff79d8 | quote: All services that were created for the BETA test are blocked from now on.
  - [2] 2026-11-03: the provider states the storage VPS series is dead | capture: sha256:a94ef4af596f7c0af362e3fc9f712072d9589427f0010a6561a0bebedfff79d8 | quote: The "Storage" VPS Series wich was planned on our ceph storage is dead
  - [3] 2026-11-03: the provider's current VPS plan list tops out at 240 GB of storage | capture: sha256:be63be2f57507a019b010b21baab9e8a58cb8bbd575602cc2615125ba0699937
  - [1] 2026-11-03: the test offer needed an account at the provider's panel and a request mail from the registered address | capture: sha256:7bb56d222ddfcd24fb0fa6328d06760bffc838d2b32742553f2adbc39c4522d1 | quote: from the email address registered with us.
- sources:
  - [1] https://lowendspirit.com/discussion/3945/kts24-com-free-storage-vps-for-at-least-3-month
  - [2] https://www.lowendspirit.com/discussion/3965/kts24-com-free-storage-vps-test-terminated-prematurely
  - [3] https://www.kts24.com/vps
