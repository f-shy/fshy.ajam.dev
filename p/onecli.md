# OneCLI

> onecli.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onecli/ | JSON https://fshy.ajam.dev/api/v1/entity/onecli.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OneCLI

- `compute/onecli` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.183Z (live) | stale on 2026-12-05
- url https://onecli.sh
- free tier: Free, $0: an isolated VM per employee, all hosted models, 3 seats, 3 agents, 500 integration calls a month and $5 of AI model credits; self-hosted deployment is not included | unit: mixed | metered on: request-count | read on: 2026-10-29 | source: [1] | note: read from the vendor pricing page
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published: the pricing table lists seats, agents, integration calls, credits and audit retention and no egress allowance or price | metered: no | source: [2]
- identity: email
- interface: cli
- limits:
  - volume-quota (binding): the Free plan includes 500 integration calls a month and $5 of AI model credits, for 3 seats and 3 agents [1]
- interface detail: CLI and SDK listed as an integration on the pricing table; no REST reference read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-29: a hosted Free plan at $0 (an isolated VM per employee, 500 integration calls a month, $5 of AI model credits) above Team, Scale and Enterprise; self-hosted deployment is Enterprise only. The site read on 2026-10-22 showed no plan
- self hosted: no
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an agent pauses and waits for approval; the page describes the pause as the product
  - free_tier_kind: none
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: 'Payments over $500 need a human. I've stopped here.' with 'approved by sam · logged by OneCLI' and 'Paused before updating Salesforce · waiting for approval', and 'Open source. Built for teams.' quoted; no plan or price appears
  - [2] 2026-10-29: the landing page offers self-hosting OneCLI or the hosted app | capture: sha256:781469c711e68e41432e5de5d41cb778c1ae6ab02695e9aa0ed9917b5d95d8f7 | quote: Or use the hosted app to get started.
  - [1] 2026-10-29: the Free plan is $0 with an isolated VM per employee, all hosted models, 3 seats, 3 agents, 500 integration calls a month and $5 of AI model credits; self-hosted deployment is not included on Free | capture: sha256:2129114cf81d0d8431959b4603be3060f83c44693115535998c8034714eb5cf7 | quote: | Integration calls | 500 /mo |
  - [1] 2026-11-03: the free plan is metered on integration calls and no egress row exists | capture: sha256:2129114cf81d0d8431959b4603be3060f83c44693115535998c8034714eb5cf7 | quote: | Integration calls | 500 /mo | Unlimited | Unlimited | Unlimited |
  - [1] 2026-11-03: the table lists a CLI and SDK feature | capture: sha256:2129114cf81d0d8431959b4603be3060f83c44693115535998c8034714eb5cf7 | quote: | OneCLI CLI & SDK | | | | |
- sources:
  - [1] https://onecli.sh/pricing
  - [2] https://onecli.sh
