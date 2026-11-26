# Nirvana Labs

> nirvanalabs.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nirvanalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/nirvanalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nirvana Labs

- `compute/nirvana-agent-sandboxes` | paid-only | evidence documented | binding volume-quota | category agent sandbox | tier N1 pay-as-you-go (ephemeral and persistent agent sandboxes)
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T10:11:14.949Z (live) | stale on 2026-12-25
- url https://nirvanalabs.io/pricing
- free tier: No recurring free sandbox allowance is published. A USD 250 signup credit was offered to accounts created by 31 October 2026 and applied to agent sandboxes, requiring a company organization and a valid payment method; the campaign end date has passed as of 2026-11-24. | unit: credits | metered on: unstated | read on: 2026-11-24 | source: [1] | note: The credit is promotional and was limited to accounts created between 22 September and 31 October 2026. It expired two calendar months after being applied, and one credit was allowed per company.
- per-object cap: not applicable: the unit is a sandbox with a workspace volume, not a stored object
- retention: Ephemeral sandboxes have no disk and leave nothing behind on pause or stop; a persistent sandbox mounts an ABS volume at /workspace that survives pause, resume and sandbox deletion, and the same volume can be mounted on a new sandbox. | source: [2]
- egress: External egress is USD 0.02 per GB transferred at any volume, including object-storage egress; ingress and transfers between Nirvana IPs are free. Sandbox ports are reached through signed, expiring endpoints on the cluster gateway. | metered: yes | free allowance: transfers between Nirvana IPs are free | price per TB: USD 20.00 per TB (1,000 GB) | source: [3]
- identity: card | detail: Signup requires an email and a company organization, and a valid payment method is required before credit can be applied. The sandbox API uses the organization API key; there is no separate sandbox key.
- interface: rest, cli, chat
- limits:
  - volume-quota (binding): Compute is USD 0.016 per vCPU-hour plus USD 0.004 per GB-RAM-hour; a billing month is 730 hours. Sandbox-only rates are not published. [3]
- limits note: An organization can run any number of sandbox clusters within its quotas; the quota numbers are not published.
- binding note: The published hourly compute meters and unpublished sandbox quota are what bound a long-running workload; no per-sandbox or organization quota number is published.
- interface detail: OpenSandbox-compatible Sandbox Lifecycle API at https://api.nirvanalabs.io/v1/sandboxes, reachable with any OpenSandbox SDK or plain HTTP; MCP server, CLI and Terraform provider for the surrounding cloud resources.
- endpoint: part of interface detail
- tooling: OpenSandbox SDKs for TypeScript, Python, Go, Java, Kotlin and C#; a hosted MCP server and a CLI for Nirvana Cloud resources.
- composes with: Sandboxes checkpoint to an ABS volume at /workspace, so a long-running agent can pause to stop paying for compute and resume on a new sandbox with the same files.
- reliability: Agent Sandboxes is an early release; creating sandboxes from snapshots is not supported yet, and pause in 1.46 s at p50 with all 5,501 checkpoints recovered after an ungraceful kill is reported on the vendor benchmark page.
- notes: Sandbox compute is billed from the same flat N1 rates as VMs: USD 0.016 per vCPU-hour plus USD 0.004 per GB-RAM-hour. A separate figure of 20% below mainstream sandbox providers carries no numeric sandbox rate. The USD 250 signup credit campaign ended on 31 October 2026.
- evidence note: Rates, egress, signup gate and sandbox limits are quoted from first-party pages read on 2026-11-24; the sandbox-only rate is not published.
- extras:
  - shape.note: sandbox cluster instance types are chosen at cluster creation; the shape is not published on the pricing page
  - billing_model: pay-as-you-go per vCPU-hour and per GB-RAM-hour, pro-rated hourly
  - term: month-to-month
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: signed, expiring endpoint for a port
  - session_cap.restart_required: no
  - session_cap.note: sandbox expiration can be renewed through the API; no default lifetime is published
