# Gravix Layer

> gravixlayer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gravixlayer/ | JSON https://fshy.ajam.dev/api/v1/entity/gravixlayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gravix Layer

- `compute/gravix-layer` | trial-only | evidence documented | binding volume-quota | category microVM sandbox | tier Early access ($250 credit)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.709Z (live) | stale on 2026-12-26
- url https://gravixlayer.com/
- free tier: Pay as you go. $250 in credit. No card required. Early access includes $250 in credit, and you do not need a card. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The $250 is an early-access credit on a private-preview service, not a permanent free plan. Compute is $0.0436 per vCPU-hour, $0.0096 per GiB-hour of memory and $0.0001 per GiB-hour of storage, billed per second; a typical 1 vCPU/1 GiB/4 GiB disk agent-hour is about $0.054. Pausing a sandbox stops the CPU and memory charge.
- per-object cap: not applicable: the billed unit is allocated vCPU, memory and disk time, not an object; no per-object cap is published | source: [1]
- retention: Files can be mounted from a bucket and kept after the run ends; no retention period for sandbox files is published. | source: [1] | note: Snapshots freeze a ready machine so every new task boots from it in about 25 ms.
- egress: not published: the pricing section states no egress allowance or price; the network policy is default deny and only named hosts and ports are reachable | metered: no | source: [1]
- identity: email | detail: The early-access form says 'Email is all we need' and asks for Email; the site says 'Gravix Layer is in private preview. Request access from this site. You do not need a card to start.' No phone, ID or institution is named.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): $250 of early-access credit at $0.0436 per vCPU-hour, $0.0096 per GiB-hour memory and $0.0001 per GiB-hour storage [1]
  - per-ip-shaping: network policy is default deny: only named hosts and ports are reachable [1]
- limits note: A runtime that exceeds its timeout is terminated. Billing is on allocated size, not observed utilization: a 2 vCPU sandbox that is idle costs the same as one at full CPU.
- binding note: The $250 early-access credit is the first limit reached at published rates, ahead of any unpublished session or concurrency cap; pausing stops the CPU and memory charge.
- interface detail: Eight native APIs cover terminal/PTY, code, files, storage, git, browser, computer and snapshots; Python SDK, TypeScript SDK and CLI are offered, with SSH access listed as a feature.
- endpoint: https://api.gravixlayer.ai/v1
- tooling: the Gravix Layer Python SDK (github.com/gravixlayer/gravixlayer-python), TypeScript SDK and CLI; sandboxes, browsers and computers are each created with one call.
- composes with: Sandbox, browser and computer run on one platform with a shared network policy and MCP gateway, so a hosted agent can use all three surfaces under one account; the vendor-managed multi-cloud lane is the hosted offer, while bring-your-own-cloud and on-premises AI Factory are roadmap items and are not recommendations here.
- reliability: Private preview with a request-access gate; hardware-isolated microVMs and a default-deny network policy; one sandbox cannot read another's files; no published SLA.
- notes: Hosted hardware-isolated microVM sandboxes, browsers and computers on one platform, billed per second for vCPU, memory and storage. The $250 credit with no card is early-access credit on a private-preview service, not a standing free tier, so the verdict is trial-only; hosted managed multi-cloud is the offer, with bring-your-own-cloud and on-premises options only on the roadmap.
- evidence note: The rates, $250 credit, no-card statement and email-only access form are quoted from the vendor's own pages read 2026-11-25; the service is still private preview.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 4
  - shape.gpu_class: none published
  - shape.gpu_count: 0
  - shape.note: a typical agent-hour is 1 vCPU, 1 GiB memory and 4 GiB disk at about $0.054
  - billing_model: per-second usage of vCPU, memory and storage, with $250 early-access credit
  - free_tier_kind: signup-credit
  - network_out.allow_outbound: yes
  - network_out.ports: named hosts and ports only
  - session_cap.restart_required: no
  - session_cap.note: pausing a sandbox stops the CPU and memory charge; no session cap published
