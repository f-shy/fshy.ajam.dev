# Bittensor

> bittensor.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bittensor/ | JSON https://fshy.ajam.dev/api/v1/entity/bittensor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bittensor

- `compute/bittensor` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T18:41:34.653Z (live) | stale on 2026-12-07
- url https://www.bittensor.com/docs/tx/register-subnet
- free tier: Permissionless GPU network of 128 subnets where a subnet slot is bought by burning TAO: the cost is 'potentially thousands of TAO', doubles after each registration, decays linearly, and 'becomes the new subnet's initial TAO pool reserve, a sunk cost, not a refundable deposit'. Miner registration is separate and clamped between 0.0005 TAO and 100 TAO per subnet. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: rest
- limits:
  - write-gated (binding): There is no free lane: a subnet slot costs 605.7 TAO at the 2026-10-22 chain state, and mining needs a GPU, so capital fails before identity does. [1]
- limits note: There is no free lane: a subnet slot costs 605.7 TAO at the 2026-10-22 chain state, and mining needs a GPU, so capital fails before identity does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A rented GPU pointed at an uncontested subnet is the only route without owned hardware: the burn is then 0.0005 TAO, but emission depends on that subnet's incentive mechanism, which varies per subnet and is not published in one place.
- reliability: no reliability event recorded
- notes: 605.7 TAO at USD 256.94 is USD 155,629 for one subnet slot; the maximum miner burn of 100 TAO is USD 25,694 on the most contested subnet. The registration cost is a third-party chain read rather than a vendor page, so the dollar figure rests on a dashboard plus a price quote. Per-subnet emission rates were not read. The page prices no GPU card: H100, A100 80GB, L40S, RTX 4090 and L4 are not listed, and it states no free or credit-backed GPU hours.
- extras:
  - facets.class: depin-marketplace
- evidence:
  - [1] 2026-10-22: registration cost taken from the coldkey, doubles per registration, decays linearly, becomes the subnet's initial TAO pool reserve as a sunk cost
  - [2] 2026-10-22: cost is demand-based, 4-day window between registrations, new subnets get 4 months immunity from deregistration
  - [3] 2026-10-22: third-party chain read at block 9,339,042: registration cost now 605.7 TAO, last paid 434.7 TAO on SN103 on 20 Oct 2026
  - [4] 2026-10-22: TAO USD 256.94
  - [5] 2026-10-22: miner burn clamped between min_burn 500,000 rao (0.0005 TAO) and max_burn 100 TAO, per subnet
  - [1] 2026-11-06: the page is the register-subnet CLI reference: it prices subnet registration in TAO and lists no GPU card, no hourly GPU rate and no free GPU hours | capture: sha256:338cf3cb666b3b86b63152a560f7a2095ed1b0894fc0a7142a5658d7e592c69e | quote: The network registration cost — potentially thousands of TAO — is taken from the coldkey
  - [1] 2026-11-06: the page is the subnet-registration reference and carries no GPU price table | capture: sha256:338cf3cb666b3b86b63152a560f7a2095ed1b0894fc0a7142a5658d7e592c69e | quote: Registers a brand-new subnet with the signing coldkey as its owner and the wallet's hotkey as the subnet-owner hotkey.
- sources:
  - [1] https://www.bittensor.com/docs/tx/register-subnet
  - [2] https://taostats.io/docs/concepts/subnets/subnet-registration
  - [3] https://chainbuying.netlify.app/
  - [4] https://api.coingecko.com/api/v3/simple/price?ids=bittensor&vs_currencies=usd
  - [5] https://www.bittensor.com/docs/guides/mining/burn
