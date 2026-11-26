# Celesto Cloud

> celesto.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/celesto/ | JSON https://fshy.ajam.dev/api/v1/entity/celesto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Celesto Cloud

- `compute/celesto` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T11:38:11.669Z (live) | stale on 2026-12-25
- url https://celesto.ai/pricing
- free tier: a one-time $5 Micro runtime credit, no card required, expiring 30 days after activation; the trial allows two retained Micro sandboxes, including stopped ones | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: stopped root disks are retained free for 30 days | days: 30 | source: [1] | note: Root disks survive a stop for 30 days; durability after deletion is not documented.
- egress: https://celesto.ai/pricing prices running time and root disk only: 'Running time only. Tax and any card issuer conversion fee are excluded.' No egress allowance or overage price is published. | metered: no | source: [1]
- identity: email | detail: The sign-up form asks first name, last name, email address and password, with AgentID, GitHub or Google as alternatives; no phone field and no card field.
- interface: cli, ssh
- limits:
  - request-rate: $5 of runtime credit, one time, on the Micro size [1]
  - retention-clamped (binding): the credit is valid for 30 days; a top-up does not end the trial, it just adds a balance [1]
- interface detail: the celesto CLI with `computer ssh` for an interactive terminal, a Python SDK and a TypeScript SDK; no REST reference was read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the trial credit, its 30-day life and the size ladder. It is a trial, so the verdict stays trial-only and the clock is now recorded
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 2
  - shape.disk: 20
  - shape.note: Micro, the default; the ladder runs to XL at 8 vCPU, 32 GB and 100 GB. $5 buys 333 hours of Micro
  - session_cap.restart_required: no
  - session_cap.note: no session clock published; the 30-day clock is on the credit, not the machine
  - free_tier_kind: trial
  - burst_x: 1.0
  - ps.gib: 20
  - ps.price: fixed root disk included in the size
  - ps.durability: root disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the machine exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Usage pricing is live. Try Micro with a one-time $5 runtime credit for 30 days, no card required.' and 'Sign up, then start the trial or add at least $2.01 in Settings -> Billing. A top-up does not end an active trial.' and the size table from Micro at $0.015 an hour to XL at $0.160 an hour, quoted
  - [1] 2026-11-03: the estimator prices running time only; no egress allowance or overage price is published | capture: sha256:eba826b8108319bfd4dc5b911bbf3e00d9757d145627433b910e1327bb46f3ce | quote: Running time only. Tax and any card issuer conversion fee are excluded.
  - [2] 2026-11-03: the celesto CLI opens an SSH session to a computer | capture: sha256:dbb5c022cb94640f5d9ab2ce02efa917b8cd506273a82d0f2f8d7f1433f291de | quote: celesto computer ssh einstein
  - [1] 2026-11-18:  | capture: sha256:1f7fd87ea1b65d7e15e18c3b164c313d039a75e599c1aa4d5796ed61b1dff355 | quote: Unused trial credit expires 30 days after activation.
  - [1] 2026-11-24: the trial credit amount, its 30-day expiry and that no card is required | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: One-time $5 Micro runtime credit. Expires 30 days after activation. No card required.
  - [1] 2026-11-24: the trial credit is unchanged in amount, card gate and 30-day expiry | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: One-time $5 Micro runtime credit. Expires 30 days after activation. No card required.
  - [1] 2026-11-24: the price covers running time only, with no separate egress line | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Running time only. Tax and any card issuer conversion fee are excluded.
  - [1] 2026-11-24: no egress allowance or overage price is published | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Running time only. Tax and any card issuer conversion fee are excluded.
  - [1] 2026-11-24: the page publishes a 30-day retention for stopped root disks | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Stopped root disks are retained free for 30 days.
  - [1] 2026-11-24: the retention period is 30 days | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Stopped root disks are retained free for 30 days.
  - [1] 2026-11-24: root disks are retained across a stop for 30 days | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Stopped root disks are retained free for 30 days.
  - [1] 2026-11-24: the page states the retention period for stopped root disks | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: Stopped root disks are retained free for 30 days.
  - [3] 2026-11-24: the sign-up form asks for a name, email address and password | capture: sha256:be4e44728d6f262ea6487f3b0e5801feebb32479146df2cb7fc3617ce77649a9 | quote: First name Last name Email address Password
  - [3] 2026-11-24: an email address and password create the account; no phone or card is asked for | capture: sha256:be4e44728d6f262ea6487f3b0e5801feebb32479146df2cb7fc3617ce77649a9 | quote: First name Last name Email address Password
  - [3] 2026-11-24: the registration gate is a name, email address and password | capture: sha256:be4e44728d6f262ea6487f3b0e5801feebb32479146df2cb7fc3617ce77649a9 | quote: First name Last name Email address Password
  - [2] 2026-11-24: the CLI opens an SSH terminal on a cloud computer | capture: sha256:048ac36dd5860c2139d3cdb151de6f107adf220a887bca80d32b934c04fcc7d9 | quote: celesto computer ssh ID --cloud
  - [2] 2026-11-24: the documented command opens an interactive terminal | capture: sha256:048ac36dd5860c2139d3cdb151de6f107adf220a887bca80d32b934c04fcc7d9 | quote: | `celesto computer ssh ID --cloud` | Open an interactive terminal. |
  - [2] 2026-11-24: the CLI provides an SSH terminal | capture: sha256:048ac36dd5860c2139d3cdb151de6f107adf220a887bca80d32b934c04fcc7d9 | quote: | `celesto computer ssh ID --cloud` | Open an interactive terminal. |
  - [1] 2026-11-24: the credit amount and its 30-day expiry bound the trial | capture: sha256:845f18db3b4ca5d09a025ffad44942bf79cd5bd479218cde984f190b959f2918 | quote: One-time $5 Micro runtime credit. Expires 30 days after activation. No card required.
- sources:
  - [1] https://celesto.ai/pricing
  - [2] https://celesto.ai/docs/cloud/cli.md
  - [3] https://celesto.ai/sign-up