- evidence:
  - [3] 2026-11-24: N1 compute is priced per vCPU-hour, with a 730-hour billing month | capture: sha256:4bb7ad59526a7272a91d0ddc2fe8ce1bb0b061459e5cb95809671b6a6ae19abf | quote: - vCPU — $0.016 per vCPU per hour. One vCPU on an AMD EPYC 9354P host. No burst credits and no shared-core throttling.
  - [3] 2026-11-24: RAM is priced separately at USD 0.004 per GB-hour | capture: sha256:4bb7ad59526a7272a91d0ddc2fe8ce1bb0b061459e5cb95809671b6a6ae19abf | quote: - Memory — $0.004 per GB of RAM per hour. Instance memory, priced per GB and independent of the vCPU count.
  - [3] 2026-11-24: a billing month is 730 hours and annual commitments take 20% off compute | capture: sha256:4bb7ad59526a7272a91d0ddc2fe8ce1bb0b061459e5cb95809671b6a6ae19abf | quote: Every published rate is reproduced below, in USD. A billing month is 730 hours and annual commitments take 20% off compute, block storage and network attachments.
  - [3] 2026-11-24: external egress is USD 0.02 per GB and transfers between Nirvana IPs are free | capture: sha256:4bb7ad59526a7272a91d0ddc2fe8ce1bb0b061459e5cb95809671b6a6ae19abf | quote: - External egress — $0.02 per GB transferred. Outbound data transfer to external destinations, Object Storage included, charged at one rate with no tiers. Ingress and transfers between Nirvana IPs are free.
  - [2] 2026-11-24: sandbox prices are stated relative to mainstream providers at 20% below, with no sandbox-specific number | capture: sha256:f58e7b5814a34c3b756318de65e1b854045cc632f4c3a2079734097db438aeda | quote: Priced 20% below mainstream managed sandbox providers, with infrastructure and orchestration on Nirvana's high-performance cloud.
  - [2] 2026-11-24: ephemeral sandboxes have no disk and persistent sandboxes keep /workspace on ABS across pause and resume | capture: sha256:f58e7b5814a34c3b756318de65e1b854045cc632f4c3a2079734097db438aeda | quote: Persistent sandboxes get a dedicated volume backed by our own Accelerated Block Storage (ABS) mounted at /workspace. First boot takes 6-7s, and everything the agent writes to /workspace survives pause and resume: pause instantly to stop paying for compute, resume instantly with every file exactly where it was.
  - [4] 2026-11-24: sandboxes use an OpenSandbox-compatible API at a fixed base URL | capture: sha256:cf0f5406ecdeec1c7a377b25061381564186b55d91e103d934a9faa090f8c505 | quote: The Nirvana API serves OpenSandbox’s Sandbox Lifecycle API at `https://api.nirvanalabs.io/v1/sandboxes`. OpenSandbox SDKs for TypeScript, Python, Go, C#, Java and Kotlin work unchanged with the base URL `https://api.nirvanalabs.io/v1`.
  - [4] 2026-11-24: no separate sandbox API key is issued | capture: sha256:cf0f5406ecdeec1c7a377b25061381564186b55d91e103d934a9faa090f8c505 | quote: Sandboxes use your Nirvana organization API key, with the same project scoping and permissions as the rest of the platform. There is no separate sandbox key.
  - [4] 2026-11-24: ports are reached only through signed, expiring endpoints | capture: sha256:cf0f5406ecdeec1c7a377b25061381564186b55d91e103d934a9faa090f8c505 | quote: Every sandbox is created with secure access. Ports are reached only through signed, expiring endpoints: the cluster’s gateway hostname plus routing headers that the API returns.
  - [4] 2026-11-24: sandbox cluster counts are bounded by unpublished organization quotas | capture: sha256:cf0f5406ecdeec1c7a377b25061381564186b55d91e103d934a9faa090f8c505 | quote: Create, rename, tag and delete sandbox clusters through the API. An organization can run any number of them, within its quotas.
  - [1] 2026-11-24: the USD 250 credit was limited to first accounts opened between 22 September and 31 October 2026 | capture: sha256:c21b02e975a82b4b5279187d13cd0a3564cdb45e851af76cbfb29e3105822f9c | quote: Available to any company opening its first Nirvana Labs account between 22 September 2026 and 31 October 2026. Eligible credits do not have to be granted by 31 October 2026; new signups after that date do not qualify.
  - [1] 2026-11-24: the credit applies to agent sandboxes | capture: sha256:c21b02e975a82b4b5279187d13cd0a3564cdb45e851af76cbfb29e3105822f9c | quote: Credit applies to Nirvana Labs service charges only: compute, storage, managed Kubernetes and agent sandboxes.
  - [1] 2026-11-24: the signup credit required a company organization and a valid payment method | capture: sha256:c21b02e975a82b4b5279187d13cd0a3564cdb45e851af76cbfb29e3105822f9c | quote: A company organization and a valid payment method are required before credits can be applied. Completing setup does not itself confirm that credits have been granted.
  - [1] 2026-11-24: the credit expires two calendar months after it is applied | capture: sha256:c21b02e975a82b4b5279187d13cd0a3564cdb45e851af76cbfb29e3105822f9c | quote: The credit expires two calendar months after the credit is applied to the account. Each grant has its own expiry date. Unused credit is not refunded, extended or carried over.
- sources:
  - [1] https://nirvanalabs.io/welcome
  - [2] https://nirvanalabs.io/blog/nirvana-agent-sandboxes
  - [3] https://nirvanalabs.io/pricing
  - [4] https://docs.nirvanalabs.io/cloud/compute/agent-sandboxes/
