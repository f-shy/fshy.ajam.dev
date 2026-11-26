# OpenCSG 传神社区

> opencsg.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencsg/ | JSON https://fshy.ajam.dev/api/v1/entity/opencsg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenCSG 传神社区 (CSGHub SaaS, opencsg.com / hub.opencsg.com)

- `storage/opencsg` | qualifies-with-caveat | evidence documented | binding retention-clamped | category model-hub
- needs card no, phone yes, ID yes, institution no | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://opencsg.com
- free tier: No published byte quota anywhere in the docs. And this is deliberate: the upload page states verbatim '上传大小和超时限制由站点、代理和存储配置决定' (upload size and timeout limits are determined by the site, proxy and storage configuration) and explicitly warns '不要把站点限制理解为 Git LFS 协议的统一上限' (do not read a site limit as a universal Git LFS protocol ceiling). What is measurable instead is what they actually host: the canonical deepseek-ai/DeepSeek-V3 repo is 176 files totalling 688.6 GB, of which 163 are shards above 1 GB. That is a single repo at 0.69 TB, i.e. the repo-level ceiling is at minimum ~700 GB and is shard-driven, not quota-driven. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: (b) Presigned OSS URLs carry X-Amz-Expires=259200. 72 hours, so re-resolve per request rather than caching a URL (§1b's expiring-redirect rule). | days: 3 | source: [1] | note: not stated
- egress: Free and unmetered. Reads are served from opencsg-gitea-lfs-new.oss-cn-beijing.aliyuncs.com (Alibaba Cloud OSS, Beijing) via presigned URLs; no per-GB line, no egress meter, no bandwidth charge appears in any billing doc. The only billing surface is the AI gateway (Token spend), not bytes. | metered: no
- identity: national-id | detail: email + any phone + password. Docs state registration collects 'username, password, phone number, and email'. No national-ID or card requirement documented for the SaaS.
- interface: rest, git, rclone, cli
- limits:
  - per-ip-shaping: 2.70 MB/s [1]
  - per-ip-shaping: 1.16 MB/s [1]
  - retention-clamped (binding): Expires=259200. 72 hours. [1]
- limits note: The real limits measured live, not documented: (a) the plain resolve path is NOT the download path. Https://hub.opencsg.com/models/Qwen/Qwen3-8B/resolve/main/model-00001-of-00005.safetensors returns HTTP 200 with a 135-byte Git-LFS pointer (Content-Type: text/plain), which is exactly the round-2 'status-code theatre' trap. You must POST the LFS batch endpoint to get bytes. (b) Presigned OSS URLs carry X-Amz-Expires=259200. 72 hours, so re-resolve per request rather than caching a URL (§1b's expiring-redirect rule). (c) Per-stream shaping is severe: 2.70 MB/s on one connection (16 MiB in 6.2 s) and 1.16 MB/s on a 32 MiB pull; 8 parallel ranged GETs reached 14.49 MB/s and 15.50 MB/s across two separate tests. That is near-linear scaling (5.4x at 8 streams), i.e. it is per-connection shaping, not an aggregate cap. The same shape as Zenodo. (d) No documented upload-bytes/day cap, no retention/expiry on repos, no pull-count limit observed.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: git
- tooling: Three real clients, all first-party: (1) git + git-lfs against https://opencsg.com/models/<ns>/<repo>.git; (2) csghub-sdk / csghub-cli (pip install csghub-sdk), with `csghub-cli upload-large-folder` purpose-built for multi-GB model trees; (3) a documented REST API at hub.opencsg.com/api/v1 (models, tree, branches, last_commit all return JSON). The whole platform is open source: github.com/OpenCSGs/csghub (4,071 stars) and csghub-server (1,039 stars), so the server-side quota logic is auditable. No rclone backend.
- composes with: Repositories are free and unlimited per account, allowing capacity across multiple repositories without a global account cap. CSGHub includes an XNet storage backend with chunk-level deduplication and instant upload for existing blocks, reducing storage overhead for forks and versions.
- reliability: Reads depend on Alibaba OSS presigned URLs, so a URL cached for more than 72 h silently dies (301/0-byte). Resolve-then-fan-out within the window. No observed rate limit on the anonymous LFS batch endpoint. Data does not expire; repos have branches and commit history, so it is mutable rather than an archive.
- notes: the same as the free tier
- evidence note: The object cap and the repository total were recomputed from the live tree API. Was reported; now documented.
- evidence:
  - [2] 2026-10-21: probe: GET -> 200, 176 files, summed size 688.6 GB, 163 shards >1 GB (largest 5.2 GB)
  - [3] 2026-10-21: probe: POST with {operation:download} -> 200, JSON containing actions.download.href to opencsg-gitea-lfs-new.oss-cn-beijing.aliyuncs.com with X-Amz-Expires=259200 — anonymous, no token required
  - [4] 2026-10-21: probe: GET -> HTTP 200 but Content-Length 135, body is a git-lfs pointer ('version https://git-lfs.github.com/spec/v1 / oid sha256:...'). The 200 is not a file transfer.
  - withheld 2026-10-21: probe: 1 ranged GET 16 MiB -> 206, 2,701,748 B/s. 8 parallel 8 MiB ranged GETs -> 14.49 MB/s aggregate; repeat on the 5.2 GB DeepSeek-V3 shard -> 15.50 MB/s aggregate
  - [1] 2026-10-21: read live: '上传大小和超时限制由站点、代理和存储配置决定 ... 不要把站点限制理解为 Git LFS 协议的统一上限' (no published quota; limits are site-config)
  - [5] 2026-10-21: read live: 'XNet 智能块加速引擎支持切块去重、秒级增量更新与并行下载 ... 整合 Git Server、Git LFS 与对象存储 OSS'
  - [6] 2026-10-21: 4,071 stars, self-hostable CSGHub CE (so the same stack can be run on your own box)
  - probe:https://hub.opencsg.com/api/v1/models/deepseek-ai/DeepSeek-V3/tree 2026-10-22: GET 2026-10-22: 200, 150,045 B; 176 files, 688,603,604,082 B total, 163 shards over 1 GB, largest 6,584,784,447 B
- sources:
  - [1] https://www.opencsg.com/docs/model/upload_models
  - [2] https://hub.opencsg.com/api/v1/models/deepseek-ai/DeepSeek-V3/tree
  - [3] https://hub.opencsg.com/models/Qwen/Qwen3-8B.git/info/lfs/objects/batch
  - [4] https://hub.opencsg.com/models/Qwen/Qwen3-8B/resolve/main/model-00001-of-00005.safetensors
  - [5] https://www.opencsg.com/docs/csghub/101/introduction
  - [6] https://github.com/OpenCSGs/csghub
