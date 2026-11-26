# Quave ONE

> quave.one | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quave/ | JSON https://fshy.ajam.dev/api/v1/entity/quave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quave ONE (agent sandboxes direct)

- `compute/quave-one-agent-sandboxes-direct` | paid-only | evidence documented | binding write-gated | category sandbox (gVisor, hosted Quave regions) | tier Direct, pay per use at 3x the regional zCloud rate
- identity a placeholder: card and phone unknown | verified 2026-11-25T02:12:34.793Z (live) | stale on 2026-12-26
- url https://quave.one/agent-sandboxes
- free tier: Direct: pay per use at 3× the regional zCloud rate. No platform fee. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Sandboxes are enabled per account: after signup the user must ask Quave to turn them on. Hobby accounts need no card and US-1 Hobby has no charge, but no first-party page states that sandboxes can run in the Hobby region, so no free sandbox route is established. The Connect license on the user own cloud account starts at USD 399 a month and is a separate offer.
- per-object cap: not applicable: the unit is a sandbox, not a stored object
- retention: an idle timeout or a maximum lifetime terminates a sandbox; the workspace can be snapshotted at pause or kept on a shared volume, which outlives the sandbox and can be attached to the next one | source: [2]
- egress: no extra fee for network traffic in supported regions; some regions cap the included outgoing traffic at 10 GB per month per zCloud, others list it as unlimited. Sandboxes can restrict outbound traffic to IP/CIDR ranges and domains, and internal infrastructure ranges are always blocked. | metered: no | free allowance: 10 GB per month per zCloud in some regions, unlimited in US-3, EU-1 and EU-2 | source: [3]
- identity: email | detail: unverified: no rendered sign-up text was captured; the public app access page has only a /continue-with-email route name in a script and loads passwordless and Google and GitHub OAuth packages, so the exact registration identity is unverified
- interface: rest, cli
- limits:
  - volume-quota: 200 active sandboxes per account by default, raisable on request [2]
  - write-gated (binding): sandboxes are enabled per account; after signing up the user must ask Quave to turn them on [1]
- binding note: the sandbox capability is not on by default: an account must ask Quave to enable it before the first sandbox can be created, which stops a new user before the 200-sandbox ceiling or the usage meter matters
- interface detail: a Public API with /sandbox/create and /sandbox/execute, an MCP server, and a Sandboxes dashboard page
- tooling: REST API, MCP server and dashboard; sandboxes run any OCI image pinned by digest, and a stock E2B-style workflow can be driven through the API
- composes with: a hosted gVisor sandbox whose workspace can be snapshotted or written to a shared object-storage volume and reused in a later sandbox, so a long agent run resumes from retained state; 200 active sandboxes per account is the default safety ceiling
- reliability: an idle timeout or maximum lifetime terminates a sandbox rather than pausing it, a terminated sandbox's snapshot remains on the shared volume or object storage, and internal infrastructure ranges are always blocked from sandbox egress
- notes: A hosted gVisor sandbox on Quave Direct regions at 3× the regional zCloud rate, billed by the second with no fixed fee and no compute charge while paused. A zCloud is 0.5 vCPU and 0.5 GB RAM at USD 9.50 per zCloud-month in standard regions. Sandboxes are opt-in per account. No page states the signup identity or a free sandbox route, so the verdict is paid-only and the identity kind is unverified. Connect runs the same platform on the user own cloud account for a license starting at USD 399 a month and is a separate offer.
- evidence note: the price, gVisor isolation and lifecycle facts are quoted from first-party product and docs pages read on 2026-11-25; the exact rate is a derived product of the published zCloud price and 3x multiplier; no sandbox was created and no first-party page states the signup identity or a free sandbox route
- extras:
  - shape.note: resources are per zCloud at 0.5 vCPU and 0.5 GB RAM; the sandbox size is set in the immutable template revision
  - billing_model: pay per use by the second at 3x zCloud rate
  - free_tier_kind: none
  - term: on demand, idempotent creation, idle and lifetime timeouts
  - price_arithmetic: zCloud USD 9.50 per month times 3 = USD 28.50 per zCloud-month equivalent (USD 0.039 per zCloud-hour at 730 hours)
  - derived: USD 9.50 per zCloud-month x 3 = USD 28.50 per zCloud-month equivalent; 28.50 / 730 = USD 0.039 per zCloud-hour
  - network_out.allow_outbound: yes
  - session_cap.restart_required: no
  - session_cap.note: idle timeout and maximum lifetime terminate rather than pause the sandbox
