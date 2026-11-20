# Anaconda.org

> anaconda.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anaconda/ | JSON https://fshy.ajam.dev/api/v1/entity/anaconda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anaconda.org (public conda channels)

- `storage/anaconda-org` | fails-quota | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:02.297Z (live) | stale on 2026-12-04
- url https://anaconda.org
- free tier: 3 GB per free personal account. Anaconda staff on the official forum: 'You'll hit a hard limit at 10 GB with the default storage settings. If you need a large amount of storage (>100GB), you'll need to contact sales.' Team plan is 50 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered for public packages. CDN-fronted (Cloudflare). conda-forge serves multi-GB packages anonymously with no auth. | metered: no
- identity: anonymous
- interface: rest
- limits note: 3 GB personal free / 10 GB default hard limit / 50 GB Team. Per-package size not separately capped. Free accounts are public-only. Package versions can be removed but not edited.
- interface detail: rest
- tooling: anaconda-client (`anaconda upload`, `anaconda copy`, `anaconda remove`); REST at api.anaconda.org; conda itself is the client for download. Public channel listing is anonymous JSON.
- composes with: Multiply by free orgs/accounts: 3 GB personal, 10 GB default cap, 50 GB Team. Even chained aggressively this is the smallest unit in the field. 10 TiB would need ~340 personal accounts at 3 GB. Not worth the operational cost against npm's 200 MB x unlimited.
- reliability: Hard-limit enforcement is a real upload block, not a warning, and Anaconda's own forum answer routes anyone above 10 GB to sales. Storage ceiling is the smallest of the registries and there is no anonymous-way around it.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 3 GB per free personal account. Anaconda staff on the official forum: 'You'll hit a hard limit at 10 GB with the default storage settings. If you need a large amount of storage (>100GB), you'll need to contact sales.' Team plan is 50 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'the personal storage limit is only 3GB'; staff reply: 'You'll hit a hard limit at 10 GB with the default storage settings. If you need a large amount of storage (>100GB), you'll need to contact sales'
  - [2] 2026-10-21: 'The free plan allows you to search for, create and host public packages, and provides up to 3 GB storage space'
  - [3] 2026-10-21: probe: GET -> 200, 3,868 files, 25.6 GB total for one package name (shows the platform itself carries far more than the free-tier limit — the limit is per publisher account, not per package)
  - [1] 2026-11-19: the 10 GB default hard limit on anaconda.org storage is still stated by Anaconda staff | capture: sha256:b6b85bc36f2f752c225cd5b3142e02d0483c1ba2c28b776864ff7fe41d5a1be9 | quote: You'll hit a hard limit at 10 GB with the default storage settings.
  - [2] 2026-11-19: the free plan is public-only with a 3 GB allowance | capture: sha256:d569f7f99a5fe9bc7acf74feb1b1acbd7b31db15ad244a945b4b0b9e2d4556b3 | quote: The free plan allows you to search for, create and host public packages, and provides up to 3 GB storage space.
- sources:
  - [1] https://forum.anaconda.com/t/anaconda-packages-storage-size-limits/92903
  - [2] https://continuumio-docs.readthedocs-hosted.com/anacondaorg/faq/
  - [3] https://api.anaconda.org/package/conda-forge/numpy
