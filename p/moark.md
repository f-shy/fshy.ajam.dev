# Moark

> moark.com | Inference, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/moark/ | JSON https://fshy.ajam.dev/api/v1/entity/moark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Moark

- `inference/moark` | paid-only | evidence unverified | binding none | category enterprise token governance platform
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-03
- url https://moark.com/
- free tier: unverified: the first-party apex is a Chinese-language enterprise Token governance pitch that says free registration to try the Token API, but states no free token allowance, price or quota | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free registration (免费注册) is advertised to try the Token API; signup fields are not stated on the page
- interface: rest
- binding note: no limit is stated on the page read
- endpoint: https://moark.com/v1
- tooling: an OpenAI-compatible key at api.moark.com/v1
- composes with: pairs with an OpenAI-compatible agent through a key; no free allowance is documented on the pages read
- reliability: no reliability event recorded
- notes: enterprise governance focus, not a self-serve free inference offer; recorded to stop rediscovery.
- evidence note: only the marketing apex and a short OpenAPI page were readable; no public price list or free-token allowance was found
- evidence:
  - [1] 2026-11-18: free registration is advertised but no free token allowance is stated | capture: sha256:52adcfda0a88a74c50e1b32e5ba680943933e23db17651f0db1c715a952e8d3e | quote: 免费注册，体验模力方舟 Token API 的强大能力。
- sources:
  - [1] https://moark.com/

## 模力方舟 / moark (formerly Gitee AI) — model & dataset hub

- `storage/moark-model-dataset-hub` | fails-quota | evidence reported | binding per-object-cap | category model-hub
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T21:14:11.824Z (live) | stale on 2026-12-04
- url https://moark.com
- free tier: Not published. Gitee documentation covers AI-model hosting where models are stored as LFS files in repositories. The platform mirrors open models and datasets, but publishes no separate storage allocation for the AI platform. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 50 MB per file | bytes: 50000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not stated; model downloads are free and anonymous. Gitee's general terms do not charge egress. | metered: no
- identity: email | detail: email + +86 phone (Gitee account).
- interface: git, cli
- limits:
  - per-object-cap (binding): 50 MB per file [1]
  - write-gated: review and takedowns of content it dislikes, which for a mutable repo is a technical a [1]
- limits note: The parent Gitee free account is the constraint and it is documented precisely: 1,000 repos, 500 MB per repo, 50 MB per file, 5 GB total across all personal and organizational repos, plus 100 MB per attachment and 1 GB of attachments per repo.
- interface detail: git
- tooling: git and git-lfs for model files, web downloader, and platform API and CLI at ai.gitee.com/docs. Documentation endpoint moark.com/docs returns HTTP 404.
- composes with: Inherits the Gitee account quota if the repo lives on Gitee proper. Which would cap it at 5 GB, making chaining the only route and a poor one.
- reliability: Gitee has a history of public-repo review and takedowns of content it dislikes, which for a mutable repo is a technical availability risk. The AI platform itself is a rebrand in progress (Gitee AI -> 模力方舟 -> moark.com), so links churn.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not published. Gitee's help centre documents the AI-model hosting flow (models are stored as LFS files inside a Gitee-style repo and the UI annotates each with its size), and 模力方舟 is presented as the successor platform that '同步了全球最热门的开源大模型和数据集' (mirrors the world's most popular open models and datasets).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: read live: '仓库容量 单仓库大小上限为 500M 单文件最大 50M 用户总仓库容量为 5G ... 附件单文件大小上限为 100MB 单仓库附件总容量 1G'
  - [1] 2026-10-21: read live: models are managed as LFS files with visible size annotations; 'Gitee 现推出了 模力方舟（原 Gitee AI）'
  - [3] 2026-10-21: read live: '模型与数据集 — 模力方舟同步了全球最热门的开源大模型和数据集'
  - [1] 2026-11-19: Gitee help still presents moark (formerly Gitee AI) as its model platform and documents LFS-annotated model files | capture: sha256:f75bf03e38a3486b42c2af597601fed9fa77db9890d9d79927b535cf63de2e2c | quote: Gitee 现推出了 [模力方舟（原 Gitee AI）](https://moark.com/) 平台，该平台汇聚了最新最热 AI 模型
  - [2] 2026-11-19: Gitee community free quota remains 500 MB per repository, 50 MB per file and 5 GB total repository capacity | capture: sha256:d5f31adea8087bc8c84501fddb8e1790f38aae8675aadd5e1f2c6c5d0b969284 | quote: 单仓库大小上限为 500M 单文件最大 50M 用户总仓库容量为 5G
  - [4] 2026-11-19: moark documentation still lists a models-and-datasets section mirroring open models and datasets which can be browsed and downloaded | capture: sha256:eb41226004551ca644ed8ab300d8c12110e266b81481fd9cb33c90f03f85e644 | quote: 模型与数据集模力方舟同步了全球最热门的开源大模型和数据集，方便您进行浏览与下载。
- sources:
  - [1] https://help.gitee.com/enterprise/code-manage/code-hosting/large-file-manage/ai-model-hosting
  - [2] https://help.gitee.com/account/usage-quota
  - [3] https://ai.gitee.com/docs/getting-started/intro
  - [4] https://moark.com/docs
