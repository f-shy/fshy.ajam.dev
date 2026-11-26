# Codefresh CI

> codefresh.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codefresh/ | JSON https://fshy.ajam.dev/api/v1/entity/codefresh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codefresh CI (Octopus Deploy)

- `ci-cd-runners/codefresh-ci` | paid-only | evidence documented | binding write-gated | category CI runner
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:00:39.389Z (live) | stale on 2026-12-05
- url https://codefresh.io/docs/docs/pipelines/run-pipeline/
- free tier: no free hosted runner: a free account runs pipelines only on a Hybrid Runner in a Kubernetes cluster the user provides; Cloud Builds (the SaaS runtime) are disabled for all accounts by default and enabled on an admin request answered within 24 hours; codefresh.io/pricing/ now serves Octopus Deploy pricing, which lists no Codefresh plan | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the pricing page as archived on 2024-01-04 offered a free Community plan: up to 5 developers, 1000 cloud credits a month, unlimited hybrid builds and 1 week of data retention; at 5 credits a minute on the S machine that is 1000 / 5 = 200 minutes
- per-object cap: unverified: no build duration limit for the SaaS runtime was found in the pages read | source: [1]
- retention: build and log data are kept for six months, for SaaS and on-premises installations | source: [1]
- egress: unverified: no egress terms for the SaaS runtime were found in the pages read | metered: no | source: [1]
- identity: any-phone | detail: sign-up through GitHub, Bitbucket, GitLab, Azure, Google or LDAP, then a phone number with a country code verified by a sent code, then organization details and use cases
- interface: git, cli
- limits:
  - write-gated (binding): Cloud Builds are disabled for all accounts by default; an account admin requests them and the answer takes up to 24 hours [1]
  - retention-clamped: build and log data are kept six months [1]
