# Jira Cloud Free

> atlassian.com | Storage, Compute; 8 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/atlassian/ | JSON https://fshy.ajam.dev/api/v1/entity/atlassian.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Atlassian Confluence Cloud Free

- `storage/atlassian-confluence-cloud-free` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.atlassian.com/software/confluence
- free tier: 2 GB file storage on the Free plan (10 users, unlimited spaces and pages). Crucially: 'Free, Standard, and Premium plans entitle you to one app instance. You can have as many of these plans as you need. You'll subscribe to each one separately.' Each instance 'will have its own storage'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: attachment default 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter anywhere in Atlassian Cloud pricing. Attachments are served from the site domain, not a billed CDN bucket. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap: attachment default 100 MB [1]
- limits note: Per-object-cap: attachment default 100 MB, admin-configurable upward ('Enter your preferred maximum size (in bytes)'). Quota is per-site, not per-org. request-rate: Atlassian Cloud REST rate limits apply. Retention: Free sites are DEACTIVATED after a period of inactivity (logging in and viewing a page counts as activity). This is the real hazard, not eviction. Over-quota does not delete data, it restricts editing/creating.
- interface detail: rest
- tooling: Confluence Cloud REST API v2/v1 (`/wiki/rest/api/content/{id}/child/attachment`), Basic auth with email + API token, or OAuth 2.0. No rclone backend; the API is the client.
- composes with: 2 GB x N free Confluence sites, and N is self-service and explicitly unbounded ('as many of these plans as you need'). Ten free sites = 20 GB; a scripted site-creation loop is the multiplier. Community reports confirm multiple free sites per account are allowed and the one-instance limit is a paid-plan construct.
- reliability: Nothing is deleted at quota. Writes are blocked until you upgrade or free space. But a Free site that goes untouched is deactivated, so a storage-only site needs a periodic login to stay alive.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Confluence Free- 2 GB / Standard- 250 GB / Premium- Unlimited storage'
  - [1] 2026-10-21: 'You can have as many of these plans as you need'
  - [3] 2026-10-21: 'if you have two Confluence instances from two sites, each will have its own storage' + Free-plan inactivity deactivation
  - [4] 2026-10-21: 'The default is 100 megabytes, expressed as 104857600 bytes', admin-adjustable
- sources:
  - [1] https://support.atlassian.com/organization-administration/docs/how-many-instances-of-a-product-does-my-organization-need/
  - [2] https://support.atlassian.com/confluence-cloud/docs/manage-your-storage-usage/
  - [3] https://support.atlassian.com/organization-administration/docs/track-storage-and-move-data-across-products/
  - [4] https://support.atlassian.com/confluence-cloud/docs/configure-attachment-size/

## Atlassian Confluence Premium via Social Impact (nonprofit) License — unlimited file storage

- `storage/atlassian-confluence-premium-via-social-impact-license-u` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.atlassian.com/teams/nonprofits/discount-pricing
- free tier: Confluence Premium = 'Unlimited file storage'. Atlassian's Feb 2026 announcement grants eligible nonprofits and social enterprises 100% off Confluence 'Standard or Premium up to 25 users' under the Social Impact License. So a verified nonprofit gets a 25-seat Confluence Premium site with no storage cap, for free. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap is the binding constraint: 'The default size limit is 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter on Confluence attachment downloads. Attachments are served from api.media.atlassian.com / the site's CDN with no bandwidth line item in the plan comparison. | metered: no
- identity: card
- interface: rest, rclone, cli
- limits:
  - per-object-cap (binding): per-object-cap is the binding constraint: 'The default size limit is 100 MB [1]
