# Intel

> intel.com | Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/intel/ | JSON https://fshy.ajam.dev/api/v1/entity/intel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Intel Tiber Developer

- `compute/intel-tiber-developer` | trial-only | evidence documented | binding retention-clamped | category dev environment
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-04T05:24:16.614Z (live) | stale on 2026-12-05
- url https://devcloud.intel.com/oneapi/home/
- free tier: Free sandbox for oneAPI work: 120 days of access with extensions available, 192 GB RAM, 220 GB of file storage, remote desktop for the oneAPI Rendering Toolkit, VS Code integration and a Linux terminal, across Intel Xeon Scalable CPUs, Intel Iris Xe MAX GPUs and Stratix 10 / Arria 10 FPGAs. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: time-boxed-access
- per-object cap: not applicable | source: [1]
- retention: the account expires after 120 days and the hardware is pre-production or retired silicon, so the access is a portability test rather than a machine to hold a workload on; the separate Intel Developer Cloud console lane has no free instances at all. | source: [1]
- egress: not published: no egress allowance or overage price on https://devcloud.intel.com/oneapi/home/ | metered: no | source: [1]
- identity: email | detail: no payment is taken for the JupyterHub batch lane: Intel staff state 'there are currently no free instances available for the Standard tier in the Intel Developer Cloud Console' while JupyterHub batch instances remain accessible without payment. The account form's fields are not described in any evidence row, so whether an email, phone number or ID document is required is unknown, and no card requirement or hold is stated: unknown.
- interface: ssh
- limits:
  - retention-clamped (binding): the account expires after 120 days and the hardware is pre-production or retired silicon, so the access is a portability test rather than a machine to hold a workload on; the separate Intel Developer Cloud console lane has no free instances at all. [1]
- limits note: the account expires after 120 days and the hardware is pre-production or retired silicon, so the access is a portability test rather than a machine to hold a workload on; the separate Intel Developer Cloud console lane has no free instances at all.
- binding note: the same as limits note
- interface detail: SSH to a compute node (VS Code Remote-SSH through an SSH tunnel); the connector project is end-of-life
- tooling: the Intel DevCloud Connector for oneAPI Toolkits VS Code extension with the VS Code Remote-SSH extension
- composes with: 192 GB of RAM on a Xeon box is the largest free single-machine memory figure found evaluated offerings and would let a pandas or oneAPI workload run that no small PaaS can hold; the 120-day clock and the retired GPU generation are what cap it.
- reliability: no reliability event recorded
- notes: This is a refutation-shaped pair and must be recorded as both halves. The page's announcement feed is stale (last entry 2023-02-03), which is a warning that the 120-day claim may not be honoured on signup.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: time-boxed-access
  - facets.shape.ram_gib: 192
  - facets.shape.gpu_class: Intel Iris Xe MAX
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: '120 days of access (extensions available)', '192 GB RAM', '220 GB of file storage', and CPU/GPU/FPGA hardware list, quoted
  - [2] 2026-10-22: End-of-Life notice: the DevCloud connector for oneAPI is discontinued in the 2025.0.0 release and points at Intel Tiber Developer Cloud as the alternative
  - [3] 2026-10-22: Intel staff reply: 'there are currently no free instances available for the Standard tier in the Intel Developer Cloud Console'; JupyterHub batch instances remain accessible without payment
  - [1] 2026-11-03: the access page lists what the sandbox includes and prints no egress allowance or overage price | capture: sha256:1aecae63fec30a8fbeb7911330c08074cd2c8854b350afed0620039703e31e4c | quote: 120 days of access (extensions available)
  - [2] 2026-11-03: the DevCloud is reached over SSH (VS Code Remote-SSH to a compute node) | capture: sha256:36bd0f598831d3e6036520a29299e718e32f042f8b47a51c5906951bd027264d | quote: establishing a Visual Studio Code* (VS Code) Remote-SSH connection to the [Intel DevCloud]
  - [2] 2026-11-04: the documented client is the VS Code connector extension | capture: sha256:36bd0f598831d3e6036520a29299e718e32f042f8b47a51c5906951bd027264d | quote: This extension assists with configuring and establishing a Visual Studio Code* (VS Code) Remote-SSH connection to the
- sources:
  - [1] https://devcloud.intel.com/oneapi/home/
  - [2] https://github.com/intel/vscode-oneapi-devcloud-connector
  - [3] https://community.intel.com/t5/Intel-Tiber-Developer-Cloud/Standard-tier-Intel-dev-cloud-is-free/m-p/1612670

