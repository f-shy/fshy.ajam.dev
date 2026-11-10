# Omega Gradient

> omegagradient.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/omegagradient/ | JSON https://fshy.ajam.dev/api/v1/entity/omegagradient.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Omega Gradient

- `compute/omega-gradient` | paid-only | evidence documented | binding none | category GPU marketplace
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://omegagradient.com/compute.html
- free tier: no free tier is published; the marketplace page serves a static snapshot dated 2026-08-29 of 98 live listings from USD 0.06 per GPU-hour. Snapshot rows per GPU-hour: H100 80 GB PCIe USD 2.63 (Canada), A100-80G PCIe USD 1.42 (Canada and US Central), L40S 48 GB PCIe USD 0.93 (US Central), RTX 4090 24 GB USD 0.42 on an 8x node (US Central) and USD 0.63 on a 1x node (Global, flexible). The snapshot lists no L4. Billing is prepaid from credits and accrues per hour only while the instance exists. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: the live board needs JavaScript and was not read; the static snapshot table read on 2026-11-03 is dated 2026-08-29, so these are not current rates
- per-object cap: not applicable | source: [1] | note: listings run from 1x to 8x GPU nodes in the snapshot
- retention: not applicable | source: [1] | note: a machine record
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: unverified: behind a sign-up. The FAQ says billing is prepaid from credits and a launch needs an SSH public key; the sign-up and payment pages were not reachable without an account (omegagradient.com/login answered a 404 page).
- interface: ssh
- limits note: No quota is stated; the constraint is the prepaid credit balance and the per-listing region and node shape.
- binding note: the same as limits note
- interface detail: inferred from the FAQ, which says to add an SSH public key and launch from a template; not probed
- tooling: one console, one bill and one SSH key across supplier listings, deployable as containers, VMs or bare metal; templates Ubuntu 22.04 + CUDA, PyTorch and JupyterLab
- composes with: A resale marketplace: listings are provider-anonymous, so the same H100 or A100 appears at several regions and prices in one board; useful to compare against single-vendor hosted rates.
- reliability: The static snapshot read on 2026-11-03 is dated 2026-08-29; the aggregator profile lists 'Supplier identities are withheld until qualification' and 'No published documentation portal'.
- notes: Found via computeprices.com (provider slug omegagradient). The aggregator shows L4 at USD 1.00 (Europe East) and RTX 4090 8x at USD 0.42, A100 SXM 8x at USD 1.42 from 2026-11-03 rows, newer than the provider snapshot. Not read: the live board (JavaScript) and the sign-up and payment steps.
- evidence:
  - [1] 2026-11-03: snapshot lists an H100 80 GB PCIe in Canada at USD 2.63 per GPU-hour | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: | H100 | 1× | 80 GB | Canada | PCIe | $2.63/GPU/hr | $2.63/hr |
  - [1] 2026-11-03: snapshot lists an A100 80 GB PCIe at USD 1.42 per GPU-hour | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: | A100-80G | 1× | 80 GB | US · Central | PCIe | $1.42/GPU/hr | $1.42/hr |
  - [1] 2026-11-03: snapshot lists an L40S at USD 0.93 per GPU-hour | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: | L40S | 1× | 48 GB | US · Central | PCIe | $0.93/GPU/hr | $0.93/hr |
  - [1] 2026-11-03: snapshot lists an RTX 4090 1x node at USD 0.63 per GPU-hour | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: | RTX 4090 | 1× | 24 GB | Global · flexible | PCIe | $0.63/GPU/hr | $0.63/hr |
  - [1] 2026-11-03: the snapshot is dated 2026-08-29 | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: 98 listings · from $0.06/GPU/hr · snapshot 2026-08-29
  - [1] 2026-11-03: billing is prepaid credits, hourly | capture: sha256:facf8e885321faa2b4f65358cc0992604715d0af6453173716cc54fbc512c3d4 | quote: Billing is prepaid from credits and accrues per hour only while the instance exists
  - [2] 2026-11-03: listed on the computeprices index with 43 GPU models | capture: sha256:ccf9f5c5a4437721a0a56b56568520eeda66b8b291346378dfc0b011f1e77805 | quote: Omega Gradient is the cheapest provider for Quadro RTX 4000 today, and under the market median on 16 of its 43 GPUs.
- sources:
  - [1] https://omegagradient.com/compute.html
  - [2] https://computeprices.com/providers/omegagradient
