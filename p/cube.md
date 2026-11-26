# Cube Computer

> cube.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cube/ | JSON https://fshy.ajam.dev/api/v1/entity/cube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cube Computer

- `compute/cube` | trial-only | evidence documented | binding volume-quota | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.386Z (live) | stale on 2026-12-05
- url https://cube.computer/
- free tier: New accounts start with USD 25 of free credit, no card required, which covers about 2 months of the smallest computer (2 shared vCPUs, 4 GB RAM, 30 GB NVMe SSD) running all the time at USD 12 a month; credit is metered per second while a computer runs or is paused | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: The credit is given once per GitHub account; when it runs out the computer pauses and running processes stop, and files stay.
- per-object cap: not stated | source: [2]
- retention: files stay on a paused computer; memory and running processes do not | source: [2]
- egress: not published: the pricing page and the billing page state no egress allowance and no overage price; only per-vCPU running and paused rates are charged | metered: no | source: [2]
- identity: email | detail: Sign in with a Google, GitHub or Apple account; no card is required for the USD 25 starting credit, which is given once per GitHub account
- interface: ssh
- limits:
  - volume-quota (binding): USD 25 of starting credit, given once per GitHub account; when credit runs out the computer pauses and running processes stop, and files stay [3]
- binding note: the USD 25 starting credit is the wall: once it is spent the computer pauses and its running processes stop, and its files stay
- interface detail: SSH from any SSH client; the Cube Mac app, a browser and a phone app; no REST API or CLI is documented on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The cube.dev pricing page cited in the evidence covers a different product, an analytics platform with workbooks and dbt integration, not Cube Computer.
- evidence note: Documented on the vendor's pricing and billing pages: USD 25 of free credit with no card required, given once per GitHub account.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-28: Cube Computer gives new accounts $25 of free credit with no card, about 2 months of the smallest computer | capture: sha256:6fdc224688895de20ef65bfead46e8d0ba965f2d0e4eaf5cb0793d32e9efe9fa | quote: New accounts start with $25 of free credit, with no card required. That covers about 2 months of the smallest computer running all the time.
  - [1] 2026-10-28: the free offer is a USD credit spent on machine time, not a developer seat | capture: sha256:6fdc224688895de20ef65bfead46e8d0ba965f2d0e4eaf5cb0793d32e9efe9fa | quote: New accounts start with $25 of free credit, with no card required. That covers about 2 months of the smallest computer running all the time.
  - [1] 2026-10-28: credit is metered per second of running or paused time | capture: sha256:6fdc224688895de20ef65bfead46e8d0ba965f2d0e4eaf5cb0793d32e9efe9fa | quote: Charges are metered per second; monthly figures are estimates based on 730 hours, not subscriptions.
  - [1] 2026-10-28: the free credit is stated on cube.computer/pricing | capture: sha256:6fdc224688895de20ef65bfead46e8d0ba965f2d0e4eaf5cb0793d32e9efe9fa | quote: New accounts start with $25 of free credit, with no card required. That covers about 2 months of the smallest computer running all the time.
  - [3] 2026-10-28: the credit is given once per GitHub account and an exhausted balance pauses the computer while files stay | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: New accounts get $25 of credit when they first sign in, with no card required. It's given once per GitHub account. ... Your computer pauses and running processes stop. Your files stay.
  - [3] 2026-10-28: the limit is a one-time USD 25 credit; an empty balance pauses the computer and keeps its files | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: New accounts get $25 of credit when they first sign in, with no card required. It's given once per GitHub account. ... Your computer pauses and running processes stop. Your files stay.
  - [3] 2026-10-28: when the credit balance is spent the computer pauses and running processes stop | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: Your computer pauses and running processes stop. Your files stay.
  - [3] 2026-10-28: an empty credit balance pauses the computer and stops running processes; files stay | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: Your computer pauses and running processes stop. Your files stay.
  - [3] 2026-10-28: the free offer is a one-time starting credit given once per GitHub account | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: New accounts get $25 of credit when they first sign in, with no card required. It's given once per GitHub account.
  - [4] 2026-10-28: sign-in is through a Google, GitHub or Apple account | capture: sha256:6df60e2c7850ea3ef21b0871eae7a326d1c474408780fae31bdfd306b83dc945 | quote: Choose Continue with Google, Continue with GitHub or Continue with Apple, and finish in your browser.
  - [3] 2026-10-28: the starting credit needs no card and is given once per GitHub account | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: New accounts get $25 of credit when they first sign in, with no card required. It's given once per GitHub account.
  - [1] 2026-10-28: pausing keeps files but not memory or running processes | capture: sha256:6fdc224688895de20ef65bfead46e8d0ba965f2d0e4eaf5cb0793d32e9efe9fa | quote: Pausing retains files, but does not hibernate memory or running processes.
  - [5] 2026-10-28: cube.dev's plan table lists Workbooks, an analytics product feature, not cloud computers | capture: sha256:5105b8a0206386709e40aa7d6c1b50e876eace3c5ee335a99615a77cd2615a70 | quote: | Workbooks | Up to 5 | Unlimited | Unlimited | Unlimited |
  - [3] 2026-10-28: the billing page states the starting credit, the no-card term and the once-per-GitHub-account rule | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: New accounts get $25 of credit when they first sign in, with no card required. It's given once per GitHub account.
  - [4] 2026-10-28: an account is created by signing in with a Google, GitHub or Apple account; no phone or card step is named | capture: sha256:6df60e2c7850ea3ef21b0871eae7a326d1c474408780fae31bdfd306b83dc945 | quote: Choose Continue with Google, Continue with GitHub or Continue with Apple, and finish in your browser.
  - [3] 2026-11-03: the billing page lists per-vCPU running and paused rates and no egress line | capture: sha256:3de17b1f781148fa2c72044d9e8898e6d3808ac66b553fdb8c04d6fa3f4414a9 | quote: | Running | $6 | The computer is on and your agents keep working. |
  - [6] 2026-11-03: SSH access is documented | capture: sha256:eef809045039769ecf4670b583b912047b99110d10eb14fec6a64c0bc5975f08 | quote: The Codex and Claude apps and any SSH client on your Mac can work on your computer over SSH.
- sources:
  - [1] https://cube.computer/pricing/
  - [2] https://cube.computer/
  - [3] https://docs.cube.computer/docs/billing/
  - [4] https://docs.cube.computer/docs/get-started/
  - [5] https://cube.dev/pricing
  - [6] https://docs.cube.computer/docs/
