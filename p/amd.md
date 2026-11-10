# AMD Developer

> amd.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amd/ | JSON https://fshy.ajam.dev/api/v1/entity/amd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AMD Developer Cloud

- `compute/amd-developer-cloud` | trial-only | evidence documented | binding retention-clamped | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T19:39:36.653Z (live) | stale on 2026-12-07
- url https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html
- free tier: 25 hours of complimentary cloud credit, stated as approximately USD 50: 'AMD is offering an initial 25 hours of complimentary cloud credit to qualified developers who apply and are accepted.' The credit is valid for 10 days from deposit, covers AMD Instinct MI300X GPUs only, and excludes attached volumes, object storage and backups. A card is required at account creation. | unit: hours | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: Two destruction triggers and one that bills silently: expiry or exhaustion destroys the VM and its data, while a powered-off instance keeps consuming credit until it is destroyed, so stopping the machine does not stop the meter. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: a valid credit card is required at the time of account creation and is required to access any complimentary cloud hours; the application is reviewed by AMD, and an expired or invalid card forfeits access to the GPUs and the data on them. AMD publishes no hold amount and no prepaid or virtual card rule: the card is entered on the hosting platform, which the vendor names as a third-party cloud with DigitalOcean support, and that platform's billing documentation sets the hold and the card types.
- interface: unknown
- limits:
  - retention-clamped (binding): Two destruction triggers and one that bills silently: expiry or exhaustion destroys the VM and its data, while a powered-off instance keeps consuming credit until it is destroyed, so stopping the machine does not stop the meter. [1]
- limits note: Two destruction triggers and one that bills silently: expiry or exhaustion destroys the VM and its data, while a powered-off instance keeps consuming credit until it is destroyed, so stopping the machine does not stop the meter.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Twenty-five hours on one MI300X with 192 GB of VRAM is a real fine-tuning window, and it composes with nothing that needs to persist, because the VM and its disk are destroyed at the end of the credit.
- reliability: no reliability event recorded
- notes: Two clauses decide how a run has to be built. First, a powered-off instance still consumes credit, so the correct discipline is to destroy and not to stop, and a reader who stops a machine to save credit loses the credit anyway. Second, expiry destroys the data, so every artefact has to be copied out before the clock ends. The allocation is also discretionary, and the larger public grant is restricted to Indian researchers and startups, which is a country gate on the 100,000-hour figure. As of 2026-10-23 the page states 25 hours and 10 days; the earlier USD 100 over 30 days figure is wrong on both the amount and the window.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: MI300X
  - facets.shape.gpu_count: 1
  - payment_methods.card_at_signup: yes
  - payment_methods.debit: accepted on the hosting platform
  - payment_methods.prepaid: refused on the hosting platform
  - payment_methods.virtual: refused on the hosting platform
  - payment_methods.hold_amount: usually USD 1 on the hosting platform; not published by AMD
  - payment_methods.hold_detail: AMD publishes no hold amount and no card-type rule. The card is entered on the hosting platform, which the vendor names as a third-party cloud with DigitalOcean support; that platform's billing documentation states a preauthorization request that 'may appear on your statement for up to 7 days, but you are not being charged and no funds are being transferred', priced on its pricing page as 'typically $1 but can vary in range', and that a card 'is only charged at the end of the billing cycle or upon exceeding a usage threshold'. The same documentation states 'We do not accept virtual, electron, or prepaid cards.'
  - payment_methods.identity: a valid credit card at account creation and to reach the complimentary hours; the application is reviewed by AMD
  - payment_methods.source_url: https://docs.digitalocean.com/platform/billing/manage-payment-methods/
  - payment_methods.read_on: 2026-11-02
