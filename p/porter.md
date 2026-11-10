# Porter

> porter.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/porter/ | JSON https://fshy.ajam.dev/api/v1/entity/porter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Porter

- `compute/porter` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:40:26.616Z (live) | stale on 2026-12-05
- url https://porter.run
- free tier: a startup programme granting 6 months free; the compute runs in self-hosted AWS, Azure or Google Cloud account and bills there | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.porter.run/pricing read 2026-11-04 prints no egress allowance or overage price; the Porter charge excludes the underlying cloud provider's cost, so network transfer bills in the user's own AWS, Azure or Google Cloud account | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - write-gated (binding): the free offer is a 6-month startup programme; the compute bills to self-hosted cloud account throughout [1]
- interface detail: CLI: the Porter CLI, documented at docs.porter.run/cli/installation, installed on macOS via Homebrew or shell script, on Linux via shell script and on Windows via manual binary download.
- tooling: the Porter CLI (`porter`), installed with `brew install porter-dev/porter/porter` on macOS.
- composes with: not established
- reliability: no reliability event recorded
- notes: Porter's control plane is a service, and the cluster it creates runs in a cloud account the user rents; Porter spins it up, and the user installs no machine.
- evidence note: the site was read on 2026-10-22 and states that the cluster runs in self-hosted cloud account, with a 6-month free startup programme. The free half is the control plane, not the compute
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a user's own cloud account holds the cluster and sets the clocks
  - persistent_storage.price: billed by a user's own cloud
  - persistent_storage.durability: a user's own cloud volumes
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: as long as a user keeps it
  - network_out.out: yes
  - network_out.in: yes
  - network_out.ports: a user's own cloud account
  - free_tier_kind: trial
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Connect your cloud account. Porter spins up a production-ready cluster in your own AWS, Azure, or Google Cloud account in minutes.' and 'Startups get 6 months free', quoted
  - [2] 2026-11-04: Porter's fee covers app resources only; the page prints no egress allowance or price | capture: sha256:87ca3af195d41080355b971240b1f0c5547d5d1ac40ef01961c2e7d462e68be5 | quote: Does not include the cost of the underlying cloud provider.
  - [3] 2026-11-04: Porter ships a CLI | capture: sha256:3d0ad85642dc512c9d22242e19a91dee53b4507d46a83a19ef4c9617c17d3eaf | quote: To install the Porter CLI, see the OS-specific instructions below.
  - [3] 2026-11-04: the provider documents the Porter CLI and its install routes | capture: sha256:3d0ad85642dc512c9d22242e19a91dee53b4507d46a83a19ef4c9617c17d3eaf | quote: Install the Porter CLI on macOS via Homebrew or shell script, on Linux via shell script, and on Windows via manual binary download
  - [3] 2026-11-04: the CLI installs as the porter-dev/porter/porter Homebrew formula | capture: sha256:3d0ad85642dc512c9d22242e19a91dee53b4507d46a83a19ef4c9617c17d3eaf | quote: brew install porter-dev/porter/porter
- sources:
  - [1] https://porter.run
  - [2] https://www.porter.run/pricing
  - [3] https://docs.porter.run/cli/installation.md