- limits note: Per-object-cap is the binding constraint: 'The default size limit is 100 MB' per attachment, and Atlassian's own migration doc says the limit 'can be configured for Legacy editor pages, but not for the default editor' (feature request CONFCLOUD-72157 still open). So 20 TB = ~200,000 objects of <=100 MB. request-rate: Atlassian does not publish a Confluence Cloud REST request rate on these pages — unverified; the storage page itself is only refreshed 'every 4 hours'. retention: none published; archiving a page does NOT free storage because Atlassian 'stores all attachments for version history purposes'. Deletes are the only way to reclaim.
- interface detail: rest
- tooling: Confluence Cloud REST API v1/v2 (POST /wiki/rest/api/content/{id}/child/attachment, GET .../child/attachment, GET /wiki/rest/api/content/{id}/download/attachments/{filename}); community CLI wrappers exist (github.com/nlink-jp/confl-cli, github.com/eddieland/confluence-dl, github.com/justmiles/go-confluence). No rclone backend.
- composes with: 'Unlimited' is per Confluence site; each site is one org. Multiply by creating many spaces inside one site (unlimited spaces even on Free), and by the number of verified nonprofits. Premium edition also removes the 250 GB Standard ceiling for the same $0. The licence tier is the multiplier, not the seat count.
- reliability: Free Confluence sites can be deactivated for inactivity (login is the counter). Premium removes the storage cap but not the 100 MB object cap, and archived content is billed forever. Anonymous read of a public space works; anonymous write does not (probed: 200 read, 403 write).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Confluence Free- 2 GB / Confluence Standard- 250 GB / Confluence Premium- Unlimited storage'
  - [2] 2026-10-21: 'access 100% off: Teamwork Collection ... Confluence – for knowledge management Standard or Premium up to 25 users'
  - [3] 2026-10-21: 'The admin of your Atlassian license specifies the attachment size limit. The default size limit is 100 MB.'
  - [4] 2026-10-21: 'This limit can be configured for Legacy editor pages, but not for the default editor.'
  - withheld 2026-10-21: probe: GET meltedmensoftware.atlassian.net/wiki/rest/api/content/293437441/child/attachment -> 200 (anonymous, 225 bytes, empty results)
  - withheld 2026-10-21: probe: POST meltedmensoftware.atlassian.net/wiki/rest/api/content/293437441/child/attachment -> 403 (anonymous write rejected)
- sources:
  - [1] https://support.atlassian.com/confluence-cloud/docs/manage-your-storage-usage/
  - [2] https://www.atlassian.com/blog/confluence/new-nonprofit-discounts
  - [3] https://support.atlassian.com/confluence-cloud/docs/upload-a-file/
  - [4] https://support.atlassian.com/migration/docs/differences-administering-confluence-data-center-and-cloud/

## Bitbucket Pipelines

- `compute/bitbucket-pipelines` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- needs card unknown, phone no, ID no, institution no | verified 2026-11-04T02:24:29.905Z (live) | stale on 2026-12-05
- url https://www.atlassian.com/software/bitbucket/pricing
- free tier: 50 build minutes a month on the Free plan, at $0 for up to 5 users, with 1 GB of Git LFS storage in total, up to 100 steps per pipeline and up to 10 concurrent steps; no overage protection on Free | unit: minutes | metered on: wall-clock | read on: 2026-10-31 | source: [1]
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published: https://www.atlassian.com/software/bitbucket/pricing and https://support.atlassian.com/bitbucket-cloud/docs/limitations-of-bitbucket-pipelines/ state no data-transfer allowance or overage price | metered: no | source: [2]
- identity: email | detail: an Atlassian account; the Free plan covers up to 5 users, and the billing documentation charges a credit card on file only for monthly Standard or Premium plans after a 30-day evaluation; whether the Free sign-up form asks for a card is unverified: the form renders client-side
- interface: rest, git
- limits:
  - request-rate: 50 build minutes a month on Free, shared by all users of the workspace; a step on a 2x runner consumes minutes at twice the rate [2]
  - write-gated (binding): past 5 users the workspace must move to Standard at $3.65 a user a month [2]
