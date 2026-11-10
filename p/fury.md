# Gemfury

> fury.co | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fury/ | JSON https://fshy.ajam.dev/api/v1/entity/fury.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gemfury — Public (free) plan

- `storage/gemfury-public-plan` | qualifies-with-caveat | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fury.co
- free tier: Public plan is $0/mo with UNLIMITED public packages, unlimited versions and unlimited collaborators, and NO private packages. No storage figure appears anywhere on the pricing table. The plan matrix lists only collaborators / private packages / public packages. The only published numbers are per-file caps. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 300 MB per file | bytes: 300000000 | source: [1] | note: not stated
- retention: Small independent operator (fury.co, the same shop as the old gemfury.com); the 20 MB repository-endpoint cap silently breaks pushes that work through the API, and cancelled accounts have packages deleted after ~1 month. | days: 30 | source: [1] | note: not stated
- egress: No published bandwidth allowance or per-GB rate for the Public plan; public repos are served from the fury.io edge to anonymous clients (probe below). Nothing meters delivery in the documented plan matrix. | metered: yes
- identity: institution
- interface: rest, cli
- limits:
  - per-object-cap (binding): 300 MB per file [1]
  - per-object-cap (binding): 20 MB per file [1]
  - retention-clamped: deleted after ~1 month [1]
- limits note: HARD per-file ceiling: 300 MB per file via push.fury.io/Dashboard/git builds, and only 20 MB per file through a repository endpoint (gem.fury.io etc.). Git-backed packages: 500 MB per repo, 20 MB per file. Public/private is a per-package toggle; everything uploads private first and must be flipped public. No private packages at all on the free plan.
- interface detail: rest (push.fury.io upload API), per-ecosystem endpoints (gem/npm/pypi/nuget/apt/yum/maven/php/go), Gemfury CLI
- tooling: `fury push` CLI and `curl` upload; documented at gemfury.com/help/upload-packages; public repo is consumed by stock pip/gem/npm/apt/yum with the account URL.
- composes with: Unlimited packages × unlimited versions per account, and unlimited free accounts. Since there is no aggregate storage line item, the effective ceiling is (unlimited public packages) × (per-file cap). The 'per-record unlimited' pattern rather than a bucket cap.
- reliability: Small independent operator (fury.co, the same shop as the old gemfury.com); the 20 MB repository-endpoint cap silently breaks pushes that work through the API, and cancelled accounts have packages deleted after ~1 month.
- notes: the same as the free tier
- evidence:
  - [1] 2026-08-28: read live (also archived 2026-08-28): 'Public free $0/mo'; table row 'Free | ∞ collaborators | - private | ∞ public | $0/mo'; no storage or bandwidth line anywhere on the page
  - [2] 2026-10-21: read live: 'Package files have an absolute limit of 300MB per file uploaded ... packages uploaded to a repository endpoint (e.g. gem.fury.io) are limited to 20MB'; 'Git repositories have a 500MB size limit, with a 20MB limit for individual files'
  - [3] 2026-10-21: read live: 'Gemfury supports distribution of public packages without the need to distribute credentials ... Anyone can plug it into one of the supported package managers'
  - [4] 2026-10-21: probe: GET -> 200, returns a live 'Simple Index' listing pyarrow and nanoarrow anonymously; GET https://pypi.fury.io/arrow-nightlies/pyarrow/ -> 200. GET https://gem.fury.io/arrow-nightlies/ -> 404 and https://gem.fury.io/solmaz/ -> 401 (private endpoints gated, public index open)
- sources:
  - [1] https://fury.co/pricing/
  - [2] https://gemfury.com/help/limits/
  - [3] https://gemfury.com/help/public-packages/
  - [4] https://pypi.fury.io/arrow-nightlies/
