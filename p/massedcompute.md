# Massed Compute

> massedcompute.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/massedcompute/ | JSON https://fshy.ajam.dev/api/v1/entity/massedcompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Massed Compute

- `compute/massed-compute` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:29.736Z (live) | stale on 2026-12-04
- url https://vm.massedcompute.com/pricing
- free tier: Operator-run on-demand GPU VMs with a full public rate card, no contract and no bandwidth charges. Quoted single-card rates: RTX A6000 48GB USD 0.55/hr on 6 vCPU, 32 GB RAM and 256 GB disk (alternate configuration) and USD 0.57/hr on 48 GB RAM; RTX 6000 Ada 48GB USD 0.79/hr; L40 48GB USD 0.86/hr; L40S 48GB USD 0.97/hr; A100 80GB USD 1.35/hr; A100 SXM4 80GB USD 1.38/hr; H100 80GB USD 2.73/hr on 20 vCPU, 128 GB RAM and 1250 GB disk; H100 SXM5 80GB USD 3.14/hr; H200 NVL 141GB USD 3.62/hr. Eight-card nodes: B300 SXM6 USD 52.80/hr and B200 SXM6 USD 43.46/hr. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: all listed rates are the on-demand tier. unverified: the pricing page states no billing granularity and no minimum bill. It lists no RTX 4090 and no L4 row.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: page description quoted: No contracts, no bandwidth charges, and no hidden fees | metered: yes | source: [1]
- identity: email | detail: email only: the signup page asks for an email address and a password, and "no card field and no company field appears on that page". No card, no hold and no identity document at signup; the record does not state whether debit or prepaid cards are accepted when payment is first taken
- interface: unknown
- limits note: Nothing published binds above the scale; the only gate is prepayment, and whether a card is demanded at deploy rather than at signup was not tested.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 2.73 for an H100 hour with 1.25 TB of included disk is above the on-demand H100 floors found later in this same session, HyperAI PCIe at USD 1.80, Voltage Park at USD 1.99 and QuantaCloud PCIe at USD 2.59, so the reason to take this row is the bundled disk and the email-only signup rather than the rate.
- reliability: no reliability event recorded
- notes: The 1250 GB of bundled disk on the H100 row is unusual at this price and is why the shape quotes that row rather than the cheapest card. Supply is asserted by a rate card with a Deploy link per row, not measured: no instance was launched. Free egress is the vendor's claim. Pre-existing A6000 rate at USD 0.55/hr sits between RunPod's USD 0.59 and TensorDock's USD 0.12 consumer floor.
- extras:
  - facets.class: gpu-broker-rate-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 20
  - facets.shape.ram_gib: 128
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 80
  - facets.shape.disk_gib: 1250
- evidence:
  - [1] 2026-10-22: quoted rate rows: RTX A6000 x1 USD 0.55/hr and USD 0.57/hr; A100 80GB x1 USD 1.35/hr; H100 80GB x1 USD 2.73/hr on 20 vCPU and 128 GB RAM; H200 NVL x1 USD 3.62/hr; B300 x8 USD 52.80/hr
  - [1] 2026-10-22: page description quoted: No contracts, no bandwidth charges, and no hidden fees
  - [2] 2026-10-22: the signup form asks for an email address and a password only; no card field and no company field appears on that page
  - [3] 2026-10-22: the operator states it has run since 2021 and claims NVIDIA Preferred Partner status; the site names the cards it runs rather than aggregating other hosts
  - [1] 2026-11-03: the page lists its GPU rows as on-demand instances | capture: sha256:96334b9ea84638ed618c1e0cedacde1a2b661797b0a3e74c53d870f4fc8260be | quote: All configurations listed below. Deploy on-demand instances instantly, or contact us for bare metal and commitment pricing.
  - [1] 2026-11-03: A100 (80GB) single card is USD 1.35 per hour | capture: sha256:96334b9ea84638ed618c1e0cedacde1a2b661797b0a3e74c53d870f4fc8260be | quote: | ×1 | 16 | 96 GB | 512 | $1.35/hr | [Deploy →](https://vm.massedcompute.com/signup) |
  - [1] 2026-11-03: L40S (48GB) single card is USD 0.97 per hour | capture: sha256:96334b9ea84638ed618c1e0cedacde1a2b661797b0a3e74c53d870f4fc8260be | quote: | ×1 | 12 | 72 GB | 625 | $0.97/hr | [Deploy →](https://vm.massedcompute.com/signup) |
  - [1] 2026-11-03: H100 (80GB) single card is USD 2.73 per hour, unchanged | capture: sha256:96334b9ea84638ed618c1e0cedacde1a2b661797b0a3e74c53d870f4fc8260be | quote: | ×1 | 20 | 128 GB | 1250 | $2.73/hr | [Deploy →](https://vm.massedcompute.com/signup) |
- sources:
  - [1] https://vm.massedcompute.com/pricing
  - [2] https://vm.massedcompute.com/signup
  - [3] https://massedcompute.com/
