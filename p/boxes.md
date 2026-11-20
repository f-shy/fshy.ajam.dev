# boxes.dev

> boxes.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxes/ | JSON https://fshy.ajam.dev/api/v1/entity/boxes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## boxes.dev

- `compute/boxes-dev` | trial-only | evidence documented | binding volume-quota | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.384Z (live) | stale on 2026-12-05
- url https://boxes.dev/
- free tier: Trial plan, $0: 20 hours of compute included per user (box-hours; one box-hour is one default 4 vCPU / 8 GB RAM / 100 GB disk devbox awake for one hour), with up to 2 awake devboxes plus the Template box and up to 2 projects; billed by the second, and sleeping devboxes are free | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: 'Sleeping devboxes are free'; 'Trial $0/free'
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published: the pricing page, the plans-and-box-hours help page and the billing-and-usage help page state no egress allowance and no overage price; only extra box-hours are priced | metered: no | source: [2]
- identity: email | detail: Sign in with Google OAuth or Sign in with Apple; a Google account whose email address Google does not manage may be asked for a six-digit email code to verify that address; some teams need to add a payment method before starting the trial, and a trial started without a card is not interrupted by a later payment-method requirement
- interface: ssh, rest, cli
- limits:
  - retention-clamped: a devbox sleeps after about five minutes without activity; nothing runs while it sleeps, and its files and memory are kept [1]
  - volume-quota (binding): Trial: 20 box-hours per user; up to 2 awake devboxes plus the Template box and up to 2 projects [3]