- limits note: a step times out after 120 minutes by default, and max-time accepts 1 to 720 minutes; sizes 4x and up are limited to Standard and Premium
- interface detail: Bitbucket REST API (OpenAPI spec published) and Git
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: free plans cannot buy extra build minutes or LFS storage beyond the plan allowances; on paid plans extra minutes are $10 per 1,000
- evidence note: documented from the Pipelines limitations page, the pricing page and the step-options page; the 1x size table and the prose of the step-options page disagree on the CPU count (2 against 4)
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 2
  - shape.ram: 4
  - shape.disk: 64
  - shape.note: a default 1x step: 2 CPU, 4 GB memory and a 64 GB volume in the size table, while the prose of the same page says 4 CPUs that might be shared; 2x gives 4 CPU and 8 GB; 4x and larger sizes need a paid plan
  - session_cap.wall_clock_min: 720
  - session_cap.restart_required: no
  - session_cap.note: a step runs for at most 120 minutes by default and at most 720 minutes with max-time
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: 'Free forever for up to 5 users' at $0, with Standard $3.65 and Premium $8 per user a month, quoted; the page's build-minute definition is in a collapsed section it does not render
  - [1] 2026-10-30: the Free plan includes 50 build minutes a month for up to 5 users | capture: sha256:7b0fa43b7fa726b70e338f2a52ef0ad289fd0636081a10714267421fcd55b62a | quote: | Free | $0 for up to 5 users | Build minutes: 50 min/monthLarge file storage: 1 GB totalSteps per pipeline: up to 100 Concurrent steps*: up to 10 | Not included |
  - [1] 2026-10-30: the Free allowance is a number of build minutes | capture: sha256:7b0fa43b7fa726b70e338f2a52ef0ad289fd0636081a10714267421fcd55b62a | quote: | Free | $0 for up to 5 users | Build minutes: 50 min/monthLarge file storage: 1 GB totalSteps per pipeline: up to 100 Concurrent steps*: up to 10 | Not included |
  - [3] 2026-10-30: build minutes are pipeline execution time | capture: sha256:2b7ecd1d6836678157c1c8cbdeb87e272a227b10e3c9ab55534ef0ea9f529d6d | quote: Build minutes measure CI/CD pipeline execution time on Atlassian cloud runners.
  - [2] 2026-10-30: the Free plan includes 50 build minutes | capture: sha256:35d795508696cf0255b943d9650af4a252c3118008812985e57428d7257e82a7 | quote: You also get 1 GB file storage for LFS and 50 build minutes to get started with Pipelines.
  - [4] 2026-10-30: a 1x step has 2 CPU, 4 GB memory and a 64 GB volume | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: | 1x | 2 | 4 | 64GB |
  - [4] 2026-10-30: a step times out after 120 minutes unless max-time is set | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: The default maximum time for pipeline steps is 120 minutes.
  - [4] 2026-10-30: max-time can be raised to at most 720 minutes per step | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: Allowed values — A positive integer between 1 and 720
  - [4] 2026-10-30: the default step timeout is 120 minutes | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: The default maximum time for pipeline steps is 120 minutes.
  - [3] 2026-10-30: the Free plan allowance cannot be extended by purchase | capture: sha256:2b7ecd1d6836678157c1c8cbdeb87e272a227b10e3c9ab55534ef0ea9f529d6d | quote: On free plans, you cannot buy extra build minutes or LFS storage beyond your plan allowances.
  - [5] 2026-10-30: a card on file is tied to the paid Standard and Premium plans | capture: sha256:f835970f560cc250c2e04fd37d11f30668a92c24d3539a39d0e9474c8348820f | quote: If you have signed up for or upgraded to a monthly Standard or Premium plan, we will start to charge your credit card on file upon completion of the 30-day evaluation.
  - [4] 2026-10-30: the size table gives 2 CPU for 1x | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: | 1x | 2 | 4 | 64GB |
  - [6] 2026-10-30: the Pipelines feature page also states 50 minutes a month on Free | capture: sha256:5c220e1fea319a91a37ca196a435cadfc67b9c7a21c9a4efa646db2e87c7678e | quote: Free: 50 min / month included
  - [4] 2026-10-30: the prose gives a default step 4 GB memory, 4 shared CPUs and 64 GB of disk | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: By default, a step running on Bitbucket Cloud infrastructure or a Linux Docker self-hosted runner has access to 4GB of memory, 4 CPUs (which might be shared with other tasks), and 64 GB of disk space per step for mounting volumes.
  - [4] 2026-10-30: the Free plan is limited to 1x and 2x steps | capture: sha256:58439f373c5d529105bcfd711350b8f84585dea7d52937bb6bcc6de84604d2ea | quote: 4x, 8x, 16x, 24x, and 32x pipelines size options are only available for builds running on a paid Bitbucket Cloud plan (Standard or Premium).
  - [2] 2026-10-30: the Free plan is still offered for up to 5 users | capture: sha256:7eb2d0af32e7a650c5208526cc808202abc718e9a6d96ddc079028959fa4b779 | quote: Free forever for up to 5 users
  - [2] 2026-10-30: Standard is still $3.65 a user a month | capture: sha256:7eb2d0af32e7a650c5208526cc808202abc718e9a6d96ddc079028959fa4b779 | quote: $3.65
  - [1] 2026-10-31: the Free row gives $0 for up to 5 users, 50 build minutes a month, 1 GB LFS in total, up to 100 steps per pipeline, up to 10 concurrent steps, and overage protection not included | capture: sha256:7b0fa43b7fa726b70e338f2a52ef0ad289fd0636081a10714267421fcd55b62a | quote: | Free | $0 for up to 5 users | Build minutes: 50 min/monthLarge file storage: 1 GB totalSteps per pipeline: up to 100 Concurrent steps*: up to 10 | Not included |
  - [7] 2026-11-03: Bitbucket exposes a REST API and Git access | capture: sha256:976dd3549aa427bf5956dcd08f5abc8f464c65031ef6de0eb7c19e74b833d91d | quote: API Tokens are personal access tokens that users can create to authenticate with Bitbucket's REST APIs or interact with Git.
  - [2] 2026-11-03: the pricing page lists seats and prices and no data-transfer allowance or price | capture: sha256:7eb2d0af32e7a650c5208526cc808202abc718e9a6d96ddc079028959fa4b779 | quote: Free forever for up to 5 users
