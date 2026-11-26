# Bitrise

> bitrise.io | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitrise/ | JSON https://fshy.ajam.dev/api/v1/entity/bitrise.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bitrise (mobile CI)

- `compute/bitrise` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T11:38:10.231Z (live) | stale on 2026-12-25
- url https://bitrise.io/pricing
- free tier: The Hobby plan is free, with 500 build minutes a month on Linux or macOS, 1 private app and unlimited public apps; it needs a credit-card verification but incurs no charge unless Pay-As-You-Go is enabled | unit: minutes | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: the Build Cache add-on states '$0 egress fee for Bitrise CI' and '- Non-Bitrise CI egress fee: $0.12/GB' | metered: no | price per TB: cache only: USD 0.12 per GB non-Bitrise-CI egress | source: [1]
- identity: card | detail: The free Hobby plan needs a credit-card verification and no charge is made unless Pay-As-You-Go is turned on; signup offers GitHub, Bitbucket, GitLab, Email, SSO and Google routes
- interface: browser, rest, cli
- limits:
  - request-rate (binding): Hobby allows 500 build minutes a month on Linux or macOS; a build times out at 90 minutes [1]
  - write-gated: the 30-day trial is separate from the Free plan, which does not expire [1]
- interface detail: Builds are configured in the browser, through the Bitrise CLI and through a token-authenticated REST API at api.bitrise.io
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and describes the Free plan in words rather than a number: 'enough build credits ... a few times per month'. That is a discretionary allowance and the record says so instead of putting a figure on it
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states no build wall-clock cap; the credit total is what runs out
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free' plan described as 'Enough build credits for you to build your small project a few times per month' and 'Recommended up to 100 builds/month', with a 30-day trial and paid tiers at $99 and $218 a month, quoted
  - [1] 2026-11-18: not stated | capture: sha256:3f1d18ce1709ce470980438a3b6c01fd90934d0f1d7f2f83275a373dea331c3c | quote: # Plans for mobile engineering teams of every size
  - [1] 2026-11-24: the free Hobby plan grants 500 build minutes a month with one private app | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: The Hobby plan is free, with 500 build minutes a month on Linux or macOS, 1 private app, and unlimited public apps.
  - [1] 2026-11-24: the Build Cache add-on bills non-Bitrise CI egress at USD 0.12 a GB | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: - Non-Bitrise CI egress fee: $0.12/GB
  - [1] 2026-11-24: a Hobby build is capped at 90 minutes | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: On our Hobby plan, your build times out at 90 minutes, while on Starter and Pro, it can run up to 210 minutes.
  - [1] 2026-11-24: the free Hobby plan requires a credit-card verification but no charge unless PAYG is enabled | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: To keep usage fair for everyone, you’ll need to verify a credit card. You won’t be charged unless you turn on Pay-As-You-Go.
  - [2] 2026-11-24: signup offers GitHub, Bitbucket and GitLab as registration routes | capture: sha256:4fff49ac93baf7a958b5072d3875fe26da3e82ba27ae25ca56bebdc8a7d2eca2 | quote: Sign up with GitHubSign up with BitbucketSign up with GitLab
- sources:
  - [1] https://bitrise.io/pricing
  - [2] https://app.bitrise.io/users/sign_up

## Bitrise Remote Dev Environments

- `compute/bitrise-remote-dev-environments` | trial-only | evidence documented | binding write-gated | category sandbox (hosted macOS and Linux development VM) | tier Basic Tier 1, 14-day trial then USD 20 per month
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.793Z (live) | stale on 2026-12-26
- url https://bitrise.io/pricing#remote-dev-environments
- free tier: a 14-day trial gives the Tier 1 allocation of 8 hours per OS with 1 concurrent VM; a credit card is required at signup for verification only and is not charged, and the trial does not auto-convert to a paid plan | unit: hours | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: 8 hours per OS is 480 minutes; each OS has its own pool. After the trial, Basic starts at USD 20 per month billed monthly (USD 18 per month billed annually) with up to 480 included minutes per OS; RDE is billed separately from Bitrise CI build credits
- per-object cap: not applicable: the unit is a development VM, not a stored object
- retention: a terminated session's persistent disk is kept indefinitely as long as the user does not delete it and the stack it was created from remains available; session disks are not backed up and are erased if the stack is removed | source: [2]
- egress: no separate session-storage or egress price is published on the page read; session storage is not billed separately today, and enterprise agreements define a storage allowance | metered: no | source: [2]
- identity: card | detail: the 14-day trial requires a credit card at signup for verification only, with no charge and no subscription; a workspace owner or manager must enable RDE and grant the RDE User role, and the CLI sign-in opens a browser to authenticate a Bitrise account
- interface: ssh, rest, cli
- limits:
  - volume-quota: 480 included minutes per OS per month at Basic Tier 1, then macOS USD 0.0288/min and Linux USD 0.0044/min up to a monthly cap of USD 99 macOS and USD 39 Linux [1]
  - write-gated (binding): a workspace owner or manager must enable RDE and grant the RDE User role before a member can start a session [2]