- evidence:
  - [1] 2026-11-25: Direct sandboxes are billed by the second at 3x the zCloud rate with no fixed fee, and pause is free of compute | capture: sha256:41adaa5cef6fa00b70fcf96dd17cd5d0c684f50e9e289ac9f62bdf68585bfb69 | quote: Direct: pay per use at 3× the regional zCloud rate. No platform fee.
  - [4] 2026-11-25: sandboxes are isolated gVisor environments billed at 3x the zCloud rate by the second with no fixed fee | capture: sha256:648d48a0e5e725df4e4158bf1847281070b10daf979dec68e93d67d95c58a2ec | quote: Agent Sandboxes on Direct Give your AI agents isolated gVisor sandboxes. Pay 3× the regional zCloud rate on allocated zClouds, by the second, with no fixed fee. Paused sandboxes do not accrue compute.
  - [5] 2026-11-25: the standard zCloud rate is USD 9.50 per zCloud-month and one zCloud is 0.5 vCPU and 0.5 GB RAM | capture: sha256:5e9cae828c81d754958e865dc7132325ab70007dd6f053c42804040cf789c7d2 | quote: A zCloud is 0.5 vCPU and 0.5 GB RAM.
  - [4] 2026-11-25: a Hobby account requires no credit card | capture: sha256:648d48a0e5e725df4e4158bf1847281070b10daf979dec68e93d67d95c58a2ec | quote: Yes. Create an account and use our Hobby regions to test everything. You can deploy your apps, try the MCP, and explore the platform with no credit card required.
  - [6] 2026-11-25: Hobby usage is not billed and needs no card, while the free Professional upgrade review asks for personal and business information | capture: sha256:fd0cc0331cad52d40973f5a38fbffe60d0251a32478cd708d82acf7781ed7909 | quote: Your personal LinkedIn profile link
  - [2] 2026-11-25: sandboxes are gVisor-isolated and run on Quave infrastructure | capture: sha256:143ceeed65a1b5580e1738d61f028a14fbf52fc4cacb60420fda1530c029f6bc | quote: Each sandbox runs your own container image under [gVisor](https://gvisor.dev/), with its own kernel boundary, on Quave ONE infrastructure or on your own nodes.
  - [2] 2026-11-25: the account-wide ceiling is 200 active sandboxes by default | capture: sha256:143ceeed65a1b5580e1738d61f028a14fbf52fc4cacb60420fda1530c029f6bc | quote: There is no per-app limit; only an account-wide safety ceiling (200 active sandboxes by default, raisable on request) stops a runaway loop.
  - [2] 2026-11-25: pausing releases compute with no charge and resumes the same sandbox | capture: sha256:143ceeed65a1b5580e1738d61f028a14fbf52fc4cacb60420fda1530c029f6bc | quote: Pause a sandbox to release its compute (no charge while paused) and resume it later with the same id.
  - [1] 2026-11-25: sandboxes must be enabled on the account after signup | capture: sha256:41adaa5cef6fa00b70fcf96dd17cd5d0c684f50e9e289ac9f62bdf68585bfb69 | quote: Sandboxes are enabled per account. After you sign up, ask us to turn them on.
  - [3] 2026-11-25: no extra fee for network traffic in supported regions | capture: sha256:d0de543a9590d379358ff2ec2bb4062ad30a607136092e9dc626580762d58b32 | quote: We do not charge extra fees for network traffic in our supported regions.
  - [1] 2026-11-25: the page states a per-use rate for sandboxes and no credit or allowance, so the free-unit vocabulary is none | capture: sha256:41adaa5cef6fa00b70fcf96dd17cd5d0c684f50e9e289ac9f62bdf68585bfb69 | quote: Direct: pay per use at 3× the regional zCloud rate. No platform fee.
- sources:
  - [1] https://quave.one/agent-sandboxes
  - [2] https://docs.quave.one/agent-sandboxes
  - [3] https://docs.quave.one/billing/pricing-details
  - [4] https://quave.one/solutions/direct
  - [5] https://docs.quave.one/billing/pricing
  - [6] https://docs.quave.one/verification

## Quave ONE (Direct)

- `compute/quave-one-direct` | paid-only | evidence documented | binding volume-quota | category PaaS app and sandbox compute on managed regions | tier Direct
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:52:45.909Z (live) | stale on 2026-12-27
- url https://docs.quave.one/billing/pricing
- free tier: No free zCloud allowance on Direct: zCloud compute has no included amount and runs $9.50 per zCloud-month in standard Quave regions. The separate Hobby account is unbilled and needs no credit card, but it is limited to the US-1 Hobby region for testing and evaluation. | unit: none | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: Hobby accounts are unbilled and need no card, but they are evaluation-only and cannot deploy to production regions; a Professional upgrade review is free and unlocks all regions.
- per-object cap: not applicable: the unit is an allocated zCloud (0.5 vCPU and 0.5 GB RAM), not an object; a managed local disk includes 5 GB per allocated zCloud and a managed database backup allowance is 30 GB per app environment in each region | source: [2]
- retention: Managed database backups are retained for up to 7 days by default; that 7-day window is the default automatic deletion policy, and 30 GB per app environment per region is a billing allowance rather than a shorter retention cap. | days: 7 | source: [2]
- egress: No extra charge for network traffic in supported regions: data can be transferred in and out without additional cost, but some regions cap the included outbound volume per zCloud each month (10 GB in US-5, EU-3 and EU-4; unlimited in US-3, EU-1 and EU-2). | metered: yes | free allowance: unlimited outgoing traffic in US-3, EU-1 and EU-2; 10 GB per zCloud per month in US-5, EU-3 and EU-4 | source: [2]
- identity: email | detail: A new user signs up for a user account and then creates an account to deploy. Hobby needs no credit card and is unbilled. The free Professional upgrade review asks for a personal LinkedIn profile link, a company or personal website, a short description of the business and intended use, and how the user found out about the platform.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): $9.50 per zCloud-month in standard Quave regions; each zCloud is 0.5 vCPU and 0.5 GB RAM, with no included compute amount [1]
  - volume-quota (binding): 600 build minutes per account per month, then $0.01 per extra build minute; 60 minutes cap per individual build [2]
  - volume-quota (binding): 5 GB of local disk per allocated zCloud and 30 GB of database backups per app environment per region included; extra disk $0.06 per GB-month, extra backup $0.05 per GB-month [2]
  - volume-quota (binding): 10 GB outgoing traffic per zCloud per month in US-5, EU-3 and EU-4; unlimited in US-3, EU-1 and EU-2 [2]
