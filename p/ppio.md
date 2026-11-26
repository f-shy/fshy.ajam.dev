# PPIO GPU

> ppio.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ppio/ | JSON https://fshy.ajam.dev/api/v1/entity/ppio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PPIO Agent Sandbox

- `compute/ppio-sandbox` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:51.744Z (live) | stale on 2026-12-26
- url https://ppio.com/docs/sandbox/pricing.md
- free tier: PPIO Sandbox（后简称“沙箱”）支持 vCPU 与内存（RAM）按秒独立计费，按需使用、灵活计费。 | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: unverified: the signup form was not read. Registration offers a phone number or an account; identity verification needs a China-mainland phone number, face recognition or a bank card, and an unverified account cannot deploy a sandbox. `email` is the nearest vocabulary term, not an observed gate.
- interface: cli
- limits:
  - request-rate: vCPU bills per core per second at CNY 0.00003 and RAM at CNY 0.000015 per GiB-second; billing stops when the sandbox stops [1]
  - write-gated (binding): 20 GB of local sandbox storage is free; each account gets 60 GB of free persistent storage, beyond which CNY 0.0005 per GB-hour applies [1]
- interface detail: A Python and JS SDK with a CLI, an E2B-compatible SDK, and SSH over a WebSocket proxy with SCP or SFTP file transfer
- tooling: the ppio-sandbox Python or JS SDK and CLI, with SSH available on a sandbox template built with an SSH server
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing documentation was read on 2026-11-24 in Chinese. It defines per-second billing on vCPU and RAM with billing stopped on sandbox stop, free local and persistent-storage allowances; the signup form was not read.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: billing stops when a sandbox stops, so stopping is the cost lever; the page states no automatic reap
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'PPIO Sandbox 支持 vCPU 与内存（RAM）按秒独立计费' - vCPU and RAM bill separately per second - with '沙箱停止后不再计费' on both rows: billing stops when a sandbox stops. The page states no free tier and points at an account voucher balance
  - [1] 2026-11-25: vCPU and RAM bill independently by the second, on demand | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: PPIO Sandbox（后简称“沙箱”）支持 vCPU 与内存（RAM）按秒独立计费，按需使用、灵活计费。
  - [1] 2026-11-25: vCPU billing is per second and stops when the sandbox stops | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: | vCPU | 按照使用的 vCPU 核心数和运行时长计费，精确到秒，当前定价可参考 [价格页](https://ppio.com/pricing?sandbox=1) 实时价格。沙箱停止后不再计费。 |
  - [1] 2026-11-25: persistent storage bills by the day with a 60 GB free allowance | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: | 持久化存储 | 模板（Template）、快照（Snapshot）会保存为持久化存储。持久化存储按天计费，提供 60GB 免费额度。具体价格请参考 [价格页](https://ppio.com/pricing?sandbox=1)。 |
  - [1] 2026-11-25: a sandbox is allocated 20 GB of local storage at no charge | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: | 本地存储空间 | 沙箱启动时会自动分配 20GB 本地存储空间，用于运行环境。 本地存储免费，不产生费用。 |
  - [1] 2026-11-25: vouchers (代金券) are an account balance used to settle bills, not a published free tier | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: 结算账单时，如果账户的可用额度（包括账户可用余额和代金券余额）小于待支付的账单，则视为账户欠费。
  - [1] 2026-11-25: vCPU and RAM bill by the second at published per-second rates, billing stops on sandbox stop, 20 GB local storage and a 60 GB persistent-storage allowance are free, and vouchers are an account balance | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: PPIO Sandbox（后简称“沙箱”）支持 vCPU 与内存（RAM）按秒独立计费，按需使用、灵活计费。 ... | vCPU | 按照使用的 vCPU 核心数和运行时长计费，精确到秒，当前定价可参考 [价格页](https://ppio.com/pricing?sandbox=1) 实时价格。沙箱停止后不再计费。 | ... | 本地存储空间 | 沙箱启动时会自动分配 20GB 本地存储空间，用于运行环境。 本地存储免费，不产生费用。 | ... | 持久化存储 | 模板（Template）、快照（Snapshot）会保存为持久化存储。持久化存储按天计费，提供 60GB 免费额度。具体价格请参考 [价格页](https://ppio.com/pricing?sandbox=1)。 | ... | 1 | ￥0.00003/s | ... 结算账单时，如果账户的可用额度（包括账户可用余额和代金券余额）小于待支付的账单，则视为账户欠费。
  - [1] 2026-11-24: each account gets 60 GB of free persistent storage, then CNY 0.0005 per GB-hour | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: 每个账号享受 60GB 免费存储额度，超出部分按量计费 | ￥0.0005/GB/h
  - [1] 2026-11-24: vCPU and RAM bill independently per second | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: PPIO Sandbox（后简称“沙箱”）支持 vCPU 与内存（RAM）按秒独立计费，按需使用、灵活计费。
  - [1] 2026-11-24: 20 GB of local sandbox storage is allocated free of charge | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: 沙箱启动时会自动分配 20GB 本地存储空间，用于运行环境。 本地存储免费，不产生费用。
  - [2] 2026-11-24: the SDK and CLI are the documented way to launch a sandbox | capture: sha256:4ebef2c0c29f18ab403cf2a34f1f9f006390db97beb5b46e366131d088c45099 | quote: pip install ppio-sandbox
  - [3] 2026-11-24: SSH access to a sandbox over a WebSocket proxy is documented | capture: sha256:560205261d30503cce86cba0f628156be00eec130a44b2daba2aa2a451f13d62 | quote: 你可以使用 WebSocket 代理，通过 SSH 连接到你的 Sandbox。
  - [3] 2026-11-24: file transfer over SCP or SFTP is documented alongside SSH | capture: sha256:560205261d30503cce86cba0f628156be00eec130a44b2daba2aa2a451f13d62 | quote: 通过 SCP 或 SFTP 等协议传输文件
  - [4] 2026-11-24: an unverified account cannot deploy a sandbox | capture: sha256:b6a07433827c657bbfb152f0ee83261cfca7150a436886b17a8437ed894e3eec | quote: | 部署 Sandbox 等算力资源 | 不可用 |
  - [5] 2026-11-24: CPU and RAM bill per second and storage bills per day | capture: sha256:719a5c6caa0403db0afaed38ba6708029ca6c6b4e4c055fe9dc5d07a062bd44f | quote: CPU 和 RAM 按秒计费。存储(包括 Template、已暂停的 Sandbox 和 Snapshot)按天收费。更多详情请参阅[定价页面](https://ppio.com/docs/sandbox/pricing.md)。
  - [6] 2026-11-24: registration uses a phone number or an account | capture: sha256:0e4c773cc5b35b3223c6f5b85920eebc224d3a40d4769ae75d301fa7339189e8 | quote: 访问[注册页面](https://ppio.com/user/register)，通过手机号注册或账号注册的方式来注册新账号。
  - [7] 2026-11-24: sandbox internet access is on by default and can be disabled; no per-GB price is stated | capture: sha256:178ed301b8a0a036f68d7c51cf289fcd75cc1adb759a36e5c1f0c2d152286b48 | quote: 每个 Sandbox 默认启用互联网访问,但对于需要隔离的工作负载,你可以将其禁用。
  - [1] 2026-11-24: billing stops when a sandbox stops | capture: sha256:07a3635d7511a3f50333feacbac326ba1a7bac3bd2b575799d5fe8e1d8a28115 | quote: 沙箱停止后不再计费。
  - [4] 2026-11-24: personal identity verification offers named alternatives | capture: sha256:b6a07433827c657bbfb152f0ee83261cfca7150a436886b17a8437ed894e3eec | quote: 个人认证支持以下三种方式：
- sources:
  - [1] https://ppio.com/docs/sandbox/pricing.md
  - [2] https://ppio.com/docs/sandbox/get-start.md
  - [3] https://ppio.com/docs/sandbox/sandbox-ssh-access.md
  - [4] https://ppio.com/docs/support/identity-verification.md
  - [5] https://ppio.com/docs/sandbox/overview.md
  - [6] https://ppio.com/docs/support/quickstart.md
  - [7] https://ppio.com/docs/sandbox/sandbox-internet-access.md

## PPIO GPU

- `compute/ppio-gpu` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone unknown, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ppio.com/ai-computing/gpu-instance
- free tier: RTX 4090 24GB in a 16 vCPU / 62 GiB container at CNY 2.31 per card-hour on demand or CNY 1.16 per card-hour preemptible; H20 96GB at CNY 6.80 or CNY 3.40; H100 SXM 80GB at CNY 23.76 or CNY 11.88; H200 141GB listed as new stock. Storage is free to 100 GB and the page states preemptible capacity saves about 50 percent, quoted. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The GPU page links to ppio.com/user/register, but the form fields were not read, so whether a mainland mobile number or a real-name check is required is not established. The provider is a mainland company with an international storefront.
- interface: unknown
- limits note: Nothing is metered except wall-clock GPU time. The spot lane is the first thing to fail, because a preemptible 4090 at CNY 1.16 is reclaimable and the on-demand price is exactly double.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A preemptible 4090 at CNY 1.16 an hour with 100 GB of free storage is the cheapest way to run a fine-tune that checkpoints often; the reclaim is the price of it.
- reliability: no reliability event recorded
- notes: The aggregator's 0 percent preemption figure is a measurement of the aggregator on 2026-10-22, not a guarantee from the vendor.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 16
  - facets.shape.ram_gib: 62
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: price cards for RTX 4090 24GB at ￥2.31/卡时 on demand and ￥1.16/卡时 preemptible, H20 96GB at ￥6.80 and ￥3.40, H100 SXM 80GB at ￥23.76 and ￥11.88, quoted
  - [1] 2026-10-22: page states 免费存储 100GB (100 GB of free storage) and 成本节省50% for preemptible capacity, quoted
  - [2] 2026-10-22: an independent price aggregator lists PPIO 4090 at USD 0.346 on demand and USD 0.174 spot in CN, with an observed preemption rate of 0 percent, consistent with the vendor figures at CNY 6.67 per USD
- sources:
  - [1] https://ppio.com/ai-computing/gpu-instance
  - [2] https://www.suanli.ai/gpus/RTX-4090
