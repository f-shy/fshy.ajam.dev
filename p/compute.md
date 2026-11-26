# Compute Cheap

> compute.cheap | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/compute/ | JSON https://fshy.ajam.dev/api/v1/entity/compute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Compute Cheap

- `compute/compute-cheap` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card unknown, phone no, ID no, institution no | verified 2026-11-06T18:41:34.657Z (live) | stale on 2026-12-07
- url https://compute.cheap/
- free tier: no free tier and no pay-as-you-go: reserved H100, H200 and B300 blocks held for a start date the buyer chooses, the H100 SXM 80GB at USD 4.29/hr, with a minimum reservation of 2,000 GPU-hours and 50% prepaid at the quoted rate | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the block size: a minimum of 2,000 GPU-hours
- retention: not applicable: the unit is a reserved block of GPU-hours, not stored bytes | source: [2] | note: each block is held at a fixed rate until it ends
- egress: not stated on the pages read: no egress term was found, so nothing is asserted | metered: no | source: [2]
- identity: email | detail: The reservation form asks for a work email to send the quote to; name, company and notes are optional. After availability is confirmed 50% is prepaid at the quoted rate. What payment method the prepayment takes is unverified: behind a sign-up.
- interface: unknown
- limits:
  - write-gated (binding): no self-serve provisioning: a reservation is requested through a form, availability is confirmed first, 50% is prepaid at the quoted rate, and the minimum is 2,000 GPU-hours [1]
- limits note: the 2,000 GPU-hour minimum and the quote step are the entry gate; the H100 rate is a reserved rate, not an on-demand one
- binding note: capacity is quote-gated: a form request, a confirmation of availability, a 50% prepayment and a 2,000 GPU-hour minimum stand between a person and a running GPU
- interface detail: capacity is requested through a web form and confirmed by a quote; no access interface to a running GPU was read
- tooling: a web request form; the site also publishes a pricing API and a leaderboard of GPU prices, which are price data and not a way to provision
- composes with: none: a quote-gated reservation cannot be chained with a free lane.
- reliability: blocks are stated as reserved and non-preemptible, held at a fixed rate until the block ends; the vendor page offers no interruptible capacity to new requests
- notes: The vendor page read on 2026-11-06 prices H100 SXM 80GB at USD 4.29/hr, H200 SXM 141GB at USD 5.19/hr and B300 SXM 288GB at USD 6.71/hr as reserved blocks, and lists no B200, A100, L40S, RTX 4090 or L4. The 2,000 GPU-hour minimum at the H100 rate is a USD 8,580 commitment. The aggregator computeprices.com lists H100 at USD 1.38/hr as Spot, collected 2026-10-30, which is below the reserved rate on the vendor page and is not an offer that page makes today.
- evidence:
  - [1] 2026-11-03: the H100 SXM 80GB reserved rate is USD 4.29/hr on the vendor request page read on 2026-11-03 | capture: sha256:8cac7494351199bed25c825cd573c40a9b24b6654116ce6b723cf2f3e03de023 | quote: ReservedHeld for you, not preemptible$4.29/hr
  - [1] 2026-11-03: the minimum reservation is 2,000 GPU-hours | capture: sha256:8cac7494351199bed25c825cd573c40a9b24b6654116ce6b723cf2f3e03de023 | quote: Minimum reservation: 2,000 GPU-hours
  - [1] 2026-11-03: the request form asks for a work email | capture: sha256:8cac7494351199bed25c825cd573c40a9b24b6654116ce6b723cf2f3e03de023 | quote: Work email
  - [1] 2026-11-03: name and company are optional on the request form | capture: sha256:8cac7494351199bed25c825cd573c40a9b24b6654116ce6b723cf2f3e03de023 | quote: Add your name or company (optional)
  - [2] 2026-11-03: the offer is reserved prepaid blocks, not instant or pay-as-you-go | capture: sha256:bebb2e732ee466ed723ce9630192ea078813adaac1279deacb96404b47f61eac | quote: Prepaid H100, H200, and B300 blocks in the US and EU, held for a start date you choose. Not instant, not pay-as-you-go.
  - [2] 2026-11-03: 50% is prepaid at the quoted rate | capture: sha256:bebb2e732ee466ed723ce9630192ea078813adaac1279deacb96404b47f61eac | quote: You prepay 50% at the quoted rate, and your block is booked.
  - [2] 2026-11-03: blocks are non-preemptible at a fixed rate | capture: sha256:bebb2e732ee466ed723ce9630192ea078813adaac1279deacb96404b47f61eac | quote: Every block is reserved and non-preemptible: it is held for you at a fixed rate until it ends.
  - [2] 2026-11-03: no interruptible capacity is offered to new requests | capture: sha256:bebb2e732ee466ed723ce9630192ea078813adaac1279deacb96404b47f61eac | quote: Interruptible capacity is not offered to new requests.
  - [3] 2026-11-03: the aggregator lists a spot H100 SXM at USD 1.38/hr collected 2026-10-30, which the vendor page read on 2026-11-03 no longer offers | capture: sha256:ad1379acdfd8c05efda2bab5596d9d2e629b58112ff1745e8ca17a6cb25472c9 | quote: | [H100 SXM](https://computeprices.com/providers/compute/gpus/h100) | $1.38/hrSpotUS and EU | 80GB | 1× | 10/30/2026 |
  - [1] 2026-11-06: the H100 SXM 80GB reserved rate is USD 4.29 per hour and B200 is no longer offered on the page | capture: sha256:5965252a9bf5e6d9aa544a86fefb48ab1671f094f23df926aa0fb5659e8b6047 | quote: ReservedHeld for you, not preemptible$4.29/hr
  - [1] 2026-11-06: the minimum reservation is still 2,000 GPU-hours, so the entry gate is unchanged | capture: sha256:5965252a9bf5e6d9aa544a86fefb48ab1671f094f23df926aa0fb5659e8b6047 | quote: Minimum reservation: 2,000 GPU-hours
- sources:
  - [1] https://compute.cheap/request-compute
  - [2] https://compute.cheap/
  - [3] https://computeprices.com/providers/compute
