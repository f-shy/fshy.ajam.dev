# Unikraft Cloud

> unikraft.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unikraft/ | JSON https://fshy.ajam.dev/api/v1/entity/unikraft.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unikraft Cloud

- `compute/unikraft-cloud` | paid-only | evidence reported | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:43.457Z (live) | stale on 2026-12-10
- url https://unikraft.com/pricing
- free tier: no free tier stated: millisecond cold boots where idle infrastructure is not billed | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: Sign in with GitHub or Google; No card, phone number or identity document is stated on the sign-in page.
- interface: cli
- limits:
  - retention-clamped (binding): idle infrastructure is not billed; a millisecond cold boot is what makes that possible [1]
  - write-gated: the page refers to plans without pricing them in the extracted body [1]
- interface detail: The unikraft CLI deploys unikernel images and manages instances, with machine-readable JSON output; REST is not stated on the captured pages.
- tooling: the user installs and runs the unikraft CLI to log in and deploy instances; the hosted lane needs no hardware the user owns
- composes with: the hosted lane bills no idle infrastructure and uses millisecond cold boots, so an intermittent workload pays only for run time; a dedicated-hosted and an on-prem lane are also listed with no published rate
- reliability: no reliability event recorded
- notes: No free tier exists; the verdict is paid-only. Idle infrastructure is not billed and cold boots are milliseconds, so an intermittent workload pays only for the time it runs. The page lists Hosted, Dedicated Hosted and On-Prem lanes; the priced offer here is the hosted one. No rate, session cap, egress charge or free allowance is published.
- evidence note: the pricing page was read on 2026-10-22 and its extracted body carries the idle-billing promise and a plan reference, but no plan table or price, so the free-tier field keeps its earlier source
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: idle infrastructure is not billed, which makes the reap question moot; cold boots are milliseconds
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '## Never Pay for Idle Again' and '### You don't pay for idle infrastructure' with 'Millisecond cold boots = lower overhead' and 'Whether you're testing, scaling, or deploying enterprise workloads, we've got a plan that fits.', quoted
  - [1] 2026-11-25: the pricing page states that idle infrastructure is not billed, with no free tier or plan price printed | capture: sha256:15f4ec5fdb2269a6faf116dca445a6b1cf82e61ee71e23aa3a14a4a86314f361 | quote: You don't pay for idle infrastructure
  - [2] 2026-11-24: registration uses a GitHub or Google account; no card or phone is asked for on the sign-in page | capture: sha256:07d892d5ea287fe71f5e0adc55b094734fd3f5882a9550e28590b211500aa90d | quote: [Continue with GitHub](https://console.unikraft.com/auth/github/signin) [Continue with Google](https://console.unikraft.com/auth/google/signin)
  - [3] 2026-11-24: the vendor publishes a CLI that deploys instances, so the interface is no longer unknown | capture: sha256:d438ffcf1417e502d48be01e8215a18fe810d8289af034a3224e055cfddc2cd6 | quote: - Deploy Instantly - Run unikernel images as serverless instances with `unikraft run`
  - [3] 2026-11-24: the CLI supports machine-readable output | capture: sha256:d438ffcf1417e502d48be01e8215a18fe810d8289af034a3224e055cfddc2cd6 | quote: - Output Formats - Machine-readable JSON or human-friendly text output
  - [3] 2026-11-24: the vendor distributes an installable CLI | capture: sha256:d438ffcf1417e502d48be01e8215a18fe810d8289af034a3224e055cfddc2cd6 | quote: curl --proto '=https' --tlsv1.2 -fsSL https://unikraft.com/cli/install.sh | sh
  - [1] 2026-11-24: the hosted lane does not bill idle time | capture: sha256:15f4ec5fdb2269a6faf116dca445a6b1cf82e61ee71e23aa3a14a4a86314f361 | quote: ### You don't pay for idle infrastructure
  - [1] 2026-11-24: the hosted lane needs no infrastructure management by the user | capture: sha256:15f4ec5fdb2269a6faf116dca445a6b1cf82e61ee71e23aa3a14a4a86314f361 | quote: - No infrastructure management
  - [1] 2026-11-24: scale-to-zero remains on the pricing page | capture: sha256:15f4ec5fdb2269a6faf116dca445a6b1cf82e61ee71e23aa3a14a4a86314f361 | quote: ### Scale-to-zero saves real money
- sources:
  - [1] https://unikraft.com/pricing
  - [2] https://console.unikraft.cloud/auth/signin
  - [3] https://unikraft.com/docs/cli/kraft/overview
