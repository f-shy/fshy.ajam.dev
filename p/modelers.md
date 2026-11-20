# Modelers 魔乐社区

> modelers.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modelers/ | JSON https://fshy.ajam.dev/api/v1/entity/modelers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modelers 魔乐社区 (modelers.cn, Huawei/Ascend ecosystem)

- `storage/modelers` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category model-hub
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://modelers.cn
- free tier: Not published. The platform hosts models, datasets, and Spaces, using the openMind Hub Client for Ascend hardware. The contribution guide specifies 'git lfs track' for files larger than 100 MB. No explicit total storage ceiling is published in documentation. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap, account quota, retention, or rate limit found | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter documented; models download through both the web and the openMind client anonymously. CN-network served. | metered: no
- identity: email | detail: email + +86 phone (Huawei-adjacent Chinese community); access token required for any write.
- interface: git
- limits:
  - per-object-cap (binding): No per-file cap, account quota, retention, or rate limit found [1]
- limits note: Unverified. git-LFS 100 MB+ tracking threshold documented. No per-file cap, account quota, retention, or rate limit found. Upload requires an access token with Write scope created in the personal centre.
- interface detail: part of the free tier
- tooling: First-party openMind Hub Client (pip) with upload/download by repo_id, plus git+LFS, plus a web UI. Documented at modelers.cn/docs/zh/openmind-hub-client. This is a genuine HF drop-in: repo types are 'model', 'dataset', 'space', same as HF.
- composes with: N repos per account, free. The strategic value is that it is the domestic Ascend/MindSpore hub, so it is the natural place a Chinese-ecosystem user would park multi-hundred-GB checkpoints.
- reliability: API surface is opaque: https://modelers.cn/api/v1/models returns 404, and model detail pages return a 1,638-byte SPA shell regardless of path. So anonymous programmatic access is effectively absent; you need the openMind client.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: '在本地Git仓库中追踪大型文件（100MB以上）', git lfs upload flow, write-scoped access token required
  - [2] 2026-10-21: read live: 'Models', 'Spaces', 'openMind Library', 'openMind Hub Client — Easily search for, upload, and download pre-trained models'; dataset upload guide dated 2024-09-22
  - [3] 2026-10-21: probe: GET -> 404; GET https://modelers.cn/models/OpenMind/DeepSeek-R1-Distill-Qwen-7B -> 200 but 1,638-byte SPA shell; POST .../info/lfs/objects/batch -> 404 (returns the SPA shell, not LFS JSON)
- sources:
  - [1] https://modelers.cn/docs/zh/best-practices/community_contribution/model_contribution.html
  - [2] https://modelers.cn/
  - [3] https://modelers.cn/api/v1/models?per=2
