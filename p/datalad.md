# DataLad + git-annex workflow

> datalad.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datalad/ | JSON https://fshy.ajam.dev/api/v1/entity/datalad.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataLad + git-annex workflow (orchestration layer)

- `storage/datalad-git-annex-workflow` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:17.593Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://handbook.datalad.org/en/latest/basics/101-139-s3.html
- free tier: N/A. DataLad is a wrapper over git-annex; quota is the special remote's. Its value here is that it makes 'dataset + N special remotes + reproducible publish' a supported, documented workflow instead of hand-written annex commands. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Inherited; DataLad's S3 walkthrough specifically configures `publicurl` so consumers clone the git metadata from GitHub and stream file content from the bucket with no credentials. | metered: no
- identity: anonymous | detail: no account for the software: the user installs and runs DataLad and git-annex 10.20230802 or later from PyPI. The walk-through's worked target is an S3 bucket on an AWS account, and the page states that AWS signup wants an email address, a physical address and a credit card before verification, plus a GitHub account for the metadata sibling. DataLad itself asks for no card and no phone number; the card belongs to the S3 account the walk-through demonstrates.
- interface: s3, git, cli
- limits note: Same as annex: no delete on LFS-backed remotes, per-store object caps. DataLad adds Python overhead and its own version-compat matrix (annex version pinned per feature).
- interface detail: s3
- tooling: `datalad` CLI (Python), `datalad create-sibling-s3`, `datalad push --to <sibling>`, `datalad get`. Requires git-annex >= 10.20230802 for S3 publicurl on post-April-2023 buckets.
- composes with: DataLad dataset hierarchy of superdatasets and subdatasets partitions large archives across independently-served subdatasets with individual remotes. Command datalad siblings distributes logical datasets across multiple S3 accounts while preserving git history.
- reliability: Used in production by academic consortia (OpenNeuro etc.) precisely for multi-TB datasets on donated storage. The most battle-tested 'big dataset on free/cheap stores' pattern that exists.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'This walk-through requires git-annex >= 10.20230802 ... Prior versions do not support public access via the publicurl parameter with S3 buckets created after April 2023'
  - [2] 2026-10-21: DataLad's Git LFS special-remote walkthrough on GitHub (linked as next chapter)
  - [1] 2026-11-01: the accounts the walk-through needs are the target's, not the software's: a GitHub account for the metadata sibling and an AWS account for the bucket | capture: sha256:f5274fa9af9ba13cb49447c64e48e9c0470c7bdc6a4e6cbe221fcee6558e1864 | quote: Signup for a [GitHub account](https://github.com/join)
  - [1] 2026-11-01: the worked target's AWS signup takes an email address, a physical address and a credit card, and the software itself needs no account | capture: sha256:f5274fa9af9ba13cb49447c64e48e9c0470c7bdc6a4e6cbe221fcee6558e1864 | quote: The [AWS signup](https://aws.amazon.com) procedure requires you to provide your e-mail address, physical address, and credit card details before verification is possible.
  - [1] 2026-11-01: the accounts the walk-through's worked example needs are a GitHub account and an AWS account, both stated on the page, so the identity kind is read rather than defaulted | capture: sha256:f5274fa9af9ba13cb49447c64e48e9c0470c7bdc6a4e6cbe221fcee6558e1864 | quote: Signup for a [GitHub account](https://github.com/join)
  - [1] 2026-11-01: the tooling requirement the record carries is unchanged on the page | capture: sha256:f5274fa9af9ba13cb49447c64e48e9c0470c7bdc6a4e6cbe221fcee6558e1864 | quote: This walk-through requires git-annex >= 10.20230802
- sources:
  - [1] https://handbook.datalad.org/en/latest/basics/101-139-s3.html
  - [2] https://handbook.datalad.org/en/latest/basics/101-139-gitlfs.html
