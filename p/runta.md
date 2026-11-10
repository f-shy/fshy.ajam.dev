# Runta

> runta.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runta/ | JSON https://fshy.ajam.dev/api/v1/entity/runta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runta

- `compute/runta` | trial-only | evidence documented | binding per-object-cap | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:16.352Z (live) | stale on 2026-12-05
- url https://runta.com/pricing/
- free tier: $50 trial balance with no payment method, capped at 32 vCPU and 64 GiB of memory in aggregate across all runtimes; prepaid thereafter with a $5 minimum top-up | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: 'receive the $50 trial balance ... without adding a payment method', quoted from runta.com/pricing read 2026-10-22
- interface: cli, rest
- limits:
  - request-rate: $50 of trial balance, one time; $5 is the minimum top-up after it [1]
  - per-object-cap (binding): 32 vCPU and 64 GiB of memory in aggregate across all trial runtimes [1]
  - write-gated: higher resource limits need a payment method on the account [1]
- interface detail: runta CLI, Python and TypeScript SDKs, REST API at api.runta.com and a web dashboard; the CLI setup targets macOS and Linux
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing FAQ was read on 2026-10-22 and states the trial balance, the aggregate shape cap and the top-up floor. The aggregate cap is the number that decides how many runtimes fit
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 32
  - shape.ram: 64
  - shape.note: the aggregate cap across all runtimes on a trial account
  - session_cap.restart_required: no
  - session_cap.note: prepaid usage-based billing with no subscription; the page states no session clock
  - free_tier_kind: trial
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'No. You can create an account, receive the $50 trial balance, and start a runtime without adding a payment method.' and 'Free trial accounts share aggregate limits of 32 vCPU and 64 GiB of memory across their runtimes' and 'The minimum manual top-up is $5', quoted
  - [2] 2026-11-03: a CLI is installable | capture: sha256:4c2c1f529d22ae44a62ac00c2817c792bf0c9cf0d9215dbba410165f4f0f0d4a | quote: npm install -g @runta/runta-cli
  - [3] 2026-11-03: an HTTP API base URL is documented | capture: sha256:cdd323a7642f13bd54568345ec3bb57e953da65fb398530edf9bed78917eff22 | quote: export RUNTA_API_URL="https://api.runta.com"
  - [1] 2026-11-03: the pricing FAQ as captured lists trial limits and top-ups and states no egress allowance or egress price | capture: sha256:71ca8346ff134c1f157f1fe9e3950c9f81962137bb78108de3db4d7c13d9f61e | quote: Runtime usage is restricted until you add funds.
- sources:
  - [1] https://runta.com/pricing/
  - [2] https://runta.com/docs
  - [3] https://runta.com/docs/cloud-agents/quickstart/
