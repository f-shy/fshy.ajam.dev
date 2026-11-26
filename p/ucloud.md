# UCloud Agent Sandbox

> ucloud.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ucloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ucloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UCloud Agent Sandbox

- `compute/ucloud` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID yes, institution no | verified 2026-11-24T13:21:06.619Z (live) | stale on 2026-12-25
- url https://astraflow.ucloud.cn/docs/agent-sandbox
- free tier: The fee page grants real-name verified accounts 480 CPU core-hours plus 960 GiB-hours of free Agent Sandbox use on first access, valid 30 days and claimable once per account (one 2C4G sandbox for 10 days or twenty 2C4G sandboxes for 12 hours), with vCPU billed by the second thereafter and the first 10 GB of local storage free. | unit: core-hours | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Every sandbox has outbound internet access by default and the platform controls it with allow and deny lists; the fee page bills vCPU, memory, local and persistent storage and publishes no per-GB outbound price. | metered: no | source: [1]
- identity: national-id | detail: The free grant requires a real-name verified account; the SDK authenticates with an API key from the key-management page.
- interface: cli, rest
- limits:
  - retention-clamped (binding): a sandbox can be paused and resumed with its full running state preserved [1]
  - per-object-cap: a Volume is independent of a sandbox and can mount into several, in beta [1]
  - write-gated: The fee page bills vCPU and memory by the second and grants the first 10 GB of local storage free with a 60 GB persistent-storage allowance; the quota page caps CPU at 8 cores, memory at 8 GB, 20 concurrent sandboxes and 10 GB of storage per user. [1]
- interface detail: Python SDK (`pip install ucloud-sandbox`), a CLI, an E2B-compatible SDK and a REST API are documented; authentication uses the UCLOUD_SANDBOX_API_KEY environment variable.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the documentation index was read on 2026-10-22 (Chinese) and states the pause-and-resume state model, the beta Volume and the E2B compatibility. The billing and quota pages it links were not read, so no figure is asserted
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: 24 hours hard cap on a single continuous run
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
  - [5] 2026-11-18:  | capture: sha256:7faadcd0503bb4cb648435d6aff0ea276c043926b9d03ed9d4a7540240b38230 | quote: 运行时长有上限**：沙箱的总运行时长默认不超过 24 小时，超时的沙箱会被强制回收，请及时保存重要数据。
  - [2] 2026-11-24: real-name verified accounts receive 480 CPU core-hours and 960 GiB-hours of free sandbox use for 30 days | capture: sha256:fb43eda6bee3c266b01354221bb2decb7d08b50a1e371bff85a5404470ab7fb5 | quote: 新用户免费额度：面向实名认证账号提供 Agent Sandbox 免费体验额度：实名认证账号首次访问Agent Sandbox时，赠送 480核时CPU＋960GiB时内存（支持1个2C4G沙箱持续运行10天或者20个2C4G沙箱持续运行12小时），有效期30天。
  - [2] 2026-11-24: vCPU bills by core count and runtime to the second, with no charge after the sandbox stops | capture: sha256:fb43eda6bee3c266b01354221bb2decb7d08b50a1e371bff85a5404470ab7fb5 | quote: | vCPU | 按照使用的 vCPU 核心数和运行时长计费，精确到秒。实时价格。沙箱停止后不再计费。 |
  - [6] 2026-11-24: every sandbox has outbound internet access by default | capture: sha256:e6623207d3b8b69ca2da107ed78f7178395d4b8179a82e5a9bfb10dc38425a44 | quote: 默认情况下，每个沙箱都拥有出站互联网访问权限。
  - [7] 2026-11-24: an API key from the key-management page is required | capture: sha256:f89b8d380eefbca93b10d79704604a6d72f89d71358fdb93e66e56444c6e93b7 | quote: 前往密钥管理页面获取您的 API 密钥：
  - [8] 2026-11-24: the platform exposes a REST API and sandbox ports | capture: sha256:de522cbda5fb09058f739e9166d5810a8803896a261bab7cc9c5056918dac33c | quote: 直接调用 REST API 或沙箱端口时，将返回 `429 Too Many Requests`
  - [4] 2026-11-24: the Python SDK is installed with pip | capture: sha256:65e175531f5a05dea74c5bee7a158c5d60a2430289b24671fa75cedc5a7f4b93 | quote: pip install ucloud-sandbox
- sources:
  - [1] https://astraflow.ucloud.cn/docs/agent-sandbox
  - [2] https://astraflow.ucloud.cn/docs/agent-sandbox/product/fee.md
  - [3] https://astraflow.ucloud.cn/docs/agent-sandbox/product/cli.md
  - [4] https://astraflow.ucloud.cn/docs/agent-sandbox/product/quickstart.md
  - [5] https://astraflow.ucloud.cn/docs/agent-sandbox.md
  - [6] https://astraflow.ucloud.cn/docs/agent-sandbox/network/internet-access.md
  - [7] https://astraflow.ucloud.cn/docs/agent-sandbox/product/prerequisites.md
  - [8] https://astraflow.ucloud.cn/docs/agent-sandbox/product/ratelimit.md
