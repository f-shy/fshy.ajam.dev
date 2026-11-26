# Modelers 魔乐社区

> modelers.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modelers/ | JSON https://fshy.ajam.dev/api/v1/entity/modelers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Modelers 魔乐社区 (modelers.cn, Huawei/Ascend ecosystem)

- `storage/modelers` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category model-hub
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T21:21:14.519Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://modelers.cn
- free tier: Not published. The platform hosts models, datasets, and Spaces, using the openMind Hub Client for Ascend hardware. The contribution guide specifies 'git lfs track' for files larger than 100 MB. No explicit total storage ceiling is published in documentation. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: The FAQ quotes the upload prompt 'The size of each file should be within 100MB'. | source: [1] | note: The FAQ quotes the upload prompt 'The size of each file should be within 100MB'.
- retention: source: [1] | note: unverified: no retention period stated in the contribution guide or FAQ
- egress: No egress meter documented; models download through both the web and the openMind client anonymously. CN-network served. | metered: no
- identity: email | detail: email + +86 phone (Huawei-adjacent Chinese community); access token required for any write.
- interface: git
- limits:
  - per-object-cap (binding): The size of each file should be within 100MB [1]
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
  - [4] 2026-11-25: the FAQ quotes a per-file upload prompt of 100MB | capture: sha256:bf0e8a567e33bb3d774ff7e384c45135e799a5d27efe1a635b7a7699d768d893 | quote: 上传模型或数据集时，提示“The size of each file should be within 100MB”时怎么处理？
  - [4] 2026-11-25: the FAQ advises deleting and re-uploading the relevant files | capture: sha256:bf0e8a567e33bb3d774ff7e384c45135e799a5d27efe1a635b7a7699d768d893 | quote: 1. 删除该仓库下的相关文件重新上传。
  - [5] 2026-11-25: the download guide lists Git, the web interface and openMind Hub Client | capture: sha256:14390b3b6e31e8abbd9fbbce6069cec9962200003c533039c78cf68542c2a946 | quote: 支持通过Git命令、Web界面和openMind Hub Client等方式下载模型，用户可根据实际需求选择下载方式。
- sources:
  - [1] https://modelers.cn/docs/zh/best-practices/community_contribution/model_contribution.html
  - [2] https://modelers.cn/
  - [3] https://modelers.cn/api/v1/models?per=2
  - [4] https://modelers.cn/docs/zh/community/others/frequently_asked_questions.html
  - [5] https://modelers.cn/docs/zh/community/models/downloading_models.html