- limits note: SaaS memory limits are Small 1 GB, Medium 4 GB and Large 8 GB; pipeline concurrency is a per-pipeline setting from 0 to 14 or unlimited, and no plan concurrency limit was found; by default a build step that prints nothing to the log for 45 minutes is terminated; no build duration limit and no monthly cloud credit allowance for a Cloud Builds grant were found in the pages read
- binding note: no hosted build runs until Codefresh grants Cloud Builds to the account; without the grant the only runtime is a Hybrid Runner on infrastructure the user supplies
- interface detail: a Codefresh pipeline triggered from a Git provider integration; the codefresh CLI
- tooling: SaaS machine sizes from S (1 CPU, 1 GB) to XXL (16 CPU, 32 GB), billed in cloud credits, once Cloud Builds are granted. The free path is the Hybrid Runner, which the user installs and runs in a Kubernetes cluster on rented or free machines; it comes after any hosted runtime
- composes with: no hosted capacity without a Cloud Builds grant; the hosted control plane can drive a Hybrid Runner placed on a free compute offer
- reliability: Octopus Deploy acquired Codefresh in February 2024; Codefresh CI remains available for customers, and the Codefresh pricing URL redirects to Octopus Deploy pricing
- notes: No free hosted runner today: a new free account gets the hosted control plane and must bring a Kubernetes cluster for the Hybrid Runner, while Cloud Builds are granted on request with no published allowance or price. The 1000-credit Community plan of January 2024 is gone from the live pricing URL.
- evidence note: the Codefresh documentation, the Octopus Deploy Codefresh pages and the live and archived pricing pages were read and quoted on 2026-10-30; the sign-up app is a login wall and was not passed, so the outcome of a Cloud Builds request is unverified.
- evidence:
  - [1] 2026-10-30: no account has the SaaS runtime by default | capture: sha256:1ae42d2fc427ec95515ac445ea56168a7d134235872692f28d84fcfd250bc69a | quote: Cloud Builds for Codefresh pipelines are disabled for all accounts by default.
  - [1] 2026-10-30: a free account runs pipelines only on a Hybrid Runner | capture: sha256:1ae42d2fc427ec95515ac445ea56168a7d134235872692f28d84fcfd250bc69a | quote: If you create a free account, to run pipelines, you need to configure Build Runtime settings with a Hybrid Runner runtime environment.
  - [1] 2026-10-30: build and log data are kept six months | capture: sha256:1ae42d2fc427ec95515ac445ea56168a7d134235872692f28d84fcfd250bc69a | quote: Codefresh retains build and log data for pipelines for a period of six months, for both on-premises and SaaS installation configurations.
  - [2] 2026-10-30: since February 2023 accounts no longer get a SaaS runtime by default | capture: sha256:bf046fc2e96e31a5a88c667bfd1bac0caf0fe65335e9c0140ccd8558df9ad233 | quote: Previously, all Codefresh accounts had access to a SaaS runtime environment to run pipelines. However, this is no longer the case.
  - [3] 2026-10-30: pipelines need the Hybrid Runner | capture: sha256:3a429e85314defdc3177be4318d4b831bf2bd1e307d900e07cebe0325f84696d | quote: the Hybrid Runner is required to run Codefresh pipelines.
  - [4] 2026-10-30: with the Hybrid Runner, builds run on the user's Kubernetes cluster | capture: sha256:53093598ce4ff684711aa5f8b294f0395ef8387315bdb092f5115c7c8eadd2d8 | quote: The UI runs on Codefresh infrastructure, while the builds happen on a Kubernetes cluster in the customer’s premises.
  - [5] 2026-10-30: the S machine is 1 CPU and 1 GB at 5 credits a minute | capture: sha256:822f3f4a6825ced2aaa501da9680447f7488c3b15a52b934b3d192a93292156e | quote: | S | 1 | 1 GB | 5 |
  - [5] 2026-10-30: the XXL machine is 16 CPU and 32 GB at 80 credits a minute | capture: sha256:822f3f4a6825ced2aaa501da9680447f7488c3b15a52b934b3d192a93292156e | quote: | XXL | 16 | 32 GB | 80 |
  - [6] 2026-10-30: sign-up verifies a phone number | capture: sha256:ce2042a0b8f3fd229aac7e98b6e2bde33c287562c60408396ea12335c56b256e | quote: Select the required country code, enter your phone number, and then click Send.
  - [6] 2026-10-30: sign-up goes through an identity provider | capture: sha256:ce2042a0b8f3fd229aac7e98b6e2bde33c287562c60408396ea12335c56b256e | quote: Codefresh currently supports the following IdPs:
  - [7] 2026-10-30: Octopus Deploy acquired Codefresh in February 2024 | capture: sha256:9b7ca092ea10bafee7e8c10edade99ef7c2f9c7ff3f57edc494b410cdd096bd1 | quote: In February 2024, Octopus acquired Codefresh.
  - [7] 2026-10-30: Codefresh CI is still offered to customers | capture: sha256:9b7ca092ea10bafee7e8c10edade99ef7c2f9c7ff3f57edc494b410cdd096bd1 | quote: Codefresh CI remains available for customers. It continues to be developed and supported within the Octopus Deploy portfolio.
  - [8] 2026-10-30: the Codefresh pricing URL now serves Octopus Deploy's plans | capture: sha256:be1be1511f6025ae1fbdd6d4ddcf3b5f86ad7b32ae3ec4e6e8b6fdd7f0232144 | quote: Free tier - No time limit, but includes usage limits: 10 projects, 10 tenants, 10 machines, and 10 users.
  - [9] 2026-10-30: the archived 2024-01-04 Community plan included 1000 cloud credits a month | capture: sha256:a186c6f42d47ca73671af450f8fde367e9acf320aa335eb9052abb6016208fe1 | quote: 1000 cloud credits per month
  - [9] 2026-10-30: the archived Community plan had unlimited hybrid builds | capture: sha256:a186c6f42d47ca73671af450f8fde367e9acf320aa335eb9052abb6016208fe1 | quote: Unlimited hybrid builds
  - [10] 2026-11-02: a build step with no log output for 45 minutes is terminated by default | capture: sha256:60b5df5841d8b5727bdb4a41b5568033ffe526b4985bcad4809d0a21e282bbd1 | quote: By default, the system terminates a build step that seems “inactive” after 45 minutes.
  - [1] 2026-11-02: Cloud Builds are enabled on an admin request, not by default | capture: sha256:1ae42d2fc427ec95515ac445ea56168a7d134235872692f28d84fcfd250bc69a | quote: Account admins can request Codefresh to enable Cloud Builds for an account.
  - [11] 2026-11-02: the SaaS memory limits (Small 1 GB, Medium 4 GB, Large 8 GB) are listed in the knowledge base | capture: sha256:60ae89911814e04ed831056c134c717fc2ac201577b984a8097a4a6de3660f33 | quote: On our SaaS offering, the standard limits are as follows:
  - [12] 2026-11-02: a Cloud Builds request is an automated email request answered within 24 hours, and an approval adds a SaaS runtime | capture: sha256:fbddd85f811723337dca98f0da8d23ee02d092b686b37fc860c0c7fe990f46d8 | quote: Clicking the Enable Cloud Builds button sends an automated email request, with a response time frame of 24 hours. If approved, you should see the SaaS runtime in the list of Runtime Environments.
  - [1] 2026-11-04: no hosted runner by default | capture: sha256:1ae42d2fc427ec95515ac445ea56168a7d134235872692f28d84fcfd250bc69a | quote: Cloud Builds for Codefresh pipelines are disabled for all accounts by default.
- sources:
  - [1] https://codefresh.io/docs/docs/pipelines/run-pipeline/
  - [2] https://codefresh.io/docs/docs/ARCHIVED/2023-02-15-february-changelog/
  - [3] https://codefresh.io/docs/docs/installation/runner/behind-the-firewall/
  - [4] https://codefresh.io/docs/docs/installation/runner/
  - [5] https://codefresh.io/docs/docs/terms-and-privacy-policy/cloud-credits/
  - [6] https://codefresh.io/docs/docs/ci-quick-start/ci-create-codefresh-account/
  - [7] https://octopus.com/codefresh
  - [8] https://codefresh.io/pricing/
  - [9] https://web.archive.org/web/20240104230433/https://codefresh.io/pricing/
  - [10] https://codefresh.io/docs/docs/kb/articles/workflow-terminated-by-system/
  - [11] https://codefresh.io/docs/docs/kb/articles/reached-your-memory-usage-limit/
  - [12] https://codefresh.io/docs/docs/pipelines/pipelines/