- limits note: A Direct sandbox is charged at 3x the regional zCloud rate on allocated zClouds, billed by the second with no minimum; paused states are not billed. Savings Plans discount zCloud compute only, not storage, builds or sandboxes.
- binding note: Compute is the meter that starts immediately on Direct: no zCloud amount is included, so the $7.50 per zCloud-month charge binds before the large-disk, backup or build overages that only unusually heavy accounts reach.
- interface detail: Public API for app environments and sandboxes, a platform dashboard with MCP access, and a CLI for source builds and deployment.
- tooling: a browser dashboard, the Quave ONE public API and MCP, and the Quave CLI; a source build is not needed when deploying a pre-built Docker image.
- composes with: Direct sandboxes are billed at 3x the regional zCloud rate by allocation, while Hobby accounts are unbilled evaluation slices; workloads needing persistent object storage pair with a separate object-storage record because managed backups are retained for 7 days by default.
- reliability: Hobby environments are stopped automatically after repeated container failures and the Hobby region is not intended for production. Regions US-3, EU-1 and EU-2 are being retired and are available only to accounts already running workloads there; legacy regions have a higher zCloud price or capped included outbound traffic.
- notes: Direct has no free compute allowance: zCloud compute is $9.50 per zCloud-month in standard regions, and a zCloud is 0.5 vCPU and 0.5 GB RAM. The separate Hobby account is unbilled with no card but is evaluation-only in US-1 Hobby. Connect is a separate paid platform license from $399/month, and sandbox compute is 3x the regional zCloud rate.
- evidence note: Rates, overages, regional outbound allowances and the account gate are first-party text quoted from the vendor's pricing, pricing-details, verification and regions pages read on 2026-11-24.
- extras:
  - connect_license: from $399/month, billed on a daily tier with a 12-month minimum contract; monthly tier prices are in the Adhesion Agreement rather than on the pricing page
  - sandbox_rate: 3x the regional zCloud rate on allocated zClouds, billed by the second with no minimum; paused states are not billed
  - free_tier_kind: evaluation-only Hobby region, unbilled, no card
  - published_shape: $7.50 per zCloud-month; 0.5 vCPU and 0.5 GB RAM per zCloud
