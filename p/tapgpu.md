# TAPGPU

> tapgpu.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tapgpu/ | JSON https://fshy.ajam.dev/api/v1/entity/tapgpu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TAPGPU (listed as Stability Cloud)

- `compute/tapgpu` | paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:22.537Z (live) | stale on 2026-12-04
- url https://tapgpu.com/
- free tier: No free tier stated; GPU instances are billed per hour in yuan from an Alipay-funded balance, with a new-user price on the first instance. Prices are shown only in the console: no H100, A100 80 GB, L40S, RTX 4090 or L4 rate is published on the page read. Models named: RTX 4090, 5090, 3090, A100, H100, H200, L40S, A40, RTX A6000, 6000 Ada and RTX PRO 6000 in 1, 2, 4 or 8 card configurations; monthly rental of a whole machine is available. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: not applicable | source: [1]
- egress: not published on the pages read | metered: no | source: [1]
- identity: country-phone | detail: unverified: behind a sign-up. The page says to register or log in and top up the balance through Alipay, the only payment method stated, and names no email, phone or ID field; an Alipay balance normally ties the account to a mainland-China payment identity, which is not stated on the page read. | country: China (Alipay payment)
- interface: ssh
- limits:
  - write-gated (binding): the balance can only be funded through Alipay and every price is console-only [1]
- limits note: Payment is Alipay only and prices are shown only inside the console after sign-in, so a rate cannot be read without an account.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: A web console with application templates (Stable Diffusion WebUI, ComfyUI, LoRA trainers, Text Generation WebUI), Jupyter terminal and SSH; data and shared model disks bill separately after an instance stops.
- composes with: A Chinese-language GPU rental for image and video generation workloads; the only payment route stated is Alipay, which limits it to readers who hold an Alipay balance.
- reliability: No reliability event was observed; the page warns that storage can keep billing after an instance stops and that data is unrecoverable after the instance or storage is deleted.
- notes: Found via computeprices as Stability Cloud (slug tapgpu, recently added, under review); the vendor's own page is branded TAPGPU. Its prices are tracked by the index but not yet published there. The vendor lists operator TAPGPU and a support contact; no registration number is stated.
- evidence:
  - [2] 2026-11-03: the index lists the provider as Stability Cloud, recently added and under review, tracking 3 prices that are not yet shown | capture: sha256:5234e90b624fb1f229e033455752324621bdc1b5165fbd7f3d7956960d32aa84 | quote: Stability Cloud provides GPU rental services with a variety of models designed for different computing tasks, including AI training and rendering.
  - [1] 2026-11-03: the vendor page publishes no price: the models, counts and prices are shown live in the console | capture: sha256:a3054aa1cb536f50f022a69c33a86cdbd51388da9a16d540b1b005c460e8a5c8 | quote: 支持 1 / 2 / 4 / 8 卡配置。实际可用型号、数量与价格以控制台实时显示为准。
  - [1] 2026-11-03: the vendor page names the A100, H100, H200 and L40S as data-centre options and lists the RTX 4090 in the consumer tier; no L4 is named | capture: sha256:a3054aa1cb536f50f022a69c33a86cdbd51388da9a16d540b1b005c460e8a5c8 | quote: A100、H100、H200、L40S、A40 等，适合大模型训练与大显存任务。
  - [1] 2026-11-03: the only payment method stated is Alipay top-up | capture: sha256:a3054aa1cb536f50f022a69c33a86cdbd51388da9a16d540b1b005c460e8a5c8 | quote: 目前支持支付宝在线充值。
  - [1] 2026-11-03: step 1 of use is to register or log in and top up the balance through Alipay | capture: sha256:a3054aa1cb536f50f022a69c33a86cdbd51388da9a16d540b1b005c460e8a5c8 | quote: 1. 注册 / 登录 TAPGPU 账户，并通过支付宝充值余额。
- sources:
  - [1] https://tapgpu.com/
  - [2] https://computeprices.com/providers/tapgpu
