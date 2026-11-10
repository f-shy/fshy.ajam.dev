# Runcrate

> runcrate.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runcrate/ | JSON https://fshy.ajam.dev/api/v1/entity/runcrate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runcrate

- `compute/runcrate` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://www.runcrate.ai/pricing
- free tier: no free GPU tier is published; the live rate card read on 2026-11-03 lists 19 GPU types from USD 0.36 an hour: H100 80GB USD 3.86, A100 80GB USD 1.73, L40S 48GB USD 0.54, L40 USD 0.47, RTX 4090 USD 0.57, H200 USD 4.63, B200 USD 7.67. No L4 is listed. Billed by the second on most GPUs and by the minute on a few; booting is never billed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: prepaid terms of 1 to 12 months are up to 15% off; the aggregator shows H100 SXM at USD 2.49 where the provider rate card shows USD 3.86
- per-object cap: not applicable | source: [1] | note: storage volumes of 10 GB to 10,000 GB at USD 0.03 per GB a month are a separate line
- retention: not applicable | source: [1] | note: credits do not expire; storage volumes are kept when the instance is deleted
- egress: not published on the pages read | metered: no | source: [1]
- identity: card | detail: The sign-up form asks for name, email, password and an age or consent checkbox; balance is added by card before use, from USD 20 to USD 10,000 at a time. Reserved multi-node clusters need a verification of the company and the need. No phone or ID document is stated for self-serve.
- interface: rest, cli, ssh
- limits:
  - write-gated (binding): a launch needs USD 10 or an hour of the machine, whichever is more; a balance is added by card from USD 20 [1]
- limits note: A launch is gated on a prepaid balance added by card; there is no free allowance.
- binding note: the same as limits note
- interface detail: taken from the pricing page, which lists SSH, a CLI and an unauthenticated /api/gpu-pricing endpoint; not probed
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
  - [3] 2026-11-03: the aggregator lists an L4 for Runcrate at USD 1.24 an hour | capture: sha256:ba188a70377a2a7eeba069ea9eb10b87a6553745984b147adf872c6461cbeb80 | quote: | [L4](https://computeprices.com/providers/runcrate/gpus/l4)1× | $1.24/hr |
- sources:
  - [1] https://www.runcrate.ai/pricing
  - [2] https://www.runcrate.ai/auth/signup
  - [3] https://computeprices.com/providers/runcrate