- evidence:
  - [1] 2026-10-22: quoted: 'your AMD GPU VM will be destroyed and you will lose access to the GPU(s) and the data on the GPU(s)'; 'If a GPU Instance is powered off, you are still billed and/or credit hours will apply. Charges are incurred until the instance is destroyed.'
  - [1] 2026-10-22: quoted: 'Complimentary credit hours expire thirty (30) days from the date of deposit'; 'Complimentary AMD cloud credit applies only to use on AMD Instinct MI300X GPUs'; volumes, object storage and backups are not covered
  - [1] 2026-10-22: allocation is discretionary: 'Cloud credit allocation on the AMD Developer Cloud is determined by AMD in its sole discretion, based on the intended use case'
  - [2] 2026-10-22: 'an initial 25 hours of complimentary cloud credit to qualified developers who apply and are accepted'; 'approximately $50 US worth of cloud credit'; 'Complimentary credit hours expire ten (10) days from the date of deposit'; 'A valid credit card is required at the time of account creation'; 'If a GPU Instance is powered off, you are still billed and/or credit hours will apply'; quoted; page 200
  - [2] 2026-10-22: 'The AMD Developer Cloud is intended for independent developers and open-source project contributors involved with ML, low-level programming, and AI applications development', quoted; no institution or degree condition appears
  - [3] 2026-10-22: member benefit: 'Receive $100 in AMD Developer Cloud credits', quoted; program signup requires only an account
  - [4] 2026-10-22: '$100 in free credits, which is enough for approximately 50 hours of usage', quoted; additional credits may be applied for by members who publicly share projects
  - [1] 2026-10-22: complimentary credit hours expire thirty days from the date of deposit unless stated otherwise, quoted; access is delivered through a third-party cloud platform that AMD may change
  - [5] 2026-10-22: 
  - [6] 2026-10-22: 
  - [2] 2026-10-23: 'AMD is offering an initial 25 hours of complimentary cloud credit to qualified developers who apply and are accepted.', quoted; the same page states the 10-day validity and the storage exclusions
  - [7] 2026-11-02: the hosting platform verifies a card with a preauthorization hold that is not a charge and clears within 7 days | capture: sha256:c34e80402ea8c7fe187d835b3d0c56bfe8730dbead020176d1f5dedb019348b4 | quote: These temporary preauthorization holds may appear on your statement for up to 7 days, but you are not being charged and no funds are being transferred from your card or account to DigitalOcean.
  - [2] 2026-11-02: a valid credit card is required at account creation and to reach the complimentary hours | capture: sha256:3c7af598526ee9947bc3c1351e676a566622353ea730e133bb5319199e1dc648 | quote: A valid credit card is required at the time of account creation and is required to access any complimentary cloud hours offered by AMD.
  - [1] 2026-11-02: the offer runs on a third-party cloud, which is where the card is entered | capture: sha256:27cc40d73c6e8bee06fb3248c94557a543fa0be622930be463369a774a1955d7 | quote: The AMD Developer Cloud is hosted by a third-party cloud provider.
  - [8] 2026-11-02: the third-party cloud is DigitalOcean | capture: sha256:3074b025f3e18cde7c421a04306829c381fd25698de6ceee6226d7867c954e75 | quote: AMD Developer Cloud gives developers direct access to AMD GPU acceleration built on DigitalOcean infrastructure.
  - [7] 2026-11-02: the hosting platform refuses virtual, electron and prepaid cards | capture: sha256:c34e80402ea8c7fe187d835b3d0c56bfe8730dbead020176d1f5dedb019348b4 | quote: We do not accept virtual, electron, or prepaid cards.
  - [9] 2026-11-02: the platform prices the preauthorization at typically USD 1 | capture: sha256:f2b3f86b937e96e95de8fc39c8a57c01ca717cfa2502a9b24125c3abb18e08a0 | quote: These temporary pre-authorizations are typically $1 but can vary in range and are immediately canceled by us.
  - [2] 2026-11-02: the card requirement at account creation is unchanged | capture: sha256:3c7af598526ee9947bc3c1351e676a566622353ea730e133bb5319199e1dc648 | quote: A valid credit card is required at the time of account creation and is required to access any complimentary cloud hours offered by AMD.
  - [2] 2026-11-06: a powered-off instance keeps consuming credit until it is destroyed | capture: sha256:3c7af598526ee9947bc3c1351e676a566622353ea730e133bb5319199e1dc648 | quote: If a GPU Instance is powered off, you are still billed and/or credit hours will apply. Charges are incurred until the instance is destroyed.
