# Synteq

> gpurentalprices.com | Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpurentalprices/ | JSON https://fshy.ajam.dev/api/v1/entity/gpurentalprices.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hot Aisle

- `compute/hot-aisle` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:28.017Z (live) | stale on 2026-12-04
- url https://gpurentalprices.com/providers/hotaisle
- free tier: AMD-only GPU host: the pricing page lists none of H100, A100 80 GB, L40S, RTX 4090 or L4. MI300X virtual machines (1, 2 and 4 GPUs) are USD 2.99 per GPU-hour and 8x MI300X bare metal is USD 3.39 per GPU-hour, billed by the minute; the page names no pricing tier and states no minimum bill. Credits are added to a team before compute is provisioned. A third-party tracker reports a minimum rental of one GPU for one minute and prepaid credits bought by card through Stripe or in USDT and USDC (checked 2026-10-17). | unit: hours | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not stated | metered: no | source: [2]
- identity: email | detail: The vendor's quick-start page signs a user in with an email address and a verification code sent to it, then credits are added to a team before compute is provisioned. Prepaid credits rather than a subscription, and a third-party tracker records payment by card or by USDT and USDC, so a stablecoin balance is an alternative to a card.
- interface: unknown
- limits note: Nothing published binds above a single GPU for a single minute; the whole cost is prepaid and the smallest unit is one minute.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The one-minute minimum and per-minute billing make this the only 192 GB card among evaluated providers sold in units a benchmark can afford, which is what a trial run needs before a multi-hour commitment.
- reliability: no reliability event recorded
- notes: Every figure here is reported by the tracker, not read on the vendor's own page: hotaisle.xyz/pricing was unverified on 2026-11-03, so the rung is reported and the vendor page is the check that would raise it. Storage price, data-out price and the rule for stopped instances are stated by the tracker as unpublished by the vendor, which matters because a 192 GB card implies a large dataset beside it.
- extras:
  - facets.class: gpu-broker-rate-floor
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: MI300X
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 192
- evidence:
  - [2] 2026-10-22: quoted: 'Hot Aisle rents 1 GPU model today, from $2.99 an hour (MI300X, on-demand)'; source of the rate given as hotaisle.xyz/pricing
  - [2] 2026-10-22: quoted billing terms: 'Billing is per minute', 'Minimum rental time: one GPU for one minute', 'prepaid credits by card (Stripe) or USDT and USDC', each checked on 2026-10-17
  - [3] 2026-10-22: MI300X market median across 5 providers is USD 2.99/hr, so Hot Aisle matches the median rather than undercutting it
  - [1] 2026-11-03: the vendor pricing page lists MI300X VMs at USD 2.99 per GPU-hour billed by the minute; its table lists no H100, A100, L40S, RTX 4090 or L4 | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 1, 2, and 4x MI300X VMs, billed by the minute.
  - [1] 2026-11-03: the rate and the per-minute billing are read on the vendor's page | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 1, 2, and 4x MI300X VMs, billed by the minute.
  - [1] 2026-11-03: the vendor pricing page was read on this date | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 1, 2, and 4x MI300X VMs, billed by the minute.
  - [1] 2026-11-03: the rate and the billing granularity are first-party | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 1, 2, and 4x MI300X VMs, billed by the minute.
  - [4] 2026-11-03: sign-in is by email address and a verification code | capture: sha256:5796e24b4f73ebfde24d3cfea610866238a1ee2fbaf6bbdf0ed40114fbe204b5 | quote: You can always sign in again with your email address and the verification code we send you.
  - [1] 2026-11-03: 8x MI300X bare metal is also billed by the minute, at USD 3.39 per GPU-hour | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: Dedicated full-node access, billed by the minute.
  - [1] 2026-11-03: the 8x bare-metal rate is USD 3.39 per GPU-hour | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 8x bare metal $3.39/GPU/hr
  - [1] 2026-11-03: the vendor pricing page confirms the MI300X VM rate and per-minute billing | capture: sha256:140e661e7a9f313397849b71e9cfae1918d1f044a49ddb6177b1feef795adba6 | quote: 1, 2, and 4x MI300X VMs, billed by the minute.
