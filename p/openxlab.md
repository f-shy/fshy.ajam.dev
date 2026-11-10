# OpenXLab 浦源

> openxlab.org.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openxlab/ | JSON https://fshy.ajam.dev/api/v1/entity/openxlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenXLab 浦源 (Shanghai AI Lab) — model + dataset centers

- `storage/openxlab-model-dataset-centers` | qualifies-with-caveat | evidence inferred | binding none | category model-hub
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://openxlab.org.cn
- free tier: Not published. The platform introduction describes the model center as building an object-storage layer for large files. Verbatim: '基于平台内的命令行工具，便于 AI 开发者上传和发布模型文件，搭建对象存储体系，提供大文件存储能力，快速上传下载功能，便于 AI 开发者进行模型存储' (object storage system providing large-file storage capability). The dataset center supports private datasets and public datasets. No numeric byte quota is published. Documentation pages returned HTTP 504 and upload pages contain no quota statement. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter found; public models and datasets are anonymously downloadable. Reads are CDN-served. Unverified at the header level because model-detail pages timed out from this network. | metered: no
- identity: email | detail: Email, plus likely +86 phone. Chinese platform, and prior rounds recorded the pans in this family demanding real-name verification.
- interface: rest, git, cli
- limits note: Unverified. Uploads use a chunked SDK rather than a web form. Dataset upload supports files, directories, and archives with server-side auto-extraction (a 50 GB zip file extracts into a directory tree where extracted size may exceed the archive). No published per-file cap, retention period, or rate limit found.
- interface detail: rest
- tooling: Pip install openxlab, then first-party subcommands: `openxlab dataset upload-file`, `openxlab dataset upload-folder`, `openxlab model upload ..` with --dataset-repo/--source-path/--target-path. Python SDK mirrors the CLI (upload_file / upload_folder). Also git+LFS. Real, named, documented client. This passes the tooling filter cleanly.
- composes with: Repos are per-user and per-org and free to create, so capacity is N repos. OpenXLab is the Shanghai AI Lab's public front door (InternLM, OpenDataLab datasets), so its per-repo sizes are already in the tens-of-GB range. Multiplying across accounts is easy but the per-account ceiling is unknown.
- reliability: Documentation endpoints returned multiple HTTP 504 responses and 25-second timeouts on opendatalab.com and openxlab.org.cn API paths on 2026-10-21. Model detail pages return HTTP 302 redirecting to login.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: model center provides '对象存储体系，提供大文件存储能力' and the dataset center supports '私有数据集的上传、管理和发布'
  - [2] 2026-10-21: read live: three upload modes (file / folder / archive with auto-extract), plus CLI and Python SDK (`pip install openxlab`, `openxlab dataset upload-folder`)
  - withheld 2026-10-21: openxlab.org.cn docs paths 504'd repeatedly and opendatalab.com API paths timed out at 25-30 s
- sources:
  - [1] https://openxlab.org.cn/docs/intro.html
  - [2] https://opendatalab.com/docs/datasets/上传数据集.html
