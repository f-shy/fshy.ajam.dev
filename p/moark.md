# 模力方舟

> moark.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/moark/ | JSON https://fshy.ajam.dev/api/v1/entity/moark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 模力方舟 / moark (formerly Gitee AI) — model & dataset hub

- `storage/moark-model-dataset-hub` | fails-quota | evidence reported | binding per-object-cap | category model-hub
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://help.gitee.com/enterprise/code-manage/code-hosting/large-file-manage/ai-model-hosting
  - [2] https://help.gitee.com/account/usage-quota
  - [3] https://ai.gitee.com/docs/getting-started/intro
