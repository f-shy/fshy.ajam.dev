# EcoHash

> ecohash.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ecohash/ | JSON https://fshy.ajam.dev/api/v1/entity/ecohash.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EcoHash

- `compute/ecohash` | trial-only | evidence documented | binding volume-quota | category GPU cloud | tier RTX PRO 6000 GPU instances
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:36:21.466Z (live) | stale on 2026-12-04
- url https://ecohash.com/pricing
- free tier: A USD 1.00 welcome credit on every new account, and one on-demand GPU model: RTX Pro 6000 (96 GB) at USD 1.89 per GPU-hour, billed per second with no minimum commitment. The GPU page says eligible accounts can try a single GPU with less than one hour of credit, subject to a minimum launch balance, capacity and account limits. None of H100, A100 80 GB, L40S, RTX 4090 or L4 is listed. Eight-GPU nodes show 'On request'; reserved nodes are by contract. | unit: credits | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1] | note: the sizes are 1, 2, 4 or 8 RTX Pro 6000 GPUs on one host
- retention: Terminating the instance releases its GPU and deletes temporary container data. Cloud drives and shared filesystems remain and continue billing until deleted. | source: [2] | note: a machine record: what is lost is the container's temporary data
- egress: not stated on the pricing or GPU pages read | metered: no | source: [1]
- identity: email | detail: sign-up at console.ecohash.com takes 'Email + password' or 'Continue with Google'; the docs state every new account receives a USD 1.00 welcome credit. Whether a card or a top-up is needed to launch beyond the credit is unverified: behind a sign-up.
- interface: ssh, rest
- limits:
  - volume-quota (binding): USD 1.00 one-time welcome credit; the GPU page states a minimum launch balance and account limits without giving the amounts [2]
- limits note: the amounts of the minimum launch balance and the account limits are not printed on the pages read: unverified: behind a sign-up
- binding note: the welcome credit of USD 1.00 is the only free allowance and covers less than one GPU-hour at the quoted rate; the launch balance and account limits are unverified: behind a sign-up
- interface detail: stated by a third-party listing, not probed: containerized Linux instances with SSH, a browser terminal and Jupyter; an OpenAI-compatible HTTP API at api.ecohash.com for models
- tooling: launch from the console at console.ecohash.com: a compute template and a 1, 2, 4 or 8 GPU size, then SSH, the browser terminal or Jupyter. Models are called through an OpenAI-compatible API with an API key.
- composes with: the USD 1.00 credit buys less than an hour of the one GPU model; the offer is a trial of RTX Pro 6000 time and a paid rental after it.
- reliability: unverified: no status page or incident history was read for this offer
- notes: Listed by computeprices.com as a GPU cloud (RTX PRO 6000 at USD 1.89 per hour, rank 17 of 41 providers on that card). It also sells an OpenAI-compatible inference API, dedicated inference endpoints and LoRA fine-tuning, which belong to the inference topic. Reserved GPU nodes are priced by contract.
- evidence:
  - [1] 2026-11-03: the only GPU in the on-demand table is the RTX Pro 6000 96 GB at USD 1.89 per GPU-hour | capture: sha256:78de5b6014c4ba3d5d83b1fa1f674bb295cdfddb03f5ae8c3815e9aed14181cb | quote: | RTX Pro 6000 | 96 GB | $1.89/GPU-hr |
  - [1] 2026-11-03: the pricing page states a USD 1 free credit on signup | capture: sha256:78de5b6014c4ba3d5d83b1fa1f674bb295cdfddb03f5ae8c3815e9aed14181cb | quote: Pay only for what you use. $1 free credit on signup.
  - [2] 2026-11-03: one per-GPU-hour rate across sizes, billed per second, no minimum commitment | capture: sha256:e1b87b6de852337473040fac3162aa7ab82a4a0ebdb2d54786a8603e1333b7d9 | quote: One rental rate per GPU-hour, whatever the size. Every configuration runs on a single machine, so all GPUs share one host. Billed per second, no minimum commitment.
  - [2] 2026-11-03: the credit covers less than one hour, and a minimum launch balance and account limits apply | capture: sha256:e1b87b6de852337473040fac3162aa7ab82a4a0ebdb2d54786a8603e1333b7d9 | quote: Eligible accounts can try a single GPU with less than one hour of credit. Minimum launch balance, capacity and account limits apply.
  - [2] 2026-11-03: termination deletes temporary container data | capture: sha256:e1b87b6de852337473040fac3162aa7ab82a4a0ebdb2d54786a8603e1333b7d9 | quote: Terminating the instance releases its GPU and deletes temporary container data.
  - [3] 2026-11-03: each new account receives a USD 1.00 welcome credit | capture: sha256:e84e02561eb51f96800b1a8bf9fefcb2d711110e32850f4d26c6cf913458f390 | quote: Every new account receives a $1.00 welcome credit automatically.
  - [3] 2026-11-03: sign-up takes an email and a password, or a Google account | capture: sha256:e84e02561eb51f96800b1a8bf9fefcb2d711110e32850f4d26c6cf913458f390 | quote: Email + password — enter your email and a password.
  - [4] 2026-11-03: third-party listing: one GPU model, so none of the H100, A100, L40S, RTX 4090 or L4 cards is offered | capture: sha256:1676695850c1c34368ce57aa7350db4133ed79c57860c8421bd14f8865daa8b8 | quote: Single GPU model (RTX PRO 6000); no H100, H200 or B200 capacity
- sources:
  - [1] https://ecohash.com/pricing
  - [2] https://ecohash.com/gpu/rtx-pro-6000
  - [3] https://docs.ecohash.com/getting-started/sign-up
  - [4] https://computeprices.com/providers/ecohash
