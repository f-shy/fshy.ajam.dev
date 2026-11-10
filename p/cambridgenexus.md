# CambridgeNexus

> cambridgenexus.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cambridgenexus/ | JSON https://fshy.ajam.dev/api/v1/entity/cambridgenexus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CambridgeNexus

- `compute/cambridgenexus` | paid-only | evidence documented | binding write-gated | category bare-metal GPU rack lease
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T07:36:21.177Z (live) | stale on 2026-12-04
- url https://cambridgenexus.com/pricing
- free tier: no free tier, no trial and no published rate: whole NVIDIA GB300 NVL72 racks and B300 systems leased single tenant on terms from 6 months up to 5+ years, quoted per request | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the unit is a whole rack or a whole server leased under contract
- retention: not applicable: the unit is a leased rack, not stored bytes | source: [1] | note: terms run from 6 months up to 5+ years
- egress: no egress price is published; the networking layer is described as 'Up to 400 Gbps external connectivity.' | metered: no | source: [2]
- identity: institution | detail: Every deployment passes KYC and technical qualification before capacity is confirmed, and the request form asks for the rack count, the term, the location and the workload requirements. The buyer is an enterprise leasing whole racks; no individual sign-up path was read.
- interface: unknown
- limits:
  - write-gated (binding): no self-serve purchase and no trial: a request goes through a contact form, then technical qualification and KYC, then a quote; racks are leased whole on terms from 6 months [1]
- limits note: the quote step and the contract term are the entry gate; the page gives no hourly rate for any card
- binding note: capacity is quote-gated: the vendor states a list price would be misleading and quotes against rack count, term, booking timeline and downpayment, after KYC and technical qualification
- interface detail: whole bare-metal racks under contract; no client API was read
- tooling: not stated: the vendor operates the rack end to end and the page names no client tooling
- composes with: none: a quote-gated lease of whole racks cannot be chained with a free lane.
- reliability: no reliability event was observed on the pages read and no status page was read
- notes: Neither the vendor pricing page nor the aggregator lists an hourly rate for an H100, A100 80 GB, L40S, RTX 4090 or L4: the vendor leases GB300 NVL72 racks and B300 systems only.
- evidence:
  - [3] 2026-11-03: the aggregator lists no hourly rate for any card; it states the provider publishes no public hourly pricing | capture: sha256:47c793d72e0e7adbde939516746724c539a931eb43d4f325af8e601890f22860 | quote: CambridgeNexus does not publish public hourly pricing.
  - [1] 2026-11-03: the vendor gives no list price | capture: sha256:3f7b357edb92cb4809c27d32a64817fcc938f108b6e619013b37c5872b0e0d03 | quote: so a list price would be misleading
  - [1] 2026-11-03: the rate is quoted per request against rack count, term, timeline and downpayment | capture: sha256:3f7b357edb92cb4809c27d32a64817fcc938f108b6e619013b37c5872b0e0d03 | quote: The rate depends on rack count, contract term, booking timeline, and downpayment
  - [1] 2026-11-03: no trial capacity is offered | capture: sha256:3f7b357edb92cb4809c27d32a64817fcc938f108b6e619013b37c5872b0e0d03 | quote: trial capacity on GB300 NVL72 is not offered by any operator in this market
  - [1] 2026-11-03: lease terms run from 6 months up to 5+ years | capture: sha256:3f7b357edb92cb4809c27d32a64817fcc938f108b6e619013b37c5872b0e0d03 | quote: Terms from 6 months up to 5+ years.
  - [1] 2026-11-03: the request form asks for rack count, term, location and workload requirements | capture: sha256:3f7b357edb92cb4809c27d32a64817fcc938f108b6e619013b37c5872b0e0d03 | quote: Tell us the rack count, the term, location, and your workload requirements.
  - [2] 2026-11-03: KYC and technical qualification precede every deployment | capture: sha256:c89d0d702d247f695c207580398ce1d8f63ec6fbe5c5a48294db09219ef61dc9 | quote: Every deployment passes KYC and technical qualification before capacity is confirmed.
  - [2] 2026-11-03: the offer is bare-metal single-tenant GB300 NVL72 racks | capture: sha256:c89d0d702d247f695c207580398ce1d8f63ec6fbe5c5a48294db09219ef61dc9 | quote: Bare-metal, single-tenant GB300 NVL72 racks, owned and run by CambridgeNexus.
  - [2] 2026-11-03: external connectivity is up to 400 Gbps | capture: sha256:c89d0d702d247f695c207580398ce1d8f63ec6fbe5c5a48294db09219ef61dc9 | quote: Up to 400 Gbps external connectivity.
- sources:
  - [1] https://cambridgenexus.com/pricing
  - [2] https://cambridgenexus.com/
  - [3] https://computeprices.com/providers/cambridgenexus
