# nightly.link

> nightly.link | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nightly/ | JSON https://fshy.ajam.dev/api/v1/entity/nightly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nightly.link (GitHub Actions artifact -> anonymous URL wrapper)

- `storage/nightly-link` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nightly.link
- free tier: No quota of its own. It is a public-read proxy over GitHub Actions artifacts, which are themselves uncounted for public repos but capped at 90-day retention. Service is 'provided totally free of charge'. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: No quota of its own. It is a public-read proxy over GitHub Actions artifacts, which are themselves uncounted for public repos but capped at 90-day retention. | days: 90 | source: [1] | note: not stated
- egress: Free. Redirects to productionresultssa*.blob.core.windows.net (Azure Blob, GitHub's artifact store) with a signed URL, so downloads never touch GitHub's HTML front end. | metered: no
- identity: institution
- interface: rest
- limits note: Inherits GitHub artifact TTL (max 90 days for public repos) and the artifact size cap. Anonymous users share one global GitHub API rate limit. The site explicitly warns 'The throttling will likely become very bad over time' unless you install their GitHub App on your repo.
- interface detail: rest
- tooling: oprypin/nightly.link, 1011 stars, AGPL, self-hostable (Go). URL grammar is deterministic: https://nightly.link/<owner>/<repo>/workflows/<workflow>/<branch>/<artifact>.zip
- composes with: This is the multiplier that makes GitHub Actions artifacts usable at all: it converts 'artifact behind a login' into 'plain CDN URL'. Combined with unlimited public repos and the 90-day max retention it becomes a rolling 90-day hot tier of unlimited size, refreshed by scheduled workflows.
- reliability: Single-maintainer free service. A single point of failure if you depend on the hosted instance. Self-host it for production use. Rate limiting is the real bite, not storage.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Any public repository is accessible by default and visitors don't need to log in'; 'don't share the global API rate limit ... throttling will likely become very bad over time'
  - [2] 2026-10-21: probe: curl -L -> 200, 56909948 bytes downloaded anonymously, redirecting to productionresultssa1.blob.core.windows.net
  - [3] 2026-10-21: 1011 stars
- sources:
  - [1] https://nightly.link/
  - [2] https://nightly.link/crystal-lang/crystal/workflows/win/master/crystal.zip
  - [3] https://github.com/oprypin/nightly.link
