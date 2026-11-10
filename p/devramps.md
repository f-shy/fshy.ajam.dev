# Dev Ramps

> devramps.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/devramps/ | JSON https://fshy.ajam.dev/api/v1/entity/devramps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dev Ramps

- `ci-cd-runners/dev-ramps-free` | qualifies-with-caveat | evidence documented | binding request-rate | category CI runner | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-09T12:52:26.661Z (live) | stale on 2026-12-10
- url https://devramps.com/pricing
- free tier: Free: $0 / month with 500 build credits / month, 1 pipeline and 4 team members | unit: credits | metered on: wall-clock | read on: 2026-11-02 | source: [1] | note: the page counts build minutes while a pipeline is running and also lists the pool as build credits; it does not state how many credits one minute uses
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an email address and a GitHub repository: the pricing page states No credit card required and Get started with the free tier, and the platform requires GitHub for source control and an AWS account the user owns for the deploy target. No phone number is named
- interface: git, cli
- limits:
  - request-rate (binding): 500 build credits a month on Free; the page also says build minutes are counted while a pipeline is running [1]
  - write-gated: 1 pipeline and 4 team members on Free; Git provider limited to GitHub [1]
- binding note: the 500-credit monthly pool fails first; the schema has no term for a compute-time or credit pool, so request-rate is the nearest
- interface detail: a pipeline defined in a YAML file at .devramps/<pipeline>/pipeline.yaml that deploys to the user's own AWS accounts, driven by a git push; the Free plan lists GitHub as its only Git provider, and the @devramps/cli CLI handles login and AWS bootstrap
- tooling: an AWS-native CI/CD and deployment service; the build and deploy steps run against AWS accounts that the user owns and pays AWS for
- composes with: not stated
- reliability: no reliability event recorded
- notes: the Free pool is named build credits in the plan table and build minutes in the text; the conversion is not stated, so the number of minutes a month is unverified. The service deploys to AWS accounts that the user owns.
- evidence note: the pricing page was read on 2026-11-02; the credit-to-minute conversion and the Free plan's sign-up requirements are unverified
- evidence:
  - [1] 2026-11-02: the Free plan carries 500 build credits a month | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: | Build credits / month | 500 | 1,500 | 3,000 | Unlimited |
  - [1] 2026-11-02: the Free plan lists a 500 build-credit monthly pool | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: 500 build credits / month
  - [1] 2026-11-02: the pool is denominated in build minutes while a pipeline runs | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: Build minutes are counted while your pipeline is actively running
  - [1] 2026-11-02: the Free plan connects to GitHub only | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: | Git providers | GitHub | All | All | All + Custom |
  - [1] 2026-11-02: deploy targets are the user's own AWS accounts, billed by AWS | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: Your AWS infrastructure runs in your own accounts, billed directly by AWS.
  - [1] 2026-11-04: the Free plan lists 500 build credits a month | capture: sha256:1cce92d8372359e56524bec3be6c9dd2bcf679768660a3ebe57837ec83cff350 | quote: 500 build credits / month
  - probe:https://devramps.com/pricing 2026-11-04: the pricing page answered HTTP 200 on 2026-11-04 | capture: sha256:8230496a66da49db286f9cff71536d26b9342ad16615c1fd18931ff95b0094eb | quote: "status": 200
  - [1] 2026-11-09: the page states that starting on the free tier needs no credit card | capture: sha256:2d5dfe9fba1bdad29a5359c5808bfacc73bde1062143b966e2450d13a76b4c03 | quote: No credit card required. Get started with the free tier and upgrade when you're ready.
  - [2] 2026-11-09: a published CLI exists, so the interface is git plus a command-line client rather than git alone | capture: sha256:9611da7e0e26a28bb20026c4a4d627af9645a589618978c441c8af8e885f00e0 | quote: The DevRamps CLI (`@devramps/cli`) manages authentication, AI agent setup, and AWS infrastructure bootstrapping.
  - [2] 2026-11-09: the CLI runs through npx, so no installation is needed to reach it | capture: sha256:9611da7e0e26a28bb20026c4a4d627af9645a589618978c441c8af8e885f00e0 | quote: npx @devramps/cli <command>
  - [1] 2026-11-09: the Free plan is still 500 build credits a month with 1 pipeline and 4 team members | capture: sha256:2d5dfe9fba1bdad29a5359c5808bfacc73bde1062143b966e2450d13a76b4c03 | quote: 500 build credits / month
- sources:
  - [1] https://devramps.com/pricing
  - [2] https://devramps.com/docs/cli/overview
