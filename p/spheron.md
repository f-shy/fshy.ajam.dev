# Spheron

> spheron.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spheron/ | JSON https://fshy.ajam.dev/api/v1/entity/spheron.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spheron

- `compute/spheron` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T10:24:24.029Z (live) | stale on 2026-12-04
- url https://docs.spheron.ai/getting-started/
- free tier: GPU marketplace that aggregates capacity from multiple data center partners, with no free allowance: the first step after signup is to add credits, 'minimum $15 by card or $50 by crypto, maximum $5,000 per transaction'. Cheapest live on-demand rate per GPU-hour on the pricing page: H100 $2.98 (spot $2.79), A100 80 GB $1.43 (spot $1.19), L40S $0.96, RTX 4090 $0.48; L4 is not listed. The pricing page states a 20-minute minimum runtime on every instance (60 minutes on a 2x AMD MI300X) and per-minute billing after it; the billing docs state pay-per-second billing | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: signup by Google, GitHub or email, then a deposit before anything runs: the billing step states 'Add initial credits (minimum $15, maximum $5,000 per transaction)' and 'Minimum deposit is $15', paid by card or USDC/USDT. The USD 15 is a minimum deposit of real money, not an authorisation hold, and there is no trial credit. Whether debit or prepaid cards are accepted is not stated
- interface: unknown
- limits:
  - write-gated (binding): Nothing runs before a deposit of at least USD 15 by card or USD 50 by crypto clears; there is no trial credit, so the first gate is money rather than identity. [1]
- limits note: Nothing runs before a deposit of at least USD 15 clears; there is no trial credit, so the first gate is money rather than identity.
- binding note: Nothing runs before a deposit of at least USD 15 by card or USD 50 by crypto clears; there is no trial credit, so the first gate is money rather than identity.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 15 at USD 0.52 per hour is about 28 hours of one RTX 4090, so a single minimum deposit funds a week of evening experiments; the deposit is prepaid balance, not a credit grant.
- reliability: no reliability event recorded
- notes: The site publishes no free credit; a third-party blog mentions a trial signup button, which the current flow does not show. The docs overview states that Spheron is not a blockchain network; no first-party page read describes EigenLayer or AVS matching.
- extras:
  - facets.class: depin-marketplace
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: billing step: payment by card or USDC/USDT, 'Add initial credits (minimum $15, maximum $5,000 per transaction)', 'Minimum deposit is $15', RTX 4090 about USD 0.52/hour
  - [2] 2026-10-22: live rates across H100, H200, B200, B300, A100, GH200, L40S, RTX 5090 and RTX 4090, per-minute billing, no commitments
  - [3] 2026-10-22: 48 GPU configurations listed, 6 unavailable at read time, signup by Google, GitHub or email
  - [2] 2026-11-03: the H100 is $2.98/hr on demand and $2.21 spot | capture: sha256:3a10550caa87ae7cc4d4a39e072924410916f4b50fac7c23f7b94890ac3a3296 | quote: ### H100 Hopper80 GB 128 GB RAM20 vCPUs1250 GB NVMe $2.98/hr Spot$2.21−26%
  - [2] 2026-11-03: the A100 80 GB is $1.43/hr on demand and $1.19 spot | capture: sha256:3a10550caa87ae7cc4d4a39e072924410916f4b50fac7c23f7b94890ac3a3296 | quote: ### A100 Ampere80 GB 240 GB RAM60 vCPUs1600 GB NVMe $1.43/hr Spot$1.19−17%
  - [2] 2026-11-03: the L40S is $0.96/hr on demand | capture: sha256:3a10550caa87ae7cc4d4a39e072924410916f4b50fac7c23f7b94890ac3a3296 | quote: ### L40S Ada48 GB 72 GB RAM12 vCPUs625 GB NVMe $0.96/hr
  - [2] 2026-11-03: the RTX 4090 is $0.48/hr on demand | capture: sha256:3a10550caa87ae7cc4d4a39e072924410916f4b50fac7c23f7b94890ac3a3296 | quote: ### RTX 4090 Ada24 GB 200 GB RAM88 vCPUs7600 GB NVMe $0.48/hr
  - [2] 2026-11-03: a 20-minute minimum runtime and per-minute billing after it | capture: sha256:3a10550caa87ae7cc4d4a39e072924410916f4b50fac7c23f7b94890ac3a3296 | quote: Yes, a 20-minute minimum runtime on every instance, and 60 minutes on a 2x AMD MI300X. After that Spheron bills per minute, so you pay for the exact time you use, with no contract and no long-term commitment.
  - [4] 2026-11-03: the billing docs state pay-per-second billing | capture: sha256:3b59aa29a58ca44c2d8113691acdacf78b9cb640d9c3261ac685adc31bf629bd | quote: - Pay-per-second billing: credits are deducted continuously based on your hourly rate, so you pay only for the exact time your instance runs
  - [4] 2026-11-03: the minimum deposit is $15 by card and $50 by crypto | capture: sha256:3b59aa29a58ca44c2d8113691acdacf78b9cb640d9c3261ac685adc31bf629bd | quote: - Minimum deposit: $15 by card, $50 by crypto
  - [1] 2026-11-03: the maximum deposit is $5,000 per transaction | capture: sha256:9ba6ee5602bb8a83293c3127c1aeee01e4f699e90cfc72db602dec10fb5047a0 | quote: 3. Add initial credits (minimum $15 by card or $50 by crypto, maximum $5,000 per transaction)
  - [2] 2026-11-03: the H100 is $2.98/hr on demand and $2.79 spot on the live pricing page | capture: sha256:91be065340f06d779aeebff43e1f30824a4fff437daa10ec03c1bc4f3d1ccb8c | quote: ### H100 Hopper80 GB 128 GB RAM20 vCPUs1250 GB NVMe $2.98/hr Spot$2.79−6%
  - [5] 2026-11-03: the docs overview states Spheron is not a blockchain network but a GPU cloud aggregating capacity from multiple providers | capture: sha256:445cf60e7c3ce304045c92293c9bf52416120989c408d39543181aec83270304 | quote: Spheron is not a blockchain network. It is a GPU cloud platform that aggregates capacity from multiple providers across North America, Europe, and Asia Pacific and exposes it through a unified API and dashboard.
  - [6] 2026-11-03: the site describes Spheron as a marketplace aggregating supply from data center partners | capture: sha256:7facf2e51160198b188f079638b892ce6960ef2345840ecff8e554fcf9fc23f7 | quote: Spheron is not a single cloud provider. It is a marketplace that aggregates GPU supply from multiple enterprise-grade data center partners.
- sources:
  - [1] https://docs.spheron.ai/getting-started/
  - [2] https://www.spheron.network/pricing
  - [3] https://app.spheron.ai/signup
  - [4] https://docs.spheron.ai/billing
  - [5] https://docs.spheron.ai/overview
  - [6] https://www.spheron.network/