- binding note: access is granted per workspace: membership alone is not enough, so a new user is stopped by the RDE User role before the 8-hour trial cap or the per-minute overage comes into play
- interface detail: a session is created from the terminal, IDE, browser UI or an AI coding agent; a REST API creates, reads, updates and deletes sessions, templates and saved inputs; a VNC desktop is exposed for macOS sessions
- tooling: the Bitrise CLI with bitrise-cli auth login and bitrise-cli rde, an RDE MCP server for AI agents, a VS Code plugin, a browser UI and a REST API
- composes with: an archive-and-restore development VM that keeps its disk between sessions, so a mobile project can be picked up later on the same stack; GitHub integration plants a short-lived token so git and the gh CLI authenticate as the user
- reliability: session disks are working storage with no backup and no service-level commitment; a session on a removed stack is unrecoverable, and long-running machines are drained for infrastructure maintenance even with the auto-terminate timer disabled
- notes: A hosted development VM rather than a code-execution sandbox: macOS M2 Pro Large or Linux up to 4 vCPU at Basic Tier 1. The free allowance is a 14-day, 8-hours-per-OS trial with a card held for verification only; after that Basic is USD 20 per month (USD 18 annual) with per-OS minute pools and metered overage capped per OS. Workspace-level RDE access must be granted by an owner or manager.
- evidence note: the trial, price, minute pools, overage rates, monthly caps and identity gate are quoted from first-party pricing, FAQ and quickstart pages read on 2026-11-25; no session was created
- extras:
  - shape.vcpu: 6
  - shape.ram_gib: 14
  - shape.note: Basic Tier 1 offers macOS M2 Pro Large at 6 vCPU and 14 GB RAM; Linux machines go up to 4 vCPU and 16 GB RAM
  - billing_model: 14-day trial then monthly plan with included minutes per OS and metered overage to a monthly cap
  - free_tier_kind: time-boxed trial
  - term: session auto-terminates after 5 days idle by default, up to 30 days or disabled on paid plans; trial sessions are capped at 8 hours
  - price_arithmetic: trial 480 minutes per OS over 14 days; Basic Tier 1 USD 20 per month; macOS overage USD 0.0288/min = USD 1.728/h; Linux overage USD 0.0044/min = USD 0.264/h
  - derived: USD 0.0288/min x 60 = USD 1.728/h macOS overage; USD 0.0044/min x 60 = USD 0.264/h Linux overage
  - network_out.allow_outbound: yes
  - session_cap.idle_reap_s: 432000
  - session_cap.restart_required: no
  - session_cap.note: trial sessions capped at 8 hours; paid sessions auto-terminate after 5 days idle by default