- sources:
  - [1] https://support.atlassian.com/bitbucket-cloud/docs/limitations-of-bitbucket-pipelines/
  - [2] https://www.atlassian.com/software/bitbucket/pricing
  - [3] https://www.atlassian.com/licensing/bitbucket
  - [4] https://support.atlassian.com/bitbucket-cloud/docs/step-options/
  - [5] https://support.atlassian.com/bitbucket-cloud/docs/manage-your-plan-and-billing/
  - [6] https://www.atlassian.com/software/bitbucket/features/pipelines
  - [7] https://developer.atlassian.com/cloud/bitbucket/rest/intro/

## bitbucket cloud free

- `storage/bitbucket-cloud-free` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.atlassian.com/blog/bitbucket/important-changes-coming-to-bitbucket-clouds-free-plan
- free tier: none reachable: Free workspaces were cut to 1 GB of total repository storage (all repos combined) effective 2025-04-28, delayed to 2025-05-29. Free plan also lost the Downloads feature entirely and lost… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free workspaces were cut to 1 GB of total repository storage (all repos combined) effective 2025-04-28, delayed to 2025-05-29. Free plan also lost the Downloads feature entirely and lost…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free workspaces were cut to 1 GB of total repository storage (all repos combined) effective 2025-04-28, delayed to 2025-05-29. Free plan also lost the Downloads feature entirely and lost…
  - [2] 2026-10-21: cited as the basis of the rejection: Free workspaces were cut to 1 GB of total repository storage (all repos combined) effective 2025-04-28, delayed to 2025-05-29. Free plan also lost the Downloads feature entirely and lost sni
- sources:
  - [1] https://www.atlassian.com/blog/bitbucket/important-changes-coming-to-bitbucket-clouds-free-plan
  - [2] https://confluence.atlassian.com/bbkb/what-are-the-repository-and-file-size-limits-1167700604.html

## Bitbucket Cloud Git LFS

- `storage/bitbucket-cloud-git-lfs` | fails-quota | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.atlassian.com/software/bitbucket/pricing
- free tier: Free (up to 5 users): 1 GB LFS storage. Academic 5 GB, Standard 5 GB, Premium 10 GB. Extra storage sold in 100 GB units at $10/month. Notable counter-property: no per-file cap at all. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: no per-file cap at all | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered. Atlassian publishes no LFS bandwidth quota, only storage in 100 GB units. This is the one LFS host where the storage number is small but the transfer side is genuinely unstated/unbilled. | metered: yes
- identity: card
- interface: ssh, git
- limits:
  - per-object-cap (binding): no per-file cap at all [1]
- limits note: 'there's no limit on the LFS file size you can push to Bitbucket Cloud'. Genuinely no per-file cap. Forks do not copy LFS objects (fork points at parent's store, and the fork lacks permission). So fork-based sharding fails. Repo archives do not include LFS files.
- interface detail: git
- tooling: Git-lfs. Note: SSH not usable for LFS repos? (not stated). The documented limitation is that repository transfer and forking both break LFS links; the alternative route is `git lfs fetch --all` + `git lfs push --all`.
- composes with: 1 GB per free workspace, unlimited free workspaces (each needs an email). 500 workspaces = 500 GB of very awkward storage. Weak: no route to manage many workspaces at once, and the workspace is tied to users.
- reliability: Fork/transfer/archive are all documented as broken for LFS repos, which makes recovery awkward. Storage overage is auto-billed in 100 GB increments rather than blocked.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free (up to 5 users): 1 GB LFS storage. Academic 5 GB, Standard 5 GB, Premium 10 GB. Extra storage sold in 100 GB units at $10/month. Notable counter-property: no per-file cap at all.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free (up to 5 users) | 1 GB'; '100 GB of file storage | Your monthly bill goes up $10'
  - [2] 2026-10-21: 'there's no limit on the LFS file size you can push'; 'the transfer of repositories with Git LFS files is disabled'