- evidence:
  - [1] 2026-11-25: vCPU is priced at $0.0436 per vCPU-hour | capture: sha256:ffaf511893323eadb57d3fe7b0e6208109a02d92144fa6aae49d8e0cd88d9eb8 | quote: <p class="metric mt-6">$0.0436</p><p class="metric-unit">per vCPU / hour</p>
  - [1] 2026-11-25: early access gives $250 of credit and needs no card | capture: sha256:ffaf511893323eadb57d3fe7b0e6208109a02d92144fa6aae49d8e0cd88d9eb8 | quote: <p class="text-sm font-medium leading-5 tracking-[-0.012em] text-foreground/75">Pay as you go. <strong class="font-semibold text-foreground">$250</strong> in credit. No card required.</p>
  - [1] 2026-11-25: memory is $0.0096 per GiB-hour and storage is $0.0001 per GiB-hour | capture: sha256:240b82f5b8368d38585feede81ffc9282606b72d4b1b06ce85fbd038526bffec | quote: $0.0436 per vCPU / hour $0.0096 memory · per GiB / hour $0.0001 storage · per GiB / hour
  - [2] 2026-11-25: the access form asks only for an email | capture: sha256:473244d170b12591a48d971fcc23644460396f4f7e1b4881093d9aa77da75c1d | quote: Email is all we need.
  - [3] 2026-11-24: usage-based per-second billing with USD 250 credit and no card required | capture: sha256:8947a20a6040b366e8325531cddc1abbdb5446c59d4320b3e5d49a9fbcbf030b | quote: Usage-based vCPU, memory and storage, billed per second. Start building with $250 in credit. No card required.
  - [4] 2026-11-24: early-access credit terms and the base-small hourly price | capture: sha256:c67456347fe3016b3a5a65c7d9fe7ebf33d4f0d4dd79d962a80bf411784525f6 | quote: Early access includes \$250 in free credit. No card required. No minimum spend.
  - [4] 2026-11-24: the base-small template rate with its vCPU, memory and disk components | capture: sha256:c67456347fe3016b3a5a65c7d9fe7ebf33d4f0d4dd79d962a80bf411784525f6 | quote: | `base-small` | 1 vCPU, 1 GiB, 4 GiB disk | \$0.0436 | \$0.0096 | \$0.000400 | \$0.0536 |
  - [4] 2026-11-24: billing is on allocated size, not observed utilization | capture: sha256:c67456347fe3016b3a5a65c7d9fe7ebf33d4f0d4dd79d962a80bf411784525f6 | quote: Billing is on allocated size, not observed utilization. A 2 vCPU sandbox that is idle costs the same as one at full CPU.
  - [5] 2026-11-24: the per-account resource and rate ceilings for a verified account | capture: sha256:5eb46065b42bdb39b10fed02e0129c410dd8c6d7b5790e8ee657a047f8b77148 | quote: | Runtime creation per minute | 100 |
  - [5] 2026-11-24: the vCPU ceiling and the account-verification condition | capture: sha256:5eb46065b42bdb39b10fed02e0129c410dd8c6d7b5790e8ee657a047f8b77148 | quote: | vCPU | 10 |
  - [2] 2026-11-24: the access request asks for email only, with no card field | capture: sha256:473244d170b12591a48d971fcc23644460396f4f7e1b4881093d9aa77da75c1d | quote: Email is all we need.
  - [6] 2026-11-24: a new sandbox cannot reach the public internet without an attached allowlist policy | capture: sha256:1131c15d65411d611195c9036bae6b7822f36dc9230d8b36e37398f824c6385f | quote: A new sandbox cannot reach the public internet. Attach a network policy to allow or deny outbound traffic: a public API, a package registry, or a private host.
  - [6] 2026-11-24: no attached policy means outbound is blocked | capture: sha256:1131c15d65411d611195c9036bae6b7822f36dc9230d8b36e37398f824c6385f | quote: No policy attached means blocked
  - [7] 2026-11-24: runtimes deny outbound traffic by default and need a network policy to reach model APIs | capture: sha256:b59e6f1edb47d045203b9db825cc00d3dc06b51227380faac195e45dd05d265e | quote: Runtimes deny outbound traffic by default.
- sources:
  - [1] https://gravixlayer.com/
  - [2] https://gravixlayer.ai/early-access
  - [3] https://gravixlayer.ai/pricing
  - [4] https://docs.gravixlayer.ai/documentation/agentruntime/pricing
  - [5] https://docs.gravixlayer.ai/documentation/agentruntime/service-quotas
  - [6] https://docs.gravixlayer.ai/documentation/agentruntime/getting-started/network-policies
  - [7] https://docs.gravixlayer.ai/documentation/agentruntime/templates
