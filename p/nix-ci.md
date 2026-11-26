# NixCI

> nix-ci.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nix-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/nix-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NixCI

- `ci-cd-runners/nixci` | trial-only | evidence documented | binding volume-quota | category CI runner | tier FOSS
- needs card unknown, phone no, ID no, institution no | verified 2026-11-09T12:54:40.941Z (live) | stale on 2026-12-10
- url https://nix-ci.com/pricing
- free tier: no free hosted compute beyond a trial: the FOSS plan is free with your own workers, hosted workers are billed at USD 0.33 an hour even on it, and new users get a 14-day trial on the demo system, after which builds stop. The demo needs no signup and builds the newest 3 commits of a repository | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the hosted plan is USD 37 a month per developer plus USD 0.33 per worker-hour; a developer is a person who pushes at least 3 commits to private repositories in a month
- per-object cap: unverified: the hosted worker and pricing pages state no per-job time limit | source: [2]
- retention: build logs are kept 60 days; build metadata 90 days; cached artefacts 90 days | days: 60 | source: [3]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: sign-in is through a GitHub, GitLab or Codeberg account, held by installing the NixCI GitHub App on the repositories or by the equivalent GitLab or Codeberg webhook; the demo states that no signup or payment details are required. Beyond the trial the account takes a Subscribe step, which is behind a login wall, so unverified: behind a sign-up whether that step asks for a card. No phone number appears anywhere in the sign-up path
- interface: git
- limits:
  - volume-quota (binding): 14-day trial on the demo system; builds stop after it ends unless the account is upgraded [1]
  - volume-quota (binding): hosted workers billed at USD 0.3342 an hour per second of job execution, on every plan [2]
  - retention-clamped: build logs 60 days; build metadata and cached artefacts 90 days [3]