- binding note: the Trial allowance of 20 box-hours per user is the constraint: once the trial ends or the allowance is used, machines cannot be started or woken without a paid seat or a billing update
- interface detail: SSH and IDE-over-SSH; an HTTP POST API trigger for automations (Bearer secret); the dvb command-line client; the desktop, mobile and web apps
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Documented on the vendor's plans help page: the Trial allowance of 20 box-hours per user, and a paid seat or a billing update once the trial ends or the allowance is used.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: 'Idle boxes sleep automatically. Sleeping boxes are free. Billed by the second. 4 vCPU / 8 GB RAM / 100 GB disk standard'; a Trial tier at $0
  - [2] 2026-10-28: the Trial plan is $0 with 20 hours of compute included on 4 vCPU / 8 GB RAM / 100 GB disk machines, billed by the second | capture: sha256:84fdeee6a991e32f5b34f340d85e3fd17069bdfa937d38ab1ca69ed7ba149361 | quote: Trial $0/ free 20 hours of compute included ... Billed by the second. 4 vCPU / 8 GB RAM / 100 GB disk standard.
  - [3] 2026-10-28: the Trial plan is free with 20 box-hours per user, 2 awake devboxes plus the Template box and up to 2 projects | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: | Trial | Free | 20 box-hours per user | 2, plus the Template box | Up to 2 |
  - [4] 2026-10-28: a devbox sleeps after about five minutes idle, nothing runs while asleep, and files and memory are kept | capture: sha256:1cd34d52827bae4154bcb4a694697a00063c9d29f574b7f1b3dfdb43d50236fc | quote: A Template box or devbox normally sleeps after about five minutes without activity. ... Nothing runs while it sleeps ... Sleeping keeps the machine's files and memory
  - [3] 2026-10-28: the Trial plan allows 20 box-hours per user, 2 awake devboxes plus the Template box and up to 2 projects | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: | Trial | Free | 20 box-hours per user | 2, plus the Template box | Up to 2 |
  - [3] 2026-10-28: the free allowance is a fixed 20 box-hours per user; sleeping machines use none | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: | Trial | Free | 20 box-hours per user | 2, plus the Template box | Up to 2 |
  - [3] 2026-10-28: after the trial ends or its allowance is used, starting or waking machines needs a paid seat or a billing update | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: Once your trial ends or you use its allowance, a team admin needs to assign you a paid seat or update billing before you can start or wake machines again.
  - [5] 2026-10-28: the product reports a trial-ended or paid-seat-required block, resolved by a team admin assigning a paid seat or updating the plan | capture: sha256:9462cb3397158ab00b9cc00a7a23f4e06365d9f40b5650f5bc82b346618047dc | quote: | Trial ended or paid seat required | Ask a team admin to assign a paid seat or update the plan. |
  - [3] 2026-10-28: the free plan is a per-user trial that ends, after which a paid seat or billing update is needed to run machines | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: The trial is per user and starts when you first use a machine. ... Once your trial ends or you use its allowance, a team admin needs to assign you a paid seat or update billing before you can start or wake machines again.
  - [6] 2026-10-28: sign-up with a Google account can require a six-digit email code when Google does not manage the address | capture: sha256:6bf31abdf11179c8f1101311235420723f2691866bf55b8eadcb8790ef48b9f7 | quote: When you sign up with a Google account whose email address Google does not manage, boxes.dev may ask for a six-digit email code to verify that address.
  - [7] 2026-10-28: sign-in is through Google OAuth or Sign in with Apple, which supply a name, email address and profile photo | capture: sha256:e149e635a7c66b297563732b4e38d3fe3834222ff2e4d820ffec22f2776591b8 | quote: When you sign in via Google OAuth or Sign in with Apple, we receive basic profile information (such as name, email address, and profile photo, depending on what you authorize).
  - [3] 2026-10-28: a payment method is required before starting for some teams; a trial started without a card is not interrupted by a later requirement | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: Some teams need to add a payment method before starting; Billing will show whether one is required. If you started without a card, a later payment-method requirement will not interrupt your remaining trial.
  - [3] 2026-10-28: the plans help page states the trial end condition and the paid-seat or billing-update remedy | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: Once your trial ends or you use its allowance, a team admin needs to assign you a paid seat or update billing before you can start or wake machines again.
  - [3] 2026-10-28: the free allowance is counted in box-hours (awake time) per user; the unit and metering are unchanged | capture: sha256:02fe6e2bf5e71d1611068f016094a00b685f46a2ffe26115caa362f57bef475a | quote: | Trial | Free | 20 box-hours per user | 2, plus the Template box | Up to 2 |
  - [7] 2026-10-28: an account is created by signing in with a Google or Apple account that supplies an email address | capture: sha256:e149e635a7c66b297563732b4e38d3fe3834222ff2e4d820ffec22f2776591b8 | quote: When you sign in via Google OAuth or Sign in with Apple, we receive basic profile information (such as name, email address, and profile photo, depending on what you authorize).
  - [1] 2026-11-03: the pricing page prices extra box-hours only; no egress allowance or overage price appears | capture: sha256:92d8b29518750b0f628c1b4684df66e60f9d1986a20ba21fbc6cb5952406c284 | quote: Extra hours anytime at $0.60/hr
  - [1] 2026-11-03: SSH access is supported | capture: sha256:92d8b29518750b0f628c1b4684df66e60f9d1986a20ba21fbc6cb5952406c284 | quote: boxes. dev supports SSH and IDE-over-SSH (VS Code, JetBrains)
  - [8] 2026-11-03: an HTTP API exists to start agent tasks | capture: sha256:b6459c41714b5965225dbcdfd96784e6105f4b418fc450e183dde56a3282eebb | quote: An API automation lets a script or another service start an agent task by sending an HTTP request.
  - [9] 2026-11-03: a CLI exists | capture: sha256:1a528ceca34d53b7bf548441484f8906cc080c2133cca635e6d68ca7bbde6549 | quote: The `dvb` CLI lets you work on your cloud devboxes from a terminal on your computer.
- sources:
  - [1] https://boxes.dev/pricing
  - [2] https://boxes.dev/
  - [3] https://boxes.dev/help/plans-and-box-hours
  - [4] https://boxes.dev/help/sleep-wake-recover
  - [5] https://boxes.dev/help/billing-and-usage
  - [6] https://boxes.dev/help/data-and-credentials
  - [7] https://boxes.dev/privacy
  - [8] https://boxes.dev/help/automation-api
  - [9] https://boxes.dev/help/use-cli
