# Tencent Cloud Studio

> tencent.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tencent-2/ | JSON https://fshy.ajam.dev/api/v1/entity/tencent-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tencent Cloud Studio

- `compute/tencent-cloud-studio` | qualifies-with-caveat | evidence documented | binding retention-clamped | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.388Z (live) | stale on 2026-12-05
- url https://cloud.tencent.cn/document/product/1039/131894
- free tier: 免费额度内每月提供5万分钟通用工作空间使用时长和1万分钟高性能空间使用时长，超出后按量计费。- inside the free allowance, 50,000 minutes a month of general workspace time and 10,000 minutes a month of high-performance workspace time; billed on demand beyond it | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: monthly-allowance
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the Cloud Studio billing page prices machine-hours per shape and states no egress allowance or overage price | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - request-rate: a machine-hour is deducted by a per-shape factor: 0.1 for 1 core and 2 GB, 1 for 8 cores and 16 GB, 14 for an A800 [1]
  - retention-clamped (binding): a prepaid resource package deducts machine-hours until it is exhausted, then billing switches to pay-as-you-go automatically [1]
- binding note: the 10,000 high-performance minutes a month and the 30-day idle release bind first; beyond the allowance the workspace bills on demand rather than stopping
- interface detail: Tencent Cloud API 3.0 (workspace create, modify, stop, query; API Explorer) and a browser IDE with terminal; free high-performance workspaces do not support API calls
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only was wrong. Cloud Studio (product 1039) publishes a monthly minute allowance for general and high-performance workspaces. A second regime runs at cloudstudio.net, where machine-hours are granted and expire in 7 days. Caveats: an exhausted pack does not stop the application and bills on demand, a free high-performance workspace idle for 30 days is released without recovery, and reaching the paying account needs Tencent Cloud real-name verification, which the China site issues for mainland, Hong Kong, Macau and Taiwan documents. The earlier free_tier sentence read 'no free tier', which contradicted the verdict; the minute allowance is the free tier and the machine-hour regime at cloudstudio.net is the second product.
- evidence note: the billing document was read on 2026-10-22 (Chinese). It defines a machine-hour deduction factor per shape and states that a package transfers to pay-as-you-go when exhausted. There is no free tier, so the record's USD 2.98 credit is not established
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 16
  - shape.ram: 32
  - shape.note: 16 cores and 32 GB has a factor of 2; an A10 is 3.3, an A800 is 14
  - session_cap.restart_required: no
  - session_cap.note: billing is a machine-hour factor; the document states no session clock
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: a 抵扣因子 (deduction factor) table: 'CPU 1核 2G 0.1', 'CPU 16核 32G 2', 'CPU 64核 128G 7', 'GPU T4 1.2', 'GPU V100 3.6', 'GPU A10 3.3', 'GPU L40 8', 'GPU A800 14', with the worked example '2.0×1 + 3.3×0.5 = 3.65 机时', quoted
  - [2] 2026-10-22: '免费额度内每月提供5万分钟通用工作空间使用时长和1万分钟高性能空间使用时长，超出后按量计费。' - 50,000 minutes a month of general workspace time and 10,000 minutes a month of high-performance workspace time inside the free allowance, billed on demand beyond it, quoted in the original
  - [1] 2026-11-03: the billing page prices machine-hours only and states no egress allowance or overage | capture: sha256:c77eeff6deb8970d2de7a255320fd69b5ff1af252139645104deea7a8c3f1452 | quote: | 资源包（预付费） | 想先充值一笔、统一管理预算 | 按“抵扣因子”扣减机时；资源包用尽后自动转按量付费 |
  - [2] 2026-11-03: a Tencent Cloud API 3.0 interface exists for workspaces | capture: sha256:8ec14fcdb013f6349614f281d98338888371fed5892c4c56ec7e9714ad4371dd | quote: 本章节介绍的 Cloud Studio API 接口均为 API 3.0 接口。
  - [2] 2026-11-03: free high-performance workspaces cannot be driven by the API | capture: sha256:8ec14fcdb013f6349614f281d98338888371fed5892c4c56ec7e9714ad4371dd | quote: 免费高性能工作空间暂不支持 API 调用。
- sources:
  - [1] https://cloud.tencent.cn/document/product/1039/131894
  - [2] https://cloud.tencent.com/document/product/1039/94098
