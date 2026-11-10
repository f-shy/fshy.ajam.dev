# Windmill Cloud

> windmill.dev | Compute, Developer services; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/windmill/ | JSON https://fshy.ajam.dev/api/v1/entity/windmill.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Windmill Cloud (Compute)

- `compute/windmill-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:50:59.431Z (live) | stale on 2026-12-01
- url https://www.windmill.dev/docs/getting_started/how_to_use_windmill
- duplicate of `dev-services/windmill-cloud`
- free tier: Community plan on Windmill Cloud: 1,000 executions a month, no credit card; sign-up with GitHub, GitLab, Google or Microsoft SSO. Windmill Cloud is hosted in the US | unit: requests | metered on: request-count | read on: 2026-10-29 | source: [1]
- per-object cap: unverified: the getting-started page read on 2026-10-29 does not state a per-object cap
- retention: unverified: the getting-started page read on 2026-10-29 does not state a retention period
- egress: unverified: the getting-started page read on 2026-10-29 does not state egress terms | metered: no
- identity: email | detail: No credit card required; sign-up with GitHub, GitLab, Google or Microsoft SSO, and the login page also offers a login without a third party.
- interface: unknown
- limits:
  - request-rate (binding): 1,000 executions a month on the Community plan [1]
- interface detail: the workspace header has a CLI / MCP button to connect external tooling; the interfaces behind it were not read
- tooling: the Windmill web app, with a CLI / MCP connection named on the page
- composes with: not established: the page does not say how a run reaches outside services
- reliability: no reliability event recorded; Windmill Cloud is hosted in the US
- notes: Hosted: Windmill runs this plan. The self-hosted Community Edition, with unlimited executions, is compute/windmill and is the last resort.
- evidence:
  - [1] 2026-10-29: the hosted Community Plan starts with 1,000 monthly executions, needs no credit card, and signs up with GitHub, GitLab, Google or Microsoft SSO | capture: sha256:4559b764c15999ac14c5429be61bd83ac8d5877ed6f026ef4040f9186037fc75 | quote: Start with 1,000 monthly executions on our Community Plan
  - [2] 2026-10-31: the login page offers a login without a third-party identity provider | capture: sha256:998500289e5058006f4dbbc50c8472a00f6b1b7a6a4a1ee049145306bf93d6b3 | quote: Log in without third-party
  - [1] 2026-10-31: the hosted Community plan starts with 1,000 executions a month, needs no credit card and signs up with GitHub, GitLab, Google or Microsoft SSO | capture: sha256:4559b764c15999ac14c5429be61bd83ac8d5877ed6f026ef4040f9186037fc75 | quote: no credit card required. Sign up using GitHub, GitLab, Google, or Microsoft SSO. Start with 1,000 monthly executions on our Community Plan, and easily upgrade for more.
- sources:
  - [1] https://www.windmill.dev/docs/getting_started/how_to_use_windmill
  - [2] https://app.windmill.dev/user/login

## Windmill Cloud (Community)

- `dev-services/windmill-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted workflow engine and script runner | tier Community
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:43:09.670Z (live) | stale on 2026-12-01
- url https://www.windmill.dev/docs/getting_started/how_to_use_windmill
- free tier: Community plan on Windmill Cloud with no credit card: 1,000 free executions per user per month and 1,000 free executions per workspace per month; one execution is one job of up to 1 second on a worker with 2GB of memory, and each further second counts as another execution | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: An execution is also counted per second of job time, so the count is partly wall-clock. Job run details are kept 60 days. Windmill Cloud is hosted in the US.
- per-object cap: unverified: the plan and getting-started pages quoted name no limit on a job's payload or result size
- retention: job run details are retained for 60 days on the Community plan (cloud) | days: 60 | source: [2]
- egress: not stated: the plan pages name no charge or cap on traffic out of a job | metered: no | source: [3]
- identity: email | detail: No credit card required; sign-up with GitHub, GitLab, Google or Microsoft SSO, and the login page also offers a login without a third party.
- interface: rest, cli
- limits:
  - request-rate (binding): 1,000 free executions per user per month and 1,000 per workspace per month [4]
  - retention-clamped: job run details kept 60 days [2]
