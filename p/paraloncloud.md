# ParalonCloud

> paraloncloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paraloncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/paraloncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ParalonCloud

- `compute/paraloncloud` | paid-only | evidence documented | binding none | category GPU marketplace
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:24:23.352Z (live) | stale on 2026-12-04
- url https://paraloncloud.com/pricing/rtx-4090
- free tier: no free GPU tier is published; the RTX 4090 page read on 2026-11-03 gives a price per hour of USD 0.41 to USD 0.45, set by independent providers, billed by the minute with no contract or minimum spend; the rent page lists H100, A100 and L40S models at list prices (H100 SXM USD 2.40 per hour, A100 80GB PCIe USD 1.90, L40S USD 0.65) with none available right now, and the pricing page's GPU table is empty in a static read. The same account has a free trial of 250,000 inference tokens on a free key. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: the GPU table on the pricing page needs JavaScript; the card page was read instead. Spot machines can be taken back by the owner with two minutes' notice
- per-object cap: not applicable | source: [1] | note: a whole machine with the card in it, not a slice
- retention: not applicable | source: [2] | note: a stopped rental is wiped
- egress: not published on the pages read | metered: no | source: [1]
- identity: email | detail: Sign in with Google or a one-time email code; a short 1-hour balance is required up front, topped up by card, by a USDC transfer or from a connected USDC or USDT wallet. No phone or ID document is stated on the pages read.
- interface: ssh
- limits note: No quota is stated; a 1-hour balance is needed up front and a rental stops when credits cannot cover the next minute.
- binding note: the same as limits note
- interface detail: inferred from the docs, which describe Jupyter Lab in the browser or SSH from a terminal; not probed
- tooling: JupyterLab or SSH on a rented machine; an OpenAI-compatible inference API with prlc_ keys; a Blender rendering beta
- composes with: Per-minute RTX 4090 rentals from independent hosts plus an inference API on the same credit balance.
- reliability: The docs state that a rental not answering within 5 minutes is closed without charge, and that after 15 minutes of failure it is ended; a machine whose credits run out is stopped and wiped.
- notes: Found via computeprices.com (provider slug paraloncloud). The aggregator lists RTX 4090 at USD 0.420 (1x) and USD 0.450 (2x) plus RTX 4060 Ti, 4070 SUPER, 4080 SUPER, 5060 Ti, 5070 Ti and 5090. The five cards asked about are not listed except the RTX 4090.
- evidence:
  - [1] 2026-11-03: RTX 4090 price per hour is USD 0.41 to USD 0.45 | capture: sha256:42fea1453c56402effb653558002c4a61e7620cebaebe5c6d572161064aa9ea6 | quote: Price per hour $0.41–$0.45 Set by independent providers
  - [1] 2026-11-03: billing is per minute with no contract or minimum spend | capture: sha256:42fea1453c56402effb653558002c4a61e7620cebaebe5c6d572161064aa9ea6 | quote: the hourly rate you see when you start is locked for the whole session, billing stops the minute you stop, and there is no contract or minimum spend
  - [2] 2026-11-03: account is by Google or email code | capture: sha256:78bd35ac88d57daf74249b1a10f753a42585b89f5e68f54afecb0cc234dc59de | quote: An account — sign in with Google or a one-time email code.
  - [2] 2026-11-03: a 1-hour balance is required and can be topped up by card or USDC | capture: sha256:78bd35ac88d57daf74249b1a10f753a42585b89f5e68f54afecb0cc234dc59de | quote: A short 1-hour balance is required up front to open a session; you're only charged for the minutes you actually use. Top up by card, by a USDC transfer
  - [3] 2026-11-03: inference has a free trial of 250,000 tokens | capture: sha256:628aa603f0de0dd1522c28e61a6f3df6dad4b2a1e4c0e70e59d34cb04a8ffe43 | quote: Free trial: 250,000 tokens on a free key.
  - [4] 2026-11-03: listed on the computeprices index with 7 GPU models | capture: sha256:f03f8c18f56ff3f8ebe414f4a18a067b8e608ad6aa15a08f852672a80b2894e2 | quote: ParalonCloud is under the market median on 2 of its 7 GPUs today.
  - [5] 2026-11-03: the rent page lists H100 SXM at a list price of USD 2.40 per hour with none available right now | capture: sha256:2830ba32a9bae3c63c630dc9fbc45b7f1ebc0a3c08bf6e5cfa16ef89290f34c9 | quote: | [Rent H100 SXM](https://paraloncloud.com/pricing/h100-sxm)Hopper | 80 GB | None right now | list$2.40 |
  - [5] 2026-11-03: the rent page lists L40S at a list price of USD 0.65 per hour, none available now | capture: sha256:2830ba32a9bae3c63c630dc9fbc45b7f1ebc0a3c08bf6e5cfa16ef89290f34c9 | quote: | [Rent L40S](https://paraloncloud.com/pricing/l40s)Ada Lovelace | 48 GB | None right now | list$0.65 |
  - [5] 2026-11-03: the rent page lists A100 80GB PCIe at a list price of USD 1.90 per hour, none available now | capture: sha256:2830ba32a9bae3c63c630dc9fbc45b7f1ebc0a3c08bf6e5cfa16ef89290f34c9 | quote: | [Rent A100 80GB PCIe](https://paraloncloud.com/pricing/a100-80gb-pcie)Ampere | 80 GB | None right now | list$1.90 |
  - [3] 2026-11-03: the pricing page GPU table has a header row only in the static read | capture: sha256:6cb2ef642be3ad7095fdc12851ff477a3d2ef39a3327c027bcc3b011e44b3254 | quote: GPUVRAMCUDAFP32 TFAvailabilityPrice
  - [3] 2026-11-03: the 250,000-token inference trial is unchanged | capture: sha256:6cb2ef642be3ad7095fdc12851ff477a3d2ef39a3327c027bcc3b011e44b3254 | quote: Free trial: 250,000 tokens on a free key.
- sources:
  - [1] https://paraloncloud.com/pricing/rtx-4090
  - [2] https://paraloncloud.com/docs/rent-a-gpu
  - [3] https://paraloncloud.com/pricing
  - [4] https://computeprices.com/providers/paraloncloud
  - [5] https://paraloncloud.com/rent