- sources:
  - [1] https://hotaisle.xyz/pricing
  - [2] https://gpurentalprices.com/providers/hotaisle
  - [3] https://gpurentalprices.com/mi300x
  - [4] https://hotaisle.xyz/quick-start

## Prime Intellect Marketplace

- `compute/prime-intellect-marketplace` | paid-only | evidence reported | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://gpurentalprices.com/providers/primeintellect
- free tier: Marketplace lane of Prime Intellect, priced per GPU-hour: H200 141GB at USD 3.14, B200 180GB at USD 3.49, B300 288GB at USD 4.99, and spot or interruptible H100 at USD 0.94, which is the cheapest H100 hour recorded anywhere among documented hosts. Prices checked 2026-10-22. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: Unchanged from the existing record: the platform uses prepaid credits, and the grant programme that once existed is gone.
- interface: unknown
- limits:
  - volume-quota (binding): Prepaid credits are the ceiling: the existing record quotes the documentation, credits are deducted every minute while a Pod is active and Pods stop when credits run out, so the balance is what limits a run. [1]
- limits note: Prepaid credits are the ceiling: the existing record quotes the documentation, credits are deducted every minute while a Pod is active and Pods stop when credits run out, so the balance is what limits a run.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 0.94 for an interruptible H100 hour is half the cheapest on-demand H100 in the same market, so a checkpointing run that tolerates preemption gets two H100 hours for the price of one anywhere else among documented hosts.
- reliability: no reliability event recorded
- notes: Extends the existing prime-intellect.json record, which covers the sandbox pricing only, and prime-intellect-2.json, which records the grant programme as dead. The marketplace rates are third-party reported and the vendor pricing page answered 404 on 2026-10-22, so the rung is reported. A spot rate is not a supply guarantee: the tracker labels it spot, and the existing record's note that Pods stop when credits run out is the practical limit.
- extras:
  - facets.class: gpu-marketplace
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 80
- evidence:
  - [1] 2026-10-22: the tracker names Prime Intellect as the spot floor for H100 at USD 0.94 per GPU-hour and as the on-demand floor for H200 at USD 3.14, B200 at USD 3.49 and B300 at USD 4.99
  - [2] 2026-10-22: quoted: 'Spot from $0.94 (Prime Intellect)' and 'Cheapest on-demand H100 today: $1.80/hr at HyperAI' with the H100 median at USD 3.29
- sources:
  - [1] https://gpurentalprices.com/providers/primeintellect
  - [2] https://gpurentalprices.com/

## SaladCloud community floor

- `compute/saladcloud-community-floor` | paid-only | evidence reported | binding retention-clamped | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:33.435Z (live) | stale on 2026-11-18
- url https://gpurentalprices.com/providers/salad
- free tier: Lowest-priority (batch, most interruptible) price per GPU-hour on the vendor pricing page, read 2026-11-03: RTX 3090 24 GB USD 0.090, RTX 4090 24 GB USD 0.160 and RTX 5090 32 GB USD 0.250; the RTX 4090 costs USD 0.253 at Low, 0.347 at Medium and 0.440 at High priority. Billing is per second while the instance runs. The page lists no L40S, H100, A100 or L4. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: Community nodes are the lowest priority tier and are preempted by higher-priority workloads, so a job that must run to completion cannot rely on holding the card. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: Unchanged from the existing record: an account, with no free trial and no minimum commitment quoted from the vendor FAQ.
- interface: unknown
- limits:
  - retention-clamped (binding): Community nodes are the lowest priority tier and are preempted by higher-priority workloads, so a job that must run to completion cannot rely on holding the card. [1]
