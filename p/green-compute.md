# Green Compute

> green-compute.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/green-compute/ | JSON https://fshy.ajam.dev/api/v1/entity/green-compute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Green Compute

- `compute/green-compute` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:51.584Z (live) | stale on 2026-12-04
- url https://www.green-compute.com/
- free tier: No free tier. RTX 4090 rental is USD 0.40 per hour, billed per minute, and the home page states 'Indicative starting rates. Final prices are set by individual verified providers and update in real time on the rental dashboard.' An account starts with a USD 5 minimum top-up. Only RTX 4090 and RTX 5090 are offered; H100, A100, L40S and L4 are not listed. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Self-serve account: the home page sign-up step reads 'Free account, $5 minimum top-up to start. Stripe, USDT, USDC, or TAO.' The sign-up form fields (email, phone, card, ID document) were not read: unverified: behind a sign-up. No institution requirement is stated on the page.
- interface: unknown
- limits:
  - write-gated (binding): A USD 5 minimum top-up is required to start ('Free account, $5 minimum top-up to start.'), paid by Stripe, USDT, USDC or TAO; the fleet is two consumer GPU models, RTX 4090 and RTX 5090. [1]
- limits note: The enterprise door fails first: the site's buyer side is framed as a negotiated enterprise contract, the fleet is two GPU SKUs in one country, and no self-serve signup or free credit is documented.
- binding note: A USD 5 minimum top-up is required to start ('Free account, $5 minimum top-up to start.'), paid by Stripe, USDT, USDC or TAO; the fleet is two consumer GPU models, RTX 4090 and RTX 5090.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. A two-SKU UK fleet aimed at enterprise contracts is not a lane an international registrant can enter without an organisation.
- reliability: no reliability event recorded
- notes: The network is two consumer GPU models. The enterprise page lists RTX 4090 at USD 0.40 and RTX 5090 at USD 0.70 per GPU per hour, says 'Rent by the hour or the month.', and offers token-metered inference through an OpenAI-compatible API. The pricing API lists only the RTX 4090 as online.
- extras:
  - facets.class: decentralized-gpu-marketplace
  - facets.shape.gpu_class: RTX 4090 and RTX 5090 only
- evidence:
  - [1] 2026-10-22: quoted: 'Indicative starting rates. Final prices are set by individual verified providers'; the buyer side is 'Enterprise inference' with 'one SKU to negotiate'; the fleet is '2 SKUs: 4090 + 5090' from 'UK farms running RTX 4090s and RTX 5090s on biogas'
  - [2] 2026-10-22: subnet directory lists Green Compute as Subnet 110 with a market cap of 62.99K TAO, making it the tenth largest subnet by that measure and a real network rather than a placeholder
  - [1] 2026-11-03: RTX 4090 rental costs USD 0.40 per hour and is billed per minute | capture: sha256:47a64e6b09b6ab7c843e500c32f988c4c20d24b177480e0f702a4d2e1d188a06 | quote: ✓ RTX 4090 ready · $0.40/hr, billed per minute
  - [1] 2026-11-03: the sign-up step is a free account with a USD 5 minimum top-up paid by Stripe, USDT, USDC or TAO | capture: sha256:47a64e6b09b6ab7c843e500c32f988c4c20d24b177480e0f702a4d2e1d188a06 | quote: Free account, $5 minimum top-up to start. Stripe, USDT, USDC, or TAO.
  - [3] 2026-11-03: the enterprise page lists RTX 5090 at USD 0.70 per GPU per hour | capture: sha256:8d08bd5a2beb7112c8d588840b6d8bc0dbf5b49370cecb317c7207016b0caea7 | quote: $0.70 / GPU / hr
  - probe:api.green-compute.com 2026-11-03: the pricing API lists the RTX 4090 at 40 cents (USD 0.4) per GPU hour | capture: sha256:5ee3671d18fef5f5e6af37e14544be4d766c8a808b36d5ee576d1adba786c646 | quote: "vram_gb":24,"cents_per_gpu_hour":40,"usd_per_gpu_hour":0.4,"usd_per_gpu_hour_paid_in_alpha":0.3636
  - [3] 2026-11-03: rental is offered by the hour or by the month | capture: sha256:8d08bd5a2beb7112c8d588840b6d8bc0dbf5b49370cecb317c7207016b0caea7 | quote: Rent by the hour or the month.
- sources:
  - [1] https://www.green-compute.com/
  - [2] https://bittensor.ai/subnets
  - [3] https://www.green-compute.com/enterprise
