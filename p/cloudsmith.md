# cloudsmith

> cloudsmith.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudsmith/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudsmith.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cloudsmith

- `storage/cloudsmith` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloudsmith.com/pricing
- disagrees on identity_kind: `storage/cloudsmith` says email, `storage/cloudsmith-open-source-repositories` says institution
- free tier: none reachable: Free Core plan provides 500 MB artifact storage and 1 GB package delivery per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Free Core plan is 500 MB artifact storage and 1 GB package delivery, and the pricing page 429'd on first fetch, requiring escalation.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free Core plan is 500 MB artifact storage and 1 GB package delivery, and the pricing page 429'd on first fetch, requiring escalation.
- sources:
  - [1] https://cloudsmith.com/pricing

## Cloudsmith — open-source (Broadcast: Open Source) repositories

- `storage/cloudsmith-open-source-repositories` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cloudsmith.com
- disagrees on identity_kind: `storage/cloudsmith` says email, `storage/cloudsmith-open-source-repositories` says institution
- free tier: At least 50 GB of artifact data + 200 GB of package delivery per month, free, pooled across ALL open-source repositories in one org. 'You get at least 50GB of artifact data + 200GB of package delivery for free, across all open-source repositories.' Available on the $0 Core plan, no special plan needed. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB maximum per file | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 200 GB/month of 'package delivery' included, then metered (Core has no overage path at all: 'Additional data: N/A'; the settings cap is '200% of plan'). Delivery counts only outgoing bytes, partial downloads prorated, requests not charged. | metered: yes | free allowance: 200 GB per month
- identity: institution
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5 GB maximum per file [1]
- limits note: 5 GB maximum per file ('the current maximum file size is 5GB'); 50 GB total artifact data and 200 GB/mo delivery per org; artifact data billed as a high-water mark within the billing period (upload-then-delete does not refund); 28+ formats plus arbitrary raw files; OSS repos must carry an SPDX licence, a project URL and a Cloudsmith attribution badge.
- interface detail: rest (Cloudsmith REST API + CLI), plus every native package client: apt/yum/npm/pypi/nuget/helm/docker/raw; public broadcast URLs on dl.cloudsmith.io
- tooling: cloudsmith-cli (`cloudsmith push raw OWNER/REPO FILE`), REST API v1, Terraform provider, officially documented; anonymous pulls need no token (probe below).
- composes with: Usage is pooled per org, not per repo. So the multiplier is orgs, not repos: unlimited free signups × 50 GB + 200 GB/mo. OSS status is granted automatically at repo creation ('We don't require advance permission to create open-source repositories'), with post-hoc checks; sponsorship raises the allowance for large projects.
- reliability: Real hosted CDN with a real CLI/API; the risk is administrative, not technical. OSS repos that fail the eligibility rules (minor fork) get suspended, and the free Core plan cannot pay overage so it hard-stops at the cap.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: At least 50 GB of artifact data + 200 GB of package delivery per month, free, pooled across ALL open-source repositories in one org — 'You get at least 50GB of artifact data + 200GB of package delivery for free, across all open-source repositories.' Available on the $0 Core plan, no special plan needed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'You get at least 50GB of artifact data + 200GB of package delivery for free, across all open-source repositories'; 'Usage for open-source repositories is tracked separately'; 'We don't require advance permission to create open-source repositories'
  - [2] 2026-10-21: read live: Core $0 = 'Artifact data 500 MB / Package delivery 1 GB / Additional data N/A'; Pro $149 = 5 GB / 25 GB / $1.50 per GB; 'Number of packages / repositories: Unlimited' on every tier
  - [3] 2026-10-21: read live FAQ: 'the current maximum file size is 5GB'
  - [4] 2026-10-21: probe: GET -> 200 (anonymous download, no token); GET https://api.cloudsmith.io/v1/packages/cloudsmith/cli/?page=1&page_size=1 -> 200 with full package JSON (anonymous read API)
- sources:
  - [1] https://docs.cloudsmith.com/open-source-hosting-policy
  - [2] https://cloudsmith.com/pricing
  - [3] https://docs.cloudsmith.com/artifact-management/package-upload
  - [4] https://dl.cloudsmith.io/public/caddy/stable/gpg.key
