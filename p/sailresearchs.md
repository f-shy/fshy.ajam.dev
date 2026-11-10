# Sailboxes

> sailresearchs.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sailresearchs/ | JSON https://fshy.ajam.dev/api/v1/entity/sailresearchs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sailboxes

- `compute/sailboxes` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier pay-as-you-go, 1 vCPU / 1 GiB, active metering
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:16.353Z (live) | stale on 2026-12-05
- url https://sailresearchs.com/sailboxes
- price parsed USD 16.79/mo
- free tier: A USD 5 monthly credit is advertised when a payment method is attached (aggregator); the vendor page read states no free allowance. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit, and it requires a payment method
- per-object cap: sandbox sizes S, M and L with a per-creation fee on the free plan (USD 0.005 / 0.01 / 0.012); the per-size ceilings were not readable first party
- retention: Independent disks and persistent state; volume storage is billed at USD 0.000411/GiB-hour and is charged even while the attached Sailbox sleeps. | source: [2]
- egress: No egress price and no transfer allowance are published on the page read; metered is recorded as false because nothing is known to be charged per gigabyte, which is an absence of evidence, not a promise of free traffic. | metered: no | free allowance: not stated | source: [2]
- identity: card | detail: The USD 5 monthly credit is attached to a payment method per the aggregator's plan table; the vendor marketing page states no payment terms. Card type and hold unverified.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): USD 0.015 per active vCPU-hour and USD 0.008 per active GB-hour; a free-plan creation fee of USD 0.005 to USD 0.012 [2]
- limits note: The smallest Sailbox holds 16 GiB of RAM, and RAM bills whether or not it is touched, so the floor is USD 0.128 per hour before a single vCPU-second is used; USD 5 of monthly credit buys about 39 hours of that.
- binding note: Active-CPU metering is the wall in both directions: a busy box costs USD 16.79 a month, and the disk keeps billing even while the box sleeps.
- interface detail: HTTPS API at sailbox-api.sailresearch.com, SDKs (Python, TypeScript), the sail CLI and SSH to devboxes
- tooling: the `sail` CLI, the Python SDK (`import sail`) and the TypeScript SDK `@sailresearch/sdk`, all built on the public HTTPS API
- composes with: A Sailbox is a full VM that never has to be torn down: the sleeping state is free, so a long-horizon agent keeps its filesystem, packages and running processes across days and pays only for the seconds it works. Pairing the USD 5 monthly credit with a sleeping box converts the credit into about 39 hours of active compute a month, which is an hour and a quarter a day.
- reliability: In-flight work survives pause and resume, and open connections survive for up to 10 minutes.
- notes: Arithmetic at 1 vCPU / 1 GiB fully active for 730 h: 0.015 x 730 = USD 10.95 + 0.008 x 730 = USD 5.84 = USD 16.79. The metering is on ACTIVE CPU, so a mostly idle box is cheaper: at 5% average CPU the compute line is USD 0.55 and the memory line USD 5.84, which is USD 6.39 and still over the line because memory is charged while the box runs. This is the provider whose pricing model most rewards idling, and it still cannot reach USD 5 at 1 GiB. The 'no runtime limits' claim is the vendor's own and was not tested.
- evidence note: The full-VM description, 'no runtime limits', root access and the two active rates are quoted from the vendor's own page read. Volume storage and the plan/credit table come from the vendor docs and an aggregator respectively, and are marked in notes.
- extras:
  - facets.class: updates-existing-record
  - facets.free_tier_kind: recurring-credit
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 16
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - billing_model: per-second
  - term: usage, no commitment
  - m10h_usd: 6.9
  - m24h_usd: 16.79
  - price_arithmetic: (0.015 + 0.008) = USD 0.023/hour at full activity x 730 h = USD 16.79; x 300 h = USD 6.90. At 5% average CPU the compute line falls to USD 0.55 and the total to USD 6.39. Volume storage adds 0.000411/GiB-hour = USD 0.30/GiB-month.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.ports: not stated on the marketing page
  - session_cap.restart_required: no
  - session_cap.note: 'No runtime limits' per the vendor
