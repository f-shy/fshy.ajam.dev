# OpenDataLab

> opendatalab.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opendatalab/ | JSON https://fshy.ajam.dev/api/v1/entity/opendatalab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenDataLab (opendatalab.com / opendatalab.org.cn)

- `storage/opendatalab` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category dataset-hosting
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://opendatalab.com
- free tier: Not published. What is documented is capability rather than quota: the dataset center accepts file, folder, or archive uploads and auto-extracts archives server-side; public datasets require a license field before they can be published (so publishing is a two-step publish flow, not a raw PUT). OpenDataLab is the org behind the WanJuan corpus and mirrors COCO and similar multi-hundred-GB sets, so its scale class is genuinely multi-TB on the read side. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap, retention, or rate limit published | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free for public datasets; anonymous downloads. No egress line found. Served from Chinese CDN endpoints. | metered: no
- identity: email | detail: email + likely +86 phone (Chinese platform).
- interface: s3-compatible, rest, cli
- limits:
  - per-object-cap (binding): No per-file cap, retention, or rate limit published [1]
- limits note: Unverified quota. Known: public publication requires a license to be set (a metadata gate, not a storage gate); archives are auto-extracted, so extracted size counts. No per-file cap, retention, or rate limit published.
- interface detail: rest
- tooling: Same openxlab toolchain (OpenDataLab runs on the OpenXLab 浦源 docs stack): `pip install openxlab`, `openxlab dataset upload-file/-folder`. Also opendatalab/opendatalab-python-sdk (60 stars) and an OpenDataLab CLI documented at opendatalab.com/docs/developers/数据集/数据集CLI. There is no S3 API.
- composes with: Per-dataset repos, unlimited count, free account. 50 GB-class datasets are the platform's normal unit, so N datasets x 50-200 GB.
- reliability: API endpoints on opendatalab.com timed out from this network (25 s, then 30 s) while HTML pages served fine. Treat the programmatic surface as CN-network-dependent.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: read live: upload types 文件/文件夹/压缩包, '如果您选择压缩包，系统将会在上传后自动解压您的文件', CLI and SDK examples
  - [2] 2026-10-21: read live: publishing requires setting visibility to public and '公开数据集需具备license信息'
  - [3] 2026-10-21: probe: GET -> 404 (18 bytes); /api/v2/... -> connection timeout at 25 s
- sources:
  - [1] https://opendatalab.com/docs/datasets/上传数据集.html
  - [2] https://opendatalab.com/docs/datasets/数据集创建流程.html
  - [3] https://opendatalab.com/api/v1/datasets?per=3