- evidence:
  - [1] 2026-11-25: the trial is two weeks at Tier 1 with 8 hours per OS, 1 concurrent VM and a card for verification only | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: Two weeks, Tier 1 allocation (8 hours per OS, 1 concurrent VM), credit card required at signup for verification only.
  - [1] 2026-11-25: the trial does not auto-bill into a paid plan | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: We will not charge your credit card or require you to purchase a subscription.
  - [1] 2026-11-25: the tier table gives Basic Tier 1 480 included minutes per OS per month, rising to 960 and 1,440 at the higher tiers | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: Up to 1,440 included minutes/month, per OS
  - [1] 2026-11-25: the Basic monthly price starts at USD 18 when billed annually | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: From $18
  - [1] 2026-11-25: the Basic column of the machine-rate table gives macOS overage USD 0.0288 per minute and Linux overage USD 0.0044 per minute | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: | macOS overage | $0.0288/min | $0.0576/min |
  - [2] 2026-11-25: the offer is an on-demand macOS or Linux cloud machine on Bitrise infrastructure | capture: sha256:c1ffb41ec94d5209233730906b2c0b22c38e574f2d7673ebc606760bdc9be134 | quote: An on-demand cloud machine - macOS or Linux - running on the same infrastructure
  - [2] 2026-11-25: access comes through self-serve signup or enterprise sales and then needs the RDE User role | capture: sha256:c1ffb41ec94d5209233730906b2c0b22c38e574f2d7673ebc606760bdc9be134 | quote: There are two ways to get RDE.
  - [2] 2026-11-25: trial sessions are capped at eight hours and cannot change the auto-terminate timer | capture: sha256:c1ffb41ec94d5209233730906b2c0b22c38e574f2d7673ebc606760bdc9be134 | quote: Sessions in free-trial workspaces are capped at eight hours and can
  - [2] 2026-11-25: session storage is not billed separately and RDE does not use CI build credits | capture: sha256:c1ffb41ec94d5209233730906b2c0b22c38e574f2d7673ebc606760bdc9be134 | quote: Session storage isn't billed separately today.
  - [2] 2026-11-25: a REST API can manage sessions and the GitHub integration plants a short-lived token | capture: sha256:c1ffb41ec94d5209233730906b2c0b22c38e574f2d7673ebc606760bdc9be134 | quote: Yes. You can create, read, update, and delete sessions, templates, and saved inputs through the API.
  - [3] 2026-11-25: the machines run in US and EU data centers with Apple silicon macOS and 2 to 48 vCPU Linux | capture: sha256:bc4d6845ee72141c3dd5be8c84212076e5da30cd05c6fe7e6ec0b6b16cf10308 | quote: RDE runs on production-grade Bitrise infrastructure in US and EU data centers:
  - [1] 2026-11-25: the tier table gives Basic Tier 1 480 included minutes per OS per month, rising to 1,440 at the highest tier | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: | Included minutes (per OS) | Up to 1,440 minutes (24 hrs) |
  - [1] 2026-11-25: the machine-rate table gives macOS overage of USD 0.0288 per minute on the Basic column | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: | macOS overage | $0.0288/min | $0.0576/min |
  - [1] 2026-11-25: the machine-rate table gives Linux overage of USD 0.0044 per minute on the Basic column | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: | Linux overage | $0.0044/min | $0.0088/min |
  - [1] 2026-11-25: the tier table lists 480, 960 and 1,440 included minutes per OS per month across the three Basic tiers | capture: sha256:226b873d453af4b37e89b2e2a61f99cc4a4b9d83c3ac132bef98aefc5b46f833 | quote: 480 minutes / month (8 hrs) | 960 minutes / month (16 hrs) | 1,440 minutes / month (24 hrs)
- sources:
  - [1] https://bitrise.io/pricing#remote-dev-environments
  - [2] https://docs.bitrise.io/en/bitrise-rde/getting-started/rde-faq
  - [3] https://docs.bitrise.io/en/bitrise-rde/getting-started/remote-dev-environments-overview

## bitrise artifacts

- `storage/bitrise-artifacts` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:57.621Z (live) | stale on 2026-12-04
- url https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
- free tier: none reachable: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the Bitrise artifact retention policy page | source: [1] | note: not stated on the Bitrise artifact retention policy page
- retention: Bitrise stores both build artifacts and build logs for a limited amount of time. The retention period varies by artifact type to balance storage costs with typical usage patterns. | source: [1] | note: per-type periods are listed in the retention table; removal is permanent with no recovery
- egress: not stated on the Bitrise artifact retention policy page | metered: no
- identity: email
- interface: rest
- interface detail: Bitrise API for listing and downloading build artifacts
- tooling: Bitrise API calls to list builds, list artifacts and fetch download URLs
- composes with: archive artifacts to the user's own storage via the API download URLs to outlive retention
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Time-boxed and aggressively shortened in 2026: non-installable artifacts 90 days, installables 150 days, HTML reports and pipeline intermediates 7 days. Removal is permanent with no…
  - [1] 2026-11-19: installable artifacts are retained for 150 days | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: | Installable artifacts (.ipa, .akp and .aab files) | 150 days | Available for Enterprise customers |
  - [1] 2026-11-19: artifact removal is permanent with no recovery | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: When artifacts are removed, they are permanently deleted with no way to recover them.
  - [1] 2026-11-19: the interface is the Bitrise HTTP API | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: You can download build artifacts via the Bitrise API in order to store them
  - [1] 2026-11-19: the documented tool is the Bitrise API | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: To keep artifacts beyond the retention period, archive them using the Bitrise API:
  - [1] 2026-11-19: no per-file cap appears in the retention policy | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: Bitrise stores both build artifacts and build logs for a limited amount of time.
  - [1] 2026-11-19: artifact retention is time-boxed and varies by artifact type | capture: sha256:91ae15e1e23812cf617b67f0334ad80447f5e35b1a49d8a857b3e9b4c9263910 | quote: Bitrise stores both build artifacts and build logs for a limited amount of time. The retention period varies by artifact type to balance storage costs with typical usage patterns.
- sources:
  - [1] https://docs.bitrise.io/en/bitrise-ci/run-and-analyze-builds/managing-build-files/artifact-retention-policy
