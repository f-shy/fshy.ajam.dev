# NEOXIS Corp.

> neoxis.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neoxis/ | JSON https://fshy.ajam.dev/api/v1/entity/neoxis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NEOXIS Corp.

- `compute/neoxis` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone yes, ID no, institution yes | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://neoxis.ai/pricing/
- free tier: no free tier is published; one fixed-term price for a whole 8x RTX PRO 6000 server, from USD 1.70 per GPU per hour, USD 13.60 an hour for the whole server and about USD 9,930 a month, excluding VAT. No hourly or on-demand instance; none of H100, A100, L40S, RTX 4090 or L4 is offered. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: the hourly figure is an equivalent for comparison; monthly figures use 730 hours
- per-object cap: not applicable | source: [1] | note: the whole server: eight GPUs, two AMD EPYC 9754 CPUs and 1.5 TB of memory
- retention: not applicable | source: [1] | note: a machine record: drives are purged at the end of a term
- egress: a dedicated 1 Gbps uplink with no traffic charges | metered: no | free allowance: unmetered | source: [1]
- identity: institution | detail: No self-service sign-up: a quote is requested by contact form, phone or WhatsApp, then a Master Services Agreement is signed electronically with company details, and the first month is paid in advance by bank transfer. Whether a private individual is accepted is unverified: behind a sign-up.
- interface: ssh
- limits note: No quota is stated; the constraint is the fixed monthly term and the quote-based onboarding of about 5 business days.
- binding note: the same as limits note
- interface detail: the page says root access, SSH keys and BMC remote console are provided; not probed
- tooling: root on the bare-metal host over SSH plus a BMC console, virtual media and power control; any OS from your own ISO
- composes with: A fixed-term whole-server rental, quoted rather than self-serve, with a 99.5% monthly availability SLA; the hourly equivalent is only a comparison with hourly offers.
- reliability: The aggregator profile states a single data centre near Sofia, Bulgaria, and a first node in production since July 2026.
- notes: Found via computeprices.com (provider slug neoxis; name on the index 'NEOXIS Corp.'). Its only offer is a whole-server fixed term, so no hourly card from the five asked about exists.
- evidence:
  - [1] 2026-11-03: one GPU per hour from USD 1.70 | capture: sha256:f7f5cf2ee62150702834f6bf4427f90128f7feddb9285b386b5bf9c7e363527f | quote: | One GPU, per hour | $1.70 |
  - [1] 2026-11-03: the whole 8-GPU server is USD 13.60 an hour | capture: sha256:f7f5cf2ee62150702834f6bf4427f90128f7feddb9285b386b5bf9c7e363527f | quote: | Whole server (8 GPUs), per hour | $13.60 |
  - [1] 2026-11-03: invoiced monthly in advance by bank transfer | capture: sha256:f7f5cf2ee62150702834f6bf4427f90128f7feddb9285b386b5bf9c7e363527f | quote: Invoiced monthly in advance and paid by bank transfer. The first month is paid before handover.
  - [2] 2026-11-03: company details are needed for the agreement and invoices | capture: sha256:0d67a67bd095dac45d2f17b5f491eb44fa310a26625ea65a19e6584110a3cd40 | quote: Company details. For the agreement and the monthly invoices.
  - [3] 2026-11-03: a signed MSA and first month in advance | capture: sha256:0009ef671d675dd984d8bfe16da77069390ae74dc49b1b7329ad4432d76874b7 | quote: A Master Services Agreement with the SLA attached, signed electronically. The first month is paid in advance by bank transfer.
  - [4] 2026-11-03: listed on the computeprices index at USD 1.70 an hour | capture: sha256:f92d45650b04dd3739b1a41f4b25cdd03872db480d1dfb4c3bf40b3e01619ed7 | quote: | [RTX PRO 6000](https://computeprices.com/providers/neoxis/gpus/rtx-pro-6000) | $1.70/hr | 96GB | 1×8× | — | — | 10/29/2026 | [Rent](https://neoxis.ai/pricing/?utm_source=computeprices&utm_medium=referral&utm_campaign=gpu-pricing) |
- sources:
  - [1] https://neoxis.ai/pricing/
  - [2] https://neoxis.ai/how-it-works/
  - [3] https://neoxis.ai/dedicated-gpu-server/
  - [4] https://computeprices.com/providers/neoxis
