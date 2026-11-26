# Superserve

> superserve.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/superserve/ | JSON https://fshy.ajam.dev/api/v1/entity/superserve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Superserve

- `compute/superserve` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T18:47:21.392Z (live) | stale on 2026-12-25
- url https://superserve.ai/pricing
- free tier: Start free, no card required, then pay for usage; the Developer plan is $20/month including $20 of usage with up to 100 concurrent sandboxes, 4 vCPU and 16 GiB per sandbox and unlimited runtime; the Pro plan is $250/month including $250 of usage with up to 2,000 concurrent sandboxes | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: estimates exclude network charges; the pricing page lists compute, memory and retained-storage rates only and states no transfer allowance and no per-GB price | metered: no | source: [1]
- identity: email | detail: The console signup page says "Create your Superserve account", offers "Continue with Google", and states the password rule "Use 8 or more characters with an uppercase letter, a lowercase letter, and a number." No card, phone or ID document is asked for on this page.
- interface: rest, cli
- limits:
  - request-rate (binding): up to 100 concurrent sandboxes on Developer, up to 2,000 on Pro, with unlimited runtime on both [1]
- interface detail: REST API, the `@superserve/cli` CLI and a TypeScript SDK; no SSH found in the docs read
- tooling: not stated
- composes with: not established
- reliability: sandboxes pause with changes saved and compute stops billing while paused; no idle reap or other reliability event stated
- evidence note: the pricing page was read on 2026-10-22. The page states 'No time limit on sandboxes', which is the wall-clock axis, and 20 concurrent sandboxes is the bound
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no runtime limit published; sandboxes pause with changes saved and no automatic idle kill is stated
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · Pay-as-you-go after credit · Up to 20 concurrent sandboxes · No time limit on sandboxes · Usage rates after credit', quoted
  - [1] 2026-11-03: network is charged outside the published rates and no price is stated | capture: sha256:efa4dda5c8cc1626e6bb870e9ef55e55115047e72d8fa63abaf6d334fa5d2b05 | quote: Estimates exclude taxes, network, and external model API charges.
  - [2] 2026-11-03: a CLI exists | capture: sha256:e6b411f14c086ffb7de76253222a35bf52084f9c3f228c31efb8ab3ebc928ca1 | quote: Create sandboxes, run commands, move files and publish ports from your terminal.
  - [2] 2026-11-03: a REST API reference exists | capture: sha256:e6b411f14c086ffb7de76253222a35bf52084f9c3f228c31efb8ab3ebc928ca1 | quote: Creates a sandbox from a template (defaults to `superserve/base` when `from_template` is omitted)
  - [1] 2026-11-18:  | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: ✓Unlimited runtime
  - [1] 2026-11-24: free signup with no card, usage paid after | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: Start free, no card required. Then pay for usage.
  - [1] 2026-11-24: the Developer concurrency limit is 100, not 20 | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: - ✓Up to 100 concurrent sandboxes
  - [3] 2026-11-24: free signup needs an account and yields an API key, with no card | capture: sha256:2b4d9a1a5ab0d27894d2f0c743efb41f42103f22edcd1d2d3829e9d9aadf7c70 | quote: Sign up for free in the [Superserve Console](https://console.superserve.ai?utm_source=docs\&utm_medium=link), no card required. Grab your API key and export it.
  - [1] 2026-11-24: network charges are outside the published rates | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: Estimates exclude taxes, network, and external model API charges.
  - [1] 2026-11-24: pause saves state and stops compute billing | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: Compute stops billing when paused; storage is billed for as long as you keep it.
  - [1] 2026-11-24: compute is billed per second at $0.0504 per vCPU-hour on every plan | capture: sha256:d87db3ebabdade069dc56ad2f68397e25c50a7243b7b03cc5de66d58bca13d5a | quote: Compute[vCPU] Per-second billing. Pay only while sandboxes are running. $0.0504/ hour
  - [3] 2026-11-24: an SDK is installed and driven with an API key | capture: sha256:2b4d9a1a5ab0d27894d2f0c743efb41f42103f22edcd1d2d3829e9d9aadf7c70 | quote: npm install @superserve/sdk
  - [2] 2026-11-24: a CLI is documented | capture: sha256:272f44b4ddeb2fcb8c7a1b61ca884d158ca19bf210432ce4f98ade5d70b3abac | quote: - [CLI](https://docs.superserve.ai/cli.md): Create sandboxes, run commands, move files and publish ports from your terminal.
  - [4] 2026-11-24: the provider's own signup page creates an account by email and password or Google, with no card, phone or ID field | capture: sha256:0eac8f11b9d788c05c2c0381d654ffcc4815f8a4a6bca2c0f3d8264622843102 | quote: Create your Superserve account
  - [4] 2026-11-24: the signup gate is an email address and a password with a stated strength rule, plus Google sign-in | capture: sha256:0eac8f11b9d788c05c2c0381d654ffcc4815f8a4a6bca2c0f3d8264622843102 | quote: Use 8 or more characters with an uppercase letter, a lowercase letter, and a number.
  - [4] 2026-11-24: the console signup page creates an account | capture: sha256:0eac8f11b9d788c05c2c0381d654ffcc4815f8a4a6bca2c0f3d8264622843102 | quote: Create your Superserve account
- sources:
  - [1] https://superserve.ai/pricing
  - [2] https://docs.superserve.ai/llms.txt
  - [3] https://docs.superserve.ai/quickstart.md
  - [4] https://console.superserve.ai/auth/signup