- limits note: the demo runs only the newest 3 commits of a repository
- binding note: hosted compute is paid by the second on every plan and the only free hosted use is the 14-day trial, so no free hosted allowance remains after it
- interface detail: a GitHub App, a GitLab or a Codeberg webhook runs CI for every repository that has a flake.nix, with no in-repo configuration required; results come back as commit statuses
- tooling: a flake.nix in the repository; the NixCI GitHub App, or a GitLab or Codeberg integration; hosted workers are 16 vCPU, 64 GiB RAM, 1 TB disk, x86_64-linux machines at Hetzner
- composes with: the hosted workers run x86_64-linux Nix builds, tests and deployments from a flake; a GitHub Actions job on a public repository comes first, and the user's own workers come last
- reliability: unverified: the vendor publishes no uptime figure or status page that was read
- notes: A hosted Nix CI exists with no free hosted allowance: the FOSS plan is free only when the user supplies the workers, and hosted worker time is paid by the second, so the offer is trial-only. Hosted runners of this topic come first. Last resort: the user's own workers, which NixCI offers to any subscriber on request. Sign-up is a GitHub, GitLab or Codeberg account through the forge App, and beyond the trial a Subscribe step follows; unverified: behind a sign-up whether that step asks for a card, so the card flag is left unknown rather than set to no.
- evidence note: every value is quoted from the vendor's pricing, workers, demo, getting-started and privacy pages; no sign-up was made, so the terms of the FOSS plan, the card requirement and any per-job time cap are unverified
- self hosted: no
- evidence:
  - [1] 2026-11-02: the FOSS plan is free with the user's own workers; hosted workers are billed at USD 0.33 an hour | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: Bring your own workers or use hosted workers at 0.27 CHF/hr $0.33/hr €0.30/hr
  - [1] 2026-11-02: the FOSS plan's free part is bring-your-own workers | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: Free with your own workers
  - [1] 2026-11-02: the only free hosted use is a 14-day trial on the demo system | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: Yes! New users get a 14-day trial on the demo system to test NixCI on their repositories.
  - [1] 2026-11-02: builds stop when the trial ends | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: After the trial period ends, your builds will stop running.
  - [1] 2026-11-02: the Hosted plan counts developers by pushes to private repositories | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: A developer is one person who pushes at least 3 commits to private repositories in any given month.
  - [1] 2026-11-02: hosted worker time is billed per second | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: Worker time is billed per second of actual job execution.
  - [4] 2026-11-02: the demo needs no signup and no payment details | capture: sha256:b675eeadb719c254f9f5b89f1c462ac5c9cb7693b5188360f115156c1032d948 | quote: No signup or payment details required.
  - [4] 2026-11-02: the demo builds the newest 3 commits | capture: sha256:b675eeadb719c254f9f5b89f1c462ac5c9cb7693b5188360f115156c1032d948 | quote: NixCI will run on the newest 3 commits of your repository.
  - [2] 2026-11-02: the hosted worker rate is USD 0.3342 an hour | capture: sha256:203480b22d4fa466848143bbe9b50a24f0ea857ed985cc456bff1da85b8a8e68 | quote: | Rate | 0.2739 CHF/hr $0.3342/hr €0.2980/hr 2.4x cheaper
  - [2] 2026-11-02: a hosted worker has 16 vCPUs | capture: sha256:203480b22d4fa466848143bbe9b50a24f0ea857ed985cc456bff1da85b8a8e68 | quote: | vCPUs | 16 |
  - [2] 2026-11-02: hosted workers run on Hetzner hardware | capture: sha256:203480b22d4fa466848143bbe9b50a24f0ea857ed985cc456bff1da85b8a8e68 | quote: NixCI hosted workers run your builds on dedicated hardware provided by Hetzner.
  - [3] 2026-11-02: build logs are kept 60 days and metadata 90 days | capture: sha256:4f906c1b573b4e47de8387bb50e61f38c13cf57ccb47f750b592a52b5fe55d20 | quote: Build logs are kept for 60 days and then automatically deleted. Build metadata (status, commit info, configuration) is kept for 90 days and then automatically deleted.
  - [3] 2026-11-02: sign-in is through a GitHub, GitLab or Codeberg account and stores the account's email address | capture: sha256:4f906c1b573b4e47de8387bb50e61f38c13cf57ccb47f750b592a52b5fe55d20 | quote: When you sign in via GitHub, GitLab, or Codeberg, we store your platform user ID, username, and email address from those platforms.
  - [3] 2026-11-02: paid plans are billed through Stripe | capture: sha256:4f906c1b573b4e47de8387bb50e61f38c13cf57ccb47f750b592a52b5fe55d20 | quote: Payment processing is handled by Stripe
  - [5] 2026-11-02: builds need a trial or a subscription | capture: sha256:ea100489db842474b934e150ce899de56d739249d92add2d3a1cbd06c68c2560 | quote: If you don't have a free trial active, subscribe to activate your builds and start building.
  - [6] 2026-11-02: the service runs CI for a repository that has a flake.nix | capture: sha256:89183ced93af18696e7f291af777282e44254ce78ecaefedcf5dbbc1b20899ea | quote: If you have a `flake.nix` , we have your CI ready for you!
  - [7] 2026-11-02: the self-hosting packages are closed and given on request | capture: sha256:8103ba58cf6ad4c00cd6e45f25f8e2ad6f1d7c5a06610db92aff4277d2506020 | quote: NixCI is not open-source, so you will need to contact us to get access to the self-hosting packages.
  - [5] 2026-11-09: the sign-up path starts with installing the GitHub App on the repositories, before any Subscribe step | capture: sha256:ea100489db842474b934e150ce899de56d739249d92add2d3a1cbd06c68c2560 | quote: ## Step 1: Install the GitHub App
  - [4] 2026-11-09: the demo states that no signup or payment details are required to run a build | capture: sha256:b675eeadb719c254f9f5b89f1c462ac5c9cb7693b5188360f115156c1032d948 | quote: No signup or payment details required.
  - [5] 2026-11-09: after the App install there is a Subscribe step for builds beyond the trial, and the page does not say what the step asks for | capture: sha256:ea100489db842474b934e150ce899de56d739249d92add2d3a1cbd06c68c2560 | quote: If you don't have a free trial active, subscribe to activate your builds and start building.
  - [1] 2026-11-09: the pricing page states the 14-day trial on the demo system, that builds stop after it, and that the FOSS plan is free with the user's own workers | capture: sha256:228e35b8ad0113ba565cfa4455c22b86efb8443faa11d7a7979006651f83f7c9 | quote: Yes! New users get a 14-day trial on the demo system to test NixCI on their repositories.
  - [5] 2026-11-09: the Subscribe step exists after the App install and the page does not say what it asks for, so the card requirement is unverified behind a sign-up | capture: sha256:ea100489db842474b934e150ce899de56d739249d92add2d3a1cbd06c68c2560 | quote: If you don't have a free trial active, subscribe to activate your builds and start building.
- sources:
  - [1] https://nix-ci.com/pricing
  - [2] https://nix-ci.com/workers
  - [3] https://nix-ci.com/privacy-policy
  - [4] https://nix-ci.com/demo
  - [5] https://nix-ci.com/documentation/getting-started/github
  - [6] https://nix-ci.com/
  - [7] https://nix-ci.com/documentation/self-hosting
