# DVC remotes

> dvc.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dvc/ | JSON https://fshy.ajam.dev/api/v1/entity/dvc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DVC remotes (S3 / WebDAV / SSH / HTTP / Drive) pointed at free backends

- `storage/dvc-remotes-pointed-at-free-backends` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://doc.dvc.org/user-guide/data-management/remote-storage
- free tier: N/A. DVC ships no storage; the remote is whatever free store you configure. Free-tier bytes = the backing store's bytes. Supports Amazon S3 + S3-compatible (MinIO etc. via `endpointurl`), Azure Blob, GCS, Google Drive, Aliyun OSS, SSH/SFTP, HDFS/WebHDFS, HTTP, WebDAV. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Inherited. The HTTP remote is read-only and can sit behind any CDN, which is the only path where DVC itself doesn't add egress cost. | metered: no
- identity: email
- interface: s3, git, cli
- limits note: No per-file logic of its own; the backend's limits apply. WebDAV is the weakest link (DVC's WebDAV support is newer and less battle-tested than S3). HTTP remote is read-only, so it cannot be a primary. No built-in retry-sharding across remotes. You script it.
- interface detail: s3
- tooling: `dvc` CLI + dvcfilesystem (fsspec). `dvc remote add s3://bucket && dvc remote modify myremote endpointurl https://s3.hf.co/<ns>` works. Native read-only Git-LFS support means `dvc get`/`dvc import` can pull straight from a Hugging Face repo without installing git-lfs.
- composes with: One repo, many remotes (`dvc remote add` x N), plus `dvc push -r <remote>` to pick. Any S3-compatible free endpoint multiplies: HF buckets, IA's IAS3, MinIO on a free VM, an Oracle/Cloudflare-adjacent free tier. DVC's content-addressed cache means the same 20 TiB corpus can be pushed to N stores and only the missing blobs transfer.
- reliability: DVC is an ML-tooling project (treeverse); remote support quality varies by backend. S3-compatible endpoints need `endpointurl` + often `use_ssl`/path-style tweaks. Reliability is effectively the backend's.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: supported storage list and 'DVC does not provide or recommend a specific storage service'
  - [2] 2026-10-21: 'Set the endpointurl parameter with the URL to connect to the S3-compatible service (e.g. Nebius, MinIO, IBM COS)'
  - [3] 2026-10-21: native HF/Git-LFS import without git-lfs installed
- sources:
  - [1] https://doc.dvc.org/user-guide/data-management/remote-storage
  - [2] https://doc.dvc.org/user-guide/data-management/remote-storage/amazon-s3
  - [3] https://doc.dvc.org/user-guide/integrations/huggingface
