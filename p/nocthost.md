# NoctHost

> nocthost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nocthost/ | JSON https://fshy.ajam.dev/api/v1/entity/nocthost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NoctHost

- `compute/nocthost-gpu` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://nocthost.com/gpu-vps
- free tier: no free tier is published; GPU VPS by the hour from a prepaid balance: fractional A16 from USD 0.085 an hour for 2 GB of VRAM, A16 16 GB USD 0.658, RTX 4000 Ada 20 GB USD 0.726, A40 48 GB USD 2.40. None of H100, A100, L40S, RTX 4090 or L4 is listed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: cards are allocated on Vultr and other providers behind the one NoctHost account
- per-object cap: not applicable | source: [1] | note: sizes run from 2 GB to 192 GB of VRAM
- retention: a GPU server is deleted, not archived, if the balance reaches zero | source: [1] | note: regular servers are snapshotted first; a GPU machine is not
- egress: traffic beyond the included amount is billed at USD 0.01 per GB from the balance | metered: yes | free allowance: an included amount that depends on the size | source: [2]
- identity: email | detail: The FAQ answers 'An email address is all you need to register.' with no documents, selfies or phone numbers; a crypto top-up needs nothing else. Cards are also accepted by a payment partner that asks for billing details.
- interface: rest, ssh
- limits:
  - write-gated (binding): a server is deployed from a prepaid balance; top-ups are final, with USDT from USD 5, other coins from USD 20 and cards from USD 20 [3]
- limits note: Deployment is gated on a prepaid, non-refundable balance.
- binding note: the same as limits note
- interface detail: taken from the API page, which says the platform is an email address and a REST API away, and the GPU page, which gives root over SSH; not probed
- tooling: REST API with register, balance, deploy, poll and destroy steps; root over SSH with a dedicated IPv4; the NVIDIA driver preinstalled
- composes with: Crypto or card top-up with an email-only account, deployed hourly across 33 cities through one API; the GPU cards are hourly-billed sizes of A16, A40 and RTX 4000 Ada.
- reliability: A GPU server is deleted when the balance reaches zero and its disk is not kept; a low-balance warning is sent by email beforehand.
- notes: Found via computeprices.com (provider slug nocthost). An existing record, compute/tothost, is a different vendor. The cheapest fractional A16 slice is below the aggregator's USD 0.658 row.
- evidence:
  - [1] 2026-11-03: A40 48 GB is USD 2.40 an hour | capture: sha256:9717df840705663b3fcf2336f717bdd84d5c492948fe850b3d6ec65dfecabf70 | quote: | A40 · 48 GB VRAM | 24 | 120 GB | 1400 GB | $1750 | $2.40 |
  - [1] 2026-11-03: RTX 4000 Ada 20 GB is USD 0.726 an hour | capture: sha256:9717df840705663b3fcf2336f717bdd84d5c492948fe850b3d6ec65dfecabf70 | quote: | RTX4000 ADA · 20 GB VRAM | 4 | 16 GB | 512 GB | $530 | $0.726 |
  - [1] 2026-11-03: fractional A16 rates | capture: sha256:9717df840705663b3fcf2336f717bdd84d5c492948fe850b3d6ec65dfecabf70 | quote: Fractional A16: $0.085/hr for 2 GB of VRAM, $0.17/hr for 4 GB, $0.33/hr for 8 GB.
  - [1] 2026-11-03: a GPU server is deleted at zero balance | capture: sha256:9717df840705663b3fcf2336f717bdd84d5c492948fe850b3d6ec65dfecabf70 | quote: A GPU server is deleted, not archived, if your balance reaches zero.
  - [2] 2026-11-03: registration needs an email address only | capture: sha256:573ddc9628495242d4cc00a6ac3a5691548155483a3465487f43942d0876423e | quote: An email address is all you need to register.
  - [3] 2026-11-03: minimum crypto top-up is USD 5 for USDT | capture: sha256:65eab18042e6a8bf0b4db1452b62482437df03a096057aab782d4392795f7a21 | quote: Paying: crypto first. USDT (Tron, BSC, Ethereum, Polygon) from $5 and 300+
  - [4] 2026-11-03: listed on the computeprices index as GPU-focused | capture: sha256:d07741305e262b2f68c2da4eca9653d088567ce58b1ce13b787979a7d37f0734 | quote: NoctHost is a cloud compute provider that offers a variety of services including VPS, dedicated CPU, GPU instances, and bare metal servers.
- sources:
  - [1] https://nocthost.com/gpu-vps
  - [2] https://nocthost.com/docs/faq
  - [3] https://nocthost.com/docs/api
  - [4] https://computeprices.com/providers/nocthost
