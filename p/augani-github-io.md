# Dory

> augani.github.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/augani-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/augani-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dory

- `compute/dory` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category local development runtime with agent sandbox VMs | tier Docker Core (free, open source)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T16:38:10.342Z (live) | stale on 2026-12-26
- url https://augani.github.io/dory/
- free tier: No hosted allowance: Dory is a native macOS app the user installs and runs locally, free and open source under GPL-3.0, with no account, no telemetry, no required cloud and no paid tier. Docker Core is the only required download and optional signed components add Kubernetes and Linux machine or desktop VMs. | unit: none | metered on: none | read on: 2026-11-25 | source: [1] | note: The operator list's $0.029 an hour for Dory has no basis on any first-party page: the product has no hosted meter. The hosted sandboxes of the other providers in this topic rank ahead of this download.
- per-object cap: not applicable: the unit is a local virtual machine, not a stored object; a managed .dorydrive grows from 128 GiB to 2 TiB and a machine disk is thin-provisioned at 64 GiB | source: [1] | note: The disk ceiling is local and set by the user.
- retention: Local Linux machines have their own disks and snapshots in the user's .dorydrive, preserved across normal uninstall; retention is set by the user, not by a vendor clock. | source: [1]
- egress: not applicable: the software runs on a machine the user supplies, so Dory meters no traffic and publishes no egress price or allowance | metered: no | source: [1]
- identity: anonymous | detail: No account is required: the site states 'No account. No telemetry. No required cloud. GPL-3.0.' and '0 accounts, telemetry, paid tiers'. Signing in is not an option because there is no vendor-hosted service. The user supplies their own Apple Silicon Mac and local disk.
- interface: cli, unknown
- limits:
  - write-gated (binding): the user installs and runs the app on an Apple Silicon Mac; there is no hosted capacity to allocate, and Windows 11 ARM and Intel hosts are unavailable [1]
- limits note: Apple Silicon only; desktop images are limited to Debian 13, Ubuntu 24.04 LTS and Kali rolling. USB passthrough and Intel host releases are unavailable, and custom ARM64 guest images are preview. The agent sandbox is policy-enforced with allowlisted egress and a daemon TTL.
- binding note: The offer is software the user installs on their own Mac, so there is no hosted quota, rate or retention clock to bind; the requirement to install it is the gate.
- interface detail: A versioned local JSON contract over stdio, an MCP server implementing protocol 2025-11-25, stable non-interactive CLI schemas and a Docker API context; sandbox VMs are driven by dory sandbox run, not by a public hosted endpoint.
- tooling: the user installs the signed Docker Core macOS app, then optional signed components for Kubernetes, headless Linux and desktop VMs; the user runs the app on their own Apple Silicon Mac and uses the dory CLI or MCP server, with no vendor-run capacity.
- composes with: A policy-enforced Linux VM per agent run with read-only mounts, allowlisted egress, resource caps, rollback and TTL cleanup can replace a hosted sandbox only where the user already has an Apple Silicon Mac; a hosted sandbox record ranks ahead of it.
- reliability: Capability support is labelled supported, preview or unavailable; the agent sandbox and custom guest images are preview, USB passthrough and Intel hosts unavailable, and signed updates keep a last-good snapshot for automatic rollback. No hosted service reliability event exists.
- notes: Dory is not hosted compute capacity: it is software the user installs and runs on an Apple Silicon Mac. The $0.029 an hour in the operator list has no source on any Dory page. It is the last-resort option: every hosted sandbox of the other providers in this topic ranks ahead of it.
- evidence note: The no-hosted-capacity finding, GPL-3.0 licence, no-account statement, component model and local sandbox description are read from the vendor's site and a third-party directory page on 2026-11-25 and quoted below.
- self hosted: yes
- extras:
  - shape.disk_gib: 64
  - shape.gpu_class: experimental in-guest GPU acceleration on Apple Silicon
  - billing_model: none: a free GPL-3.0 download with no hosted meter
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: the agent sandbox carries a daemon TTL set by the user; no vendor clock
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: published ports bind to localhost unless widened deliberately
  - network_out.static_ip: no