- evidence:
  - [1] 2026-11-24: Direct zCloud compute is $7.50 per zCloud-month with no included amount in standard regions | capture: sha256:4e41f2bc6aff046adec3c81c0247a59890109d3fe76311a406e6ba92602a4b6d | quote: | zCloud compute | None; you choose the zClouds, containers, and hours you run | $7.50 per zCloud-month in standard Quave regions | Apps, databases, and services running in Quave-managed regions |
  - [1] 2026-11-24: a zCloud is 0.5 vCPU and 0.5 GB RAM | capture: sha256:4e41f2bc6aff046adec3c81c0247a59890109d3fe76311a406e6ba92602a4b6d | quote: A zCloud is 0.5 vCPU and 0.5 GB RAM.
  - [1] 2026-11-24: 600 build minutes are included monthly, with a $0.01 per-minute overage | capture: sha256:4e41f2bc6aff046adec3c81c0247a59890109d3fe76311a406e6ba92602a4b6d | quote: | Build overage | 600 build minutes per account per month | $0.01 per extra build minute | Source builds above the included minutes. Customer charging starts with August 2026 billing; July 2026 is internal preview only. |
  - [1] 2026-11-24: Connect is a separate paid platform license from $399/month | capture: sha256:4e41f2bc6aff046adec3c81c0247a59890109d3fe76311a406e6ba92602a4b6d | quote: Quave ONE Connect starts from $399/month as a platform license.
  - [2] 2026-11-24: supported regions carry no separate network traffic charge | capture: sha256:193609ffd279aa76f8473b1143203d6686b1e095ccb25bf485aa57e8f4d0d5d7 | quote: We do not charge extra fees for network traffic in our supported regions. You can transfer data in and out of your applications without incurring additional costs.
  - [2] 2026-11-24: some regions cap included outbound traffic at 10 GB per zCloud per month | capture: sha256:193609ffd279aa76f8473b1143203d6686b1e095ccb25bf485aa57e8f4d0d5d7 | quote: | US-5 | 10 GB |
  - [2] 2026-11-24: included local disk is 5 GB per allocated zCloud and 30 GB backup per app environment, with per-GB overage prices | capture: sha256:193609ffd279aa76f8473b1143203d6686b1e095ccb25bf485aa57e8f4d0d5d7 | quote: | Managed local disk | 5 GB per allocated zCloud (per replica for managed databases) | Average extra allocated GB-month | $0.06 per extra GB-month |
  - [2] 2026-11-24: managed database backups are retained up to 7 days by default | capture: sha256:193609ffd279aa76f8473b1143203d6686b1e095ccb25bf485aa57e8f4d0d5d7 | quote: We retain managed database [backups](https://docs.quave.one/deploy/storage#backups) for up to 7 days by default.
  - [3] 2026-11-24: Hobby usage is unbilled and requires no credit card | capture: sha256:fd0cc0331cad52d40973f5a38fbffe60d0251a32478cd708d82acf7781ed7909 | quote: Hobby usage is not billed, and no credit card is required.
  - [3] 2026-11-24: the free Professional upgrade review asks for a LinkedIn profile, a website, a business description and how the user found out | capture: sha256:fd0cc0331cad52d40973f5a38fbffe60d0251a32478cd708d82acf7781ed7909 | quote: Your personal LinkedIn profile link
  - [4] 2026-11-24: US-1 Hobby is the only region available to Hobby accounts and production regions require Professional | capture: sha256:a3f90734dab8bd273a35e95c0e1d27046063d682b3bb12a121e2ca151fb115f4 | quote: Hobby accounts:
  - [1] 2026-11-25: the pricing page lists zCloud compute at USD 9.50 per zCloud-month in standard regions | capture: sha256:5e9cae828c81d754958e865dc7132325ab70007dd6f053c42804040cf789c7d2 | quote: $9.50 per zCloud-month in standard Quave regions
  - [1] 2026-11-25: the pricing page was read again on 2026-11-25 and lists zCloud compute at USD 9.50 per zCloud-month | capture: sha256:5e9cae828c81d754958e865dc7132325ab70007dd6f053c42804040cf789c7d2 | quote: $9.50 per zCloud-month in standard Quave regions
- sources:
  - [1] https://docs.quave.one/billing/pricing
  - [2] https://docs.quave.one/billing/pricing-details
  - [3] https://docs.quave.one/verification
  - [4] https://docs.quave.one/regions/