- binding note: A job longer than one second counts once per second, so 1,000 executions is at most 1,000 seconds, about 16 minutes, of job time a month.
- interface detail: Every request to the Windmill API carries a Bearer user token, which can be scoped; the wmill CLI syncs scripts and authenticates with a user token
- tooling: the Windmill web app, the REST API with user tokens and the wmill CLI
- composes with: A hosted scheduler and script runner on a 2GB worker: 1,000 one-second jobs a month cover an hourly check that calls free APIs and writes to a free database.
- reliability: no reliability event recorded; Windmill Cloud is hosted in the US
- notes: Hosted: Windmill runs this plan, and the same offer is also recorded as compute/windmill-cloud. The open-source edition, which the user installs and runs, is compute/windmill and is the last resort after this hosted plan.
- self hosted: no
- evidence:
  - [1] 2026-10-31: the hosted Community plan starts with 1,000 monthly executions, needs no credit card and signs up with GitHub, GitLab, Google or Microsoft SSO | capture: sha256:4559b764c15999ac14c5429be61bd83ac8d5877ed6f026ef4040f9186037fc75 | quote: no credit card required. Sign up using GitHub, GitLab, Google, or Microsoft SSO. Start with 1,000 monthly executions on our Community Plan, and easily upgrade for more.
  - [1] 2026-10-31: Windmill Cloud is hosted in the US | capture: sha256:4559b764c15999ac14c5429be61bd83ac8d5877ed6f026ef4040f9186037fc75 | quote: Windmill cloud is hosted in the US.
  - [4] 2026-10-31: the Free plan in the Windmill app source gives 1,000 executions per user and 1,000 per workspace each month | capture: sha256:1bdfebd1fd6573ea0caa3478bd9de08290a198bb29e2626fe0a4190cd74cb42c | quote: '<b>1 000</b> free global executions per-user per month', '<b>1 000</b> free executions per workspace per month'
  - [4] 2026-10-31: one execution is one job of up to 1 second on a 2GB worker, and each further second is another execution | capture: sha256:1bdfebd1fd6573ea0caa3478bd9de08290a198bb29e2626fe0a4190cd74cb42c | quote: One execution equals one job up to 1 second on a worker with 2GB of memory, with each additional second counting as an extra execution.
  - [4] 2026-10-31: a workspace not on a paid plan draws on its users' free-tier quotas | capture: sha256:1bdfebd1fd6573ea0caa3478bd9de08290a198bb29e2626fe0a4190cd74cb42c | quote: Users use their global free-tier quotas when doing executions in this workspace. Upgrade to a Team or Enterprise plan to unlock unlimited executions in this workspace.
  - [2] 2026-10-31: job run details are kept 60 days on the Community plan in the cloud | capture: sha256:a701501774c2c1cc283320e6e9746b8fdc5b3b9f98ef9295cdac724d124397a3 | quote: Community plan (cloud): Jobs runs details are retained for 60 days.
  - [3] 2026-10-31: the cloud plans are Community, Team and Enterprise, and share most Enterprise features | capture: sha256:5383c7002df33aaaea034c00edff4a23546a09889d47dac76c19fa310559ec68 | quote: All Windmill cloud plans (Community, Team, Enterprise) have most of the Enterprise features.
  - [5] 2026-10-31: the Windmill API authenticates every request with a Bearer user token | capture: sha256:5f3e508846cbe116b2cff8d0dfa8cc38fee8f3351b208e7f988928c69aa11ec5 | quote: User tokens are used to authenticate API requests to Windmill. Every interaction with the Windmill API requires a `Bearer` token.
  - [5] 2026-10-31: the wmill CLI authenticates with a user token | capture: sha256:5f3e508846cbe116b2cff8d0dfa8cc38fee8f3351b208e7f988928c69aa11ec5 | quote: The Windmill CLI (`wmill sync push`/`pull`) and the [GitHub Action git sync](https://www.windmill.dev/docs/advanced/git_sync) authenticate with a user token.
  - [6] 2026-10-31: the login page offers GitHub, GitLab, Google, or a login without a third party | capture: sha256:998500289e5058006f4dbbc50c8472a00f6b1b7a6a4a1ee049145306bf93d6b3 | quote: Continue with GitHub Continue with GitLab Continue with Google or Log in without third-party
- sources:
  - [1] https://www.windmill.dev/docs/getting_started/how_to_use_windmill
  - [2] https://www.windmill.dev/docs/core_concepts/jobs
  - [3] https://www.windmill.dev/docs/misc/plans_details
  - [4] https://github.com/windmill-labs/windmill/blob/main/frontend/src/lib/components/settings/PremiumInfo.svelte
  - [5] https://www.windmill.dev/docs/core_concepts/user_tokens
  - [6] https://app.windmill.dev/user/login

## Windmill

- `compute/windmill` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:26.168Z (live) | stale on 2026-12-05
- url https://www.windmill.dev/pricing
- free tier: Free and open source at USD 0 a month with unlimited executions when self-hosted; Enterprise Self-Host from USD 120 a month. The hosted Community plan is dev-services/windmill-cloud | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page and the CLI docs state no egress term; for the self-hosted software egress is set by the machine that runs it | metered: no | source: [1]
- identity: anonymous | detail: No account with Windmill is needed: the documented install downloads docker-compose.yml, Caddyfile and.env from raw.githubusercontent.com and runs docker compose up, and the first login is on the user's own instance.
- interface: cli, rest
- limits:
  - request-rate: 'Unlimited executions' on the self-hosted open-source tier; Enterprise Self-Host from $120/mo [1]
- limits note: The free self-hosted edition caps an instance at 3 workspaces, 50 users, 10 users with SSO, a 10 GiB workspace object storage quota, job run details kept up to 30 days and 100 trigger emails a day; executions are unlimited.
- binding note: Executions are unlimited when self-hosted, so no vendor cap binds a single user's jobs; the machine the user runs the instance on bounds throughput.
- interface detail: wmill CLI (list, get, new, sync); REST API described by an OpenAPI document linked from the pricing page; no SSH or SDK read
- tooling: the user installs and runs the Windmill server and worker containers and a Postgres database, with Docker Compose on one machine or the Helm chart on Kubernetes, on a rented or free machine
- composes with: not established
- reliability: no reliability event recorded
- notes: The hosted Community plan that Windmill runs is dev-services/windmill-cloud (also recorded as compute/windmill-cloud) and comes first. This record is no duplicate of it and stays: it is the open-source edition that the user installs and runs, with unlimited executions on the user's own instance, and it is the last resort.
- evidence note: the pricing page was read on 2026-10-22. 'Unlimited executions' is a claim about a missing limit, so it is recorded as the unit unlimited and not multiplied into a capacity figure
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free and Open-source · from$0/mo · Unlimited executions', quoted
  - [2] 2026-10-29: self-hosted Windmill is free and open source with unlimited executions; Enterprise Self-Host starts from a trial portal; the cloud plans are Community, Team and Enterprise | capture: sha256:f052fbcce4a7104913b2835723336a76f878d89b8c2e7cbf79b2b907d1ded8a9 | quote: Windmill is free and open source. If self-hosted, the number of executions will be unlimited.
  - [2] 2026-10-31: self-hosted Windmill is free and open source with unlimited executions | capture: sha256:c3a4dd5e49ac84d8e100da83ec762ceeccca4e669e7fa2b7911f5df7de1747e2 | quote: Windmill is free and open source. If self-hosted, the number of executions will be unlimited.
  - [3] 2026-10-31: the documented install downloads the compose file from a public URL with no sign-in step | capture: sha256:a6ad104d25553048396563623ef97ef9e44fe6ef41803884f6ce4a4b76bd0847 | quote: curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
  - [3] 2026-10-31: the first login after the install is on the user's own instance | capture: sha256:a6ad104d25553048396563623ef97ef9e44fe6ef41803884f6ce4a4b76bd0847 | quote: Go to [http://localhost](http://localhost/) et voilà. Then you can login for the first time.
  - [3] 2026-10-31: the self-hosted edition runs with Docker Compose on one instance or the Helm chart on Kubernetes | capture: sha256:a6ad104d25553048396563623ef97ef9e44fe6ef41803884f6ce4a4b76bd0847 | quote: For small setups, use Docker and Docker Compose on a single instance. For larger and production use-cases, use our Helm chart to deploy on Kubernetes.
  - [1] 2026-10-31: the free open-source tier has unlimited executions | capture: sha256:7eb2ec23a2f01097084bd80845847348ddab49259ac06dd0579b8b83ab2466c8 | quote: Unlimited executions.
  - [1] 2026-10-31: the free self-hosted tier caps email triggers at 100 emails a day, beside its other caps in the feature table | capture: sha256:7eb2ec23a2f01097084bd80845847348ddab49259ac06dd0579b8b83ab2466c8 | quote: Max 100 emails per day
  - [4] 2026-11-03: a CLI exists | capture: sha256:93f0691df249fe56ded7c6816254898958131393a8f7a384b6a3fb90f7d0767b | quote: The Windmill CLI, `wmill` allows you to interact with Windmill instances right from your terminal.
  - [1] 2026-11-03: the page links the OpenAPI document of the REST API | capture: sha256:128a2edd1c4f00dfc325723587306f41598bda532b667fc1507ec5aa0f3de2c9 | quote: [OpenAPI](https://app.windmill.dev/openapi.html#/)
- sources:
  - [1] https://www.windmill.dev/pricing
  - [2] https://www.windmill.dev/docs/misc/plans_details
  - [3] https://www.windmill.dev/docs/advanced/self_host
  - [4] https://www.windmill.dev/docs/advanced/cli