- evidence:
  - withheld 2026-11-25: the operator's list places Dory at $0.029 an hour; no first-party page states such a price | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 22. Dory → $0.029/h · billed per second
  - [1] 2026-11-25: Dory is a free open-source macOS app with no account or telemetry | capture: sha256:fa81c24e51bc280c3176495f86622c321f72da83173912e495854529188b4b29 | quote: Free and open source macOS 14+ No account or telemetry
  - [1] 2026-11-25: Dory runs a policy-enforced Linux VM per agent run locally, with resource caps, rollback and TTL | capture: sha256:fa81c24e51bc280c3176495f86622c321f72da83173912e495854529188b4b29 | quote: A dedicated non-root Linux VM per run. Read-only mount defaults, allowlisted egress, credential grants, resource caps, rollback, manifests, kill, and daemon TTL.
  - [1] 2026-11-25: the engine, disks and data live in a managed local drive on the user's Mac, not with a vendor | capture: sha256:fa81c24e51bc280c3176495f86622c321f72da83173912e495854529188b4b29 | quote: Images, containers, named volumes, networks, machines, and snapshots stay in one managed `.dorydrive` on local APFS storage.
  - [2] 2026-11-25: Dory is a native open-source macOS system that requires no cloud and has no account | capture: sha256:ecd53152264b2c1b77ed509facc3861748eb40711c69172a4034601f409b434b | quote: No account. No telemetry. No required cloud. GPL-3.0.
  - [3] 2026-11-25: a third-party directory describes Dory as a free, open-source local macOS app requiring no account and with no paid tiers | capture: sha256:09c18e3df87259b73427cdc6a5b70569ca77be8fe80e80f6ee91fca836364f9b | quote: Fully free, GPL-3.0 licensed. No account, no telemetry, no paid tiers.
  - [2] 2026-11-24: Dory is free, open source, local and needs no account or cloud service | capture: sha256:571984f79fce67a7b6ebec40b375360d865ea4af8dce4200c96a14a2c3157631 | quote: No account. No telemetry. No required cloud. GPL-3.0.
  - [2] 2026-11-24: the Docker data disk starts at a 128 GiB logical ceiling and grows on demand to 2 TiB | capture: sha256:571984f79fce67a7b6ebec40b375360d865ea4af8dce4200c96a14a2c3157631 | quote: The Docker data disk starts with a 128 GiB logical ceiling without reserving that physical space.
  - [2] 2026-11-24: published ports bind to localhost unless deliberately widened | capture: sha256:571984f79fce67a7b6ebec40b375360d865ea4af8dce4200c96a14a2c3157631 | quote: Published ports bind to localhost unless you deliberately widen them.
  - [4] 2026-11-24: no account, cloud control plane, telemetry or commercial-use tier is required; the software runs on the user's Mac | capture: sha256:f4138e9c7d644623e539454be47a11959b883288ca5c32931f01aa93610d8ea1 | quote: There is no required Docker Desktop, external VM manager, account, cloud control plane, telemetry, or commercial-use tier. Dory is GPL-3.0 software and stores workload data on your Mac.
  - [4] 2026-11-24: there is no Dory account or sign-in | capture: sha256:f4138e9c7d644623e539454be47a11959b883288ca5c32931f01aa93610d8ea1 | quote: No Dory account or sign-in
  - [5] 2026-11-24: sandbox egress defaults to none and blocks all workload egress, with explicit outbound and full modes | capture: sha256:13f9f0a574eb43286043bd78e026effee9d33a8ee96ca9c8bc000b9d87196d1e | quote: `none` is the default and blocks all workload egress.
  - [5] 2026-11-24: the local stdio MCP contract needs no account, cloud service or control plane and starts read-only | capture: sha256:13f9f0a574eb43286043bd78e026effee9d33a8ee96ca9c8bc000b9d87196d1e | quote: Dory exposes a local, versioned automation contract for coding agents. It does not require a Dory account, cloud service, or remote control plane.
  - [5] 2026-11-24: sandbox runs are deleted by default, see no host files unless mounted and keep a daemon-owned TTL | capture: sha256:13f9f0a574eb43286043bd78e026effee9d33a8ee96ca9c8bc000b9d87196d1e | quote: The sandbox is a dedicated VM, runs non-root, and is deleted by default. It sees no host files unless a mount is supplied; omitted mount modes are read-only:
  - [1] 2026-11-25: Dory is a free local system with no account, no hosted control plane and no paid tier, so no hosted quota failure is documented | capture: sha256:fa81c24e51bc280c3176495f86622c321f72da83173912e495854529188b4b29 | quote: No Dory account, no telemetry, no remote control plane, and no paid commercial-use tier. Sandboxes share no files by default and support bundles are redacted.
  - [4] 2026-11-25: Dory is free GPL-3.0 software the user installs and runs on their own Mac, with no hosted capacity and no quota, so qualifies-with-caveat stands | capture: sha256:f4138e9c7d644623e539454be47a11959b883288ca5c32931f01aa93610d8ea1 | quote: There is no required Docker Desktop, external VM manager, account, cloud control plane, telemetry, or commercial-use tier. Dory is GPL-3.0 software and stores workload data on your Mac.
- sources:
  - [1] https://augani.github.io/dory/
  - [2] https://usedory.dev/
  - [3] https://www.everydev.ai/tools/dory
  - [4] https://github.com/Augani/dory
  - [5] https://augani.github.io/dory/docs/agents.md
