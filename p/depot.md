# Depot

> depot.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/depot/ | JSON https://fshy.ajam.dev/api/v1/entity/depot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Depot (GitHub Actions runners)

- `compute/depot` | trial-only | evidence documented | binding retention-clamped | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T11:38:12.988Z (live) | stale on 2026-12-25
- url https://depot.dev/pricing
- free tier: No free tier: a 7-day trial, then the Developer plan is USD 20 a month and includes 2,000 GitHub Actions minutes, 2,000 sandbox minutes, 500 container build minutes and 25 GB of cache and registry storage each month; additional GitHub Actions minutes are USD 0.006 a minute for the base 2 vCPU Linux runner. | unit: minutes | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: snapshots are limited to 25 GiB of file data | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: email: the terms require a valid email address at signup; no phone number or identity document is named
- interface: rest, cli
- limits:
  - request-rate: 2,000 GitHub Actions minutes a month on the USD 20 Developer plan, then USD 0.006 a minute for the base 2 vCPU Linux runner [1]
  - per-object-cap: 25 GB of cache and registry storage on the Developer plan, then USD 0.20 a GB-month [1]
  - retention-clamped (binding): the free window is a 7-day trial; the monthly allowance needs the USD 20 plan [1]
- limits note: the Startup plan at USD 200 a month raises the included GitHub Actions minutes to 20,000 and cache to 250 GB; the Business plan is custom and can run in the customer AWS account
- interface detail: Node.js @depot/sandbox SDK wrapping the depot.sandbox.v1 API, with a depot CLI; web console at depot.dev
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The 2,000 sandbox minutes and 2,000 GitHub Actions minutes are an allowance included in the USD 20 a month Developer plan, not a grant inside the 7-day trial; the trial is the only free window. The overage rate is USD 0.006 a minute for the base 2 vCPU Linux runner, and cache beyond 25 GB is USD 0.20 a GB-month.
- evidence note: The plan grid, the included allowances and the overage rates are read from the vendor own pricing page. Raise by running a job in the trial and reading the invoice line for a minute beyond the included block.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a 7-day clock on the trial, not on a job
  - free_tier_kind: trial
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 25
  - ps.price: included in the trial, then metered
  - ps.durability: cache and registry
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the trial term
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start for free, scale to any size, and pay per second for what you use' with an included block of '2,000 sandbox minutes', '2,000 GitHub Actions minutes', '500 container build minutes' and '25 GB cache and registry storage', under a 'START A 7-DAY TRIAL' button, quoted
  - [1] 2026-11-10: the Developer plan includes 2,000 GitHub Actions minutes a month | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: 2,000 GitHub Actions minutes
  - [1] 2026-11-10: additional GitHub Actions minutes are USD 0.006 a minute | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: $0.006 / minute
  - [1] 2026-11-10: the Startup plan includes 20,000 GitHub Actions minutes | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: 20,000 GitHub Actions minutes
  - [1] 2026-11-10: a 7-day trial is the only free window | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: START A 7-DAY TRIAL
  - [1] 2026-11-24: the Developer plan includes 2,000 GitHub Actions minutes | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: - 2,000 GitHub Actions minutes
  - [1] 2026-11-24: the free window is a 7-day trial | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: [START A 7-DAY TRIAL](https://depot.dev/start)
  - [2] 2026-11-24: Depot sandboxes are driven by a Node.js SDK over an API | capture: sha256:3ac98ec0fc33b374baf316db711eb9429d9650813b73591a089bc4ac68a0f533 | quote: The [`@depot/sandbox`](https://www.npmjs.com/package/@depot/sandbox) package is the Node.js SDK for Depot sandboxes. It wraps the `depot.sandbox.v1` API with ergonomic classes for creating sandboxes, running commands, streaming command output, and working with a sandbox's file system through a `node:fs/promises`-shaped interface.
  - [2] 2026-11-24: a REST/SDK client drives the sandbox; a depot CLI is named in the same page | capture: sha256:3ac98ec0fc33b374baf316db711eb9429d9650813b73591a089bc4ac68a0f533 | quote: Set `DEPOT_TOKEN` in your environment, then create a client and use it to create a sandbox, run a command, read its output, write a file, and stop the sandbox:
  - [3] 2026-11-24: the signup gate is an email address | capture: sha256:6d53bded7fd13d3787622d8efcf6196f31ad1bad636b2740680c61141cc96486 | quote: You must provide a valid email address in order to complete the signup process.
  - [3] 2026-11-24: an email address is required to sign up | capture: sha256:6d53bded7fd13d3787622d8efcf6196f31ad1bad636b2740680c61141cc96486 | quote: You must provide a valid email address in order to complete the signup process.
  - [2] 2026-11-24: snapshots are capped at 25 GiB of file data | capture: sha256:3ac98ec0fc33b374baf316db711eb9429d9650813b73591a089bc4ac68a0f533 | quote: Snapshots preserve files, not running processes or memory, and are limited to 25 GiB of file data.
  - [2] 2026-11-24: sandbox compute is billed per vCPU-second | capture: sha256:3ac98ec0fc33b374baf316db711eb9429d9650813b73591a089bc4ac68a0f533 | quote: Sandboxes are billed per vCPU-second at the Depot CI compute rate.
  - [1] 2026-11-24: sandbox compute is $0.00005 per vCPU-second beyond the included minutes | capture: sha256:13ef3b8f597e6b5cb32d37833b14bc15df6f2405009ddcf08d06399d67d4e560 | quote: | Sandbox computeDepot CIDepot SandboxesDepot Managed Agents | 2,000 minutesShared by all three | 20,000 minutesShared by all three | $0.00005 / second / vCPUIncluded minutes are measured at 2 vCPUs |
- sources:
  - [1] https://depot.dev/pricing
  - [2] https://depot.dev/docs/api/sandbox-sdk-reference
  - [3] https://depot.dev/terms-of-service
