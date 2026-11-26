# Voltage Park

> voltagepark.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/voltagepark/ | JSON https://fshy.ajam.dev/api/v1/entity/voltagepark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Voltage Park

- `compute/voltage-park` | paid-only | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-24T14:51:50.061Z (live) | stale on 2026-12-25
- url https://www.voltagepark.com/pricing
- free tier: No free tier is listed: on-demand and long-term reserve H100 capacity is contact for pricing, with 1 to 1,016 HGX H100 GPUs for bursts and 32 to 8,000+ in a single configuration, and no hidden ingress, egress or support costs. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: The pricing page states there are no hidden ingress, egress or support costs and lists no price or allowance for network traffic. | metered: no | source: [1]
- identity: email | detail: The pricing page offers contact-for-pricing and a registration link; it does not state which fields registration asks for.
- interface: unknown
- limits:
  - request-rate (binding): HGX H100 capacity from 1 to 1,016 GPUs for bursts, or 32 to 8,000+ in one configuration on a contract [1]
  - per-ip-shaping: no ingress, egress or support costs are charged [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the cluster sizes, the contract terms and the zero-cost network position. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: NVIDIA HGX H100
  - shape.gpu_count: 8
  - shape.note: single-GPU bursts through to 8,000+ H100s in one configuration
  - session_cap.restart_required: no
  - session_cap.note: burst capacity and six-month contracts; the page states no per-session clock
  - free_tier_kind: none
  - net.out: yes
  - net.in: yes
  - net.allowance: no ingress, egress or support costs
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'No hidden ingress, egress or support costs.' with '1-1016 HGX H100 GPUs for your bursts and experimentation', '32-8000+ H100 GPUs in a single configuration' and 'Harness enterprise NVIDIA GPU cloud access when you need it and only pay for what you use', quoted
  - [2] 2026-10-22: quoted: 'Voltage Park rents 1 GPU model today, from $1.99 an hour (H100, on-demand)' and 'Voltage Park's H100 is 40% below' the USD 3.29 market median
  - [3] 2026-10-22: the tracker names this support article as the source of the rate, which is the page that would raise the rung to documented
  - [1] 2026-11-24: the pricing page states no hidden ingress, egress or support costs | capture: sha256:a3a1d256a6ccc5ad8468685ff246657f7b1259e54cfd12174a3d8c936df97292 | quote: No hidden ingress, egress or support costs.
  - [1] 2026-11-24: the burst range is stated and the page lists no free tier | capture: sha256:a3a1d256a6ccc5ad8468685ff246657f7b1259e54cfd12174a3d8c936df97292 | quote: 1-1016 HGX H100 GPUs for your bursts and experimentation.
  - [1] 2026-11-24: the pricing page links to registration but names no fields | capture: sha256:a3a1d256a6ccc5ad8468685ff246657f7b1259e54cfd12174a3d8c936df97292 | quote: [Contact Us](https://voltagepark.com/register)
  - [1] 2026-11-24: the long-term reserve configuration range is stated | capture: sha256:a3a1d256a6ccc5ad8468685ff246657f7b1259e54cfd12174a3d8c936df97292 | quote: 32-8000+ H100 GPUs in a single configuration.
  - [1] 2026-11-24: no hidden ingress, egress or support costs | capture: sha256:a3a1d256a6ccc5ad8468685ff246657f7b1259e54cfd12174a3d8c936df97292 | quote: No hidden ingress, egress or support costs.
- sources:
  - [1] https://www.voltagepark.com/pricing
  - [2] https://gpurentalprices.com/providers/voltagepark
  - [3] https://support.voltagepark.com/article/example-deploying-gpt-oss-on-voltage-park