- limits note: Community nodes are the lowest priority tier and are preempted by higher-priority workloads, so a job that must run to completion cannot rely on holding the card.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At USD 0.09 a 3090-hour, USD 10 buys 111 hours on a 24 GB card, which is the cheapest way among documented hosts to run a long checkpointed fine-tune; the preemption risk is what the discount pays for.
- reliability: no reliability event recorded
- notes: The vendor pricing page lists the per-class table by priority tier. The figures in the free-tier text are its Lowest tier and match the third-party tracker rows for the RTX 3090 (USD 0.09), RTX 4090 (USD 0.16) and RTX 5090 (USD 0.25). The USD 0.015 per GPU-hour headline applies to classes below the table, such as the RTX 3060, at Lowest priority.
- extras:
  - facets.class: gpu-marketplace
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 3090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [2] 2026-10-22: quoted: RTX 3090 spot or marketplace from USD 0.09 'community, SaladCloud' across 3 providers
  - [3] 2026-10-22: quoted: RTX 4090 spot or marketplace from USD 0.16 'community, SaladCloud'
  - [4] 2026-10-22: quoted: RTX 5090 spot or marketplace from USD 0.25 'community, SaladCloud', down 12.8 percent in 7 days
  - [5] 2026-10-22: quoted page text: four priority tiers where 'Higher priority can take over lower-priority workloads', and 'Lowest is the lowest cost and the most interruptible'
  - [6] 2026-11-03: the RTX 4090 is USD 0.160 at the Lowest tier and 0.253, 0.347, 0.440 at Low, Medium and High | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: | RTX 4090 | 24 GB | $0.440 | $0.347 | $0.253 | $0.160 | $116.80 |
  - [6] 2026-11-03: the RTX 3090 24 GB is USD 0.090 per GPU-hour at the Lowest tier | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: | RTX 3090 | 24 GB | $0.200 | $0.163 | $0.127 | $0.090 | $65.70 |
  - [6] 2026-11-03: the RTX 5090 32 GB is USD 0.250 per GPU-hour at the Lowest tier | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: | RTX 5090 | 32 GB | $0.600 | $0.483 | $0.367 | $0.250 | $182.50 |
  - [6] 2026-11-03: billing is per second while an instance runs | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: Billing is per second while an instance is in the running state.
  - [6] 2026-11-03: the USD 0.015 headline applies to classes outside the table at Lowest priority | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: Additional classes (RTX 3060, RTX 3070, RTX 3070 Ti, and others) are available in the portal from $0.015 per GPU-hour at Lowest priority.
  - [1] 2026-11-03: the tracker lists the RTX 4090 at USD 0.16 on the community tier, lowest priority, interruptible, checked 2 November 2026 | capture: sha256:3e56aaa7203b18229c79bd729533260f91677ce5b7abcf0c66d41c9a25429747 | quote: | [RTX 4090](https://gpurentalprices.com/rtx-4090) · [SaladCloud](https://gpurentalprices.com/providers/salad)24 GB | community cloudlowest priority, interruptible | $0.16 | – | [Rent →](https://salad.com/)checked 2 NovDetailsChecked2 November 2026Add to shortlist
  - [6] 2026-11-03: the RTX 3090 is USD 0.090 at the Lowest tier | capture: sha256:6518f404333125ae0cea16a10827162bbdce018d02eac2fdd91f2a81909c9c3e | quote: | RTX 3090 | 24 GB | $0.200 | $0.163 | $0.127 | $0.090 | $65.70 |
- sources:
  - [1] https://gpurentalprices.com/providers/salad
  - [2] https://gpurentalprices.com/rtx-3090
  - [3] https://gpurentalprices.com/rtx-4090
  - [4] https://gpurentalprices.com/rtx-5090
  - [5] https://salad.com/pricing
  - [6] https://salad.com/pricing/

## Synteq

- `compute/synteq` | paid-only | evidence reported | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:50:35.126Z (live) | stale on 2026-11-18
- url https://gpurentalprices.com/providers/synteq
- free tier: no free tier. The vendor catalogue lists five GPU plans, every one with in_stock false: Intel Arc Pro A40 $45 a month, NVIDIA RTX PRO 4000 $185, RTX PRO 5000 $450, RTX PRO 6000 $885 and B300 $4555. H100, A100 80 GB, L40S, RTX 4090 and L4 are not listed. The price index divides $185 a month by 730 hours to USD 0.25 per GPU-hour for the RTX PRO 4000, which is not a published hourly rate. The vendor GPU page lists bare-metal servers from $1545 a month (8 x RTX Pro 4000) and $1785 a month (2 x RTX PRO 6000). Block storage is USD 4 per TB per month, bandwidth is included on every plan, billing is prepaid monthly with a one-month minimum rental, and cancelling gives no partial refund | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'None of these listed configurations is reported in stock'; and the terms 'Billing is monthly, prepaid', 'Minimum rental time: 1 month; cancelling gives no partial refund', 'Data out: bandwidth included on every plan' | metered: no | source: [1]
- identity: card | detail: The first month is paid up front and the tracker records no free tier.
- interface: unknown
- limits:
  - write-gated (binding): A one-month prepaid commitment with no partial refund is the binding term: a cancelled month is a lost month, and none of the five GPU plans in the vendor catalogue was in stock on the day checked. [1]
- limits note: A one-month prepaid commitment with no partial refund is the binding term: a cancelled month is a lost month, and none of the four configurations was in stock on the day checked.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A USD 185 month with bandwidth included is a fixed-cost way to hold one card continuously, but LeaderGPU's USD 140 month for a 3090 is cheaper and this is a commitment, so it only composes with a workload that runs for most of 730 hours.
- reliability: no reliability event recorded
- notes: Supply is the finding and it is explicit: zero in stock. The USD 0.25 per hour is the tracker's division of a monthly price, not a published hourly rate, and a month used for 100 hours costs USD 1.85 per hour on the same invoice.
- extras:
  - facets.class: committed-gpu-host
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX PRO 4000 Blackwell
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: quoted: 'Synteq rents 4 GPU models today, from $0.25 an hour (RTX PRO 4000 Blackwell, reserved / committed, 1 month, $185/month divided by 730 hours; monthly billing, out of stock)'
  - [1] 2026-10-22: quoted: 'None of these listed configurations is reported in stock'; and the terms 'Billing is monthly, prepaid', 'Minimum rental time: 1 month; cancelling gives no partial refund', 'Data out: bandwidth included on every plan'
  - [2] 2026-10-22: the tracker names this endpoint as the source of the catalogue it reads, which is the machine-readable way to re-check availability later
  - [2] 2026-11-03: the RTX PRO 4000 GPU plan is $185 a month | capture: sha256:2400d7668944c46be94341f104b2b925ce3b7ce19a9991cf3db03212a35ab668 | quote: "name":"NVIDIA RTX PRO 4000","kind":"gpu_cloud","category":"gpu_cloud","cpu_cores":8,"ram_gb":24,"disk_gb":240,"monthly_price":185
  - [2] 2026-11-03: the B300 plan is in the catalogue | capture: sha256:2400d7668944c46be94341f104b2b925ce3b7ce19a9991cf3db03212a35ab668 | quote: "name":"NVIDIA B300","kind":"gpu_cloud"
  - [3] 2026-11-03: bare-metal 8-GPU RTX Pro 4000 servers start at $1545 a month | capture: sha256:1fad43fec94137061264527767fa6d2c0649c90289487df8bac91ed6c9378645 | quote: (8) NVIDIA RTX Pro 4000 (2) AMD EPYC 128GB+ SSDs or NVMe 100TB @ 10Gbps Starting at $1545/mo
  - [4] 2026-11-03: billing is prepaid monthly and a cancelled resource runs to period end | capture: sha256:11d9178aebea117635b6b7e3c8d10293a3516be5bf812ccd3b108793f97faeb4 | quote: Synteq bills resources prepaid monthly: you pay for a month up front, and the resource runs to the end of that period before it's destroyed when you cancel.
  - [1] 2026-11-03: the price index reports none of the listed configurations in stock | capture: sha256:41527bf503e39bfeb86c0b50ba68914677c05aaea51dfcd80110800fb67bcf02 | quote: None of these listed configurations is reported in stock.
  - [2] 2026-11-03: the catalogue lists the GPU plans | capture: sha256:2400d7668944c46be94341f104b2b925ce3b7ce19a9991cf3db03212a35ab668 | quote: "slug":"nvidia-b300","name":"NVIDIA B300"
- sources:
  - [1] https://gpurentalprices.com/providers/synteq
  - [2] https://synteq.com/api/catalog/vps
  - [3] https://synteq.com/gpu
  - [4] https://cloud.synteq.com/docs/refund-eligibility
