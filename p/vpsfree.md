# VPSFree.es

> vpsfree.es | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpsfree/ | JSON https://fshy.ajam.dev/api/v1/entity/vpsfree.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPSFree.es

- `compute/vpsfree-es` | paid-only | evidence documented | binding none | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:17:37.953Z (live) | stale on 2026-12-26
- url https://vpsfree.es/
- free tier: Not free: Elige entre Intel Xeon desde 4,49 €, AMD EPYC desde 4,99 €, Ryzen 5950X desde 5,99 € o Ryzen EVO desde 6,00 € al mes, sin impuestos. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits note: There is no free tier at all: the cheapest product is EUR 2.45 a month, so the first euro is the first hour.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: EUR 2.45 a month for a dedicated IPv4 with unmetered traffic in Madrid is a strong egress and IPv4 price, but it composes as a paid floor rather than as free capacity.
- reliability: no reliability event recorded
- notes: vpsFree.es sells commercial VPS hosting plans with no free tier. Account registration requires standard payment.
- extras:
  - facets.class: refutation-not-free
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: front page prices four VPS families from EUR 2.45 a month with own hardware in Madrid, NVMe, a dedicated IPv4 and unmetered traffic, quoted from the Spanish page
  - [2] 2026-10-22: a collected list of free VPS offers classifies vpsfree.es as a free IPv6-only 1 core 2 GB LXC host with no renewal requirement, which is the claim this record refutes
  - [1] 2026-11-25: the cheapest published VPS price on the vendor page is Intel Xeon from EUR 4.49 per month, taxes excluded | capture: sha256:5ee5dcb84fec8f7a7aa3e69b87c19e6d9604fad8994fe962b4032b51239874a5 | quote: Elige entre Intel Xeon desde 4,49 €, AMD EPYC desde 4,99 €, Ryzen 5950X desde 5,99 € o Ryzen EVO desde 6,00 € al mes, sin impuestos.
- sources:
  - [1] https://vpsfree.es/
  - [2] https://anyun.org/a/jishu/2023/1226/15857.html