- sources:
  - [1] https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html
  - [2] https://www.amd.com/en/developer/resources/cloud-access.html
  - [3] https://developer.amd.com/ai-developer-program/
  - [4] https://www.amd.com/en/developer/resources/technical-articles/2026/openclaw-with-vllm-running-for-free-on-amd-developer-cloud-.html
  - [5] https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-claim-amd-cloud-credits.html
  - [6] https://www.amd.com/en/blogs/2025/100k-hours-free-developer-cloud-access.html
  - [7] https://docs.digitalocean.com/platform/billing/manage-payment-methods/
  - [8] https://docs.digitalocean.com/products/amd/details/credits/
  - [9] https://www.digitalocean.com/pricing

## AMD University Program

- `compute/amd-university-program` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:49.063Z (live) | stale on 2026-12-04
- url https://www.amd.com/en/corporate/university-program/ai-hpc-cluster.html
- free tier: Node-hour allocations on a cluster of dual EPYC hosts with Instinct accelerators, awarded quarterly by proposal, reachable over SSH at hpcfund.amd.com with Slurm. The vendor states: 'Node-hour based allocations are awarded quarterly to proposal submissions supporting innovative, impactful, open-source AI and HPC research', and 'Successful proposals receive cluster access for up to one year'. The enrollment page closes the loop: 'Membership is open exclusively to faculty and researchers at universities and research institutions worldwide. Enroll using your official academic email address - personal emails won't qualify.' | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: No card, hold, debit or prepaid term is stated on the pages read.
- interface: ssh
- limits:
  - write-gated (binding): the AMD University Program enrolls only faculty and researchers at institutions, on an official academic email, and personal addresses are refused, so the quarterly proposal review is never reached. [1]
- limits note: the AMD University Program enrolls only faculty and researchers at institutions, on an official academic email, and personal addresses are refused, so the quarterly proposal review is never reached.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. The sibling AMD Developer Cloud lane, recorded separately, is the only AMD route with no institution gate, and it is 25 hours rather than a node-year.
- reliability: no reliability event recorded
- notes: Classified as the academic half of AMD's program so the next reader does not confuse it with the 25-hour developer credit, which is a different door on a different site with a different amount. The institution condition is stated three times across three AMD pages, including the enrollment rule that personal email addresses will not qualify, which is the clearest statement of the gate found in this class. A fourth page states the cluster is reviewed by an internal team at the end of each quarter and requires an annual survey and publication notification. Worth noting for completeness: the cluster is reachable over SSH and runs Slurm, so the constraint is purely the door, not the tooling.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: AMD Instinct (MI300X generation on the sibling developer cloud)
- evidence:
  - [1] 2026-10-22: 'Node-hour based allocations are awarded quarterly to proposal submissions supporting innovative, impactful, open-source AI and HPC research or educational initiatives'; 'Successful proposals receive cluster access for up to one year'; quoted; page 200
  - [2] 2026-10-22: 'An AMD internal cross-functional team reviews applications at the end of each quarter', quoted
  - [3] 2026-10-22: 'Membership is open exclusively to faculty and researchers at universities and research institutions worldwide. Enroll using your official academic email address - personal emails won't qualify.', quoted
  - [4] 2026-10-22: no instance was probed and no credential…
  - [1] 2026-11-03: the cluster allocation is node-hours awarded quarterly by proposal; the page lists no price per GPU-hour and none of H100, A100, L40S, RTX 4090 or L4 | capture: sha256:70b8df32cea361138fdbd319d815990bc0c1ad680d9c33ab8b2a688d45a20069 | quote: Node-hour based allocations are awarded quarterly to proposal submissions supporting innovative, impactful, open-source AI and HPC research or educational initiatives.
- sources:
  - [1] https://www.amd.com/en/corporate/university-program/ai-hpc-cluster.html
  - [2] https://www.amd.com/en/developer/resources/cloud-access.html
  - [3] https://www.amd.com/en/corporate/university-program/enroll.html
  - [4] https://amdresearch.github.io/hpcfund/access.html