- evidence:
  - [3] 2026-10-22: USD 0.015 per used vCPU-hour, USD 0.008 per GiB-hour of RAM, USD 0.0007 per GiB-hour of NVMe, USD 0.000411 per GiB-hour of volume storage, creation fees USD 0.005 to USD 0.012 on Free and waived on Pro
  - [4] 2026-10-22: sizes: s is 1 vCPU with 16 GiB (up to 64 GiB), m is 4 vCPU with 32 GiB (up to 128 GiB), l is 8 vCPU with 64 GiB (up to 256 GiB), m is the default; you are charged only for observed usage, so a 4 vCPU ceiling using 0.01 vCPU bills 0.01 vCPU
  - [4] 2026-10-22: 'Sleeping, paused, checkpointing, and cold-starting time is not billed'; when credits run out Sail pauses running and sleeping Sailboxes and blocks creation, resume and run, and nothing is terminated
  - [5] 2026-10-22: '$5 in free credits every month when you attach a payment method' and 'Get started with $5 free credit'
  - [6] 2026-10-22: 'Full VMs that can run for infinite time, only bill for actively used resources'
  - [2] 2026-10-24: quoted: 'A full, kernel-isolated Linux VM with root access. Independent disks, persistent state, Docker support, and local NVMe.'; 'No runtime limits. Agents can live for days, weeks, or forever without losing state.'
  - [2] 2026-10-24: quoted table: 'Sail | $0.015 active vCPU·h | $0.008 active GB·h'
  - [3] 2026-10-24: reported via search index of the vendor docs: 'Volume storage (GiB)/hour $0.000411' and 'Volume storage is billed separately for each hour the volume exists, even when attached Sailboxes are sleeping, until it's deleted.'
  - [7] 2026-11-03: Sailboxes accept SSH | capture: sha256:7ec5cea0b6dbb4851fd1398de5ceef0b11946b1c6b7fb90b23e3cc9d38601e4c | quote: * sets up SSH, so your editor and other SSH tools can connect;
  - [8] 2026-11-03: a REST API exists | capture: sha256:456ceaaa16df2bd346c15a4310a7c50f6dc8d5e8976aab5017c5c1e543542d24 | quote: Sailboxes have a public HTTPS API.
  - [3] 2026-11-03: the rate table lists vCPU, RAM, NVMe, volume and creation charges and no transfer or egress dimension | capture: sha256:1177c514afdae86260156c4bd616f39776fedb5c3a58d9351d4f71a00fddfc3b | quote: Volume storage is billed separately for each hour the volume exists, even
  - [9] 2026-11-04: the TypeScript SDK is @sailresearch/sdk; the same page shows a Python import sail | capture: sha256:8839467e0806b805df3453201dcae1b12f12d03af90f69bb77e604a09c1607bb | quote: import { App, Sailbox } from "@sailresearch/sdk";
  - [8] 2026-11-04: the HTTPS API underlies the SDKs and the CLI | capture: sha256:456ceaaa16df2bd346c15a4310a7c50f6dc8d5e8976aab5017c5c1e543542d24 | quote: Sailboxes have a public HTTPS API. The SDKs and the CLI are built on it
- sources:
  - [1] https://boxyard.dev/providers/sail/pricing
  - [2] https://sailresearchs.com/sailboxes
  - [3] https://docs.sailresearch.com/sailboxes-pricing
  - [4] https://docs.sailresearch.com/sailboxes-billing
  - [5] https://sailresearch.com/
  - [6] https://app.sailresearch.com/sign-up
  - [7] https://docs.sailresearch.com/sailboxes-devboxes
  - [8] https://docs.sailresearch.com/sailboxes-http-api
  - [9] https://docs.sailresearch.com/sailbox-sdk.md
