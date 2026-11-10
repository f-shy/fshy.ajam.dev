# openICPSR

> openicpsr.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openicpsr/ | JSON https://fshy.ajam.dev/api/v1/entity/openicpsr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## openICPSR (ICPSR, University of Michigan) — self-publishing repository

- `storage/openicpsr-self-publishing-repository` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.openicpsr.org
- free tier: 30 GB per file with a 30 GB total per deposit and 1,000 files/folders per deposit; explicitly 'no cost to you'. Because deposits are unlimited and instant, the effective ceiling is per-deposit, not per-person. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 30 GB per file | bytes: 30000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, 'no cost dissemination to other data users'. Downloads are immediate and public in the format submitted; no egress pricing exists in the product. Restricted-use options exist but are optional. | metered: no
- identity: anonymous
- interface: s3, rest, rclone
- limits:
  - per-object-cap (binding): 30 GB per file [1]
  - per-object-cap (binding): 30 GB/file [1]
- limits note: Per-object-cap 30 GB/file; per-deposit 30 GB and 1,000 files; ZIP extraction capped at 1,000 entries. Content is scope-gated to social/behavioural/health sciences and replication data, and every deposit gets a DOI, so deposits are citable publications rather than scratch storage.
- interface detail: rest
- tooling: Web upload plus 'Import From Zip' bulk extractor (1,000 files/folders per zip), versioning with a new DOI per version, and the underlying ICPSR deposit pipeline. No public rclone backend; automation is a scripted HTTP/form loop rather than a documented S3-style API. This is the weak point versus RepOD.
- composes with: Unlimited deposits x 30 GB each. 17 deposits = 510 GB; no account-level aggregate is published, and requests above 30 GB go to ICPSR Acquisitions for approval rather than being refused outright.
- reliability: Long-running (ICPSR since 1962) with DOI permanence and version history; the failure mode is editorial/scope rejection, not data loss or throttling.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'openICPSR depositors may share up to 30GB per file, with a total limit of 30GB and 1,000 files per deposit'
  - [2] 2026-10-21: 'Your deposit to openICPSR involves no cost to you'; 'up to 30GB in storage space, up to 1,000 files and folders per deposit'
  - [3] 2026-10-21: 'Anyone can self-deposit and publish uncurated data'
- sources:
  - [1] https://www.openicpsr.org/openicpsr/faqs
  - [2] https://www.openicpsr.org/openicpsr/about
  - [3] https://www.icpsr.umich.edu/sites/shared/posts/deposit-options
