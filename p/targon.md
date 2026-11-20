# Targon

> targon.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/targon/ | JSON https://fshy.ajam.dev/api/v1/entity/targon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Targon

- `compute/targon` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:35.126Z (live) | stale on 2026-12-04
- url https://targon.com/inventory
- free tier: No signup credit. Inventory page, price per hour per GPU: VM H100 x1 Small $3.09 and H100 x8 Extra Large $3.09 (in stock); bare metal H100 x8 $3.11 and RTX 4090 x4 $0.60 in Austin US (in stock); H200 $3.59; B200 x8 $6.50, B300 x8 $8.40 and $8.50, and RTX PRO 6000B x1 $1.69 out of stock; CPU - Small (AMD) with 4 vCPU $0.15. A100, L40S and L4 are not listed. The page says 'Live hourly pricing'; the billing granularity and the minimum bill are not stated on the pages read. Signup quoted as a plain email and password form at targon.com/create-account | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: email only: the create-account page is an email address, a password and a password confirmation, "with no wallet field", so a Bittensor wallet is not part of onboarding. No card, phone or identity document is stated at signup and no hold exists there; the record does not state whether debit or prepaid cards are accepted when a balance is funded, and independent metadata records onboarding as self-serve with "trial: no"
- interface: ssh
- limits:
  - volume-quota (binding): There is no free tier, so a funded balance fails first. The cheapest thing that runs at all is a CPU-only instance at USD 0.15 per hour. [1]
- limits note: There is no free tier, so a funded balance fails first. The cheapest thing that runs at all is a CPU-only instance at USD 0.15 per hour.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: part of the free tier
- composes with: None at zero budget. Worth noting that Targon's email signup means a Bittensor-hosted GPU business can be reached without any wallet, which contradicts the common assumption that Bittensor subnets are wallet-gated.
- reliability: no reliability event recorded
- notes: Targon is the counter-example to the wallet assumption for Bittensor subnets. Its account creation is a plain email form, its docs never ask for a TAO balance, and the wallet appears only on the provider side where a miner hotkey is used. The GPU business is therefore reachable in principle by any client with money, and not at all by this one. A LinkedIn post from a Targon representative offers free credits on request, which is an interpersonal door and not a documented program.
- extras:
  - facets.class: decentralized-gpu-cloud
  - facets.shape.vcpu: 12
  - facets.shape.ram_gib: 175
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: live table shows H100 x1 at USD 3.09 per hour In Stock, RTX PRO 6000B x1 at USD 1.69 in stock, CPU Small AMD 4 vCPU at USD 0.15 in stock, B300 x8 at USD 8.40-8.50 Out of Stock
  - [2] 2026-10-22: signup is an email address, password and password confirmation, with no wallet field
  - [3] 2026-10-22: confidential GPU VMs with Intel TDX and direct SSH; requires attaching an SSH key at creation; login user is always ubuntu
  - [4] 2026-10-22: independent metadata records onboarding as self-serve with 'trial: no'
  - [1] 2026-11-03: the H100 x1 Small VM is $3.09 per hour per GPU and in stock | capture: sha256:dc2c3d74ab2b978723eb5c6e92651e94796eb0c1290f9a31df4482b988b73179 | quote: | H100 × 1Small | 12 | 175 GB | 320 GB | $3.09 | In Stock |
  - [1] 2026-11-03: the H100 x8 Extra Large VM is $3.09 per hour per GPU | capture: sha256:dc2c3d74ab2b978723eb5c6e92651e94796eb0c1290f9a31df4482b988b73179 | quote: | H100 × 8Extra Large | 96 | 1400 GB | 2.5 TB | $3.09 | In Stock |
  - [1] 2026-11-03: the RTX PRO 6000B x1 Small is $1.69 and out of stock | capture: sha256:dc2c3d74ab2b978723eb5c6e92651e94796eb0c1290f9a31df4482b988b73179 | quote: | RTX PRO 6000B × 1Small | 32 | 128 GB | 320 GB | $1.69 | Out of Stock |
  - [5] 2026-11-03: bare-metal H100 x8 is $3.11 per hour per GPU in Austin US | capture: sha256:e42b21fd642a1b0fe92ea80a0a8270ce372146af1282bf521bdac7c67684a909 | quote: | H100 × 8Nvidia H100 Bare metal | 192 | 1907 GB | 14.4 TB | Austin US | $3.11 | In Stock |
  - [5] 2026-11-03: bare-metal RTX 4090 x4 is $0.60 per hour per GPU in Austin US | capture: sha256:e42b21fd642a1b0fe92ea80a0a8270ce372146af1282bf521bdac7c67684a909 | quote: | RTX 4090 × 4Nvidia RTX 4090 Bare metal | 128 | 751 GB | 3.5 TB | Austin US | $0.60 | In Stock |
- sources:
  - [1] https://targon.com/inventory
  - [2] https://targon.com/create-account
  - [3] https://docs.targon.com/guides/virtual-machines
  - [4] https://apis.io/providers/targon/
  - [5] https://targon.com/inventory/bare-metal