## Intel Liftoff

- `compute/intel-liftoff` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.intel.com/content/www/us/en/developer/tools/oneapi/liftoff.html
- free tier: The programme promises 'Free cloud credits for the Intel Tiber AI Cloud' and 'Credits from cloud service providers', with 'No Fees, No Equity Requirements, No Technology Restrictions', but the population is companies: 'Intel Liftoff for startups is open to early-stage AI and machine learning startups.' No credit amount, no expiry and no hardware quota is published anywhere on the page. The live URL now redirects to the generic Intel Developer Zone overview, so the terms are quoted from the 2025-06-12 capture. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: unpublished-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): the application is reviewed and the unit is a startup, so the gate is a company identity and an approval, not a quota. [1]
- limits note: the application is reviewed and the unit is a startup, so the gate is a company identity and an approval, not a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It would chain with the free Intel Developer Cloud allowance if the applicant is a company, since both spend one Tiber account. It does not chain for an individual.
- reliability: no reliability event recorded
- notes: Application form was inaccessible, returning HTTP 403 or redirect on attempted routes.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: unpublished-credit
  - facets.shape.gpu_class: Intel Gaudi / Xeon
- evidence:
  - [2] 2026-10-22: archived 2025-06-12 capture: 'Intel Liftoff for startups is open to early-stage AI and machine learning startups' and 'Free cloud credits for the Intel Tiber AI Cloud', both quoted
  - [1] 2026-10-22: read the URL resolves to the Developer Zone overview, which carries no programme terms
  - [3] 2026-10-22: the Tiber AI Cloud startups page returned HTTP 530, so current terms could not be read
  - [4] 2026-10-22: Intel's blog names two startup tracks, Catalyst and Community, and states credits go to startups
- sources:
  - [1] https://www.intel.com/content/www/us/en/developer/tools/oneapi/liftoff.html
  - [2] https://web.archive.org/web/20250612171913/https://www.intel.com/content/www/us/en/developer/tools/oneapi/liftoff.html?provider=wayback
  - [3] https://ai.cloud.intel.com/solutions/startups/
  - [4] https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/How-Intel-Liftoff-Accelerates-AI-Startups/post/1683078

## Intel Developer Cloud

- `compute/intel-developer-cloud` | fails-quota | evidence reported | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://console.cloud.intel.com/
- free tier: No free instances. Intel staff state the Standard tier has no free instances since the migration to the Intel Developer Cloud console, and instances are reservable only on Premium and Enterprise; free access that remains is limited to JupyterHub batch-processing training notebooks. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: Unverified: no page stating the signup requirement was read; the record's evidence covers the absence of free instances, the account tier that blocks a reservation, and the decommissioning of the service, and names no email, phone, card, ID document or institution. The gate it does establish is a paid service tier, not an identity check.
- interface: rest
- limits:
  - write-gated (binding): reserving an instance requires the Premium or Enterprise service tier, so the free lane stops before a machine is allocated. [1]
- limits note: reserving an instance requires the Premium or Enterprise service tier, so the free lane stops before a machine is allocated.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing composes here: the free lane is a JupyterHub training notebook, not a reservable machine.
- reliability: no reliability event recorded
- notes: The community replies are the evidence. This is a refutation of the 'Intel gives free Gaudi time' belief.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: Intel Gaudi 2
- evidence:
  - [2] 2026-10-22: Intel support reply, quoted: 'there are currently no free instances available for the Standard tier'; JupyterHub batch instances are accessible without payment
  - [3] 2026-10-22: 'you cannot reserve any instance if you are in a Standard account. The instance is only available for Premium and Enterprise only'
  - [4] 2026-10-22: Intel reply that the Developer Cloud 'has been formally discontinued, and the infrastructure fully decommissioned' with customer data sanitised and unrecoverable
- sources:
  - [1] https://console.cloud.intel.com/
  - [2] https://community.intel.com/t5/Intel-Tiber-Developer-Cloud/Standard-tier-Intel-dev-cloud-is-free/m-p/1612670
  - [3] https://community.intel.com/t5/Intel-Tiber-Developer-Cloud/Insufficient-cloud-credits/td-p/1550099
  - [4] https://community.intel.com/t/unacceptable-response-for-my-pull-request-and-issue/137190/4
