# FABRIC testbed

> fabric-testbed.net | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fabric-testbed/ | JSON https://fshy.ajam.dev/api/v1/entity/fabric-testbed.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FABRIC

- `compute/fabric` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://portal.fabric-testbed.net/about/about-fabric
- free tier: FABRIC is an NSF-funded instrument of 29 sites across commercial collocation, national laboratories and campuses, connecting configurable compute with SmartNICs, GPUs, FPGAs and NVMe, plus P4-programmable switches at selected sites. Experimenters build project-scoped slices of virtual machines, network services and storage across sites, through the portal, a JupyterHub, or the FABlib API. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: unmetered-experiment-slices
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: an institutional login through CILogon: the signup guide states 'Currently, FABRIC requires the use of your institutional login via CI Logon. Using other options like Google, GitHub, Microsoft, or ORCID might require extra approvals and should be avoided whenever possible', and resource access additionally needs 'membership in an active FABRIC project'. The portal's identity-provider dropdown defaults to ORCID, which anyone can register for, so whether an ORCID signup completes without staff approval is unverified. No card, hold, debit or prepaid term is stated.
- interface: rest
- limits:
  - write-gated (binding): The documented sign-up route is an institutional login through CILogon, and access to resources additionally requires membership of an active FABRIC project; ORCID, Google, GitHub and Microsoft are named as possible identity providers but the teaching materials say they "might require extra approvals" without naming the approver or the criteria. [1]
- limits note: The documented sign-up route is an institutional login through CILogon, and access to resources additionally requires membership of an active FABRIC project; ORCID, Google, GitHub and Microsoft are named as possible identity providers but the teaching materials say they "might require extra approvals" without naming the approver or the criteria.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: FABRIC composes with an ACCESS allocation for anything compute-heavy, because it supplies the programmable network and SmartNIC hardware that Jetstream2 and the OSPool do not, and its API means a slice can be created from a script rather than a portal session.
- reliability: no reliability event recorded
- notes: Self-sign-up workflow with ORCID remains unverified without staff intervention.
- extras:
  - facets.class: open-science-grid
  - facets.free_tier_kind: unmetered-experiment-slices
- evidence:
  - [1] 2026-10-22: 29 sites of equipment at commercial collocation spaces, national laboratories and campuses, quoted
  - [2] 2026-10-22: FABRIC provides compute and storage with SmartNICs, GPUs, FPGAs and NVMe; "Specialized components such as GPUs, FPGAs, SmartNICs, NVMe devices, or programmable switches may require additional project permissions and are subject to site availability", quoted
  - [3] 2026-10-22: "Currently, FABRIC requires the use of your institutional login via CI Logon. Using other options like Google, GitHub, Microsoft, or ORCID might require extra approvals and should be avoided whenever possible", quoted
  - [2] 2026-10-22: "Access to testbed resources also requires membership in an active FABRIC project", quoted
  - [4] 2026-10-22: the portal's identity provider dropdown defaults to ORCID, and the instructions say to change it to a university affiliation, quoted
- sources:
  - [1] https://portal.fabric-testbed.net/about/about-fabric
  - [2] https://support.access-ci.org/documentation/resources/fabric
  - [3] https://github.com/fabric-testbed/teaching-materials/blob/main/Aditional%20Resources/Using%20Fabric%20Structure/Signing%20up.md
  - [4] https://teaching-on-testbeds.github.io/hello-fabric/

## FABRIC testbed

- `storage/fabric-testbed` | fails-identity | evidence reported | binding none | category research testbed - distributed compute + 0.5-1 PB file storage
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://portal.fabric-testbed.net/
- free tier: VMs up to 64 cores / 384 GB RAM with directly attached NVMe, GPUs, SmartNICs; 'large storage volumes'; facility holds 'between 1/2 and 1PB of file storage space' for experiment data, plus experiment-attached block storage | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Bastion keys expire in 6 months, sliver keys in 2 years. | days: 180 | source: [1] | note: not stated
- egress: free; on-demand 25-100 Gbps inter-site links, public IPv4/IPv6 peering, Internet2 100 Gbps cloud peering | metered: no
- identity: institution | detail: institution
- interface: ssh, cli
- limits:
  - per-ip-shaping: 1 Gbps [1]
  - retention-clamped: expire in 6 months [1]
- limits note: Slices have 'a finite lifetime, but can typically be extended before they expire'. Management plane is rate-limited to ~1 Gbps and 'has traffic filtering rules to prevent hosting Internet-facing services' - so you cannot serve from the control network, only from experiment links. Identity is CILogon/InCommon R&S, i.e. an institutional IdP. Bastion keys expire in 6 months, sliver keys in 2 years.
- interface detail: fablib Python API, JupyterHub, portal; ssh via bastion.fabric-testbed.net
- tooling: fablib, FABRIC CLI, Jupyter notebooks with preloaded tokens
- composes with: slice with NVMe + block storage; the management plane is explicitly not a data path
- reliability: Explicitly 'experimental and no production'; not expected to provide production-grade reliability.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: VMs up to 64 cores / 384 GB RAM with directly attached NVMe, GPUs, SmartNICs; 'large storage volumes'; facility holds 'between 1/2 and 1PB of file storage space' for experiment data, plus experiment-attached block storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The facility has between 1/2 and 1PB of file storage space'; VMs 'with storage in the form of dedicated NVMe drives and slower, but larger persistent block storage'; 'The portal and Jupyter Hub use federated identity through CI Logon and support any institutional identity provider that is part of InCommon R&S'
  - [2] 2026-10-21: 'Management plane is rate-limited to about 1Gbps ... has traffic filtering rules to prevent hosting Internet-facing services and should not be used as part of experiment data flows'; 'Slices have a finite lifetime'
  - [1] 2026-10-21: international nodes exist at CERN, University of Amsterdam, Bristol, Tokyo, but framed as partner facilities, not individual access
- sources:
  - [1] https://learn.fabric-testbed.net/knowledge-base/frequently-asked-starter-questions/
  - [2] https://learn.fabric-testbed.net/knowledge-base/things-to-know-when-using-fabric-for-the-first-time/
