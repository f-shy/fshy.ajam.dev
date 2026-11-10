# Packagecloud.io

> packagecloud.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/packagecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/packagecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Packagecloud.io — Free plan

- `storage/packagecloud-io-free-plan` | fails-quota | evidence reported | binding per-ip-shaping | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://packagecloud.io/pricing/
- free tier: 2 GB storage + 10 GB bandwidth per month, unlimited repositories and unlimited CI/CD minutes. Private repositories are no longer usable on the free plan (restricted since 7 Sep 2023), so the free tier is effectively public-repo only. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 10 GB/month of download bandwidth; overage is $1.50/GB on paid plans and the account is disabled at the 'maximum overage amount' setting. So on Free it is a hard wall. | metered: yes | free allowance: 10 GB per month
- identity: email
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): bandwidth per month, unlimited repositories and unlimited CI/CD minutes [1]
- limits note: 2 GB storage (high-water mark, so delete-then-reupload does not refund within a period); 10 GB/month bandwidth; private repos gated; packages over 2.6 GB are a paid-plan feature; bandwidth metered from request logs, HEAD/conditional GETs excluded.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest (packagecloud API), native apt/yum/ruby/pypi/npm clients via packagecloud.io/install/repositories/...
- tooling: packagecloud CLI (`packagecloud push`), `curl -X POST` to the API, setup scripts for apt/yum; public repos pull anonymously.
- composes with: Unlimited repositories per account, but storage and bandwidth are account-level watermarks ('high watermark for any given billing period'), so N repos do not multiply the 2 GB. Only N accounts would.
- reliability: Stable hosted service; the 2023 change that cut private repos off the free plan shows the free tier is a moving target.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 2 GB storage + 10 GB bandwidth per month, unlimited repositories and unlimited CI/CD minutes. Private repositories are no longer usable on the free plan (restricted since 7 Sep 2023), so the free tier is effectively public-repo only.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live (firecrawl render): 'Free ... 10 GB bandwidth ... 2 GB storage ... Unlimited CI/CD Minutes'; comparison table shows 'Unlimited repositories', 'Public repositories' ticked, 'Private repositories' and 'Package sizes > 2.6 GB' as paid
  - [2] 2026-10-21: read live: 'if you upload 100GB of packages, and delete 90GB of them, you'll still have used 100GB for that billing period' (high-water mark)
  - [3] 2026-10-21: read live: free-plan private repos got 402s from 7 Sep 2023
  - [4] 2026-10-21: probe: GET -> 200 (anonymous public-repo read)
- sources:
  - [1] https://packagecloud.io/pricing/
  - [2] https://packagecloud.io/pricing/faq/
  - [3] https://blog.packagecloud.io/packagecloud-private-repositories-on-the-free-plan/
  - [4] https://packagecloud.io/install/repositories/github/git-lfs/config_file.list?os=ubuntu&dist=xenial
