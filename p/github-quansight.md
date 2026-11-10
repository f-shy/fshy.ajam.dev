# Quansight

> github.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-quansight/ | JSON https://fshy.ajam.dev/api/v1/entity/github-quansight.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quansight

- `compute/quansight` | dead | evidence documented | binding write-gated | category CI runner
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://github.com/Quansight/open-gpu-server
- free tier: This was the clearest free-GPU-CI offer in the open-source ecosystem and it is gone. Quoted at the top of the repository: 'The server will be decommissioned as of 2026-03-13 and the service will not be available from then on.' What it offered while alive: an OpenStack host with '48 Cores', '~500 GB Memory' and '6x NVIDIA Tesla V100', spinning up runners from gpu_tiny at 4 vCPU / 2 GB / 20 GB / 1x V100 up to gpu_4xlarge at 8 vCPU / 64 GB / 100 GB / 1x V100, free to conda-forge feedstocks that needed GPU CI. Quoted limitation: 'Only 4 GPUs can be exposed to the VMs at a time; expect queues. This is not per repository, but a server-wide limitation.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: sponsored-community-service
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Two things failed, in order: access required a conda-forge feedstock and a maintainer listed in the project's access file, which requires an institutional affiliation, and then the hardware was decommissioned on 2026-03-13, so the capacity is now zero on both counts. [1]
- limits note: Two things failed, in order: access required a conda-forge feedstock and a maintainer listed in the project's access file, which requires an institutional affiliation, and then the hardware was decommissioned on 2026-03-13, so the capacity is now zero on both counts.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing to chain now. The structural lesson is that the free-GPU-CI lane existed as one sponsored host with six GPUs, four of them exposed at a time, and it went away with one colocation decision.
- reliability: no reliability event recorded
- notes: The free GPU CI lane is not a category with several providers in it; it was one sponsored OpenStack host for one package ecosystem, gated on being a conda-forge maintainer, and it is decommissioned. The nearest live substitute is GitLab's OSS programme with its T4 runner, recorded separately, and the nearest paid substitutes are GitHub's GPU larger runner at USD 0.052 a minute and external runner vendors.
- extras:
  - facets.class: ci-runner-capacity
  - facets.free_tier_kind: sponsored-community-service
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 8
  - facets.shape.gpu_class: V100
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: 'The server will be decommissioned as of 2026-03-13 and the service will not be available from then on.'; base host 48 cores, ~500 GB memory, 6x NVIDIA Tesla V100; the six gpu_* and five ci_* runner shapes; 'Only 4 GPUs can be exposed to the VMs at a time ... a server-wide limitation'; 'We have not yet implemented a time limit per job'
  - [2] 2026-10-22: the same text from the repository's own main branch, confirming the decommission notice is not a rendering artefact
  - [3] 2026-10-22: reported origin: at SciPy 2024 the project learned that 'free GPU runners are available via the Quansight's/MetroStar's Open GPU Server', which fixes roughly when was known and how it was described to outsiders
  - [4] 2026-10-22: the successor did not restore GPU: conda-forge moved to GitHub Actions large runners and states 'Sadly, we don't have GPU CI jobs yet.'
- sources:
  - [1] https://github.com/Quansight/open-gpu-server
  - [2] https://raw.githubusercontent.com/Quansight/open-gpu-server/main/README.md
  - [3] https://github.com/stumpy-dev/stumpy/issues/1005
  - [4] https://conda-forge.org/blog/2026/06/17/large-runners-gha/
