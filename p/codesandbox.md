# CodeSandbox

> codesandbox.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codesandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/codesandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CodeSandbox

- `compute/codesandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:01:15.545Z (live) | stale on 2026-12-05
- url https://codesandbox.io/docs/learn/plans/subscriptions
- free tier: CodeSandbox Free: "Every Free workspace gets 400 free monthly credits ... it's enough to develop a small React web app for 40 hours per month on a Nano VM", quoted, with "access to 20 Sandboxes for the entire workspace" | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the pricing page and the subscriptions page state no egress allowance and no overage price; limits are on credits, VMs and SDK requests | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): the 400 monthly credits run out before anything else, and every VM and repository in the workspace then enters a frozen state until the next billing cycle. [1]
- limits note: the 400 monthly credits run out before anything else, and every VM and repository in the workspace then enters a frozen state until the next billing cycle.
- binding note: the same as limits note
- interface detail: CLI, per the CodeSandbox SDK CLI page: "The CodeSandbox SDK provides a command-line interface (CLI) called `csb` for managing sandboxes, templates, and configurations."
- tooling: the csb command-line interface of the CodeSandbox SDK, per the CLI page: "The CodeSandbox SDK provides a command-line interface (CLI) called `csb`"
- composes with: 40 Nano-VM hours a month is a free headless Linux box with a filesystem and a port, which is what a build, a scrape or a test run needs; it is the cheapest server-shaped free tier among evaluated providers per credit, and it composes with any static host for the output.
- reliability: no reliability event recorded
- notes: The credits are worth USD 6 a month at the vendor's own rate, which is small in dollars and large in hours because a Nano VM is one vCPU. The pricing page and the docs disagree: the 40-hour bullet was removed from the pricing page in September 2026 while the docs still state 400 credits, so the allowance may be mid-change. compute/codesandbox-sdk already records the SDK from Together AI's docs, not this free tier; merge into one CodeSandbox record. Browser Sandboxes do not consume credits, so the 20-Sandbox allowance is a separate and unmetered free lane.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: recurring-allowance
  - facets.shape.vcpu: 1
- evidence:
  - [1] 2026-10-22: "Every Free workspace gets 400 free monthly credits ... it's enough to develop a small React web app for 40 hours per month on a Nano VM" and "the Free tier also provides access to 20 Sandboxes", quoted
  - [2] 2026-10-22: "A workspace on the free plan gets 400 credits per month" and unused credits do not roll over, quoted
  - [3] 2026-10-22: "VM credits ... are priced at $0.015 each", quoted, so 400 free credits is USD 6 of VM runtime at list price
  - [4] 2026-10-22: rate limits on the Free (Build) plan were doubled from 5 to 10 concurrent VMs, quoted; the same post records the Together AI acquisition
  - [5] 2026-10-22: a third party recorded that between 2026-09-07 and 2026-09-14 the Build plan lost the bullet '40 hours of monthly VM credits', reported
  - [3] 2026-11-03: the plan table limits requests, VMs and credits; no egress allowance or overage price appears | capture: sha256:38fc849ba53460d963550008dcffbde8a75bdfcbc412c1546b40959c8ac08548 | quote: The hourly rate limit for requests to CodeSandbox SDK.
  - [6] 2026-11-03: a CLI exists | capture: sha256:f7e36cb6d8ebc249368cc5ef44f854911453c640a719127338898bc30f73b2f0 | quote: The CodeSandbox SDK provides a command-line interface (CLI) called `csb` for managing sandboxes, templates, and configurations.
  - [7] 2026-11-03: an SDK exists | capture: sha256:c2abb03644a6e3238372b3292b5a3e353e727b762d9523dcfde7b69d43ba7e39 | quote: The CodeSandbox SDK has been designed to let you to rapidly create and run secure code environments at scale.
  - [6] 2026-11-04: the page names the csb CLI | capture: sha256:f7e36cb6d8ebc249368cc5ef44f854911453c640a719127338898bc30f73b2f0 | quote: The CodeSandbox SDK provides a command-line interface (CLI) called `csb` for managing sandboxes, templates, and configurations.
- sources:
  - [1] https://codesandbox.io/docs/learn/plans/subscriptions
  - [2] https://codesandbox.io/docs/learn/credit-usage/credits
  - [3] https://codesandbox.io/pricing
  - [4] https://codesandbox.io/blog/codesandbox-sdk
  - [5] https://pricingsaas.com/companies/codesandbox/diffs/2026W38
  - [6] https://codesandbox.io/docs/sdk/cli
  - [7] https://codesandbox.io/docs/sdk
