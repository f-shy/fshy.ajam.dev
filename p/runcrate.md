# Runcrate

> runcrate.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runcrate/ | JSON https://fshy.ajam.dev/api/v1/entity/runcrate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runcrate

- `compute/runcrate` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:21:02.389Z (live) | stale on 2026-12-25
- url https://www.runcrate.ai/pricing
- free tier: no free GPU tier is published; the live rate card read on 2026-11-24 lists 24 GPU types from USD 0.23 an hour: H100 80GB USD 3.87, A100 80GB USD 1.73, L40S 48GB USD 0.55, L4 USD 0.58, RTX 4090 USD 0.63. Billed by the second on most GPUs and by the minute on a few; booting is never billed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: prepaid terms of 1 to 12 months are up to 15% off; the live rate card is also published as JSON at /api/gpu-pricing without a key
- per-object cap: not applicable | source: [1] | note: storage volumes of 10 GB to 10,000 GB at USD 0.03 per GB a month are a separate line
- retention: not applicable | source: [1] | note: credits do not expire; storage volumes are kept when the instance is deleted
- egress: no egress fees: GPU instances bill by runtime and storage volumes by provisioned GB-month | metered: no | source: [1]
- identity: card | detail: The sign-up form asks for name, email, password and an age or consent checkbox; balance is added by card before use, from USD 20 to USD 10,000 at a time. Reserved multi-node clusters need a verification of the company and the need. No phone or ID document is stated for self-serve.
- interface: rest, cli, ssh
- limits:
  - write-gated (binding): a launch needs USD 10 or an hour of the machine, whichever is more; a balance is added by card from USD 20 [1]
- limits note: A launch is gated on a prepaid balance added by card; there is no free allowance.
- binding note: the same as limits note
- interface detail: SSH with a CLI and an OpenAI-compatible API at https://api.runcrate.ai/v1, which returns a missing-API-key error to an anonymous caller; a keyless /api/gpu-pricing JSON rate card
- tooling: SSH, Jupyter and VS Code in the browser, Python and TypeScript SDKs, a CLI and an MCP server; an OpenAI-compatible inference API on the same balance
- composes with: One prepaid balance pays for GPU hours, token-billed inference and storage volumes; the public /api/gpu-pricing endpoint publishes the live rate card without a key.
- reliability: Capacity is sourced multi-cloud rather than from owned data centres per the aggregator profile; sold-out GPUs stay listed for 30 days at 0 available per the rate card.
- notes: Found via computeprices.com (provider slug runcrate). The aggregator row for L4 (USD 1.24) is not on the provider rate card read 2026-11-03. Not read: the L4 availability.
- evidence:
  - [1] 2026-11-03: H100 80GB rate is USD 3.86 an hour | capture: sha256:905bbd6781aa5b909c02127c47d91809cd799299414887baab14b87dd66adcac | quote: | H100 Hopper | 80GB | $3.86/hr |
  - [1] 2026-11-03: A100 80GB rate is USD 1.73 an hour | capture: sha256:905bbd6781aa5b909c02127c47d91809cd799299414887baab14b87dd66adcac | quote: | A100 80GB Ampere | 80GB | $1.73/hr |
  - [1] 2026-11-03: L40S rate is USD 0.54 an hour | capture: sha256:905bbd6781aa5b909c02127c47d91809cd799299414887baab14b87dd66adcac | quote: | L40S Ada Lovelace | 48GB | $0.54/hr |
  - [1] 2026-11-03: RTX 4090 rate is USD 0.57 an hour | capture: sha256:905bbd6781aa5b909c02127c47d91809cd799299414887baab14b87dd66adcac | quote: | RTX 4090 Ada Lovelace | 24GB | $0.57/hr |
  - [1] 2026-11-03: balance is added by card from USD 20; a launch needs USD 10 | capture: sha256:905bbd6781aa5b909c02127c47d91809cd799299414887baab14b87dd66adcac | quote: Add $20 to $10,000 at a time by card. It does not expire. A launch needs $10 or an hour of the machine, whichever is more
  - [2] 2026-11-03: sign-up asks for name, email and password | capture: sha256:db88879f55eb7bfbdb5e9c7b27ac2711570a3acbf5c64e76f0107c5bfe6fc8c7 | quote: Name Email Password Confirm password
  - [1] 2026-11-24: the lowest listed GPU rate is USD 0.23 an hour on an RTX 3090 | capture: sha256:2104e9586d59eb892ec0cac315ef0497ab1978ba0e08bffb941b2360424aa314 | quote: | RTX 3090 Ampere | 24GB | $0.23/hr |
  - [1] 2026-11-24: the live GPU rate card is available as JSON without a key | capture: sha256:2104e9586d59eb892ec0cac315ef0497ab1978ba0e08bffb941b2360424aa314 | quote: GET [/api/gpu-pricing](/api/gpu-pricing)
  - [3] 2026-11-24: Runcrate publishes that it charges no egress fees | capture: sha256:0f12c8d12016056d97dcb33dc251dc9362a3dc13213d6d2637d8e84a1a2fcb21 | quote: No egress fees. You only pay for provisioned volume size.
  - [4] 2026-11-24: the inference API requires a bearer key and the anonymous response reports the authentication requirement | capture: sha256:aaf92c1f67e2e3e380fb6ba6d329ad089c900fc14b3a64008d7235784a9dc5b6 | quote: Missing API key. Pass Authorization: Bearer rc_live_...
  - [1] 2026-11-24: the H100 80GB rate is now USD 3.87 an hour | capture: sha256:2104e9586d59eb892ec0cac315ef0497ab1978ba0e08bffb941b2360424aa314 | quote: | H100 Hopper | 80GB | $3.87/hr |
  - [1] 2026-11-24: an L4 is listed at USD 0.58 an hour, correcting the record's note that none was listed | capture: sha256:2104e9586d59eb892ec0cac315ef0497ab1978ba0e08bffb941b2360424aa314 | quote: | L4 Ada Lovelace | 24GB | $0.58/hr |
  - [2] 2026-11-24: the sign-up form asks for name, email, password and confirmation plus an age consent checkbox | capture: sha256:db88879f55eb7bfbdb5e9c7b27ac2711570a3acbf5c64e76f0107c5bfe6fc8c7 | quote: Name Email Password Confirm password
  - [5] 2026-11-24: the provider registry names the API base URL as https://api.runcrate.ai/v1 | capture: sha256:17a73619f7113a4f534e1d2cd01bc8d3005ae376f11ced93c5a80b749ee2a38b | quote: API https://api.runcrate.ai/v1
- sources:
  - [1] https://www.runcrate.ai/pricing
  - [2] https://www.runcrate.ai/auth/signup
  - [3] https://runcrate.ai/docs/billing/pricing.md
  - [4] https://api.runcrate.ai/v1
  - [5] https://models.dev/providers/runcrate
