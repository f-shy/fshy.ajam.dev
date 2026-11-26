# ParalonCloud

> paraloncloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paraloncloud/ | JSON https://fshy.ajam.dev/api/v1/entity/paraloncloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ParalonCloud

- `compute/paraloncloud` | paid-only | evidence documented | binding none | category GPU marketplace
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:21:00.910Z (live) | stale on 2026-12-25
- url https://paraloncloud.com/pricing/rtx-4090
- free tier: no free GPU tier is published; the RTX 4090 page gives a price of USD 0.45 an hour, set by independent providers, billed by the minute with no contract or minimum spend. The same account has a free trial of inference tokens on a free key and free Blender rendering during beta. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: the GPU table on the pricing page needs JavaScript; the card page was read instead. Spot machines can be taken back by the owner with two minutes' notice
- per-object cap: not applicable | source: [1] | note: a whole machine with the card in it, not a slice
- retention: not applicable | source: [2] | note: a stopped rental is wiped
- egress: not published on the pages read | metered: no | source: [1]
- identity: email | detail: Sign in with Google, GitHub, LinkedIn or a one-time email code; a short 1-hour balance is required up front, topped up by card, by a USDC transfer or from a connected USDC or USDT wallet. No phone or ID document is stated on the pages read.
- interface: ssh
- limits note: No quota is stated; a 1-hour balance is needed up front and a rental stops when credits cannot cover the next minute.
- binding note: the same as limits note
- interface detail: Jupyter Lab in the browser or SSH with the renter's own key, chosen at start; a rental API and MCP servers drive the same actions
- tooling: JupyterLab or SSH on a rented machine; an OpenAI-compatible inference API with prlc_ keys; a Blender rendering beta
- composes with: Per-minute RTX 4090 rentals from independent hosts plus an inference API on the same credit balance.
- reliability: The docs state that a rental not answering within 5 minutes is closed without charge, and that after 15 minutes of failure it is ended; a machine whose credits run out is stopped and wiped.
- notes: Found via computeprices.com (provider slug paraloncloud). The aggregator lists RTX 4090 at USD 0.420 (1x) and USD 0.450 (2x) plus RTX 4060 Ti, 4070 SUPER, 4080 SUPER, 5060 Ti, 5070 Ti and 5090. The five cards asked about are not listed except the RTX 4090.
- evidence:
  - [1] 2026-11-03: billing is per minute with no contract or minimum spend | capture: sha256:42fea1453c56402effb653558002c4a61e7620cebaebe5c6d572161064aa9ea6 | quote: the hourly rate you see when you start is locked for the whole session, billing stops the minute you stop, and there is no contract or minimum spend
  - [2] 2026-11-03: a 1-hour balance is required and can be topped up by card or USDC | capture: sha256:78bd35ac88d57daf74249b1a10f753a42585b89f5e68f54afecb0cc234dc59de | quote: A short 1-hour balance is required up front to open a session; you're only charged for the minutes you actually use. Top up by card, by a USDC transfer
  - [3] 2026-11-03: listed on the computeprices index with 7 GPU models | capture: sha256:f03f8c18f56ff3f8ebe414f4a18a067b8e608ad6aa15a08f852672a80b2894e2 | quote: ParalonCloud is under the market median on 2 of its 7 GPUs today.
  - [4] 2026-11-03: the rent page lists H100 SXM at a list price of USD 2.40 per hour with none available right now | capture: sha256:2830ba32a9bae3c63c630dc9fbc45b7f1ebc0a3c08bf6e5cfa16ef89290f34c9 | quote: | [Rent H100 SXM](https://paraloncloud.com/pricing/h100-sxm)Hopper | 80 GB | None right now | list$2.40 |
  - [4] 2026-11-03: the rent page lists A100 80GB PCIe at a list price of USD 1.90 per hour, none available now | capture: sha256:2830ba32a9bae3c63c630dc9fbc45b7f1ebc0a3c08bf6e5cfa16ef89290f34c9 | quote: | [Rent A100 80GB PCIe](https://paraloncloud.com/pricing/a100-80gb-pcie)Ampere | 80 GB | None right now | list$1.90 |
  - [5] 2026-11-03: the pricing page GPU table has a header row only in the static read | capture: sha256:6cb2ef642be3ad7095fdc12851ff477a3d2ef39a3327c027bcc3b011e44b3254 | quote: GPUVRAMCUDAFP32 TFAvailabilityPrice
  - [5] 2026-11-03: the 250,000-token inference trial is unchanged | capture: sha256:6cb2ef642be3ad7095fdc12851ff477a3d2ef39a3327c027bcc3b011e44b3254 | quote: Free trial: 250,000 tokens on a free key.
  - [1] 2026-11-24: the RTX 4090 card page now shows USD 0.45 an hour | capture: sha256:62f585e797e06f784f0975471adf9f7885c8feb50f89acd4be9ddaf17a6c4e10 | quote: Price per hour $0.45
  - [2] 2026-11-24: the account sign-in methods now include GitHub and LinkedIn | capture: sha256:5e75e67af5a320ff0bd92069b5f564dd365b9f38364b7f7a9be11e20342ec7c1 | quote: An account — sign in with Google, GitHub, LinkedIn or a one-time email code.
  - [2] 2026-11-24: the access interface is a browser IDE or SSH with the renter's public key | capture: sha256:5e75e67af5a320ff0bd92069b5f564dd365b9f38364b7f7a9be11e20342ec7c1 | quote: Choose how you connect — Jupyter Lab (a browser IDE with Python, a terminal, and a file browser) is selected by default. Pick SSH for a root shell from your own terminal or editor: it logs in with your SSH public key, which you add right there or on the [SSH keys](https://paraloncloud.com/ssh-keys) page (no key yet: `ssh-keygen -t ed25519`).
  - [1] 2026-11-24: the RTX 4090 price is USD 0.45 an hour | capture: sha256:62f585e797e06f784f0975471adf9f7885c8feb50f89acd4be9ddaf17a6c4e10 | quote: Price per hour $0.45
  - [2] 2026-11-24: an account by Google, GitHub, LinkedIn or an email code is required before renting | capture: sha256:5e75e67af5a320ff0bd92069b5f564dd365b9f38364b7f7a9be11e20342ec7c1 | quote: An account — sign in with Google, GitHub, LinkedIn or a one-time email code.
  - [2] 2026-11-24: the renter picks Jupyter Lab or SSH at start | capture: sha256:5e75e67af5a320ff0bd92069b5f564dd365b9f38364b7f7a9be11e20342ec7c1 | quote: Choose how you connect — Jupyter Lab (a browser IDE with Python, a terminal, and a file browser) is selected by default. Pick SSH for a root shell from your own terminal or editor: it logs in with your SSH public key, which you add right there or on the [SSH keys](https://paraloncloud.com/ssh-keys) page (no key yet: `ssh-keygen -t ed25519`).
  - [2] 2026-11-24: a non-responding rental is ended after 15 minutes | capture: sha256:5e75e67af5a320ff0bd92069b5f564dd365b9f38364b7f7a9be11e20342ec7c1 | quote: - After 15 minutes the rental is ended and you get an email.
  - [5] 2026-11-24: inference has a free trial of 250,000 tokens | capture: sha256:08f9fc6f0eefc85d4f5d8fbc0d0d89b582371f0c76ab56ea6fbaae18d95844cf | quote: Free trial: 250,000 tokens on a free key.
  - [4] 2026-11-24: the H100 SXM list price is USD 2.30 an hour with none available now | capture: sha256:7199e3456fa94c91ddc417c96dc97b0f0b5a8d59194afef8a83bd6ffa5b74483 | quote: [Rent H100 SXM](https://paraloncloud.com/pricing/h100-sxm)Hopper · [specs](https://paraloncloud.com/pricing/h100-sxm) | 80 GB | None right now | list$2.30/h |
  - [4] 2026-11-24: the A100 80GB PCIe list price is USD 0.98 an hour | capture: sha256:7199e3456fa94c91ddc417c96dc97b0f0b5a8d59194afef8a83bd6ffa5b74483 | quote: list$0.98/h
  - [4] 2026-11-24: the L40S list price is USD 0.75 an hour with none available now | capture: sha256:7199e3456fa94c91ddc417c96dc97b0f0b5a8d59194afef8a83bd6ffa5b74483 | quote: [Rent L40S](https://paraloncloud.com/pricing/l40s)Ada Lovelace · [specs](https://paraloncloud.com/pricing/l40s) | 48 GB | None right now | list$0.75/h |
  - [1] 2026-11-24: billing is per minute with no contract or minimum spend | capture: sha256:62f585e797e06f784f0975471adf9f7885c8feb50f89acd4be9ddaf17a6c4e10 | quote: The hourly rate you see when you start is locked for the whole session, billing stops the minute you stop, and there is no contract or minimum spend.
- sources:
  - [1] https://paraloncloud.com/pricing/rtx-4090
  - [2] https://paraloncloud.com/docs/rent-a-gpu
  - [3] https://computeprices.com/providers/paraloncloud
  - [4] https://paraloncloud.com/rent
  - [5] https://paraloncloud.com/pricing
