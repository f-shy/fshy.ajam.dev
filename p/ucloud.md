# UCloud Agent Sandbox

> ucloud.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ucloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ucloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UCloud Agent Sandbox

- `compute/ucloud` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.818Z (live) | stale on 2026-12-05
- url https://astraflow.ucloud.cn/docs/agent-sandbox
- free tier: no published free tier: sandboxes pause and resume with full state preserved, a Volume is independent persistent storage that mounts into several sandboxes in beta, and the API has an E2B compatibility mode | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the fee page (https://astraflow.ucloud.cn/docs/agent-sandbox/product/fee.md) lists vCPU, memory, local storage and persistent storage and no outbound transfer allowance or price; every sandbox has outbound internet access by default | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - retention-clamped (binding): a sandbox can be paused and resumed with its full running state preserved [1]
  - per-object-cap: a Volume is independent of a sandbox and can mount into several, in beta [1]
  - write-gated: the billing and quota details are on pages this record does not cite [1]
- interface detail: Python SDK (`pip install ucloud-sandbox`, authenticated with `UCLOUD_SANDBOX_API_KEY`), the UCloud Sandbox CLI and an E2B-compatible mode; no SSH or REST reference read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the documentation index was read on 2026-10-22 (Chinese) and states the pause-and-resume state model, the beta Volume and the E2B compatibility. The billing and quota pages it links were not read, so no figure is asserted
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: pause keeps the full running state, so a stop is a pause; the docs state no automatic reap
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.price: priced on the fee page this record does not cite
  - ps.durability: Volume, independent of the sandbox and mountable to several; snapshots supported
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '| 数据持久化 | 暂停并恢复沙箱，保留完整运行状态 |' - pause and resume a sandbox keeping the full running state - with '| Volume | 独立于沙箱的持久化存储，可挂载到多个沙箱（内测中）|' and 'E2B 兼容模式', quoted
  - [2] 2026-11-03: the fee page's billing items are vCPU, memory, local and persistent storage | capture: sha256:fb43eda6bee3c266b01354221bb2decb7d08b50a1e371bff85a5404470ab7fb5 | quote: | vCPU | 按照使用的 vCPU 核心数和运行时长计费，精确到秒。实时价格。沙箱停止后不再计费。 |
  - [3] 2026-11-03: a CLI exists | capture: sha256:99953862d1e19dda9e9b30eec3d6de97db7b69cbc0cc99194fd57c6c0766d273 | quote: 强大的命令行工具，用于本地管理沙箱生命周期、构建模板及执行运维任务。
  - [4] 2026-11-03: a Python SDK exists | capture: sha256:65e175531f5a05dea74c5bee7a158c5d60a2430289b24671fa75cedc5a7f4b93 | quote: pip install ucloud-sandbox
- sources:
  - [1] https://astraflow.ucloud.cn/docs/agent-sandbox
  - [2] https://astraflow.ucloud.cn/docs/agent-sandbox/product/fee.md
  - [3] https://astraflow.ucloud.cn/docs/agent-sandbox/product/cli.md
  - [4] https://astraflow.ucloud.cn/docs/agent-sandbox/product/quickstart.md
