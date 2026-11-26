# lfs.gg

> lfs.gg | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lfs/ | JSON https://fshy.ajam.dev/api/v1/entity/lfs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## lfs.gg

- `storage/lfs-gg` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:07.998Z (inherited) | stale on 2026-12-04
- url https://lfs.gg/
- free tier: none reachable: Markets 'Unlimited Git LFS bandwidth for GitHub, GitLab, and Bitbucket' but is paid per 100 GB/month with only the first 10 GB free, and is 'currently invite-only'. Not free storage at… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: Markets 'Unlimited Git LFS bandwidth for GitHub, GitLab, and Bitbucket' but is paid per 100 GB/month with only the first 10 GB free, and is 'currently invite-only'. Not free storage at…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Markets 'Unlimited Git LFS bandwidth for GitHub, GitLab, and Bitbucket' but is paid per 100 GB/month with only the first 10 GB free, and is 'currently invite-only'. Not free storage at…
  - probe:https://lfs.gg/ 2026-11-19: probe on 2026-11-19: lfs.gg name did not resolve (transport error, status null), no response body | capture: sha256:109cf86616d6df849a6a0bb5cb170c99503fe37e1b72d78a045f4d646a8b5f74 | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 502 the name did not resolve>"
  - probe:https://lfs.gg/ 2026-11-19: probe on 2026-11-19 confirms lfs.gg no longer resolves, so the host is unreachable | capture: sha256:109cf86616d6df849a6a0bb5cb170c99503fe37e1b72d78a045f4d646a8b5f74 | quote: "error_detail": "URLError: <urlopen error Tunnel connection failed: 502 the name did not resolve>"
- sources:
  - [1] https://lfs.gg/
