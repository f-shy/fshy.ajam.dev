# OpenPond Cloud Sandboxes

> openpond.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openpond/ | JSON https://fshy.ajam.dev/api/v1/entity/openpond.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenPond Cloud Sandboxes

- `compute/openpond` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-24T13:20:59.952Z (live) | stale on 2026-12-25
- url https://openpond.ai/pricing
- free tier: no free tier stated: the pricing page is headed Pay as you go and lists paid training and inference rates; sandbox compute is configured by contact | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page lists training and inference rates and names no egress allowance or price | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): NVIDIA A100 training at USD 3.99 an hour, H100 at USD 6.49 an hour and B200 at USD 10.99 an hour [1]
  - write-gated: sandbox compute and storage configuration is stated by contact, with no published rate [1]
- interface detail: CLI (`npx openpond@latest`), desktop app, web, TUI, Slack and Microsoft Teams, plus an account-or-API-key-authenticated public API
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-11-24 and no longer states a free tier, a monthly credit tier or any concurrent-sandbox allowance; the current page lists paid training and inference rates and refers sandbox configuration to contact
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session clock or idle reap published; sandbox configuration is by contact
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Start free. Upgrade for more projects, team access, and concurrent cloud sandboxes. Add credits whenever you need more hosted usage.' with 'Limited monthly usage included' on Free and '$10 in monthly hosted usage' plus 'Up to 10 concurrent cloud sandboxes' on the next tier, quoted
  - [1] 2026-11-03: the sandbox meter is compute time; no egress meter is listed | capture: sha256:a7a6893d401369a60f1efe27f1ff001ffec9fe277368749e7f87c9eefa50f002 | quote: Sandbox compute
  - [2] 2026-11-03: a CLI exists | capture: sha256:99d464ae11fe3790007884d54d1b778ec7cd0f989c1cf3eaa7382afa51a73f89 | quote: - [OpenPond CLI](https://openpond.ai/products/cli): Run `npx openpond@latest` to start from the terminal.
  - [1] 2026-11-18:  | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Contact us about the compute and storage configuration for your workload.
  - [1] 2026-11-24: the pricing page no longer states a Free tier or a $10 sandbox tier | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Run agents, code, and tools in isolated cloud workspaces. Contact us about the compute and storage configuration for your workload.
  - [1] 2026-11-24: the current page states a pay-as-you-go model with no Free tier row | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Pay as you go
  - [1] 2026-11-24: no free allowance is stated on the current pricing page | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Pay as you go
  - [1] 2026-11-24: the page describes usage-based paid compute with no free allowance | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Clear compute rates for training and usage-based serverless inference. Add credits when you need them and review your estimate before you start.
  - [1] 2026-11-24: the A100 training rate is USD 0.06650 a minute and USD 3.99 an hour | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: | NVIDIA A100 | 80 GB | $0.06650 | $3.99 |
  - [1] 2026-11-24: sandbox capacity is quoted on contact | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Contact us about the compute and storage configuration for your workload.
  - [1] 2026-11-24: the pricing page lists compute and model categories with no egress meter | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Hosted model APIs
  - [2] 2026-11-24: a public API with sandbox endpoints is documented | capture: sha256:d2c181e1a6f29dd03b833f799ab40f63a2581932fd212faba420824d8417df45 | quote: [OpenPond public API](https://api.openpond.ai): API-key and account-authenticated endpoints for OpenPond products, sandboxes, and OpChat.
  - [1] 2026-11-24: the pricing page still has a Sandboxes section but with no free tier | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: ## Sandboxes
  - [1] 2026-11-24: no free allowance is stated | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Pay as you go
  - [1] 2026-11-24: the current pricing page offers paid compute with no free tier stated | capture: sha256:4d26f1937a73044aaa2183171e27faf8340d63c5a27fbfda952f2dbe0d7df882 | quote: Clear compute rates for training and usage-based serverless inference. Add credits when you need them and review your estimate before you start.
- sources:
  - [1] https://openpond.ai/pricing
  - [2] https://openpond.ai