- sources:
  - [1] https://support.atlassian.com/bitbucket-cloud/docs/storage-policy-for-git-lfs-with-bitbucket/
  - [2] https://support.atlassian.com/bitbucket-cloud/docs/current-limitations-for-git-lfs-with-bitbucket/

## Confluence Cloud Free

- `storage/confluence-cloud-free` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://atlassian.com/software/confluence
- free tier: 2 GB per site on Free (250 GB Standard, unlimited Premium); 100 MB default per attachment, admin-configurable | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB/file | bytes: 100000000 | source: [1] | note: not stated
- retention: 2 GB per site on Free (250 GB Standard, unlimited Premium); 100 MB default per attachment, admin-configurable | 2 GB hard cap per site. Exceeding it freezes page/space creation until you delete content; archived pages still count ('Archiving content that contain attachments will not free up any storage'); 100 MB/file default. | source: [1] | note: not stated
- egress: free direct attachment download links, Atlassian media CDN, no egress billing | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB/file [1]
- limits note: 2 GB hard cap per site. Exceeding it freezes page/space creation until you delete content; archived pages still count ('Archiving content that contain attachments will not free up any storage'); 100 MB/file default.
- interface detail: rest
- tooling: Confluence Cloud REST v2 /wiki/api/v2/attachments (documented, OAuth or API token); atlassian-python-api wraps it
- composes with: 2 GB x unlimited free sites (10 users each, unlimited free orgs on the same email domain). 500 GB = 250 sites; 20 TiB = 10,000 sites. The site-creation step is the bottleneck, not the API.
- reliability: the cleanest API of the Atlassian trio and the highest per-file ceiling (100 MB configurable), but the 2 GB bucket is small; multi-site chaining is the only route to scale
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 GB per site on Free (250 GB Standard, unlimited Premium); 100 MB default per attachment, admin-configurable
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Confluence Free- 2 GB / Standard- 250 GB / Premium- Unlimited storage'
  - [2] 2026-10-21: 'The default is 100 megabytes'
  - [3] 2026-10-21: '2 GB of file storage' on Free, 10-user cap
- sources:
  - [1] https://support.atlassian.com/confluence-cloud/docs/manage-your-storage-usage/
  - [2] https://support.atlassian.com/confluence-cloud/docs/configure-attachment-size/
  - [3] https://support.atlassian.com/confluence-cloud/docs/learn-about-confluence-cloud-plans/

## confluence standard/premium as a free route

- `storage/confluence-standard-premium-as-a-free-route` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.atlassian.com/confluence-cloud/docs/manage-your-storage-usage/
- free tier: none reachable: 250 GB and unlimited are paid tiers; the free tier is hard-capped at 2 GB and archived content still counts | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 250 GB and unlimited are paid tiers; the free tier is hard-capped at 2 GB and archived content still counts
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 250 GB and unlimited are paid tiers; the free tier is hard-capped at 2 GB and archived content still counts
- sources:
  - [1] https://support.atlassian.com/confluence-cloud/docs/manage-your-storage-usage/

## Jira Cloud Free

- `storage/jira-cloud-free` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://atlassian.com/software/jira
- free tier: 2 GB storage on Free, 250 GB Standard, unlimited Premium | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free attachment links, Atlassian CDN | metered: no
- identity: email
- interface: rest
- limits note: 2 GB site cap; default attachment max 10 MB unless raised by an admin; every attachment needs an issue to hang off
- interface detail: rest
- tooling: Jira Cloud REST API v3 issue attachments (multipart POST /rest/api/3/issue/{key}/attachments); jira-python wraps it
- composes with: 2 GB x unlimited free sites; same math as Confluence but with the same 2 GB ceiling and a smaller default file cap
- reliability: Identical bucket economics to Confluence Free. Only worth it if you are already farming Atlassian sites; issue-per-attachment bookkeeping is worse than Confluence pages.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 2 GB storage on Free, 250 GB Standard, unlimited Premium
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '2 GB of storage' (Free), '250 GB of storage' (Standard), 'Unlimited storage' (Premium)
- sources:
  - [1] https://www.atlassian.com/software/jira/pricing
