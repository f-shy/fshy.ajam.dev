# Arga Labs

> argalabs.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/argalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/argalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arga Labs

- `compute/arga-labs` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card unknown, phone no, ID no, institution no | verified 2026-11-04T15:51:56.485Z (live) | stale on 2026-12-05
- url https://www.argalabs.com/
- free tier: service twins that are short-lived or permanent; a short-lived one expires automatically after 60 minutes | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page and the docs plans page list plan prices and run limits but state no egress allowance, price or overage | metered: no | source: [1]
- identity: email | detail: an email address, or a GitHub sign-in: 'Sign in with GitHub or create an account with email.' The CLI then stores a device credential, '`arga login` starts the device authorization flow and stores a device-scoped credential', and one email belongs to one account. Whether a payment method is asked for at sign-up is unverified: behind a sign-up; https://docs.argalabs.com/plans.md and https://www.argalabs.com/pricing publish none.
- interface: rest, cli
- limits:
  - retention-clamped (binding): a short-lived service twin expires automatically after 60 minutes; the page's own example counts down from 60 [1]
- interface detail: API, CLI and MCP; Python and TypeScript SDKs; a web app
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the 60-minute automatic expiry, which is the wall-clock axis. The page publishes no plan or price, so the free-tier claim cannot be settled from…
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: the 60-minute expiry is automatic and is stated in the product copy; a permanent twin is the alternative
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: yes
  - net.ports: full clones reachable by API, MCP and CLI
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Spin up short-lived or permanent service twins without deploying app code.' and 'Expires automatically after 60 minutes.' with a live example reading 'Support agent sandbox · 58 minutes remaining', quoted
  - [1] 2026-11-04: twins are reachable by API, MCP and CLI | capture: sha256:b21ce071558c6566f9e1f728ef6a7dfdab9e7945559e5a53ac350686feea9292 | quote: Full clones with API, MCP, and CLI support for third-party services your agents need to read from and write to.
  - [2] 2026-11-04: a CLI exists beside the web app | capture: sha256:f7f25eaea653074f557f3cf0a6d1a35bc3584cc44dfaf0b18182b7ce581aee61 | quote: The `arga` CLI authenticates your machine and gives scripts or coding agents access to the same core workflows as the web app.
  - [1] 2026-11-04: the page offers a demo and a sandbox start, with no plan or rate table | capture: sha256:b21ce071558c6566f9e1f728ef6a7dfdab9e7945559e5a53ac350686feea9292 | quote: Book a demoStart a sandbox
  - [3] 2026-11-04: the Team plan lists usage limits (runs, minutes, CI checks) and none of the plan listings names egress | capture: sha256:d820d79c139bbc6823a252073616615b0f36a4a3a2efb0df57fac33a8a512ee1 | quote: Unlimited CI checks
  - [4] 2026-11-04: an account is created with an email address, or with a GitHub sign-in | capture: sha256:66033a654af3c8c226a0c9f4a3ba2fbf6f49072294e4257c9c2ae9d4ad0b12c1 | quote: Sign in with GitHub or create an account with email.
  - [2] 2026-11-04: the CLI authorises a device against the account rather than a separate credential | capture: sha256:a79b91b8617bda7af0146c478a95da95880032126c631f15ac1355d9cee2acf5 | quote: `arga login` starts the device authorization flow and stores a device-scoped credential
  - [5] 2026-11-04: the free plan is open to an individual evaluation account, with no organisation gate stated | capture: sha256:f1e5ae965babaa72a5682e780d7b6ed11df6b7bc3b27605c4eb844c5a5ff85b9 | quote: The Free plan is intended for individual evaluation:
  - [4] 2026-11-04: the web app states the two account routes | capture: sha256:66033a654af3c8c226a0c9f4a3ba2fbf6f49072294e4257c9c2ae9d4ad0b12c1 | quote: Sign in with GitHub or create an account with email.
- sources:
  - [1] https://www.argalabs.com/
  - [2] https://docs.argalabs.com/cli-and-mcp.md
  - [3] https://www.argalabs.com/pricing
  - [4] https://docs.argalabs.com/web-app
  - [5] https://docs.argalabs.com/plans.md
